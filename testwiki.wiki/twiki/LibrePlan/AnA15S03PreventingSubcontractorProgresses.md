[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA15S03PreventingSubcontractorProgresses](LibrePlan_AnA15S03PreventingSubcontractorProgresses "Topic revision: 6 (28 Mar 2012 - 11:24:54)") (28 Mar 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA15S03PreventingSubcontractorProgresses?t=1520344063 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA15S03PreventingSubcontractorProgresses "Attach an image or document to this topic")  

 [AnA15S03PreventingSubcontractorProgresses](LibrePlan_AnA15S03PreventingSubcontractorProgresses)
=================================================================================================

|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Preventing subcontractor progresses measurements                                                 |
| Iteration              | [AnA15SubcontractorModule](LibrePlan_AnA15SubcontractorModule)                                   |
| FEA                    | [AnA15S03PreventingSubcontractorProgresses](LibrePlan_AnA15S03PreventingSubcontractorProgresses) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

###  Tasks

####  Avoid to subcontract a task if there are subcontractor progresses incompatible with receiving progress reporting from the provider

This task consists of including on the pop-up to subcontract a task a check to control that there are not incompatible progress type assigments in the wbs which would provoke an error on receiving the progress report from the customers.

The validation has to be done on choosing the value `Subcontract` in the *Resource allocation type* combo.

The validation consists of the following points:

1.  If the task has an associated order element which is a container, check if this container has a direct or indirect progress type assigment that is of type **subcontractor**.
2.  If the task has an associated order element which is a leave, check if the `OrderLine` associated has a direct progress type assigment of type **subcontractor**.
3.  Check that the associated `OrderElement` of the task has any ancestor with a **Direct** progress assigment of type **subcontractor**.

If any of the three checks is not passed, then a message is given to the user in the pop-up and the *Resource allocation type* combo is resetted to the previous value (the one before selecting in the subcontractor option).

This validation has to be done only at interface level, the model has to keep allowing this.

####  Avoid to add subcontractor progress in a project with subcontracted tasks.

This use case of inserting a condition to allow to add a new *progress type assigment* of type **subcontractor** to an `OrderElement`. This will not be allowed if the `OrderElement` or any of its descendants has an associated task which has been subcontracted.

So, to do this, on the progress allocation pop-up (WBS or Gantt) or in the tab at `Order` level in the *Project details* perspective, it is needed to remove from the combo in which the user select the **type of progress**, the possibility to choose the value **subcontractor**.

However, this progress type assigments will be created in the process of importing the progress reports from the customers. Because of this, the solution has to be able to view a progress type assigment of type **subcontractor** and its values if they are already created. They must be rendered in read only mode, to avoid to erase a progress reported by the provider. So, in a order element which has an associated task subcontracted which has a direct progress type assigment of type subcontractor, it must be rendered in read only mode.

This validation has to be done only at interface level, the model has to keep allowing this.

In order to keep the user informed if in an order element which has an associated task subcontracted, there is the direct **subcontractor** progres type assigned with values in read only mode, a message in the top of the pop-up explaining this must be added. Message: *Subcontractor values are read only because they were reported by the subcontractor company.*

####  Avoid to delete a subcontractor progress that has been sent in subcontractor

In a subcontracted project, that is, a project which has been received from a customer, it has to be avoided to delete or modify a progress already sent, reported to the customer.

It is going to be avoided this fact by modifying the interface in ZK to disable the possibility to edit or delete these already reported progress values.

The condition which is needed to implement is:

-   Search for the date of the last reported progress to the customer of the subcontracted project that is being edited. Let's call this date D.
-   In all the progress windows (project details global tab, in the wbs pop-up or in the gantt tab) do read-only the progress measurement of type subcontractor if they have a date &lt;= D.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Besides it must be forbidden to add subcontractor progress measurements with a date &lt;= D.

###  User stories

-   [ItEr75S31PreventingSubcontractorProgresses](LibrePlan_ItEr75S31PreventingSubcontractorProgresses)
-   [ItEr76S19PreventingSubcontractorProgressesItEr75S31](LibrePlan_ItEr76S19PreventingSubcontractorProgressesItEr75S31)

###  Tasks in this story

| [Tasks](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                                                                      | [Start Date](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                   | 5                                                                                                                    | 6                                                                                                                      | 0                                                                                                                      | Low                                                                                                                   | [JavierMoran](Main_JavierMoran)                                                                                           | [SusanaMontes](Main_SusanaMontes)                                                                                          | [Avoid to subcontract a task if there are subcontractor progresses incompatible with receiving progress reporting from the provider](LibrePlan_AnA15S03PreventingSubcontractorProgresses#TasK1) |                                                                                                                             |                                                                                                                               |                                                                                                                            |
| Task                                                                                                                   | 5                                                                                                                    | 9                                                                                                                      | 0                                                                                                                      | Low                                                                                                                   | [JavierMoran](Main_JavierMoran)                                                                                           | [SusanaMontes](Main_SusanaMontes)                                                                                          | [Avoid to add subcontractor progress in a project with subcontracted tasks.](LibrePlan_AnA15S03PreventingSubcontractorProgresses#TasK2)                                                         |                                                                                                                             |                                                                                                                               |                                                                                                                            |
| Task                                                                                                                   | 6                                                                                                                    | 0                                                                                                                      | 6                                                                                                                      | Low                                                                                                                   | [JavierMoran](Main_JavierMoran)                                                                                           | [SusanaMontes](Main_SusanaMontes)                                                                                          | [Avoid to delete a subcontractor progress that has been sent in subcontractor.](LibrePlan_AnA15S03PreventingSubcontractorProgresses#TasK3)                                                      |                                                                                                                             |                                                                                                                               |                                                                                                                            |

###  Total Hours in this Story

| [User](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA15S03PreventingSubcontractorProgresses?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](Main_SusanaMontes)                                                                                     | 15                                                                                                                                  | 0                                                                                                                                   | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                    |
| Total                                                                                                                 | 15                                                                                                                                  | 0                                                                                                                                   | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                    |

------------------------------------------------------------------------
