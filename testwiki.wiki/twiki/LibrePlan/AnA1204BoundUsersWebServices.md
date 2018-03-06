[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA1204BoundUsersWebServices](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices "Topic revision: 1 (08 Nov 2012 - 11:43:31)") (08 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA1204BoundUsersWebServices?t=1520337853 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA1204BoundUsersWebServices "Attach an image or document to this topic")

 [AnA1204BoundUsersWebServices](/twiki/LibrePlan/AnA1204BoundUsersWebServices)
======================================================================================================================================



|                        |                                                                                        |
|------------------------|----------------------------------------------------------------------------------------|
| Story summary          | Bound Users Web Services                                                               |
| Iteration              | [AnA12WebServices](/twiki/LibrePlan/AnA12WebServices)                         |
| FEA                    | [AnA1204BoundUsersWebServices](/twiki/LibrePlan/AnA1204BoundUsersWebServices) |
| Story Lead             |                                                                                        |
| Next Story             |                                                                                        |
| Passed acceptance test | No                                                                                     |

###  Tasks



####  Service to get tasks assigned to a bound user

It should return the information in **My tasks** area in the user dashboard.

The service should be able to be called with the credentials of a bound user.



####  Service to get personal timesheets data of a task

It'll return the list of days and hours reported on a given task in personal timesheets. The user should send as GET parameter the task code (`OrderElement` code) and the list will return the worked hours registered in the personal timesheets of that user for the task.

Again a bound user should be able to call this service.



####  Service to import data for personal timesheets

In this case it'll be implemented a `POST` service that will allow to a bound user report hours in some of his/her assigned tasks. The service will receive a XML with the data and it'll created/modify the personal timesheets information as required.

Again a bound user should be able to call this service.

###  User stories

-   [ItEr77S14BoundUsersWebServices](/twiki/LibrePlan/ItEr77S14BoundUsersWebServices)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA1204BoundUsersWebServices?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                          | 1                                                                                                                                                           | 1                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                     | [Service to get tasks assigned to a bound user](/twiki/LibrePlan/AnA1204BoundUsersWebServices#TasK1)                                                     |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |
| Task                                                                                                                                                          | 1                                                                                                                                                           | 1                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                     | [Service to get personal timesheets data of a task](/twiki/LibrePlan/AnA1204BoundUsersWebServices#TasK2)                                                 |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |
| Task                                                                                                                                                          | 1                                                                                                                                                           | 1                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                     | [Service to import data for personal timesheets](/twiki/LibrePlan/AnA1204BoundUsersWebServices#TasK3)                                                    |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |

