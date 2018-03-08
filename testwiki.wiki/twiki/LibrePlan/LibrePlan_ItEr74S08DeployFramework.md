[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr74S08DeployFramework](LibrePlan_ItEr74S08DeployFramework "Topic revision: 7 (03 Jan 2012 - 13:13:39)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_ItEr74S08DeployFramework?t=1520343673 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr74S08DeployFramework "Attach an image or document to this topic")  

 [ItEr74S08DeployFramework](LibrePlan_ItEr74S08DeployFramework)
===============================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Deploy framework                                                                 |
| Iteration              | [ItEr74week14To24](LibrePlan_ItEr74week14To24)                                   |
| FEA                    | [ItEr74S08DeployFramework](LibrePlan_ItEr74S08DeployFramework)                   |
| Story Lead             |                                                                                  |
| Next Story             | [ItEr75S19DeployFrameworkItEr74S08](LibrePlan_ItEr75S19DeployFrameworkItEr74S08) |
| Passed acceptance test | No                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

###  Load Tests

For doing a simple load stress test I've used jMeter. In Ubuntu can be installed `apt-get install jmeter`. Your mileage may vary.

You should open load-test-libreplan.jmx file with jMeter. It contains a stress test with 20 simultaneous users accessing several parts of the application. It contains a big order and a small order. The ids of the orders are hardcoded in the urls of the stress test, so you should use the attached dumps or modify the stress test. There is one dump for just before the merge of migration-to-zk5 and one for the current point in master. You can get it up to date applying liquibase migrations, i.e., `mvn process-resources`.

In order to execute the test:

-   Initialize database with one of the associated dumps and run `mvn process-resources` to get it up to date.
-   Launch navalplan
-   In jMeter File -&gt; Open and choose the attached .jmx file.
-   In jMeter Run -&gt; Start
-   You can see the results in Summary Report as they are being produced.
-   When you have enough samples, for example around 60 for each action you can do Run -&gt; Stop

Results for before the merge and after the merge are attached in .csv format, showing an improvement using zk5.

Results have been produced using a Intel(R) Core(TM)2 Duo CPU T7700 @ 2.40GHz with two cores and 4096 KB of cache. RAM memory: 2Gb. Jetty was launched with -Xmx1024m. PostgreSQL[?](LibrePlan_PostgreSQL?topicparent=LibrePlan.ItEr74S08DeployFramework "Create this topic") 8.4 with default configuration has been used. java version "1.6.0\_20" OpenJDK[?](LibrePlan_OpenJDK?topicparent=LibrePlan.ItEr74S08DeployFramework "Create this topic") Runtime Environment (IcedTea6[?](LibrePlan_IcedTea6?topicparent=LibrePlan.ItEr74S08DeployFramework "Create this topic") 1.9.8) kernel version: 2.6.35-30-generic \#54-Ubuntu SMP i686

If you want to reproduce the results for before the merge go to c50dbd372c7bbbd0dede04ad53d21dfe163a785c and `cherry-pick f66cf0f278084acdbaee993aa51093bb49a28219` . Otherwise the results of loading the orders are not real (the orders are not really loaded).

-   [dump-for-before-merge.sql](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/dump-for-before-merge.sql): dump-for-before-merge.sql

&nbsp;

-   [load-test-libreplan.jmx](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/load-test-libreplan.jmx): load-test-libreplan.jmx

&nbsp;

-   [dump-for-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.sql](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/dump-for-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.sql): dump-for-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.sql

&nbsp;

-   [results-before-merge.csv](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/results-before-merge.csv): results-before-merge.csv

&nbsp;

-   [results-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.csv](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/results-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.csv): results-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.csv

-- [OscarGonzalez](Main_OscarGonzalez) - 02 Jul 2011

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

| [Tasks](LibrePlan_ItEr74S08DeployFramework?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr74S08DeployFramework?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr74S08DeployFramework?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr74S08DeployFramework?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr74S08DeployFramework?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr74S08DeployFramework?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr74S08DeployFramework?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr74S08DeployFramework?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr74S08DeployFramework?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr74S08DeployFramework?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr74S08DeployFramework?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Task                                                                                                  | 35                                                                                                  | 35                                                                                                    | 0                                                                                                     | Low                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                          | [OscarGonzalez](Main_OscarGonzalez)                                                                       | [Servlet container installation](LibrePlan_AnA04S05DeployFramework#TasK1)                                 |                                                                                                            |                                                                                                              |                                                                                                           |

###  Total Hours in this Story

| [User](LibrePlan_ItEr74S08DeployFramework?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr74S08DeployFramework?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr74S08DeployFramework?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr74S08DeployFramework?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [OscarGonzalez](Main_OscarGonzalez)                                                                  | 35                                                                                                                 | 0                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                   |
| Total                                                                                                | 35                                                                                                                 | 0                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                   |

------------------------------------------------------------------------

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_ItEr74S08DeployFramework#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_ItEr74S08DeployFramework#)

| [I](LibrePlan_ItEr74S08DeployFramework?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_ItEr74S08DeployFramework?sortcol=1;table=4;up=0#sorted_table "Sort by this column")                                                   | [Action](LibrePlan_ItEr74S08DeployFramework?sortcol=2;table=4;up=0#sorted_table "Sort by this column")                                                                                        |  [Size](LibrePlan_ItEr74S08DeployFramework?sortcol=3;table=4;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_ItEr74S08DeployFramework?sortcol=4;table=4;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_ItEr74S08DeployFramework?sortcol=5;table=4;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_ItEr74S08DeployFramework?sortcol=6;table=4;up=0#sorted_table "Sort by this column") |
|:-------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
|                       ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)sql                      | [dump-for-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.sql](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/dump-for-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.sql) | [manage](/twiki/bin/attach/LibrePlan/ItEr74S08DeployFramework?filename=dump-for-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.sql;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                               293.8 K| 02 Jul 2011 - 15:53                                                                                  | [OscarGonzalez](Main_OscarGonzalez)                                                                 |                                                                                                         |
|                       ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)sql                      | [dump-for-before-merge.sql](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/dump-for-before-merge.sql)                                                         | [manage](/twiki/bin/attach/LibrePlan/ItEr74S08DeployFramework?filename=dump-for-before-merge.sql;revInfo=1 "change, update, previous revisions, move, delete...")                             |                                                                                               293.0 K| 02 Jul 2011 - 15:52                                                                                  | [OscarGonzalez](Main_OscarGonzalez)                                                                 |                                                                                                         |
|                       ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)jmx                      | [load-test-libreplan.jmx](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/load-test-libreplan.jmx)                                                             | [manage](/twiki/bin/attach/LibrePlan/ItEr74S08DeployFramework?filename=load-test-libreplan.jmx;revInfo=1 "change, update, previous revisions, move, delete...")                               |                                                                                                21.4 K| 02 Jul 2011 - 15:51                                                                                  | [OscarGonzalez](Main_OscarGonzalez)                                                                 |                                                                                                         |
|                       ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)csv                      | [results-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.csv](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/results-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.csv)   | [manage](/twiki/bin/attach/LibrePlan/ItEr74S08DeployFramework?filename=results-8cdaf4e50381b7550fc01455553d8b31dc03fbf5.csv;revInfo=1 "change, update, previous revisions, move, delete...")  |                                                                                                 1.4 K| 02 Jul 2011 - 15:54                                                                                  | [OscarGonzalez](Main_OscarGonzalez)                                                                 |                                                                                                         |
|                       ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)csv                      | [results-before-merge.csv](/twiki/pub/LibrePlan/ItEr74S08DeployFramework/results-before-merge.csv)                                                           | [manage](/twiki/bin/attach/LibrePlan/ItEr74S08DeployFramework?filename=results-before-merge.csv;revInfo=1 "change, update, previous revisions, move, delete...")                              |                                                                                                 1.4 K| 02 Jul 2011 - 15:54                                                                                  | [OscarGonzalez](Main_OscarGonzalez)                                                                 |                                                                                                         |