#!/usr/bin/env python
# -*- coding: utf-8 -*
#
# Program for converting LibrePlan Twiki pages to GitHub Wiki+markdown

# Because some content comes from separate MySQL table we use the webpage as root
# and not the Twiki/data files
# Call url https://wiki.libreplan.org/bin/view/LibrePlan/WebTopicList

import os,sys, re
import requests
from bs4 import BeautifulSoup
from pprint import pprint,pformat
import pypandoc
import codecs
import copy

# URL that lists all pages
#url = "http://wiki.libreplan.org/bin/view/LibrePlan/WebTopicList"
url = "http://wiki.libreplan-enterprise.com/bin/view/LibrePlan/WebTopicList"
# Root directory of old Twiki page
root_url="http://wiki.libreplan-enterprise.com/"
# Dir to start exporting to
export_root_dir="./libreplan.wiki/twiki"
# All urls we are interested in start with:
starts_with="/twiki/bin/view"
# new url location
new_url_root="https://github.com/LibrePlan/libreplan/wiki/twiki"
bugcounter=0
copyright_notice="<p>\n\nCopyright (c) by the contributing authors. All material on this collaboration platform is the property of the contributing authors.</body></html>"

print("Pandoc version: "+pypandoc.get_pandoc_version())
#print(pypandoc.get_pandoc_path())
#print(pypandoc.get_pandoc_formats())

#
r  = requests.get(url)
data = r.text
data2=copy.copy(data)

# Copyright © by the contributing authors. All material on this collaboration platform is the property of the contributing authors.
mysearch = "<!-- /patternContent-->"
if mysearch in data2:
    data2 = data2[0:data2.index(mysearch)]
#  </body> </html>
data2 = data2 + copyright_notice

# let's try to shorten urls:
# data2 = re.sub(r'href="(.*?)/(.*?)/(.*?)(\?(.*) )"',
#                r'href=\"\2/\3\"',
#                data2)
# removing all http://wiki.libreplan-enterprise.com and relocate to the testrepo

# This url works on github: [ItEr61S03RFPerformanceCompanyView](ItEr61S03RFPerformanceCompanyView)
data2 = data2.replace("http://wiki.libreplan-enterprise.com","")
if "/twiki/kwoot/" in data2:
    print 1
    sys.exit(2)
# intermediarie change
data2 = data2.replace("/twiki/bin/edit", "/twiki/bin/view")
# /twiki/bin/view/
data2 = data2.replace(r"/twiki/bin/view/LibrePlan/", r"")
if "/twiki/kwoot/" in data2:
    print 2
    sys.exit(2)



soup = BeautifulSoup(data, "html.parser")
print type(soup)
#soup2=copy.copy(soup)
soup2=BeautifulSoup(data2, "html.parser")

# remove tages and do not keep children
invalid_tags = ["style","script","head"]
for tag in invalid_tags:
    for match in soup.findAll(tag):
        match.clear()
        # print "intermediate"+str(len(pformat(soup2))) + ":" + pformat(soup2)
print str(len(pformat(soup2))) + ":" + pformat(soup2)

# remove tages but keep children
invalid_tags = ['div','span',"base"]
for tag in invalid_tags:
    for match in soup2.findAll(tag):
        match.replaceWithChildren()
        # print "intermediate"+str(len(pformat(soup2))) + ":" + pformat(soup2)
print str(len(pformat(soup2))) + ":" + pformat(soup2)


basefilename="libreplan.wiki/twiki/LibrePlan/All_Twiki_Pages"
filename=basefilename+".pre-pandoc-concersion"
print "Filename: " + filename
# Save in libreplan.wiki/twiki
text_file = codecs.open(filename, "w", "utf-8")
text_file.write(soup2.prettify())
text_file.close()

# Convert page to markdown_github syntax

#filters = ['pandoc-citeproc']
#pdoc_args = ['--mathjax',
#             '--smart']
filters=[]
pdoc_args=["--wrap=none"]

# extensions: simple_tables, multiline_tables, grid_tables, pipe_tables
# disable extension: raw_html, native_spans
#extensions = "-raw_html-native_spans+pipe_tables"
extensions = "-native_spans"
# pipe_tables geeft hele brede kolommen. Next!
# simple_tables idem

print "Start pandoc conversion..."
print str(len(pformat(soup2))) + ":" + pformat(soup2)
my_output = pypandoc.convert_text(soup2,
                                  'markdown_github'+extensions,
                                  format='html',
                                  extra_args=pdoc_args,
                                  filters=filters)
print "*" * 80
print str(len(pformat(my_output))) + ":" + pformat(my_output)
pprint(my_output)
print "*" * 80

# After pandoc conversion save intermediate file
filename=basefilename + ".raw-md"
print "Filename: " + filename
# Save in libreplan.wiki/twiki
text_file = codecs.open(filename, "w", "utf-8")
text_file.write(my_output)
text_file.close()

# File handling part
filename=basefilename + ".md"
print "Filename: " + filename
# Save in libreplan.wiki/twiki
text_file = codecs.open(filename, "w", "utf-8")
text_file.write(my_output)
text_file.close()
#output = pypandoc.convert_text(soup2, "markdown_github", format='html', outputfile=filename)
# assert output == ""


#sys.exit(1)

counter=0
for link in soup.find_all('a'):
    counter+=1
    print "#" * 120
    link=link.get('href')
    #pprint(link)

    #print(link.get('href'))
    # trial: only convert pages from "LibrePlan" space
    #if link is not None and link.startswith(starts_with) and "/LibrePlan/" in link:
    if link is not None and "/LibrePlan/" in link:
        print link,
        link_parts=link.split("/")
        print ", in parts: ",pformat(link_parts),
        page_to_convert_url= root_url + link  #  _parts[-1] # get last part after splitting to get page name
        print "page to request: ",page_to_convert_url

        # Directory handling part
        # Check for directory
        twiki_space=link_parts[-2]
        if twiki_space=="LibrePlan":
            destination_directory = export_root_dir + "/" + twiki_space
            print "Directory: " + destination_directory,
            if os.path.isdir(destination_directory):
                print "Found..."
            else:
                print "Not found! Creating!"
                os.makedirs(destination_directory)


            # todo get history of page and build a loop around it
            filename = destination_directory + "/" + link_parts[-1] + ".original-html"
            print "Filename: " + filename

            if os.path.exists(filename):
                # Load file
                text_file = codecs.open(filename, "r", "utf-8")
                data2=text_file.read()
                text_file.close()
                #file = open(“testfile.text”, “r”)
                #print file.read()
            else:
                # Actually retrieve wiki page
                try:
                    r2 = requests.get(page_to_convert_url, allow_redirects=False) # to prevent redirection to https
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                data2=r2.text
                #print data2
                #sys.exit(1)

                # save original html for checking purposes
                # File handling part
                # Save in libreplan.wiki/twiki
                text_file = codecs.open(filename, "w", "utf-8")
                text_file.write(data2)
                text_file.close()



            # Try to remove everything after <!-- /patternContent--> being the footer of the page.
            # Remove everything after start of footer
            # if 'span id=\"topic-actions\"' in data2:
            #    data2=data2[0:data2.index('span id=\"topic-actions\"')]
            # if 'http://twiki.org/?ref=twiki.org/topmenuskin' in data2:
            #    data2=data2[0:data2.index('http://twiki.org/?ref=twiki.org/topmenuskin')]
            # Copyright © by the contributing authors. All material on this collaboration platform is the property of the contributing authors.
            mysearch = "<!-- /patternContent-->"
            if mysearch in data2:
                data2 = data2[0:data2.index(mysearch)]
            #  </body> </html>
            data2 = data2 + copyright_notice

            # let's try to shorten urls:
            # data2 = re.sub(r'href="(.*?)/(.*?)/(.*?)(\?(.*) )"',
            #                r'href=\"\2/\3\"',
            #                data2)
            # removing all http://wiki.libreplan-enterprise.com and relocate to the testrepo

            # This url works on github: [ItEr61S03RFPerformanceCompanyView](ItEr61S03RFPerformanceCompanyView)
            data2 = data2.replace("http://wiki.libreplan-enterprise.com","")
            if "/twiki/kwoot/" in data2:
                print 1
                sys.exit(2)
            # intermediarie change
            data2 = data2.replace("/twiki/bin/edit", "/twiki/bin/view")
            # /twiki/bin/view/
            data2 = data2.replace(r"/twiki/bin/view/LibrePlan/", r"")
            if "/twiki/kwoot/" in data2:
                print 2
                sys.exit(2)

            # Fix strange Twiki bug:  <th>&nbsp;</td>
            if "<th>&nbsp;</td>" in data2:
                data2 = data2.replace("<th>&nbsp;</td>", "<th>&nbsp;</th>")
                bugcounter+=1

            #
            # data2 = data2.replace("/bin/edit", "/kwoot/testwiki/wiki/twiki")
            # data2 = data2.replace(r"/twiki/bin/view/Main/", r"")
            # if "/twiki/kwoot/" in data2:
            #     print 3
            #     sys.exit(2)

            # adding images: [[https://github.com/username/repository/blob/master/img/octocat.png|alt=octocat]]

            # Change page using Beautifulsoup
            soup2=BeautifulSoup(data2, "html.parser")
            print "*" * 80
            print str(len(pformat(soup2)))+":"+pformat(soup2)

            # save original html for checking purposes
            # File handling part
            # filename = destination_directory + "/" + link_parts[-1] + ".pre-html-processing"
            # print "Filename: " + filename
            # # Save in libreplan.wiki/twiki
            # text_file = codecs.open(filename, "w", "utf-8")
            # text_file.write(soup2.prettify())
            # text_file.close()

            # Remove some attributes
            REMOVE_ATTRIBUTES = [
                'lang', 'language', 'onmouseover', 'onmouseout', 'script', 'style', 'font',
                'dir', 'face', 'size', 'color', 'style', 'class', 'width', 'height', 'hspace',
                'border', 'valign', 'align', 'background', 'bgcolor', 'text', 'link', 'vlink',
                'alink', 'cellpadding', 'cellspacing']
            for tag in soup2.recursiveChildGenerator():
                if hasattr(tag, 'attrs'):
                    tag.attrs = {key:value for key,value in tag.attrs.iteritems()
                                 if key not in REMOVE_ATTRIBUTES}
            print str(len(pformat(soup2))) + ":" + pformat(soup2)

            # for s in soup2.find_all("span"):
            #     print "==>"
            #     pprint(s)
            #     #s.decompose()
            #     s.replace_with('')

            # remove tages and do not keep children
            invalid_tags = ["style","script","head"]
            for tag in invalid_tags:
                for match in soup2.findAll(tag):
                    match.clear()
                    # print "intermediate"+str(len(pformat(soup2))) + ":" + pformat(soup2)
            print str(len(pformat(soup2))) + ":" + pformat(soup2)

            # remove tages but keep children
            invalid_tags = ['div','span',"base"]
            for tag in invalid_tags:
                for match in soup2.findAll(tag):
                    match.replaceWithChildren()
                    # print "intermediate"+str(len(pformat(soup2))) + ":" + pformat(soup2)
            print str(len(pformat(soup2))) + ":" + pformat(soup2)

            # Remove stuff on top of page: <a name="PageTop">  </a>
            # for match in soup2.find_all("a",{"name":"PageTop"}):
            #     match.decompose()
            #
            # for match in soup2.find_all("form",{"name":"tagmeshow"}):
            #     match.decompose()
            #
            # # <a href="/bin/view/TWiki/TagMeViewAllTags">
            # for match in soup2.find_all("a",{"href":"/bin/view/TWiki/TagMeViewAllTags"}):
            #     match.decompose()
            #
            # for match in soup2.find_all("span"):
            #     pprint(match)
            #     match.decompose()


            # Change urls
            # tmp disable
            # from_root="http://wiki.libreplan-enterprise.com/bin/view/"
            # for a in soup2.find_all("a","href"):
            #     #print a
            #     # to point to md files
            #     #if from_root in a:
            #     #if a.get("href") is not None:
            #     a["href"] = a["href"]+".md"
            #     # remove create new tag url
            #     if "create new tag" in a:
            #         a.decompose()
            #     # remove view all tags url
            #     if "view all tags" in a:
            #         a.decompose()

            # Change img src="http://wiki.libreplan-enterprise.com/twiki/pub/TWiki/SmiliesPlugin/smile.gif
            #                 http://wiki.libreplan-enterprise.com/pub/

            # for d in soup2.find_all("div","patternBottomBar"):
            #     pprint(d)
            #     if d["id"]=="patternBottomBar":
            #         d.decompose()

            # no longer needed
            # span id="topic-actions
            # for s in soup2.find_all("span","topic-actions"):
            #     pprint(s)
            #     s.decompose()

            # Also replace urls to relocate pages:
            # From: http://wiki.libreplan.org/bin/view/LibrePlan/MinuteS20121009
            # To: https://github.com/LibrePlan/libreplan/wiki/twiki
            # from_root="http://wiki.libreplan.org/bin/view/"
            # from_root = "/bin/view/"
            # to_root="https://github.com/LibrePlan/libreplan/wiki/twiki/"
            # for a in soup2.findAll("a"):
            #     #print a
            #     if from_root in a:
            #         a["href"] = a["href"].replace(from_root, to_root)
            # print str(len(pformat(soup2))) + ":" + pformat(soup2)


            # save intermediate html for checking purposes
            # File handling part
            filename=destination_directory+"/"+link_parts[-1] + ".pre-pandoc-concersion"
            print "Filename: " + filename
            # Save in libreplan.wiki/twiki
            text_file = codecs.open(filename, "w", "utf-8")
            text_file.write(soup2.prettify())
            text_file.close()

            # Convert page to markdown_github syntax

            #filters = ['pandoc-citeproc']
            #pdoc_args = ['--mathjax',
            #             '--smart']
            filters=[]
            pdoc_args=["--wrap=none"]

            # extensions: simple_tables, multiline_tables, grid_tables, pipe_tables
            # disable extension: raw_html, native_spans
            #extensions = "-raw_html-native_spans+pipe_tables"
            extensions = "-native_spans"
            # pipe_tables geeft hele brede kolommen. Next!
            # simple_tables idem

            print "Start pandoc conversion..."
            print str(len(pformat(soup2))) + ":" + pformat(soup2)
            my_output = pypandoc.convert_text(soup2,
                                              'markdown_github'+extensions,
                                              format='html',
                                              extra_args=pdoc_args,
                                              filters=filters)
            print "*" * 80
            print str(len(pformat(my_output))) + ":" + pformat(my_output)
            pprint(my_output)
            print "*" * 80

            # After pandoc conversion save intermediate file
            filename=destination_directory+"/"+link_parts[-1] + ".raw-md"
            print "Filename: " + filename
            # Save in libreplan.wiki/twiki
            text_file = codecs.open(filename, "w", "utf-8")
            text_file.write(my_output)
            text_file.close()
            #output = pypandoc.convert_text(soup2, "markdown_github", format='html', outputfile=filename)
            # assert output == ""

            # replace strings in md output
            # (/bin/view/ => (twiki/
            #my_output = my_output.replace("(/bin/view/", "(twiki/")

            # Next is not possible because also gifs in original
            #output = output.replace(")", ".md)")

            # change img urls to local
            #my_output = my_output.replace("http://wiki.libreplan-enterprise.com/twiki/pub/TWiki/TWikiDocGraphics/", "twiki/TWiki/TWikiDocGraphics/")
            #my_output = my_output.replace("http://wiki.libreplan-enterprise.com/twiki/pub/", "/twiki/")

            # Also replace all urls with "pub" in them
            #my_output = my_output.replace("/twiki/pub/TWiki/", "/twiki/TWiki/")

            # /twiki/bin/view/
            #my_output = my_output.replace("/twiki/bin/view/", "/twiki/")

            # remove persistent span in top of page
            #my_output = re.sub(r"<span id=\".*\">.*<\/span>", "", my_output)


            # Remove complete footer part from edit button to end of file!
            # Now doing this earlier in original html

            # Change url's in md phase
            # To create a reference link, use two sets of square brackets.
            # [[my internal link|internal-ref]] will link to the internal reference internal-ref.
            # examples
            # from: [url](/twiki/bin/view/Main/WebHome)
            # to:   [[url|/twiki/Main/WebHome]]
            #my_output = my_output.replace("/twiki/bin/view/", "/twiki/")
            #my_output="[url](/twiki/bin/view/Main/WebHome)  and image [](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif)"
            #
            # First succesfull re
            # my_output = re.sub(r"\[(.*?)\]\(/twiki/bin/view/(.*?)\)",
            #                    r"\n[[\1|/twiki/\2]]\n",
            #                    my_output)
            # Expanding with optional   http://wiki.libreplan-enterprise.com/twiki/bin/view/
            #my_output = re.sub(r"\[(.*?)\]\((http://wiki.libreplan-enterprise.com)?/twiki/bin/(view|edit)/(.*?)\)",
            #                   r"[[\1|/twiki/\4]]",
            #                   my_output)
            # Extra info for me: [[url|pagename]] refers to pagename without directory!
            # my_output = re.sub(r"\[(.*?)\]\((.*)/twiki/bin/.*/(.*?)\)",
            #                                  r"[[\1|\3]]",
            #                                  my_output)
            #
            # # and image [](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif)
            # my_output = re.sub(r"\[\]\(/twiki/pub/TWiki/TWikiDocGraphics/(.*?)\)",
            #                    r"[[|\1]]",
            #                    my_output)

            # File handling part
            filename=destination_directory+"/"+link_parts[-1] + ".md"
            print "Filename: " + filename
            # Save in libreplan.wiki/twiki
            text_file = codecs.open(filename, "w", "utf-8")
            text_file.write(my_output)
            text_file.close()
            #output = pypandoc.convert_text(soup2, "markdown_github", format='html', outputfile=filename)
            # assert output == ""
            # todo: add to git



        # Let's halt execution
        if counter>=5:
            #sys.exit(1)
            pass

print "Bugcounter final value: " + str(bugcounter)
# Play sound to indicate end of run
os.system("aplay /usr/share/games/simutrans/pak/sound/boing.wav")
