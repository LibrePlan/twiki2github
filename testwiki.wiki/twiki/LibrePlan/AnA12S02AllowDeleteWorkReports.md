[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA12S02AllowDeleteWorkReports](LibrePlan_AnA12S02AllowDeleteWorkReports "Topic revision: 1 (27 Aug 2012 - 09:11:55)") (27 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA12S02AllowDeleteWorkReports?t=1520344057 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA12S02AllowDeleteWorkReports "Attach an image or document to this topic")  

 [AnA12S02AllowDeleteWorkReports](LibrePlan_AnA12S02AllowDeleteWorkReports)
===========================================================================

|                        |                                                                            |
|------------------------|----------------------------------------------------------------------------|
| Story summary          | Allow Delete Work Reports From Web Services                                |
| Iteration              | [AnA12WebServices](LibrePlan_AnA12WebServices)                             |
| FEA                    | [AnA12S02AllowDeleteWorkReports](LibrePlan_AnA12S02AllowDeleteWorkReports) |
| Story Lead             |                                                                            |
| Next Story             |                                                                            |
| Passed acceptance test | No                                                                         |

###  Tasks

####  Add delete operation for work reports and work report lines from web services

The feature to implement will be to include a DELETE HTTP operation to erase work report and work report lines:

-   There will be two new web services:
    -   One for deleting whole work reports
    -   Other to delete a specific work report line inside a work report

&nbsp;

-   Both web services will have as parameter the external code of the entity to erase

&nbsp;

-   If the entity is found, it will be deleted. On the contrary, if the entity does not exist, a 404 status code will be returned.

###  User stories

-   [ItEr77S06AllowDeleteWorkReports](LibrePlan_ItEr77S06AllowDeleteWorkReports)

###  Tasks in this story

| [Tasks](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                 | [Start Date](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA12S02AllowDeleteWorkReports?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                        | 5                                                                                                         | 5                                                                                                           | 0                                                                                                           | Low                                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                  | [ManuelRego](Main_ManuelRego)                                                                                   | [Add delete operation for work reports and work report lines from web services](LibrePlan_AnA12S02AllowDeleteWorkReports#TasK1) |                                                                                                                  |                                                                                                                    |                                                                                                                 |
