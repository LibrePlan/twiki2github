[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S14ConcurrencyProblemWorkReports](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports "Topic revision: 11 (19 Oct 2012 - 10:56:53)") (19 Oct 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?t=1520337936 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports "Attach an image or document to this topic")

 [ItEr76S14ConcurrencyProblemWorkReports](/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports)
==============================================================================================================================================================



|                        |                                                                                                            |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Story summary          | Concurrency problems work reports                                                                          |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                                             |
| FEA                    | [ItEr76S14ConcurrencyProblemWorkReports](/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports) |
| Story Lead             |                                                                                                            |
| Next Story             |                                                                                                            |
| Passed acceptance test | No                                                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

####  Change the way the SumChargedEffort are created and mapped to the database

Started to change the mapping and detected that we need to get rid of column `sum_charged_effort_id` in `order_element` table.

So finally the mapping will be as follows:

-   In **OrderElement**:

                <one-to-one name="sumChargedEffort" class="SumChargedEffort"
                    cascade="delete" property-ref="orderElement" />

-   In **SumChargedEffort**:

                <many-to-one name="orderElement" column="order_element"
                    class="OrderElement" cascade="none" unique="true" />

This implies to do a migration of data, moving info from column `sum_charged_effort_id` in `order_element` table to a new column `order_element` in `sum_charged_effort` table. In order to do this data migration it was needed to use specific procedures for PostgreSQL and MySQL.

-- [ManuelRego](/twiki/Main/ManuelRego) - 28 Mar 2012

Methods to update and create the `SumChargedEffort` has been moved from `OrderElementDAO` to `SumChargedEffortDAO` (actually the `SumChargedEffort` entities were created before by default every time an `OrderElement` was created).

In these methods a map is used to avoid query the database once the `SumChargedEffort` corresponding to an `OrderElement` has already been found before.

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 Mar 2012

####  Recalculate SumChargedEffort when order elements are moved in the WBS

It has been implemented the solution explained in the analysis adding a method `recalculateSumChargedEfforts` in `SumChargedEffortDAO` and an attribute `neededToRecalculateSumChargedEfforts` in `Order`.

Anyway it should be reviewed the possibility to use a thread for the recalculations in `SumChargedEffortDAO`. And avoid the current problem of concurrency that has been added again with this task.

-- [ManuelRego](/twiki/Main/ManuelRego) - 02 Apr 2012

Finally a thread to do this recalculations has been added.

~~The thread uses a `BlockingQueue` which provides 2 methods (`put` and `take`) that make easier the development of the thread.~~

The thread is launched in the constructor of a singleton class called `SumChargedEffortRecalculator` (this class is created by Spring). The thread has an infinite loop and it waits in the method `take` till there's any element in the queue in order to be recalculated.

Finally, a `BlockingQueue` was not needed and it was enough with a single `[http://docs.oracle.com/javase/1.5.0/docs/api/java/util/concurrent/ExecutorService.html][ExecutorService]]` which is in charge of run the thread that do the recalculations one by one.

The previous patch was modified to change the behavior explained in the strike-through text above for the new one.

-- [ManuelRego](/twiki/Main/ManuelRego) - 04 Apr 2012

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

-   Review problems in procedure with PostgreSQL 8. For the moment the solution is execute the following sentence with PostgreSQL superuser:

        CREATE LANGUAGE plpgsql;

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                    | 14                                                                                                                                                                    | 14                                                                                                                                                                      | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                               | [Change the way the SumChargedEffort are created and mapped to the database](/twiki/LibrePlan/AnA11S02ConcurrencyProblemWorkReports#TasK1)                         |                                                                                                                                                                              |                                                                                                                                                                                |                                                                                                                                                                             |
| Task                                                                                                                                                                    | 10                                                                                                                                                                    | 11.75                                                                                                                                                                   | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                               | [Recalculate SumChargedEffort when order elements are moved in the WBS](/twiki/LibrePlan/AnA11S02ConcurrencyProblemWorkReports#TasK2)                              |                                                                                                                                                                              |                                                                                                                                                                                |                                                                                                                                                                             |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S14ConcurrencyProblemWorkReports?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                          | 25.75                                                                                                                                                                                | 0                                                                                                                                                                                    | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                     |
| Total                                                                                                                                                                  | 25.75                                                                                                                                                                                | 0                                                                                                                                                                                    | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                     |

------------------------------------------------------------------------
