[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA08S18WBSSettingUpBehavior](LibrePlan_AnA08S18WBSSettingUpBehavior "Topic revision: 5 (10 Aug 2012 - 16:43:40)") (10 Aug 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA08S18WBSSettingUpBehavior?t=1520344052 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S18WBSSettingUpBehavior "Attach an image or document to this topic")  

 [AnA08S18WBSSettingUpBehavior](LibrePlan_AnA08S18WBSSettingUpBehavior)
=======================================================================

|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | Improve WBS Configuration Behavior                                     |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)                             |
| FEA                    | [AnA08S18WBSSettingUpBehavior](LibrePlan_AnA08S18WBSSettingUpBehavior) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

###  Tasks

These set of tasks are thought to improve the *user experience* of the WBS tree configuration window. Now the current behavior is:

***Related to the creation of a new wbs leaf task***


    1)

    Task A (Leaf)

    2) Task A selected and a new node is added with the name Task B

    New container
       -> Task A
       -> Task B

***Related to the identation of a leaf task***


    1) 

    Task A (Leaf)
    Task B (Leaf)

    2) Select Task B and indent it to the right

    New container
       -> Task B
       -> Task A

####  Change leaf creation behavior when selected parent is a leaf with zero hours

This is a change in the WBS creation behavior when the selected parent of the next WBS leaf to add is an empy leaf task or when you indent a task and the task above it is a empty leaf task.

An empty leaf is defined as:

-   A leaf with number of hours zero.
-   A leaf without direct criteria assigned
-   A leaf without progress
-   A leaf without quality forms
-   A leaf without labels
-   A leaf without materials
-   A leaf without work report lines devoting time to it
-   A leaf without resource allocations (not assigned yet)

In this scenario when you do:

-   A creation of a new task having selected an empty leaf.
-   An indentation of a task being the task above is an empty leaf.

the empty leaf will be deleted and the created container will have the name of the deleted leaf. Specifically, the steps are the following:

***Related to the creation of a new wbs leaf task***

    1)

    Task A (Leaf)

    2) Task A selected and a new node is added with the name Task B

    Task A
       -> Task B

***Related to the identation of a leaf task***


    1) 

    Task A (Leaf)
    Task B (Leaf)

    2) Select Task B and indent it to the right

    Task A
       -> Task B

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Include also the drag & drop behavior. The task over which you drop the task dragged plays the role of the selected task in the task creation.

####  Change leaf creation behavior when selected a not empty leaf task

This task is a slight change in the behavior to create a new leaf task in the WBS having selected a leaft task *not empty* or when you ident a task and the task about it is *not empty* leaf task.

The new behavior will be to keep the structure and nodes created currently ans just to change two points:

1.  The "new container" task. The new container created is currently created with the name "new container". The new behavior to implement is to change the name of the container just created to be the name:
    1.  In the case of task creation. It will be the name of the *not empy* leaf task selected.
    2.  In the case of task identantion. It will be the name of the leaf task *not empty* above the task to be indented.
2.  The *not empty* task name will be deleted and the mouse cursor focus will be put in the textbox of the WBS tree where the name of the task is edited. The rationale behind this is that the next user action is in a high percentage in this situation to enter the new name for the original *not empty* leaf task.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Include also the drag & drop behavior. The task over which you drop the task dragged plays the role of the selected task in the task creation.

####  Move the configuration data to the new container node just created (Not included at first in 1.3)

This task consists of moving the data configured in:

-   The *non empty leaf task* selected in the case of a task creation.
-   The *non empty leaf task* above the task you are indenting

to the container just created. Let's call this task as *Moving leaf task*

The data moved to the container will be:

-   The direct required criteria
-   The direct progress measurements.
-   The direct labels.
-   The direct quality forms.

The data that will be kept in the *moving leaf task* are:

-   The hours existing in the moment of the task creation or identation.
-   The existing resource allocations.
-   The work reports assigning time are kept pointing to the *Moving leaf task*

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Include also the drag & drop behavior. The task over which you drop the task dragged plays the role of the selected task in the task creation.

###  User stories

-   [ItEr76S13WBSSettingUpBehavior](LibrePlan_ItEr76S13WBSSettingUpBehavior)

###  Tasks in this story

| [Tasks](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                | [Start Date](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task                                                                                                      | 7                                                                                                       | 7                                                                                                         | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [ManuelRego](Main_ManuelRego)                                                                                 | [Change leaf creation behavior when selected parent is a leaf with zero hours](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK1) |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 3                                                                                                       | 3                                                                                                         | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [ManuelRego](Main_ManuelRego)                                                                                 | [Change leaf creation behavior when selected a not empty leaf task](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK2)            |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 20                                                                                                      | 0                                                                                                         | 20                                                                                                        | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [ManuelRego](Main_ManuelRego)                                                                                 | [Change leaf creation behavior when selected a not empty leaf task](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK3)            |                                                                                                                |                                                                                                                  |                                                                                                               |

###  Total Hours in this Story

| [User](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA08S18WBSSettingUpBehavior?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                            | 10                                                                                                                     | 0                                                                                                                      | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                       |
| Total                                                                                                    | 10                                                                                                                     | 0                                                                                                                      | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                       |

------------------------------------------------------------------------
