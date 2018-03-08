[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S05CalendarAdminInterfaceItEr74S06](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06 "Topic revision: 7 (03 Jan 2012 - 13:16:56)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?t=1520343676 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S05CalendarAdminInterfaceItEr74S06 "Attach an image or document to this topic")  

 [ItEr75S05CalendarAdminInterfaceItEr74S06](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06)
===============================================================================================

|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Calendar administration interface refactoring                                                  |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                                                 |
| FEA                    | [ItEr75S05CalendarAdminInterfaceItEr74S06](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

A new constraint when adding a work week which it was not specified in the previous specification. If the new work week includes whole another week, causing that this one is overwritten:

use case: DA \[ - \] \[ 10 \] DB \[ 11 \] \[ 20 \] DC \[ 21 \] \[ 30 \]

and adding \[ 11 \] \[ 26 \]

DA \[ - \] \[ 10 \] DB --&gt; is removed DN \[11\]\[26\] DC \[27\]\[30\]

the system does not must permit this operation and let the user remove or update handy the work week in the work weeks list.

-- [SusanaMontes](Main_SusanaMontes) - 20 Jun 2011

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                  | 3                                                                                                                   | 12                                                                                                                    | 0                                                                                                                     | Low                                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                                          | [SusanaMontes](Main_SusanaMontes)                                                                                         | [Corrections in calendars listing](LibrePlan_AnA08S09CalendarAdminInterface#TasK4)                                        |                                                                                                                            |                                                                                                                              |                                                                                                                           |
| Task                                                                                                                  | 2                                                                                                                   | 8                                                                                                                     | 0                                                                                                                     | Low                                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                                          | [SusanaMontes](Main_SusanaMontes)                                                                                         | [Change the format of the summary work week line in work weeks table](LibrePlan_AnA08S09CalendarAdminInterface#TasK5)     |                                                                                                                            |                                                                                                                              |                                                                                                                           |
| Task                                                                                                                  | 2                                                                                                                   | 10                                                                                                                    | 0                                                                                                                     | Low                                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                                          | [SusanaMontes](Main_SusanaMontes)                                                                                         | [Change layout in calendars](LibrePlan_AnA08S09CalendarAdminInterface#TasK6)                                              |                                                                                                                            |                                                                                                                              |                                                                                                                           |
| Task                                                                                                                  | 2                                                                                                                   | 4                                                                                                                     | 0                                                                                                                     | Low                                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                                          | [SusanaMontes](Main_SusanaMontes)                                                                                         | [Create default work week of non-derived calendar](LibrePlan_AnA08S09CalendarAdminInterface#TasK7)                        |                                                                                                                            |                                                                                                                              |                                                                                                                           |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S05CalendarAdminInterfaceItEr74S06?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](Main_SusanaMontes)                                                                                    | 34                                                                                                                                 | 0                                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                   |
| Total                                                                                                                | 34                                                                                                                                 | 0                                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                   |

------------------------------------------------------------------------
