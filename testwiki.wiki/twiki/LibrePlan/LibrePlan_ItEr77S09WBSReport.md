[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr77S09WBSReport](LibrePlan_ItEr77S09WBSReport "Topic revision: 9 (25 Oct 2012 - 10:23:03)") (25 Oct 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr77S09WBSReport?t=1520343704 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S09WBSReport "Attach an image or document to this topic")  

 [ItEr77S09WBSReport](LibrePlan_ItEr77S09WBSReport)
===================================================

|                        |                                                    |
|------------------------|----------------------------------------------------|
| Story summary          | WBS Report                                         |
| Iteration              | [ItEr77Week34To44](LibrePlan_ItEr77Week34To44)     |
| FEA                    | [ItEr77S09WBSReport](LibrePlan_ItEr77S09WBSReport) |
| Story Lead             |                                                    |
| Next Story             |                                                    |
| Passed acceptance test | No                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Created the new report with the required information.

The tasks in the report has been indented adding extra spaces depending on the depth in the tasks tree. Adding 4 spaces as prefix for each level.

-- [ManuelRego](Main_ManuelRego) - 11 Sep 2012

Included new columns and parameters in the report with information about costs.

-- [ManuelRego](Main_ManuelRego) - 16 Oct 2012

Implemented filtering by labels and criteria.

Only the tasks with the direct assignments are shown. In each case it works different:

-   Labels: Only tasks with label directly assigned is shown. Inherited labels are not used.
-   Criteria: Only tasks with criterion directly assigned is used. Indirect criteria is only used if it's deactivated to discount the value in the parent task to be shown.

For the last developments a new remote branch called `project-status-report` is being used. Lately, it'll be merged into master and published in the next minor version.

-- [ManuelRego](Main_ManuelRego) - 22 Oct 2012

Filter by project is now optional, however you have to choose at least one project or label or criterion to generate the report. You cannot generate a report for all the tasks in [LibrePlan](LibrePlan_LibrePlan).

If you don't chose a project the report header will be changed and it'll show the filter instead.

An exclamation mark has been added in the columns *imputed hours* and *total cost* in order to highlight if you're exceeding your estimation in hours or money.

-- [ManuelRego](Main_ManuelRego) - 23 Oct 2012

Created query to get the list of `OrderElements` with the assigned labels and/or criteria, when it's not selected any project. This will avoid to load all the projects when you're only filtering by labels and/or criteria.

-- [ManuelRego](Main_ManuelRego) - 24 Oct 2012

This development is merged now into `master`.

-- [ManuelRego](Main_ManuelRego) - 25 Oct 2012

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

| [Tasks](LibrePlan_ItEr77S09WBSReport?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr77S09WBSReport?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr77S09WBSReport?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr77S09WBSReport?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr77S09WBSReport?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr77S09WBSReport?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr77S09WBSReport?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr77S09WBSReport?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr77S09WBSReport?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr77S09WBSReport?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr77S09WBSReport?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| Task                                                                                            | 10                                                                                            | 3.5                                                                                             | 0                                                                                               | Low                                                                                            | [ManuelRego](Main_ManuelRego)                                                                      | [ManuelRego](Main_ManuelRego)                                                                       | [New WBS report with information about hours](LibrePlan_AnA22S02WBSReport#TasK1)                    |                                                                                                      |                                                                                                        |                                                                                                     |
| Task                                                                                            | 5                                                                                             | 4.5                                                                                             | 0                                                                                               | Low                                                                                            | [ManuelRego](Main_ManuelRego)                                                                      | [ManuelRego](Main_ManuelRego)                                                                       | [Include cost information in the report](LibrePlan_AnA22S02WBSReport#TasK2)                         |                                                                                                      |                                                                                                        |                                                                                                     |
| Task                                                                                            | 7                                                                                             | 7.75                                                                                            | 0                                                                                               | Low                                                                                            | [ManuelRego](Main_ManuelRego)                                                                      | [ManuelRego](Main_ManuelRego)                                                                       | [Include filter by criteria and labels in the report](LibrePlan_AnA22S02WBSReport#TasK3)            |                                                                                                      |                                                                                                        |                                                                                                     |
| Task                                                                                            | 7                                                                                             | 7.75                                                                                            | 0                                                                                               | Low                                                                                            | [ManuelRego](Main_ManuelRego)                                                                      | [ManuelRego](Main_ManuelRego)                                                                       | [Make optional filter by projects](LibrePlan_AnA22S02WBSReport#TasK4)                               |                                                                                                      |                                                                                                        |                                                                                                     |
