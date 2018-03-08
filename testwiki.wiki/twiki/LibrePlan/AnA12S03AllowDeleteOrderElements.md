[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA12S03AllowDeleteOrderElements](LibrePlan_AnA12S03AllowDeleteOrderElements "Topic revision: 1 (05 Nov 2012 - 10:14:14)") (05 Nov 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA12S03AllowDeleteOrderElements?t=1520344058 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA12S03AllowDeleteOrderElements "Attach an image or document to this topic")  

 [AnA12S03AllowDeleteOrderElements](LibrePlan_AnA12S03AllowDeleteOrderElements)
===============================================================================

|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Allow Delete Order Elements From Web Services                                  |
| Iteration              | [AnA12WebServices](LibrePlan_AnA12WebServices)                                 |
| FEA                    | [AnA12S03AllowDeleteOrderElements](LibrePlan_AnA12S03AllowDeleteOrderElements) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

###  Tasks

####  Add delete operation for order elements from web services

The behavior of the DELETE operation in [LibrePlan](LibrePlan_LibrePlan) that will be implemented will be the next one:

-   It will delete the order element in the WBS and all its associated configuration: criteria requirements, label assignments, progress measurements, quality forms and material requirements.
-   It will delete the task in the planning if the order element to remove is a planning point or if it is an ancestor of a planning point.
-   It will erase the incoming dependencies to the task in the Gantt and the outgoing dependencies too.
-   If the order element to remove in the WBS has children elements (it is a WBS container), the service will delete them in cascade.
-   If the order element to delete is inside a container and is its only child, we will convert the container in an order line. A container cannot be empty, it has to have always inner tasks.
-   If the order element to delete is the project order (the root WBS element) all the project will be removed.

As validation condition, the DELETE order web service will throw an error message in the order element to delete or one of its children has time tracked (work hours have been tallied as devoted or) or expenses.

###  User stories

-   [ItEr77S13AllowDeleteOrderElements](LibrePlan_ItEr77S13AllowDeleteOrderElements)

###  Tasks in this story

| [Tasks](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA12S03AllowDeleteOrderElements?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                          | 7                                                                                                           | 7                                                                                                             | 0                                                                                                             | Low                                                                                                          | [ManuelRego](Main_ManuelRego)                                                                                    | [ManuelRego](Main_ManuelRego)                                                                                     | [Add delete operation for order elements from web services](LibrePlan_AnA12S03AllowDeleteOrderElements#TasK1)     |                                                                                                                    |                                                                                                                      |                                                                                                                   |
