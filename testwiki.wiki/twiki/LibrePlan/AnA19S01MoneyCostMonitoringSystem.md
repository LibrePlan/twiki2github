[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA19S01MoneyCostMonitoringSystem](LibrePlan_AnA19S01MoneyCostMonitoringSystem "Topic revision: 2 (14 Mar 2012 - 16:07:29)") (14 Mar 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA19S01MoneyCostMonitoringSystem?t=1520343619 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA19S01MoneyCostMonitoringSystem "Attach an image or document to this topic")  

 [AnA19S01MoneyCostMonitoringSystem](LibrePlan_AnA19S01MoneyCostMonitoringSystem)
=================================================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Money Based Cost Monitoring System                                               |
| Iteration              | [AnA19CostModule](LibrePlan_AnA19CostModule)                                     |
| FEA                    | [AnA19S01MoneyCostMonitoringSystem](LibrePlan_AnA19S01MoneyCostMonitoringSystem) |
| Story Lead             |                                                                                  |
| Next Story             |                                                                                  |
| Passed acceptance test | No                                                                               |

###  Tasks

####  Incorporate a field in the task to store the budget to represent the amount of money that the task is expected to cost

The Project Details perspective and, inside it, the WBS tab. In the WBS tab a column called Budget will be added.

This new column will have the the following features:

-   By default it will have a value of 0.
-   It will be editable in the leaf tasks.
-   In the containers will be read-only and the value that it will show will be the addition of all the the Budget column of its descendants.

####  Graphic representation

The graphic representation of this money based method to monitor the cost will be following:

-   It will be included a second cost bar on top of the task. It will called it Money Cost Bar.
-   It will be possible to enable/disable the Money Cost Bar, its display, with a button in the toolbar similar to the ones for turning on/off the progress display, the cost display.
-   There will be the possibility to see at the same time the Money Cost Bar and the Hours Cost Bar.

The representation of the Money Cost Bar will consist of next points:

-   **Money Cost Bar for tasks**  
    It will consist of:
    -   The length that represents the Budget configured in the WBS, will be the duration of the task.
    -   The Money Cost Bar will have a duration for a task equal to: `(Amount_Money_Spent/Budget)*Task_Length`

&nbsp;

-   **Money Cost Bar for the containers**  
    It will consist of:
    -   The Budget of the container is the sum of the budget of all the tasks and containers being inside.
    -   The length that represents the 100% of the budget of the container is the length of the container.
    -   The Money Cost Bar will have a duration for a container equal to: `(Amount_Money_Spent_By_All_Container_Descendants/Sum_Budget_All_Container_Descendants)*Container_Length`

`Amount_Money_Spent` will be calculated according to the following formula:

    Sum of all the hours devoted to a task multiplied by the cost of each hour according to these parameters (type of hour, cost category of the resource, date of the work report)

###  User stories

-   [ItEr76S17MoneyCostMonitoringSystem](LibrePlan_ItEr76S17MoneyCostMonitoringSystem)

###  Tasks in this story

| [Tasks](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                                                          | [Start Date](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA19S01MoneyCostMonitoringSystem?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                           | 5                                                                                                            | 5                                                                                                              | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [ManuelRego](Main_ManuelRego)                                                                                      | [Incorporate a field in the task to store the budget to represent the amount of money that the task is expected to cost](LibrePlan_AnA19S01MoneyCostMonitoringSystem#TasK1) |                                                                                                                     |                                                                                                                       |                                                                                                                    |
| Task                                                                                                           | 16                                                                                                           | 16                                                                                                             | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [ManuelRego](Main_ManuelRego)                                                                                      | [Graphic representation](LibrePlan_AnA19S01MoneyCostMonitoringSystem#TasK2)                                                                                                 |                                                                                                                     |                                                                                                                       |                                                                                                                    |

------------------------------------------------------------------------
