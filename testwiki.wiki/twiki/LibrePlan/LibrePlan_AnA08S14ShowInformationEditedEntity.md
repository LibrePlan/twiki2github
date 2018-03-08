[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA08S14ShowInformationEditedEntity](LibrePlan_AnA08S14ShowInformationEditedEntity "Topic revision: 7 (20 Aug 2012 - 09:52:45)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA08S14ShowInformationEditedEntity?t=1520344050 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S14ShowInformationEditedEntity "Attach an image or document to this topic")  

 [AnA08S14ShowInformationEditedEntity](LibrePlan_AnA08S14ShowInformationEditedEntity)
=====================================================================================

|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | Show Information Edited Entity                                                       |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)                                           |
| FEA                    | [AnA08S14ShowInformationEditedEntity](LibrePlan_AnA08S14ShowInformationEditedEntity) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

###  Tasks

####  Create new interface `IHumanIdentifiable`

-   This interface will have just one method `getHumanId`. This method will be implemented in all entities that are directly manipulated in the interface to return a text identifier of the entity, this text pretends to be a human readable identifier. For example, for calendars, this method would just return the calendar name.

&nbsp;

-   We're going to show information for each entity that is edited with a common CRUD in LibrePlan. These entities are:
    -   Worker
    -   VirtualWorker
    -   Machine
    -   ExternalCompany
    -   Scenario
    -   BaseCalendar
    -   QualityForm
    -   CostCategory
    -   User
    -   Profile
    -   AdvanceType
    -   CriterionType
    -   ExceptionDayTypes
    -   LabelType
    -   UnitType
    -   TypeOfWorkHours
    -   WorkReportType

&nbsp;

-   For those classes implements interface `IHumanIdentifiable` and method `getHumanId` with following behaviour:
    -   For all entities it's going to return just the entity name.
    -   Exceptions:
        -   Worker: First name + Surname
        -   UnitType: measure

####  Show information about entity currently being edited

-   Modify `BaseCRUDController` adding a new public final method called `updateWindowTitle`:
    -   This method will use `getEntityBeingEdited()` and call `getHumanId()` over the entity.
    -   And depending on controller `state` will update corresponding window title.

&nbsp;

-   This method will be called from `goToEditForm` for the moment.

####  Update information dynamically when user modifies entity

-   Use `ON_BLUR` event in form fields used to calculate `humanId` (usually field name) and call `updateWindowTitle` method. This will update window title while user is modifying these values.

###  User stories

-   [ItEr75S14ShowInformationEditedEntity](LibrePlan_ItEr75S14ShowInformationEditedEntity)

###  Tasks in this story

| [Tasks](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                             | 20                                                                                                             | 20                                                                                                               | 0                                                                                                                | Low                                                                                                             | [ManuelRego](Main_ManuelRego)                                                                                       | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                           | [Create new interface IHumanIdentifiable](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK1)                       |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 10                                                                                                             | 10                                                                                                               | 0                                                                                                                | Low                                                                                                             | [ManuelRego](Main_ManuelRego)                                                                                       | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                           | [Show information about entity currently being edited](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK2)          |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 10                                                                                                             | 10                                                                                                               | 0                                                                                                                | Low                                                                                                             | [ManuelRego](Main_ManuelRego)                                                                                       | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                           | [Update information dynamically when user modifies entity](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK3)      |                                                                                                                       |                                                                                                                         |                                                                                                                      |

###  Total Hours in this Story

| [User](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA08S14ShowInformationEditedEntity?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                      | 40                                                                                                                            | 0                                                                                                                             | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                              |
| Total                                                                                                           | 40                                                                                                                            | 0                                                                                                                             | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                              |

------------------------------------------------------------------------
