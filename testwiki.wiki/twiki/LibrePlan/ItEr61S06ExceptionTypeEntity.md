[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr61S06ExceptionTypeEntity](LibrePlan_ItEr61S06ExceptionTypeEntity "Topic revision: 3 (13 Oct 2010 - 15:00:27)") (13 Oct 2010, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr61S06ExceptionTypeEntity?t=1520343630 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr61S06ExceptionTypeEntity "Attach an image or document to this topic")  

 [ItEr61S06ExceptionTypeEntity](LibrePlan_ItEr61S06ExceptionTypeEntity)
=======================================================================

|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | ExceptionType entity management                                        |
| Iteration              | [ItEr61week38To40](LibrePlan_ItEr61week38To40)                         |
| FEA                    | [ItEr61S06ExceptionTypeEntity](LibrePlan_ItEr61S06ExceptionTypeEntity) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

The entity **ExceptionType** already exists in the system, known as **CalendarExceptionType**. I added managing capabilities to this entity (now is possible to create, remove, update and list *CalendarExceptionType*). The use case also demanded to add a new field, *duration*, of type **EffortDuration** to this type. When an user creates a new *ExceptionDay*, the field *workable hours* will be set to the value of the field `duration` associated with its *CalendarExceptionType*.

I also pushed the patch of adding a new report for listing *hours worked per worker in a month* in this story.

-- [ManuelRego](Main_ManuelRego) - 13 Oct 2010

Pushed patches related with web services of **CalendarExceptionType** entity.

**Delay Causes**

**Final or Pending Considerations**

###  Tasks in this story

| [Tasks](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr61S06ExceptionTypeEntity?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task                                                                                                      | 10                                                                                                      | 9.5                                                                                                       | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [DiegoPino](Main_DiegoPino)                                                                                   | [Create the entity ExceptionType for Calendars](LibrePlan_AnA05S01ExceptionTypeEntity#TasK1)                  | 26/09/10                                                                                                       | 02/10/10                                                                                                         | 28/09/10                                                                                                      |
| Task                                                                                                      | 0                                                                                                       | 0.5                                                                                                       | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [ManuelRego](Main_ManuelRego)                                                                                 | [Create the entity ExceptionType for Calendars](LibrePlan_AnA05S01ExceptionTypeEntity#TasK1)                  | 26/09/10                                                                                                       | 02/10/10                                                                                                         | 28/09/10                                                                                                      |

------------------------------------------------------------------------
