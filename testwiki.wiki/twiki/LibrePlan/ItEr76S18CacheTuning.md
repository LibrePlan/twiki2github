[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr76S18CacheTuning](LibrePlan_ItEr76S18CacheTuning "Topic revision: 14 (20 Aug 2012 - 09:50:17)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr76S18CacheTuning?t=1520343695 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S18CacheTuning "Attach an image or document to this topic")  

 [ItEr76S18CacheTuning](LibrePlan_ItEr76S18CacheTuning)
=======================================================

|                        |                                                        |
|------------------------|--------------------------------------------------------|
| Story summary          | Cache Tuning                                           |
| Iteration              | [ItEr76Week01To33](LibrePlan_ItEr76Week01To33)         |
| FEA                    | [ItEr76S18CacheTuning](LibrePlan_ItEr76S18CacheTuning) |
| Story Lead             |                                                        |
| Next Story             |                                                        |
| Passed acceptance test | No                                                     |

###  Acceptance Criteria

-   Activate Second-Level Cache
    -   Measure perfomance improvements (check if there are cache hits)
-   Activate Batch-Fetching
    -   Check if there are less SQL queries
    -   Check with fetch strategies: *size = 2* and *subselect*

###  Additional Specification Comments

###  Implementation Notes

-- [DiegoPino](Main_DiegoPino) - 19 Mar 2012

**Caches**

Entidades que tienen cachés activadas:

-   AdvanceType:nonstrict-read-write
-   AdvanceType:nonstrict-read-write
-   BaseCalendar:read-write
-   TypeOfWorkHours:nonstrict-read-write
-   Label:nonstrict-read-write
-   LabelType:nonstrict-read-write
-   labels:nonstrict-read-write
-   UnitType:nonstrict-read-write
-   Resource:read-write
-   criterionSatisfactions:read-write
-   Criterion:nonstrict-read-write
-   CriterionSatisfaction:read-write
-   CriterionType:nonstrict-read-write
-   criterions:nonstrict-read-write
-   WorkReportType:nonstrict-read-write

Did:

-   Read about second-level cache and batch fetching (read Hibernate's bible chapter about caches and batch fetching, plus several blogs).
-   Wrote the analysis story with all the information collected.
-   Created a project with several entities which were set to be cached.

-- [DiegoPino](Main_DiegoPino) - 26 Mar 2012

-   I managed to configure Hibernate for using second-level cache and logging the second cache activity to a file.
-   There are cache-hits for BaseCalendar.
-   TODO: Try other entities and find a way to measure the performance improvement.

**Cache hits**

-   AdvanceType:checked
-   BaseCalendar:checked
-   TypeOfWorkHours:checked
-   Label:checked
-   LabelType:checked
-   labels:checked
-   UnitType:checked
-   Resource:checked
    -   criterionSatisfactions:checked
-   Criterion:checked
-   CriterionSatisfaction:checked
-   CriterionType:checked
    -   criterions:checked
-   WorkReportType:checked

I checked that all the entities that have second-level cached configured are being cached and there are cache hits for all of them.

-- [DiegoPino](Main_DiegoPino) - 27 Mar 2012

-   Identify which entities could benefit the most from batch fetching.
-   Identify entities that have sets.
-   Activate batch-size=10 for all one-to-many sets in all Entitites.
-   When I opened my current project I got the following error in the Gantt view: "Failed to process invoke W\[V\] is undefined (TypeError[?](LibrePlan_TypeError?topicparent=LibrePlan.ItEr76S18CacheTuning "Create this topic") )".
-   I had to fix a coding error in liquibase in order to launch [LibrePlan](LibrePlan_LibrePlan).

-- [DiegoPino](Main_DiegoPino) - 28 Mar 2012

It seems batch-size="10" is not working for sets. I get a LazyInitializationException. Things to try:

-   Configurate batch\_fetch\_size at global level. hibernate.default\_batch\_fetch\_size.
-   Configure batch\_fetching for only one entity OrderElement[?](LibrePlan_OrderElement?topicparent=LibrePlan.ItEr76S18CacheTuning "Create this topic") .

-- [DiegoPino](Main_DiegoPino) - 28 Mar 2012

It seems batch-size="10" is not working for sets. I get a LazyInitializationException. Things to try:

-   Configurate batch\_fetch\_size at global level. hibernate.default\_batch\_fetch\_size.
-   Configure batch\_fetching for only one entity OrderElement[?](LibrePlan_OrderElement?topicparent=LibrePlan.ItEr76S18CacheTuning "Create this topic") .

-- [DiegoPino](Main_DiegoPino) - 18 Apr 2012

I did some benchmarking of the cache-tunning branch. I used Jmeter, following the instructions at:

<http://wiki.libreplan.orgLibrePlan_ItEr74S08DeployFramework>

Here are the results:

-   [without-cache-tunning.csv](/twiki/pub/LibrePlan/ItEr76S18CacheTuning/before-cache-tunning.csv): Without cache tunning (commit: 7c91d)
-   [with-cache-tunning.csv](/twiki/pub/LibrePlan/ItEr76S18CacheTuning/after-cache-tunning.csv): With cache tunning

I executed the tests twice and the results are identical. I notice a big improvement on the **MAX** value and **Standard Deviation** with cache-tunning, the other values improve only a bit or are almost identical.

The results are apparently better using cache-tunnning and batch-fetching, specially the standard deviation, but I don't fully understand what each parameter means. I was reading about it here: [Some thoughts on stress testing with JMeter](http://nico.vahlas.eu/2010/03/30/some-thoughts-on-stress-testing-web-applications-with-jmeter-part-2/)

-- [DiegoPino](Main_DiegoPino) - 16 May 2012

I have been reading about JMeter, how to understand the results, etc. What puzzled me a bit was that with the given results I couldn't understand if the performance improved or not. I was looking for something like *response time* but couldn't find it.

The columns *average*, *aggregate\_report\_min* and *aggregate\_report\_max* are a measure of the response time for each use case. With the caches the average of these results improve a bit but what improves the most is the *max* value. As the *max* value decreases significantly the *standard deviation* (varianza) decreases a lot too.

In conclusion, with the adjustments done the results are much better and is worth to push these patches to master.

**Summary**

Summary of the results *without cache* and *with cache*.

| [aggregate\_report\_count](LibrePlan_ItEr76S18CacheTuning?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [average](LibrePlan_ItEr76S18CacheTuning?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [aggregate\_report\_min](LibrePlan_ItEr76S18CacheTuning?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [aggregate\_report\_max](LibrePlan_ItEr76S18CacheTuning?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [aggregate\_report\_stddev](LibrePlan_ItEr76S18CacheTuning?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [aggregate\_report\_error%](LibrePlan_ItEr76S18CacheTuning?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [aggregate\_report\_rate](LibrePlan_ItEr76S18CacheTuning?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [aggreg\_report\_bandwidth](LibrePlan_ItEr76S18CacheTuning?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [average\_bytes](LibrePlan_ItEr76S18CacheTuning?sortcol=8;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| 520                                                                                                                  | 2                                                                                                   | 1                                                                                                                  | 34                                                                                                                 | 2.7873014828347897                                                                                                    | 1.0                                                                                                                   | 2.0230156939332873                                                                                                  | 2.934934241048156                                                                                                     | 1485.5903846153847                                                                                         |
| 521                                                                                                                  | 2                                                                                                   | 0                                                                                                                  | 9                                                                                                                  | 0.9711978332274673                                                                                                    | 1.0                                                                                                                   | 1.9918338634695378                                                                                                  | 2.8898175199661273                                                                                                    | 1485.6525911708254                                                                                         |
| \-                                                                                                                   | 0%                                                                                                  | 100%                                                                                                               | 75%                                                                                                                | 65%                                                                                                                   | \-                                                                                                                    | \-                                                                                                                  | \-                                                                                                                    | \-                                                                                                         |

Explanation:

-   **Aggregate report count**. It's the number of use cases executed. According to <http://wiki.libreplan.orgLibrePlan_ItEr74S08DeployFramework>, Oscar recommended to execute 60 samples for each use case. Both tests, executed a similar number of samples (520 vs 521, a difference of 1).
-   **Average**. It's the average response time. On average there is no gain.
-   **Aggregate\_report\_min**. It's the min response time. With cache the min is 0, without cache 1.
-   **Aggregate\_report\_max**. It's the max response time. With cache the max is 9, without cache 34, so there's a 75% gain (34 - 9 / 34)
-   **Aggregate\_report\_stddev**. Standard deviation. Without cache was high because the the average is 2 and the min and max are 1 and 34 respectively.

As with caches the max value is considerably reduced, the standard deviation is reduced too. There's a 65%.

Times are in milliseconds. More info here: [JMeter Aggregate Report](https://jmeter.apache.org/usermanual/component_reference.html#Aggregate_Report)

-- [DiegoPino](Main_DiegoPino) - 16 May 2012

|     |     |
|-----|-----|
|     |     |

###  Delay Causes

###  Final or Pending Considerations

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr76S18CacheTuning?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr76S18CacheTuning?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr76S18CacheTuning?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr76S18CacheTuning?sortcol=3;table=3;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr76S18CacheTuning?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr76S18CacheTuning?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr76S18CacheTuning?sortcol=6;table=3;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr76S18CacheTuning?sortcol=7;table=3;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr76S18CacheTuning?sortcol=8;table=3;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr76S18CacheTuning?sortcol=9;table=3;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr76S18CacheTuning?sortcol=10;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Task                                                                                              | 35                                                                                              | 32                                                                                                | 0                                                                                                 | Low                                                                                              | [ManuelRego](Main_ManuelRego)                                                                        | [DiegoPino](Main_DiegoPino)                                                                           | Implementation                                                                                        | 12/03/2011                                                                                             | 23/03/2011                                                                                               | 24/05/2012                                                                                            |

###  Total Hours in this Story

| [User](LibrePlan_ItEr76S18CacheTuning?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr76S18CacheTuning?sortcol=1;table=4;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr76S18CacheTuning?sortcol=2;table=4;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr76S18CacheTuning?sortcol=3;table=4;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [DiegoPino](Main_DiegoPino)                                                                      | 32                                                                                                             | 0                                                                                                              | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                               |
| Total                                                                                            | 32                                                                                                             | 0                                                                                                              | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                               |

------------------------------------------------------------------------

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_ItEr76S18CacheTuning#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_ItEr76S18CacheTuning#)

| [I](LibrePlan_ItEr76S18CacheTuning?sortcol=0;table=5;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_ItEr76S18CacheTuning?sortcol=1;table=5;up=0#sorted_table "Sort by this column") | [Action](LibrePlan_ItEr76S18CacheTuning?sortcol=2;table=5;up=0#sorted_table "Sort by this column")                                                           |  [Size](LibrePlan_ItEr76S18CacheTuning?sortcol=3;table=5;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_ItEr76S18CacheTuning?sortcol=4;table=5;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_ItEr76S18CacheTuning?sortcol=5;table=5;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_ItEr76S18CacheTuning?sortcol=6;table=5;up=0#sorted_table "Sort by this column") |
|:---------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|
|                     ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)csv                    | [after-cache-tunning.csv](/twiki/pub/LibrePlan/ItEr76S18CacheTuning/after-cache-tunning.csv)           | [manage](/twiki/bin/attach/LibrePlan/ItEr76S18CacheTuning?filename=after-cache-tunning.csv;revInfo=1 "change, update, previous revisions, move, delete...")  |                                                                                             1.2 K| 18 Apr 2012 - 16:09                                                                              | [DiegoPino](Main_DiegoPino)                                                                     | With cache tunning                                                                                  |
|                     ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)csv                    | [before-cache-tunning.csv](/twiki/pub/LibrePlan/ItEr76S18CacheTuning/before-cache-tunning.csv)         | [manage](/twiki/bin/attach/LibrePlan/ItEr76S18CacheTuning?filename=before-cache-tunning.csv;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                             1.2 K| 18 Apr 2012 - 16:08                                                                              | [DiegoPino](Main_DiegoPino)                                                                     | Without cache tunning (7c91d)                                                                       |
