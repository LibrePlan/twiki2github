[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S14ShowInformationEditedEntity](LibrePlan_ItEr75S14ShowInformationEditedEntity "Topic revision: 9 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_ItEr75S14ShowInformationEditedEntity?t=1520343680 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S14ShowInformationEditedEntity "Attach an image or document to this topic")  

 [ItEr75S14ShowInformationEditedEntity](LibrePlan_ItEr75S14ShowInformationEditedEntity)
=======================================================================================

|                        |                                                                                        |
|------------------------|----------------------------------------------------------------------------------------|
| Story summary          | Show Information Edited Entity                                                         |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                                         |
| FEA                    | [ItEr75S14ShowInformationEditedEntity](LibrePlan_ItEr75S14ShowInformationEditedEntity) |
| Story Lead             |                                                                                        |
| Next Story             |                                                                                        |
| Passed acceptance test | No                                                                                     |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Created `IHumanIdentifiable` and implemented expected behaviour for `LabelType` entity.

-- [ManuelRego](Main_ManuelRego) - 06 Jul 2011

Implemented behaviour for exception days and machines too.

-- [ManuelRego](Main_ManuelRego) - 07 Jul 2011

The folowing entities are implemented: Machine, ExternalCompany, Scenario, QualityForm, CostCategory, User, Profile, AdvanceType, ExceptionDayTypes, LabelType, UnitType, TypeOfWorkHours

Pending: WorkReportType

BaseCalendar[?](LibrePlan_BaseCalendar?topicparent=LibrePlan.ItEr75S14ShowInformationEditedEntity "Create this topic") and CriterionType[?](LibrePlan_CriterionType?topicparent=LibrePlan.ItEr75S14ShowInformationEditedEntity "Create this topic") entities can't be implemented

Worker and VirtualWorker[?](LibrePlan_VirtualWorker?topicparent=LibrePlan.ItEr75S14ShowInformationEditedEntity "Create this topic") entities can't be implemented too.

-- [CristinaAlvarino](Main_CristinaAlvarino) - 20 Jul 2011

Worker and VirtualWorker are not going to extend `BaseCRUDController` because of they share the same controller. A specific implementation has been done in order to show information about the worker (or virtual worker) being edited.

For BaseCalendar a specific implementation was done too (the controller is reused in worker edition).

Now we have just 2 entities pending to show information: WorkReportType (this will be adapted to `BaseCRUDController`) and CriterionType

-- [ManuelRego](Main_ManuelRego) - 20 Jul 2011

Finally both WorkReportType and CriterionType were adapted too `BaseCRUDController`.

This task is completed now.

-- [ManuelRego](Main_ManuelRego) - 21 Jul 2011

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

| [Tasks](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                              | 0.5                                                                                                             | 3                                                                                                                 | 0                                                                                                                 | Low                                                                                                              | [ManuelRego](Main_ManuelRego)                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                         | [Create new interface IHumanIdentifiable](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK1)                        |                                                                                                                        |                                                                                                                          |                                                                                                                       |
| Task                                                                                                              | 20                                                                                                              | 20                                                                                                                | 0                                                                                                                 | Low                                                                                                              | [ManuelRego](Main_ManuelRego)                                                                                        | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                            | [Create new interface IHumanIdentifiable](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK1)                        |                                                                                                                        |                                                                                                                          |                                                                                                                       |
| Task                                                                                                              | 0.5                                                                                                             | 4.25                                                                                                              | 0                                                                                                                 | Low                                                                                                              | [ManuelRego](Main_ManuelRego)                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                         | [Show information about entity currently being edited](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK2)           |                                                                                                                        |                                                                                                                          |                                                                                                                       |
| Task                                                                                                              | 10                                                                                                              | 10                                                                                                                | 0                                                                                                                 | Low                                                                                                              | [ManuelRego](Main_ManuelRego)                                                                                        | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                            | [Show information about entity currently being edited](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK2)           |                                                                                                                        |                                                                                                                          |                                                                                                                       |
| Task                                                                                                              | 1                                                                                                               | 2                                                                                                                 | 0                                                                                                                 | Low                                                                                                              | [ManuelRego](Main_ManuelRego)                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                         | [Update information dynamically when user modifies entity](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK3)       |                                                                                                                        |                                                                                                                          |                                                                                                                       |
| Task                                                                                                              | 10                                                                                                              | 10                                                                                                                | 0                                                                                                                 | Low                                                                                                              | [ManuelRego](Main_ManuelRego)                                                                                        | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                            | [Update information dynamically when user modifies entity](LibrePlan_AnA08S14ShowInformationEditedEntity#TasK3)       |                                                                                                                        |                                                                                                                          |                                                                                                                       |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S14ShowInformationEditedEntity?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                                    | 9.25                                                                                                                           | 0                                                                                                                              | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                               |
| [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                       | 40                                                                                                                             | 0                                                                                                                              | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                               |
| Total                                                                                                            | 49.25                                                                                                                          | 0                                                                                                                              | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                               |

------------------------------------------------------------------------
