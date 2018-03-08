[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA10S01AdvanceAllocationFix](LibrePlan_AnA10S01AdvanceAllocationFix "Topic revision: 2 (07 Feb 2011 - 11:24:39)") (07 Feb 2011, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA10S01AdvanceAllocationFix?t=1520344055 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA10S01AdvanceAllocationFix "Attach an image or document to this topic")  

 [AnA10S01AdvanceAllocationFix](LibrePlan_AnA10S01AdvanceAllocationFix)
=======================================================================

|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | Advance allocation fix                                                 |
| Iteration              | [AnA10AdvanceAllocationWindow](LibrePlan_AnA10AdvanceAllocationWindow) |
| FEA                    | [AnA10S01AdvanceAllocationFix](LibrePlan_AnA10S01AdvanceAllocationFix) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

###  Tasks

####  Disable start/end dates changes in advance allocation to tasks

This task it to prevent dependency updates problems in advance allocation window on saving as a temporary solution before including in this window the dependency travel subsystem.

The steps to correct this are:

-   Forbide to add new cells in front of the start date and after the end date of a task.
-   Forbide to put to zero cells in a resource allocation if that change causes the start or end date of the task to change. Important to design how to implement this. Possible solutions:
    -   Not changing the start/end date if we put zeros after the start date or before the end date.
    -   Detecting when an edition causes the start/end date to be updated.

From the interface point of view the cells outside the interval of a task must be marked disabled and, inside a task, they must be edited but we have to control how to avoid the changes in the start date and end date (both for specific resource allocation / general resource allocation).

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) It is needed to take into account too the consolidated hours of a task. They are not changeable. ![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Now there are several things strange with the cell style: days before start day are not updatable however the days after the end are updatable, there is one day before the start day which is updatable. Fix these things properly.

###  User stories

-   [ItEr69S08AdvanceAllocationFix](LibrePlan_ItEr69S08AdvanceAllocationFix)

###  Tasks in this story

| [Tasks](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=7;table=2;up=0#sorted_table "Sort by this column")  | [Start Date](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task                                                                                                      | 7                                                                                                       | 7                                                                                                         | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [OscarGonzalez](Main_OscarGonzalez)                                                                           | [Disable start/end dates changes in advance allocation to tasks](LibrePlan_AnA10S01AdvanceAllocationFix#TasK1) |                                                                                                                |                                                                                                                  |                                                                                                               |

###  Total Hours in this Story

| [User](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA10S01AdvanceAllocationFix?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [OscarGonzalez](Main_OscarGonzalez)                                                                      | 7                                                                                                                      | 0                                                                                                                      | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                       |
| Total                                                                                                    | 7                                                                                                                      | 0                                                                                                                      | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                       |

------------------------------------------------------------------------
