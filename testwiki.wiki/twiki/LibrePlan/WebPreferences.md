[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[WebPreferences](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences "Topic revision: 21 (29 Nov 2011 - 18:05:42)") (29 Nov 2011, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/WebPreferences?t=1520337988 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/WebPreferences "Attach an image or document to this topic")

 LibrePlan Web Preferences
===================================================================================================================

The following settings are ***web preferences*** of the [LibrePlan](/twiki/LibrePlan/WebHome) web. These preferences overwrite the ***site-level preferences*** in [TWiki.TWikiPreferences](/twiki/TWiki/TWikiPreferences) and [Main.TWikiPreferences](/twiki/Main/TWikiPreferences), and can be overwritten by ***user preferences*** (your personal topic, eg: [TWikiGuest](/twiki/Main/TWikiGuest) in the [Main](/twiki/Main/WebHome) web).

-   [Web Preferences Settings](#Web_Preferences_Settings)
-   [Help on Preferences](#Help_on_Preferences)
-   [Related Topics](#Related_Topics)
-   [Tools](#Tools)

 Web Preferences Settings
--------------------------------------------------------------------

These settings override the defaults for this web only. See [full list of defaults with explanation](/twiki/TWiki/TWikiPreferences#DefaultWebPreferences). Many of the settings below are commented out. Remove the \# sign to enable a local customisation.

-   PhpReport Project data:
    -   Set PROJECTNAME = [LibrePlan](/twiki/LibrePlan/LibrePlan)
    -   Set PROJECTTYPE = \*
    -   Set PROJECTCUSTOMER = Igalia

-   List of topics of the LibrePlan web:
    -   \#Set WEBTOPICLIST = [Changes](/twiki/LibrePlan/WebChanges)  |  [Index](/twiki/LibrePlan/WebIndex)  |  [Search](/twiki/LibrePlan/WebSearch)  |  Go

 \#DDDDDD 

-   Web-specific background color: (Pick a lighter one of the [StandardColors](/twiki/TWiki/StandardColors)).
    -   Set WEBBGCOLOR = \#DDDDDD
    -   ***Note:*** This setting is automatically configured when you create a web

-   Image, URL and alternate tooltip text of web's logo.
    ***Note:*** Don't add your own local logos to the [TWikiLogos](/twiki/TWiki/TWikiLogos) topic; create your own logos topic instead.
    -   Set WEBLOGOIMG = ![librePlanLogo.png](http://www.libreplan.com/fileadmin/templates/libreplan/i/librePlanLogo.png)
    -   Set WEBLOGOURL = <http://www.libreplan.com/>
    -   Set WEBLOGOALT = [LibrePlan](/twiki/LibrePlan/LibrePlan) - Open Web Planning

-   List this web in the [SiteMap](/twiki/TWiki/SiteMap). If you want the web listed, then set SITEMAPLIST to `on`, do not set NOSEARCHALL, and add the "what" and "use to..." description for the site map. Use links that include the name of the web, i.e. LibrePlan.Topic links.
    ***Note:*** Unlike other variables, the setting of SITEMAPLIST is **not** inherited from parent webs. It has to be set in **every** web that is to be listed in the [SiteMap](/twiki/TWiki/SiteMap)
    -   Set SITEMAPLIST = on
    -   Set SITEMAPWHAT =
    -   Set SITEMAPUSETO =
    -   ***Note:*** Above settings are automatically configured when you create a web

-   Exclude web from a `web="all"` search: (Set to `on` for hidden webs).
    -   Set NOSEARCHALL =
    -   ***Note:*** This setting is automatically configured when you create a web

-   Prevent automatic linking of [WikiWords](/twiki/TWiki/WikiWord) and acronyms (if set to `on`); link WikiWords (if empty); can be overwritten by web preferences:
    -   \#Set NOAUTOLINK =
    -   ***Note:*** You can still use the `[[...][...]]` syntax to link topics if you disabled WikiWord linking. The `<noautolink> ... </noautolink>` syntax can be used to prevents links within a block of text.

-   Default template for **new topics** for this web:
    -   [WebTopicEditTemplate](/twiki/LibrePlan/WebTopicEditTemplate): Default template for new topics in this web. (Site-level is used if topic does not exist)
    -   [TWiki.WebTopicEditTemplate](/twiki/TWiki/WebTopicEditTemplate): Site-level default topic template

-   Comma separated list of **forms** that can be attached to topics in this web. See [TWikiForms](/twiki/TWiki/TWikiForms) for more information.
    -   Set WEBFORMS =

-   Users or groups who ***are not*** / ***are*** allowed to ***view*** / ***change*** / ***rename*** topics in the LibrePlan web: (See [TWikiAccessControl](/twiki/TWiki/TWikiAccessControl)).
    -   Set DENYWEBVIEW =
    -   Set ALLOWWEBVIEW =
    -   Set DENYWEBCHANGE =
    -   Set ALLOWWEBCHANGE =
    -   Set DENYWEBRENAME =
    -   Set ALLOWWEBRENAME =

-   Users or groups allowed to change or rename this WebPreferences topic: (e.g., [TWikiAdminGroup](/twiki/Main/TWikiAdminGroup))
    -   Set ALLOWTOPICCHANGE =
    -   Set ALLOWTOPICRENAME =

-   Web preferences that are **not** allowed to be overridden by user or topic preferences:
    -   Set FINALPREFERENCES = NOSEARCHALL, ATTACHFILESIZELIMIT, WIKIWEBMASTER, WEBCOPYRIGHT, WEBTOPICLIST, DENYWEBVIEW, ALLOWWEBVIEW, DENYWEBCHANGE, ALLOWWEBCHANGE, DENYWEBRENAME, ALLOWWEBRENAME

 Help on Preferences
----------------------------------------------------------

-   A preference setting is defined by:
    `3 or 6 spaces * Set NAME = value`
    Example:
    -   Set WEBBGCOLOR = \#FFFFC0
-   A preferences setting can be disabled with a \# sign. Remove the \# sign to enable a local customisation. Example:
    -   \#Set DENYWEBCHANGE = [UnknownUser](/twiki/Main/UnknownUser)
-   Preferences are used as [TWikiVariables](/twiki/TWiki/TWikiVariables) by enclosing the name in percent signs. Example:
    -   When you write variable `%WEBBGCOLOR%` , it gets expanded to `#DDDDDD`
-   The sequential order of the preference settings is significant. Define preferences that use other preferences first, i.e. set `WEBCOPYRIGHT` before `WIKIWEBMASTER` since `%WEBCOPYRIGHT%` uses the `%WIKIWEBMASTER%` variable.
-   You can introduce your own preferences variables and use them in your topics and templates.

 Related Topics
------------------------------------------------

-   [TWiki.TWikiPreferences](/twiki/TWiki/TWikiPreferences), [Main.TWikiPreferences](/twiki/Main/TWikiPreferences) - site-level preferences
-   [TWikiUsers](/twiki/Main/TWikiUsers) - list of user topics. User topics can have optional user preferences
-   [TWikiVariables](/twiki/TWiki/TWikiVariables) - list of common `%VARIABLES%`
-   [TWikiAccessControl](/twiki/TWiki/TWikiAccessControl) - explains how to restrict access by users or groups

 Tools
------------------------------

-   ![move](/twiki/TWiki/TWikiDocGraphics/move.gif) **Rename, move or delete this web:**
    -   **[Rename/move/delete web...](/twiki/bin/rename/LibrePlan/WebPreferences?action=renameweb)**, looking for references in *all public webs* - See also: [ManagingWebs](/twiki/TWiki/ManagingWebs)

[![](/twiki/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](#) [![](/twiki/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](#)

| [I](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=0;table=1;up=0#sorted_table "Sort by this column") | [Attachment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=1;table=1;up=0#sorted_table "Sort by this column") | [Action](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=2;table=1;up=0#sorted_table "Sort by this column") | [Size](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=3;table=1;up=0#sorted_table "Sort by this column") | [Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=4;table=1;up=0#sorted_table "Sort by this column") | [Who](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=5;table=1;up=0#sorted_table "Sort by this column") | [Comment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebPreferences?sortcol=6;table=1;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![bmp](/twiki/TWiki/TWikiDocGraphics/bmp.gif)ico                                                                                        | [favicon.ico](/twiki/pub/LibrePlan/WebPreferences/favicon.ico)                                                                                       | [manage](/twiki/bin/attach/LibrePlan/WebPreferences?filename=favicon.ico;revInfo=1 "change, update, previous revisions, move, delete...")        | 16.6 K                                                                                                                                         | 29 Nov 2011 - 17:51                                                                                                                            | [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                             | placeholder favicon                                                                                                                               |


