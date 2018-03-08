[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA03RFPerformanceCompanyView](LibrePlan_AnA03RFPerformanceCompanyView "Topic revision: 5 (20 Aug 2012 - 09:52:44)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA03RFPerformanceCompanyView?t=1520344119 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA03RFPerformanceCompanyView "Attach an image or document to this topic")  

 [AnA03RFPerformanceCompanyView](LibrePlan_AnA03RFPerformanceCompanyView)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Performance Improve in Company View                                      |
| Iteration              | [AnA03PerformanceTuning](LibrePlan_AnA03PerformanceTuning)               |
| FEA                    | [AnA03RFPerformanceCompanyView](LibrePlan_AnA03RFPerformanceCompanyView) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

###  Tasks

####  Calculate and save the number of hours allocated to a task

Now to calculate the advance for an order it is needed to do the following steps:

-   To load all the tasks recursively of the root `TaskContainer` which represents an order.
-   For each task get the `ResourceAllocations` of the task.
-   For each `ResourceAllocation` load the `DayAssigment` and sum the hours of all of them.

This provokes that at company view all the `DayAssigments` for all the orders are loaded. This has a big impact of performance.

The solution to this is to have these quantities calculated at each `TaskElement`. `TaskContainers` do not have resource allocation, but they will have stored and calculated the sum of hours allocated to all their descendants tasks.

It will be needed to add one field to the `TaskElement`. It will be:

-   *sumOfHoursAllocated*

The field will be updated on saving the planning for an order.

####  Snapshot to calculate the load chart in company view

This task consists of creating a *snapshot*, strategy used in LibrePlan to load data or have precalculated things in memory. So, this task consists of creating an object with the data used by the graphic.

The *snapshot* will be recalculated when the following entities change:

-   Calendars.
-   Resources. Really it is only needed when it changes the calendar and the activation period.
-   Tasks.

[OscarGonzalez](Main_OscarGonzalez) to explanation about *snapshot*.

###  User stories

-   [ItEr61S03RFPerformanceCompanyView](LibrePlan_ItEr61S03RFPerformanceCompanyView)
-   [ItEr62S03RFPerformanceCompanyView](LibrePlan_ItEr62S03RFPerformanceCompanyView)

###  Tasks in this story

| [Tasks](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA03RFPerformanceCompanyView?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 7                                                                                                        | 7                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [JacoboAragunde](Main_JacoboAragunde)                                                                          | [Calculate and save the number of hours allocated to a task](LibrePlan_AnA03RFPerformanceCompanyView#TasK1)    |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 14                                                                                                       | 0                                                                                                          | 14                                                                                                         | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [JacoboAragunde](Main_JacoboAragunde)                                                                          | [Snapshot to calculate the load chart in company view](LibrePlan_AnA03RFPerformanceCompanyView#TasK2)          |                                                                                                                 |                                                                                                                   |                                                                                                                |

------------------------------------------------------------------------
