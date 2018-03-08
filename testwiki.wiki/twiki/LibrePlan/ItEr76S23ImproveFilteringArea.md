[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr76S23ImproveFilteringArea](LibrePlan_ItEr76S23ImproveFilteringArea "Topic revision: 4 (20 Aug 2012 - 09:50:18)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr76S23ImproveFilteringArea?t=1520343698 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S23ImproveFilteringArea "Attach an image or document to this topic")  

 [ItEr76S23ImproveFilteringArea](LibrePlan_ItEr76S23ImproveFilteringArea)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Improve filtering area in resource load view                             |
| Iteration              | [ItEr76Week01To33](LibrePlan_ItEr76Week01To33)                           |
| FEA                    | [ItEr76S23ImproveFilteringArea](LibrePlan_ItEr76S23ImproveFilteringArea) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Added the possibility to filter by criteria in the bandbox search.

This was using a finder called `WorkerMultipleFiltersFinder` that has been changed and renamed to `ResourceFilterEnumByResourceAndCriterion`.

Moreover, previous finder only look for Workers but the new one look for any kind of Resource (Worker, Machine and VirtualWorker).

-- [ManuelRego](Main_ManuelRego) - 11 Apr 2012

Now you don't need to click the filter button as the event listener has been added to the bandbox too. So, the **filter button has been removed** as it was not useful (nothing changes after click it as filter was already applied while selecting the options).

-- [ManuelRego](Main_ManuelRego) - 13 Apr 2012

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

| [Tasks](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                                           | [Start Date](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 5                                                                                                        | 5.75                                                                                                       | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [ManuelRego](Main_ManuelRego)                                                                                  | [Implement new filtering option in resource load view (company and per project) in show by resources mode](LibrePlan_AnA09S02ImproveFilteringArea#TasK1) |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 3                                                                                                        | 0.5                                                                                                        | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [ManuelRego](Main_ManuelRego)                                                                                  | [Change the order and labels of the filtering area](LibrePlan_AnA09S02ImproveFilteringArea#TasK2)                                                        |                                                                                                                 |                                                                                                                   |                                                                                                                |

###  Total Hours in this Story

| [User](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr76S23ImproveFilteringArea?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                             | 6.25                                                                                                                    | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |
| Total                                                                                                     | 6.25                                                                                                                    | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |

------------------------------------------------------------------------
