[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S08MigrationZK5](LibrePlan_ItEr75S08MigrationZK5 "Topic revision: 15 (05 Jan 2012 - 08:30:54)") (05 Jan 2012, [JacoboAragunde](Main_JacoboAragunde))[Edit](LibrePlan_ItEr75S08MigrationZK5?t=1520343677 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S08MigrationZK5 "Attach an image or document to this topic")  

 [ItEr75S08MigrationZK5](LibrePlan_ItEr75S08MigrationZK5)
=========================================================

|                        |                                                          |
|------------------------|----------------------------------------------------------|
| Story summary          | Migration to ZK5                                         |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)           |
| FEA                    | [ItEr75S08MigrationZK5](LibrePlan_ItEr75S08MigrationZK5) |
| Story Lead             |                                                          |
| Next Story             |                                                          |
| Passed acceptance test | No                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Fixed combo style in Firefox and Epiphany.

-- [ManuelRego](Main_ManuelRego) - 05 Jul 2011

Attended to coordination meeting and reviewed items to fix.

-- [LorenzoTilve](Main_LorenzoTilve) - 01 Aug 2011

Fixed issue with calendar exception days, they were not highlighted since ZK 5 migration. Now it's fixed, I've used jQuery for that you can read more info about that in ZK forum: <http://www.zkoss.org/forum/listComment/17068-Highlight-calendar-days-with-jQuery>

-- [ManuelRego](Main_ManuelRego) - 04 Aug 2011

Fixed issue for highlight days in calendars in limiting resources datebox too.

-- [ManuelRego](Main_ManuelRego) - 08 Aug 2011

Implemented widget for QueueTask[?](LibrePlan_QueueTask?topicparent=LibrePlan.ItEr75S08MigrationZK5 "Create this topic") in ZK5-style.

Added the parameters idTaskOrig and idTaskEnd to the widget LimitingDependencyComponent[?](LibrePlan_LimitingDependencyComponent?topicparent=LibrePlan.ItEr75S08MigrationZK5 "Create this topic") .

Started writing the code to draw the dependency, trying to reuse the code from ganttz.DependencyComponent instead of adapting the code from the 3.x version.

-- [JacoboAragunde](Main_JacoboAragunde) - 21 Sep 2011

Implemented dependency draw using the code of the old ZK3.x version as a base.

-- [JacoboAragunde](Main_JacoboAragunde) - 23 Sep 2011

Fixed the problem of dependencies not being rendered in the correct place of the DOM. Cleaned and commited the patches.

-- [JacoboAragunde](Main_JacoboAragunde) - 27 Sep 2011

Fixed \#1198 and \#1203.

-- [JacoboAragunde](Main_JacoboAragunde) - 06 Oct 2011

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

| [Tasks](LibrePlan_ItEr75S08MigrationZK5?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S08MigrationZK5?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S08MigrationZK5?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S08MigrationZK5?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S08MigrationZK5?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S08MigrationZK5?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S08MigrationZK5?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S08MigrationZK5?sortcol=7;table=2;up=0#sorted_table "Sort by this column")              | [Start Date](LibrePlan_ItEr75S08MigrationZK5?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S08MigrationZK5?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S08MigrationZK5?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Task                                                                                               | 40                                                                                               | 0                                                                                                  | 0                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [OscarGonzalez](Main_OscarGonzalez)                                                                    | [ZK5 migration](LibrePlan_AnA05S07MigrationZK5#TasK1)                                                               |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 80                                                                                               | 37.5                                                                                               | 0                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [LorenzoTilve](Main_LorenzoTilve)                                                                      | [Layout fixes for migration to ZK5](LibrePlan_AnA05S07MigrationZK5#TasK2)                                           |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 0                                                                                                | 8.5                                                                                                | 0                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [ManuelRego](Main_ManuelRego)                                                                          | [Layout fixes for migration to ZK5](LibrePlan_AnA05S07MigrationZK5#TasK2)                                           |                                                                                                         |                                                                                                           |                                                                                                        |
| Task                                                                                               | 40                                                                                               | 102.92                                                                                             | 0                                                                                                  | Low                                                                                               | [JavierMoran](Main_JavierMoran)                                                                       | [JacoboAragunde](Main_JacoboAragunde)                                                                  | [Do the migration of the components to ZK5 of the limiting resources window.](LibrePlan_AnA05S07MigrationZK5#TasK2) |                                                                                                         |                                                                                                           |                                                                                                        |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S08MigrationZK5?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S08MigrationZK5?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S08MigrationZK5?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S08MigrationZK5?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [LorenzoTilve](Main_LorenzoTilve)                                                                 | 37.5                                                                                                            | 0                                                                                                               | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                |
| [ManuelRego](Main_ManuelRego)                                                                     | 8.5                                                                                                             | 0                                                                                                               | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                |
| [OscarGonzalez](Main_OscarGonzalez)                                                               | 0                                                                                                               | 0                                                                                                               | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                 |
| [JacoboAragunde](Main_JacoboAragunde)                                                             | 102.92                                                                                                          | 0                                                                                                               | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                |
| Total                                                                                             | 148.92                                                                                                          | 0                                                                                                               | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                |

------------------------------------------------------------------------
