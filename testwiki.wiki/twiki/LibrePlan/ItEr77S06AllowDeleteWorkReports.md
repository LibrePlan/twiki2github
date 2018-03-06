[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S06AllowDeleteWorkReports](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports "Topic revision: 2 (27 Aug 2012 - 11:10:27)") (27 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S06AllowDeleteWorkReports?t=1520337945 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S06AllowDeleteWorkReports "Attach an image or document to this topic")

 [ItEr77S06AllowDeleteWorkReports](/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports)
===============================================================================================================================================



|                        |                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------|
| Story summary          | Allow Delete Work Reports From Web Services                                                  |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                               |
| FEA                    | [ItEr77S06AllowDeleteWorkReports](/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports) |
| Story Lead             |                                                                                              |
| Next Story             |                                                                                              |
| Passed acceptance test | No                                                                                           |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Implemented 2 new methods in `WorkReportServiceREST` to remove a work report or a work report line.

Configured properly Spring security to allow DELETE requests for `wswriter` user.

Added scripts to test the new methods:

-   `scripts/rest-clients/remove-work-report-line.sh`
-   `scripts/rest-clients/remove-work-report.sh`

Updated web services documentation.

-- [ManuelRego](/twiki/Main/ManuelRego) - 27 Aug 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S06AllowDeleteWorkReports?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                             | 5                                                                                                                                                              | 2.75                                                                                                                                                             | 0                                                                                                                                                                | Low                                                                                                                                                             | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                       | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                        | [Add delete operation for work reports and work report lines from web services](/twiki/LibrePlan/AnA12S02AllowDeleteWorkReports#TasK1)                      |                                                                                                                                                                       |                                                                                                                                                                         |                                                                                                                                                                      |


