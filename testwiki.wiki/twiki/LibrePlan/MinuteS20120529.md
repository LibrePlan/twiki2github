[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20120529](LibrePlan_MinuteS20120529 "Topic revision: 1 (30 May 2012 - 05:51:08)") (30 May 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20120529?t=1520343720 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20120529 "Attach an image or document to this topic")  

 LibrePlan Meeting 2012/04/24
=============================

-   Date: May 29, 2012 at 16:30 CET (GMT +2)
-   Agenda: Coordination meeting
-   Log: `libreplan-coordination-meeting-20120529.txt`

 Minutes
--------

-   Manuel Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Finished resource binding first part: [ItEr76S27ResourceBinding](LibrePlan_ItEr76S27ResourceBinding)
        -   Updated to Liquibase 2.0.5 and fix issues with MySQL
        -   Improved doc about LibrePlan webservices: <http://libreplan.org/libreplan-web-services.html#available-web-services>
        -   Bugfixing: \#1445, \#1450, \#1448
        -   Uploaded Czech language
        -   Released [LibrePlan](LibrePlan_LibrePlan) 1.2.4 (first version with MySQL supported)
        -   Started with the second part of resource binding (WIP): [ItEr76S28UserDashboard](LibrePlan_ItEr76S28UserDashboard)
            -   Spent quite a lot of time to redirect bound users to user dashboard (finally used a URL target resolver)
            -   First usable version of the monthly timesheet is pushed but lots of things are pending yet
        -   Done the common patch review
        -   Replaying to LibrePlan community, specially <http://ask.libreplan.org>
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish the second part of resource binding: [ItEr76S28UserDashboard](LibrePlan_ItEr76S28UserDashboard)
        -   Common patch review and bugfixing

&nbsp;

-   Jacobo Aragunde
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Bugfixing:
            -   Reported \#1433, \#1434, \#1435, \#1436, \#1437, \#1438, \#1439, \#1443, \#1444 and \#1449
            -   Fixed \#1433, \#1442, \#1444
            -   Added favicon to see if \#1284 (404 error trying to open favicon) gets fixed. It seems fixed since 1.2.4 so far
            -   Helped with \#1451, but it's not fixed yet
        -   Audiovisual branch:
            -   Finished budget template creation/edition screen
            -   Started working on project budgets: entities, creation of budget from template
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Bugfixing towards 1.3 release

&nbsp;

-   Diego Pino
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Project Dashboard: [ItEr76S15OrganizingPerProjectDashboard](LibrePlan_ItEr76S15OrganizingPerProjectDashboard)
            -   Implemented pending charts: 'Overtime Ratio'
            -   Code refactoring: EarnedValueCalculator
            -   Added feature to allow set colors in PieCharts
            -   Isolated 'Global Progress' chart code in different files
            -   Removed unused code in jqplot
            -   Removed unused code in DashboardModel
            -   Bug Fixing in 'Task Completation' and 'Absolute Margin with Deadline' charts
            -   Bug Fixing: Dashboard didn't show up in live demo (wrong path to JS files)
            -   Bug Fixing: Wrong paths to other JS files
            -   WIP: Move jqplot JS code to jqplot4java
        -   Cache tuning: [ItEr76S18CacheTuning](LibrePlan_ItEr76S18CacheTuning)
            -   Performance tests (MAX values improved considerably, around 75%)
            -   Landed patches in master
            -   Bug Fixing: Crash in live demo when it was deployed (wrong version of ehcache included)
        -   Work Reports Improvements [ItEr76S29WorkReports](LibrePlan_ItEr76S29WorkReports)
            -   Improved work report lines filtering and report output
            -   Increased number of results per page to 15
            -   Included summary line at the end of the report
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Continue with moving jqplot JS code to jqplot4java
        -   Bugfixing
