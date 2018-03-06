[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr61S03RFPerformanceCompanyView](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView "Topic revision: 12 (11 Oct 2010 - 10:31:33)") (11 Oct 2010, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr61S03RFPerformanceCompanyView?t=1520337874 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr61S03RFPerformanceCompanyView "Attach an image or document to this topic")

 [ItEr61S03RFPerformanceCompanyView](/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Performance of company view                                                                      |
| Iteration              | [ItEr61week38To40](/twiki/LibrePlan/ItEr61week38To40)                                   |
| FEA                    | [ItEr61S03RFPerformanceCompanyView](/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 23 Sep 2010:

I've added the attribute and implemented the methods to update it in cascade, but with this issues:

-   I started the development before the analysis was ready, so I added to attributes to store directly and indirectly allocated hours. It has to be reduced to only one attribute.
-   I'm trying to test the update methods, but:
    -   I didn't manage to make a SpecificResourceAllocation return &gt; 0 in allocation.getAssignedHours(), even when I used .createAssignmentsAtDay() to add DayAssignments. Did I use the latter method wrongly, maybe?
    -   I'm getting an exception from hibernate, which is caused by a change in the primary key of the Task entity inside the ResourceAllocation object, according to [some comments in the internet](http://www.coderanch.com/t/215964/ORM/java/change-value-PK-Hibernate) that I have checked by myself (when execution reaches the second IOnTransaction, the id of the Task has changed):

<!-- -->

          HibernateSystemException: Don't change the reference to a collection with cascade="all-delete-orphan":
          org.navalplanner.business.planner.entities.TaskElement.dependenciesWithThisOrigin

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 27 Sep 2010:

I've replaced the two attributes direct and indirectAllocatedHours with a single one. I've also solved the problem wih the HibernateSystemException in the unit tests. I still have to fix the problem with allocation.getAssignedHours() returning 0.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 28 Sep 2010:

I was studing the implementation of the application model to add the calls to updateSumOfAllocatedHoursWithResourceAllocationSet in the proper places. This approach ended being too complicated, so I started a different one: I reimplemented TaskElementDAO[?](/twiki/bin/edit/LibrePlan/TaskElementDAO?topicparent=LibrePlan.ItEr61S03RFPerformanceCompanyView "Create this topic") .save() to update the attribute sumOfHoursAllocated when saving.

The new approach looks better (cleaner, less changes) but has some problems:

-   A process of update from parents to children seems to be necessary.
-   Doesn't update the changes made in the advanced allocation screen.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 29 Sep 2010:

-   Tried to implement the update of sumOfHoursAllocated with Hibernate callbacks, unsuccessfully.
-   Implemented update of sumOfHoursAllocated attribute from parents to children.
-   Updated the unit tests with the new operations.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 30 Sep 2010:

-   Corrected the unit test.
-   Modified Advanced Allocation screen to update correctly sumOfHoursAllocated.
-   Modified company screen to use the new functions.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 01 Oct 2010:

I've been measuring the impact of the changes in the performance, using my test DB. We have the following facts:

-   The time consumed by the operation TaskElementWrapper.getAdvanceEndDate() has been reduced from 6.44 s to just 320 us.
-   Unfortunately, the time consumed by CompanyPlanningModel.setConfigurationToPlanner() has only been reduced from 15.1 s to 12.4 s. It means that some of the load operations that were being done in getAdvanceEndDate() now are done in a later call to a different method.
-   To verify this, I've checked the hibernate log, and I've found that data from day\_assignment table is still being loaded, and it shouldn't.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 06 Oct 2010:

I've located the point where the application loads the DayAssignments, and fixed it with patch 0e3788. That operation used to take 4,57 s which were reduced to 737 ms. The time of the operation CompanyPlanningModel.setConfigurationToPlanner() has decreased from 5.18 s to 1.08 s.

Anyway, there are still a lot of unnecessary queries. There are ~500 queries asking for the attribute hoursGroups (a list) inside OrderLine[?](/twiki/bin/edit/LibrePlan/OrderLine?topicparent=LibrePlan.ItEr61S03RFPerformanceCompanyView "Create this topic") . Those loads took around 1.47 s, and have been prevented now with commits 79425 and 222c9.

**Delay Causes**

**Final or Pending Considerations**

###  Entregables de código

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr61S03RFPerformanceCompanyView?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 7                                                                                                                                                                | 44.25                                                                                                                                                              | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                       | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                  | [Calculate and save the number of hours allocated to a task](/twiki/LibrePlan/AnA03RFPerformanceCompanyView#TasK1)                                            |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |
| Task                                                                                                                                                               | 0                                                                                                                                                                | 0                                                                                                                                                                  | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                       | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                  | [Snapshot to calculate the load chart in company view](/twiki/LibrePlan/AnA03RFPerformanceCompanyView#TasK2)                                                  |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |

------------------------------------------------------------------------
