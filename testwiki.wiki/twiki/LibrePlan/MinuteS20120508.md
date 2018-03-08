[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20120508](LibrePlan_MinuteS20120508 "Topic revision: 2 (14 May 2012 - 07:23:23)") (14 May 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20120508?t=1520343719 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20120508 "Attach an image or document to this topic")  

 LibrePlan Meeting 2012/04/24
=============================

-   Date: May 8, 2012 at 16:30 CET (GMT +2)
-   Agenda: Coordination meeting
-   Log: `libreplan-coordination-meeting-20120508.txt`

 Minutes
--------

-   Manuel Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Upgraded Liquibase to 2.0.4, so from now on we should be 100% compatible with MySQL
        -   Upgraded ZK to 5.0.11
        -   Fixed several bugs: \#1422, \#1412, \#1424, \#1423, \#1388, \#1263, \#1425, \#1430, \#1428, \#1431
        -   Analyzed and implemented task [ItEr76S25CurrencyManagement](LibrePlan_ItEr76S25CurrencyManagement)
        -   Started a new task for 1.3: [ItEr76S27ResourceBinding](LibrePlan_ItEr76S27ResourceBinding)
        -   Updated keys.pot files for release 1.2.4 and notified translators
        -   Updated Spanish and Galician translators
        -   General patch review
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Liquibase 2.0.5 has been released, so we should upgrade to it as it has some minor bugfixes
        -   Keep working in the tasks for [ItEr76S27ResourceBinding](LibrePlan_ItEr76S27ResourceBinding)
        -   General patch review as bugfixing
        -   Test LibrePlan for release 1.2.4
        -   Release LibrePlan 1.2.4 in week 20

&nbsp;

-   Loren Tilve
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Push two small bugfixes
        -   Worked on Galician translation of libreplan.com website
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Some bugfixes
        -   Try to evolve the new help for 1.3

&nbsp;

-   Javi Morán
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Analysis Mantis - LibrePlan integration ... (pending to be written)
        -   Support Rego with currency analysis
        -   Worked in analysis of audiovisual branch. Some tasks that will be in master and 1.3 (for example: [AnAS20RemoveExternalCodeFromTemplates](LibrePlan_AnAS20RemoveExternalCodeFromTemplates))
        -   Analysis of the first part of resource binding [AnA11S03ResourceBinding](LibrePlan_AnA11S03ResourceBinding)
        -   Community: talked to users, forums, ...
        -   Testing: few bugs filed \#1423, \#1424
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish with resource binding analysis
        -   Do permission revamp analysis
        -   LibrePlan audivisual analysis
        -   LibrePlan testing
        -   Community news
        -   Collaborate in writing the index for the new help

&nbsp;

-   Jacobo Aragunde
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Implemented task [ItEr76S26RemoveExternalCodeFromTemplates](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates)
        -   Prepared and gave a talk about LibrePlan at FIC (A Coruña University)
        -   Worked on budget template creation/edition screen in audiovisual branch
        -   Reported \#1425, \#1429
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Continue with the work on audiovisual branch and eventually fix urgent bugs
        -   Integrate in master a patch for creating templates from scratch

&nbsp;

-   Diego Pino
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Kept on working in the KPIs dashboard
        -   Revamped some pending charts
        -   Bugfixing on some charts
        -   Refactored earned value code to be used from the dashboard
        -   Removed the global progress chart that was in the part below of every project
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Keep working in the KPIs dashboard

&nbsp;

-   We finally talked about LibrePlan 1.3 release that is already delayed
    -   About the [RoadMap](LibrePlan_RoadMap)
        -   We agreed that all the top priority tasks from the [RoadMap](LibrePlan_RoadMap) should be included in the release. Some of them are already implemented and the ones pending are:
            -   Bind users to resources (WIP)
            -   Permissions enhancement
            -   Improve help
        -   From the medium priority the ones that will be included in LibrePlan 1.3 are:
            -   Vertical line to show with the start of the project
            -   KPIs per project
            -   Subcontracting module
        -   And some new features (not present in the [RoadMap](LibrePlan_RoadMap)) will be included in 1.3 too:
            -   Money based cost monitoring system
            -   Expenses tracking
    -   Taking this into account we agree to set as new estimated date for LibrePlan 1.3 the week 24
