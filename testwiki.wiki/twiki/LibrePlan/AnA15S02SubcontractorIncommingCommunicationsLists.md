[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA15S02SubcontractorIncommingCommunicationsLists](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists "Topic revision: 3 (03 Jan 2012 - 16:39:53)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?t=1520344063 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA15S02SubcontractorIncommingCommunicationsLists "Attach an image or document to this topic")  

 [AnA15S02SubcontractorIncommingCommunicationsLists](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists)
=================================================================================================================

|                        |                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| Story summary          | Subcontractor incommunication communications list                                                                |
| Iteration              | [AnA15SubcontractorModule](LibrePlan_AnA15SubcontractorModule)                                                   |
| FEA                    | [AnA15S02SubcontractorIncommingCommunicationsLists](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists) |
| Story Lead             |                                                                                                                  |
| Next Story             |                                                                                                                  |
| Passed acceptance test | No                                                                                                               |

###  Tasks

This set of tasks consists of doing explicit the communications sent from the subcontractor companies towards their customer companies. Therefore, these communications are the ones reviewed by the company which subcontracts to their providers. At this moment, the communication is:

-   Progress communication from provider companies towards their customer.

####  Create a list with all the communications received from subcontractors

This task consists of modifying the reception service of progress measurements to have a log of all the communications.

It is needed to implement, therefore, a new entity called `SubcontractorCommunication`. It will be an entity defined by the following features:

-   N:1 relationship with entity `SubcontractedTaskData`.
-   Attributes:
    -   *Communication date*. Date at which the reception of the communication is had.
    -   *Reviewed*. Boolean to track if the user reviewed the communication.
    -   *Values*. Hibernate component consisting of a list of pairs \[progress value, date\]
    -   *Communication type*. Enum to show the type of the received communication from the subcontractor. At this time, Progress Update

It will be created a page below the menu entry *Resources – Subcontracted tasks* with name Incoming communications from subcontractors

For each entity `SubcontractorCommunication` will be showed a list with the following columns:

    | Communication type | Subcontracted task | Project name | Project code | Company | Communication date | Values | Reviewed | Operations |

-   *Communication type*. Got from `SubcontractorCommunication`
-   *Subcontracted task*. Name of the subcontracted task. Got from `SubcontractedTaskData`.
-   *Project name*. Project name to which the subcontracted task belongs (in the customer). It is got through `SubcontractedTaskData`
-   *Project code*. The project code in the customer. Got through `SubcontractedTaskData`.
-   *Values*. Value set transmitted during communication. Got from `SubcontractorCommunication`
-   *Communication date*. Got from `SubcontractorCommunication`
-   *Reviewed*. Got from `SubcontractorCommunication`.
-   *Operations*. There will be a edit button which will do the following: It will open the project to which the `SubcontractorCommunication` row belongs and the progress pop-up of the bounded task is opened in the gantt.

This list will be sortable by all the columns except by the columns Reviewed and Operations.

####  Check the incoming communications items coming from subcontractor companies as reviewed

The subcontractor incoming communication list has a columna called `Reviewed`, that will inform if the communication exchange was already processed by the user or not.

Therefore, the behavior to implement will be that on checking/unchecking each list item, in the database the field `Reviewed` of `SubcontractorCommunication` will be udpated.

####  Include a filter in the subcontractor incoming communication list

It is needed to include a filter with the following format:

    Filter by: Combo with two values [ All, Not Reviewed]

By default this filter must have selected the value Not reviewed. The effect that is wanted in this filter with the value Not reviewed is that, after checking the communication item as reviewed, this is kept in the list.

This should not be a problem if the list is not reloaded. On entering again in the list, the item will disappear, thing which is the expected behavior.

###  User stories

-   [ItEr75S30SubcontractorIncommingCommunicationsLists](LibrePlan_ItEr75S30SubcontractorIncommingCommunicationsLists)

###  Tasks in this story

| [Tasks](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                           | [Start Date](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                           | 10                                                                                                                           | 10                                                                                                                             | 0                                                                                                                              | Low                                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                                   | [SusanaMontes](Main_SusanaMontes)                                                                                                  | [Create a list with all the communications received from subcontractors](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists#TasK1)                  |                                                                                                                                     |                                                                                                                                       |                                                                                                                                    |
| Task                                                                                                                           | 5                                                                                                                            | 5                                                                                                                              | 0                                                                                                                              | Low                                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                                   | [SusanaMontes](Main_SusanaMontes)                                                                                                  | [Check the incoming communications items coming from subcontractor companies as reviewed](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists#TasK2) |                                                                                                                                     |                                                                                                                                       |                                                                                                                                    |
| Task                                                                                                                           | 3                                                                                                                            | 3                                                                                                                              | 0                                                                                                                              | Low                                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                                   | [SusanaMontes](Main_SusanaMontes)                                                                                                  | [Include a filter in the subcontractor incoming communication list](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists#TasK3)                       |                                                                                                                                     |                                                                                                                                       | 0                                                                                                                                  |

###  Total Hours in this Story

| [User](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA15S02SubcontractorIncommingCommunicationsLists?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](Main_SusanaMontes)                                                                                             | 18                                                                                                                                          | 0                                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                            |
| Total                                                                                                                         | 18                                                                                                                                          | 0                                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                            |

------------------------------------------------------------------------
