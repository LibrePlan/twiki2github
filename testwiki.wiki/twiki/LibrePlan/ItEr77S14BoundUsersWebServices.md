[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S14BoundUsersWebServices](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices "Topic revision: 4 (28 Nov 2012 - 17:12:59)") (28 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S14BoundUsersWebServices?t=1520337948 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S14BoundUsersWebServices "Attach an image or document to this topic")

 [ItEr77S14BoundUsersWebServices](/twiki/LibrePlan/ItEr77S14BoundUsersWebServices)
============================================================================================================================================



|                        |                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------|
| Story summary          | Bound Users Web Services                                                                   |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                             |
| FEA                    | [ItEr77S14BoundUsersWebServices](/twiki/LibrePlan/ItEr77S14BoundUsersWebServices) |
| Story Lead             |                                                                                            |
| Next Story             |                                                                                            |
| Passed acceptance test | No                                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

The new services are implemented under a new URL `/ws/rest/bounduser/` that is restricted by Spring Security to `ROLE_BOUND_USER`.

The URLs of the new services are:

-   Service to get tasks assigned to a bound user: `/bounduser/mytasks`
-   Service to get personal timesheets data of a task: `/bounduser/timesheets/{task-code}/`
-   Service to import data for personal timesheets: `/bounduser/timesheets/`

-- [ManuelRego](/twiki/Main/ManuelRego) - 08 Nov 2012

Added documentation about the new web services.

-- [ManuelRego](/twiki/Main/ManuelRego) - 28 Nov 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S14BoundUsersWebServices?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                            | 1                                                                                                                                                             | 1                                                                                                                                                               | 0                                                                                                                                                               | Low                                                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                       | [Service to get tasks assigned to a bound user](/twiki/LibrePlan/AnA1204BoundUsersWebServices#TasK1)                                                       |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 1                                                                                                                                                             | 1                                                                                                                                                               | 0                                                                                                                                                               | Low                                                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                       | [Service to get personal timesheets data of a task](/twiki/LibrePlan/AnA1204BoundUsersWebServices#TasK2)                                                   |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |
| Task                                                                                                                                                            | 1                                                                                                                                                             | 2.5                                                                                                                                                             | 0                                                                                                                                                               | Low                                                                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                       | [Service to import data for personal timesheets](/twiki/LibrePlan/AnA1204BoundUsersWebServices#TasK3)                                                      |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |


