[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr61S04NavalPlanEntities](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities "Topic revision: 7 (20 Aug 2012 - 09:52:47)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr61S04NavalPlanEntities?t=1520337874 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr61S04NavalPlanEntities "Attach an image or document to this topic")

 [ItEr61S04NavalPlanEntities](/twiki/LibrePlan/ItEr61S04NavalPlanEntities)
================================================================================================================================



|                        |                                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| Story summary          | Code generation for LibrePlan entities                                             |
| Iteration              | [ItEr61week38To40](/twiki/LibrePlan/ItEr61week38To40)                     |
| FEA                    | [ItEr61S04NavalPlanEntities](/twiki/LibrePlan/ItEr61S04NavalPlanEntities) |
| Story Lead             |                                                                                    |
| Next Story             |                                                                                    |
| Passed acceptance test | No                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

I have created the entities EntitySequence, EntitySequenceDao, and the EntitySequenceTest . Also I have created an enum that represents the entities which use code generation. Also I changed the configuration interface to add the code sequence for each entity.

The problem was fixed. It was reused a method implemented that removes the orderSequence but this one had one problem. it uses the ids of all the sequences which it was going to save or update, to order to select the sequences to remove. It is include in this list of ids the id of the new objects so this returned always a empty list.

It performed the creation of default sequences for the entities with code generation and it replaced the current generation scheme based on random UUID by sequences, except on Calendar entity which has not any generation scheme.

It integrated the entity OrderSequence in the general EntitySequence. This means that the current OrderSequence and OrderSequenceDAO were deleted and the sequences for orders will be managed through rows with entityName=ORDER of EntitySequence .

All integration services were checked. During this verification it found an bug which was reported.

**Delay Causes**

I have any problems with the transactions when I delete an active sequence and save a new active sequence in your place.

**Final or Pending Considerations**

It is necessary to create the generation scheme of calendar and the constraint to the configuration interface in order that the prefixes are not repeated. Also it still is should adding the separator ( - ) to other entities sequences like order elements, criteria or labels y the functionality which lets skip a number sequence if this already exists.

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S04NavalPlanEntities?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                        | 20                                                                                                                                                        | 24                                                                                                                                                          | 0                                                                                                                                                           | Low                                                                                                                                                        | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                               | [LibrePlan configuration for generated entity codes](/twiki/LibrePlan/AnA04S01NavalPlanEntities#TasK1)                                                 | 0                                                                                                                                                                | 0                                                                                                                                                                  | 0                                                                                                                                                               |

------------------------------------------------------------------------
