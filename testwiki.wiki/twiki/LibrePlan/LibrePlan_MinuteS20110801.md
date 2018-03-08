[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20110801](LibrePlan_MinuteS20110801 "Topic revision: 3 (20 Aug 2012 - 09:52:57)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20110801?t=1520343713 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20110801 "Attach an image or document to this topic")  

 LibrePlan Meeting 2011/08/01
=============================

-   Date: [August 1, 2011 at 12:00 CEST (GMT +2)](http://www.timeanddate.com/worldclock/fixedtime.html?day=1&month=8&year=2011&hour=12&min=0&sec=0&p1=48)
-   Agenda: Coordination meeting
-   Log: `navalplan-coordination-meeting-20110801.txt`

 Minutes
--------

-   Introduced Nacho Barrientos to the community. He's a new igalian and it's going to work in [ItEr75S19DeployFrameworkItEr74S08](LibrePlan_ItEr75S19DeployFrameworkItEr74S08) during next weeks.

&nbsp;

-   Review tasks of every developer:
    -   Rego
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Bug \#1180 which implied release a new version 1.1.2
            -   Helped Cristina to finish some topics in task [ItEr75S14ShowInformationEditedEntity](LibrePlan_ItEr75S14ShowInformationEditedEntity) (13 controllers are extending BaseCRUDController)
                -   Adapted scenarios and criteria to BaseCRUDController
                -   Implemented a particular solution for special cases: workers/virtual workers and calendars
                -   It's still pending update development documentation to use BaseCRUDController
            -   Bugfixing: \#1116 (a new progress type appeared) and \#1117 (problem with server language)
            -   Helped Susana to finally close earned value bug \#1088
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Patches review
            -   Some bugfixing
            -   Try to start "fix allocation model" task from roadmap
    -   Nacho Díaz
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Started [ItEr75S15FilteringByLabelsPlanningGantt](LibrePlan_ItEr75S15FilteringByLabelsPlanningGantt) (Rego helped with a CSS issue)
            -   Not too many advance in the filtering part (less time than expected due to office movement)
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Keep working in this task
    -   Cristina
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Adapted WorkReportType to BaseCRUDController
            -   Bugfixing:
                -   \[Bug \#1115\] DataIntegrityViolationException saving a Cost Category with repeated name (already closed)
                -   \[Bug \#1111\] There are several problems with this report: Task Scheduling Status In Project (pending to send a patch)
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Keep working on different bugs
    -   Óscar
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Worked in [ItEr75S11PreventLooseChanges](LibrePlan_ItEr75S11PreventLooseChanges)
                -   Unified the state of gantt, resourceload and advanced allocation perspectives
                -   Resource load was harder than expected, due to having to handle scenarios
                -   Still working in WBS part
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Keep working in this task
            -   Note down some ideas about future improvements related to this task
            -   Help Rego with fix advanced allocation task
    -   Susana
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Finished [ItEr75S05CalendarAdminInterfaceItEr74S06](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06)
            -   Finished [ItEr75S09ImproveBandboxFinders](LibrePlan_ItEr75S09ImproveBandboxFinders) too (pending to be reviewed by Javichan)
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Not work during next weeks
    -   Pablo
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Review application doing training exercises
            -   Done some automatic functional tests (with SAHI) for 2 data types: Criteria and Progress Types
            -   Reported some bugs
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Carry on with functional tests
            -   Tests should be pushed upstream in a new folder with basic information to running them
    -   Nacho Barrientos
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Read developer and user documentation
            -   Play with LibrePlan to have a general overview of the application
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Work in stress load tests ([ItEr75S19DeployFrameworkItEr74S08](LibrePlan_ItEr75S19DeployFrameworkItEr74S08))
            -   Investigate possible issues with jmeter and AJAX
    -   Loren
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Fix ZK 5 layout issues ([ItEr75S08MigrationZK5](LibrePlan_ItEr75S08MigrationZK5))
            -   Try to replace some components to depend on ZK5 CE
    -   Javichan
        -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
            -   Helping and answering people from the community
            -   Tested application
            -   Done analysis about WBS task name and Gantt task name
            -   Written some website contents
        -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
            -   Continue with website contents
            -   Testing and analisys

&nbsp;

-   Finally Rego introduced a new point about the roadmap
    -   This week is planned as feature freeze in the roadmap, so from next week on only bugfixing and not new tasks should be added in master
    -   We'll have 4 weeks testing period before the release (as we're in summer some people is going to be on holidays for sure)
    -   We agree on finish in master the following features:
        -   ZK5 migration (WIP)
        -   Prevent lose changes changing perspective (WIP)
        -   FIx advanced allocation model (to be started during next weeks)
    -   The rest of things to be done in master are going to be just bufixing, if a new feature appears we'll discuss it in detail but on the first sight it should have a new remote branch
    -   The rest of tasks from the roadmap should be moved to future releases

&nbsp;

-   To close the meeting Javichan encourage the rest of the people to write more comments in the wiki and mark tasks as closed when finished
