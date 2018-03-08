[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA05S07MigrationZK5](LibrePlan_AnA05S07MigrationZK5 "Topic revision: 12 (01 Nov 2012 - 20:09:52)") (01 Nov 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA05S07MigrationZK5?t=1520344037 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA05S07MigrationZK5 "Attach an image or document to this topic")  

 [AnA05S07MigrationZK5](LibrePlan_AnA05S07MigrationZK5)
=======================================================

|                        |                                                        |
|------------------------|--------------------------------------------------------|
| Story summary          | Migration to ZK5                                       |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)       |
| FEA                    | [AnA05S07MigrationZK5](LibrePlan_AnA05S07MigrationZK5) |
| Story Lead             |                                                        |
| Next Story             |                                                        |
| Passed acceptance test | No                                                     |

###  Tasks

####  Migration to ZK5

This tasks consists of finishing the migration to ZK5.

The goal of the task is doing the merge in the master branch of the repository and solve the errors and issues detected in this process.

####  Layout fixes for migration to ZK5

There are a set of interface fixes to finish the migration to ZK5. This initial list of detected things are:

***Firefox***:

-   Combo style. The combo style is wrong. Letters are huge. Test in firefox. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)

***Chrome***:

-   Header in limiting resource allocation window bad. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Tables that do not stretch to occupy the 100% width:
    -   Input task buffer in limiting resources. `limiting resources has a critical bug which has to be fixed`
    -   Top table in exceptions inside calendar does bad layout chrome. Blue bar in the right side. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Work report list. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)

***Both***:

-   Dependencies in Gantt ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Right vertical margin in gantt windows (company view and project view). `partially done`
-   Tooltip letter huge in all pages. `tooltipText property is defined by the browser, it's just an attribute, can't have styles`
-   Table in progress allocation in pop-up and tab do not strech. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Better layout for progress measures. More size to table of measurements. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Hours group table in criterion requirement. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Header letter of left table in Gantt huge. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Watermark in gantt view not right.
-   Calendar widget needs to adapted because exception days are not marked. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Exception list in calendar table is not stretched. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Work week table and list of work weeks in calendar too narrow. `not reproducible`
-   Report "Hours worked per resource" filter tables do not strecht. Right blue column. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Report "Work and progress per project" filter table does not stretch. Right blue column. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   WBS selection color blue instead of original orange. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Labels list in label type screen does not stretch. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Printing layout. ![done.gif](/twiki/pub/TWiki/TWikiDocGraphics/done.gif)
-   Combo to register project is not working fine set in company view. `undetectable`

####  Do the migration of the limiting resources window

Do the migration of the components to ZK5 of the limiting resources window.

###  User stories

-   [ItEr75S08MigrationZK5](LibrePlan_ItEr75S08MigrationZK5)

| [Tasks](LibrePlan_AnA05S07MigrationZK5?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA05S07MigrationZK5?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA05S07MigrationZK5?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA05S07MigrationZK5?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA05S07MigrationZK5?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA05S07MigrationZK5?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA05S07MigrationZK5?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA05S07MigrationZK5?sortcol=7;table=2;up=0#sorted_table "Sort by this column")               | [Start Date](LibrePlan_AnA05S07MigrationZK5?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA05S07MigrationZK5?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA05S07MigrationZK5?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Task                                                                                              | 40                                                                                              | 0                                                                                                 | 0                                                                                                 | Low                                                                                              | [JavierMoran](Main_JavierMoran)                                                                      | [OscarGonzalez](Main_OscarGonzalez)                                                                   | [ZK5 migration](LibrePlan_AnA05S07MigrationZK5#TasK1)                                                               |                                                                                                        |                                                                                                          |                                                                                                       |
| Task                                                                                              | 80                                                                                              | 0                                                                                                 | 0                                                                                                 | Low                                                                                              | [JavierMoran](Main_JavierMoran)                                                                      | [LorenzoTilve](Main_LorenzoTilve)                                                                     | [Layout fixes for migration to ZK5](LibrePlan_AnA05S07MigrationZK5#TasK2)                                           |                                                                                                        |                                                                                                          |                                                                                                       |
| Task                                                                                              | 40                                                                                              | 0                                                                                                 | 0                                                                                                 | Low                                                                                              | [JavierMoran](Main_JavierMoran)                                                                      | [JacoboAragunde](Main_JacoboAragunde)                                                                 | [Do the migration of the components to ZK5 of the limiting resources window.](LibrePlan_AnA05S07MigrationZK5#TasK2) |                                                                                                        |                                                                                                          |                                                                                                       |

###  Total Hours in this Story

| [User](LibrePlan_AnA05S07MigrationZK5?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA05S07MigrationZK5?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA05S07MigrationZK5?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA05S07MigrationZK5?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [LorenzoTilve](Main_LorenzoTilve)                                                                | 0                                                                                                              | 0                                                                                                              | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                |
| [OscarGonzalez](Main_OscarGonzalez)                                                              | 0                                                                                                              | 0                                                                                                              | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                |
| [JacoboAragunde](Main_JacoboAragunde)                                                            | 0                                                                                                              | 0                                                                                                              | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                |
| Total                                                                                            | 0                                                                                                              | 0                                                                                                              | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                |

------------------------------------------------------------------------
