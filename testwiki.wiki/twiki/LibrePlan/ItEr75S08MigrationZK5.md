[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S08MigrationZK5](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5 "Topic revision: 15 (05 Jan 2012 - 08:30:54)") (05 Jan 2012, [JacoboAragunde](/twiki/Main/JacoboAragunde))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S08MigrationZK5?t=1520337921 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S08MigrationZK5 "Attach an image or document to this topic")

 [ItEr75S08MigrationZK5](/twiki/LibrePlan/ItEr75S08MigrationZK5)
=================================================================================================================



|                        |                                                                          |
|------------------------|--------------------------------------------------------------------------|
| Story summary          | Migration to ZK5                                                         |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)           |
| FEA                    | [ItEr75S08MigrationZK5](/twiki/LibrePlan/ItEr75S08MigrationZK5) |
| Story Lead             |                                                                          |
| Next Story             |                                                                          |
| Passed acceptance test | No                                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Fixed combo style in Firefox and Epiphany.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Jul 2011

Attended to coordination meeting and reviewed items to fix.

-- [LorenzoTilve](/twiki/Main/LorenzoTilve) - 01 Aug 2011

Fixed issue with calendar exception days, they were not highlighted since ZK 5 migration. Now it's fixed, I've used jQuery for that you can read more info about that in ZK forum: <http://www.zkoss.org/forum/listComment/17068-Highlight-calendar-days-with-jQuery>

-- [ManuelRego](/twiki/Main/ManuelRego) - 04 Aug 2011

Fixed issue for highlight days in calendars in limiting resources datebox too.

-- [ManuelRego](/twiki/Main/ManuelRego) - 08 Aug 2011

Implemented widget for QueueTask[?](/twiki/bin/edit/LibrePlan/QueueTask?topicparent=LibrePlan.ItEr75S08MigrationZK5 "Create this topic") in ZK5-style.

Added the parameters idTaskOrig and idTaskEnd to the widget LimitingDependencyComponent[?](/twiki/bin/edit/LibrePlan/LimitingDependencyComponent?topicparent=LibrePlan.ItEr75S08MigrationZK5 "Create this topic") .

Started writing the code to draw the dependency, trying to reuse the code from ganttz.DependencyComponent instead of adapting the code from the 3.x version.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 21 Sep 2011

Implemented dependency draw using the code of the old ZK3.x version as a base.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 23 Sep 2011

Fixed the problem of dependencies not being rendered in the correct place of the DOM. Cleaned and commited the patches.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 27 Sep 2011

Fixed \#1198 and \#1203.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 06 Oct 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                   | 40                                                                                                                                                   | 0                                                                                                                                                      | 0                                                                                                                                                      | Low                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                           | [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                        | [ZK5 migration](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK1)                                                                                      |                                                                                                                                                             |                                                                                                                                                               |                                                                                                                                                            |
| Task                                                                                                                                                   | 80                                                                                                                                                   | 37.5                                                                                                                                                   | 0                                                                                                                                                      | Low                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                           | [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                          | [Layout fixes for migration to ZK5](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK2)                                                                  |                                                                                                                                                             |                                                                                                                                                               |                                                                                                                                                            |
| Task                                                                                                                                                   | 0                                                                                                                                                    | 8.5                                                                                                                                                    | 0                                                                                                                                                      | Low                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                           | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                              | [Layout fixes for migration to ZK5](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK2)                                                                  |                                                                                                                                                             |                                                                                                                                                               |                                                                                                                                                            |
| Task                                                                                                                                                   | 40                                                                                                                                                   | 102.92                                                                                                                                                 | 0                                                                                                                                                      | Low                                                                                                                                                   | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                           | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                      | [Do the migration of the components to ZK5 of the limiting resources window.](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK2)                        |                                                                                                                                                             |                                                                                                                                                               |                                                                                                                                                            |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S08MigrationZK5?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                     | 37.5                                                                                                                                                                | 0                                                                                                                                                                   | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                    |
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                         | 8.5                                                                                                                                                                 | 0                                                                                                                                                                   | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                    |
| [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                   | 0                                                                                                                                                                   | 0                                                                                                                                                                   | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                     |
| [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                 | 102.92                                                                                                                                                              | 0                                                                                                                                                                   | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                    |
| Total                                                                                                                                                 | 148.92                                                                                                                                                              | 0                                                                                                                                                                   | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                    |

------------------------------------------------------------------------
