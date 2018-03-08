[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr62S03RFPerformanceCompanyView](LibrePlan_ItEr62S03RFPerformanceCompanyView "Topic revision: 5 (19 Oct 2010 - 10:07:59)") (19 Oct 2010, [JacoboAragunde](Main_JacoboAragunde))[Edit](LibrePlan_ItEr62S03RFPerformanceCompanyView?t=1520343632 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr62S03RFPerformanceCompanyView "Attach an image or document to this topic")  

 [ItEr62S03RFPerformanceCompanyView](LibrePlan_ItEr62S03RFPerformanceCompanyView)
=================================================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Performance company view                                                         |
| Iteration              | [ItEr62week41To43](LibrePlan_ItEr62week41To43)                                   |
| FEA                    | [ItEr62S03RFPerformanceCompanyView](LibrePlan_ItEr62S03RFPerformanceCompanyView) |
| Story Lead             |                                                                                  |
| Next Story             |                                                                                  |
| Passed acceptance test | No                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Finally, snapshots for both charts (resource load and earned value) were implemented. The reason is that both needed related data, so after implementing the snapshot for load chart, there wasn't a noticeable improvement because data were loaded to calculate the earned value chart anyway.

Once finished the implementation, the time spent displaying the chart decreased from 9.9 s to 135 ms, which is an amazing improvement ![smile](/twiki/pub/TWiki/SmiliesPlugin/smile.gif "smile") .

-- [JacoboAragunde](Main_JacoboAragunde) - 15 Oct 2010

I spent some extra time rebasing the patches, since there were some deep changes in the application which conflicted with mine.

-- [JacoboAragunde](Main_JacoboAragunde) - 19 Oct 2010

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

| [Tasks](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                           | 14                                                                                                           | 24.75                                                                                                          | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [JacoboAragunde](Main_JacoboAragunde)                                                                              | [Snapshot to calculate the load chart in company view](LibrePlan_AnA03RFPerformanceCompanyView#TasK2)              |                                                                                                                     |                                                                                                                       |                                                                                                                    |

###  Total Hours in this Story

| [User](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr62S03RFPerformanceCompanyView?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [JacoboAragunde](Main_JacoboAragunde)                                                                         | 24.75                                                                                                                       | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |
| Total                                                                                                         | 24.75                                                                                                                       | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |

------------------------------------------------------------------------
