[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S12AdaptPlanningAccordingTimesheets](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets "Topic revision: 16 (23 Nov 2012 - 08:16:56)") (23 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?t=1520337947 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets "Attach an image or document to this topic")

 [ItEr77S12AdaptPlanningAccordingTimesheets](/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets)
====================================================================================================================================================================



|                        |                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| Story summary          | Adapt planning according to timesheets                                                                           |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                                                   |
| FEA                    | [ItEr77S12AdaptPlanningAccordingTimesheets](/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets) |
| Story Lead             |                                                                                                                  |
| Next Story             |                                                                                                                  |
| Passed acceptance test | No                                                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Development is being done in a remote branch called `adapt-planning-according-timesheets`.

######  Store minimum and maximum date from timesheets in tasks

In order to calculate the minimum and maximum date when a work report is saved/edited/removed you'll follow the next algorithm:

-   Before saving the `WorkReport` we'll generate a set of `OrderElements`, including:
    -   For the `WorkReportLines` that are going to be added:
        -   All the `OrderElements` that are linked now
    -   For the `WorkReportLines` that are going to be modified:
        -   All the `OrderElements` that were linked before the changes
        -   All the `OrderElements` that are linked now
    -   For the `WorkReportLines` that are going to be deleted:
        -   All the `OrderElements` that were linked before the changes (if any). So, if the line to be removed is a new object, we won't take into account that `OrderElement`, and if the line to be removed has been modified, we'll take into account only the `OrderElement` before the modification.
-   After saving the `WorkReport` we'll recalculate using the data into the database the first and last dates for the set of `OrderElements` generated in the previous point:
    -   In order to calculate that it'll be used a query:

            MIN(date), MAX(date) FROM WorkReportLine WHERE orderElement = :orderElement
                  * Moreover it'll be needed to recalculate the parents too, for each =OrderElement= in the set

######  New predefined progress type for progress reported by timesheets

Created the new predefined progress type called `TIMESHEETS`. Included a new field `readOnly` in `AdvanceType` in order to be used in the UI to disable the different functionalities related with progress management.

######  Mark tasks as finished in timesheets standard UI

Added a checkbox in the work reports UI to mark a task as finished. The checkbox is disabled is the task is already finished in another work report.

Moreover, a new field `finishedTimesheets` has been added to `SumChargedEffort`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 Oct 2012

It has been modified the personal timesheets UI to include a pop-up allowing to mark a task as finished too.

-- [ManuelRego](/twiki/Main/ManuelRego) - 22 Nov 2012

######  New predefined progress type for progress reported by timesheets

Added new field `updatedFromTimesheets` to `TaskElement`.

Included the new button to adapt planning in the toolbar.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Nov 2012

Started implementation of the adapt planning command following description in the analysis. It's pending to remove the resource allocations after the end date, for the tasks marked as finished.

On the other hand, it's also pending to disable the different parts of the UI, for the tasks that have been updated with the information from the timesheets.

-- [ManuelRego](/twiki/Main/ManuelRego) - 06 Nov 2012

Implemented the following restrictions in the tasks marked as `updatedFromTimesheets`:

-   Mark task as **fixed** having priority over dependencies in any case (even if the project is marked as *dependencies have priority*)
-   Disable constraints combo and date in task properties pop-up
-   Disable scheduling state toggler, not allowing to change the scheduling point

-- [ManuelRego](/twiki/Main/ManuelRego) - 07 Nov 2012

Implemented more restrictions in the tasks marked as `updatedFromTimesheets`:

-   Disable resource allocation pop-up for tasks updated from timesheets
-   Disable tasks movement for tasks updated from timesheets
-   Disable advanced allocation window for tasks updated from timesheets
-   Prevent tasks updated from timesheets to be reassigned
-   Disable movement in WBS (disable drag & drop too). Allowing to move the element up and down as it doesn't have any bad consequence.
    -   Disabled unindent in children of a task updated from timesheets
    -   Disabled indent if previous sibling (the future parent) is a task updated from timesheets

-- [ManuelRego](/twiki/Main/ManuelRego) - 12 Nov 2012

Finished the pending task:

-   Removed allocations after the end date for tasks marked as finished in the timesheets

After some testing fixed some other stuff:

-   Tasks position is now updated after all the tasks dates are adapted according to timesheets. In order to avoid doing resignations if tasks have already reported hours.
-   Containers are not adapted according to timesheets to avoid wrong behaviors. It seems clear that if you use this feature you wouldn't report hours to containers.
-   A feedback message for the user has been added while doing the planing.

-- [ManuelRego](/twiki/Main/ManuelRego) - 13 Nov 2012

Finally some marks have been added to show the first/last timesheets dates when you're showing the reported hours bar. Also the tasks that you cannot move in the Gantt (like the ones updated from timesheets) are displayed with a special style.

-- [ManuelRego](/twiki/Main/ManuelRego) - 15 Nov 2012

Fixed problem with progress and hours bars in Gantt. As they were calculated regarding task allocation and if the task was updated from timesheets, sometimes some allocations appear before the task start. Finally it was decided to simplify the code and paint the bar proportionally to the task length.

-- [ManuelRego](/twiki/Main/ManuelRego) - 19 Nov 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                       | 4                                                                                                                                                                        | 4.5                                                                                                                                                                        | 0                                                                                                                                                                          | Low                                                                                                                                                                       | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                  | [Store minimum and maximum date from timesheets in tasks](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK1)                                            |                                                                                                                                                                                 |                                                                                                                                                                                   |                                                                                                                                                                                |
| Task                                                                                                                                                                       | 6                                                                                                                                                                        | 8.5                                                                                                                                                                        | 0                                                                                                                                                                          | Low                                                                                                                                                                       | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                  | [Mark tasks as finished in timesheets standard UI](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK2)                                                   |                                                                                                                                                                                 |                                                                                                                                                                                   |                                                                                                                                                                                |
| Task                                                                                                                                                                       | 2                                                                                                                                                                        | 1.75                                                                                                                                                                       | 0                                                                                                                                                                          | Low                                                                                                                                                                       | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                  | [New predefined progress type for progress reported by timesheets](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK3)                                   |                                                                                                                                                                                 |                                                                                                                                                                                   |                                                                                                                                                                                |
| Task                                                                                                                                                                       | 16                                                                                                                                                                       | 16.5                                                                                                                                                                       | 0                                                                                                                                                                          | Low                                                                                                                                                                       | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                  | [Update planning according to timesheets](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK4)                                                            |                                                                                                                                                                                 |                                                                                                                                                                                   |                                                                                                                                                                                |


