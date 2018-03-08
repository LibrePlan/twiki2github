[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20110829](LibrePlan_MinuteS20110829 "Topic revision: 3 (20 Aug 2012 - 09:52:57)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20110829?t=1520343714 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20110829 "Attach an image or document to this topic")  

 LibrePlan Meeting 2011/08/29
=============================

-   Date: [August 29, 2011 at 12:00 CEST (GMT +2)](http://www.timeanddate.com/worldclock/fixedtime.html?day=29&month=8&year=2011&hour=12&min=0&sec=0&p1=48)
-   Agenda: Coordination meeting
-   Log: `navalplan-coordination-meeting-20110829.txt`

 Minutes
--------

-   Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Week 33: Holidays
        -   Staring to work in fix allocation model task. Finally the new enum **AllocationType** is not created, you can read more info about the implementation in the story notes: [ItEr75S23FixAllocationModel](LibrePlan_ItEr75S23FixAllocationModel)
        -   Patch review
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish advanced allocation task
        -   Patch review
        -   Help with the new website if free time
-   Nacho Díaz
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Last weeks working on change work reports to EffortDuration: [ItEr75S22WortReportsEffortDuration](LibrePlan_ItEr75S22WortReportsEffortDuration)
            -   We're going to use a remote branch for this task
            -   All the changes are going to be done to EffortDuration instead of BigDecimal
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Work in a small task: [ItEr75S20RefactoringWorkReportWS](LibrePlan_ItEr75S20RefactoringWorkReportWS)
        -   Carry on with the change to EffortDuration
-   Cristina
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Fixing bugs: \#1114 (not reproducible pending of dump), \#1123 (pending to be reviewed), \#1143
        -   Reported bug \#1166
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Work on \#1166
        -   Keep fixing bugs
        -   Holidays from 1st to 19th of September
-   Loren
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Bugfixing related to graphical issues appeared after migration to ZK5
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Keep fixing these ZK5 issues
        -   Start to integrate the new LibrePlan logo in master
        -   Help with new website
-   Óscar
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Finished the unification of state on the load perspective (done some refactorings there)
        -   Working in unifiying the state with the WBS
        -   Fixed some bugs related to this task: \#1164 and \#1165
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Keep working in this task
        -   Help with some bugs for release 1.2 if needed
-   Pablo
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Finishes all *Administration / Management* tests
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Work in *Resources* tests
-   Nacho Barrientos
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   No time these weeks for the project
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   If any time we'll discuss the possible tasks
-   Jacobo
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   He'll have some time during next weeks to help Loren with some ZK5 issues related with jQuery in limiting resources
-   Other issues discussed in the meeting:
    -   We're late for the current plan for release 1.2, so we think that it's going to be delayed till week 38-39
    -   We've been working in LibrePlan website, we should have a draft ready for week 36 and start to gather feedback around it
    -   For LibrePlan 1.2 we're going to depend on ZKEE (as it's not possible to manage the migration to ZKCE). Migration to ZKCE should be done as maximum in LibrePlan 1.3