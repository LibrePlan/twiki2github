[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S13GenericCRUDController](LibrePlan_ItEr75S13GenericCRUDController "Topic revision: 7 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_ItEr75S13GenericCRUDController?t=1520343679 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S13GenericCRUDController "Attach an image or document to this topic")  

 [ItEr75S13GenericCRUDController](LibrePlan_ItEr75S13GenericCRUDController)
===========================================================================

|                        |                                                                            |
|------------------------|----------------------------------------------------------------------------|
| Story summary          | Generic CRUD Controller                                                    |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                             |
| FEA                    | [ItEr75S13GenericCRUDController](LibrePlan_ItEr75S13GenericCRUDController) |
| Story Lead             |                                                                            |
| Next Story             |                                                                            |
| Passed acceptance test | No                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Implemented `BaseCRUDController` and moved a lot of stuff to there.

Adapted `LabelTypeCRUDController` in order to extend `BaseCRUDController` as first example.

-- [ManuelRego](Main_ManuelRego) - 06 Jul 2011

Used `BaseCRUDController` for exception days and machines. Detected that it's not possible to use it directly for workers, because of it's sharing controller with virtual workers.

-- [ManuelRego](Main_ManuelRego) - 07 Jul 2011

Finally not all the classes were adapted to `BaseCRUDController` because of different issues (you can read more info at [ItEr75S14ShowInformationEditedEntity](LibrePlan_ItEr75S14ShowInformationEditedEntity)).

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

| [Tasks](LibrePlan_ItEr75S13GenericCRUDController?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S13GenericCRUDController?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S13GenericCRUDController?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S13GenericCRUDController?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S13GenericCRUDController?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S13GenericCRUDController?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S13GenericCRUDController?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S13GenericCRUDController?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr75S13GenericCRUDController?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S13GenericCRUDController?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S13GenericCRUDController?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                        | 5                                                                                                         | 8                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [ManuelRego](Main_ManuelRego)                                                                                   | [Create a new class BaseCRUDController](LibrePlan_AnA04S09GenericCRUDController#TasK1)                          |                                                                                                                  |                                                                                                                    | 0                                                                                                               |
| Task                                                                                                        | 30                                                                                                        | 30                                                                                                          | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                      | [Modify CRUD controllers to use new class BaseCRUDController](LibrePlan_AnA04S09GenericCRUDController#TasK2)    |                                                                                                                  |                                                                                                                    |                                                                                                                 |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S13GenericCRUDController?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S13GenericCRUDController?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S13GenericCRUDController?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S13GenericCRUDController?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                              | 8                                                                                                                        | 0                                                                                                                        | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                         |
| [CristinaAlvarino](Main_CristinaAlvarino), [IgnacioDiaz](Main_IgnacioDiaz)                                 | 30                                                                                                                       | 0                                                                                                                        | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                         |
| Total                                                                                                      | 38                                                                                                                       | 0                                                                                                                        | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                         |

------------------------------------------------------------------------
