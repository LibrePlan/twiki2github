[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Meetings](LibrePlan_Meetings)&gt;[MinuteS20110620](LibrePlan_MinuteS20110620 "Topic revision: 2 (20 Aug 2012 - 09:52:56)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_MinuteS20110620?t=1520343712 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/MinuteS20110620 "Attach an image or document to this topic")  

 LibrePlan Meeting 2011/06/20
=============================

-   Date: [June 20, 2011 at 12:00 CEST (GMT +2)](http://www.timeanddate.com/worldclock/fixedtime.html?day=20&month=6&year=2011&hour=12&min=0&sec=0&p1=48)
-   Agenda: Coordination meeting
-   Log: `navalplan-coordination-meeting-20110620.txt`

 Minutes
--------

-   Rego
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Improved content of `README`, `INSTALL` and `HACKING` files. Now with info about how to install in Debian, Ubuntu or openSUSE and how to compile in Debian, Ubuntu, openSUSE and Fedora.
        -   Get rid of Ruby for web services example scripts. Updated web services `README` file too.
        -   Prepared PPAs for Natty found an issue because of CutyCapt is already packaged in Natty (and also in Debian Sqeeze) and the command is `cutycapt` instead of `CutyCapt`. We should update LibrePlan to use the new command, and also update packages for Lucid and Maverick.
        -   Bugfixing: closed \#971 and \#1090
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Not too much time this week.
        -   Patch review and general bugfixing.

&nbsp;

-   Nacho
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   LDAP LibrePlan role matching, some patches pending.
        -   Realised that small patches are better to review and manage.
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish this week the role matching task.
        -   If more time available help Cristina with her task.

&nbsp;

-   Cristina
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Working on language configuration for users.
        -   Found a problem getting authentication user in the controller.
        -   New method for that: `org.navalplanner.web.security.SecurityUtils.getLoggedUser()`
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Keep working in those tasks.

&nbsp;

-   Óscar
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Working in ZK5 merge.
        -   Fixed some critical bugs: JavaScript issue changing zoom, JavaScript error moving tasks.
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish to try ZK5 and merge it in master.
        -   Document the user stress testing done in previous weeks.

&nbsp;

-   Susana
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Changing calendar interface to include some usability improvements.
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Finish this task.
        -   Some bugfixing if free time.

&nbsp;

-   Javichan
    -   ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
        -   Analysed task about user language and preferences.
        -   Sent mail about some Monte Carlo issues.
    -   ![todo.gif](/twiki/pub/TWiki/TWikiDocGraphics/todo.gif)
        -   Analyse more tasks for 1.2 release.
        -   Test and develop some of the features that are being developed.

&nbsp;

-   After that we reviewed a proposal by Óscar to send this info to the mailing list and avoid the meetings. But we think that sending the minutes and logs is enough. And 1h every 2 weeks is not too much.

&nbsp;

-   Next meeting will take place on July, the 4th.
