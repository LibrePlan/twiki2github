[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S18DataTypesTests](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests "Topic revision: 13 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S18DataTypesTests?t=1520337924 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S18DataTypesTests "Attach an image or document to this topic")

 [ItEr75S18DataTypesTests](/twiki/LibrePlan/ItEr75S18DataTypesTests)
=======================================================================================================================



|                        |                                                                              |
|------------------------|------------------------------------------------------------------------------|
| Story summary          | Data type tests                                                              |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)               |
| FEA                    | [ItEr75S18DataTypesTests](/twiki/LibrePlan/ItEr75S18DataTypesTests) |
| Story Lead             |                                                                              |
| Next Story             |                                                                              |
| Passed acceptance test | No                                                                           |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Data type progress

-   1 - Create a new process
-   2 - Create a process with the same name (most be failure)
-   3 - Create a new process without name (most be failure)
-   4 - Check Max value and precision
    -   4.1 - Wrong values (last input precision)
    -   4.2 - Wrong values (last input Max Value)
-   5 - Edit a process
-   6 - Try to delete a previously assigned progress (most be failure)
    -   6.1 - Create a Project
    -   6.2 - Assign a progress to a project
    -   6.3 - try to delete this progress
    -   6.4 - Delete the previously created project
-   7 - Delete a process
-   8 - Try to edit a default value
-   9 - Try to delete a default value

Data type criteria:

-   1 - Create a new criterion
-   2 - Create a criterion with duplicate type (it should be a failure)
-   3 - Create a criterion with empty type
-   4 - Create a criterion with duplicate name (it should be a failure)
-   5 - Create with Hierarchy
-   6 - Create without Hierarchy (clicking on a previous name)
-   7 - Edit a criterion
-   8 - Check code
    -   8.1 - Change configuration
    -   8.2 - Try to create a new Criterion without Code (it should be a failure)
    -   8.3 - Change configuration like before
-   9 - Delete all criteria

Data type Exception Days:

-   1 - Create a new Exception Day
-   2 - Create a Exception Day with duplicate type (it should be a failure)
-   3 - Create a Exception Day with empty type (it should be a failure)
-   4 - Create a Exception Day with duplicate name (it should be a failure)
-   5 - Edit a Exception Day
-   6 - Check code label
    -   6.1 - Change configuration
    -   6.2 - Try to create a new Exception day without Code (it should be a failure)
    -   6.3 - Change configuration like before
-   7 - Delete Exception Day

Data type Label:

-   1 - Create a new Label
-   2 - Create a Label with duplicate type (it should be a failure)
-   3 - Create a Label with empty type (it should be a failure)
-   4 - Create a Label with duplicate name (it should be a failure)
-   5 - Edit a Label
-   6 - Assign a Label
    -   6.1 - Create a project
    -   6.2 - Add a Label to a project
    -   6.3 - Try to delete this assigned Label (it should be a failure)
    -   6.4 - Delete the project
-   7 - Check code
    -   7.1 - Change configuration
    -   7.2 - Try to create a new Label type without Code (it should be a failure)
    -   7.3 - Try to create a new Label name without Code (it should be a failure)
    -   7.4 - Change configuration like before
-   8 - Delete Label

Data type Unit Measure:

-   1 - Create a new Unit Measure
-   2 - Create a Unit Measure with duplicate type (most be failure)
-   3 - Create a Unit Measure with empty type (most be failure)
-   4 - Edit a Unit Measure
-   5 - Assign a Unit Measure to a material
    -   5.1 Create a material and assign the Unit
    -   5.1 Try to delete the assigned Unit (most be failure)
    -   5.2 Delete the material
-   6 - Delete Unit Measure

Data type Work Hour:

-   1 - Create a new Work Hour
-   2 - Create a Work Hour with duplicate name (it should be a failure)
-   3 - Create a Work Hour with empty name (it should be a failure)
-   4 - Edit a Work Hour
-   5 - Assign a work Hour to a project with Work Report Model
    -   5.1 - Create a new Work Report Models
    -   5.2 - Create a new proyect
    -   5.3 - Create a new Machine
    -   5.4 - Create a new Work Report and assign our Work hour and Work Report Models
    -   5.5 - Try to delete the assigned Work Hour (it should be a failure)
    -   5.6 - Try to delete the assigned Work Report Models (it should be a failure)
    -   5.7 - Try to delete the project (it should be a failure)
    -   5.8 - Delete the Work Report
    -   5.9 - Delete the project
    -   5.10 - Delete the machine
    -   5.11 - Delete the work report model
-   6 - Delete Work Hour
-   7 - Check code
    -   7.1 - Change configuration
    -   7.2 - Try to create a new Work Hour without Code (it should be a failure)
    -   7.3 - Change configuration like before
-   8 - Assign a work Hour to a Cost Category
    -   8.1 - Create a Work Hour again
    -   8.2 - Create a Cost Category and associate our Work Hour
    -   8.3 - Try to delete the Work Hour
    -   8.4 - Delete the Cost Category
    -   8.5 - Delete the Work Hour

Data type Work Report Model:

-   1 - Create a new Work Report Model
-   2 - Create a Work Report Model with duplicate type (it should be a failure)
-   3 - Create a Work Report Model with empty type (it should be a failure)
-   4 - Create a Work Report Model with duplicate name (it should be a failure)
-   5 - Edit a Work Report Model
-   6 - Check Different Fields
    -   6.1 - Check code
        -   6.1.1 - Change configuration
        -   6.1.2 - Try to create a new Work Report Model without Code (it should be a failure)
        -   6.1.3 - Change configuration like before
    -   6.2 - Check Complementary Text Fields
    -   6.3 - Check Label Type Fields
        -   6.3.1 - Create a label
        -   6.3.2 - Check Fields
        -   6.3.3 - Delete the label
-   7 - Delete Work Report Model

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                     | 16                                                                                                                                                     | 90                                                                                                                                                       | 0                                                                                                                                                        | Low                                                                                                                                                     | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                             | [PabloFernandez](/twiki/Main/PabloFernandez)                                                                                                        | [Progress Type tests](/twiki/LibrePlan/AnA13S03DataTypesTests#TasK1)                                                                                |                                                                                                                                                               |                                                                                                                                                                 |                                                                                                                                                              |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S18DataTypesTests?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PabloFernandez](/twiki/Main/PabloFernandez)                                                                                                   | 90                                                                                                                                                                    | 0                                                                                                                                                                     | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                      |
| Total                                                                                                                                                   | 90                                                                                                                                                                    | 0                                                                                                                                                                     | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                      |

------------------------------------------------------------------------
