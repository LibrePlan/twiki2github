[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA04S09GenericCRUDController](LibrePlan_AnA04S09GenericCRUDController "Topic revision: 3 (07 Jul 2011 - 16:33:53)") (07 Jul 2011, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA04S09GenericCRUDController?t=1520344036 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA04S09GenericCRUDController "Attach an image or document to this topic")  

 [AnA04S09GenericCRUDController](LibrePlan_AnA04S09GenericCRUDController)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Generic CRUD Controller                                                  |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)                         |
| FEA                    | [AnA04S09GenericCRUDController](LibrePlan_AnA04S09GenericCRUDController) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

###  Tasks

####  Create a new class `BaseCRUDController`

New class to share common behaviour in controllers. Specially to specify window title due to [AnA08S14ShowInformationEditedEntity](LibrePlan_AnA08S14ShowInformationEditedEntity)

####  Modify CRUD controllers to use new class `BaseCRUDController`

-   Modify CRUD controller of following entities to extend `BaseCRUDController` removing all the unneeded stuff that is already in base class:
    -   ~~Worker~~ - It shares the same controller with VirtualWorker and makes more difficult to apply the refactorization
    -   ~~VirtualWorker~~
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

###  User stories

-   [ItEr75S13GenericCRUDController](LibrePlan_ItEr75S13GenericCRUDController)

###  Tasks in this story

| [Tasks](LibrePlan_AnA04S09GenericCRUDController?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA04S09GenericCRUDController?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA04S09GenericCRUDController?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA04S09GenericCRUDController?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA04S09GenericCRUDController?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA04S09GenericCRUDController?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA04S09GenericCRUDController?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA04S09GenericCRUDController?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA04S09GenericCRUDController?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA04S09GenericCRUDController?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA04S09GenericCRUDController?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 5                                                                                                        | 5                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [ManuelRego](Main_ManuelRego)                                                                                  | [Create a new class BaseCRUDController](LibrePlan_AnA04S09GenericCRUDController#TasK1)                         |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 30                                                                                                       | 30                                                                                                         | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                     | [Modify CRUD controllers to use new class BaseCRUDController](LibrePlan_AnA04S09GenericCRUDController#TasK2)   |                                                                                                                 |                                                                                                                   |                                                                                                                |

###  Total Hours in this Story

| [User](LibrePlan_AnA04S09GenericCRUDController?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA04S09GenericCRUDController?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA04S09GenericCRUDController?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA04S09GenericCRUDController?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                             | 5                                                                                                                       | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |
| [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                | 30                                                                                                                      | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |
| Total                                                                                                     | 35                                                                                                                      | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |

------------------------------------------------------------------------
