[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA22S02WBSReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport "Topic revision: 4 (16 Oct 2012 - 10:48:00)") (16 Oct 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA22S02WBSReport?t=1520337869 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA22S02WBSReport "Attach an image or document to this topic")

 [AnA22S02WBSReport](/twiki/LibrePlan/AnA22S02WBSReport)
=====================================================================================================



|                        |                                                                  |
|------------------------|------------------------------------------------------------------|
| Story summary          | WBS Report                                                       |
| Iteration              | [AnA22Reports](/twiki/LibrePlan/AnA22Reports)           |
| FEA                    | [AnA22S02WBSReport](/twiki/LibrePlan/AnA22S02WBSReport) |
| Story Lead             |                                                                  |
| Next Story             |                                                                  |
| Passed acceptance test | No                                                               |

###  Tasks



####  New WBS report with information about hours

The report will include all the tasks in the WBS with the information about:

-   Estimated hours: The ones inserted in the WBS
-   Planned hours: The real hours scheduled in the Gantt
-   Imputed hours: The ones inserted in the work reports



####  Include cost information in the report

-   Budget: Estimated budget in the WBS
-   Cost:
    -   Hours cost: Cost calculated depending on resources cost categories and the imputed hours
    -   Expenses cost: Cost imputed via expenses sheets
    -   Total cost: Addition of 2 previous costs (hours + expenses)



####  Include filter by criteria and labels in the report

-   Like in other reports we should include the filter by criteria and label in this new report too as in some cases it'll be useful for the end-users.
-   Both filter will be optional



####  Make optional filter by projects

-   Currently you have to choose a project in order to generate this report.
-   We'll remove that restriction in order to allow the report generation for all the tasks in any project (this could be very powerful combined with criteria and labels filters).
-   The project name will be appended to the task name in each row.

###  User stories

-   [ItEr77S09WBSReport](/twiki/LibrePlan/ItEr77S09WBSReport)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S02WBSReport?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                               | 10                                                                                                                                               | 10                                                                                                                                                 | 0                                                                                                                                                  | Low                                                                                                                                               | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [New WBS report with information about hours](/twiki/LibrePlan/AnA22S02WBSReport#TasK1)                                                       |                                                                                                                                                         |                                                                                                                                                           |                                                                                                                                                        |
| Task                                                                                                                                               | 5                                                                                                                                                | 5                                                                                                                                                  | 0                                                                                                                                                  | Low                                                                                                                                               | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [Include cost information in the report](/twiki/LibrePlan/AnA22S02WBSReport#TasK2)                                                            |                                                                                                                                                         |                                                                                                                                                           |                                                                                                                                                        |
| Task                                                                                                                                               | 7                                                                                                                                                | 7                                                                                                                                                  | 0                                                                                                                                                  | Low                                                                                                                                               | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [Include filter by criteria and labels in the report](/twiki/LibrePlan/AnA22S02WBSReport#TasK3)                                               |                                                                                                                                                         |                                                                                                                                                           |                                                                                                                                                        |
| Task                                                                                                                                               | 7                                                                                                                                                | 7                                                                                                                                                  | 0                                                                                                                                                  | Low                                                                                                                                               | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                          | [Make optional filter by projects](/twiki/LibrePlan/AnA22S02WBSReport#TasK4)                                                                  |                                                                                                                                                         |                                                                                                                                                           |                                                                                                                                                        |


