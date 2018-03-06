[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA03RFPerformanceCompanyView](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView "Topic revision: 5 (20 Aug 2012 - 09:52:44)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA03RFPerformanceCompanyView?t=1520337828 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA03RFPerformanceCompanyView "Attach an image or document to this topic")

 [AnA03RFPerformanceCompanyView](/twiki/LibrePlan/AnA03RFPerformanceCompanyView)
=========================================================================================================================================



|                        |                                                                                          |
|------------------------|------------------------------------------------------------------------------------------|
| Story summary          | Performance Improve in Company View                                                      |
| Iteration              | [AnA03PerformanceTuning](/twiki/LibrePlan/AnA03PerformanceTuning)               |
| FEA                    | [AnA03RFPerformanceCompanyView](/twiki/LibrePlan/AnA03RFPerformanceCompanyView) |
| Story Lead             |                                                                                          |
| Next Story             |                                                                                          |
| Passed acceptance test | No                                                                                       |

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

[OscarGonzalez](/twiki/Main/OscarGonzalez) to explanation about *snapshot*.

###  User stories

-   [ItEr61S03RFPerformanceCompanyView](/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView)
-   [ItEr62S03RFPerformanceCompanyView](/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03RFPerformanceCompanyView?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                           | 7                                                                                                                                                            | 7                                                                                                                                                              | 0                                                                                                                                                              | Low                                                                                                                                                           | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                   | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                              | [Calculate and save the number of hours allocated to a task](/twiki/LibrePlan/AnA03RFPerformanceCompanyView#TasK1)                                        |                                                                                                                                                                     |                                                                                                                                                                       |                                                                                                                                                                    |
| Task                                                                                                                                                           | 14                                                                                                                                                           | 0                                                                                                                                                              | 14                                                                                                                                                             | Low                                                                                                                                                           | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                   | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                              | [Snapshot to calculate the load chart in company view](/twiki/LibrePlan/AnA03RFPerformanceCompanyView#TasK2)                                              |                                                                                                                                                                     |                                                                                                                                                                       |                                                                                                                                                                    |

------------------------------------------------------------------------
