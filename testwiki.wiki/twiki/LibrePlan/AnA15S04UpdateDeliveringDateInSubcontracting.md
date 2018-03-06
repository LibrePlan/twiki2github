[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA15S04UpdateDeliveringDateInSubcontracting](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting "Topic revision: 10 (28 Mar 2012 - 17:29:40)") (28 Mar 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?t=1520337860 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting "Attach an image or document to this topic")

 [AnA15S04UpdateDeliveringDateInSubcontracting](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting)
==========================================================================================================================================================================



|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Story summary          | Update delivering date in subcontracting                                                                               |
| Iteration              | [AnA15SubcontractorModule](/twiki/LibrePlan/AnA15SubcontractorModule)                                         |
| FEA                    | [AnA15S04UpdateDeliveringDateInSubcontracting](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting) |
| Story Lead             |                                                                                                                        |
| Next Story             |                                                                                                                        |
| Passed acceptance test | No                                                                                                                     |

###  Tasks



####  Creation of new field in Order entity

This task consists of creating a new field in the `Order` entity to store the *delivering dates communications* from the customers in the subcontracted projects.

This field `deliveringdates` will be a list (**sorted**) component of elements of the class `DeadlineCommunication`.This class will have two fields:

-   `SaveDate`. It is the date at which a delivering date was saved. This field is the one that is going to be used to sort the list
-   `DeliverDate`. Date at which the subcontractor should finish the project.



####  Creation of new field in SubcontractedTaskData and refactor subcontractor interface

This task consists of creating a new field in the SubcontractedTaskData called `requiredDeliveringDates` and that will be a list (**sorted**) of elements of type `SubcontractorDeliverDate` with the following fields:

-   `SaveDate`. Date at which the `RequiredDeliveringDate` is added.
-   `SubcontractorDeliverDate` Date at which the customer should deliver the project decided at `SaveDate`.
-   `CommunicationDate`. Date at which the `SubcontractorDeliverDate` has been communicated to the subcontractor. If it has not been communicated yet it will be null.

Once created this field, it is needed to revamp and fix several issues in the *subcontract pop-up*, that is, the pop-up in which a task is subcontracted. the changes that it is needed to do are:

-   Change the area of the **End date** with the following modifications. Add an area instead of the **End date** with the following characteristics:
    -   Name of the area: Deliver date
    -   Insise a line:
        -   Label: New deliver date
        -   Date component to catch the new date.
        -   Button **Add**
    -   Add a table with all the `SubcontractorDeliverDate` values of the field `requiredDeliveringDates`. Each element of the table will have 3 columns with the following information:
        -   Save Date (sorted by this field). Label.
        -   Deliver Date. Label.
        -   Communication Date
        -   A delete button that will be enabled just in the last row. The one which has the `CommunnicationDate` null.
    -   It will only be possible to add a *Deliver Date* if all the deliver date exiting in the table have a `CommunicationDate` not null.
    -   The first time we are subcontracting a task it will be added a `SubcontractorDeliverDate` with value `DeliverDate` the end date of the task.
    -   Once subcontracted a task, on adding a new `SubcontractorDeliverDate` it will be updated too the end date of the subcontracted task and the gantt will be properly updated with this change (should be automatic).

-   Once a subcontracted task has been sent the first time it will be needed to do read-only the following fields in the subcontraction pop-up:
    -   External company.
    -   Work description.
    -   Subcontract price
    -   Subcontract code
    -   Export options.
-   The fields `Subcontracting date` and `Subcontracting communication date` of the *subcontractor pop-up* must be converted in labels because they are always read only fields.

It will be needed as part of this task too to modify the subcontractor communication window to send the tasks to the subcontractors by web services. The modificacion will consist of updating the `CommunicationDate` of the first `SubcontractorDeliverDate` of the list `requiredDeliveringDates` of the task sent to the subcontractor after being this operation successful.



####  Create new subcontractor communication, sending of delivering date update

Currently there is only posible to send an initial communication with the task to be subcontracted. This task consists of allowing to send an update of the deliver date for the subcontractor.

A first to do is to modify the enum `SubcontractState` of the class `SubcontractedTaskDate`:

-   Modify the state ***PENDING*** to be ***PENDING\_INITIAL\_SEND***.
-   Create a new state ***PENDING\_UDPATE\_DELIVERING\_DATE***.

Now it has to be modified the list of task in order to be sortable by `State` but **not** using alphabetic sort. The first task will be the task with states:

-   PENDING
-   PENDING\_UPDATE\_DELIVERING\_DATE.

It is needed to implement a new XML message to represent an update of delivering date and that will be send to update this information. It will built with a DTO called `UpdateDeliveringDateDTO` and it will have the following fields:

-   `CustomerReference`. This field will be the *subcontractedCode* of the subcontracted task.
-   `ExternalCode`. This field will be the *code* field of the `OrderElement` associated to the subcontracted task.
-   `CompanyNif`. It will be the company id of the company making the subcontraction.
-   `DeliverDate`. It will be the `DeliverDate` of the element `CustomerDeliverDate` of the field ***requiredDeliveringDates*** not sent (`CommunicationDate` is null). It is only possible to have a `CustomerDeliverDate` with `CommunicationDate` null.

This message will be send from the *subcontracted tasks* list with the state of one row is *PENDING\_UPDATE\_DELIVERING\_DATE*. The process of send the message describe imply to do the next things:

-   Sent the message to the subcontractor.
-   Change the state of the object `SubcontractedTaskData` to be *Successful Sent*, save in the `CommunicationDate` of the `CustomerDeliverDate` sent to the subcontractor the current date (precission of days), and update the field `subcontractCommunicationDate`, the current date.



####  Delivering date update reception

This consists of receiving in the subcontractor LibrePlan deployment the communication of the an update on the delivering date for a subcontracted project.

The incoming web service will have the following specs:

-   Authentication in the web service
-   Identify the order that is needed to update. The query to identify the order will be the following: Search the order which has in the field `ExternalCode` the value of `ExternalCode` of the `UpdateDeliveringDateDTO`. It has to be checked too tha this order has as customer a company which satisfies two conditions:
    -   It is a company that is a client (customer).
    -   The ID of this company is the one that comes in the `UpdateDeliveringDateDTO`.
-   If the identification has been right it will be needed to get the field created int the task [AnA15S04UpdateDeliveringDateInSubcontracting\#TasK1](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting#TasK1) called `deliveringdates` and a new value will be added to this list. With the numbers:
    -   `SaveDate`. The current date.
    -   `DeliverDate`. The `DeliverDate` which comes in the object `UpdateDeliveringDateDTO` on the web service.

It will be needed to revamp the interface of the **General Data** tab in the **Project Details** perspective in a project. The new design of this window will consist of doing some areas:

-   **Identification**. Under this section, the following fields will be placed:
    -   Name
    -   Code and Generate code
    -   Responsible
    -   Description
    -   Status
-   **Customer information**.
    -   Include a field called Project Type. It will be a label and there will be two possible project types: \* Subcontracted by client. In this case the external code is not null. In the case of a subcontracted by client project it will be needed to put in read only the fiedls customer, customer reference too. \* Regular project. In this case the external code is null.
    -   External code
    -   Customer
    -   Customer reference
    -   Delivering dates. At this point it will be added a table with all the delivering dates that have been sent so far. A table with two columns:
        -   Communication date. It will be a label. Include it in hour minute precission
        -   Delivery date. It will be a label.
        -   Current. Include a checkbox to show which one is the current. The current is the one with the older communication date.
-   **Planning Configuration**.
    -   Start date.
    -   Deadline.
    -   Calendar
    -   Scheduling mode.
    -   Dependency have priority
-   **Cost**
    -   Budget.
    -   Hours.



####  Create new incomming communication type for update of delivering date

This task consists of creating a new `CustomerCommunication` to track the updates of the delivering dates in subcontracting. The fields for this new type of `CustomerCommunication` are the following:

-   Project Deadline. Save here the delivery date. Change the name of the column to be `DeliveryDate`
-   Communication Type. A new value in the enum, **Update Delivering Date**
-   Communication Date. Date at which happens the communication.
-   Reviewed. Initialize to false.

The data that will be in each column in the :

-   Communication Type. Got from CustomerCommunication
-   Project Name. Name of the project, got from associated Order to the CustomerCommunication entity
-   Deadline. Chage the name of this column to be ***Delivery Date***. Show here the `DeliveryDate` of the object CustomerCommunication
-   Project Code. Code of the project hired. Got from Order.
-   Customer. Name of the customer who hires the project. Got through CustomerCommunication.
-   Communication Date. Date the communication happened. Got from CustomerCommunication.
-   Reviewed. Checkbox showing that the line was reviewed. Got from CustomerCommunication.
-   Operations. Edit button. On pressing on it, it is opened the ***project details*** perspective of the project.

It has to be changed

###  User stories

-   [ItEr75S32AnA15S04UpdateDeliveringDateInSubcontracting](/twiki/LibrePlan/ItEr75S32AnA15S04UpdateDeliveringDateInSubcontracting)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                          | 4                                                                                                                                                                           | 4                                                                                                                                                                             | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Creation of new field in Order entity](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting#TasK1)                                                             |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |
| Task                                                                                                                                                                          | 10                                                                                                                                                                          | 10                                                                                                                                                                            | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Creation of new field in SubcontractedTaskData and refactor subcontractor interface](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting#TasK2)               |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |
| Task                                                                                                                                                                          | 10                                                                                                                                                                          | 14                                                                                                                                                                            | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Create new subcontractor communication, sending of delivering date update](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting#TasK3)                         |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |
| Task                                                                                                                                                                          | 10                                                                                                                                                                          | 9                                                                                                                                                                             | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Delivering date update reception](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting#TasK4)                                                                  |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |
| Task                                                                                                                                                                          | 10                                                                                                                                                                          | 9                                                                                                                                                                             | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Create new incomming communication type for update of delivering date](/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting#TasK5)                             |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S04UpdateDeliveringDateInSubcontracting?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                            | 46                                                                                                                                                                                         | 0                                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                           |
| Total                                                                                                                                                                        | 46                                                                                                                                                                                         | 0                                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                           |

------------------------------------------------------------------------
