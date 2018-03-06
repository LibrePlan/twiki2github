[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S17MoneyCostMonitoringSystem](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem "Topic revision: 13 (26 Nov 2012 - 12:18:33)") (26 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?t=1520337937 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S17MoneyCostMonitoringSystem "Attach an image or document to this topic")

 [ItEr76S17MoneyCostMonitoringSystem](/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem)
======================================================================================================================================================



|                        |                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------|
| Story summary          | Money Based Cost Monitoring System                                                                 |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                                     |
| FEA                    | [ItEr76S17MoneyCostMonitoringSystem](/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem) |
| Story Lead             |                                                                                                    |
| Next Story             |                                                                                                    |
| Passed acceptance test | No                                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

It was created a new remote branch in the repository to work in this story. This branch is called `money-cost-monitoring-system` and it was created from current stable branch.



####  Incorporate a field in the task to store the budget to represent the amount of money that the task is expected to cost

The new field `budget` will be in `OrderLine` level (i.e., only tasks will have a `budget` in the DB and the containers will calculate this value). The same behavior than for the hours field.

It was implemented a restriction because of a `budget` field cannot have negative values.

In order to make things simpler, this field was also added in templates. Because of, the code for WBS is shared for projects and templates, so having the field in both places make everything easier. Moreover, it's ok that templates have this new field too.

-- [ManuelRego](/twiki/Main/ManuelRego) - 14 Mar 2012



####  Graphic representation

Started to create the new **Money Cost Bar**. For the moment it's going to be painted a green bar very similar to the pink bar for the reported hours. The **Money Cost Bar** is painted over the reported hours bar.

With current pushed patches, both bars are showing/painting the same value.

Also a new percentage is shown in the tooltip text, that will be modified later.

The work has been centered in the graphical part and no new calculations have been done so far.

-- [ManuelRego](/twiki/Main/ManuelRego) - 16 Mar 2012

Created a new class called `MoneyCostCalculator` that maybe could be used in the future from other places. This class is used to calculate the cost of a task (that means, the associated OrderElement and all its children). It was created a basic test to check its behavior.

The new class has 2 methods:

-   `BigDecimal getMoneyCost(OrderElement orderElement)`: Calculates the cost of an OrderElement and all its children. It delegates in 2 methods:
    -   `org.libreplan.business.workreports.daos.IWorkReportLineDAO.findByOrderElementAndChildren(OrderElement, boolean)`: Which already existed
    -   `org.libreplan.business.costcategories.daos.IHourCostDAO.getPriceCostFromResourceDateAndType(Resource, LocalDate, TypeOfWorkHours)`: A new method to get the price from a resource, date and hours type.
-   `static BigDecimal getMoneyCostProportion(BigDecimal moneyCost, BigDecimal budget)`: An static utility method that simply divides the 2 BigDecimals received if the second one is different from zero. Otherwise, returns zero.

The information about the budget showed in the tooltip has been improved and now has the following format:

    Budget: 600 , Consumed: 150  (25%)

Changed the way how **Money Cost Bar** is printed, now the size is proportional to the size of the task as it was specified in the analysis. Two new methods were created in `IntraDayDate` (with their corresponding tests) and these new methods are used from `org.libreplan.web.planner.TaskElementAdapter.Adapter.TaskElementWrapper.calculateLimitDateProportionalToTaskElementSize(BigDecimal)`.

A new field called **Calculated budget** has been added in **General data** tab of projects. To show the total budget of the project calculated from the new `budget` attribute.

![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!") **NOTE**: It has been detected an special case in order to calculate the budget of a task. Maybe the resource is not associated to any cost category or the type of hour specified in the work report is not specified in any cost category of this resource. Then, the default price defined in the type of hours is used.

-- [ManuelRego](/twiki/Main/ManuelRego) - 19 Mar 2012

A new option to print **Money Cost Bar** has been added, allowing to print or not that bar.

-- [ManuelRego](/twiki/Main/ManuelRego) - 20 Mar 2012

Added a new unit tests to check `MoneyCostCalculator` is working properly with a tree of tasks and not only an individual task.

Now information about money cost is also shown in **Imputed hours** tab.

-- [ManuelRego](/twiki/Main/ManuelRego) - 21 Mar 2012

Added more unit tests to check `MoneyCostCalculator` behavior.

-- [ManuelRego](/twiki/Main/ManuelRego) - 23 Mar 2012

**Money Cost Bar** is not available in company view in order to avoid performance issues. Print the bar for a project implies to query all the work report lines associated to it.

On the other hand, `MoneyCostCalculator` has been enhanced adding a map to cache the calculated cost of an element. This avoids do any extra recalculation when the money cost of an element is requested. And now, `MoneyCostCalculator` map is reset every time you enter in a project.

-- [ManuelRego](/twiki/Main/ManuelRego) - 26 Mar 2012

Changed color of **Money Cost Bar** for a darker one (in order to avoid possible issues for people with visual disabilities).

Added `budget` information on a read-only field inside task properties tab.

Merged remote branch into `master` and `libreplan-1.2` so this feature will be included in the next LibrePlan releases.

-- [ManuelRego](/twiki/Main/ManuelRego) - 27 Mar 2012

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

-   Review what to do with current field called **Budget** inside the tab **General data** in project edition. For the moment a new field called **Calculated budget** has been added with the information of the new attribute created in this task.

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                     | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S17MoneyCostMonitoringSystem?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                | 5                                                                                                                                                                 | 5                                                                                                                                                                   | 0                                                                                                                                                                   | Low                                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                        | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                           | [Incorporate a field in the task to store the budget to represent the amount of money that the task is expected to cost](/twiki/LibrePlan/AnA19S01MoneyCostMonitoringSystem#TasK1) |                                                                                                                                                                          |                                                                                                                                                                            |                                                                                                                                                                         |
| Task                                                                                                                                                                | 16                                                                                                                                                                | 16                                                                                                                                                                  | 0                                                                                                                                                                   | Low                                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                        | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                           | [Graphic representation](/twiki/LibrePlan/AnA19S01MoneyCostMonitoringSystem#TasK2)                                                                                                 |                                                                                                                                                                          |                                                                                                                                                                            |                                                                                                                                                                         |

------------------------------------------------------------------------
