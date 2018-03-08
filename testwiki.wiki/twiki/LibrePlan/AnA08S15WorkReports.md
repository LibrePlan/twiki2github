[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA08S15WorkReports](LibrePlan_AnA08S15WorkReports "Topic revision: 4 (23 Jan 2012 - 18:12:43)") (23 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA08S15WorkReports?t=1520344050 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S15WorkReports "Attach an image or document to this topic")  

 [AnA08S15WorkReports](LibrePlan_AnA08S15WorkReports)
=====================================================

|                        |                                                      |
|------------------------|------------------------------------------------------|
| Story summary          | Work Reports                                         |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)           |
| FEA                    | [AnA08S15WorkReports](LibrePlan_AnA08S15WorkReports) |
| Story Lead             |                                                      |
| Next Story             |                                                      |
| Passed acceptance test | No                                                   |

###  Tasks

####  Improve work report lines filtering and report output

For users it is important that when you specify the filtering for a task, container or project, you get not only the direct hours assigned but the indirect hours.

So, in order to allow this, a new filtering option must be included to the filter. It will consist of a selector with 3 values:

-   All
-   Direct
-   Indirect

The default value will be **All** and the behavior of each filtering option will be the following:

-   **All**. If **all** is selected and a filter by task is used then the output must include not only the work report lines imputing directly to the task but also include the work report lines imputing to any of the descendants of the task selected in the filter.
-   **Direct**. If **direct** is selected in the filter of the work report lines and a task is selected for filtering, just the work report lines imputing directly to the task are selected. This means that if the task is a container, the indirect work report lines are not extracted to show in the result.
-   **Indirect**. If **indirect** is selected in the filter of work report lines and a task is selected for filtering, only the work report lines imputing to the descendants of the task selected for filtering are showed.

In this task a new column will be included in the output table with the work report lines result of the search. This new column will be defined by:

-   Title of the column: Type
-   Content of the column: All, Direct, Indirect

Another thing to do is to increase to **15** the number of results to show per page (currently is 10 rows).

As last point of this task a final line summing up the total amount of hours of the work report lines must be included. This final line must be placed outside the table with the list of work report lines result of the search query with the filter input parameters.

####  Add button to copy work report line

Pending to define behavior.

###  User stories

-   [ItEr76S11WorkReports](LibrePlan_ItEr76S11WorkReports)

###  Tasks in this story

| [Tasks](LibrePlan_AnA08S15WorkReports?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA08S15WorkReports?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA08S15WorkReports?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA08S15WorkReports?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA08S15WorkReports?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA08S15WorkReports?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA08S15WorkReports?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA08S15WorkReports?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA08S15WorkReports?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA08S15WorkReports?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA08S15WorkReports?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Task                                                                                             | 15                                                                                             | 0                                                                                                | 15                                                                                               | Low                                                                                             | [ManuelRego](Main_ManuelRego)                                                                       | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                           | [Improve work report lines filtering and report output](LibrePlan_AnA08S15WorkReports#TasK1)         |                                                                                                       |                                                                                                         |                                                                                                      |
| Task                                                                                             | 15                                                                                             | 0                                                                                                | 15                                                                                               | Low                                                                                             | [ManuelRego](Main_ManuelRego)                                                                       | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                           | [Add button to copy work report line](LibrePlan_AnA08S15WorkReports#TasK2)                           |                                                                                                       |                                                                                                         |                                                                                                      |

###  Total Hours in this Story

| [User](LibrePlan_AnA08S15WorkReports?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA08S15WorkReports?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA08S15WorkReports?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA08S15WorkReports?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                      | 0                                                                                                             | 0                                                                                                             | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                               |
| Total                                                                                           | 0                                                                                                             | 0                                                                                                             | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                               |

------------------------------------------------------------------------
