[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA12S04UserDashboard](LibrePlan_AnA12S04UserDashboard "Topic revision: 21 (07 Jun 2012 - 10:19:24)") (07 Jun 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA12S04UserDashboard?t=1520344058 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA12S04UserDashboard "Attach an image or document to this topic")  

 [AnA12S04UserDashboard](LibrePlan_AnA12S04UserDashboard)
=========================================================

|                        |                                                          |
|------------------------|----------------------------------------------------------|
| Story summary          | User dashboard                                           |
| Iteration              | [AnA11UsersModule](LibrePlan_AnA11UsersModule)           |
| FEA                    | [AnA12S04UserDashboard](LibrePlan_AnA12S04UserDashboard) |
| Story Lead             |                                                          |
| Next Story             |                                                          |
| Passed acceptance test | No                                                       |

###  Tasks

This analysis story is to describe the creation of an area for those resources of type ***Bound to resources***. This area will be called ***User dashboard*** and will be the home page of the users of this type.

The new page will be placed under the menú ***My account*** and will be called ***My dashboard***.

####  Creation of the areas of the personal dashboard

The personal dashboard will be a page splitted in four areas.

![pencil\_personal\_dashboard.png](/twiki/pub/LibrePlan/AnA12S04UserDashboard/pencil_personal_dashboard.png)

The layout will have those for areas and they can be placed in a 2x2 matrix as is showed in the figure or in a 4x1 arrangement depending on the size of each area.

####  My tasks area

The my tasks area will be a section where the tasks in which the user has been assigned will be listed. In the query to get all the tasks a user takes part only the ***specific allocation*** are taken into account. This means that generic allocations in which the resource bound to the user has been assigned are discarded.

The information that will be needed to retrieve from the database for all the specific allocated tasks for the bounded user will be the following:

-   **Name**. It will be the name of the project.
-   **Code**. It will be the code of the project.
-   **Project**. The name of the project the task belongs.
-   **Start date**. The start date for the task.
-   **End date**. The end date for the task.
-   **Progress**. It will be the last progress value measured over the task set as spread. The format will be: `[progress value] (progress date)` where
    -   *progress value*. It is the last progress value of the progress set as spread.
    -   *progress date*. It the date value of the progress.
-   **Work done**. It is the sum of all the hours of all work reports imputing time to the task or to any children (if the task is not a leaf WBS element). This is precalculated and saved in `SumChargedEffort`.
-   **Operations column**. In the operations column there will be the following icons:
    -   *Icon to track time*: This icon will send the user to the monthly timesheet of the task depending on the dates:
        -   If task is in current month, it sends to the monthly timesheet of the current month.
        -   If task is in the past, it sends to the monthly timehseet of the task end.
        -   If task is in the future, it sends to the monthly timehseet of the task start.

####  My projects area (this task will be delayed after 1.3)

This task consists of creating an area where the projects in which a user has permission are listed so that he can have access to them easily and know the information more important about their status.

The first part of this task is to create a flag in the `Order` entity to configure the access level you want to give to the project with regard to the *bounded users*. It will be an enum with three possible values:

-   `NOT_ACCESS`. With this configuration option the bounded resources assigned to the project will not have permission to access the project.
-   `READ_ONLY`. With this configuration option the bounded resources assigned will be able to access to the project in read only access mode.
-   `WRITE`. With this configuration option the bounded resources assigned will be able to access the project with full permissions over it.

It will be included in the ***Authorizations*** tab three radio buttons to track this purpose. By default, the option configured in the project by default will be ***NOT\_ACCESS***.

About how this new permission system integrates with the former user and profile based one, it will be by addition. In the case that a user is affected by the ***bounded users access mode to a project permision*** and this user is also given a permission on being affected by the ***profiles authorization*** or ***user authorization*** area, the final permission for the user will be the most powerful one of all of the given. For example:

-   If a project is configured as `READ_ONLY` because of the *bounded users access mode to a project*
-   If a resource asigned to the project is a bounded user and this user has been authorized with write permission to the project
-   The effective permission for the user will be ***write permission***.

In the **My projects** area will be listed all the the projects satisfying this query: Projects in which the user has been specifically assigned in some project configured with *\_bounded users access permission* `READ_ONLY` or `WRITE` or that have been authorized directly or through any of their profiles in any project.

The list will have the following information:

-   **Project name**
-   **Project code**
-   **Start date**
-   **Deadline**
-   **Hours**
-   **Project status**

####  Model for the Monthly timesheets

It will be not done any modification in the entity model to store this new way to store `WorkReport` objects. The solution suggested is to do the next points:

-   Modify the bootstrap process to include a new `WorkReportType` object that will be bound to all `WorkReport` objects that are **Monthly timesheets**. Include a definition in the `WorkReportType` that will not be used by that can reflect the features of this new work report type. The configuration will be:
    -   `DataIsSharedByLines`. False
    -   `ResourceIsSharedByLines`. True
    -   `OrderElementIsSharedByLines` False
    -   `HoursManagement`. *NUMBER\_OF\_HOURS*.
-   Modify the pages to list/create/edit work report types in the following points:
    -   Remove this work report type from the query which obtain the list. For the user, this work report type would not exist.
    -   Protect the edit URL to avoid to edit this work report type or to delete it if the user knows the URL.
-   Modify the page ***Time Tracking***:
    -   Edition of a work report of type monthly timesheet should be done with the new grid
    -   For the creation of a new work report of type monthly timesheet we have to ask the user for 2 data (resource and month). Then:
        -   If there's already a monthly timesheet for that resource in that monht, the edition of that timesheet with the new grid will be opened
        -   Otherwise, a new timesheet will be created with the new grid
-   Modify the service to import/update work reports to prevent wrong modifications of monthly timesheets
    -   For each `WorkReportLine` to be added or modified we should check:
        -   The date is in the month of the monthly timesheet
        -   There's only 1 `WorkReportLine` per day and task in the monthly timesheet
        -   The resource is the same than in the monthly timesheet
        -   The resource is bound to any user

On the other hand it'll be needed to set the `TypeOfWorkHours` to be used in the monthly timesheets. In order to do that the proposal is:

-   Add a new configuration field to choose the `TypeOfWorkHours` for the monthly timesheets.
    -   It'll be a Bandbox with the list of active `TypeOfWorkHours`
-   In the bootstrap process the `TypeOfWorkHours` for the monthly timesheets should be set if it's not yet.
    -   If the `TypeOfWorkHours` for the monthly timesheets is already set: do nothing.
    -   If not:
        -   Try to use the `TypeOfWorkHours` with name *Deafult*
        -   If it doesn't exist, use the first `TypeOfWorkHours` active
-   Add some restrictions in the `TypeOfWorkHours` edition:
    -   Do not allow remove the `TypeOfWorkHours` configured for the monthly timesheets
    -   Do not allow disable the `TypeOfWorkHours` configured for the monthly timesheets

####  Monthly timesheets

In this part will be listed the monthly timesheets for the user. A monthly timesheet is a `WorkReport` which is created to store all the `WorkReportLine` of the users during a whole month.

Here it is going to be proposed an interface where it is not needed to create a timesheet for a month in order to be listed. The philosophy will be: List it and if does not exist, on editing it create it. If it exists, edit it with the data stored in the database.

The number of monthly timesheets to show will be the next one:

-   First month: Date at which the resource has been activated in the system.
-   Last month: The current month + 1.

The list will be sorted from last month to first month (descendant order).

The number of columns to show per monthly timesheet is the next one:

-   **Date**. It will be the date of the month of which the timesheet belongs to. The format can be `Month_Name YYYY`
-   **Available hours**. It is the number of hours which the resource bound to the user can work according to his calendar.
-   **Total work**. It is the sum of all the hours worked by the resource in the month.
-   **Number of tasks**. It is the number of different tasks in which the user has tracked time in the month.
-   **Operations**. It will have a button to access or create the timesheet of the row month.

####  Monthly timesheet creation/edition

In this project will be saved a `WorkReport` with a set of `WorkReportLine` objects. The `WorkReport` is for a month in the sense that it will have a set of `WorkReportLine` objects inside, as maximum one for each date of the month.

The interface will have the following features:

-   There will be a grid in which rows are the tasks in which the user has devoted time in the month. The columns will be the days of the month and 2 more columns. They will start in the 1st of the month the monthly timesheet is and the last column will be the last day of the month of the timesheet.
    -   There will be a extra column that will be a total cell that will sum all the hours assigned in all the row. It will not include the other column value.
-   There will be 1 extra column and 1 extra row called **Other** for the hours reported in all the work report lines with a type different from *Monthly Timesheet* imputing time in the month of the *Monthly time Timesheet*.
-   There will be two special columns in front of the days columns. These columns will be:
    -   Name: **Project**. It will contain a label with the name of the project to which the task belong.
    -   Name: **Task**. It will contain a label with the name of the task to which the row belongs.
-   This grid will be filled with a query with the following parameters:
    -   It will be queried from the database all the tasks that have been assigned with a specific resource allocation to the resource and that have at least one `DayAssigment` in that month.
    -   If there are already some `WorkReportLine` objects in the `WorkReport` it is needed to gather the task to whom they belong and include the (project, task) in a new row.
    -   The order in which the rows are rendered is the next one: They will be sorted in alphabetic order by the pair: Project name, task name
-   There will be two additional rows after all the task rows. These two special rows are the next ones:
    -   Capacity: It will be the capacity in hours which determines the calendar of the resource for the day to which the columns correspond.
    -   Total per day: It is the addition of all the hours worked in the day the column corresponds (sum of the values of the column)
-   There will be in the bottom right corner of the grid of the timesheet 3 special cells:
    -   Total month: It will be the total of the hours worked by the user in the month because of the timesheet.
    -   Total capacity: It is the sum of all the hours available to work in the month according to the capacity defined by the capacity of the worker calendar.
    -   Extra time: It is the difference "Total month - Total capacity"
-   The columns will be rendered with a background with a color scheme similar to the *Gantt chart* and the *Advanced Allocation*. This means that it depends on the calendar of the resource to which the **Monthly Timesheet** belongs. The idea is that the days in which the capacity of his calendar is 0 is shown in light pink.
    -   It is suggested that the cells are rendered empty and not with 0 as values. An empty value is a zero.
-   It will be added a component on top of the grid to add tasks in which the user has not been assigned. The component will be a searchable combo with two columns:
    -   First column: Task Name (Code)
    -   Second column: Project Name (Code)
-   The former component to find new tasks will have an **Add** button next it:
    -   On pressing on **Add** button, if the task is not already in one of the rows of the ***Monthly expenses***, it will be added. Note that the place to add it, it will be in the alphabetic order specified before (project, task).
-   In this page the codes for the `WorkReport` and the `WorkReportLine` objects will be autogenerated but they will not be shown in any part of the screen.
-   There will be two buttons in the top area to go to the timesheet of the next month and to the previous month timesheet.
-   In the heading of the page it must be identified the month date at which the timesheet belongs.
-   In the cells of the timesheet it will be used the same logic to introduce time as the one used in the rest of the application. It consists of having the ***:*** as hour minute separator.

####  My expenses area

It is needed to modify the entity model to be able to distinguish between two types of expenses sheets:

-   The expense sheets saved by an administrator through the *Expenses tracking* menu option.
-   The expense sheets saved through this new area *My expenses area*

It will be needed to add a new `boolean` field in the `ExpenseSheet` class to save if it was created from *My expenses area* or not. The field can be called `personal` and will be of type `boolean`.

It will be needed to modify the list of expenses so that it will be added a **Type** column to identify the type of expense timesheet. Two values are possible:

-   Regular
-   Personal

In the ***My expense area*** will be listed all the personal expense timesheets of the resource bound to the user who is accessing the dashboard. The query is to get all the `ExpenseSheet` objects of type ***Personal*** with a `WorkReportLine` in which the resource registered is the bound the user. It is not possible to have `ExpenseLine` with 0 `ExpenseSheetLine` and, therefore, it is possible to do the query described.

It also be adapted the interface to create/update an `ExpenseShee` for the case of *Personal*. The modification in the interface are:

-   To remove the *Resource* from the line to add a new expense line. Put the resource that will be the same for all the lines in the ***Identification*** area as a label.
-   Remove the resource from the *Expense line* table.

###  User stories

-   [ItEr76S28UserDashboard](LibrePlan_ItEr76S28UserDashboard)

###  Tasks in this story

| [Tasks](LibrePlan_AnA12S04UserDashboard?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA12S04UserDashboard?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA12S04UserDashboard?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA12S04UserDashboard?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA12S04UserDashboard?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA12S04UserDashboard?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA12S04UserDashboard?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA12S04UserDashboard?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA12S04UserDashboard?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA12S04UserDashboard?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA12S04UserDashboard?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Task                                                                                               | 4                                                                                                | 0                                                                                                  | 4                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [Creation of the areas of the personal dashboard](LibrePlan_AnA12S04UserDashboard#TasK1)               |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 7                                                                                                | 0                                                                                                  | 7                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [My tasks area](LibrePlan_AnA12S04UserDashboard#TasK2)                                                 |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 4                                                                                                | 0                                                                                                  | 4                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [My projects area](LibrePlan_AnA12S04UserDashboard#TasK3)                                              |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 7                                                                                                | 0                                                                                                  | 7                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [Model for the Monthly timesheets](LibrePlan_AnA12S04UserDashboard#TasK4)                              |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 20                                                                                               | 0                                                                                                  | 20                                                                                                 | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [Monthly timesheet creation/edition](LibrePlan_AnA12S04UserDashboard#TasK6)                            |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 10                                                                                               | 0                                                                                                  | 10                                                                                                 | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [My expenses area](LibrePlan_AnA12S04UserDashboard#TasK7)                                              |                                                                                                         |                                                                                                           |                                                                                                        |

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_AnA12S04UserDashboard#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_AnA12S04UserDashboard#)

| [I](LibrePlan_AnA12S04UserDashboard?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_AnA12S04UserDashboard?sortcol=1;table=3;up=0#sorted_table "Sort by this column")     | [Action](LibrePlan_AnA12S04UserDashboard?sortcol=2;table=3;up=0#sorted_table "Sort by this column")                                                                |  [Size](LibrePlan_AnA12S04UserDashboard?sortcol=3;table=3;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_AnA12S04UserDashboard?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_AnA12S04UserDashboard?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_AnA12S04UserDashboard?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|:----------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
|                      ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                      | [pencil\_personal\_dashboard.png](/twiki/pub/LibrePlan/AnA12S04UserDashboard/pencil_personal_dashboard.png) | [manage](/twiki/bin/attach/LibrePlan/AnA12S04UserDashboard?filename=pencil_personal_dashboard.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                             22.1 K| 08 May 2012 - 17:06                                                                               | [JavierMoran](Main_JavierMoran)                                                                  | personal dashboard layout                                                                            |
