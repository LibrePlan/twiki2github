[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA12S03AllowDeleteOrderElements](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements "Topic revision: 1 (05 Nov 2012 - 10:14:14)") (05 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA12S03AllowDeleteOrderElements?t=1520337854 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA12S03AllowDeleteOrderElements "Attach an image or document to this topic")

 [AnA12S03AllowDeleteOrderElements](/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Allow Delete Order Elements From Web Services                                                  |
| Iteration              | [AnA12WebServices](/twiki/LibrePlan/AnA12WebServices)                                 |
| FEA                    | [AnA12S03AllowDeleteOrderElements](/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

###  Tasks



####  Add delete operation for order elements from web services

The behavior of the DELETE operation in [LibrePlan](/twiki/LibrePlan/LibrePlan) that will be implemented will be the next one:

-   It will delete the order element in the WBS and all its associated configuration: criteria requirements, label assignments, progress measurements, quality forms and material requirements.
-   It will delete the task in the planning if the order element to remove is a planning point or if it is an ancestor of a planning point.
-   It will erase the incoming dependencies to the task in the Gantt and the outgoing dependencies too.
-   If the order element to remove in the WBS has children elements (it is a WBS container), the service will delete them in cascade.
-   If the order element to delete is inside a container and is its only child, we will convert the container in an order line. A container cannot be empty, it has to have always inner tasks.
-   If the order element to delete is the project order (the root WBS element) all the project will be removed.

As validation condition, the DELETE order web service will throw an error message in the order element to delete or one of its children has time tracked (work hours have been tallied as devoted or) or expenses.

###  User stories

-   [ItEr77S13AllowDeleteOrderElements](/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 7                                                                                                                                                               | 7                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                        | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Add delete operation for order elements from web services](/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements#TasK1)                                         |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |


