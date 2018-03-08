[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S22WortReportsEffortDuration](LibrePlan_ItEr75S22WortReportsEffortDuration "Topic revision: 7 (03 Jan 2012 - 17:35:13)") (03 Jan 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr75S22WortReportsEffortDuration?t=1520343683 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S22WortReportsEffortDuration "Attach an image or document to this topic")  

 [ItEr75S22WortReportsEffortDuration](LibrePlan_ItEr75S22WortReportsEffortDuration)
===================================================================================

|                        |                                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| Story summary          | Introduce Effort Duration in Work Reports                                          |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                                     |
| FEA                    | [ItEr75S22WortReportsEffortDuration](LibrePlan_ItEr75S22WortReportsEffortDuration) |
| Story Lead             |                                                                                    |
| Next Story             |                                                                                    |
| Passed acceptance test | No                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Uploaded a patch with some TODOs. These TODOs refers to some calculations made rounding to hours instead of using minutes. It's better to review this first patch before going on with the new calculations minute-based.

-- [IgnacioDiaz](Main_IgnacioDiaz) - 19 Aug 2011

Created a remote branch for this task called `work-reports-effort-duration`

Split patch by Nacho Díaz in some small patches:

-   Change to effort in WorkReportLine. Keeping methods `getNumHours() and setNumHours()`
-   Change UI to use EffortDurationPicker in work reports

-- [ManuelRego](Main_ManuelRego) - 31 Aug 2011

ManuelRego[?](LibrePlan_ManuelRego?topicparent=LibrePlan.ItEr75S22WortReportsEffortDuration "Create this topic") merged the branch in master.

Maybe we could improve this implementation with the things told in this link: <http://sourceforge.net/mailarchive/message.php?msg_id=28060493>

-- [IgnacioDiaz](Main_IgnacioDiaz) - 12 Sep 2011

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

| [Tasks](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=7;table=2;up=0#sorted_table "Sort by this column")   | [Start Date](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                            | 20                                                                                                            | 49                                                                                                              | 0                                                                                                               | Low                                                                                                            | [JavierMoran](Main_JavierMoran)                                                                                    | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                     | [Modify the field numHours in WorkReportLine to be EffortDuration](LibrePlan_AnA05S10WortReportsEffortDuration#TasK1) | 09/08/2011                                                                                                           |                                                                                                                        | 09/09/2011                                                                                                          |
| Task                                                                                                            | 20                                                                                                            | 2.25                                                                                                            | 0                                                                                                               | Low                                                                                                            | [JavierMoran](Main_JavierMoran)                                                                                    | [ManuelRego](Main_ManuelRego)                                                                                       | [Modify the field numHours in WorkReportLine to be EffortDuration](LibrePlan_AnA05S10WortReportsEffortDuration#TasK1) |                                                                                                                      |                                                                                                                        |                                                                                                                     |
| Task                                                                                                            | 20                                                                                                            | 0.5                                                                                                             | 0                                                                                                               | Low                                                                                                            | [JavierMoran](Main_JavierMoran)                                                                                    | [IgnacioDiaz](Main_IgnacioDiaz)                                                                                     | [Create Liquibase configuration to migrate data](LibrePlan_AnA05S10WortReportsEffortDuration#TasK2)                   | 09/08/2011                                                                                                           |                                                                                                                        | 09/09/2011                                                                                                          |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S22WortReportsEffortDuration?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz)                                                                                | 49.5                                                                                                                         | 0                                                                                                                            | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                             |
| [ManuelRego](Main_ManuelRego)                                                                                  | 2.25                                                                                                                         | 0                                                                                                                            | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                             |
| Total                                                                                                          | 51.75                                                                                                                        | 0                                                                                                                            | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                             |

------------------------------------------------------------------------
