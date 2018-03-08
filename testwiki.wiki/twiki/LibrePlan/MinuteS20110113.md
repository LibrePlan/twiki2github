[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20110113](LibrePlan_MinuteS20110113 "Topic revision: 5 (20 Aug 2012 - 09:52:55)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20110113?t=1520343711 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20110113 "Attach an image or document to this topic")  

 LibrePlan Meeting 2011/01/13
=============================

-   Date: [January 13, 2011 at 17:00 CET (GMT +1)](http://www.timeanddate.com/worldclock/fixedtime.html?day=13&month=1&year=2011&hour=17&min=0&sec=0&p1=48)
-   Goal: Discuss and update [RoadMap](LibrePlan_RoadMap) for versions 1.1 and 1.2
-   Agenda: [Agenda](https://etherpad.igalia.com/191)
-   Log: [navalplan-roadmap-meeting-20110113.txt](http://wiki.navalplan.org/twiki/pub/NavalPlan/Meetings/navalplan-roadmap-meeting-20110113.txt)

 Minutes
--------

-   Review and explanation of proposed tasks for version 1.1.
-   Debate about which features to include in version 1.1.
    -   Added some tasks for 1.1:
        -   Help improvement as we agreed is important for a complex application like LibrePlan.
        -   Allow configuration for default login auto-completion (`admin/admin`).
        -   Improve task identification for some reports (adding task name and project name).
        -   Support of intraday operations. Changing the grain of the work to allocate in order to introduce quantities that are not multiple of hours.
    -   Delayed some tasks to 1.2:
        -   [Critical chain](http://en.wikipedia.org/wiki/Critical_Chain_Project_Management).
        -   Improve performance of resource load view.
    -   Prioritize the tasks for 1.1:
        -   Most important:
            -   Printing support improvement.
            -   Help improvement.
            -   Chromium browser complete support.
        -   Important:
            -   Limiting resources. New appropriative insertion algorithm.
            -   Resource levelling.
            -   Over allocation control.
            -   Heuristics in general allocations.
            -   Allocation functions (steps, S-curve) in simple allocation pop-up and some usability improvements.
        -   Minor:
            -   Violation of dependencies showed in Gantt.
            -   Default login auto-completion configuration.
            -   Tasks identification improvements in some reports.
        -   Delayable:
            -   Support of intraday operations. Possibility to establish not integer number of hours in allocations, task work (hours, minutes, seconds).
            -   Advance allocation fix.
-   Rough estimation for version 1.2.
    -   Added some tasks for 1.2:
        -   Add export/import for different format files.
        -   Possibility to attach documentation to projects and tasks.
    -   Delayed some tasks to future:
        -   Monte Carlo simulation improvements.
