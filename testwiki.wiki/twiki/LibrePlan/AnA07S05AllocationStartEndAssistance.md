[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA07S05AllocationStartEndAssistance](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance "Topic revision: 8 (04 Apr 2011 - 12:05:06)") (04 Apr 2011, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA07S05AllocationStartEndAssistance?t=1520337840 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S05AllocationStartEndAssistance "Attach an image or document to this topic")

 [AnA07S05AllocationStartEndAssistance](/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance)
==========================================================================================================================================================



|                        |                                                                                                        |
|------------------------|--------------------------------------------------------------------------------------------------------|
| Story summary          | Allocation Start End Assistance                                                                        |
| Iteration              | [AnA07PlanningWindow](/twiki/LibrePlan/AnA07PlanningWindow)                                   |
| FEA                    | [AnA07S05AllocationStartEndAssistance](/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance) |
| Story Lead             |                                                                                                        |
| Next Story             |                                                                                                        |
| Passed acceptance test | No                                                                                                     |

###  Tasks



####  Allocation duration calculation assistance

In the Gantt planning of a project tasks are allocated from start to end or from end to start dependending on the interaction of the following parameters:

-   Type of scheduling used for the project: Forwards scheduling or backwards scheduling.
-   Constraint configured in the task: START\_NOT\_SOONER\_THAN, FINISH\_NOT\_LATER\_THAN, START\_IN\_FIXED\_DATE
-   Project configuration saying if dependencies or constraints have priority.
-   Input/Output dependencies of a task.

Allocations more frequently used are from beginning to end. So, let's put an example about an allocation from end to start:


       * Project A: Forwards planning and dependencies have priority.
       * Task 1:
          * Constraint: START_NOT_SOONER_THAN 1st March
          * Output dependencies: END_END dependency Task1->Task2
          * Allocation: Calculate Workable days
                              Hours: 40h.
                              Resources per day: 1 (100%)
       * Task 2:
          * Constraint: AS_SOON_AS_POSSIBLE
          * Input dependencies: END_END dependency Task1->Task2
          * Allocation: Calculate Resources Per Day
                              Workable days: 3
                              Hours: 20h.

In the scenario above, the Task2 will be allocated from end to start beginning by the end date of the Task1 until completing 3 workable days with 20h of allocation.

In the situation above there is a need in which the user can be assisted more by the program and it is the following: Many times project managers know when a task want to be finished or started but do not have an estimation about the workable days of the task. So, currently user would have to translate to workable days from the calendar to configure allocation and that is a time consuming, boring task which can be automated.

So, specification to solve that is the following:

-   Include a first row in the allocation configuration section aboce start and end dates with the name ***Allocation direction*** and two possible values *Forwards* and *Backwards*.
-   If the allocation direction is *forwards* then, do editable the start date if the allocation strategy lets specify duration (calculate number of hours and calculate number of hours).
-   If the allocation direction is *backwards* then, do editable the end date if the allocation strategy lets specify duration (calculate number of hours and calculate number of hours).
-   If you edit the start date of the task update the planned workable days. The same if you edit the end date of the task.
-   If you change the planned workable days update the start date of the task in case of *forwards allocation* of the task.
-   If you change the planned workable days update the end date of the task in case of *backwards allocation* of the task.

***How to translate from start/end dates to planned workable days***

It will be used the calendar that the task has configured. A workable day will be a day in which the number of hours to work as timetable specified by the task is different from zero.

***Implementation note: Hint about how to know if a task is (or will be) allocated forwards or backwards***

Class `org.navalplanner.web.planner.allocation.FormBinder.WorkableDaysAndDatesBinder` and there methods there like `allocationRowsHandler.isForwardsAllocation()`

###  User stories

-   [ItEr72S07AllocationStartEndAssistance](/twiki/LibrePlan/ItEr72S07AllocationStartEndAssistance)
-   [ItEr74S06CalendarAdminInterfaceItEr73S06](/twiki/LibrePlan/ItEr74S06CalendarAdminInterfaceItEr73S06)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                  | 14                                                                                                                                                                  | 0                                                                                                                                                                     | 14                                                                                                                                                                    | Low                                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                          | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                         | [Allocation duration calculation assistance](/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance#TasK1)                                                        |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S05AllocationStartEndAssistance?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                    | 0                                                                                                                                                                                  | 0                                                                                                                                                                                  | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                                    |
| Total                                                                                                                                                                | 0                                                                                                                                                                                  | 0                                                                                                                                                                                  | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                                    |

------------------------------------------------------------------------
