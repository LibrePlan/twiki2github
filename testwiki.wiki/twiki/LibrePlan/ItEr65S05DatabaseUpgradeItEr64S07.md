[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr65S05DatabaseUpgradeItEr64S07](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07 "Topic revision: 7 (03 Mar 2011 - 06:42:58)") (03 Mar 2011, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?t=1520343643 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr65S05DatabaseUpgradeItEr64S07 "Attach an image or document to this topic")  

 [ItEr65S05DatabaseUpgradeItEr64S07](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07)
=================================================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Database upgrade                                                                 |
| Iteration              | [ItEr65week49To50](LibrePlan_ItEr65week49To50)                                   |
| FEA                    | [ItEr65S05DatabaseUpgradeItEr64S07](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07) |
| Story Lead             | [ItEr64S07DatabaseUpgrade](LibrePlan_ItEr64S07DatabaseUpgrade)                   |
| Next Story             |                                                                                  |
| Passed acceptance test | No                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Review [LiquiBase forum](http://liquibase.org/forum/index.php?topic=814.0) for more info.

-- [ManuelRego](Main_ManuelRego) - 07 Dec 2010

Final solution:

-   First changelog that create database: `db.changelog-database.xml`
-   Keep using `db.changelog-initial.xml` for new changes
-   Disabled Hibernate schema generation, now it just validates the schema:

            <hibernate.hbm2ddl.auto>validate</hibernate.hbm2ddl.auto>

More info in the mail sent to [navalplan-devel](http://sourceforge.net/mailarchive/forum.php?thread_name=20101210104523.6babcede%40erizana&forum_name=navalplan-devel) mailing list.

-- [ManuelRego](Main_ManuelRego) - 10 Dec 2010

LiquiBase plugin has moved to a profile where [liquibase:update](http://www.liquibase.org/manual/maven_update) Maven goal will be executed. This profile is called **liquibase-update** and is enabled by default. It could be disabled it needed with: `-P-liquibase-update`

On the other hand another new profile for [liquibase:updateSQL](http://www.liquibase.org/manual/maven_updatesql) goal was created. This profile is called **liquibase-updatesql** and is disabled by default. In order to enable it you should disable the previous one, so the result will be something like: `-P-liquibase-update,liquibase-updatesql`

This second profile will generate a `migrate.sql` file with the SQL needed to be applied in a database. We could generate the SQL migration script just for a changelog file with the next argument: `-Dliquibase.changeLogFile=src/main/resources/db.changelog-initial.xml`

**TODO**:

-   Check how to integrate `diffChangeLog` in Maven in order to automatically create changesets when we modify `.hbm.xml` files. For the moment this is done manually:

&nbsp;

    java -jar liquibase.jar \
            --classpath=/home/mrego/.m2/repository/postgresql/postgresql/8.3-603.jdbc4/postgresql-8.3-603.jdbc4.jar:/home/mrego/.m2/repository/org/hibernate/hibernate/3.2.7.ga/hibernate-3.2.7.ga.jar:lib/liquibase-hibernate-2.0.jar:/home/mrego/.m2/repository/org/hibernate/hibernate-annotations/3.3.1.GA/hibernate-annotations-3.3.1.GA.jar:/home/mrego/.m2/repository/dom4j/dom4j/1.6.1/dom4j-1.6.1.jar:/home/mrego/.m2/repository/org/hibernate/hibernate-commons-annotations/3.0.0.ga/hibernate-commons-annotations-3.0.0.ga.jar:/home/mrego/.m2/repository/commons-logging/commons-logging/1.1.1/commons-logging-1.1.1.jar:/home/mrego/.m2/repository/org/hibernate/ejb3-persistence/1.0.1.GA/ejb3-persistence-1.0.1.GA.jar:/home/mrego/.m2/repository/commons-collections/commons-collections/3.2/commons-collections-3.2.jar:.:./hbms/ \
            --changeLogFile=db.changelog.xml \
            --driver=org.postgresql.Driver \
            --url=jdbc:postgresql://localhost/navaldev \
            --username=naval \
            --password=naval \
       diffChangeLog \
            --referenceUrl=hibernate:hibernate.cfg.xml

-- [ManuelRego](Main_ManuelRego) - 13 Dec 2010

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

| [Tasks](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                           | 10                                                                                                           | 13.75                                                                                                          | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [ManuelRego](Main_ManuelRego)                                                                                      | [Install and configure Liquibase](LibrePlan_AnA04S03DatabaseUpgrade#TasK2)                                         |                                                                                                                     |                                                                                                                       |                                                                                                                    |

###  Total Hours in this Story

| [User](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr65S05DatabaseUpgradeItEr64S07?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                                 | 13.75                                                                                                                       | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |
| Total                                                                                                         | 13.75                                                                                                                       | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |

------------------------------------------------------------------------
