[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA08S11ImproveBandboxFinders](LibrePlan_AnA08S11ImproveBandboxFinders "Topic revision: 4 (04 Nov 2011 - 13:16:47)") (04 Nov 2011, [SusanaMontes](Main_SusanaMontes))[Edit](LibrePlan_AnA08S11ImproveBandboxFinders?t=1520344049 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S11ImproveBandboxFinders "Attach an image or document to this topic")  

 [AnA08S11ImproveBandboxFinders](LibrePlan_AnA08S11ImproveBandboxFinders)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Improve regibility of bandbox finders                                    |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)                               |
| FEA                    | [AnA08S11ImproveBandboxFinders](LibrePlan_AnA08S11ImproveBandboxFinders) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

###  Tasks

####  Change the format of the matching results of a search

Change the format in which are shown the results in the bandbox finders which are used in several parts of the appliation.

These bandbox finders are the ones used to search criteria, labels and resources.

In these bandboxes currently there are two columns. A first column to show the type of entity and the second one to show the data of the entity. Now the change we want to introduce is to show in the first column the data of the entity and in the second one the type of entity. This order is better because peolple reads from left to right.

The format for each entity type will be the following:

***Criterion***

-   First column: *CriterionName* ( *CriterionTypeName* )
-   Second column: Criterion ( *TypeOfCriterionType* )

*CriterionName*: Name of the criterion. The string which matches the search term. *CriterionTypeName*: The name of the criterion type. *TypeOfCriterionType*: Two possible words here. *Machine* or *Worker*.

***Label***

-   First column: *LabelName* ( *LabelNameType* )
-   Second column: Label

***Worker***

-   First column: *Surname, Name*
-   Second column: Resource ( Worker )

***Machine***

-   First column: *Machine name*
-   Second column: Resource (Machine)

Places identified where it is needed to change this are:

-   Workers: Filter by criterion
-   Machines: Filter by criterion
-   Project list: Filters by label and criterion
-   Non limiting Allocation: Filter by criterion, no limiting worker.
-   Non limiting Allocation: Filter by criterion, limiting resource
-   Reports
-   Work reports.
-   Gantt filtering
-   WBS assigment of criteria

###  Tasks in this story

-   [ItEr75S09ImproveBandboxFinders](LibrePlan_ItEr75S09ImproveBandboxFinders)

| [Tasks](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 5                                                                                                        | 16                                                                                                         | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                              | [Change the format of the matching results of a search](LibrePlan_AnA08S11ImproveBandboxFinders#TasK1)         |                                                                                                                 |                                                                                                                   |                                                                                                                |

###  Total Hours in this Story

| [User](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA08S11ImproveBandboxFinders?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [SusanaMontes](Main_SusanaMontes)                                                                         | 16                                                                                                                      | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |
| Total                                                                                                     | 16                                                                                                                      | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |

------------------------------------------------------------------------
