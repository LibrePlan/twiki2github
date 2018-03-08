[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20120306](LibrePlan_MinuteS20120306 "Topic revision: 3 (08 Mar 2012 - 08:37:18)") (08 Mar 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20120306?t=1520343718 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20120306 "Attach an image or document to this topic")  

 LibrePlan Meeting 2012/03/06
=============================

-   Date: March 6, 2012 at 16:30 CET (GMT +1)
-   Agenda: Coordination meeting
-   Log: `libreplan-coordination-meeting-20120306.txt`

 Minutes
--------

-   Jacobo Aragunde
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Fixed bugs related with the scheduling algorithm: 1354, 1355, 1356, 1380.
            -   These bugs helped getting a better knowledge of the algorithm.
            -   Also, the work in \#1355 helped to identify a performance problem (the algorithm was being run more times than necessary) and fix it.
        -   Fixed \#1344, related with violated dependencies not being shown in red in some cases.
        -   Triagging, closed some old bugs as fixed or invalid (18, 49, 59, 110, 122, 128, 140, 141, 142, 171, 834), confirmed and updated some other (123, 130).
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Fix a pending bug before the release (1387).
        -   Testing previous to the release.
        -   Start working in features for 1.3.

&nbsp;

-   Lorenzo Tilve
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Fixed bugs
        -   Pushed the 'show project start line' feature into both master and 1.2.
        -   Other minor fixes to be pushed for 1.2.2.
        -   Documentation: experimenting a new approach for the help based on a simple 'procedures map' with "what you want to do?" like boxes: 'create and assing projects', 'manage outsorcing', etc. which link to the sections.
            -   This is in a beta state but should be considered in the future as the documentation bible is difficult to maintain and not user-friendly.
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Fix the tests for 1.2.2 release.

&nbsp;

-   Javier Morán
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Analysis:
            -   WBS: [AnA08S18WBSSettingUpBehavior](LibrePlan_AnA08S18WBSSettingUpBehavior)
            -   Tested and analysed the pending work to do of the project dashboard (KPIs). Analysed wrote: [AnA14S02OrganizingPerProjectDashboard](LibrePlan_AnA14S02OrganizingPerProjectDashboard)
            -   Analysis for bind user-resource feature for 1.3: <http://sourceforge.net/mailarchive/message.php?msg_id=28896528>
            -   Meeting with Javier Toja to advance on the analysis for the [LibrePlan](LibrePlan_LibrePlan) - Mantis Bugtracker integration.
        -   Blog post: <http://blogs.igalia.com/javimoran/2012/03/03/libreplan-makes-easier-to-know-the-project-status/>
        -   Review and report bugs
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   keep with analysis, coordination, help with the release, and community tasks.

&nbsp;

-   Javier Toja
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Started developing webservice client to communicate with Mantis WS.
            -   Started implementing with Axis but had to change to CXF.
            -   Now he has checked that Mantis WS are good and have all the operations we need.
            -   As a side note, Mantis services are SOAP and we don't have that kind of services in LP yet.
            -   A connector software was evaluated to implement the SOAP client but it was discarded (not free software and unmaintained).
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Change the Axis implementation to CXF.
        -   Do performance tests.

&nbsp;

-   Nacho Díaz
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Working on feature for 1.3: [AnA17S01ConfigurationUnitInterfaceCorrections\#TasK1](LibrePlan_AnA17S01ConfigurationUnitInterfaceCorrections#TasK1)
            -   Work is almost done, but there are problems showing the error messages on input constraints.
                -   Jacobo to review this.
        -   Working on the Android app together with Lucía
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Keep working on [AnA17S01ConfigurationUnitInterfaceCorrections](LibrePlan_AnA17S01ConfigurationUnitInterfaceCorrections).
        -   Continue with the Android client.
