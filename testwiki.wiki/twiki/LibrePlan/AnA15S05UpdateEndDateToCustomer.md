[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA15S05UpdateEndDateToCustomer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer "Topic revision: 6 (15 Nov 2012 - 15:17:48)") (15 Nov 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA15S05UpdateEndDateToCustomer?t=1520337860 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA15S05UpdateEndDateToCustomer "Attach an image or document to this topic")

 [AnA15S05UpdateEndDateToCustomer](/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer)
===============================================================================================================================================



|                        |                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------|
| Story summary          | Update end date from subcontractor to customers                                              |
| Iteration              | [AnA15SubcontractorModule](/twiki/LibrePlan/AnA15SubcontractorModule)               |
| FEA                    | [AnA15S05UpdateEndDateToCustomer](/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer) |
| Story Lead             |                                                                                              |
| Next Story             |                                                                                              |
| Passed acceptance test | No                                                                                           |

###  Tasks

This set of tasks is related with adding the support to send the date at which the subcontractor is going to finish a task to the customer. This will allow him to adjust the planning and to know if the subcontractor is going to fulfill the deadline.



####  Modification of project edition to allow to save end dates to send to the customers

The first thing to do is to add to the `Order` class a new component that will be a list (sorted) of elements of the class `EndDateCommunitationToCustomer`. This class will have two fields:

-   `SaveDate`. It is the date at which the end date was saved.
-   `EndDate`. It is the date at which the subcontractors wants to say that is going to finish the project.
-   `CommunicationDate`. It is the date at which the enda date has been sent to the customer

To manage these dates it will be needed to modify the *General Data* tab of the *Project details* perspective of a project. Specifically, it will be needed to modify the *Customer information* area.

-   Put a title in the talbe of the delivery dates asked by the subcontractor. Title: Delivery dates requested by the customer.
-   In the bottom of the area *Customer information* add a new table to save the *end date communications to send to the customer*.
    -   Put a first line to add new `EndDateCommunicationToCustumer`. It will have a label **New end date for the customer**. Next to it there will be a date component. Finally there will be an **Add button**.
    -   The columns of the table will be four: Save Date, End Date, Communication Date and an operations column with a Delete button.
    -   It will be able only to have 1 end date with Communication Date not null.
    -   It will not be possible to delete an `EndCommunicationDate` already sent to the customer, that is, with communication date not null.



####  Adaptation of the XML message to send end date communications from subcontractor to customer

This task consists of making it possible to send and end date from the subcontractor to the customer.

The first thing to do is to detect that there is a new end date pending to send from a subcontractor to its customer. To do that is needed to modify the screen =Communications -&gt; Send to customers = in the following points:

-   When filling the state of the **subcontracted projects**, include in the checking if each subcontracted project has any `EndCommunicationDate` with `CommunicationDate` null.
-   Include to new status to put in the cell State:
    -   Pending update for communication date. This is put when it is needed to send only the communication date.
    -   Pending update of progress and communication date. This is put when it is needed to send both and end date and progress values.

It is needed to modify the message to send to the customer to include the possibility to include an end date. Hints:

-   Refactor the class `OrderElementWithAdvanceMeasurementsDTO` to be `OrderElementWithAdvanceMeasurementsOrEndDateDTO`.
-   Include an attribute in `OrderElementWithAdvanceMeasurementsOrEndDateDTO` for the end date.
-   Implement correctly the sending of an `OrderElementWithAdvanceMeasurementsOrEndDateDTO`. It has to have progress values, or end date or both things. It is not possible that is empty.

After the successful sending of an `OrderElementWithAdvanceMeasurementOrEndDateDTO` it is needed to update properly the `CommunicationDate` of the `EndDateCommunicationDate` sent to the customer.



####  Create a new type of communication in the list of communications received from subcontractors

It is needed to modify the list of incomming communications from the subcontractors to track the new end dates communications.

It will be needed, therefore, to create a new type of `SubcontractorCommunication`. Changes:

-   Create a new communication type in the enum of the field `CommunicationType` of the class `SubcontractorCommunication`. It will be *End date update*.
-   Probably is needed to refactor the class `SubcontractorCommunicationValue` to be able to save just date values for the end date.

So, on receiving a web service communication from a subcontractor it will be needed to create a new object of class `SubcontractorCommunication` if it comes with an end date inside.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) If the `OrderElementWithAdvanceMeasurementOrEndDateDTO` comes with an progress values and an end value, **two** objects `SubcontractorCommunication` are created.



####  Modification of the class SubcontractedTaskData

Add a new set in the class `SubcontractedTaskData` to store the end dates comming from the customers called `endDatesCommunicatedFromCustomers`.

Modify also the reception of a web service incomming message from a customer if it contains a end value communication. If this is the case, it is needed to include the saving of the end date in the `endDatesCommunicationFromCustomers` set of the suitable `SubcontractedTaskData`.

It is also needed to modify the subcontract pop-up to view the information of the end dates communicated by the customers:

-   A new table will be added in the bottom of the table called `Ended date communicated by the customer`.
-   The table will have the following columns:
    -   End date
    -   Communication date
    -   There will be a third operations column. It will contain a button called **Update task end**. This button will be enabled only for the last end date communicated end date and also it will enabled if the current end date of thet ask is different from the end date communicated.

###  User stories

-   [ItEr76S21UpdateEndDateToCustomer](/twiki/LibrePlan/ItEr76S21UpdateEndDateToCustomer)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                             | 10                                                                                                                                                             | 10                                                                                                                                                               | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                    | [Modification of project edition to allow to save end dates to send to the customers](/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer#TasK1)               |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |
| Task                                                                                                                                                             | 10                                                                                                                                                             | 10                                                                                                                                                               | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                    | [Adaptation of the XML message to send end date communications from subcontractor to customer](/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer#TasK2)      |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |
| Task                                                                                                                                                             | 10                                                                                                                                                             | 10                                                                                                                                                               | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                    | [Create a new type of communication in the list of communications received from subcontractors](/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer#TasK3)     |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |
| Task                                                                                                                                                             | 10                                                                                                                                                             | 10                                                                                                                                                               | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                    | [Create a new type of communication in the list of communications received from subcontractors](/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer#TasK4)     |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S05UpdateEndDateToCustomer?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                               | 40                                                                                                                                                                            | 0                                                                                                                                                                             | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                              |
| Total                                                                                                                                                           | 40                                                                                                                                                                            | 0                                                                                                                                                                             | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                              |

------------------------------------------------------------------------
