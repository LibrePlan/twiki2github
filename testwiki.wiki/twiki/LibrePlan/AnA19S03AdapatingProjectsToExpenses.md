[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA19S03AdapatingProjectsToExpenses](LibrePlan_AnA19S03AdapatingProjectsToExpenses "Topic revision: 7 (11 Sep 2012 - 17:14:32)") (11 Sep 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA19S03AdapatingProjectsToExpenses?t=1520343620 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA19S03AdapatingProjectsToExpenses "Attach an image or document to this topic")  

 [AnA19S03AdapatingProjectsToExpenses](LibrePlan_AnA19S03AdapatingProjectsToExpenses)
=====================================================================================

|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | Adapting projects to expenses                                                        |
| Iteration              | [AnA19CostModule](LibrePlan_AnA19CostModule)                                         |
| FEA                    | [AnA19S03AdapatingProjectsToExpenses](LibrePlan_AnA19S03AdapatingProjectsToExpenses) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

###  Tasks

In these tasks are described a set of adaptations needed to adapt completely the expenses to be used in the [LibrePlan](LibrePlan_LibrePlan) projects.

####  Avoid to delete a project with expenses

It is needed to implement a validation to be checked when a user requests to delete a project. The validation to be checked will be the following: Search in the database if there are some `ExpenseSheetLine` imputing money to some of the `OrderElement` of the project. It must be avoided the deletion in this case with a **red** info message.

####  Avoid to delete an order element with expenses

If you try to delete an `OrderElement` that has objects `WorkReportLine` imputing time, it is prevented this deletion with an error message.

It must be implemented a validation similar to the `WorkReportLine` for the `ExpenseSheetLine`. It must be prevented the deletion of a `OrderElement` if there are some `ExpenseSheetLine` object imputing cost.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) It must be also checked that the `OrderElement` that wanted to be deleted do not have any descendant with some `ExpenseSheetLine` imputing cost to it.

####  Order expenses cache system

This task consists of precalculating the total money spent in expenses in the `OrderElement` of an `Order` instead of having to query the database each time the expenses cost can be displayed in a project. It is a cache mechanism similar to the one developed for the sum of hours devoted in the projects.

The class diagram for this task is the next one:

![expense\_cache\_class\_diagram.png](/twiki/pub/LibrePlan/AnA19S03AdapatingProjectsToExpenses/expense_cache_class_diagram.png)

The mapping of the `OrderElement` and `SumExpenses` class must be similar to the one existing between `OrderElement` and `SumChargedEffort`. It must be guaranteed that:

-   On saving a project, the `OrderElement`, it has to cascade to `SumExpenses` the delete operation.

&nbsp;

     
    <one-to-one name="sumChargedEffort" class="SumChargedEffort"
                cascade="delete" property-ref="orderElement" />

    <many-to-one name="orderElement" column="order_element"
                class="OrderElement" cascade="none" unique="true" />

-   The `SumExpenses` are not created on editing a project, they will be just read to calculate the cost taking into account the expenses.

***Creation of the SumExpenses objects***

The creation of the `SumExpenses` objects will be done on saving a `ExpenseSheet`. At this moment for each `ExpenseSheetLine` are created/updated the `SumExpense` objects associated to the `OrderElement` and its parents to which the `ExpenseSheetLine` imputes time.

![tip](/twiki/pub/TWiki/TWikiDocGraphics/tip.gif) You can inspire and guide yourself looking into the code that does a similar action but for the `WorkReportLine`.

***Update the SumExpenses on planning a project***

The database mapping has been designed in order to avoid storing the `SumExpenses` objects when saving the project plan. This is to avoid concurrency problems between the *project planning perspectives* and the screen to manage the expenses.

So, the strategy that we will need to implement here is the same as the one for the `WorkReport` lines. This strategy consists of:

-   Detect when it is needed to recalculate the `SumExpenses` of an `Order`. It is needed to include in the WBS interface a system to detect when it is changed the position of an `OrderElement` with some `ExpenseSheetLine` imputing money to it. If some of this movements is done in the WBS tree then the `Order` is flagged to be recalculated the `SumExpenses`.
-   The recalculation is done by an **independent thread** and not by the `Order` saving code. It must be followed the same approach that the used in the `SumChargedEffort` case.

![tip](/twiki/pub/TWiki/TWikiDocGraphics/tip.gif) Some classes that you should take a look to implement this task:

-   `org.libreplan.business.orders.daos.SumChargedEffortDAO`
-   `org.libreplan.business.orders.entities.SumChargedEffortRecalculator`

####  Update money based cost bar in Gantt chart with expenses

In the Gantt diagram of the projects in LibrePlan there is a bar which shows the spent money in the the `OrderElement` bound to a task and all its descendants `OrderElement` objects. Cost categories, type of hours and the configuration of the resources related to the cost category they belong are taken into account. This can can called the **cost because of worked hours**.

This task consists of adding the cost because of expenses to the **cost because of worked hours**. They must be added not only the expenses because of the direct expenses but because of the indirect expenses, expenses of the `OrderElement` children to the cost bar. These quantities must be extracted from the `SumExpenses` object.

####  Include the cost because of expenses in the WBS imputed hours pop-up

This task consists of adding the information about the expenses done in an `OrderElement` in the tab **Imputed hours**.

The changes to do are the next ones:

-   Change the name of the tab. It will be **Cost**.
-   Create a new section below **Imputed hours allocation** called **Expenses**. Do a table with the list of the direct expenses imputing in the `OrderElement`. The expenses must appear sorted by `Date`. It will have the following columns:

&nbsp;

          | Date | Concept | Resource  | Value |
          |         |              |                 |          |
          Sum of direct expenses
          Sum of expenses imputed in children tasks

-   Do a new format of the bottom table **Money spent** to be:
    -   Money spent. It will be the sum of the cost because of worked time and expenses.
        -   Because of hours. The total cost because of the hours worked in the `OrderElement` and its children.
        -   Because of expenses. The total cost because of the expenses in the `OrderElement` and its children.

####  Modify the report Project cost by resource

Change the name of the report to be just **Project cost**

The report will have a new area per `OrderElement` called **Expenses**. It will contain a list of expenses imputing money to the `OrderElement`. The columns of the **Expenses** area will be:

            | Date | Concept | Resource  | Value |
            |         |              |                 |          |

The table will be order by `Date` and must include a subtotal with all the expenses done in an `OrderElement`.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) If an `OrderElement` has not any expenses the area must not be rendered, not even the heading of the table.

###  User stories

-   [ItEr76S24AdapatingProjectsToExpenses](LibrePlan_ItEr76S24AdapatingProjectsToExpenses)

###  Tasks in this story

| [Tasks](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=7;table=2;up=0#sorted_table "Sort by this column")        | [Start Date](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                             | 3                                                                                                              | 3                                                                                                                | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [SusanaMontes](Main_SusanaMontes)                                                                                    | [Avoid to delete a project with expenses](LibrePlan_AnA19S03AdapatingProjectsToExpenses#TasK1)                              |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 3                                                                                                              | 3                                                                                                                | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [SusanaMontes](Main_SusanaMontes)                                                                                    | [Avoid to delete an order element with expenses](LibrePlan_AnA19S03AdapatingProjectsToExpenses#TasK2)                       |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 14                                                                                                             | 14                                                                                                               | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [SusanaMontes](Main_SusanaMontes)                                                                                    | [Order expenses cache system](LibrePlan_AnA19S03AdapatingProjectsToExpenses#TasK3)                                          |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 14                                                                                                             | 14                                                                                                               | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [SusanaMontes](Main_SusanaMontes)                                                                                    | [Update money based cost bar in Gantt chart with expenses](LibrePlan_AnA19S03AdapatingProjectsToExpenses#TasK4)             |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 7                                                                                                              | 7                                                                                                                | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [SusanaMontes](Main_SusanaMontes)                                                                                    | [Include the cost because of expenses in the WBS imputed hours pop-up](LibrePlan_AnA19S03AdapatingProjectsToExpenses#TasK5) |                                                                                                                       |                                                                                                                         |                                                                                                                      |
| Task                                                                                                             | 5                                                                                                              | 5                                                                                                                | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [SusanaMontes](Main_SusanaMontes)                                                                                    | [Modify the report Project cost by resource](LibrePlan_AnA19S03AdapatingProjectsToExpenses#TasK6)                           |                                                                                                                       |                                                                                                                         |                                                                                                                      |

------------------------------------------------------------------------

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_AnA19S03AdapatingProjectsToExpenses#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_AnA19S03AdapatingProjectsToExpenses#)

| [I](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=1;table=3;up=0#sorted_table "Sort by this column")          | [Action](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=2;table=3;up=0#sorted_table "Sort by this column")                                                                  |  [Size](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=3;table=3;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_AnA19S03AdapatingProjectsToExpenses?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|:------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
|                             ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                             | [expense\_cache\_class\_diagram.png](/twiki/pub/LibrePlan/AnA19S03AdapatingProjectsToExpenses/expense_cache_class_diagram.png) | [manage](/twiki/bin/attach/LibrePlan/AnA19S03AdapatingProjectsToExpenses?filename=expense_cache_class_diagram.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                                            7.6 K| 19 Apr 2012 - 17:13                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                | Expenses class diagram                                                                                             |
