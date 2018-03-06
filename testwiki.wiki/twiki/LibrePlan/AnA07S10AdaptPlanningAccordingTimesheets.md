[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA07S10AdaptPlanningAccordingTimesheets](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets "Topic revision: 3 (06 Nov 2012 - 18:12:37)") (06 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?t=1520337842 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets "Attach an image or document to this topic")

 [AnA07S10AdaptPlanningAccordingTimesheets](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets)
==================================================================================================================================================================



|                        |                                                                                                                |
|------------------------|----------------------------------------------------------------------------------------------------------------|
| Story summary          | Adapt planning according to timesheets                                                                         |
| Iteration              | [AnA07PlanningWindow](/twiki/LibrePlan/AnA07PlanningWindow)                                           |
| FEA                    | [AnA07S10AdaptPlanningAccordingTimesheets](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets) |
| Story Lead             |                                                                                                                |
| Next Story             |                                                                                                                |
| Passed acceptance test | No                                                                                                             |

###  Tasks



####  Store minimum and maximum date from timesheets in tasks

For each task in the WBS 2 new fields will be calculated:

-   First timesheet date: Date of the first timesheet reporting hours to the task (or any subtask).
-   Last timeshet date: Date of the last timesheet reporting hours to the task (or any subtask).

These dates will be calculated during the timesheet saving process (edition and deletion included). The dates for the containers will be calculated taking into account their own hours reported and their children too.

If after a deletion, there is no timesheets reporting hours over a task, the dates will be empty.

The dates will be recalculated when there're any children movement in the WBS.

It'll be used the class `SumChargedEffort` to store this information.



####  Mark tasks as finished in timesheets standard UI

`WorkReportLine` will be modified to include a new filed showing if a task is or not finished.

A new validation will be added in order that only one timesheet line per task can be marked as finished.

In the UI, if a task is marked as finished in a line, the rest of the lines of the tasks will have disabled the field finished.

Moreover, it'll be stored in `SumChargedEffort` a new field to know if a task is finished or not according to the timesheets. That will be updated while editing/deleting a timesheet. The field in the containers will be calculated only taken into account their own mark, and not the children.



####  New predefined progress type for progress reported by timesheets

New predefined progress type called `TIMESHEETS`.

The user won't be allowed to edit/remove this progress type.

In the progress management window, this new progress type will be not allowed to be added/edited/removed as this will be done automatically in the following task. So, this progress will appear always as disabled and it'll be always the spread progress.



####  Update planning according to timesheets

In the project Gantt view a new button will be included in order to adapt the planning according to the information from timesheets.

The tasks will have a new field called `UPDATED_FROM_TIMESHEETS`, in order to know if they've been updated taking into account the information in the timesheets.

Updated tasks will have the following behavior:

-   You cannot reassign that tasks. Resource allocation pop-up and advanced allocation windows will be disabled. And these tasks won't be reassigned using the *Reassign* button either.
-   They'll have a restriction `START_ON_FIXED_DATE` that will make the tasks immovable even if the dependencies have priority. Constraint combo and date will be disabled too.
-   You cannot change the position in the WBS or remove the scheduling point status.
-   If the timesheets are removed and the update planning button is used, the `UPDATED_FROM_TIMESHEETS` field will be unset.

The algorithm triggered after clicking the new button will be the following:

-   All the tasks with reported hours from timesheets and without the `UPDATED_FROM_TIMESHEETS` mark will be marked as updated.
-   For all the tasks `UPDATED_FROM_TIMESHEETS`:
    -   The start date will be taken from the first date from the timesheets.
    -   If the current task end date is earlier than last date from the timesheets, task end date is updated to the last date from the timsheets.
    -   If the task is marked as finished in the timesheets:
        -   If there's not a progress of type `TIMESHEETS` of 100% marked as spread, it'll be added and marked as spread.
        -   All the resource allocations after the end date will be removed.
        -   The end date will be taken from the last date from the timesheets.
    -   If the task is NOT marked as finished in the timesheets:
        -   If there's a progress of type `TIMESHEETS`, it'll be removed.
    -   All the tasks depending on this task will be moved and reassigned accordingly to the changes in the start/end dates.

###  User stories

-   [ItEr77S12AdaptPlanningAccordingTimesheets](/twiki/LibrePlan/ItEr77S12AdaptPlanningAccordingTimesheets)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                      | 4                                                                                                                                                                       | 4                                                                                                                                                                         | 0                                                                                                                                                                         | Low                                                                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [Store minimum and maximum date from timesheets in tasks](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK1)                                           |                                                                                                                                                                                |                                                                                                                                                                                  |                                                                                                                                                                               |
| Task                                                                                                                                                                      | 6                                                                                                                                                                       | 6                                                                                                                                                                         | 0                                                                                                                                                                         | Low                                                                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [Mark tasks as finished in timesheets standard UI](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK2)                                                  |                                                                                                                                                                                |                                                                                                                                                                                  |                                                                                                                                                                               |
| Task                                                                                                                                                                      | 2                                                                                                                                                                       | 2                                                                                                                                                                         | 0                                                                                                                                                                         | Low                                                                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [New predefined progress type for progress reported by timesheets](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK3)                                  |                                                                                                                                                                                |                                                                                                                                                                                  |                                                                                                                                                                               |
| Task                                                                                                                                                                      | 16                                                                                                                                                                      | 16                                                                                                                                                                        | 0                                                                                                                                                                         | Low                                                                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [Update planning according to timesheets](/twiki/LibrePlan/AnA07S10AdaptPlanningAccordingTimesheets#TasK4)                                                           |                                                                                                                                                                                |                                                                                                                                                                                  |                                                                                                                                                                               |


