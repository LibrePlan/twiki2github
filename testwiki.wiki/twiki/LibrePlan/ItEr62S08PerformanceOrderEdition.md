[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr62S08PerformanceOrderEdition](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition "Topic revision: 16 (09 Nov 2010 - 09:22:40)") (09 Nov 2010, [JacoboAragunde](/twiki/Main/JacoboAragunde))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr62S08PerformanceOrderEdition?t=1520337879 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr62S08PerformanceOrderEdition "Attach an image or document to this topic")

 [ItEr62S08PerformanceOrderEdition](/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Increase performance in order edition window                                                   |
| Iteration              | [ItEr62week41To43](/twiki/LibrePlan/ItEr62week41To43)                                 |
| FEA                    | [ItEr62S08PerformanceOrderEdition](/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

I've been studying the time spent by the system in the save process. Some facts:

-   The method `OrderModel.initEditAfterSave()` reloads all the objects related with the order, and takes around 1 second. It could be replaced by calls to `dontPoseAsTrasientObjectAnymore()` for all the related objects, it's more laborious but less heavy, in theory.
-   The method `OrderCRUDController.refreshOrderWindow`, which is called after right after pressing the OK button on the 'Order saved' modal, takes between 1 and 2 seconds. Most of the time is spent on the call `reloadTree(orderElementsTree)` in the method `initializeTabs`.
-   After performing `OrderCRUDController.refreshOrderWindow`, most of the time is spent in the browser-side of the application, reloading the order elements tree. I couldn't measure exactly the time spent, but it seems to be 2-3 seconds.

All these measurements were done with my test DB, with the order called 'Pedido 1' which contains 51 lines.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 18 Oct 2010

I have replaced `OrderModel.initEditAfterSave()` with calls to `dontPoseAsTransientObjectAnymore()`. That operation used to take around 1 second, and now it takes less than 20 ms.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 19 Oct 2010

I've been studying the time spent when rendering the order element tree. Some conclusions:

-   `OrderCRUDController.setupOrderElementTreeController()` takes around 2 seconds (with 'Pedido 1' in my test DB). After that, most of the time is spent in the client side (the browser).
-   I tried ZK5 and there's no noticeable improvement in the performance of the order tree.
-   Removing cells does seem to have impact. Removing all the cells but the first column, the load times improve greatly both in the client and the server (`reloadTree()` inside `setupOrderElementTreeController()` is reduced from 1.5 s to ~0.1 s).

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 25 Oct 2010

The cells with most impact are the ones containing icons (the operations column). The cell containing a datebox doesn't seem to be very heavy, since removing them doesn't have a noticeable impact.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 27 Oct 2010

I've been reading the documentation about load-on-demand solutions. Unfortunately, the two small tals from zkoss.org are about load on demand in tree objects when changing pages or opening tree nodes, and I was looking for a solution to avoid rendering the rows that are outside the scroll area.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 27 Oct 2010

I was making some tests of performance on the order elements tree. It seems that 20 elements per page and eliminating the operations column has a good performance. Anyway, I have to check if rows are refreshed every time an order line is added (they shouldn't).

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 28 Oct 2010

Our main problem with the order elements tree is the fact that all the rows are re-rendered when the tree is manipulated (for example, when you add a new row). It can be checked looking at the response from ZK when adding a row; its XML contains all the rows of the tree.

After some experiments with trees, I realized that it's our fault: a simple tree, using `MutableTreeModel<String>` as model, doesn't do that. When a row is added, the XML only contains the new row. I suspect the problem can be in our custom renderers, since I don't use them in my example.

Files of the example with trees:

-   [TestTreeController.java](/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition/TestTreeController.java): Example with a simple tree: controller class.

-   [testTree.zul](/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition/testTree.zul): Example with a simple tree: .zul file

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 05 Nov 2010

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Entregables de código

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 7                                                                                                                                                               | 19.5                                                                                                                                                              | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                 | [Rendering of large orders with the tree widget.](/twiki/LibrePlan/AnA03S02PerformanceOrderEdition#TasK2)                                                    |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 20                                                                                                                                                              | 24                                                                                                                                                                | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                 | [Rendering of large orders with the tree widget.](/twiki/LibrePlan/AnA03S02PerformanceOrderEdition#TasK3)                                                    |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | 43.5                                                                                                                                                                           | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |
| Total                                                                                                                                                            | 43.5                                                                                                                                                                           | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |

------------------------------------------------------------------------

[![](/twiki/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](#) [![](/twiki/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](#)

| [I](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Attachment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=1;table=4;up=0#sorted_table "Sort by this column") | [Action](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=2;table=4;up=0#sorted_table "Sort by this column")      | [Size](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=3;table=4;up=0#sorted_table "Sort by this column") | [Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=4;table=4;up=0#sorted_table "Sort by this column") | [Who](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=5;table=4;up=0#sorted_table "Sort by this column") | [Comment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S08PerformanceOrderEdition?sortcol=6;table=4;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![java](/twiki/TWiki/TWikiDocGraphics/java.gif)java                                                                                                       | [TestTreeController.java](/twiki/pub/LibrePlan/ItEr62S08PerformanceOrderEdition/TestTreeController.java)                                                               | [manage](/twiki/bin/attach/LibrePlan/ItEr62S08PerformanceOrderEdition?filename=TestTreeController.java;revInfo=1 "change, update, previous revisions, move, delete...") | 1.4 K                                                                                                                                                            | 05 Nov 2010 - 10:57                                                                                                                                              | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                           | Example with a simple tree: controller class.                                                                                                                       |
| ![else](/twiki/TWiki/TWikiDocGraphics/else.gif)zul                                                                                                        | [testTree.zul](/twiki/pub/LibrePlan/ItEr62S08PerformanceOrderEdition/testTree.zul)                                                                                     | [manage](/twiki/bin/attach/LibrePlan/ItEr62S08PerformanceOrderEdition?filename=testTree.zul;revInfo=1 "change, update, previous revisions, move, delete...")            | 1.1 K                                                                                                                                                            | 05 Nov 2010 - 10:58                                                                                                                                              | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                           | Example with a simple tree: .zul file                                                                                                                               |


