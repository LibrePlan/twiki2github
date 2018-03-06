[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S23ImproveFilteringArea](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea "Topic revision: 4 (20 Aug 2012 - 09:50:18)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S23ImproveFilteringArea?t=1520337940 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S23ImproveFilteringArea "Attach an image or document to this topic")

 [ItEr76S23ImproveFilteringArea](/twiki/LibrePlan/ItEr76S23ImproveFilteringArea)
=========================================================================================================================================



|                        |                                                                                          |
|------------------------|------------------------------------------------------------------------------------------|
| Story summary          | Improve filtering area in resource load view                                             |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                           |
| FEA                    | [ItEr76S23ImproveFilteringArea](/twiki/LibrePlan/ItEr76S23ImproveFilteringArea) |
| Story Lead             |                                                                                          |
| Next Story             |                                                                                          |
| Passed acceptance test | No                                                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Added the possibility to filter by criteria in the bandbox search.

This was using a finder called `WorkerMultipleFiltersFinder` that has been changed and renamed to `ResourceFilterEnumByResourceAndCriterion`.

Moreover, previous finder only look for Workers but the new one look for any kind of Resource (Worker, Machine and VirtualWorker).

-- [ManuelRego](/twiki/Main/ManuelRego) - 11 Apr 2012

Now you don't need to click the filter button as the event listener has been added to the bandbox too. So, the **filter button has been removed** as it was not useful (nothing changes after click it as filter was already applied while selecting the options).

-- [ManuelRego](/twiki/Main/ManuelRego) - 13 Apr 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=7;table=2;up=0#sorted_table "Sort by this column")       | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                           | 5                                                                                                                                                            | 5.75                                                                                                                                                           | 0                                                                                                                                                              | Low                                                                                                                                                           | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                   | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                      | [Implement new filtering option in resource load view (company and per project) in show by resources mode](/twiki/LibrePlan/AnA09S02ImproveFilteringArea#TasK1) |                                                                                                                                                                     |                                                                                                                                                                       |                                                                                                                                                                    |
| Task                                                                                                                                                           | 3                                                                                                                                                            | 0.5                                                                                                                                                            | 0                                                                                                                                                              | Low                                                                                                                                                           | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                   | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                      | [Change the order and labels of the filtering area](/twiki/LibrePlan/AnA09S02ImproveFilteringArea#TasK2)                                                        |                                                                                                                                                                     |                                                                                                                                                                       |                                                                                                                                                                    |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S23ImproveFilteringArea?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                 | 6.25                                                                                                                                                                        | 0                                                                                                                                                                           | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                            |
| Total                                                                                                                                                         | 6.25                                                                                                                                                                        | 0                                                                                                                                                                           | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                            |

------------------------------------------------------------------------
