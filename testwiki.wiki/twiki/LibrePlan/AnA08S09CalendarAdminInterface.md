[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA08S09CalendarAdminInterface](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface "Topic revision: 8 (16 Jun 2011 - 14:37:27)") (16 Jun 2011, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA08S09CalendarAdminInterface?t=1520337845 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S09CalendarAdminInterface "Attach an image or document to this topic")

 [AnA08S09CalendarAdminInterface](/twiki/LibrePlan/AnA08S09CalendarAdminInterface)
============================================================================================================================================



|                        |                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------|
| Story summary          | Calendar administration interface refactoring                                              |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)                                 |
| FEA                    | [AnA08S09CalendarAdminInterface](/twiki/LibrePlan/AnA08S09CalendarAdminInterface) |
| Story Lead             |                                                                                            |
| Next Story             |                                                                                            |
| Passed acceptance test | No                                                                                         |

###  Tasks



####  Refactoring calendar interface to include some usability improvements

The changes to introduce are the following:

-   **Move parameters to popup on creating new work week**. When you press the button *create new work week* the parameter ***Derived from*** and ***valid from to*** must be asked only in a popup. Improve the pop-up style. **Add secon level table column groups**. This is for columns *Normal effort* and *Extra effort*.
-   **Extra effort combo** Add a combo to get the hours of the extra effort.
-   **Remove heredated from parent calendars**. Change the work for *inherited*.
-   \*Fill with default values the fields valid data and valid until in each calendar period.
-   **Ask [OscarGonzalez](/twiki/Main/OscarGonzalez) the impact of removing seconds in interface level for calendars**.
-   **Titles, widths, and tooltips in table headers**
-   **Explore the possiblity of changing the layout with the calendar widget in the upper side of the screen**.
-   **Introduce save and continue button**



####  Change pop-up to create new work week

Change the pop-up for one with better layout. Add to it the following components:

-   The derived calendar. In case you are creating a work week for a derived calendar. A base calendar cannot have work weeks derived fron any other calendar.
-   Add the **Valid from**
-   Add the **Valid until**

In the list of work weeks do editable the start date (valid from) and the end date (valid until).

If you are creating a new work week or you are changing the start date or end date of a work week, do the following checks and forbide the operation if they are not passed:

-   The start date is mandatory for all the work weeks except the first.
-   The end date is mandatory for all the work week except the last.
-   If the work week being created ot the work week being edited is the firt one (sorte from oldest to newest) start date is not allowed. Give an informative message saying this.
-   If the work week being created or the work week being edited is the last one (sorted from oldest to newest) the end date is not allowed. Give an informative message saying this.
-   If there is only a work week it cannot have, therefor, start date and end date.
-   If the work week being modified or the one created includes inside any other work week, an error message must be showed.
-   If the work week being created is intersecting two work weeks do the following changes:
    -   \[SDA - SEA\]\[SDB-SEB\]
    -   It is created \[SDC-SEC\]
    -   The result is: \[SDA-SDC-1\]\[SDC-SEC\]\[SCE+1-SEB\]
-   Changing the end date of a work week: Adapt the start date of the following work week.
-   Changing the start date of a work week: Adapt the end date of the work week before.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) Do unit tests for each case.



####  Allow to change derived calendar in work week table

It is possible to change the derived calendar of a work week from calendar which were created derivating from others. Now, the way to change the derived calendar of a work week will be with a combo in the work week table.

A label will appear instead of this combo in the non derived calendards. Make sure than on changing the base calendar the table is reloaded.



####  Corrections in calendars listing

Change the calendars listings in the following way:

-   Now it is showed a derived calendar bellow the calendar its last work week derives for. A better idea would be to see the current date and show the derived calendar as soon of the calendar in which the work week of the current date is deriving from.
-   Change the list adding to new columns: *From Date* and *Up to date*. These columns will show the start date and the end date of the work week to which the current date belongs.



####  Change the format of the summary work week line in work weeks table.

Add for each day the following syntax: AA:BB (XX:YY) Include always the minutes although they are zero.



####  Change layout in calendars

Test to include the right table for work weeks and exceptions bellow.

Include a title line informing about what it is each table:

-   Exceptions list.
-   Work weeks list.



####  Create default work week of non-derived calendar

When you create a new calendar, non derived, it is created by default a work week of:

-   Monday: 8h (0h extra)
-   Tuesday: 8h (0h extra)
-   Wednesday: 8h (0h extra)
-   Thursday: 8h (0h extra)
-   Friday: 8h (0h extra)
-   Saturday: 0h (0h extra)
-   Monday: 0h (0h extra)

However, on creating a new work week over a calendar non derivated it is created with 0h in all days. Use the default week above for the new work weeks of non-derived calendars.

###  User stories

-   [ItEr69S09CalendarAdminInterface](/twiki/LibrePlan/ItEr69S09CalendarAdminInterface)
-   [ItEr70S07CalendarAdminInterfaceItEr69S09](/twiki/LibrePlan/ItEr70S07CalendarAdminInterfaceItEr69S09)
-   [ItEr72S06CalendarAdminInterfaceItEr70S07](/twiki/LibrePlan/ItEr72S06CalendarAdminInterfaceItEr70S07)
-   [ItEr74S06CalendarAdminInterfaceItEr73S06](/twiki/LibrePlan/ItEr74S06CalendarAdminInterfaceItEr73S06)
-   [ItEr75S05CalendarAdminInterfaceItEr74S06](/twiki/LibrePlan/ItEr75S05CalendarAdminInterfaceItEr74S06)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                            | 10                                                                                                                                                            | 2.5                                                                                                                                                             | 7.5                                                                                                                                                             | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                                   | [Refactoring calendar interface to include some usability improvements](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK1)                             |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 7                                                                                                                                                             | 0                                                                                                                                                               | 7                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Change pop-up to create new work week](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK2)                                                             |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 2                                                                                                                                                             | 0                                                                                                                                                               | 2                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Allow to change derived calendar in work week table](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK3)                                               |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 2                                                                                                                                                             | 0                                                                                                                                                               | 2                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Allow to change derived calendar in work week table](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK3)                                               |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 3                                                                                                                                                             | 0                                                                                                                                                               | 3                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Corrections in calendars listing](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK4)                                                                  |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 2                                                                                                                                                             | 0                                                                                                                                                               | 2                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Change the format of the summary work week line in work weeks table](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK5)                               |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 2                                                                                                                                                             | 0                                                                                                                                                               | 2                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Change layout in calendars](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK6)                                                                        |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 2                                                                                                                                                             | 0                                                                                                                                                               | 2                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                         | [Create default work week of non-derived calendar](/twiki/LibrePlan/AnA08S09CalendarAdminInterface#TasK7)                                                  |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S09CalendarAdminInterface?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                              | 2.5                                                                                                                                                                          | 0                                                                                                                                                                            | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                             |
| [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                    | 0                                                                                                                                                                            | 0                                                                                                                                                                            | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                              |
| Total                                                                                                                                                          | 2.5                                                                                                                                                                          | 0                                                                                                                                                                            | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                             |

------------------------------------------------------------------------
