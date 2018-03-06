[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S09WBSReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport "Topic revision: 9 (25 Oct 2012 - 10:23:03)") (25 Oct 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S09WBSReport?t=1520337946 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S09WBSReport "Attach an image or document to this topic")

 [ItEr77S09WBSReport](/twiki/LibrePlan/ItEr77S09WBSReport)
========================================================================================================



|                        |                                                                    |
|------------------------|--------------------------------------------------------------------|
| Story summary          | WBS Report                                                         |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)     |
| FEA                    | [ItEr77S09WBSReport](/twiki/LibrePlan/ItEr77S09WBSReport) |
| Story Lead             |                                                                    |
| Next Story             |                                                                    |
| Passed acceptance test | No                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Created the new report with the required information.

The tasks in the report has been indented adding extra spaces depending on the depth in the tasks tree. Adding 4 spaces as prefix for each level.

-- [ManuelRego](/twiki/Main/ManuelRego) - 11 Sep 2012

Included new columns and parameters in the report with information about costs.

-- [ManuelRego](/twiki/Main/ManuelRego) - 16 Oct 2012

Implemented filtering by labels and criteria.

Only the tasks with the direct assignments are shown. In each case it works different:

-   Labels: Only tasks with label directly assigned is shown. Inherited labels are not used.
-   Criteria: Only tasks with criterion directly assigned is used. Indirect criteria is only used if it's deactivated to discount the value in the parent task to be shown.

For the last developments a new remote branch called `project-status-report` is being used. Lately, it'll be merged into master and published in the next minor version.

-- [ManuelRego](/twiki/Main/ManuelRego) - 22 Oct 2012

Filter by project is now optional, however you have to choose at least one project or label or criterion to generate the report. You cannot generate a report for all the tasks in [LibrePlan](/twiki/LibrePlan/LibrePlan).

If you don't chose a project the report header will be changed and it'll show the filter instead.

An exclamation mark has been added in the columns *imputed hours* and *total cost* in order to highlight if you're exceeding your estimation in hours or money.

-- [ManuelRego](/twiki/Main/ManuelRego) - 23 Oct 2012

Created query to get the list of `OrderElements` with the assigned labels and/or criteria, when it's not selected any project. This will avoid to load all the projects when you're only filtering by labels and/or criteria.

-- [ManuelRego](/twiki/Main/ManuelRego) - 24 Oct 2012

This development is merged now into `master`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 25 Oct 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S09WBSReport?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                | 10                                                                                                                                                | 3.5                                                                                                                                                 | 0                                                                                                                                                   | Low                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                           | [New WBS report with information about hours](/twiki/LibrePlan/AnA22S02WBSReport#TasK1)                                                        |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 5                                                                                                                                                 | 4.5                                                                                                                                                 | 0                                                                                                                                                   | Low                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                           | [Include cost information in the report](/twiki/LibrePlan/AnA22S02WBSReport#TasK2)                                                             |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 7                                                                                                                                                 | 7.75                                                                                                                                                | 0                                                                                                                                                   | Low                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                           | [Include filter by criteria and labels in the report](/twiki/LibrePlan/AnA22S02WBSReport#TasK3)                                                |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 7                                                                                                                                                 | 7.75                                                                                                                                                | 0                                                                                                                                                   | Low                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                           | [Make optional filter by projects](/twiki/LibrePlan/AnA22S02WBSReport#TasK4)                                                                   |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |


