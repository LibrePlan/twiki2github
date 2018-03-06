[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr74S07WBSTreeRefactoring](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring "Topic revision: 9 (19 Jun 2011 - 14:58:29)") (19 Jun 2011, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr74S07WBSTreeRefactoring?t=1520337916 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr74S07WBSTreeRefactoring "Attach an image or document to this topic")

 [ItEr74S07WBSTreeRefactoring](/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring)
===================================================================================================================================



|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | WBS tree refactoring                                                                 |
| Iteration              | [ItEr74week14To24](/twiki/LibrePlan/ItEr74week14To24)                       |
| FEA                    | [ItEr74S07WBSTreeRefactoring](/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Created a new test class called `OrderElementTreeModelTest` with tests for basic operations:

-   Add element
-   Remove element
-   Add advances on element
-   Add criteria on element

`OrderElementTreeModel` extends `EntitiesTree` (in the webapp module), and defines a method `added` which is called after some element is added to the tree. The implementation for this method calls to `updateCriterionRequirementsInHierarchy` method which finally calls to `OrderElement::updateCriterionRequirements` (in business).

Which means that `OrderElementTreeModel` is taking care of some business logic and it shouldn't. So, method `EntitiesTree::added` is removed. We need to still keep calling to `OrderElement::updateCriterionRequirements` at some point, but in the business module (that should be in charge of this logic).

In the business part there're an interface called `ITreeParentNode` implemented by `TreeNodeOnList` (with all the basic behaviour for operations) and defining some abstract methods `onChildAdded` and `onChildRevomed`. `TreeNodeOnList` is extended by `TreeNodeOnListWithSchedulingState` (in charge of keep scheduling state with proper values) which defines a method `onChildRevomedAditionalActions`. This method is overridden at `ChildrenManipulator` class inside `OrderLineGroup`.

Then I added a new `onChildAddedAditionalActions` in `TreeNodeOnListWithSchedulingState` to take care of update criteria.

All the business logic related with entities used in `OrderElement` (like criteria, advances, ...) when some element is added or removed should be controlled by these 2 methods in `ChildrenManipulator`:

-   `onChildAddedAditionalActions`
-   `onChildRemovedAditionalActions`

-- [ManuelRego](/twiki/Main/ManuelRego) - 19 Apr 2011

We will need to do some refactorization to use the same methods in all the cases. Moreover, templates part is broken as it has a particular implementation that should be reused when possible.

For the moment I've been adding more and more tests to `OrderElementTreeModelTest` and patching current implementation to make it works.

-- [ManuelRego](/twiki/Main/ManuelRego) - 04 May 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                         | 20                                                                                                                                                         | 42.75                                                                                                                                                        | 0                                                                                                                                                            | Low                                                                                                                                                         | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Do the tests and implement things in order to satisfy operations](/twiki/LibrePlan/AnA08S12WBSTreeRefactoring#TasK1)                                   |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | 42.75                                                                                                                                                                     | 0                                                                                                                                                                         | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                          |
| Total                                                                                                                                                       | 42.75                                                                                                                                                                     | 0                                                                                                                                                                         | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                          |

------------------------------------------------------------------------
