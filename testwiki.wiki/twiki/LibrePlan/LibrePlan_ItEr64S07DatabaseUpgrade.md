[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr64S07DatabaseUpgrade](LibrePlan_ItEr64S07DatabaseUpgrade "Topic revision: 10 (20 Aug 2012 - 09:52:49)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr64S07DatabaseUpgrade?t=1520343640 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr64S07DatabaseUpgrade "Attach an image or document to this topic")  

 [ItEr64S07DatabaseUpgrade](LibrePlan_ItEr64S07DatabaseUpgrade)
===============================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Database upgrade                                                                 |
| Iteration              | [ItEr64week47To48](LibrePlan_ItEr64week47To48)                                   |
| FEA                    | [ItEr64S07DatabaseUpgrade](LibrePlan_ItEr64S07DatabaseUpgrade)                   |
| Story Lead             |                                                                                  |
| Next Story             | [ItEr65S05DatabaseUpgradeItEr64S07](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07) |
| Passed acceptance test | No                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

After a review of different tools that make easy the process to maintain the database updated, it seems that [LiquiBase](http://www.liquibase.org/) has a lot of interesting features:

-   Hibernate integration
-   Maven plugin
-   Custom refactorizations

Configured maven plugin for LiquiBase based on information at: <http://www.liquibase.org/manual/maven>

-- [ManuelRego](Main_ManuelRego) - 24 Nov 2010

We need to check how we could generate SQL sentences to be applied on a production database when LibrePlan is not deployed using Maven.

Fixed [bug \#37](https://bugs.navalplan.org/show_bug.cgi?id=37) renaming all tables and fields in order to avoid problems between MySQL and PostgreSQL.

Uploaded LiquiBase plugin configuration, after checking that it would be possible to generate a SQL from the change sets: <http://www.liquibase.org/manual/sql_output>

-- [ManuelRego](Main_ManuelRego) - 30 Nov 2010

Added documentation about how to use LiquiBase and database conventions at [Documentation](LibrePlan_Documentation) page.

-- [ManuelRego](Main_ManuelRego) - 01 Dec 2010

We need to work more in this issue as we have problems for people downloading for first time the project with an empty database. Please see next message at LiquiBase forum to understand the problem and possible solutions: <http://liquibase.org/forum/index.php?topic=814.0>

-- [ManuelRego](Main_ManuelRego) - 03 Dec 2010

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Entregables de código

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Task                                                                                                  | 4                                                                                                   | 14.25                                                                                                 | 0                                                                                                     | Low                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                          | [ManuelRego](Main_ManuelRego)                                                                             | [Assess database upgrade possibilities](LibrePlan_AnA04S03DatabaseUpgrade#TasK1)                          |                                                                                                            |                                                                                                              |                                                                                                           |

###  Total Hours in this Story

| [User](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr64S07DatabaseUpgrade?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                        | 14.25                                                                                                              | 0                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                   |
| Total                                                                                                | 14.25                                                                                                              | 0                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                   |

------------------------------------------------------------------------
