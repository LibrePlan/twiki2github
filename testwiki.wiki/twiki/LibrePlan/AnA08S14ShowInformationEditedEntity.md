[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA08S14ShowInformationEditedEntity](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity "Topic revision: 7 (20 Aug 2012 - 09:52:45)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA08S14ShowInformationEditedEntity?t=1520337846 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S14ShowInformationEditedEntity "Attach an image or document to this topic")

 [AnA08S14ShowInformationEditedEntity](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity)
========================================================================================================================================================



|                        |                                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------|
| Story summary          | Show Information Edited Entity                                                                       |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)                                           |
| FEA                    | [AnA08S14ShowInformationEditedEntity](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity) |
| Story Lead             |                                                                                                      |
| Next Story             |                                                                                                      |
| Passed acceptance test | No                                                                                                   |

###  Tasks



####  Create new interface `IHumanIdentifiable`

-   This interface will have just one method `getHumanId`. This method will be implemented in all entities that are directly manipulated in the interface to return a text identifier of the entity, this text pretends to be a human readable identifier. For example, for calendars, this method would just return the calendar name.

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

-   For those classes implements interface `IHumanIdentifiable` and method `getHumanId` with following behaviour:
    -   For all entities it's going to return just the entity name.
    -   Exceptions:
        -   Worker: First name + Surname
        -   UnitType: measure



####  Show information about entity currently being edited

-   Modify `BaseCRUDController` adding a new public final method called `updateWindowTitle`:
    -   This method will use `getEntityBeingEdited()` and call `getHumanId()` over the entity.
    -   And depending on controller `state` will update corresponding window title.

-   This method will be called from `goToEditForm` for the moment.



####  Update information dynamically when user modifies entity

-   Use `ON_BLUR` event in form fields used to calculate `humanId` (usually field name) and call `updateWindowTitle` method. This will update window title while user is modifying these values.

###  User stories

-   [ItEr75S14ShowInformationEditedEntity](/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                 | 20                                                                                                                                                                 | 20                                                                                                                                                                   | 0                                                                                                                                                                    | Low                                                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                           | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                               | [Create new interface IHumanIdentifiable](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK1)                                                           |                                                                                                                                                                           |                                                                                                                                                                             |                                                                                                                                                                          |
| Task                                                                                                                                                                 | 10                                                                                                                                                                 | 10                                                                                                                                                                   | 0                                                                                                                                                                    | Low                                                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                           | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                               | [Show information about entity currently being edited](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK2)                                              |                                                                                                                                                                           |                                                                                                                                                                             |                                                                                                                                                                          |
| Task                                                                                                                                                                 | 10                                                                                                                                                                 | 10                                                                                                                                                                   | 0                                                                                                                                                                    | Low                                                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                           | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                               | [Update information dynamically when user modifies entity](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK3)                                          |                                                                                                                                                                           |                                                                                                                                                                             |                                                                                                                                                                          |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                          | 40                                                                                                                                                                                | 0                                                                                                                                                                                 | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                  |
| Total                                                                                                                                                               | 40                                                                                                                                                                                | 0                                                                                                                                                                                 | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                  |

------------------------------------------------------------------------
