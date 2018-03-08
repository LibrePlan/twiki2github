[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[WebPreferences](LibrePlan_WebPreferences "Topic revision: 21 (29 Nov 2011 - 18:05:42)") (29 Nov 2011, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_WebPreferences?t=1520343749 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/WebPreferences "Attach an image or document to this topic")  

 LibrePlan Web Preferences
==========================

The following settings are ***web preferences*** of the [LibrePlan](LibrePlan_WebHome) web. These preferences overwrite the ***site-level preferences*** in [TWiki.TWikiPreferences](/twiki/bin/view/TWiki/TWikiPreferences) and [Main.TWikiPreferences](Main_TWikiPreferences), and can be overwritten by ***user preferences*** (your personal topic, eg: [TWikiGuest](Main_TWikiGuest) in the [Main](Main_WebHome) web).

-   [Web Preferences Settings](LibrePlan_WebPreferences#Web_Preferences_Settings)
-   [Help on Preferences](LibrePlan_WebPreferences#Help_on_Preferences)
-   [Related Topics](LibrePlan_WebPreferences#Related_Topics)
-   [Tools](LibrePlan_WebPreferences#Tools)

 Web Preferences Settings
-------------------------

These settings override the defaults for this web only. See [full list of defaults with explanation](/twiki/bin/view/TWiki/TWikiPreferences#DefaultWebPreferences). Many of the settings below are commented out. Remove the \# sign to enable a local customisation.

-   PhpReport Project data:
    -   Set PROJECTNAME = [LibrePlan](LibrePlan_LibrePlan)
    -   Set PROJECTTYPE = \*
    -   Set PROJECTCUSTOMER = Igalia

&nbsp;

-   List of topics of the LibrePlan web:
    -   \#Set WEBTOPICLIST = [Changes](LibrePlan_WebChanges)  \|  [Index](LibrePlan_WebIndex)  \|  [Search](LibrePlan_WebSearch)  \|  Go

 \#DDDDDD 

-   Web-specific background color: (Pick a lighter one of the [StandardColors](/twiki/bin/view/TWiki/StandardColors)).
    -   Set WEBBGCOLOR = \#DDDDDD
    -   ***Note:*** This setting is automatically configured when you create a web

&nbsp;

-   Image, URL and alternate tooltip text of web's logo.  
    ***Note:*** Don't add your own local logos to the [TWikiLogos](/twiki/bin/view/TWiki/TWikiLogos) topic; create your own logos topic instead.
    -   Set WEBLOGOIMG = ![librePlanLogo.png](http://www.libreplan.com/fileadmin/templates/libreplan/i/librePlanLogo.png)
    -   Set WEBLOGOURL = <http://www.libreplan.com/>
    -   Set WEBLOGOALT = [LibrePlan](LibrePlan_LibrePlan) - Open Web Planning

&nbsp;

-   List this web in the [SiteMap](/twiki/bin/view/TWiki/SiteMap). If you want the web listed, then set SITEMAPLIST to `on`, do not set NOSEARCHALL, and add the "what" and "use to..." description for the site map. Use links that include the name of the web, i.e. LibrePlan.Topic links.  
    ***Note:*** Unlike other variables, the setting of SITEMAPLIST is **not** inherited from parent webs. It has to be set in **every** web that is to be listed in the [SiteMap](/twiki/bin/view/TWiki/SiteMap)  
    -   Set SITEMAPLIST = on
    -   Set SITEMAPWHAT =
    -   Set SITEMAPUSETO =
    -   ***Note:*** Above settings are automatically configured when you create a web

&nbsp;

-   Exclude web from a `web="all"` search: (Set to `on` for hidden webs).
    -   Set NOSEARCHALL =
    -   ***Note:*** This setting is automatically configured when you create a web

&nbsp;

-   Prevent automatic linking of [WikiWords](/twiki/bin/view/TWiki/WikiWord) and acronyms (if set to `on`); link WikiWords (if empty); can be overwritten by web preferences:
    -   \#Set NOAUTOLINK =
    -   ***Note:*** You can still use the `[[...][...]]` syntax to link topics if you disabled WikiWord linking. The `<noautolink> ... </noautolink>` syntax can be used to prevents links within a block of text.

&nbsp;

-   Default template for **new topics** for this web:
    -   [WebTopicEditTemplate](LibrePlan_WebTopicEditTemplate): Default template for new topics in this web. (Site-level is used if topic does not exist)
    -   [TWiki.WebTopicEditTemplate](/twiki/bin/view/TWiki/WebTopicEditTemplate): Site-level default topic template

&nbsp;

-   Comma separated list of **forms** that can be attached to topics in this web. See [TWikiForms](/twiki/bin/view/TWiki/TWikiForms) for more information.
    -   Set WEBFORMS =

&nbsp;

-   Users or groups who ***are not*** / ***are*** allowed to ***view*** / ***change*** / ***rename*** topics in the LibrePlan web: (See [TWikiAccessControl](/twiki/bin/view/TWiki/TWikiAccessControl)).
    -   Set DENYWEBVIEW =
    -   Set ALLOWWEBVIEW =
    -   Set DENYWEBCHANGE =
    -   Set ALLOWWEBCHANGE =
    -   Set DENYWEBRENAME =
    -   Set ALLOWWEBRENAME =

&nbsp;

-   Users or groups allowed to change or rename this WebPreferences topic: (e.g., [TWikiAdminGroup](Main_TWikiAdminGroup))
    -   Set ALLOWTOPICCHANGE =
    -   Set ALLOWTOPICRENAME =

&nbsp;

-   Web preferences that are **not** allowed to be overridden by user or topic preferences:
    -   Set FINALPREFERENCES = NOSEARCHALL, ATTACHFILESIZELIMIT, WIKIWEBMASTER, WEBCOPYRIGHT, WEBTOPICLIST, DENYWEBVIEW, ALLOWWEBVIEW, DENYWEBCHANGE, ALLOWWEBCHANGE, DENYWEBRENAME, ALLOWWEBRENAME

 Help on Preferences
--------------------

-   A preference setting is defined by:  
    `3 or 6 spaces * Set NAME = value`  
    Example:
    -   Set WEBBGCOLOR = \#FFFFC0
-   A preferences setting can be disabled with a \# sign. Remove the \# sign to enable a local customisation. Example:  
    -   \#Set DENYWEBCHANGE = [UnknownUser](Main_UnknownUser)
-   Preferences are used as [TWikiVariables](/twiki/bin/view/TWiki/TWikiVariables) by enclosing the name in percent signs. Example:
    -   When you write variable `%WEBBGCOLOR%` , it gets expanded to `#DDDDDD`
-   The sequential order of the preference settings is significant. Define preferences that use other preferences first, i.e. set `WEBCOPYRIGHT` before `WIKIWEBMASTER` since `%WEBCOPYRIGHT%` uses the `%WIKIWEBMASTER%` variable.
-   You can introduce your own preferences variables and use them in your topics and templates.

 Related Topics
---------------

-   [TWiki.TWikiPreferences](/twiki/bin/view/TWiki/TWikiPreferences), [Main.TWikiPreferences](Main_TWikiPreferences) - site-level preferences
-   [TWikiUsers](Main_TWikiUsers) - list of user topics. User topics can have optional user preferences
-   [TWikiVariables](/twiki/bin/view/TWiki/TWikiVariables) - list of common `%VARIABLES%`
-   [TWikiAccessControl](/twiki/bin/view/TWiki/TWikiAccessControl) - explains how to restrict access by users or groups

 Tools
------

-   ![move](/twiki/pub/TWiki/TWikiDocGraphics/move.gif) **Rename, move or delete this web:**
    -   **[Rename/move/delete web...](/twiki/bin/rename/LibrePlan/WebPreferences?action=renameweb)**, looking for references in *all public webs* - See also: [ManagingWebs](/twiki/bin/view/TWiki/ManagingWebs)

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_WebPreferences#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_WebPreferences#)

| [I](LibrePlan_WebPreferences?sortcol=0;table=1;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_WebPreferences?sortcol=1;table=1;up=0#sorted_table "Sort by this column") | [Action](LibrePlan_WebPreferences?sortcol=2;table=1;up=0#sorted_table "Sort by this column")                                              |  [Size](LibrePlan_WebPreferences?sortcol=3;table=1;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_WebPreferences?sortcol=4;table=1;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_WebPreferences?sortcol=5;table=1;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_WebPreferences?sortcol=6;table=1;up=0#sorted_table "Sort by this column") |
|:---------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
|                   ![bmp](/twiki/pub/TWiki/TWikiDocGraphics/bmp.gif)ico                  | [favicon.ico](/twiki/pub/LibrePlan/WebPreferences/favicon.ico)                                   | [manage](/twiki/bin/attach/LibrePlan/WebPreferences?filename=favicon.ico;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                      16.6 K| 29 Nov 2011 - 17:51                                                                        | [LorenzoTilve](Main_LorenzoTilve)                                                         | placeholder favicon                                                                           |
