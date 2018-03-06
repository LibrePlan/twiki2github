[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA05S10WortReportsEffortDuration](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration "Topic revision: 4 (03 Jan 2012 - 15:18:21)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA05S10WortReportsEffortDuration?t=1520337835 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA05S10WortReportsEffortDuration "Attach an image or document to this topic")

 [AnA05S10WortReportsEffortDuration](/twiki/LibrePlan/AnA05S10WortReportsEffortDuration)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Introduce Effort Duration in Work Reports                                                        |
| Iteration              | [AnA04Architecture](/twiki/LibrePlan/AnA04Architecture)                                 |
| FEA                    | [AnA05S10WortReportsEffortDuration](/twiki/LibrePlan/AnA05S10WortReportsEffortDuration) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

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

-   [ItEr75S22WortReportsEffortDuration](/twiki/LibrePlan/ItEr75S22WortReportsEffortDuration)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 20                                                                                                                                                               | 36                                                                                                                                                                 | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                       | [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                                        | [Modify the field numHours in WorkReportLine to be EffortDuration](/twiki/LibrePlan/AnA05S10WortReportsEffortDuration#TasK1)                                  |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |
| Task                                                                                                                                                               | 20                                                                                                                                                               | 0.5                                                                                                                                                                | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                       | [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                                        | [Create Liquibase configuration to migrate data](/twiki/LibrePlan/AnA05S10WortReportsEffortDuration#TasK2)                                                    |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S10WortReportsEffortDuration?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                                   | 36.5                                                                                                                                                                            | 0                                                                                                                                                                               | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                |
| Total                                                                                                                                                             | 36.5                                                                                                                                                                            | 0                                                                                                                                                                               | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                |

------------------------------------------------------------------------