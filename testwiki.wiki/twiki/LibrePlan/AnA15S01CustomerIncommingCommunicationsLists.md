[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA15S01CustomerIncommingCommunicationsLists](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists "Topic revision: 11 (11 Sep 2012 - 17:12:58)") (11 Sep 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?t=1520337859 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists "Attach an image or document to this topic")

 [AnA15S01CustomerIncommingCommunicationsLists](/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists)
==========================================================================================================================================================================



|                        |                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------|
| Story summary          | Incomming communications lists                                                                                         |
| Iteration              | [AnA15SubcontractorModule](/twiki/LibrePlan/AnA15SubcontractorModule)                                         |
| FEA                    | [AnA15S01CustomerIncommingCommunicationsLists](/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists) |
| Story Lead             |                                                                                                                        |
| Next Story             |                                                                                                                        |
| Passed acceptance test | No                                                                                                                     |

###  Tasks

This set of tasks are related to have a log about the the communications received related to the subcontracting module. From the side of the receiver, at this moment are implicit the following communications:

-   When a subcontractor receives the communication of a new project to be developed.
-   When the customer receives the progres communication from the subcontractor.



####  Create a list of incoming projects accepted by customers and contracted with the company

The task consists in first place in modifying the process of importing a project in order to register that, in the case the this importing were a subcontracting project, there is an incoming communication to be showed to the user.

We know that a project is subcontracted because has the field `external_code` filled. So, this criterion must be used in the process of importation.

In the import service, therefore, if it is the import of a subcontracted project, it will be needed to store this communication in a new entity. The entity will be called `CustomerCommunication`. It will have the following fields.

-   Project Deadline. Project deadline specified by the customer
-   Communication Type. It will be an enum with the communication type exchanged. At this type the enum will have only one value *New Project*
-   Communication Date. Date at which happens the communication.
-   Reviewed. It will be a boolean.

The entity `CustomerCommunication` will have a relation N:1 with the entity `Order`.

It will be created a page under the menu entry `Resources -> Subcontracting` called **Customer subcontracted projects communications**.

There will be rendered a list with the following columns. The list will be obtained querying all the `CustomerCommunication` of this entity.

    | Communication Type | Project Name | Deadline | Project Code | Customer | Communication Date |  Reviewed |  Operations |

The data that will be in each column is the following:

-   *Communication Type*. Got from `CustomerCommunication`
-   *Project Name*. Name of the project, got from associated `Order` to the `CustomerCommunication` entity
-   *Deadline*. Got from `Order`
-   *Project Code*. Code of the project hired. Got from `Order`.
-   *Customer*. Name of the customer who hires the project. Got through `CustomerCommunication`.
-   *Communication Date*. Date the communication happened. Got from `CustomerCommunication`.
-   *Reviewed*. Checkbox showing that the line was reviewed. Got from `CustomerCommunication`.
-   *Operations*. Edit button. On pressing on it, it is opened the project details perspective of the project.

The list will be sortable by all the columns except the *Reviewed* and *Operations* column.



####  Mark the items of incoming projects communications as reviewed

The list of of incoming projects communications has a column called *Reviewed* that will show if the communication interchange has already been processed or not by the user.

So, the behavior to implement is that on checking/unchecking each element of the list, this is saved in the database in a new boolean field in the `CustomerCommunication` object called `subcontractingReviewed`.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) It is important to note that this window is different than others of the app. We do not to save all the list of incomming communications at once to the database. We want to do item by item at the moment of checking/unchecking the item.

![tip](/twiki/TWiki/TWikiDocGraphics/tip.gif) Do not forget of updating the Liquibase database script.



####  Include filter in the incoming projects communications list

Include a filter with the following format:

    Filter by:  Combo with two values [All, Not Reviewed]

By default the filter must have the vaule `Not Reviewed` selected. The effect wanted of this filter with the value `Not Reviewed` is that after checking a communication item as `reviewed` it is kept in the list. This should not be problem if we do not reload the list. On entering again it will disappear of course.

###  User stories

-   [ItEr75S28CustomerIncommingCommunicationsLists](/twiki/LibrePlan/ItEr75S28CustomerIncommingCommunicationsLists)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                          | 7                                                                                                                                                                           | 10                                                                                                                                                                            | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Create a list of incoming projects accepted by customers and contracted with the company](/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists#TasK1)          |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |
| Task                                                                                                                                                                          | 7                                                                                                                                                                           | 8                                                                                                                                                                             | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Mark the items of incoming projects communications as reviewed](/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists#TasK2)                                    |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |
| Task                                                                                                                                                                          | 7                                                                                                                                                                           | 12                                                                                                                                                                            | 0                                                                                                                                                                             | Low                                                                                                                                                                          | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                  | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                                 | [Include filter in the incoming projects communications list](/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists#TasK3)                                       |                                                                                                                                                                                    |                                                                                                                                                                                      |                                                                                                                                                                                   |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA15S01CustomerIncommingCommunicationsLists?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                            | 30                                                                                                                                                                                         | 0                                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                           |
| Total                                                                                                                                                                        | 30                                                                                                                                                                                         | 0                                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                           |

------------------------------------------------------------------------
