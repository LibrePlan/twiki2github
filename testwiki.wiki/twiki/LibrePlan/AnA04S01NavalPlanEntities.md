[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA04S01NavalPlanEntities](LibrePlan_AnA04S01NavalPlanEntities "Topic revision: 12 (20 Aug 2012 - 09:52:44)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA04S01NavalPlanEntities?t=1520344034 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA04S01NavalPlanEntities "Attach an image or document to this topic")  

 [AnA04S01NavalPlanEntities](LibrePlan_AnA04S01NavalPlanEntities)
=================================================================

|                        |                                                                  |
|------------------------|------------------------------------------------------------------|
| Story summary          | Tasks related with the entities                                  |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)                 |
| FEA                    | [AnA04S01NavalPlanEntities](LibrePlan_AnA04S01NavalPlanEntities) |
| Story Lead             |                                                                  |
| Next Story             |                                                                  |
| Passed acceptance test | No                                                               |

###  Tasks

####  Sequence generation in entities

This task consists of subtituting the sequence mechanism which is being used currently in LibrePlan (which is a random UUID) by another mechanism.

The problem of the current system is that codes generated are not human friendly: They are too long and are not related each other (they do not have an order relationship).

#####  LibrePlan configuration for generated entity codes.

The codes that will be generated will have an scheme similar to the codes used for the orders. The codes will have the following scheme:

-   ***PREFIX***: An alphanumeric part for the beginning of the code.
-   ***NUMBER***: Correlative sequence of numbers.

Each entity will have its prefix and number. These data will be stored in a new table: `EntitySequence` with the following description:

-   entityName: Name of the entity the configuration of the code generation is for.
-   lastValue: Last number used of this sequence.
-   numberOfDigits: Number of digits that the NUMBER part has.
-   active: If the current sequence is the active.

It is needed to add the following restriction: For all the rows sharing the same entityName only one of them has and can be active at the same time.

NOTES:

-   It would be suitable to integrate the entity `OrderSequence` in the general `EntitySequence`. This means that the current `OrderSequence` would be deleted and the sequences for orders will be managed through rows with entityName=ORDER of `EntitySequence`.

The interface will be the same as the one used for administration the codes for Orders. It will be a new grid for each entity.

A change over the current interface will be that because of the fact only one row per entityName (per grid) can be activated it is better to gather the active one through a radio button instead of a checkbox. Moreover, it will be good to include the fixed dash which separated *PREFIX* part from *NUMBER* in the PREFIX part - in this way it is converted in optional or changeable by another character the separator -.

The entities which use code generation and, therefore, will have a grid in the configuration window are:

-   Criterio
-   Label
-   Machine
-   Worker
-   UnitType
-   Calendar

#####  Creation of default sequences for the entities with code generation

On the startup of the application it has to be included the insertion of the default sequences for the entities with code generation. These default sequences will be:

-   PREFIX: The name of the entity: ORDER, CRITERIO, LABEL, MACHINE, WORKER
-   Number Of Digits: 5

#####  Replace the current generation scheme based on random UUID by sequences

Once the entities and the interface in order to manage the sequences for code generation for each of the entities with code generation is finished, it will be replaced in each of the windows of use cases are created entities of these types by the new mechanism in case the generation of code is requested by the interface or configured.

####  Interface refactoring for the configuration screen

This task consists of doing the configuration screen more usable.

The steps are the following:

***Create two tabs***

One tab called **Main preferences** which includes the first table.

A second tab called **Entity sequences** for all the sequences of the entities with integration.

***Change the way to edit/create the entity sequences***

It will be needed to show all the entity sequences in the same table. However there will be an area inside the table for each entity.

The effect is the one showed in this widget: <http://www.zkoss.org/zkdemo/grid/grouping>

It will be needed to add the boxes to get the values to add:

-   *Entity*: Combo to select the entity to which add the new sequence.
-   *Prefix*: Textbox to get the prefix.
-   *Number of digits*: Textbox with just numbers allowed to get the number of digits of the chain.

On the other hand, the rows of the table will be editable in the same way that they are editable currently.

Finally it will be needed to implement the fact that each section of the table will have a group of radio button which corresponds only to the sequences over the same entities.

###  User stories

-   [ItEr61S04NavalPlanEntities](LibrePlan_ItEr61S04NavalPlanEntities)
-   [ItEr62S04NavalPlanEntities](LibrePlan_ItEr62S04NavalPlanEntities)
-   [ItEr63S07NavalPlanEntities](LibrePlan_ItEr63S07NavalPlanEntities)
-   [ItEr64S06NavalPlanEntities](LibrePlan_ItEr64S06NavalPlanEntities)

###  Tasks in this story

| [Tasks](LibrePlan_AnA04S01NavalPlanEntities?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA04S01NavalPlanEntities?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA04S01NavalPlanEntities?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA04S01NavalPlanEntities?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA04S01NavalPlanEntities?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA04S01NavalPlanEntities?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA04S01NavalPlanEntities?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA04S01NavalPlanEntities?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA04S01NavalPlanEntities?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA04S01NavalPlanEntities?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA04S01NavalPlanEntities?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| Task                                                                                                   | 30                                                                                                   | 30                                                                                                     | 0                                                                                                      | Low                                                                                                   | [JavierMoran](Main_JavierMoran)                                                                           | [SusanaMontes](Main_SusanaMontes)                                                                          | [LibrePlan configuration for generated entity codes](LibrePlan_AnA04S01NavalPlanEntities#TasK1)            |                                                                                                             |                                                                                                               |                                                                                                            |
| Task                                                                                                   | 7                                                                                                    | 7                                                                                                      | 0                                                                                                      | Low                                                                                                   | [JavierMoran](Main_JavierMoran)                                                                           | [SusanaMontes](Main_SusanaMontes)                                                                          | [Interface refactoring for the configuration screen](LibrePlan_AnA04S01NavalPlanEntities#TasK2)            |                                                                                                             |                                                                                                               |                                                                                                            |

------------------------------------------------------------------------
