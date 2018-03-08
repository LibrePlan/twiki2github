[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S20RefactoringWorkReportWS](LibrePlan_ItEr75S20RefactoringWorkReportWS "Topic revision: 5 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_ItEr75S20RefactoringWorkReportWS?t=1520343683 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S20RefactoringWorkReportWS "Attach an image or document to this topic")  

 [ItEr75S20RefactoringWorkReportWS](LibrePlan_ItEr75S20RefactoringWorkReportWS)
===============================================================================

|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Refactoring Work Report Web Service                                            |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                                 |
| FEA                    | [ItEr75S20RefactoringWorkReportWS](LibrePlan_ItEr75S20RefactoringWorkReportWS) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

At the end the implementation is made with an interface IBindingOrderElementStrategy[?](LibrePlan_IBindingOrderElementStrategy?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") , that must be implementated with some strategy.

At this time there is an Strategy that allows only one OrderElement[?](LibrePlan_OrderElement?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") for each WorkReportLine[?](LibrePlan_WorkReportLine?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") .

Now, both WorkReport[?](LibrePlan_WorkReport?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") and WorkReportLine[?](LibrePlan_WorkReportLine?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") implement an interface called IWorkReportsElements[?](LibrePlan_IWorkReportsElements?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") -also this was made for their corresponding DTOs-, with this, the strategy uses IWorkReportsElements[?](LibrePlan_IWorkReportsElements?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") and could serve for both kind of objects.

-- [IgnacioDiaz](Main_IgnacioDiaz) - 02 Sep 2011

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

| [Tasks](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                          | 3                                                                                                           | 9                                                                                                             | 0                                                                                                             | Low                                                                                                          | [JavierMoran](Main_JavierMoran)                                                                                  | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                         | [Abstract strategy to associate order element](LibrePlan_AnA05S09RefactoringWorkReportWS#TasK1)                   | 31/08/2011                                                                                                         | 01/09/2011                                                                                                           | 02/09/2011                                                                                                        |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S20RefactoringWorkReportWS?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                    | 9                                                                                                                          | 0                                                                                                                          | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                           |
| Total                                                                                                        | 9                                                                                                                          | 0                                                                                                                          | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                           |

------------------------------------------------------------------------
