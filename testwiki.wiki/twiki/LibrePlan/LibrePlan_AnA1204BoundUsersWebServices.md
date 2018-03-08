[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA1204BoundUsersWebServices](LibrePlan_AnA1204BoundUsersWebServices "Topic revision: 1 (08 Nov 2012 - 11:43:31)") (08 Nov 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA1204BoundUsersWebServices?t=1520344057 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA1204BoundUsersWebServices "Attach an image or document to this topic")  

 [AnA1204BoundUsersWebServices](LibrePlan_AnA1204BoundUsersWebServices)
=======================================================================

|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | Bound Users Web Services                                               |
| Iteration              | [AnA12WebServices](LibrePlan_AnA12WebServices)                         |
| FEA                    | [AnA1204BoundUsersWebServices](LibrePlan_AnA1204BoundUsersWebServices) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

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

-   [ItEr77S14BoundUsersWebServices](LibrePlan_ItEr77S14BoundUsersWebServices)

###  Tasks in this story

| [Tasks](LibrePlan_AnA1204BoundUsersWebServices?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA1204BoundUsersWebServices?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA1204BoundUsersWebServices?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA1204BoundUsersWebServices?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA1204BoundUsersWebServices?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA1204BoundUsersWebServices?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA1204BoundUsersWebServices?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA1204BoundUsersWebServices?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA1204BoundUsersWebServices?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA1204BoundUsersWebServices?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA1204BoundUsersWebServices?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task                                                                                                      | 1                                                                                                       | 1                                                                                                         | 0                                                                                                         | Low                                                                                                      | [ManuelRego](Main_ManuelRego)                                                                                | [ManuelRego](Main_ManuelRego)                                                                                 | [Service to get tasks assigned to a bound user](LibrePlan_AnA1204BoundUsersWebServices#TasK1)                 |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 1                                                                                                       | 1                                                                                                         | 0                                                                                                         | Low                                                                                                      | [ManuelRego](Main_ManuelRego)                                                                                | [ManuelRego](Main_ManuelRego)                                                                                 | [Service to get personal timesheets data of a task](LibrePlan_AnA1204BoundUsersWebServices#TasK2)             |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 1                                                                                                       | 1                                                                                                         | 0                                                                                                         | Low                                                                                                      | [ManuelRego](Main_ManuelRego)                                                                                | [ManuelRego](Main_ManuelRego)                                                                                 | [Service to import data for personal timesheets](LibrePlan_AnA1204BoundUsersWebServices#TasK3)                |                                                                                                                |                                                                                                                  |                                                                                                               |
