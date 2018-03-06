[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S26SchedulingTests](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests "Topic revision: 4 (03 Jan 2012 - 13:16:58)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S26SchedulingTests?t=1520337928 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S26SchedulingTests "Attach an image or document to this topic")

 [ItEr75S26SchedulingTests](/twiki/LibrePlan/ItEr75S26SchedulingTests)
==========================================================================================================================



|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Tests for Scheduling                                                           |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)                 |
| FEA                    | [ItEr75S26SchedulingTests](/twiki/LibrePlan/ItEr75S26SchedulingTests) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Tests included about templates:

-   1 - Create a Project
-   2 - Create a Project template
-   3 - Assign the template
-   4 - Check Assigned project template
-   5 - Create a task tree
-   6 - Create a Template about the current Task tree
-   7 - Assign the template
-   8 - Check Assigned task template
-   9 - Try to delete assigned templates
-   10 - Delete all required elements

Tests included to check the correct performance of the criteria in project planning:

-   1 - Create a Criterion
-   2 - Create a Calendar
-   3 - Create a Worker
-   4 - Assign elements to a worker
    -   4.1 - Assign Criterion
    -   4.2 - Assign Calendar (Incorrect dates)
-   5 - Create a project
-   6 - Create a Task
-   7 - Try to assign the worker with the incorrect calendar
-   8 - Assign elements to a worker
    -   8.1 - Assign Criterion (Incorrect dates)
    -   8.2 - Assign Calendar
-   9 - Allocate criterion into the first task
-   10 - Check Project planning filter
-   11 - Delete all required elements

Tests included to check the correct performance of the labels in project planning:

-   1 - Create a Label
-   2 - Create a Project
-   3 - Create two tasks
-   4 - Assign the label to the first of the tasks
-   5 - Check that the label is showed when label button is pressed
-   6 - Filter the showed task by the the assigned label
-   7 - Check that just the task with the assigned label lis showed
-   8 - Delete required elements

-- [PabloFernandez](/twiki/Main/PabloFernandez) - 13 Sep 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                      | 40                                                                                                                                                      | 40                                                                                                                                                        | 0                                                                                                                                                         | Low                                                                                                                                                      |                                                                                                                                                              |                                                                                                                                                               | Implementation                                                                                                                                                |                                                                                                                                                                |                                                                                                                                                                  |                                                                                                                                                               |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S26SchedulingTests?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                          | 40                                                                                                                                                                     | 0                                                                                                                                                                      | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                       |
| Total                                                                                                                                                    | 40                                                                                                                                                                     | 0                                                                                                                                                                      | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                       |

------------------------------------------------------------------------
