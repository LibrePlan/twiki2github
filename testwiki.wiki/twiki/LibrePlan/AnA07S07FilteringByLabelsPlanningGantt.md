[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA07S07FilteringByLabelsPlanningGantt](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt "Topic revision: 4 (03 Jan 2012 - 15:14:28)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?t=1520344044 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S07FilteringByLabelsPlanningGantt "Attach an image or document to this topic")  

 [AnA07S07FilteringByLabelsPlanningGantt](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt)
===========================================================================================

|                        |                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------|
| Story summary          | Refactoring filtering by labels planning gantt                                             |
| Iteration              | [AnA07PlanningWindow](LibrePlan_AnA07PlanningWindow)                                       |
| FEA                    | [AnA07S07FilteringByLabelsPlanningGantt](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt) |
| Story Lead             |                                                                                            |
| Next Story             |                                                                                            |
| Passed acceptance test | No                                                                                         |

###  Tasks

The set of tasks of this analysis story is related to the correction of several flaws in the filtering of labels in

####  Display labels in the container they are assigned

Labels are hierarchical and if they are assigned in a container node of the WBS they are inherited by the descendant nodes.

At present if containers are unfolded labels are displayed only in the tasks. This is unconsistent, becuase they are asigned to the containers too and the user has not any clue about the point where labels are assigned. Therefore, this task consists in displaying the labels in the Gantt in the node in which are assigned and its descendants.

####  Including options panel in Gantt task filter

Now the filter with labels is inconsistent with the hierarchical behavior of the labels. Now if you filter by a label and this label has been directed applied to a container just the container in which the label has been applied is displayed. However, all this inner tasks have the label assigend by inheritance and this behavior is strange.

However, the current behavior although it is strange it is interesting for some users.

So, in order to make a consistent situation and allow the current behavior an options panel it is going to be included for the filter in Gantt window. The description of this filter will be the following:

-   The interface will be a small widget next to the filter button which will raise a pop-up with the current options which defines the filter behavior.
-   The pop-pup will have at this moment one checkbox defined in the following way:
    -   Title: Labels without inheritance \[X\]
    -   If the check box is set, this will imply that the filter only showed the nodes until the level that a label has been applied. Its descendants will not be displayed.
    -   If the check box is not set, the filter will show all the tree sin the root containers until the tasks which inherites the labels.

In this task the full filter will be revamped:


    || Task [........] With [.........................] More [icon] Filter [icon]

    || => It is a separator.

In the pop-up there will be three things:

-   From Date \[component\]
-   To Date \[component\]
-   Labels without inheritance \[X\]

####  Optioin not show parents in gantt task filter

This task consists of adding a new check box to the options panel for the gantt filter with the following definition:

-   Title: Show parents for label filtering \[X\]
-   If the check box is set thet the behavior is the current one and when a container or node is selected by the filter the root path of elements is displayed.
-   If the check box is not set, then only the node satisfying the filter is showed (the node or the node and its decendants depending on if the previous check box *labels without inheritance* is set).

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) At this moment the behavior for criteria filtering is not analysed and proposed to change or correct its flaws.

###  Users story

-   [ItEr75S15FilteringByLabelsPlanningGantt](LibrePlan_ItEr75S15FilteringByLabelsPlanningGantt)

###  Tasks in this story

| [Tasks](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                | 16                                                                                                                | 16                                                                                                                  | 0                                                                                                                   | Low                                                                                                                | [JavierMoran](Main_JavierMoran)                                                                                        | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                         | [Display labels in the container they are assigned](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt#TasK1)             |                                                                                                                          |                                                                                                                            |                                                                                                                         |
| Task                                                                                                                | 16                                                                                                                | 16                                                                                                                  | 0                                                                                                                   | Low                                                                                                                | [JavierMoran](Main_JavierMoran)                                                                                        | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                         | [Including options panel in Gantt task filter](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt#TasK2)                  |                                                                                                                          |                                                                                                                            |                                                                                                                         |
| Task                                                                                                                | 16                                                                                                                | 0                                                                                                                   | 16                                                                                                                  | Low                                                                                                                | [JavierMoran](Main_JavierMoran)                                                                                        | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                         | [Optioin not show parents in gantt task filter](LibrePlan_AnA07S07FilteringByLabelsPlanningGantt#TasK3)                 |                                                                                                                          |                                                                                                                            |                                                                                                                         |
