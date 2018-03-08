[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA19S02ExpenseTrackingSystem](LibrePlan_AnA19S02ExpenseTrackingSystem "Topic revision: 8 (11 Sep 2012 - 17:13:51)") (11 Sep 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA19S02ExpenseTrackingSystem?t=1520343619 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA19S02ExpenseTrackingSystem "Attach an image or document to this topic")  

 [AnA19S02ExpenseTrackingSystem](LibrePlan_AnA19S02ExpenseTrackingSystem)
=========================================================================

|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Expense tracking system                                                  |
| Iteration              | [AnA19CostModule](LibrePlan_AnA19CostModule)                             |
| FEA                    | [AnA19S02ExpenseTrackingSystem](LibrePlan_AnA19S02ExpenseTrackingSystem) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

###  Tasks

In this analysis story a set of tasks which allow to impute expenses to the projects.

####  Data model for expense tracking

This task consists of creating a new set of classes to allow to track expenses in money in the projects. The expenses will impute to `OrderElement`, i.e, they impute into the WBS.

The class diagram which is needed to create is the next one:

![expense\_tracking\_diagram.png](/twiki/pub/LibrePlan/AnA19S02ExpenseTrackingSystem/expense_tracking_class_diagram.png)

On saving a `ExpenseSheet` the following attributes are calculated from the `ExpenseSheetLine` belonging to the `ExpenseSheet`:

-   *firstExpense*. It is the earliest `ExpenseSheetLine` according to its date.
-   *lastExpense*. It is the last `ExpenseSheetLine` according to its date.
-   *total*. It is the sum of the value of all the objects `ExpenseSheetLine`

It is important to pay attention to two things:

-   `ExpenseSheet`, `ExpenseSheetLine` are entities that will have a **code** and it will be possible to import/export them through web services.
-   The relationship with `Resource` is optional.

####  Expense edition

This task is put to develop the edition and list screen pages to manage expenses.

The expense edition window to create and update expenses must have the following interface:

![expense\_edition\_sketch.png](/twiki/pub/LibrePlan/AnA19S02ExpenseTrackingSystem/expense_edition_sketch.png)

Some notes than complete the UI sketch are the next ones:

-   Combo *Tasks of project*.
    -   The component will be a *Bandbox search*.
    -   This combo will be filled with all the projects saved in the system which are **NOT** in the following states: CANCELLED, STORED.
    -   The combo will have an empty value too. This will be the default value selected.
    -   This combo has the following behavior: If the user selects a project there, then in the **Task** combo of the expenses lines there will be showed the tasks of the project that has been selected in the *tasks of project combo*.
    -   The format to show the project will be the next one: `project name (project code)`
-   *Expense date* selector.
    -   This data selector will be filled by default with the current date.
    -   The behavior of this selector is that on creating new expense lines, the data in which they will be added is the one selected in this component.
-   *Task selector* selector.
    -   The component will be fill be a *MultipleBandboxSearch*
    -   It will have two columns:
        -   First column: `task name (task code)`
        -   Second column: `project name (project code)`
    -   It will be searchable by the first column.
    -   As it was said in the previous point, this component will search:
        -   If in the *Task of project* component the selected value is the empty one, it will search in the tasks of all the projects **NOT** in the states: CANCELLED, STORED.
        -   If the *Task of project* component there one project select, it will search in the tasks of that project.
        -   A value selected in this component is mandatory to create a new expense line.
-   Value text box.
    -   Only numerical values with two decimals are allowed.
    -   It will be filled by default with the value 0.
    -   0 is allowed, but the field is mandatory, it cannot be empty.
-   Concept is a text box and is optional. It will be empty by default.
-   Resource selector.
    -   The resource will be optional.
    -   It will be a *MultipleBandboxSearch* with two columns:
        -   First column: `resource name ( resource id)`
        -   Second colum: Two possible values
            -   Resource (Worker)
            -   Resource (Machine)
        -   It will be searchable by the first column

Apart from the components, it is needed to take into account the next points:

-   In the table with the `ExpenseSheetLine` objects added to the `ExpenseSheet` the columns in the sketch are not labels, but they are the components described in the new expense line.
-   There will be a **Delete** button to allow to remove a expense line.
-   On saving the `ExpenseSheet` they must be calculated the attributres of the `ExpenseSheet` *firstExpense*, *lastExpense* and *total*.
-   It must be avoided to save the `ExpenseSheet` if any of the mandatory fields of the `ExpenseSheetLine` objects does not pass the validation.
-   Behavior to check it works.
    -   There are several `ExpenseSheetLine` objects
    -   I change the value in the *Tasks of project* selector to a different project.
    -   Then in the *Task selector* of each existent `ExpenseSheetLine` must be shown the current task selected (although it is of another project) + search in the tasks of the new project.
-   It has to be implemented the generation code mechanism. The `ExpenseSheetLine` have a code dependent of the `ExpenseSheet`. Besides it has to added the sequence mechanism configuration in the menu option *Administration/Management -&gt; LibrePlan configuration* in the tab Entity sequences.
-   It must be included a validation that avoids to store a `ExpenseSheet` without any `ExpenseSheetLine`.

####  Expense sheet list

This task is to create the list page in LibrePlan to see all the expenses created in the system and access to the edition of a a specific `TimeSheet`.

This page will be added in the top menu **Resources**. It will be placed below *Work Reports* and it will be called *Expense Tracking*. Besides we can change the name of the entry *Work Reports* to be *Time Tracking*.

The columns to include in the list are the next ones. It must be observed the order they are listed here:

-   ***First expense***. It will be the field `firstExpense` of the object `ExpenseSheet`. It must be a sortable column.
-   ***Last expense***. It will be the field `lastExpense` of the object `ExpenseSheet`. It must be a sortable column
-   ***Total***. It is the attribute `total` of the object `ExpenseSheet`. It must be a sortable column.
-   ***Code***. It is the `code` of `ExpenseSheet`. It must be a sortable column.
-   ***Description***. It is the `description` of `ExpenseSheet`. Not sortable.
-   ***Operations***. Two icons here:
    -   Edit button.
    -   Delete button. Delete button must ask for confirmation, as usual.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) The query to get the list must only load in memory the `ExpenseSheet`. Please, take care with the lazy configuration.

####  Configuring persmissions to access and save the expenses

This task consists of protecting the access and the display of the pages to store and list expenses.

A new LibrePlan permission has to be created. It will be called `Expenses tracking allowed`.

The expenses listing page, the expenses edition page have to be protected by checking that the connected user has this permission or *Administration* one.

Besides in the top menu the *Expenses Tracking* option will not be rendered if the connected user has not `Expenses tracking allowed` or `Administration` permissions.

###  User stories

-   [ItEr76S22ExpenseTrackingSystem](LibrePlan_ItEr76S22ExpenseTrackingSystem)

###  Tasks in this story

| [Tasks](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                       | 7                                                                                                        | 7                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                              | [Data model for expense tracking](LibrePlan_AnA19S02ExpenseTrackingSystem#TasK1)                               |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 24                                                                                                       | 24                                                                                                         | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                              | [Expense edition](LibrePlan_AnA19S02ExpenseTrackingSystem#TasK2)                                               |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 7                                                                                                        | 7                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                              | [Expense sheet list](LibrePlan_AnA19S02ExpenseTrackingSystem#TasK3)                                            |                                                                                                                 |                                                                                                                   |                                                                                                                |
| Task                                                                                                       | 3                                                                                                        | 3                                                                                                          | 0                                                                                                          | Low                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                              | [Configuring persmissions to access and save the expenses](LibrePlan_AnA19S02ExpenseTrackingSystem#TasK4)      |                                                                                                                 |                                                                                                                   |                                                                                                                |

------------------------------------------------------------------------

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_AnA19S02ExpenseTrackingSystem#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_AnA19S02ExpenseTrackingSystem#)

| [I](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=1;table=3;up=0#sorted_table "Sort by this column")                | [Action](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=2;table=3;up=0#sorted_table "Sort by this column")                                                                     |  [Size](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=3;table=3;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_AnA19S02ExpenseTrackingSystem?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|:------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
|                          ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                          | [expense\_edition\_sketch.png](/twiki/pub/LibrePlan/AnA19S02ExpenseTrackingSystem/expense_edition_sketch.png)                  | [manage](/twiki/bin/attach/LibrePlan/AnA19S02ExpenseTrackingSystem?filename=expense_edition_sketch.png;revInfo=1 "change, update, previous revisions, move, delete...")         |                                                                                                     59.5 K| 09 Apr 2012 - 18:08                                                                                       | [JavierMoran](Main_JavierMoran)                                                                          | expense edition sketch                                                                                       |
|                          ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                          | [expense\_tracking\_class\_diagram.png](/twiki/pub/LibrePlan/AnA19S02ExpenseTrackingSystem/expense_tracking_class_diagram.png) | [manage](/twiki/bin/attach/LibrePlan/AnA19S02ExpenseTrackingSystem?filename=expense_tracking_class_diagram.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                                     21.6 K| 10 Apr 2012 - 09:31                                                                                       | [JavierMoran](Main_JavierMoran)                                                                          | Expense tracking class diagram                                                                               |
