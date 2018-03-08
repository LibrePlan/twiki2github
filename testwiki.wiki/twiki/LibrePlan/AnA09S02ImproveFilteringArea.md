[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA09S02ImproveFilteringArea](LibrePlan_AnA09S02ImproveFilteringArea "Topic revision: 3 (11 Sep 2012 - 17:07:44)") (11 Sep 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA09S02ImproveFilteringArea?t=1520344053 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA09S02ImproveFilteringArea "Attach an image or document to this topic")  

 [AnA09S02ImproveFilteringArea](LibrePlan_AnA09S02ImproveFilteringArea)
=======================================================================

|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | Improving filtering area                                               |
| Iteration              | [AnA09ResourceLoadWindow](LibrePlan_AnA09ResourceLoadWindow)           |
| FEA                    | [AnA09S02ImproveFilteringArea](LibrePlan_AnA09S02ImproveFilteringArea) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

###  Tasks

####  Implement new filtering option in resource load view (company and per project) in show by resources mode

Currently in the resource load window when you are viewing the load group by resources, you only can filter the resources to be shown selecting one or several in the `MultipleBandboxSearch`. The logic that is applied is the **OR logic**.

This tasks consists of allowing to include in the `MultipleBandboxSearch` the option to search by criteria too. The behaviour will be:

-   It will have **OR logic**.
-   It will allow to mix resources with criteria in the filtering. For example, you can filter by criterion Junior (CATEGORY) and resource John Doe, this will show you all the junior resources + Jonh Doe.
-   They will be shown the resources which satisfy the criteria used in the filtering in the data range that is selected in the time filters.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) To make coherent the filtering area it will be needed to register a listering to lauch the filtering each time I select a value in the `MultipleBandBoxSearch`. Now you have to press the *filter icon* and this is confusing, because it is not required for other components of the filter.

####  Change the order and labels of the filtering area

The new layout for the filtering area for the resource area will be (respect this order):

![filtering\_resource\_load\_sketch.png](/twiki/pub/LibrePlan/AnA09S02ImproveFilteringArea/filtering_resource_load_sketch.png)

Notes:

-   **Page** is the new label for *Name filter*
-   **Group by** is the replacement of *Show*. New labels inside.
-   The `MultipleBandSearch` has a label **Criteria or resources** in the case that the *group by* selected value is *resources*. If the *group by* selected value is *Generic allocation criteria* then the label is **Criteria**.

###  User stories

-   [ItEr76S23ImproveFilteringArea](LibrePlan_ItEr76S23ImproveFilteringArea)

###  Tasks in this story

| [Tasks](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                                            | [Start Date](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task                                                                                                      | 5                                                                                                       | 5                                                                                                         | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [ManuelRego](Main_ManuelRego)                                                                                 | [Implement new filtering option in resource load view (company and per project) in show by resources mode](LibrePlan_AnA09S02ImproveFilteringArea#TasK1) |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 3                                                                                                       | 3                                                                                                         | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [ManuelRego](Main_ManuelRego)                                                                                 | [Change the order and labels of the filtering area](LibrePlan_AnA09S02ImproveFilteringArea#TasK2)                                                        |                                                                                                                |                                                                                                                  |                                                                                                               |

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_AnA09S02ImproveFilteringArea#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_AnA09S02ImproveFilteringArea#)

| [I](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=1;table=3;up=0#sorted_table "Sort by this column")                | [Action](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=2;table=3;up=0#sorted_table "Sort by this column")                                                                     |  [Size](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=3;table=3;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_AnA09S02ImproveFilteringArea?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|:-----------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
|                          ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                         | [filtering\_resource\_load\_sketch.png](/twiki/pub/LibrePlan/AnA09S02ImproveFilteringArea/filtering_resource_load_sketch.png) | [manage](/twiki/bin/attach/LibrePlan/AnA09S02ImproveFilteringArea?filename=filtering_resource_load_sketch.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                                    13.1 K| 11 Apr 2012 - 11:25                                                                                      | [JavierMoran](Main_JavierMoran)                                                                         | Resource load filtering sketch                                                                              |
