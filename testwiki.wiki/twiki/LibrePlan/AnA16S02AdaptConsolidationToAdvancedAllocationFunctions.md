[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA16S02AdaptConsolidationToAdvancedAllocationFunctions](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions "Topic revision: 2 (19 Dec 2011 - 19:09:02)") (19 Dec 2011, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?t=1520337862 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions "Attach an image or document to this topic")

 [AnA16S02AdaptConsolidationToAdvancedAllocationFunctions](/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions)
================================================================================================================================================================================================



|                        |                                                                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Story summary          | Analysis to adapt consolidation to advanced allocation functions                                                                             |
| Iteration              | [AnA16ConsolidationModule](/twiki/LibrePlan/AnA16ConsolidationModule)                                                               |
| FEA                    | [AnA16S02AdaptConsolidationToAdvancedAllocationFunctions](/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions) |
| Story Lead             |                                                                                                                                              |
| Next Story             |                                                                                                                                              |
| Passed acceptance test | No                                                                                                                                           |

###  Tasks



####  Adapt consolidation process to manual allocation function

When there is a consolidation of a progress at date ***D*** a flat allocation is done from the date D to the end of the task.

Therefore if the task has been manually allocated the work is lost from D to the end of the task. However, it is manual allocatioin flag is kept on doing the consolidation.

As middle step the idea is to modifify the consolidation on manually allocated task in the next way: On consolidating a task with a manual allocation, it is needed to implement to remove the flag *manual* and configure the task as flat.



####  Adapt consolidation process to stretches function

Now, the behavior of consolidating resource allocation which have a *stretched function applied* is not working properly.

The process to implement will be the following:

-   If the consolidation date is greater than the start date of the task, it will be created a new stretch at date D of the consolidation and with a percentage of of completion equal to the progress that is being consolidated.
-   All the stretches from the date D till the end of the task are removed except the 100% one.
-   The flat consolidation is applied in the last stretch.

The process of desconsolidation will be to

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) Check that all works properly when more than one progress are consolidated at once.

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                                     | 0                                                                                                                                                                                      | 0                                                                                                                                                                                        | 0                                                                                                                                                                                        | Low                                                                                                                                                                                     |                                                                                                                                                                                             |                                                                                                                                                                                              | Implementation                                                                                                                                                                               |                                                                                                                                                                                               |                                                                                                                                                                                                 |                                                                                                                                                                                              |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA16S02AdaptConsolidationToAdvancedAllocationFunctions?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                         | 0                                                                                                                                                                                                     | 0                                                                                                                                                                                                     | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                                                       |
| Total                                                                                                                                                                                   | 0                                                                                                                                                                                                     | 0                                                                                                                                                                                                     | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                                                       |

------------------------------------------------------------------------