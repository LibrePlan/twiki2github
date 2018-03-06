[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S23FixAllocationModel](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel "Topic revision: 17 (03 Jan 2012 - 15:59:19)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S23FixAllocationModel?t=1520337926 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S23FixAllocationModel "Attach an image or document to this topic")

 [ItEr75S23FixAllocationModel](/twiki/LibrePlan/ItEr75S23FixAllocationModel)
===================================================================================================================================



|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | Fix allocation model                                                                 |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)                       |
| FEA                    | [ItEr75S23FixAllocationModel](/twiki/LibrePlan/ItEr75S23FixAllocationModel) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

######  [Fix bug applying the sigmoid and stretched functions on being moved](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK0)

Fixed issue when moving tasks with an assignment function.

Assignment function is applied again in destination.

When you move a task, maybe duration of task can change due to weekends, bank days or whatever. This is why it's needed to apply before the flat allocation in order to calculate task duration and apply assignment function afterwards.

Patch was also applied in stable branch as it was straightforward.

-- [ManuelRego](/twiki/Main/ManuelRego) - 23 Aug 2011

######  [Modify ResourceAllocation to register a manual allocation](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK1)

Finally the new enum `AllocationType` was not created as it adds some redundant and makes more complex the implementation. Maybe this could be reviewed and changed in the future.

The approach used was create a new `AssignmentFunction` called `ManualFunciont`, which do nothing when it's applied. This function is saved `ResourceAllocation::assignmentFunction` attribute.

When an allocation is manually edited in advanced allocation window, function is changed to *Manual*. Then if a *Manual* task is moved in the Gantt, as a flat function is applied it's reset to *Flat*.

Moreover 2 more minor fixes were done during this task:

-   Removed warnings while doing manual allocations ("there must be ...")
-   Disabled edition button for *Flat*, *Manual* and *Sigmoid* functions (added a tooltip explaining that these options are not configurable)

Also, an extra thing was implemented to keep consistency, now In advanced allocation if you change the total hours of an allocation, the assignment function configured is applied if any. Something similar to the previous task.

######  [Inform about the allocation type in the allocation pop-up](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK2)

Added a new column *Function* with information about assignment function in allocation pop-up. This column is only shown if there's any allocation which is not flat.

-- [ManuelRego](/twiki/Main/ManuelRego) - 26 Aug 2011

Disabling **resources per day** and **hours** inputs if allocation is not flat.

-- [ManuelRego](/twiki/Main/ManuelRego) - 29 Aug 2011

For the moment, if something is changed in resource allocation popup, the approach followed is the same than when you move a task. First a flat allocation is applied, then if an assignment function is defined it's applied afterwards (if assignment function was manual it's reseted to flat).

Maybe, it's not needed to disable **resources per day** and **hours** inputs even when we have a special assignment function, as it could work like in the previous case.

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 Aug 2011

Finally I've re-enabled **resources per day** and **hours inputs** for any allocation, as with current implementation is not needed to disable anything.

On the other hand, I've fixed an issue when changing to flat in advanced allocation window, task size could be increased and we want to avoid it.

-- [ManuelRego](/twiki/Main/ManuelRego) - 01 Sep 2011

I've been working in removing the date from Stretch class, as it's relative. The problem is that it's not relative to Task dates but to ResourceAllocation dates. I need to redo some work to take into account this issue.

-- [ManuelRego](/twiki/Main/ManuelRego) - 08 Sep 2011

Removed `date` field from `Stretch` class. Date is now calculated with `lengthPercentage` using start and end date of the resource allocation.

Detected an issue in *Resource Allocation* pop-up. If you change the hours of a flat resource allocation, for example from 40h to 80h, you click apply button and use *Go to advanced allocation* button directly. You are going to be able to modify only the days of the first 40h, the rest of the days are not going to be editable.

This is because of, before click in *Accept* task dates are not changed. And in advanced allocation is not possible to modify task length, so days out of the task limits are not editable. A possible solution would be move *Go to advanced allocation* button to contextual menu over a task. It seems like a good approach.

-- [ManuelRego](/twiki/Main/ManuelRego) - 12 Sep 2011

Disabled all fields in resource allocation pop-up if there's any manual allocation. For the rest of allocations, it's possible to do some modifications as they're relatives, but in case of manual allocation it's not possible to do any change in this pop-up.

**Go to advanced allocation** button has been removed from resource allocation pop-up and has been moved to an option in the secondary menu over a task. This is because of if you do some changes in resource allocation pop-up and go to advanced allocation without apply, we get an inconsistent state. So, from now on in order to go to advanced allocation of a single task, this should be done through the contextual menu of a task.

-- [ManuelRego](/twiki/Main/ManuelRego) - 27 Sep 2011

Used a combo in *Resource Allocation* pop-up to give the possibility to change to **Flat** assignment function when you're using any other.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Oct 2011

######  [Implement reallocation strategy for manual allocation](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK3)

At this moment the implementation done is the following one:

-   When a manual allocation is done the task is marked with `START_IN_FIXED_DATE`
-   Tasks with manual allocation are not allowed to be moved manually in the Gantt
-   The start constraint combo and date are disabled while a manual application is used, in order to avoid change it from `START_IN_FIXED_DATE`
-   In order to enable this field, you need to change from manual to flat allocation

-- [ManuelRego](/twiki/Main/ManuelRego) - 08 Oct 2011

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

-   All **AssignmentFunctions** are using LocalDate, it should be changed to use EffortDuration instead.

-- [ManuelRego](/twiki/Main/ManuelRego) - 23 Aug 2011

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                         | 20                                                                                                                                                         | 8.5                                                                                                                                                          | 0                                                                                                                                                            | Low                                                                                                                                                         | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Fix bug applying the sigmoid and stretched functions on being moved](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK0)                                |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |
| Task                                                                                                                                                         | 20                                                                                                                                                         | 14                                                                                                                                                           | 0                                                                                                                                                            | Low                                                                                                                                                         | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Modify ResourceAllocation to register a manual allocation](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK1)                                          |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |
| Task                                                                                                                                                         | 20                                                                                                                                                         | 40.25                                                                                                                                                        | 0                                                                                                                                                            | Low                                                                                                                                                         | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Inform about the allocation type in the allocation pop-up](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK2)                                          |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |
| Task                                                                                                                                                         | 3                                                                                                                                                          | 3                                                                                                                                                            | 0                                                                                                                                                            | Low                                                                                                                                                         | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Implement reallocation strategy for manual allocation](/twiki/LibrePlan/AnA07S08FixAllocationModel#TasK3)                                              |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S23FixAllocationModel?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | 65.75                                                                                                                                                                     | 0                                                                                                                                                                         | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                          |
| Total                                                                                                                                                       | 65.75                                                                                                                                                                     | 0                                                                                                                                                                         | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                          |

------------------------------------------------------------------------
