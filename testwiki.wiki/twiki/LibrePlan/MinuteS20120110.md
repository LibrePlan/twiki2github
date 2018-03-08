[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20120110](LibrePlan_MinuteS20120110 "Topic revision: 2 (20 Aug 2012 - 09:50:20)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20120110?t=1520343717 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20120110 "Attach an image or document to this topic")  

 LibrePlan Meeting 2012/01/10
=============================

-   Date: [January 10, 2012 at 16:30 CET (GMT +1)](http://www.timeanddate.com/worldclock/fixedtime.html?day=10&month=01&year=2012&hour=16&min=30&sec=0&p1=48)
-   Agenda: Coordination meeting
-   Log: `libreplan-coordination-meeting-20120110.txt`

 Minutes
--------

-   Previous meeting was canceled (2 weeks ago) because of there were very few people present and most of us were on holidays somehow. A mail was sent to -devel mailing list: <http://sourceforge.net/mailarchive/forum.php?thread_name=4EF9F015.2080606%40igalia.com&forum_name=libreplan-devel>

&nbsp;

-   Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Fixed lots of bugs: \#1291, \#1290, \#1287, \#1296, \#1073, \#1303, \#1300, \#1314, \#1301, \#1305, \#1308, \#1307, \#1288, \#1309, \#1319, \#1323, \#1321, \#1325, \#1326, \#1327, \#1328
        -   New document about how to develop LibrePlan in Eclipse: <http://www.libreplan.org/howto-start-development-with-eclipse.html>
        -   Fix tests in Debian Wheezy (postgres 9.1.2)
        -   Rename project in [SourceForge.net](https://sourceforge.net/projects/libreplan/) (repository, mailing lists, ...)
        -   Created a new folder with links to documentation that is automatically updated in libreplan.org
        -   Working on bug \#1295. I have a possible patch applied in the demo to see if it fix the issues in database (once this is fixed we should release LibrePlan 1.2.1)
        -   Propose to change tags format in commits and start to use "XXX:" instead of "\[XXX\]" (updated info in [documentation section](LibrePlan_Documentation#Commit_Messages_Format))
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   General patch review
        -   Bugfixing
        -   Manage the release of the new version 1.2.1

&nbsp;

-   Jacobo
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Fixed: 1316, 1311, 1310, 1304, 1299, 1297, 1294, 1292 (according to bugzilla search tool)
        -   Worked on bugs related with the size of the bars on the Gantt, size of orders, and size of progress bars
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Bugfixing

&nbsp;

-   Javichan
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Analysis:
            -   Sent an analysis mail about consolidation: <http://sourceforge.net/mailarchive/message.php?msg_id=28565283>
            -   Analysed part of the corrections needed in order that machine configuration units works in the application Three analysis stories created:
                -   [AnA17S01ConfigurationUnitInterfaceCorrections](LibrePlan_AnA17S01ConfigurationUnitInterfaceCorrections)
                -   [AnA17S02TakingIntoAccountDerivedDayAssigments](LibrePlan_AnA17S02TakingIntoAccountDerivedDayAssigments)
                -   [AnA17S03EnforceDerivedDayAssignmentsWithAllocations](LibrePlan_AnA17S03EnforceDerivedDayAssignmentsWithAllocations)
        -   Tested the application and reported several bugs: \#1321, \#1322, \#1323, \#1324, \#1325, \#1326, \#1327, \#1328, \#1329, \#1330
        -   Holidays during week 52
        -   Closed former iteration and opened the new one [ItEr76Week01To33](LibrePlan_ItEr76Week01To33) (WARNING: from now on please use the new iteration)
        -   Helped with some complex bugs to Rego (mainly bug \#1295)
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Analysis for Susana
        -   Translate LibrePlan website into Spanish
        -   Test application
        -   Finish to prepare roadmap meeting

&nbsp;

-   Susana
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   On holidays and working in other projects during this period
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Maybe help with some bugfixing
        -   Carry on with some tasks related to subcontracting system once Javichan analyze them
        -   Update subcontracting remote branch with master contents

&nbsp;

-   Loren
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Some slight bugfixing
        -   Playing with functional testing and screencast generation
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Upgrade website to next TYPO3 version in order to fix some issues
        -   Bugfixing

&nbsp;

-   Nacho Barrientos
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   On holidays so nothing to highlight here
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Review pending patches for KPIs
        -   Carry on with KPIs
        -   Help in some sysadmin tasks if needed

&nbsp;

-   Tomorrow we will have the coordination meeting to debate about the features to be included in the next release.
