[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA11S02ConcurrencyProblemWorkReports](LibrePlan_AnA11S02ConcurrencyProblemWorkReports "Topic revision: 3 (02 Apr 2012 - 07:16:14)") (02 Apr 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?t=1520344055 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA11S02ConcurrencyProblemWorkReports "Attach an image or document to this topic")  

 [AnA11S02ConcurrencyProblemWorkReports](LibrePlan_AnA11S02ConcurrencyProblemWorkReports)
=========================================================================================

|                        |                                                                                          |
|------------------------|------------------------------------------------------------------------------------------|
| Story summary          | Solve concurrency limitations of saving work reports                                     |
| Iteration              | [AnA11UsersModule](LibrePlan_AnA11UsersModule)                                           |
| FEA                    | [AnA11S02ConcurrencyProblemWorkReports](LibrePlan_AnA11S02ConcurrencyProblemWorkReports) |
| Story Lead             |                                                                                          |
| Next Story             |                                                                                          |
| Passed acceptance test | No                                                                                       |

###  Tasks

The problem that addresses this analysis is a concurrency behavior which happens on saving work reports. This concurrency behavior limits the parallel operations of tracking time and working in the project planning that the work reports are devoting hours at the same time.

So, when:

-   A user is tracking time storing work reports devoting time to tasks belonging to a project P.
-   Another user is planning (modifying any information) in the project planning perspectives of the P project (Project Planning, Project Details, Resource Load, Advanced allocation).

a collision may occur.

The reason why currently saving a work report may cause an optimistic locking exception on storing a project planning is a precalculation mechanism that has been implemented to save for each order element (leaf or container) the sum of all the work hours that have been devoted to it or any of its descendants.

The motivation of this cache mechanism is to improve the performance of loading the projects. In order to load a project before this precalculation subsystem, it was needed to query to the database for each order element all the work reports that imputed time to it (direct assignment) or to any of its descendants (indirect assigment). This had an overhead that was avoided by having the sum of hours calculated.

####  Change the way the SumChargedEffort are created and mapped to the database

***Current data structures***

The precalculated addition of tracking time is currently stored in a class called `SumChargedEffort` with the following configuration:

-   Two attributes:
    -   `directChargedEffort`. It is the sum of the time devoted by all work report lines directly imputing to the bound order element.
    -   `indirectChargedEffort`. It is the sum of the time devoted by all work report lines imputing time to any of the descendants of the bounded order element (if any).
-   The `SumChargedEffort` objects are creating on saving a project plan.
-   They have the following Hibernate mapping options:

&nbsp;

       
       <many-to-one name="sumChargedEffort"
               class="SumChargedEffort"
               column="sum_charged_effort_id"
               cascade="save-update, delete"
               unique="true"
               lazy="false"/>

Because of the cascade option *save-udpate* the `SumChargedEffort` objects are updated every time a project plan is saved, and this is the cause of the concurrency conflict.

***Proposed solution***

The analysis solution for this concurrency limitation is based on the following points:

1.  The `SumChargedEffort` objects are only needed in read access in the project plan. And as they're going to be created when a work report is saved, we need to have a relation from the `SumChargedEffort` to the `OrderElement`. Then the mapping should be changed in order to have a one-to-one relation from `OrderElement` to `SumChargedEffort` and a many-to-one from `SumChargedEffort` to `OrderElement`.
2.  The creation of the `SumChargedEffort` objets must be done from the work report edition window instead of being creating from the project plan. To do this, the algorithm must be take into account the following points:
    1.  Before saving a work report line, it must queried if there is in the DB the bound `SumChargedObject` of the order element the work report line is going to charge time. Let's call OE-A to this order element.
    2.  If there is that `SumChargedEffort` object, it must be brought into memory - that object and all its ancestors. By ancestors I mean all the `SumChargedEffort` objects bound to the ancestors of the order element OE-A.
    3.  If there is not `SumChargedEffort` object bound to OE-A, this `SumChargedEffort` object must be created. It must be checked that there is also linked `SumChargedEffort` object to each of the OE-A ancestors. If not, they must be created all the `SumChargedEffort` objects needed.

As a note, it is assumed that the work report lines are saved one by one. If all the work report lines of a work report are saved at the same time, in a single operation, the algorithm must be modified slightly. The modification is related to the detection of the existence of the `SumChargedEffort` objects. They check will consist in this case in two points:

1.  Check if the `SumChargedEffort` is in memory (in the state). The state in memory can be a transiet object or an older one (already with id). If exists in memory, must be reused.
2.  Query the database for the existence of the `SumChargedEffort` object.

####  Recalculate SumChargedEffort when order elements are moved in the WBS

***Description***

This mail is to solve one point that had passed unnoticed in the first analysis proposal.

The thing is that the order elements can be moved in the WBS structure, and because of these movements, the hours imputed by the work reports must be recalculated.

Currently this situation is not being taken into account and, therefore, is a bug of the program that is needed to be solved.

***Proposed solution***

The easiest and satisfactory solution is to do two things:

a) To include in the WBS interface a mechanism to track when an order element with work reports imputing hours has been moved. The order would be flagged as: NeededToRecalculateWorkReports

b) In the method which saves all the shared state among the project perspectives, to include a new method placed in the end of storing operations. The execution of this new method would be optional and would happen when the project is marked as NeededToRecalculateWorkReports.

The body of these method will recalculate and save each object SumChargedEffort of all the order elements of the project.

I think it is not worth implementing a tracking system to know which specific SumChargedEffort objects is needed to calculate and save.

This solutions keeps being satisfactory of the concurrency problem because the cases where a order element is moved when it has already received work reports should be a small percentage of the cases. Therefore, the probability of conflict is low.

###  User stories

-   [ItEr76S14ConcurrencyProblemWorkReports](LibrePlan_ItEr76S14ConcurrencyProblemWorkReports)

###  Tasks in this story

| [Tasks](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=7;table=2;up=0#sorted_table "Sort by this column")              | [Start Date](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                               | 14                                                                                                               | 14                                                                                                                 | 0                                                                                                                  | Low                                                                                                               | [JavierMoran](Main_JavierMoran)                                                                                       | [ManuelRego](Main_ManuelRego)                                                                                          | [Change the way the SumChargedEffort are created and mapped to the database](LibrePlan_AnA11S02ConcurrencyProblemWorkReports#TasK1) |                                                                                                                         |                                                                                                                           |                                                                                                                        |
| Task                                                                                                               | 10                                                                                                               | 10                                                                                                                 | 0                                                                                                                  | Low                                                                                                               | [JavierMoran](Main_JavierMoran)                                                                                       | [ManuelRego](Main_ManuelRego)                                                                                          | [Recalculate SumChargedEffort when order elements are moved in the WBS](LibrePlan_AnA11S02ConcurrencyProblemWorkReports#TasK2)      |                                                                                                                         |                                                                                                                           |                                                                                                                        |

###  Total Hours in this Story

| [User](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA11S02ConcurrencyProblemWorkReports?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                                     | 24                                                                                                                              | 0                                                                                                                               | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                |
| Total                                                                                                             | 24                                                                                                                              | 0                                                                                                                               | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                |

------------------------------------------------------------------------
