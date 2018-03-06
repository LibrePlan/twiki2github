[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr63S05PerformanceOrderEdition](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition "Topic revision: 2 (09 Nov 2010 - 09:06:45)") (09 Nov 2010, [JacoboAragunde](/twiki/Main/JacoboAragunde))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr63S05PerformanceOrderEdition?t=1520337881 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr63S05PerformanceOrderEdition "Attach an image or document to this topic")

 [ItEr63S05PerformanceOrderEdition](/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Increase performance in order edition window                                                   |
| Iteration              | [ItEr63week45To46](/twiki/LibrePlan/ItEr63week45To46)                                 |
| FEA                    | [ItEr63S05PerformanceOrderEdition](/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

After some trial-and-error, I found that the reason why the tree sends the full page instead of the affected event every time there is a modification: the option `mold="paging"`. When paging is activated, all the elements of the page are sent because ZK has to calculate which ones have to be shown and which not. Without paging there isn't such a problem because all elements are shown.

Since it could be very difficult to modify this behaviour, we decided to go for a different approach: remove most of the buttons in the operations row to speed up the rendering time of each row. They have been replaced by buttons on the top of the page, which act on the selected row.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 09 Nov 2010

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 10                                                                                                                                                              | 8                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                 | [Rendering of large orders with the tree widget.](/twiki/LibrePlan/AnA03S02PerformanceOrderEdition#TasK3)                                                    |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr63S05PerformanceOrderEdition?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | 8                                                                                                                                                                              | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |
| Total                                                                                                                                                            | 8                                                                                                                                                                              | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |

------------------------------------------------------------------------
