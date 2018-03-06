[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S24ResourcesTests](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests "Topic revision: 7 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S24ResourcesTests?t=1520337927 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S24ResourcesTests "Attach an image or document to this topic")

 [ItEr75S24ResourcesTests](/twiki/LibrePlan/ItEr75S24ResourcesTests)
=======================================================================================================================



|                        |                                                                              |
|------------------------|------------------------------------------------------------------------------|
| Story summary          | Tests in module resources                                                    |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)               |
| FEA                    | [ItEr75S24ResourcesTests](/twiki/LibrePlan/ItEr75S24ResourcesTests) |
| Story Lead             |                                                                              |
| Next Story             |                                                                              |
| Passed acceptance test | No                                                                           |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Tests for Workers;

-   1 - Create a new Worker
-   2 - Create a Worker with duplicate type (it should be a failure)
-   3 - Create a Worker with empty type (it should be a failure)
-   4 - Create a Worker with duplicate name (it should be a failure)
-   5 - Edit a Worker
-   6 - Check other tabs
    -   6.1 - Check assigned criteria tab
        -   6.1.1 - Create a criterion
        -   6.1.2 - Assign this criterion to the worker
        -   6.1.3 - Try to delete the criterion
    -   6.2 - Check assigned calendar tab
        -   6.2.1 - Create a calendar
        -   6.2.2 - Assign this calendar to the worker
        -   6.2.3 - Try to delete the calendar
    -   6.3 - Check assigned cost category tab
        -   6.3.1 - Create a work hour
        -   6.3.2 - Create a cost category
        -   6.3.3 - Assign this cost category to the worker
        -   6.3.4 - Try to delete the cost category
-   7 - Try create a Worker without Code
    -   7.1 - Change configuration
    -   7.2 - create a Worker without Code (it should be a failure)
-   8 - Assign the Worker in a project
    -   8.1 - Create a project
    -   8.2 - Create a task
    -   8.3 - Assign the Worker in limiting resource form
    -   8.4 - Try to delete the assigned Worker
    -   8.5 - Delete the Project
-   9 - Delete Worker
-   10 - Delete all required elements

Tests for Machines:

-   1 - Create a new Machine
-   2 - Create a Machine with empty name (it should be a failure)
-   3 - Edit a Machine
-   4 - Assign a criteria to a machine
    -   5.1 - Create a criteria
    -   5.2 - Edit Assigned criteria tab
    -   5.3 - Try to delete a assigned criteria
-   5 - Assign a calendar
    -   5.1 - Create a calendar
    -   5.2 - Edit Calendar tab
    -   5.3 - Try to delete a assigned calendar
-   6 - Assign a cost category
    -   6.1 - Create a cost category
    -   6.2 - Edit cost category tab
    -   6.3 - Try to delete a assigned cost category
-   7 - Try create a Machine without Code
    -   7.1 - Change configuration
    -   7.2 - Create a Machine without Code (it should be a failure)
-   8 - Assign the Machine in a project
    -   8.1 - Create a project
    -   8.2 - Create a task
    -   8.3 - Assign the Machine in limiting resource form
    -   8.4 - Try to delete the assigned Machine
    -   8.5 - Delete the Project
-   9 - Delete Machine
-   10 - Delete all required elements

Tests for Virtual Workers Groups:

-   1 - Create a new Virtual Worker
-   2 - Create a Virtual Worker with duplicate type (it should be a failure)
-   3 - Create a Virtual Worker with empty type (it should be a failure)
-   4 - Create a Virtual Worker with duplicate name (it should be a failure)
-   5 - Edit a Virtual Worker
-   6 - Check other tabs
    -   6.1 - Check assigned criteria tab
        -   6.1.1 - Create a criterion
        -   6.1.2 - Assign this criterion to the Virtual worker
        -   6.1.3 - Try to delete the criterion
    -   6.2 - Check assigned calendar tab
        -   6.2.1 - Create a calendar
        -   6.2.2 - Assign this calendar to the Virtual worker
        -   6.2.3 - Try to delete the calendar
    -   6.3 - Check assigned cost category tab
        -   6.3.1 - Create a work hour
        -   6.3.2 - Create a cost category
        -   6.3.3 - Assign this cost category to the Virtual worker
        -   6.3.4 - Try to delete the cost category
-   7 - Try create a Virtual worker without Code
    -   7.1 - Change configuration
    -   7.2 - create a Virtual worker without Code (it should be a failure)
-   8 - Assign the virtual worker in a project
    -   8.1 - Create a project
    -   8.2 - Create a task
    -   8.3 - Assign the virtual worker in limiting resource form
    -   8.4 - Try to delete the assigned Virtual worker
    -   8.5 - Delete the Project
-   9 - Delete Virtual Worker
-   10 - Delete all required elements

Tests for Work Reports:

-   1 - Create a work report without any work report model (it should be a failure)
-   2 - Create a Work report from a lineal work report model
    -   2.1 - Create a lineal work report model
    -   2.2 - Create a work report
-   3 - Create a Work report from a heading work report model
    -   3.1 - Create a heading work report model
    -   3.2 - Try to create a work report from heading model without task (it should be a failure)
-   4 - Edit the work report including a line
    -   4.1 - Create a machine
    -   4.2 - Create a Work hour
    -   4.3 - Create a project
    -   4.4 - Complete the form and check the fields
-   5 - Delete all the work reports
-   6 - Delete all required elements

Tests for Companies:

-   1 - Create a new Company
-   2 - Create a Company with duplicate type (it should be a failure)
-   3 - Create a Company with empty type (it should be a failure)
-   4 - Create a Company with duplicate name (it should be a failure)
-   5 - Edit a Company
-   6 - Delete Company

Tests for Subcontracting:

-   1 - Create a Company
-   2 - Create a project
-   3 - Create a task
-   4 - Create a subcontract and assign the company like subcontractor
-   5 - Send the task
-   6 - Assign a progress to a subcontracted task
-   7 - Send the progress
-   8 - Check that the progress was send
-   9 - Delete all required elements

Some tests to check the correct performance of the search labels from resources:

-   1 - Create a criteria
-   2 - Create workers
    -   2.1 - Create three workers
    -   2.2 - Assign different criterion to each one
    -   2.3 - Filter the elements
    -   2.4 - Check if the elements are correctly filtered
-   2 - Create Virtual workers
    -   2.1 - Create three virtual workers
    -   2.2 - Assign different criterion to each one
    -   2.3 - Filter the elements
    -   2.4 - Check if the elements are correctly filtered
-   3 - Delete all the workers
-   4 - Delete all the virtual workers
-   5 - Edit the criterion to be able to use it for machines
-   6 - Create Machines
    -   6.1 - Create three machines
    -   6.2 - Assign different criterion to each one
    -   6.3 - Filter the elements
    -   6.4 - Check if the elements are correctly filtered
-   7 - Delete all the machines
-   8 - Delete criterion

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                     | 50                                                                                                                                                     | 56                                                                                                                                                       | 0                                                                                                                                                        | Low                                                                                                                                                     | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                             | [PabloFernandez](/twiki/Main/PabloFernandez)                                                                                                        | [Resources Tests](/twiki/LibrePlan/AnA13S05ResourcesTests#TasK1)                                                                                    |                                                                                                                                                               |                                                                                                                                                                 |                                                                                                                                                              |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S24ResourcesTests?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PabloFernandez](/twiki/Main/PabloFernandez)                                                                                                   | 56                                                                                                                                                                    | 0                                                                                                                                                                     | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                      |
| Total                                                                                                                                                   | 56                                                                                                                                                                    | 0                                                                                                                                                                     | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                      |

------------------------------------------------------------------------
