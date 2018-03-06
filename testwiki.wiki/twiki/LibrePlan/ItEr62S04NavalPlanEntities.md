[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr62S04NavalPlanEntities](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities "Topic revision: 7 (20 Aug 2012 - 09:52:48)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr62S04NavalPlanEntities?t=1520337878 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr62S04NavalPlanEntities "Attach an image or document to this topic")

 [ItEr62S04NavalPlanEntities](/twiki/LibrePlan/ItEr62S04NavalPlanEntities)
================================================================================================================================



|                        |                                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| Story summary          | Code generation for LibrePlan entities                                             |
| Iteration              | [ItEr62week41To43](/twiki/LibrePlan/ItEr62week41To43)                     |
| FEA                    | [ItEr62S04NavalPlanEntities](/twiki/LibrePlan/ItEr62S04NavalPlanEntities) |
| Story Lead             |                                                                                    |
| Next Story             |                                                                                    |
| Passed acceptance test | No                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

###  It was performed the followings tasks:

It was added the default separator to generate the code sequences of the child entities.

It was added a new functionality to EntitySequenceDAO to skip repeated code sequences.If code sequence is added by importation services , this functionality lets skip repeated codes and update the last value of the entity code sequence.

It was added the Spanish and Galician translations for the labels on the configuration interface.

It was replaced the generated code by the code sequence for each of the following entities.

-   Type of work hours.
-   Material category.
-   Base calendars.
-   Work Report and its work report lines.
-   Resource calendars.
-   Calendar Exception
-   Calendar Data
-   Calendar Availability.

It was changed the configuration interface. It was deleted the border of each grid of the sequences code. It was added a ToolTipText on the code sequence row.This message informing that it can not be modified if the code sequence is being used. Also it was added a message informing on deleting sequences. If the sequence is the last one then it is shown a message informing that it can not be deleted because at least one sequence is necessary

It was added the IntegrationEntityModel to auto-generated code management.This class generalizes the methods for managing the auto-generated codes and so reuse them on each model.

Replacing the generated code by the code sequence for each of the following entities .

-   WorkReportType
-   Material
-   HoursGroup
-   CalendarExceptionType
-   CostCategory
-   HourCost

The code of the following entities always is generated:

-   ResourcesCostCategoryAssignment
-   CriterionSatisfaction
-   ResourceCalendar

Changing the service of the resources to check if the resource calendar, the criterion satisfactions or the assignment of resource cost category have not code, so this one is generated. Including of the Spanish and Galician translations for the labels on the modified models and the controllers . It has not deleted the method generateCode of the IntegrationEntity class.

-- [SusanaMontes](/twiki/Main/SusanaMontes) - 20 Oct 2010

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

It should be adding the Work report type service.

-- [SusanaMontes](/twiki/Main/SusanaMontes) - 28 Oct 2010

It should be reload the configuration before saving , because it can throw a version error.

-- [SusanaMontes](/twiki/Main/SusanaMontes) - 28 Oct 2010

|     |     |
|-----|-----|
|     |     |

###  Entregables de código

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                        | 10                                                                                                                                                        | 48                                                                                                                                                          | 0                                                                                                                                                           | Low                                                                                                                                                        | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                               | [LibrePlan configuration for generated entity codes](/twiki/LibrePlan/AnA04S01NavalPlanEntities#TasK1)                                                 |                                                                                                                                                                  |                                                                                                                                                                    |                                                                                                                                                                 |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr62S04NavalPlanEntities?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                          | 48                                                                                                                                                                       | 0                                                                                                                                                                        | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                         |
| Total                                                                                                                                                      | 48                                                                                                                                                                       | 0                                                                                                                                                                        | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                         |

------------------------------------------------------------------------
