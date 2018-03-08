[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA14S01PerProjectDashboard](LibrePlan_AnA14S01PerProjectDashboard "Topic revision: 11 (01 Mar 2012 - 19:45:05)") (01 Mar 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA14S01PerProjectDashboard?t=1520344062 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA14S01PerProjectDashboard "Attach an image or document to this topic")  

 [AnA14S01PerProjectDashboard](LibrePlan_AnA14S01PerProjectDashboard)
=====================================================================

|                        |                                                                      |
|------------------------|----------------------------------------------------------------------|
| Story summary          | Project per project dashboard                                        |
| Iteration              | [AnA14ProjectsDashboards](LibrePlan_AnA14ProjectsDashboards)         |
| FEA                    | [AnA14S01PerProjectDashboard](LibrePlan_AnA14S01PerProjectDashboard) |
| Story Lead             |                                                                      |
| Next Story             |                                                                      |
| Passed acceptance test | No                                                                   |

###  Tasks

They will be developed two screens:

1.  ***Per project***. It will be a perspective in which several charts and KPI (Key Performance Indicators) related to the project will be shown.
2.  ***Per company***.It will be a screen in which less detailed KPI are shown for the projects that are opened in the company view.

In this analysis story will be described the dashboard per project. It is useful to divide the KPI and charts in several sections:

-   Progress =&gt; KPIs related with the progress of the project.
-   Time =&gt; KPIs related with the delay of the project
-   Resources =&gt; KPIs related with the resources of a project
-   Cost =&gt; KPIs related with the cost of a project

####  Number of tasks by status

Number of tasks per status. The following status are considered:

-   Task blocked. They have a progress in 0% and they do not have work reports and:
    -   all the dependencies END\_START which have the task as destination have a progress different than 100% (not ended).
    -   all the dependencies START\_START which have the task as destination are blocked or ready to start.
-   Tasks in progress. They have a progress &lt; 100% or at least a work report associated with them
-   Tasks ended. Thay have a progress of 100%
-   Tasks ready to start. They have a progress in 0% and they do not have associated work reports and:
    -   all the dependencies END\_START which have the task as destination are ended.
    -   all the dependencies START\_START which have the task as destination are ended or in progress.

Count all the tasks of these types and show the numbers absolut and relative in a pie chart.

####  Deadline violation KPI

Pie chart with number of tasks of the project with deadline violations Tasks classified in three categories:

-   Tasks without deadline.
-   Tasks with the end date &gt; due date.
-   Tasks with the end date &lt;= due date.

####  Global progress of the project

Horizontal chart with two bar per row.

-   Current progress of the project
-   Expected progress of the project

![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!") **NOTE**: take into account that when we talk about allocated or assigned hours, we're talking about hours and minutes as resource allocations are done with `EffortDuration` which allows to specify minutes too.

Three rows must be shown:

*3.1 Progress by all tasks by hours.*

-   Bar 1: Sum the progress of all tasks.
-   Bar 2: Select tasks with start date &lt;= current date.
    -   For tasks with end date &lt;= current date: compute all the hours allocated as done.
    -   For tasks with end date &gt; currentdate: compute the hours allocated as done with date &lt;= current date in that task.

*3.2 Progress with critical path tasks by hours.*

-   Bar 1:
    -   SUM\_A: Sum for each task belonging to any of the critical paths the quantity (current\_progress \* number of hours allocated to the task)/100.
    -   SUM\_B: Sum of all the hours allocated of the tasks which belong to any of the critical paths for the gantt of a project.
    -   Bar 1 is SUM\_A/SUM\_B\*100
-   Bar 2: Select tasks with start date &lt;= current date which belongs to any critical path:
    -   For tasks with end date &lt;= current date. Compute all the hours SUM\_C
    -   For tasks with end date &gt; current date. Sum the hours of these tasks allocated in the days with date &lt;= current date. SUM\_D
    -   Bar 2 is (SUM\_C + SUM\_D)/SUM\_B\*100

*3.3 Progress with critical path tasks by duration*

-   Bar 1:
    -   SUM\_A: Sum of (Duration \* progress) of all the tasks belonging to any of the critical paths of the project.
    -   SUM\_B: Sum the duration of all the task of any of the critical paths of the project.
    -   Bar 1: SUM\_A / SUM\_B \* 100
-   Bar 2: Select tasks with start date &lt;= current date which belongs to any critical path:
    -   For tasks with end date &lt;= current date. Compute their duration. SUM\_C
    -   For tasks with end date &gt; current date. Calculate the percentage of its duration which represents its progress. Progress\*duration/100. SUM\_D
    -   Bar 2: (SUM\_C + SUM\_D) / SUM\_B\*100

####  Progress of tasks by label (NOT WILL BE DONE)

In [LibrePlan](LibrePlan_LibrePlan) you can have the tasks with labels in order to do several groups of them and to identify them clearly. With this KPI it is proposed to analyse the progress of the tasks sharing a label with the theoretical progress the group.

-   Bar 1: Add the last progress measured of the tasks having a label assigned. Divide the total progress accumulated by the number of tasks.
-   Bar 2: Select all the tasks sharing a label and the current date:
    -   If the task has a start date &gt; current date =&gt; progress to add 0
    -   If the task has an end date &lt;= current date =&gt; progress to add 100
    -   If the task has a start date &lt; current date and end date &gt; current date =&gt; progress to add will be the percentage o the task duration which is \[current date - start date\]/\[end date - start date\]

####  Burn Down Chart (NOT WILL BE DONE)

A light description of what a burn down chart is.

<http://en.wikipedia.org/wiki/Burn_down_chart>

Proposal of implementation:

-   Ideal line `f(t)`:
    -   Addition of all the hours allocated hours = T.
    -   One point per day
    -   f(t) = T - sum(day assigments with date &lt; t)
-   Current line c(t):
    -   Addition of all the hours allocated hours = T
    -   One point each time at least progress measure for a task is had. If several measures of the spread progress for a task are had in the same day, get the higher.
    -   c(t) = T - sum\_tasks( (progress(t) - progress\_before)\*number\_hours\_task) if there is not progress before then, progress\_before = 0 \* Intrapolate function: Apply an apache match function which passes by all the points of the current line and assess the function until it crosses axis y=0.

####  Margin with deadline

This is a **time KPI**. It consists of calculating the difference with the deadline of the project if there is such a deadline. The difference is calculated in days.

It will be represented with a bar chart. This bar chart can get values positives or negatives. The meaning is:

-   Positive values shows that the project finishes before the deadline. We have margin.
-   Negative values shows that the project finishes after the deadline. We have not margin.

The bar with the positive values will be *green* and if the bar has negative values will be *red*.

The units will be relative to the duration of the project. Imagine that the duration of the project is ***D*** days. Choose to represent D at a fixed position in the horizontal axis (to avoid too much space.

Taking this into account the duration ***D*** it will be showed a size of the bar equals to:

       (Deadline of the project - Date last task of the project) / D

We should define a maximum x value to avoid paint further than a maximum. If the deviation is 1000D for instance, we do not want to paint outside the space booked to the chart.

####  Estimation accuracy

This KPI is to show the estimation accuracy of the tasks of a project. It will be done in the following way:

-   Population of tasks to have into accoun P: All the tasks that have the a progress of 100%.
-   Calculate the % of deviation quatity:

&nbsp;


    x = total number of allocated hours.
    y = total number of spent hours. This is the addition of all the work reports 
    imputing hours to the associated order element or one of its descendents 
    (look for the appropiate method to obtain it, it must be done).

    (x - y)/ y * 100 (We will show in 100 percentage)

With the number it is required to convert that continuous variable in a discrete one. We can think in streches of 10% (we can do several tests here to have a suitable number). These stretches will be the abscissa of the function to represent (horizontal axis).

The vertical axis, will be the p.d.f (probability density function) of the aleatory variable defined as the chance of a task to be in one of the stretches which define the horizontal axis. The calculos will be.


    * Calculate the number or tasks N which are placed in an abcissa interval. 
    * Represent the probability of the abcissa interval by: N / P 

    P = Population = Number of tasks with 100% of progress.

Represent this by a bar chart

Next to the chart show the mean.

####  Lead/Lag in task completion

This KPI is to show which is the probability of having a delay. Therefore, it consists of displaying the p.d.f. of the random variable "Lag in task completion".

X = Lag in task completion.

How does X takes a value for a task ? If the task is completed (100% of progress) it is got the date D1 of the last work report tracking time on the order element associated to the task or any of its descendants. Then, if D2 is the task finish time, the X = D1 - D2

The population is made up of all the task finished (with a progress of 100%)

X will be a discrete random variable and can have positive and negative values. An idea is to define the discrete values is the following:

-   Calculate the maximum delay of all the tasks. MAX
-   Calculate the minimum delay (advance if it is negative) of all tasks MIN
-   Assume a number of bars, each bar is an abcisse value. N
-   Each interval will have a size of (MAX-MIN)/N and the starting value will be the MIN

To calculate the p.d.f we have to do:


    for each task of the population calculate the value of the X variable for it.

    For an interval i [a,b], the p.d.f is: (number of tasks D1-D2 belongs to [a,b]) / P

    P = the number of task of the population.

Represent the function with a bar chart and next to the bar chart, show the mean.

####  Amount of unstaffed time in project planning

This is a resource KPI. A resource informing about resources in a project.

Unstaffed resources are the resources who are devoting hours to a project and are not planned.

The way to calculate the unstaffed hours in few words consists of querying the hours worked in the tasks of a project and classify these hours in two groups:

-   **Hours staffed**. Hours dedicated by resources were planning so.
-   **Hours unstaffed**. Hours dedicated by resources were not expected to do so.
-   **Hours not known**. These are work report hours in which the application has not data to sort them as staffed or unstaffed.

The procedure to sort a work report line as staffed or unstaffed is the following:

1.  Query all the *work report lines* belonging to any of the order elements of the the project. This must be done with a query in the DAO.
2.  The next step is to sort the *work report lines* in two types.
    1.  *Work report lines associated with a task (planning task)*. In order to do this, it is needed to see if there is a planning point in the WBS tree in the associated order element or in any of its parents. ![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Take into account that this is scenario dependent. You have to know in which scenario are you connected to know the planning points.
    2.  *Work report lines not associated with a task*. These are the work report lines in which the associated order element in the scenario is not a planning point and there is not a planning point in the wbs tree above it. All these hours will be added as **hours not known**.

With the set of hours known as **work report lines associated with a task (planning task)** it is needed to continue sorting them. For doing that it is needed to access to the resource allocations of the associated tasks. There are two types of allocations (**generic allocations** and **specific allocations**) and depending on the type the procedure to set the hours as staffed or not is different. One task can have one or more resource allocations and the algorithm is the following: *If the work report line is regarded as staffed for at least one of the resource allocations of the task, then the hours of the work report line are sorted as staffed*.

***Procedure to sort as staffed the hours for specific allocations***

In this case the method is simple. If the resource associated in the work report line is the one of the specific allocation, then the work report line is staffed.

***Procedure to sort as as staffed the hours for generic allocation***

If the resource associated to the work report line satisfies all the criteria configured in the resource allocation between the start date and the end date of the task, then the hours of the work report line are regarded as staffed.

Now, having sorted the hours as staffed, unstaffed and unknown, we have the conditions to represent them in a chart.

Two charts are proposed:

-   A pie chart to show the percentage of hours of each type.
-   Two use an histogram bar chart to know how the *staffed, unstaffed and unknown* hours worked are represented in the time. The procedure would be:
    -   To have a parameter to set the number of bar charts **N**.
    -   To divide the horizontal axis of the project in **N** intervals from the total amount of time \[min(first date of work reportline devoted to the project, first allocated hour to the project), max(last date of work report line devoted to the project, last allocated hour to the project (day assignment)\]
    -   Compute the number of *staffed, unstaffed and unknown hours* in each interval.
    -   Represent the number of hours in a bar with three sections (one bar with three colors). One color per type of allocated hour.

###  User stories

-   [ItEr75S27PerProjectDashboard](LibrePlan_ItEr75S27PerProjectDashboard)
-   [LibrePlanItEr76S06PerProjectDashboardItEr75S27](/twiki/bin/view/Trash/LibrePlanItEr76S06PerProjectDashboardItEr75S27)

###  Tasks in this story

| [Tasks](LibrePlan_AnA14S01PerProjectDashboard?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA14S01PerProjectDashboard?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA14S01PerProjectDashboard?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA14S01PerProjectDashboard?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA14S01PerProjectDashboard?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA14S01PerProjectDashboard?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA14S01PerProjectDashboard?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA14S01PerProjectDashboard?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA14S01PerProjectDashboard?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA14S01PerProjectDashboard?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA14S01PerProjectDashboard?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Task                                                                                                     | 20                                                                                                     | 20                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Number of tasks by status](LibrePlan_AnA14S01PerProjectDashboard#TasK1)                                     |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 20                                                                                                     | 20                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Deadline violation KPI](LibrePlan_AnA14S01PerProjectDashboard#TasK2)                                        |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 20                                                                                                     | 20                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Global progress of the project](LibrePlan_AnA14S01PerProjectDashboard#TasK3)                                |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 20                                                                                                     | 20                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Progress of tasks by label](LibrePlan_AnA14S01PerProjectDashboard#TasK4)                                    |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 20                                                                                                     | 20                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Burn Down Chart](LibrePlan_AnA14S01PerProjectDashboard#TasK5)                                               |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 10                                                                                                     | 10                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Margin with deadline](LibrePlan_AnA14S01PerProjectDashboard#TasK6)                                          |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 10                                                                                                     | 10                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Estimation accuracy](LibrePlan_AnA14S01PerProjectDashboard#TasK7)                                           |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 10                                                                                                     | 10                                                                                                       | 0                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Lead/Lag in task completion](LibrePlan_AnA14S01PerProjectDashboard#TasK8)                                   |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 20                                                                                                     | 0                                                                                                        | 20                                                                                                       | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [NachoBarrientos](Main_NachoBarrientos)                                                                      | [Amount of unstaffed time in project planning](LibrePlan_AnA14S01PerProjectDashboard#TasK9)                  |                                                                                                               |                                                                                                                 |                                                                                                              |

###  Total Hours in this Story

| [User](LibrePlan_AnA14S01PerProjectDashboard?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA14S01PerProjectDashboard?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA14S01PerProjectDashboard?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA14S01PerProjectDashboard?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [NachoBarrientos](Main_NachoBarrientos)                                                                 | 130                                                                                                                   | 0                                                                                                                     | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                      |
| Total                                                                                                   | 130                                                                                                                   | 0                                                                                                                     | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                      |

------------------------------------------------------------------------
