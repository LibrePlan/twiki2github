#!/usr/bin/env python
# -*- coding: utf-8 -*
#
# Program for converting LibrePlan Twiki pages to GitHub Wiki+markdown

# Because some content comes from separate MySQL table we use the webpage as root
# and not the Twiki/data files
# Call url https://wiki.libreplan.org/bin/view/LibrePlan/WebTopicList

import os,sys
import requests
from bs4 import BeautifulSoup
from pprint import pprint,pformat
import pypandoc
import codecs

# URL that lists all pages
url = "http://wiki.libreplan.org/bin/view/LibrePlan/WebTopicList"
# Root directory of old Twiki page
root_url="http://wiki.libreplan.org/"
# Dir to start exporting to
export_root_dir="./libreplan.wiki/twiki"
# All urls we are interested in start with:
starts_with="/bin/view"
# new url location
new_url_root="https://github.com/LibrePlan/libreplan/wiki/twiki"


print(pypandoc.get_pandoc_version())
print(pypandoc.get_pandoc_path())
print(pypandoc.get_pandoc_formats())

#
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html.parser")

counter=0
for link in soup.find_all('a'):
    counter+=1
    print "#" * 120
    link=link.get('href')

    #print(link.get('href'))
    if link is not None and link.startswith(starts_with):
        print link,
        link_parts=link.split("/")
        print ", in parts: ",pformat(link_parts),
        page_to_convert_url= root_url + link  #  _parts[-1] # get last part after splitting to get page name
        print "page to request: ",page_to_convert_url

        # todo get history of page and build a loop around it

        # Actually retrieve wiki page
        try:
            r2 = requests.get(page_to_convert_url, allow_redirects=False) # to prevent redirection to https
        except:
            print "Unexpected error:", sys.exc_info()[0]

        data2=r.text
        soup2=BeautifulSoup(data2, "html.parser")
        print "*" * 80
        print str(len(pformat(soup2)))+":"+pformat(soup2)

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

        # remove all div tages
        invalid_tags = ['div','span',"base"]
        for tag in invalid_tags:
            for match in soup2.findAll(tag):
                match.replaceWithChildren()
        print str(len(pformat(soup2))) + ":" + pformat(soup2)

        # Also replace urls to relocate pages:
        # From: http://wiki.libreplan.org/bin/view/LibrePlan/MinuteS20121009
        # To: https://github.com/LibrePlan/libreplan/wiki/twiki
        #from_root="http://wiki.libreplan.org/bin/view/"
        # from_root = "/bin/view/"
        # to_root="https://github.com/LibrePlan/libreplan/wiki/twiki/"
        # for a in soup2.findAll("a"):
        #     #print a
        #     if from_root in a:
        #         a["href"] = a["href"].replace(from_root, to_root)
        # print str(len(pformat(soup2))) + ":" + pformat(soup2)

        output = pypandoc.convert_text(soup2, 'markdown_github', format='html')
        print "*" * 80
        pprint(output)
        print "*" * 80

        # replace strings in md output
        # (/bin/view/ => (twiki/
        output = output.replace("(/bin/view/","(twiki/")
        output = output.replace(")", ".md)")


        # Directory handling part
        # Check for directory
        destination_directory=export_root_dir+"/"+link_parts[-2]
        print "Directory: " + destination_directory,
        if os.path.isdir(destination_directory):
            print "Found..."
        else:
            print "Not found! Creating!"
            os.makedirs(destination_directory)

        # File handling part
        filename=destination_directory+"/"+link_parts[-1] + ".md"
        print "Filename: " + filename
        # Save in libreplan.wiki/twiki
        text_file = codecs.open(filename, "w", "utf-8")
        text_file.write(output)
        text_file.close()
        #output = pypandoc.convert_text(soup2, "markdown_github", format='html', outputfile=filename)
        # assert output == ""
        # todo: add to git


    # Let's halt execution
    if counter>5:
        #sys.exit(1)
        pass


