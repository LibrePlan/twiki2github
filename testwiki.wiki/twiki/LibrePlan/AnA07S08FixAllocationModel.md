[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA07S08FixAllocationModel](LibrePlan_AnA07S08FixAllocationModel "Topic revision: 3 (03 Jan 2012 - 15:58:40)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA07S08FixAllocationModel?t=1520344044 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S08FixAllocationModel "Attach an image or document to this topic")  

 [AnA07S08FixAllocationModel](LibrePlan_AnA07S08FixAllocationModel)
===================================================================

|                        |                                                                    |
|------------------------|--------------------------------------------------------------------|
| Story summary          | Fix allocation model                                               |
| Iteration              | [AnA07PlanningWindow](LibrePlan_AnA07PlanningWindow)               |
| FEA                    | [AnA07S08FixAllocationModel](LibrePlan_AnA07S08FixAllocationModel) |
| Story Lead             |                                                                    |
| Next Story             |                                                                    |
| Passed acceptance test | No                                                                 |

###  Fix bug applying the sigmoid and stretched functions on being moved

Now there is a bug in the application. If you configure a Stretched Function (both lineal or polynomial) and that task is reallocated as a consequence of a movement in gantt, a flat allocation function is applied with the configuration strategy of the simple allocation pop-up in database.

However, both the stretched function (lineal or polynomial) and the sigmoid function are relative, that's to say, they are not dependant of the allocation point and can be applied at any point.

Because of that, this first task consists of launching the allocation specified by the allocation assigment function (stretched or sigmoid) if a task is moved because of gannt dependencies.

###  Modify ResourceAllocation to register a manual allocation

One of the needs to fix the allocation model is to know if an allocation has been manually modified.

To regard a resource allocation as manually allocated is conceptually equivalent to think that the manual allocation is another type of assigment function.

Now we have the following `AssigmentFunctions`:

-   SigmoidFunction
-   StretchedFunction
-   And implicitily, without needing to store anything FlatFunction.

The proposal for this task is to have a new enum field in the `ResourceAllocation` entity to save the type of allocation. This field would have four values and can be called ***AllocationType***:

-   FLAT
-   MANUAL
-   LINEAL\_STRETCHED\_FUNCTION
-   POLYNOMIAL\_STRETCHED\_FUNCTION
-   SIGMOID FUNCTION

There will be a small redundancy but more uniformity by saving LINEAL\_STRETCHED\_FUNCTION, POLYNOMIAL\_STRETCHED\_FUNCTION and SIGMOID\_FUNCTION as values of the enum. This information is now got navigating the `AssigmentFunction` relationship with `ResourceAllocation`. All in all, I think it is worth this small redundancy.

It is needed to change the selector in Advanced Allocation to include these enum values. Now the values are None, Stretches, Interpolation, Sigmoid. New ones will be: Flat, Manual, Stretches, Interpolation, Sigmoid.

The last part of this task is to detect changes made by the users in the advanced allocation window.

The behavior to implement is:

If a user edits a cell changing one value, then two things are needed to do:

-   If the value of the field ***AllocationType*** is different from MANUAL, change it to this value. It is needed to delete the `AssignmentFunction` object too if the allocation is Stretched or Sigmoid and if this erasure is not currently being done.
-   Change the combo selected value which shows the `AllocationType` to MANUAL.

**![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!") WARNING ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!"): Implementation doesn't follow this analysis and for the moment ***AllocationType*** enum is not created. More info at: [ItEr75S23FixAllocationModel\#Modify\_ResourceAllocation\_to\_reg](LibrePlan_ItEr75S23FixAllocationModel#Modify_ResourceAllocation_to_reg)**

####  Inform about the allocation type in the allocation pop-up

If we have an allocation different from Flat, the parameters about the allocation are not allowed to change if the allocation function is configured. The parameters are:

-   Number of hours. This is a parameter per allocation row.
-   Resources per day. This is a parameter per allocation row.
-   Number of days (duration). This affects all the resource allocations of the task.

The interface proposal is:

1.  To include an assignment function column in the allocation table. This allocation column will be rendered only if one of the resource allocation has an allocation type different from **Flat** Justification for this is that, from usability point of view, there are concerns about complicating this window unnecessary in all cases.
2.  If the allocation assignment function for the resource allocation is one different from **Flat**, the fields **Hours** and **Resources per day** will be disabled independently of the global resource allocation strategy being used (calculate number of hours, calculate workable days or calculate resource per day).
3.  If one of the resource allocations is different from **Flat** then the global field **Planned workable days** will be set to the current duration of the task. This is a temporal solution too, because what it really happens is that the allocation duration is per resource allocation not shared for all the resource allocations.
4.  To include in the column **Assignment function** one combo set with the current allocation function being used.
    1.  The combo will have only one value for the Flat function if this is the one set. This implies it is not allowed to change in the screen from Flat to any other allocation strategy. Reason for this is just to save work for the release 1.2. To change from Flat to any other assignment function will have to be done through the advanced allocation window as usual.
    2.  If the combo is configured with Strechted, Interpolation or Sigmoid it will be filled to with the value **Flat** (two values in the combo). It is allowed, therefore, to change from these advanced allocations to **Flat**. On doing this, the fields **Hours** and **Resources per day** will be enabled depending on the semantics specified by the current allocation strategy (calculate resources per day, calculate number of hours or calculate workable days).

####  Implement reallocation strategy for manual allocation

In a previous analysis was agreed that three reallocation strategies were going to be provided for tasks with manual allocation.

The proposal is to configure reallocation with project scope and that, therefore, the strategy is stored once for all the tasks of a project. It will be saved in the entity Order and the interface to choose this value will be the **General data** tab of the **Project details perspective**.

There will be an enum with the following values:

1.  \- FLAT\_REALLOCATION =&gt; Automatically tasks are moved and reallocated with flat allocation and the **Manual** assignment function is changed to **Flat** for the resource allocations of the task being moved.
2.  \- DO\_NOT\_MOVE =&gt; The task is marked as START\_IN\_FIXED\_DATE and dependencies will be violated. To move a manual allocation task with this project strategy, the user should change to flat the allocation function in the resource allocation row and, at that moment, it will be moved.
3.  \- APPLY\_AS\_IT\_IS =&gt; With this strategy the task is moved being copied day by day in the new date. Besides the Manual flag is kept in the tasks resource allocations which had them.
    -   For general allocations the proposal is to do an allocation of the same amount per day in the new dates but over the resources less loaded satisfying the criteria in the new dates. If it is easier just to keep the resources as well, we can start with this approach.

###  User stories

-   [ItEr75S23FixAllocationModel](LibrePlan_ItEr75S23FixAllocationModel)
-   [ItEr76S05FixAllocationModelItEr75S23](LibrePlan_ItEr76S05FixAllocationModelItEr75S23)

###  Tasks in this story

| [Tasks](LibrePlan_AnA07S08FixAllocationModel?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA07S08FixAllocationModel?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA07S08FixAllocationModel?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA07S08FixAllocationModel?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA07S08FixAllocationModel?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA07S08FixAllocationModel?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA07S08FixAllocationModel?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA07S08FixAllocationModel?sortcol=7;table=2;up=0#sorted_table "Sort by this column")       | [Start Date](LibrePlan_AnA07S08FixAllocationModel?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA07S08FixAllocationModel?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA07S08FixAllocationModel?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Task                                                                                                    | 20                                                                                                    | 20                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [ManuelRego](Main_ManuelRego)                                                                               | [Fix bug applying the sigmoid and stretched functions on being moved](LibrePlan_AnA07S08FixAllocationModel#TasK0) |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 20                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [ManuelRego](Main_ManuelRego)                                                                               | [Modify ResourceAllocation to register a manual allocation](LibrePlan_AnA07S08FixAllocationModel#TasK1)           |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 20                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [ManuelRego](Main_ManuelRego)                                                                               | [Inform about the allocation type in the allocation pop-up](LibrePlan_AnA07S08FixAllocationModel#TasK2)           |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 3                                                                                                       | 17                                                                                                      | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [ManuelRego](Main_ManuelRego)                                                                               | [Implement reallocation strategy for manual allocation](LibrePlan_AnA07S08FixAllocationModel#TasK3)               |                                                                                                              |                                                                                                                |                                                                                                             |

###  Total Hours in this Story

| [User](LibrePlan_AnA07S08FixAllocationModel?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA07S08FixAllocationModel?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA07S08FixAllocationModel?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA07S08FixAllocationModel?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                          | 63                                                                                                                   | 0                                                                                                                    | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                     |
| Total                                                                                                  | 63                                                                                                                   | 0                                                                                                                    | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                     |

------------------------------------------------------------------------
