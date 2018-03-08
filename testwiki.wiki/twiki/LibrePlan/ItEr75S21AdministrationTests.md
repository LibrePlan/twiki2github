[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S21AdministrationTests](LibrePlan_ItEr75S21AdministrationTests "Topic revision: 8 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_ItEr75S21AdministrationTests?t=1520343683 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S21AdministrationTests "Attach an image or document to this topic")  

 [ItEr75S21AdministrationTests](LibrePlan_ItEr75S21AdministrationTests)
=======================================================================

|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | Administration tests                                                   |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                         |
| FEA                    | [ItEr75S21AdministrationTests](LibrePlan_ItEr75S21AdministrationTests) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Navalplan Configuration tests:

-   1 - Change Login checkbox
-   2 - Change Checkboxes of Generate code for all the elements
-   3 - Change perspectives of all elements
-   4 - Check login form
-   5 - Check perspective is visible
-   6 - Check that the code is not auto generated in all the elements
-   7 - Change configuration like default configuration
-   8 - Change default Calendar
    -   8.1 - Create a new calendar
    -   8.2 - Change the configuration
    -   8.3 - Check Calendar in Workers
    -   8.4 - Check Calendar in Projects
    -   8.5 - Change the calendar configuration like default configuration
    -   8.6 - Delete calendar

Calendar tests:

-   1 - Create a new Calendar
-   2 - Create a Calendar with duplicate type (it should be a failure)
-   3 - Create a Calendar with empty type (it should be a failure)
-   4 - Create a derived calendar
-   5 - Edit the Calendar
-   6 - Assign the son calendar
    -   6.1 - Create a worker with the assigned calendar
    -   6.2 - Try to delete the assigned calendar (it should be a failure)
    -   6.3 - Delete the worker
-   7 - Assign the child calendar to a project
    -   7.1 - Create a project with the assigned calendar
    -   7.2 - Try to delete the assigned calendar (it should be a failure)
    -   7.3 - Delete the project
-   8 - Try to delete the parent calendar (it should be a failure)
-   9 - Delete the son calendar
-   10 - Delete the parent Calendar

Material tests:

-   1 - Create a new Material
-   2 - Create a Material without any category selected
-   3 - Create a material with empty description (it should be a failure)
-   4 - Edit a Material
-   5 - Assign a material in a project
    -   5.1 - Create a project
    -   5.2 - Assign the material
    -   5.3 - Try to delete the assigned material
    -   5.4 \_ Delete the calendar
-   6 - Delete Material

Cost category tests:

-   1 - Create a new Cost Category
    -   1.1 - Create a work hour data type
-   2 - Create a Cost Category with duplicate type (it should be a failure)
-   3 - Create a Cost Category with empty type (it should be a failure)
-   4 - Edit a Cost Category
-   5 - Delete Cost Category
    -   5.1 - Delete the work hour data type

Quality form tests:

-   1 - Create a new Quality Form
-   2 - Create a Quality Form with duplicate name (it should be a failure)
-   3 - Create a Quality Form with empty type (it should be a failure)
-   4 - Create a Quality Form with duplicate items (it should be a failure)
-   5 - Edit the Quality Form
-   6 - Assign this Quality form to a project
    -   6.1 - Create a project
    -   6.2 - Assign it
    -   6.3 - TRY TO DELETE IT(PENDING OF A BUG)
    -   6.4 - Delete the project
-   6 - Delete the Quality Form

User tests:

-   Accounts included tests:
    -   1 - Create a new Account
    -   2 - Create other user with same password
    -   3 - Do a login with this new Account
    -   4 - Check the role
    -   5 - Create a Account with duplicate type (it should be a failure)
    -   6 - Create a Account with empty type (it should be a failure)
    -   7 - Create a new Account with two different passwords (it should be a failure)
    -   8 - Edit a Account
    -   9 - Do a login with this new Account
    -   10 - Check the role
    -   11 - Check the no user no pass
    -   12 - Check pass without user
    -   13 - Check the user no pass
    -   14 - Check fake pass and user
    -   15 - Delete both Accounts

&nbsp;

-   Profile Included tests
    -   1 - Create a new Profile
    -   2 - Create a Profile with duplicate type (It should be a failure)
    -   3 - Create a Profile with empty type (It should be a failure)
    -   4 - Create a Profile with duplicate name (It should be a failure)
    -   5 - Edit a Profile
    -   6 - Assign this profile
        -   6.1 - Create a new Account with this profile
        -   6.2 - Try to delete the profile
        -   6.3 - Delete the Account
    -   6 - Delete Profile

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

-   Try to delete a quality form, it's pending of a bug

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr75S21AdministrationTests?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S21AdministrationTests?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S21AdministrationTests?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S21AdministrationTests?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S21AdministrationTests?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S21AdministrationTests?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S21AdministrationTests?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S21AdministrationTests?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr75S21AdministrationTests?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S21AdministrationTests?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S21AdministrationTests?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Task                                                                                                      | 8                                                                                                       | 15                                                                                                        | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [PabloFernandez](Main_PabloFernandez)                                                                         | [User tests](LibrePlan_AnA13S04AdministrationTests#TasK1)                                                     |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 8                                                                                                       | 15                                                                                                        | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [PabloFernandez](Main_PabloFernandez)                                                                         | [Cost categories tests](LibrePlan_AnA13S04AdministrationTests#TasK2)                                          |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 8                                                                                                       | 10                                                                                                        | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [PabloFernandez](Main_PabloFernandez)                                                                         | [Materials tests](LibrePlan_AnA13S04AdministrationTests#TasK3)                                                |                                                                                                                |                                                                                                                  |                                                                                                               |
| Task                                                                                                      | 8                                                                                                       | 24                                                                                                        | 0                                                                                                         | Low                                                                                                      | [JavierMoran](Main_JavierMoran)                                                                              | [PabloFernandez](Main_PabloFernandez)                                                                         | [Configuration](LibrePlan_AnA13S04AdministrationTests#TasK4)                                                  |                                                                                                                |                                                                                                                  |                                                                                                               |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S21AdministrationTests?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S21AdministrationTests?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S21AdministrationTests?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S21AdministrationTests?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [PabloFernandez](Main_PabloFernandez)                                                                    | 64                                                                                                                     | 0                                                                                                                      | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                       |
| Total                                                                                                    | 64                                                                                                                     | 0                                                                                                                      | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                       |

------------------------------------------------------------------------
