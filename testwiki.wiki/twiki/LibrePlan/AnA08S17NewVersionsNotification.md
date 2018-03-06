[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA08S17NewVersionsNotification](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification "Topic revision: 1 (13 Jan 2012 - 14:24:18)") (13 Jan 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA08S17NewVersionsNotification?t=1520337848 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S17NewVersionsNotification "Attach an image or document to this topic")

 [AnA08S17NewVersionsNotification](/twiki/LibrePlan/AnA08S17NewVersionsNotification)
===============================================================================================================================================



|                        |                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------|
| Story summary          | System to notify users about new versions being published                                    |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)                                   |
| FEA                    | [AnA08S17NewVersionsNotification](/twiki/LibrePlan/AnA08S17NewVersionsNotification) |
| Story Lead             |                                                                                              |
| Next Story             |                                                                                              |
| Passed acceptance test | No                                                                                           |

###  Tasks



####  Show notification to admins when a new version is released

This tasks consist to implement a new warning in LibrePlan to notify users with **Administration** profile about new versions being released.

In order to do this we will need to follow the following steps:

-   Create a new file `VERSION`
    -   This will be a simple text file with the full number of current version. Right now it will have the next string: `1.2.0`
    -   This file will be accessible at `http://www.libreplan.org/VERSION` (simply add a link to this file in `www` folder at LibrePlan repo)
-   Show the notification message
    -   Message text when a new version is be available will be the following:

            A new version of LibrePlan is avilable. Please check next link for more information: http://www.libreplan.com/download/

    -   The idea is to show a warning only to users with **Administrator** profile
    -   The warning will be placed at LibrePlan footer (like the warning about default passwords)
    -   Warning behavior:
        -   It always checks the URL of file VERSION on LibrePlan startup
        -   If you're running and older version of LibrePlan
            -   It stores a cached value and show the warning
            -   URL is not going to be checked anymore (until you restart LibrePlan on that machine) as we already now that you're running an old version and we can show the warning (when you install a new version LibrePlan is restarted so there isn't any issue with this approach)
        -   If you're running the last version of LibrePlan
            -   It stores the cached value accordingly
            -   The URL will be checked again 1 day later (or when you restart LibrePlan on that machine)



####  Add option to disable notification

Maybe some people doesn't want to enjoy this feature. We should add a new option in configuration to disable it. This option will be set to `TRUE` by default.

Steps:

-   Add new field `checkNewVersionEnabled` to `Configuration` entity
-   Modify configuration window to show this new option and a checkbox to enable/disable it with the following text:

        Check for updates: [X] Show a notification when new LibrePlan versions are released
        Tooltip text: Enable/Disable warning about new LibrePlan versions available

-   Don't show warning if that option is disabled



####  Add option to request permissions to collect stats

As we're going to use the request to `http://www.libreplan.org/VERSION` to know how many people is using LibrePlan, in order to be kind, we should ask for permission to the users to collect that data.

We'll add a new option in configuration to give us permissions to collect data as usage stats. This option will be set to `FALSE` by default.

Steps:

-   Add new field `allowToGatherUsageStatsEnabled` to `Configuration` entity
-   Modify configuration window to show a new checkbox inside \*Warning new version" option to enable/disable it with the following text:

        [ ] Help project developers to collect information about which LibrePlan version you are using
        Tooltip: Check this option to send this information to LibrePlan developers in order to generate usage statistics

-   If that option is marked pass as GET parameters `stats=1` in the request. The complete URL will be to `http://www.libreplan.org/VERSION?stats=1`
-   We're going to take advantage to send too LibrePlan version in another GET param `version=1.2.0`. So the final URL would be something like this: `http://www.libreplan.org/VERSION?stats=1&version=1.2.0`

###  User stoties

-   [ItEr76S10NewVersionsNotification](/twiki/LibrePlan/ItEr76S10NewVersionsNotification)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S17NewVersionsNotification?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                             | 3                                                                                                                                                              | 3                                                                                                                                                                | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                        | [Show notification to admins when a new version is released](/twiki/LibrePlan/AnA08S17NewVersionsNotification#TasK1)                                        |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |
| Task                                                                                                                                                             | 2                                                                                                                                                              | 2                                                                                                                                                                | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                        | [Add option to disable notification](/twiki/LibrePlan/AnA08S17NewVersionsNotification#TasK2)                                                                |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |
| Task                                                                                                                                                             | 2                                                                                                                                                              | 2                                                                                                                                                                | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                        | [Add option to request permissions to collect stats](/twiki/LibrePlan/AnA08S17NewVersionsNotification#TasK3)                                                |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |


