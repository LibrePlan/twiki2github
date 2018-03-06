[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr62S03RFPerformanceCompanyView](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView "Topic revision: 5 (19 Oct 2010 - 10:07:59)") (19 Oct 2010, [JacoboAragunde](/twiki/Main/JacoboAragunde))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr62S03RFPerformanceCompanyView?t=1520337877 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr62S03RFPerformanceCompanyView "Attach an image or document to this topic")

 [ItEr62S03RFPerformanceCompanyView](/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Performance company view                                                                         |
| Iteration              | [ItEr62week41To43](/twiki/LibrePlan/ItEr62week41To43)                                   |
| FEA                    | [ItEr62S03RFPerformanceCompanyView](/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Finally, snapshots for both charts (resource load and earned value) were implemented. The reason is that both needed related data, so after implementing the snapshot for load chart, there wasn't a noticeable improvement because data were loaded to calculate the earned value chart anyway.

Once finished the implementation, the time spent displaying the chart decreased from 9.9 s to 135 ms, which is an amazing improvement ![smile](/twiki/TWiki/SmiliesPlugin/smile.gif "smile") .

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 15 Oct 2010

I spent some extra time rebasing the patches, since there were some deep changes in the application which conflicted with mine.

-- [JacoboAragunde](/twiki/Main/JacoboAragunde) - 19 Oct 2010

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 14                                                                                                                                                               | 24.75                                                                                                                                                              | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                       | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                  | [Snapshot to calculate the load chart in company view](/twiki/LibrePlan/AnA03RFPerformanceCompanyView#TasK2)                                                  |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S03RFPerformanceCompanyView?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                             | 24.75                                                                                                                                                                           | 0                                                                                                                                                                               | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                |
| Total                                                                                                                                                             | 24.75                                                                                                                                                                           | 0                                                                                                                                                                               | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                |

------------------------------------------------------------------------
