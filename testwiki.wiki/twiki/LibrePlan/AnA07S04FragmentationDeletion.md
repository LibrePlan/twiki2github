[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA07S04FragmentationDeletion](LibrePlan_AnA07S04FragmentationDeletion "Topic revision: 5 (07 Mar 2011 - 09:56:22)") (07 Mar 2011, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA07S04FragmentationDeletion?t=1520344042 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S04FragmentationDeletion "Attach an image or document to this topic")  

 [AnA07S04FragmentationDeletion](LibrePlan_AnA07S04FragmentationDeletion)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Fragmentation deletion in generic allocation                             |
| Iteration              | [AnA07PlanningWindow](LibrePlan_AnA07PlanningWindow)                     |
| FEA                    | [AnA07S04FragmentationDeletion](LibrePlan_AnA07S04FragmentationDeletion) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

###  Tasks

####  Sharing block algorithm for resource allocation.

***Normal hours***

-   Starting point: Sharing block for a day D.
-   Resources satisfying the set of criteria in day D which define the generic allocation are found = Set A.
-   Resource in set A are sorted in ascending order from less load to more assigned load.
-   Resources are retrieved from set A and receive an allocation in day D with the formula: Workable hours of the resource calendar - Hours already allocated in day D to the resource.
-   The process continues until the sharing block to be allocated in day D is done.

***Extra hours***

This part of the algorithm tells what to do when the set A has not enough free normal hours to satisfy the sharing block in day D.

-   Resources in set A are sorted in ascending according to the number of extra hours allocated in that day to each resource.
-   About the sharing algorithm of these hours I have two proposals:

The sharing block algorithm currently implemented but now only will used in the over allocating region.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Of course, it has to be taken into account that now an over allocation control strategy is used in calendars with the philosophy **one calendar per task approach**. This means that a resource can have a limit of hours to allocate in day D (with the special cases of zero and infinitum).

***Sharing block for the end day of a task***

The desired behaviour is to use the same sharing algorithm than in intermediate days. The end hour of the task, will be the hour of the resource with more hours allocated that day.

For instance: If we have 10 hours to allocate the last day of a task and two free resources, resource one would receive 8h, resource two 2h and the end hour of the task will the 8th hour.

####  Implement heuristic "trying to keep the same resources all the time"

When you do an allocation and you are the person in charge of planning a project, in general, it is normal that you want to keep the same resources allocated during the whole duration of the task if possible.

So, the above is relevant for the resource allocation generic algorithm described. I think that it can be enriched with the heuristic **trying to keep the same resources all the time**.

-   First block sharing algorithm is the same described but resources used are stored in a list.
-   Successive days set A is sorted according the pair (used before, free load) and retrieved in this order. Resource used before are used before than other resources even when later ones have more free load.

###  User stories

-   [ItEr70S09FragmentationDeletion](LibrePlan_ItEr70S09FragmentationDeletion)
-   [ItEr71S07FragmentationDeletionItEr70S09](LibrePlan_ItEr71S07FragmentationDeletionItEr70S09)

###  Tasks

| [Tasks](LibrePlan_AnA07S04FragmentationDeletion?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA07S04FragmentationDeletion?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA07S04FragmentationDeletion?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA07S04FragmentationDeletion?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA07S04FragmentationDeletion?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA07S04FragmentationDeletion?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA07S04FragmentationDeletion?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA07S04FragmentationDeletion?sortcol=7;table=2;up=0#sorted_table "Sort by this column")        | [Start Date](LibrePlan_AnA07S04FragmentationDeletion?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA07S04FragmentationDeletion?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA07S04FragmentationDeletion?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 20                                                                                                       | 13                                                                                                         | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [OscarGonzalez](Main_OscarGonzalez)                                                                            | [Sharing block algorithm for resource allocation](LibrePlan_AnA07S04FragmentationDeletion#TasK1)                      |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 20                                                                                                       | 8                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [OscarGonzalez](Main_OscarGonzalez)                                                                            | [Implement heuristic "trying to keep the same resources all the time"](LibrePlan_AnA07S04FragmentationDeletion#TasK2) |                                                                                                                 |                                                                                                                   |                                                                                                                |

###  Total Hours in this Story

| [User](LibrePlan_AnA07S04FragmentationDeletion?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA07S04FragmentationDeletion?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA07S04FragmentationDeletion?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA07S04FragmentationDeletion?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [OscarGonzalez](Main_OscarGonzalez)                                                                       | 21                                                                                                                      | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |
| Total                                                                                                     | 21                                                                                                                      | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |

------------------------------------------------------------------------
