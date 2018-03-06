[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S20RefactoringWorkReportWS](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS "Topic revision: 5 (03 Jan 2012 - 13:16:57)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S20RefactoringWorkReportWS?t=1520337925 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S20RefactoringWorkReportWS "Attach an image or document to this topic")

 [ItEr75S20RefactoringWorkReportWS](/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Refactoring Work Report Web Service                                                            |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)                                 |
| FEA                    | [ItEr75S20RefactoringWorkReportWS](/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

At the end the implementation is made with an interface IBindingOrderElementStrategy[?](/twiki/bin/edit/LibrePlan/IBindingOrderElementStrategy?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") , that must be implementated with some strategy.

At this time there is an Strategy that allows only one OrderElement[?](/twiki/bin/edit/LibrePlan/OrderElement?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") for each WorkReportLine[?](/twiki/bin/edit/LibrePlan/WorkReportLine?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") .

Now, both WorkReport[?](/twiki/bin/edit/LibrePlan/WorkReport?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") and WorkReportLine[?](/twiki/bin/edit/LibrePlan/WorkReportLine?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") implement an interface called IWorkReportsElements[?](/twiki/bin/edit/LibrePlan/IWorkReportsElements?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") -also this was made for their corresponding DTOs-, with this, the strategy uses IWorkReportsElements[?](/twiki/bin/edit/LibrePlan/IWorkReportsElements?topicparent=LibrePlan.ItEr75S20RefactoringWorkReportWS "Create this topic") and could serve for both kind of objects.

-- [IgnacioDiaz](/twiki/Main/IgnacioDiaz) - 02 Sep 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 3                                                                                                                                                               | 9                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [IgnacioDiaz](/twiki/Main/IgnacioDiaz) [CristinaAlvarino](/twiki/Main/CristinaAlvarino)                                                             | [Abstract strategy to associate order element](/twiki/LibrePlan/AnA05S09RefactoringWorkReportWS#TasK1)                                                       | 31/08/2011                                                                                                                                                             | 01/09/2011                                                                                                                                                               | 02/09/2011                                                                                                                                                            |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S20RefactoringWorkReportWS?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](/twiki/Main/IgnacioDiaz) [CristinaAlvarino](/twiki/Main/CristinaAlvarino)                                                        | 9                                                                                                                                                                              | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |
| Total                                                                                                                                                            | 9                                                                                                                                                                              | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |

------------------------------------------------------------------------
