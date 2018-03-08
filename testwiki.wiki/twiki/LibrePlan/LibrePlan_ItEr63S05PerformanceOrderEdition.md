[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr63S05PerformanceOrderEdition](LibrePlan_ItEr63S05PerformanceOrderEdition "Topic revision: 2 (09 Nov 2010 - 09:06:45)") (09 Nov 2010, [JacoboAragunde](Main_JacoboAragunde))[Edit](LibrePlan_ItEr63S05PerformanceOrderEdition?t=1520343636 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr63S05PerformanceOrderEdition "Attach an image or document to this topic")  

 [ItEr63S05PerformanceOrderEdition](LibrePlan_ItEr63S05PerformanceOrderEdition)
===============================================================================

|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Increase performance in order edition window                                   |
| Iteration              | [ItEr63week45To46](LibrePlan_ItEr63week45To46)                                 |
| FEA                    | [ItEr63S05PerformanceOrderEdition](LibrePlan_ItEr63S05PerformanceOrderEdition) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

After some trial-and-error, I found that the reason why the tree sends the full page instead of the affected event every time there is a modification: the option `mold="paging"`. When paging is activated, all the elements of the page are sent because ZK has to calculate which ones have to be shown and which not. Without paging there isn't such a problem because all elements are shown.

Since it could be very difficult to modify this behaviour, we decided to go for a different approach: remove most of the buttons in the operations row to speed up the rendering time of each row. They have been replaced by buttons on the top of the page, which act on the selected row.

-- [JacoboAragunde](Main_JacoboAragunde) - 09 Nov 2010

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Entregables de código

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                          | 10                                                                                                          | 8                                                                                                             | 0                                                                                                             | Low                                                                                                          | [JavierMoran](Main_JavierMoran)                                                                                  | [JacoboAragunde](Main_JacoboAragunde)                                                                             | [Rendering of large orders with the tree widget.](LibrePlan_AnA03S02PerformanceOrderEdition#TasK3)                |                                                                                                                    |                                                                                                                      |                                                                                                                   |

###  Total Hours in this Story

| [User](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr63S05PerformanceOrderEdition?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [JacoboAragunde](Main_JacoboAragunde)                                                                        | 8                                                                                                                          | 0                                                                                                                          | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                           |
| Total                                                                                                        | 8                                                                                                                          | 0                                                                                                                          | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                           |

------------------------------------------------------------------------
