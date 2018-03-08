[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA05S10WortReportsEffortDuration](LibrePlan_AnA05S10WortReportsEffortDuration "Topic revision: 4 (03 Jan 2012 - 15:18:21)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA05S10WortReportsEffortDuration?t=1520344038 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA05S10WortReportsEffortDuration "Attach an image or document to this topic")  

 [AnA05S10WortReportsEffortDuration](LibrePlan_AnA05S10WortReportsEffortDuration)
=================================================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Introduce Effort Duration in Work Reports                                        |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)                                 |
| FEA                    | [AnA05S10WortReportsEffortDuration](LibrePlan_AnA05S10WortReportsEffortDuration) |
| Story Lead             |                                                                                  |
| Next Story             |                                                                                  |
| Passed acceptance test | No                                                                               |

###  Tasks

####  Modify the field numHours in WorkReportLine to be EffortDuration

Currently the field `numHours` in `WorkReportLine` is of type **Integer**. Because of that at present it is not possible to track time which is not a multiple of an hour.

In order to overcome this, this task consists of using the type `EffortDuration` to save the amount of work done in a `WorkReportLine`. There is an Hibernate type for this `org.navalplanner.business.workingday.hibernate.EffortDurationType`.

Besides changing the above in the database, it is needed to do the following things:

-   At interface level use the component to introduce hours and minutes sepatared by colon (:). It is used in the resource allocation and in advanced allocation windows.
-   Examine the places where this field is used for calculation and change then accordinly. For instance, it is needed to change:
    -   Some reports
    -   The tab in the WBS where the addittion of worked hours is displayed.
    -   The earned value management.

####  Create Liquibase configuration to migrate data

We are changing the type of a column from `Integer` to `EffortDuration`. Because of this, in order to avoid data loss we should elaborate a proper Liquibase configuration to conver integer values to `EfforDuration` types.

###  User stories

-   [ItEr75S22WortReportsEffortDuration](LibrePlan_ItEr75S22WortReportsEffortDuration)

###  Tasks in this story

| [Tasks](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=7;table=2;up=0#sorted_table "Sort by this column")    | [Start Date](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                           | 20                                                                                                           | 36                                                                                                             | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                    | [Modify the field numHours in WorkReportLine to be EffortDuration](LibrePlan_AnA05S10WortReportsEffortDuration#TasK1) |                                                                                                                     |                                                                                                                       |                                                                                                                    |
| Task                                                                                                           | 20                                                                                                           | 0.5                                                                                                            | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                    | [Create Liquibase configuration to migrate data](LibrePlan_AnA05S10WortReportsEffortDuration#TasK2)                   |                                                                                                                     |                                                                                                                       |                                                                                                                    |

###  Total Hours in this Story

| [User](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA05S10WortReportsEffortDuration?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz)                                                                               | 36.5                                                                                                                        | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |
| Total                                                                                                         | 36.5                                                                                                                        | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |

------------------------------------------------------------------------
