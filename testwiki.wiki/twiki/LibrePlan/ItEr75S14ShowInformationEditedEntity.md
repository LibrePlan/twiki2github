[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S14ShowInformationEditedEntity](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity "Topic revision: 9 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S14ShowInformationEditedEntity?t=1520337923 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S14ShowInformationEditedEntity "Attach an image or document to this topic")

 [ItEr75S14ShowInformationEditedEntity](/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity)
==========================================================================================================================================================



|                        |                                                                                                        |
|------------------------|--------------------------------------------------------------------------------------------------------|
| Story summary          | Show Information Edited Entity                                                                         |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)                                         |
| FEA                    | [ItEr75S14ShowInformationEditedEntity](/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity) |
| Story Lead             |                                                                                                        |
| Next Story             |                                                                                                        |
| Passed acceptance test | No                                                                                                     |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Created `IHumanIdentifiable` and implemented expected behaviour for `LabelType` entity.

-- [ManuelRego](/twiki/Main/ManuelRego) - 06 Jul 2011

Implemented behaviour for exception days and machines too.

-- [ManuelRego](/twiki/Main/ManuelRego) - 07 Jul 2011

The folowing entities are implemented: Machine, ExternalCompany, Scenario, QualityForm, CostCategory, User, Profile, AdvanceType, ExceptionDayTypes, LabelType, UnitType, TypeOfWorkHours

Pending: WorkReportType

BaseCalendar[?](/twiki/bin/edit/LibrePlan/BaseCalendar?topicparent=LibrePlan.ItEr75S14ShowInformationEditedEntity "Create this topic") and CriterionType[?](/twiki/bin/edit/LibrePlan/CriterionType?topicparent=LibrePlan.ItEr75S14ShowInformationEditedEntity "Create this topic") entities can't be implemented

Worker and VirtualWorker[?](/twiki/bin/edit/LibrePlan/VirtualWorker?topicparent=LibrePlan.ItEr75S14ShowInformationEditedEntity "Create this topic") entities can't be implemented too.

-- [CristinaAlvarino](/twiki/Main/CristinaAlvarino) - 20 Jul 2011

Worker and VirtualWorker are not going to extend `BaseCRUDController` because of they share the same controller. A specific implementation has been done in order to show information about the worker (or virtual worker) being edited.

For BaseCalendar a specific implementation was done too (the controller is reused in worker edition).

Now we have just 2 entities pending to show information: WorkReportType (this will be adapted to `BaseCRUDController`) and CriterionType

-- [ManuelRego](/twiki/Main/ManuelRego) - 20 Jul 2011

Finally both WorkReportType and CriterionType were adapted too `BaseCRUDController`.

This task is completed now.

-- [ManuelRego](/twiki/Main/ManuelRego) - 21 Jul 2011

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                  | 0.5                                                                                                                                                                 | 3                                                                                                                                                                     | 0                                                                                                                                                                     | Low                                                                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                             | [Create new interface IHumanIdentifiable](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK1)                                                            |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |
| Task                                                                                                                                                                  | 20                                                                                                                                                                  | 20                                                                                                                                                                    | 0                                                                                                                                                                     | Low                                                                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                            | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                | [Create new interface IHumanIdentifiable](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK1)                                                            |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |
| Task                                                                                                                                                                  | 0.5                                                                                                                                                                 | 4.25                                                                                                                                                                  | 0                                                                                                                                                                     | Low                                                                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                             | [Show information about entity currently being edited](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK2)                                               |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |
| Task                                                                                                                                                                  | 10                                                                                                                                                                  | 10                                                                                                                                                                    | 0                                                                                                                                                                     | Low                                                                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                            | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                | [Show information about entity currently being edited](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK2)                                               |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |
| Task                                                                                                                                                                  | 1                                                                                                                                                                   | 2                                                                                                                                                                     | 0                                                                                                                                                                     | Low                                                                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                             | [Update information dynamically when user modifies entity](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK3)                                           |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |
| Task                                                                                                                                                                  | 10                                                                                                                                                                  | 10                                                                                                                                                                    | 0                                                                                                                                                                     | Low                                                                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                            | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                | [Update information dynamically when user modifies entity](/twiki/LibrePlan/AnA08S14ShowInformationEditedEntity#TasK3)                                           |                                                                                                                                                                            |                                                                                                                                                                              |                                                                                                                                                                           |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S14ShowInformationEditedEntity?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                        | 9.25                                                                                                                                                                               | 0                                                                                                                                                                                  | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                   |
| [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                           | 40                                                                                                                                                                                 | 0                                                                                                                                                                                  | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                   |
| Total                                                                                                                                                                | 49.25                                                                                                                                                                              | 0                                                                                                                                                                                  | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                   |

------------------------------------------------------------------------