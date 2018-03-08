[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA05S09RefactoringWorkReportWS](LibrePlan_AnA05S09RefactoringWorkReportWS "Topic revision: 6 (03 Jan 2012 - 15:17:22)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA05S09RefactoringWorkReportWS?t=1520344038 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA05S09RefactoringWorkReportWS "Attach an image or document to this topic")  

 [AnA05S09RefactoringWorkReportWS](LibrePlan_AnA05S09RefactoringWorkReportWS)
=============================================================================

|                        |                                                                              |
|------------------------|------------------------------------------------------------------------------|
| Story summary          | Refactoring Work Report WS                                                   |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)                             |
| FEA                    | [AnA05S09RefactoringWorkReportWS](LibrePlan_AnA05S09RefactoringWorkReportWS) |
| Story Lead             |                                                                              |
| Next Story             |                                                                              |
| Passed acceptance test | No                                                                           |

###  Tasks

####  Abstract strategy to associate order element

This task consists of modifying the work report service to allow to look for the set of OrderElement associated with a WorkReportLine.

First it will be created a new interface called `IWorkReportsElements` that is going to be implemented by `WorkReport` and `WorkReportLine`. This interface will have the following methods:

       * Date getDate & setDate
       * Resource getResource & setResource
       * OrderElement getOrderElement & setOrderElement
       * Set<Label> getLabels & setLabels
       * Set<DescriptionValue> getDescriptionValues & setDescriptionValues

We're going to create a new interface called `IWorkReportDTOsElements` with the same methods than before but returning different values:

       * XMLGregorianCalendar getDate & setDate
       * String getResource & setResource
       * String getOrderElement & setOrderElement
       * Set<LabelReferenceDTO> getLabels & setLabels
       * Set<DescriptionValueDTO> getDescriptionValues & setDescriptionValues

Then it will be created an interface called `IBindingOrderElementStrategy` with these methods:

       * List<OrderElement> getOrderElementsBound(IWorkReportDTOsElements workReportDTO) throws ValidationException;
       * String getOrderElementCodesBound(IWorkReportsElements workReportEntity);
       * void assignOrderElementsToWorkReportLine(IWorkReportsElements workReportEntity, List<OrderElement> list) throws ValidationException;

It will be developed a default implementation (example name `OneOrderElementPerWorkReportLine`) with the following features:

-   It will look for the orderelement using the ***code*** (![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!") *externalCode* is only used in subcontracting system) of the work report line related to the order line.
-   The method `assignOrderElementsToWorkReportLine` will throw a ValidationException if the list is empty or if it has more than 1 element.

It is needed to modify the converter `org.navalplanner.ws.workreports.impl.WorkReportConverter` in four places because the OrderElement specification can come probably both in the WorkReport heading and in the WorkReportLine.

![warning](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif) Use this specification as a guide and feel free to design at implementation level. Use this

###  User stories

-   [ItEr75S20RefactoringWorkReportWS](LibrePlan_ItEr75S20RefactoringWorkReportWS)

###  Tasks in this story

| [Tasks](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                         | 3                                                                                                          | 3                                                                                                            | 0                                                                                                            | Low                                                                                                         | [JavierMoran](Main_JavierMoran)                                                                                 | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                        | [Abstract strategy to associate order element](LibrePlan_AnA05S09RefactoringWorkReportWS#TasK1)                  |                                                                                                                   |                                                                                                                     |                                                                                                                  |

###  Total Hours in this Story

| [User](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA05S09RefactoringWorkReportWS?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | 3                                                                                                                         | 0                                                                                                                         | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                          |
| Total                                                                                                       | 3                                                                                                                         | 0                                                                                                                         | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                          |

------------------------------------------------------------------------
