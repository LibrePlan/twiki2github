[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA09S12ReccurrentAllocationBasic](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic "Topic revision: 3 (12 Jul 2013 - 15:40:06)") (12 Jul 2013, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA09S12ReccurrentAllocationBasic?t=1520337850 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA09S12ReccurrentAllocationBasic "Attach an image or document to this topic")

 [AnA09S12ReccurrentAllocationBasic](/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Recurrent Allocation Basic                                                                       |
| Iteration              | [AnA07PlanningWindow](/twiki/LibrePlan/AnA07PlanningWindow)                             |
| FEA                    | [AnA09S12ReccurrentAllocationBasic](/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

###  Tasks

In this analysis it is gathered a first basic model for recurrent allocations.



####  Data model to store the recurrent information

The data model that will be gathered for the scroll has the following fields:

-   Number of repetitions. It is the number of times that the recurrent allocation will be done.
-   Periodicity. It is the period that will be used to repeat the allocation done. This will be an enumerated type and will have three values:
    -   Daily
    -   Weekly
    -   Monthly



####  Save basic data for recurrent allocation

In this task the purpose is to save the allocations (recurrent) in a basic way for the data coming from the interface. The strategy will be to generate the allocations in the business model, where it seems more feasible to introduce the change reusing the code and structures currently present In LibrePlan

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 0                                                                                                                                                                | 0                                                                                                                                                                  | 0                                                                                                                                                                  | Low                                                                                                                                                               |                                                                                                                                                                       |                                                                                                                                                                        | Implementation                                                                                                                                                         |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |


