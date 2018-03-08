[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA03S02PerformanceOrderEdition](LibrePlan_AnA03S02PerformanceOrderEdition "Topic revision: 7 (08 Nov 2010 - 17:39:09)") (08 Nov 2010, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA03S02PerformanceOrderEdition?t=1520344120 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA03S02PerformanceOrderEdition "Attach an image or document to this topic")  

 [AnA03S02PerformanceOrderEdition](LibrePlan_AnA03S02PerformanceOrderEdition)
=============================================================================

|                        |                                                                              |
|------------------------|------------------------------------------------------------------------------|
| Story summary          | Performance tuning in order edition window                                   |
| Iteration              | [AnA03PerformanceTuning](LibrePlan_AnA03PerformanceTuning)                   |
| FEA                    | [AnA03S02PerformanceOrderEdition](LibrePlan_AnA03S02PerformanceOrderEdition) |
| Story Lead             |                                                                              |
| Next Story             |                                                                              |
| Passed acceptance test | No                                                                           |

###  Tasks

####  Change validation of unique order code and hours group from entity to XXXModel

The validation of being unique the order code has to be changed from being validated in the entities to be validated in the XXXModel becuase the validation is runned for each order element. It is needed just to execute it once for all the order elements of an order.

The same has to be done for the codes of the hours group. It has to be moved the validation from entities to XXXModel.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) It is important to realize that it will be needed to change the import system in order to do these validations too.

####  Solve the reload on saving order

When an order is saved it is reloaded completely. This causes an unnecessary delay because in this case this could be avoided.

This can be avoided. The only field that changes is the code. So we have three options to assess:

-   Really not load the generated code and in this case, not update the order completely.
-   Assess if update quickly only this column without reloading is an option.
-   Generate the code in the moment of adding the line to the order.

Of course, we have to see if technically the objects in the model have the ids and the codes generated although we do not reload the tree.

####  Rendering of large orders with the tree widget.

Now it is being used a paginated tree for editing an order with a page size of 50 elements per size. With this size, the change of page is really slow. So, we need to improve the times to browse and use the tree.

Steps to do are (not needed in this order):

-   Measure the time is being consumed in the interface for the rendering of these trees with this number of elements.
-   Do tests to identify inside a row the elements which takes longer to render. Assess if we can change some of the widgets of a row and delete and simplify these rows.
-   Assess solutions as load-on-demand. Can it be applied?
    -   <http://www.zkoss.org/smalltalks/loadondemand/>
    -   <http://www.zkoss.org/smalltalks/zkTreeModel/>
    -   <http://www.pichelhofer.at/ZKTests/BindJDBC11c.zul>
    -   <http://www.zkoss.org/forum/listComment/13844>
    -   <http://www.zkoss.org/forum/listComment/5567>
-   Checkout the ZK5 branch and make a merge to have it updated with the last changes in the repo. Assess if with the ZK5 version of the framework we have a better performance.
-   As a last solution we could reduce the size of the page - to 20 elements -. It would be nice to be able to show some feedback while changing the page it is being visited.

###  User stories

-   [ItEr61S07PerformanceOrderEdition](LibrePlan_ItEr61S07PerformanceOrderEdition)
-   [ItEr62S08PerformanceOrderEdition](LibrePlan_ItEr62S08PerformanceOrderEdition)
-   [ItEr63S05PerformanceOrderEdition](LibrePlan_ItEr63S05PerformanceOrderEdition)

###  Tasks in this story

| [Tasks](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                  | [Start Date](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA03S02PerformanceOrderEdition?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                         | 10                                                                                                         | 10                                                                                                           | 0                                                                                                            | Low                                                                                                         | [JavierMoran](Main_JavierMoran)                                                                                 | [DiegoPino](Main_DiegoPino)                                                                                      | [Change validation of unique order code and hours group from entity to XXXModel](LibrePlan_AnA03S02PerformanceOrderEdition#TasK1) |                                                                                                                   |                                                                                                                     |                                                                                                                  |
| Task                                                                                                         | 7                                                                                                          | 0                                                                                                            | 7                                                                                                            | Low                                                                                                         | [JavierMoran](Main_JavierMoran)                                                                                 | [JacoboAragunde](Main_JacoboAragunde)                                                                            | [Rendering of large orders with the tree widget.](LibrePlan_AnA03S02PerformanceOrderEdition#TasK2)                                |                                                                                                                   |                                                                                                                     |                                                                                                                  |
| Task                                                                                                         | 20                                                                                                         | 0                                                                                                            | 20                                                                                                           | Low                                                                                                         | [JavierMoran](Main_JavierMoran)                                                                                 | [JacoboAragunde](Main_JacoboAragunde)                                                                            | [Rendering of large orders with the tree widget.](LibrePlan_AnA03S02PerformanceOrderEdition#TasK3)                                |                                                                                                                   |                                                                                                                     |                                                                                                                  |

------------------------------------------------------------------------
