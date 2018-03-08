[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr77S15FilteringEnhancements](LibrePlan_ItEr77S15FilteringEnhancements "Topic revision: 12 (28 Mar 2013 - 09:05:48)") (28 Mar 2013, [LorenzoTilve](Main_LorenzoTilve))[Edit](LibrePlan_ItEr77S15FilteringEnhancements?t=1520343707 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S15FilteringEnhancements "Attach an image or document to this topic")  

 [ItEr77S15FilteringEnhancements](LibrePlan_ItEr77S15FilteringEnhancements)
===========================================================================

|                        |                                                                            |
|------------------------|----------------------------------------------------------------------------|
| Story summary          | Filtering enhancements                                                     |
| Iteration              | [ItEr77Week34To44](LibrePlan_ItEr77Week34To44)                             |
| FEA                    | [ItEr77S15FilteringEnhancements](LibrePlan_ItEr77S15FilteringEnhancements) |
| Story Lead             |                                                                            |
| Next Story             |                                                                            |
| Passed acceptance test | No                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

There have been issues detected on the ResourcesLoad component <http://bugs.libreplan.org/show_bug.cgi?id=1607>

-- [LorenzoTilve](Main_LorenzoTilve) - 29 Jan 2013

The filter behaviour on the projects list view was experimenting some problems. First, it was only considering project deadline dates, and has also issues when using both start and end date filter dates. Both problems should not be happening any longer once the new database direct query would be filtering taking into consideration all the variables.

-- [LorenzoTilve](Main_LorenzoTilve) - 30 Jan 2013

The MultipleSearchBandboxComponent used to specify labels or criteria, is not doing an explicit notification of the ON\_CHANGE event once the value it has is removed, nor are external listeners attached to the listbox. It's needed to press manually fhe filter button or selecting the 'empty' listbox element to reapply the filter.

-- [LorenzoTilve](Main_LorenzoTilve) - 31 Jan 2013

There is still some issue happening with the company date filtering settings, which are being cleared after changes on the label combo.

-- [LorenzoTilve](Main_LorenzoTilve) - 01 Feb 2013

It's also necessary to trigger somehow the event that forces a filter reload to apply the modified parameters when changing between projects view and projects list, as their doAfterCompose() it's only called once.

-- [LorenzoTilve](Main_LorenzoTilve) - 01 Feb 2013

Implemented database query to filter projects and used it from projects list.

-- [ManuelRego](Main_ManuelRego) - 04 Feb 2013

The database query has been improved, in order to include the unscheduled projects too (basically the projects coming from the web services).

On the other hand the query has been used too from the company Gantt view.

-- [ManuelRego](Main_ManuelRego) - 05 Feb 2013

Stored zoom in session for company Gantt view and each project Gantt view.

-- [ManuelRego](Main_ManuelRego) - 06 Feb 2013

Finished to store zoom in session.

There'll be 3 zoom variables stored in session:

-   `zoomLevelCompanyView`: Used for Gantt company view
-   `zoomLevelResourcesLoad`: Used for resources load company view
-   `<project-code>-zoomLevel`: 1 variable per project, the same zoom is shared in all the views inside project edition (Gantt, resources load and advanced allocation)

-- [ManuelRego](Main_ManuelRego) - 07 Feb 2013

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                                         | [Start Date](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr77S15FilteringEnhancements?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Task                                                                                                        | 4                                                                                                         | 6                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [Adding configuration parameters in user preferences for projects planning and projects list perspective](LibrePlan_AnAS21FilteringEnhancements#TasK1)  |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 5                                                                                                         | 8                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [Including per user filtering in projects planning and project lists perspective](LibrePlan_AnAS21FilteringEnhancements#TasK2)                          |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 0                                                                                                         | 14.5                                                                                                        | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [ManuelRego](Main_ManuelRego)                                                                                   | [Including per user filtering in projects planning and project lists perspective](LibrePlan_AnAS21FilteringEnhancements#TasK2)                          |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 7                                                                                                         | 6                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [User session store of the last value of the filters used in the projects planning and projects list view](LibrePlan_AnAS21FilteringEnhancements#TasK3) |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 0                                                                                                         | 4                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [ManuelRego](Main_ManuelRego)                                                                                   | [User session store of the last value of the filters used in the projects planning and projects list view](LibrePlan_AnAS21FilteringEnhancements#TasK3) |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 4                                                                                                         | 4                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [Adding configuration parameters for filters in user preferences for resource load window](LibrePlan_AnAS21FilteringEnhancements#TasK4)                 |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 5                                                                                                         | 6                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [Incluing the per user filtering in the resource load view](LibrePlan_AnAS21FilteringEnhancements#TasK5)                                                |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 4                                                                                                         | 2                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [User session store of the last value of the filters used in resources load view](LibrePlan_AnAS21FilteringEnhancements#TasK6)                          |                                                                                                                  |                                                                                                                    |                                                                                                                 |
| Task                                                                                                        | 7                                                                                                         | 5                                                                                                           | 0                                                                                                           | Low                                                                                                        | [JavierMoran](Main_JavierMoran)                                                                                | [LorenzoTilve](Main_LorenzoTilve)                                                                               | [Memory mechansim for filters used in the project planning](LibrePlan_AnAS21FilteringEnhancements#TasK7)                                                |                                                                                                                  |                                                                                                                    |                                                                                                                 |
