[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr61S07PerformanceOrderEdition](LibrePlan_ItEr61S07PerformanceOrderEdition "Topic revision: 4 (01 Oct 2010 - 17:22:36)") (01 Oct 2010, [JoseMariaCasanova](Main_JoseMariaCasanova))[Edit](LibrePlan_ItEr61S07PerformanceOrderEdition?t=1520343630 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr61S07PerformanceOrderEdition "Attach an image or document to this topic")  

 [ItEr61S07PerformanceOrderEdition](LibrePlan_ItEr61S07PerformanceOrderEdition)
===============================================================================

|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Performance improvements in order edition                                      |
| Iteration              | [ItEr61week38To40](LibrePlan_ItEr61week38To40)                                 |
| FEA                    | [ItEr61S07PerformanceOrderEdition](LibrePlan_ItEr61S07PerformanceOrderEdition) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

There was a considerable bottleneck related to validation when an Order is saved. For each order, there is a constraint checking that validates none each HoursGroup[?](LibrePlan_HoursGroup?topicparent=LibrePlan.ItEr61S07PerformanceOrderEdition "Create this topic") .code is unique. This is done for each OrderElement[?](LibrePlan_OrderElement?topicparent=LibrePlan.ItEr61S07PerformanceOrderEdition "Create this topic") within an Order, when it should be a big improvement to do all this checking in one pass. To do that, it's necessary to move this validation to *OrderModel*. This approach has being already done for *OrderElement.code*.

This change implies that is necessary to add this checking to *OrderElementService* too.

The entity *HoursGroup* extends now from *IntegrationEntity*.

**Delay Causes**

**Final or Pending Considerations**

###  Entregables de código

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                 | [Start Date](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                          | 10                                                                                                          | 9.25                                                                                                          | 0                                                                                                             | Low                                                                                                          | [JavierMoran](Main_JavierMoran)                                                                                  | [DiegoPino](Main_DiegoPino)                                                                                       | [Change validation of unique order code and hours group from entity to XXXModel](LibrePlan_AnA03S02PerformanceOrderEdition#TasK1) |                                                                                                                    |                                                                                                                      |                                                                                                                   |

------------------------------------------------------------------------

###  Total Hours in this Story

| [User](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr61S07PerformanceOrderEdition?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [DiegoPino](Main_DiegoPino)                                                                                  | 9.25                                                                                                                       | 0                                                                                                                          | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                           |
| Total                                                                                                        | 9.25                                                                                                                       | 0                                                                                                                          | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                           |
