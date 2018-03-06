[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA05S07MigrationZK5](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5 "Topic revision: 12 (01 Nov 2012 - 20:09:52)") (01 Nov 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA05S07MigrationZK5?t=1520337834 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA05S07MigrationZK5 "Attach an image or document to this topic")

 [AnA05S07MigrationZK5](/twiki/LibrePlan/AnA05S07MigrationZK5)
==============================================================================================================



|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | Migration to ZK5                                                       |
| Iteration              | [AnA04Architecture](/twiki/LibrePlan/AnA04Architecture)       |
| FEA                    | [AnA05S07MigrationZK5](/twiki/LibrePlan/AnA05S07MigrationZK5) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

###  Tasks



####  Migration to ZK5

This tasks consists of finishing the migration to ZK5.

The goal of the task is doing the merge in the master branch of the repository and solve the errors and issues detected in this process.



####  Layout fixes for migration to ZK5

There are a set of interface fixes to finish the migration to ZK5. This initial list of detected things are:

***Firefox***:

-   Combo style. The combo style is wrong. Letters are huge. Test in firefox. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)

***Chrome***:

-   Header in limiting resource allocation window bad. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Tables that do not stretch to occupy the 100% width:
    -   Input task buffer in limiting resources. `limiting resources has a critical bug which has to be fixed`
    -   Top table in exceptions inside calendar does bad layout chrome. Blue bar in the right side. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Work report list. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)

***Both***:

-   Dependencies in Gantt ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Right vertical margin in gantt windows (company view and project view). `partially done`
-   Tooltip letter huge in all pages. `tooltipText property is defined by the browser, it's just an attribute, can't have styles`
-   Table in progress allocation in pop-up and tab do not strech. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Better layout for progress measures. More size to table of measurements. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Hours group table in criterion requirement. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Header letter of left table in Gantt huge. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Watermark in gantt view not right.
-   Calendar widget needs to adapted because exception days are not marked. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Exception list in calendar table is not stretched. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Work week table and list of work weeks in calendar too narrow. `not reproducible`
-   Report "Hours worked per resource" filter tables do not strecht. Right blue column. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Report "Work and progress per project" filter table does not stretch. Right blue column. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   WBS selection color blue instead of original orange. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Labels list in label type screen does not stretch. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Printing layout. ![done.gif](/twiki/TWiki/TWikiDocGraphics/done.gif)
-   Combo to register project is not working fine set in company view. `undetectable`



####  Do the migration of the limiting resources window

Do the migration of the components to ZK5 of the limiting resources window.

###  User stories

-   [ItEr75S08MigrationZK5](/twiki/LibrePlan/ItEr75S08MigrationZK5)



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                  | 40                                                                                                                                                  | 0                                                                                                                                                     | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                       | [ZK5 migration](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK1)                                                                                     |                                                                                                                                                            |                                                                                                                                                              |                                                                                                                                                           |
| Task                                                                                                                                                  | 80                                                                                                                                                  | 0                                                                                                                                                     | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                         | [Layout fixes for migration to ZK5](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK2)                                                                 |                                                                                                                                                            |                                                                                                                                                              |                                                                                                                                                           |
| Task                                                                                                                                                  | 40                                                                                                                                                  | 0                                                                                                                                                     | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                     | [Do the migration of the components to ZK5 of the limiting resources window.](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK2)                       |                                                                                                                                                            |                                                                                                                                                              |                                                                                                                                                           |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S07MigrationZK5?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                    | 0                                                                                                                                                                  | 0                                                                                                                                                                  | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                    |
| [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                  | 0                                                                                                                                                                  | 0                                                                                                                                                                  | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                    |
| [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                | 0                                                                                                                                                                  | 0                                                                                                                                                                  | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                    |
| Total                                                                                                                                                | 0                                                                                                                                                                  | 0                                                                                                                                                                  | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                    |

------------------------------------------------------------------------
