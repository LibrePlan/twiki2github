[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20120612](LibrePlan_MinuteS20120612 "Topic revision: 2 (26 Jun 2012 - 14:52:06)") (26 Jun 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20120612?t=1520343720 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20120612 "Attach an image or document to this topic")  

 LibrePlan Meeting 2012/06/12
=============================

-   Date: June 12, 2012 at 16:30 CEST (GMT +2)
-   Agenda: Coordination meeting
-   Log: `libreplan-coordination-meeting-20120612.txt`

 Minutes
--------

-   Manuel Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Finished implementation 2nd part of resource binding: [ItEr76S28UserDashboard](LibrePlan_ItEr76S28UserDashboard). There are still some pending patches by Loren to fix some UI issues in the new user dashboard and monthly timesheet.
        -   Bugfixing: \#1452, \#1459, \#1454, \#1439, \#1460, \#1463
        -   Started with the task: [ItEr76S30PermissionsEnhancements](LibrePlan_ItEr76S30PermissionsEnhancements) (and helped Javi Morán with the analysis of that task)
        -   Patch review
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish [ItEr76S30PermissionsEnhancements](LibrePlan_ItEr76S30PermissionsEnhancements)
        -   Start to test the application and try to create a draft of the user help in order to release LibrePlan 1.3

&nbsp;

-   Javi Morán
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Week 22 on holidays
        -   Analysis of how to measure the filming progress in LibrePlan audivisual
        -   Working in analysis of permissions enhancements: [AnA20S01PermissionsEnhancements](LibrePlan_AnA20S01PermissionsEnhancements)
        -   Reported a pair of bugs
        -   Did community tasks
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish the analysis of the permissions tasks: [AnA20S01PermissionsEnhancements](LibrePlan_AnA20S01PermissionsEnhancements)
        -   Test all the new developments for LibrePlan 1.3

&nbsp;

-   Diego Pino
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Dashboard: [ItEr76S15OrganizingPerProjectDashboard](LibrePlan_ItEr76S15OrganizingPerProjectDashboard)
            -   Update Global Progress chart dinamically (without saving project)
            -   Moved js jqplot code to jar
                -   Created own version of jqplot4java, served now from our Nexus.
            -   Fixed bug in Tomcat: Cannot load resource files
            -   Fixed syntax error in Javascript that caused 'Global Chart' chart could not be loaded some times
            -   Refactored coded in MonteCarlo for building critical path (reused by Dashboard now)
            -   Fixed NPE when switching from 'Project Details' view to 'Dashboard'
            -   Added 'Spread Progress' bar to 'Global Progress' chart
            -   Added pop-up tooltip to 'Global Progress' chart
        -   WorkReports[?](LibrePlan_WorkReports?topicparent=LibrePlan.MinuteS20120612 "Create this topic") improvements: [ItEr76S29WorkReports](LibrePlan_ItEr76S29WorkReports)
            -   Improve work report lines filtering and report output
            -   Increase number of results per page
            -   Include summary line at the end of the report
        -   BugFixing[?](LibrePlan_BugFixing?topicparent=LibrePlan.MinuteS20120612 "Create this topic") : [ItEr76S04BugFixing](LibrePlan_ItEr76S04BugFixing)
            -   Fixed: \#1457, \#1461
            -   WIP: \#1275
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Bugfixing

&nbsp;

-   Jacobo Aragunde
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Focused in audiovisual branch:
            -   Creation of Budget object from a Template
            -   Implement budget perspective inside a project
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish budget perspective
        -   Implement the creation of the project WBS based on the budget
        -   Help with bugfixing for release 1.3

&nbsp;

-   Loren Tilve
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Worked on audiovisual branch (analysis and coordination)
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Integrate some small design fixes pending on user and project dashboards
        -   Upload a first skeleton (or draft) of the new user help

&nbsp;

-   Susana Montes
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Did the import and export of expenses sheets
        -   Fixed bug \#1446 (pending to close it in the bugzilla)
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Fix an issue in the subcontracting process

&nbsp;

-   Lucía García
    -   She has been working in the mobile app to report work hours.
    -   Currently the application reads the work reports from the web services and show them in a list. It's also possible to create a new work report with its work report lines
    -   She is working in generating the XML file to be sent to the web service

&nbsp;

-   LibrePlan 1.3
    -   We're in the week 24 that it was supposed to be the release week ([see announcement](http://www.libreplan.com/news/detail/article/some-updates-about-libreplan-13/)) but we're delayed again ![frown](/twiki/pub/TWiki/SmiliesPlugin/frown.gif "frown")
    -   Pending things:
        -   Permissions enhancements: Plan is to finish it this week or at the beginning of the next one
        -   Help improvement: We're really delayed with this task, we'll try to have something for the release, but it won't block the release and will be included in a later minor version (like 1.3.1 or so)
    -   There're a lot of new features in LibrePlan 1.3 so we need to invest some time in testing and bugfixing
    -   We should notify the translators with some margin as there're a lot of new features, but we want to do a day of strings review to improve some of them in the original language
    -   So the new date for LibrePlan 1.3 release is **week 28**. We should announce this new delay again this week
