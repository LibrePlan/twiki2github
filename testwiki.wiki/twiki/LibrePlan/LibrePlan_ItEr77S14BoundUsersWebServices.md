[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr77S14BoundUsersWebServices](LibrePlan_ItEr77S14BoundUsersWebServices "Topic revision: 4 (28 Nov 2012 - 17:12:59)") (28 Nov 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr77S14BoundUsersWebServices?t=1520343706 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S14BoundUsersWebServices "Attach an image or document to this topic")  

 [ItEr77S14BoundUsersWebServices](LibrePlan_ItEr77S14BoundUsersWebServices)
===========================================================================

|                        |                                                                            |
|------------------------|----------------------------------------------------------------------------|
| Story summary          | Bound Users Web Services                                                   |
| Iteration              | [ItEr77Week34To44](LibrePlan_ItEr77Week34To44)                             |
| FEA                    | [ItEr77S14BoundUsersWebServices](LibrePlan_ItEr77S14BoundUsersWebServices) |
| Story Lead             |                                                                            |
| Next Story             |                                                                            |
| Passed acceptance test | No                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

The new services are implemented under a new URL `/ws/rest/bounduser/` that is restricted by Spring Security to `ROLE_BOUND_USER`.

The URLs of the new services are:

-   Service to get tasks assigned to a bound user: `/bounduser/mytasks`
-   Service to get personal timesheets data of a task: `/bounduser/timesheets/{task-code}/`
-   Service to import data for personal timesheets: `/bounduser/timesheets/`

-- [ManuelRego](Main_ManuelRego) - 08 Nov 2012

Added documentation about the new web services.

-- [ManuelRego](Main_ManuelRego) - 28 Nov 2012

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

| [Tasks](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr77S14BoundUsersWebServices?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                        | 1                                                                                                         | 1                                                                                                           | 0                                                                                                           | Low                                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                  | [ManuelRego](Main_ManuelRego)                                                                                   | [Service to get tasks assigned to a bound user](LibrePlan_AnA1204BoundUsersWebServices#TasK1)                   |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 1                                                                                                         | 1                                                                                                           | 0                                                                                                           | Low                                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                  | [ManuelRego](Main_ManuelRego)                                                                                   | [Service to get personal timesheets data of a task](LibrePlan_AnA1204BoundUsersWebServices#TasK2)               |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 1                                                                                                         | 2.5                                                                                                         | 0                                                                                                           | Low                                                                                                        | [ManuelRego](Main_ManuelRego)                                                                                  | [ManuelRego](Main_ManuelRego)                                                                                   | [Service to import data for personal timesheets](LibrePlan_AnA1204BoundUsersWebServices#TasK3)                  |                                                                                                                  |                                                                                                                    |                                                                                                                 |
