[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA14S02OrganizingPerProjectDashboard](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard "Topic revision: 7 (11 Sep 2012 - 17:11:20)") (11 Sep 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA14S02OrganizingPerProjectDashboard?t=1520337858 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA14S02OrganizingPerProjectDashboard "Attach an image or document to this topic")

 [AnA14S02OrganizingPerProjectDashboard](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard)
============================================================================================================================================================



|                        |                                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------------|
| Story summary          | Organizing per project dashboard                                                                         |
| Iteration              | [AnA14ProjectsDashboards](/twiki/LibrePlan/AnA14ProjectsDashboards)                             |
| FEA                    | [AnA14S02OrganizingPerProjectDashboard](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard) |
| Story Lead             |                                                                                                          |
| Next Story             |                                                                                                          |
| Passed acceptance test | No                                                                                                       |

###  Tasks

In this analysis story are included the things to complete the KPI module for LibrePlan version 1.3



####  Solve the Java exceptions when the data for the charts are not available

There are exceptions when you visit the *Order Dashboard*. The charts must not fail when:

-   There is not any task with progress = 100%.
-   All the tasks have 100% of progress
-   There are tasks without work reports devoting time to them.

Change also the name of *Order Dashboard* for *Dashboard*. Look for an icon for it.



####  Revamping the layout for the project dashboard first section (progress)

The KPI developed will be arranged in four sections:

-   Progress.
-   Time
-   Resources
-   Cost

In this task will be created the first area (horizontal area). The title will be ***Progress***. The area will have two KPI charts:

-   The global progress chart
-   The task status chart.

The task status chart must be completed with a bottom text area where the number of tasks by status is summed up. It will be:

    The project consists of X tasks and the number of tasks by status is:
       * N1 tasks are finished.
       * N2 tasks are blocked
       * N3 tasks are in progress
       * N4 tasks are ready to start.



####  Revamping the layout for the project dashboard second section (Time section)

This second area will have the title of *Time* and there will be included in it three indicators.

***Lead/Lag in task completion***

The original specification is at [AnA14S01PerProjectDashboard\#TasK8](/twiki/LibrePlan/AnA14S01PerProjectDashboard#TasK8)

This KPI has to be slightly corrected in the following points:

-   Title: *Day histogram in task completion*.
-   Label Y axis: *Number of ended tasks (X)*. Replace X with the number of tasks taken into account for the calculation.
-   Label X axis: \_Days (Negative values represent days ahead of time).

Besides it will be changed how this KPI is calculated:

-   It will be always represented 6 bars. Now there is a problem if there is only one finished task. It is only represented a bar very wide.
    -   For the case of one finished task, complete do the calculations to get 6 bars of one day duration in the next way.
        -   Minimum value: delay in days of the finished task - 2
        -   Maximum value: delay in days of the finished task + 3
-   The label for each bar will be: `a,b days` where
    -   `a` is the bottom limit of the bar
    -   `b` is the upper limit of the bar
-   Do the calculations in order that the bottom and upper limit of each interval - bar - is integer days.
-   Finally it is needed to change the calculations so that in the vertical axis is represented the total number of tasks. So, it is proposed no to use probabilities but number of hours.

***Deadline violation KPI***

About this pie chart, it has to be included in this area (*Time*), but no modifications are needed.

***Margin with dealine***

In this case this is going to be just a value. The current representation in chart form is confusing. So, it is wanted to show it just as a number. It is originally analysed at [AnA14S01PerProjectDashboard\#TasK6](/twiki/LibrePlan/AnA14S01PerProjectDashboard#TasK6)

It only was calculated in a relative way according to the duration of the project. Now, it is suggested to complete this information with the absolut information too. It would be:


    The project finishes before the deadline with a margin of D days. This represents finishing  d times ahead of time the duration of the project.

    or 

    The project finishes after the dealine D days late. This represents ending d times late the duration of the project. 



####  Revamping the layout for the project dashboard third section (Resources)

This section will have the title *Resources*

It will include two KPIs:

***Estimation accuracy***

It is analysed at [AnA14S01PerProjectDashboard\#TasK7](/twiki/LibrePlan/AnA14S01PerProjectDashboard#TasK7).

Several changes will have to be done to improve the user experience of this KPI.

-   New title and labels:
    -   Title: *Estimation accuracy histogram*.
    -   Label Y axis: *Number of ended tasks (X)*.
    -   Label X axis: *% of deviation (Negative values represent spending less time than expected)*.
-   It will be always represented 6 bars. Do this dynamic, now they the number of bars is fixed.
    -   For the case of one finished task, complete do the calculations to get 6 bars of one day duration in the next way.
        -   Minimum value: delay in days of the finished task - 20
        -   Maximum value: delay in days of the finished task + 30
-   The label for each bar will be: `a,b%` where
    -   `a` is the bottom limit of the bar
    -   `b` is the upper limit of the bar \* Do the intervals with integer numbers, no decimal ones. \* Finally it is needed to change the calculations so that in the vertical axis is represented the total number of tasks. So, it is proposed no to use probabilities but number of hours.

 ***Resource usage ratios***

There will be 2 ratios related with resource usage:

-   **Availability ratio**:
    -   It will be calculated using the following formula:

            availability = 1 - (load / capacity)

        Where `load` doesn't include the overload.

    -   The possible values are between 0 (fully assigned, even when you have overload) and 1 (no assigned)
    -   It'll be shown as a percentage between 0% and 100%

-   **Overtime ratio**:
    -   It will be calculated using the following formula:

            overtime = overload / (load + overload)

    -   Then result will be always positive and starting in 0 which means that you don't have overload.
    -   It'll be shown as a percentage starting in 0%
    -   If the value is 0% it will be shown a ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE") (because of you don't have overload). Otherwise it'll show a ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")



####  Revamping the layout for the project dashboard forth section (Cost)

Represent in a table the value of the earned value indicators related to the cost of the project. They will be represented the following indicators:

-   Cost Variance(current date) = BCWP(current date) - ACWP (current date).
-   CPI (Cost Performance Index) = BCWP / ACWP
-   BAC (Budget At Completion) = The total value of BCWS at the end of the project.
-   EAC (Estimate At Completion) = AC + (BAC ­ EV)/CPI = BAC/CPI
-   VAC (Variance At Completion) = BAC - ­ EAC

Do a presentation of the information in a board in the sense that most important one will be the VAC. Represent the VAC absolut values and also in percentage of the total value of the project: BAC - EAC / BAC



####  Remove bottom tab Overall progress in Planning view

It is needed to remove this tab and its content because it is allready represented in the *Dashboard*



####  Create flags summing up the status of the project

This task consists of adding 4 flags in the class `Order` to store the global status of the project according to the KPIs. The four flags are the following:

-   Progress. It is to sum up the status of the project according to its progress.
-   Time. It is to sum up the status of the project according of its time schedule, if the project is going to finish on time or not.
-   Resources. It is to sum up the status of the project according to the resource allocations.
-   Cost. It is to sum up the status of the project according to how much is costing.

These flags will be an enum with the following 4 possible values to store:

-   NotApplicable
-   Bad - 1
-   Expected -2
-   Good - 3

This four flags will be calculated only when a project is saved from the any of the project planning perspectives.

To calculate each flag it is calculated an average of the KPIs which there is in each area. A result of:

-   From 1 to 1.5 -&gt; Bad.
-   From 1.5 to 2.5 -&gt; Expected
-   From 2.5 to 3 -&gt; Good.

***Progress***

-   Global progress. \* Bad. &gt; 20% of delay in progress. \* Expected. 20% - 0% of delay in progress \* Good. &lt; 0%
-   Task status. \* Bad. &gt; 20% of blocked tasks. \* Expected. 20% -10% of delay in progress \* Good - 10% - 0%

***Time***

...

###  User stories

-   [ItEr76S15OrganizingPerProjectDashboard](/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                   | 4                                                                                                                                                                    | 4                                                                                                                                                                      | 0                                                                                                                                                                      | Low                                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                           |                                                                                                                                                                            | [Solve the Java exceptions when the data for the charts are not available](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK1)                          |                                                                                                                                                                             |                                                                                                                                                                               |                                                                                                                                                                            |
| Task                                                                                                                                                                   | 14                                                                                                                                                                   | 14                                                                                                                                                                     | 0                                                                                                                                                                      | Low                                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                           |                                                                                                                                                                            | [Revamping the layout for the project dashboard first section (progress)](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK2)                           |                                                                                                                                                                             |                                                                                                                                                                               |                                                                                                                                                                            |
| Task                                                                                                                                                                   | 20                                                                                                                                                                   | 20                                                                                                                                                                     | 0                                                                                                                                                                      | Low                                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                           |                                                                                                                                                                            | [Revamping the layout for the project dashboard third section (Resources)](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK3)                          |                                                                                                                                                                             |                                                                                                                                                                               |                                                                                                                                                                            |
| Task                                                                                                                                                                   | 20                                                                                                                                                                   | 20                                                                                                                                                                     | 0                                                                                                                                                                      | Low                                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                           |                                                                                                                                                                            | [Revamping the layout for the project dashboard forth section (Cost)](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK4)                               |                                                                                                                                                                             |                                                                                                                                                                               |                                                                                                                                                                            |
| Task                                                                                                                                                                   | 4                                                                                                                                                                    | 4                                                                                                                                                                      | 0                                                                                                                                                                      | Low                                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                           |                                                                                                                                                                            | [Remove bottom tab Overall progress in Planning view](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK5)                                               |                                                                                                                                                                             |                                                                                                                                                                               |                                                                                                                                                                            |
| Task                                                                                                                                                                   | 14                                                                                                                                                                   | 14                                                                                                                                                                     | 0                                                                                                                                                                      | Low                                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                           |                                                                                                                                                                            | [Create flags summing up the status of the project](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK6)                                                 |                                                                                                                                                                             |                                                                                                                                                                               |                                                                                                                                                                            |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                       | 76                                                                                                                                                                                  | 0                                                                                                                                                                                   | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                    |
| Total                                                                                                                                                                 | 76                                                                                                                                                                                  | 0                                                                                                                                                                                   | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                    |

------------------------------------------------------------------------
