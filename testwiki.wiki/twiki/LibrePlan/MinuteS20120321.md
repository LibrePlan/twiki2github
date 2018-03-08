[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20120321](LibrePlan_MinuteS20120321 "Topic revision: 1 (21 Mar 2012 - 16:38:33)") (21 Mar 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20120321?t=1520343718 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20120321 "Attach an image or document to this topic")  

 LibrePlan Meeting 2012/03/21
=============================

-   Date: March 21, 2012 at 16:30 CET (GMT +1)
-   Agenda: Coordination meeting
-   Log: `libreplan-coordination-meeting-20120321.txt`

 Minutes
--------

-   Susana Montes
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Updated subcontracting branch against master to have up to date
        -   Started to fix pending issues in that branch
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Continue fixing pending issues in subcontracting branch

&nbsp;

-   Manuel Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Uploaded French and Dutch translations
        -   Fixed bugs: \#1393, \#1394, \#1397 and \#1398
        -   Added a new Maven profile called "i18n" to save compilation time
        -   Released [LibrePlan](LibrePlan_LibrePlan) 1.2.2
        -   Worked in [ItEr76S17MoneyCostMonitoringSystem](LibrePlan_ItEr76S17MoneyCostMonitoringSystem). The task consits in add a new field budget in OrderElement[?](LibrePlan_OrderElement?topicparent=LibrePlan.MinuteS20120321 "Create this topic") and use it to show a new progress bar in the Gantt (taking into account the money spent and the task budget)
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   General patch review and bugfixing
        -   Finish [ItEr76S17MoneyCostMonitoringSystem](LibrePlan_ItEr76S17MoneyCostMonitoringSystem)
        -   Start to work in a new task for 1.3: [ItEr76S14ConcurrencyProblemWorkReports](LibrePlan_ItEr76S14ConcurrencyProblemWorkReports)

&nbsp;

-   Manuel Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Uploaded French and Dutch translations
        -   Fixed bugs: \#1393, \#1394, \#1397 and \#1398
        -   Added a new Maven profile called "i18n" to save compilation time
        -   Released [LibrePlan](LibrePlan_LibrePlan) 1.2.2
        -   Worked in [ItEr76S17MoneyCostMonitoringSystem](LibrePlan_ItEr76S17MoneyCostMonitoringSystem). The task consits in add a new field budget in OrderElement[?](LibrePlan_OrderElement?topicparent=LibrePlan.MinuteS20120321 "Create this topic") and use it to show a new progress bar in the Gantt (taking into account the money spent and the task budget)
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   General patch review and bugfixing
        -   Finish [ItEr76S17MoneyCostMonitoringSystem](LibrePlan_ItEr76S17MoneyCostMonitoringSystem)
        -   Start to work in a new task for 1.3: [ItEr76S14ConcurrencyProblemWorkReports](LibrePlan_ItEr76S14ConcurrencyProblemWorkReports)

&nbsp;

-   Jacobo Aragunde
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   [LibrePlan](LibrePlan_LibrePlan) 1.2.2 release:
            -   Started doing the standard tests but I stopped because of some bugs found
            -   Tested and applied patches for RPM packaging
        -   Bugfixing:
            -   Reported \#1386, \#1387, \#1391
            -   Testing one of idiazt patches to help him with a bug with ZK validation; I couldn't fix it, I suspect it's a bug in the framework
            -   Fixed \#1382 (deadlines on tasks not being saved).
            -   Fixed \#1390 (a regression in task assignment).
            -   Commited a patch to partially fix \#1387 (problem with scheduling points).
            -   Working on \#1387, it's quite complex.
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Start working on features for 1.3
        -   Bugfixing

&nbsp;

-   Javi Morán
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Answered several messages in the forum
        -   Tested the a application for the 1.2.2 release
        -   Filled several bugs thanks to this testing
        -   Had some coordination and analysis meeting with some of you
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Carry on with analysis for 1.3
        -   Testing

&nbsp;

-   Nacho Díaz
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Sent some patches two weeks ago and I need to fix some of them
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Fix issues in these bugs
        -   Start with task [AnA08S15WorkReports\#TasK1](LibrePlan_AnA08S15WorkReports#TasK1)

&nbsp;

-   Loren Tilve
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Collaborated in the 1.2.2 release
        -   Still have some minor fix I'm pushing now on master and 1.2 regarding showing companies in subcontracted tasks
        -   Worked with Javi Morán in the technical design and implementation in audiovisual branch
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Keep working in the audiovisual branch

&nbsp;

-   Javier Toja
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Tried to do some performance tests (load, bandwidth, ...). Using jmeter (maybe some info could be found at [ItEr74S08DeployFramework](LibrePlan_ItEr74S08DeployFramework) and [ItEr75S19DeployFrameworkItEr74S08](LibrePlan_ItEr75S19DeployFrameworkItEr74S08))
        -   Started to use Apache CXF but some work pending yet
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Carry on with the performance tests
        -   Review the issues with Apache CXF

&nbsp;

-   Apart from that, Jeroen Baten has sent a script to send data from JIRA (<http://www.atlassian.com/software/jira/overview>) to LibrePlan. He will send a README file explaining how to use the script and it will be uploaded under `scripts/` folder in LibrePlan repository.
