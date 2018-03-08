[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr76S13WBSSettingUpBehavior](LibrePlan_ItEr76S13WBSSettingUpBehavior "Topic revision: 8 (20 Aug 2012 - 09:50:16)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr76S13WBSSettingUpBehavior?t=1520343693 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S13WBSSettingUpBehavior "Attach an image or document to this topic")  

 [ItEr76S13WBSSettingUpBehavior](LibrePlan_ItEr76S13WBSSettingUpBehavior)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Improve WBS Configuration Behavior                                       |
| Iteration              | [ItEr76Week01To33](LibrePlan_ItEr76Week01To33)                           |
| FEA                    | [ItEr76S13WBSSettingUpBehavior](LibrePlan_ItEr76S13WBSSettingUpBehavior) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

####  [Change leaf creation behavior when selected parent is a leaf with zero hours](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK1)

To implement this new behavior 2 new methods were added to `org.libreplan.business.trees.ITreeNode`:

-   `isEmptyLeaf()`: To check if a leaf is or not empty (no hours, no criteria, no progresses...). This method is used in `org.libreplan.web.tree.EntitiesTree.turnIntoContainerIfNeeded(ITreeNode? )`, if true the leaf is not added to the new container created.
-   `isLeaf()`: To avoid using `org.libreplan.web.tree.TreeController.isLine(T)` (that has been removed). `isLine()` checked that the element has not children, but after adding the previous condition when you're creating the container and the leaf is empty, as you're not adding the leaf, the container has not children for a while, however it's a leaf (or line).

Moreover the method `org.libreplan.web.tree.EntitiesTree.addElementAt(T, String, int)` has been modified and now it returns the new element. This is used in `org.libreplan.web.tree.TreeController.addElement(Component)` to update the hours input in the new element and parents. As now if the leaf is empty the old element is removed you cannot use it to update the hours inputs.

Finally, `org.libreplan.business.orders.entities.OrderLine.toContainer()` was modified to keep the task name if the leaf is empty. Otherwise, *new container* is used for the moment.

####  [Change leaf creation behavior when selected a not empty leaf task](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK2)

The first part of this task (put an empty name) is already pushed. It just needed a change in the method `org.libreplan.business.orders.entities.OrderLine.toContainer()`. Then it was needed to fix some tests in `OrderElementTreeModelTest`.

To fix the issue with the focus, a new map has been added `org.libreplan.web.tree.TreeController.Renderer.nameTextboxByElement` in order to know the `Textbox` corresponding to the different tasks.

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=7;table=2;up=0#sorted_table "Sort by this column")               | [Start Date](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 7                                                                                                        | 6.75                                                                                                       | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [ManuelRego](Main_ManuelRego)                                                                                  | [Change leaf creation behavior when selected parent is a leaf with zero hours](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK1) |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 3                                                                                                        | 2                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [ManuelRego](Main_ManuelRego)                                                                                  | [Change leaf creation behavior when selected a not empty leaf task](LibrePlan_AnA08S18WBSSettingUpBehavior#TasK2)            |                                                                                                                 |                                                                                                                   |                                                                                                                |

###  Total Hours in this Story

| [User](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr76S13WBSSettingUpBehavior?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                             | 8.75                                                                                                                    | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |
| Total                                                                                                     | 8.75                                                                                                                    | 0                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                        |

------------------------------------------------------------------------
