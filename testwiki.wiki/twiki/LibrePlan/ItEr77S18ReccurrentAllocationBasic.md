[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S18ReccurrentAllocationBasic](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic "Topic revision: 4 (12 Jul 2013 - 17:04:08)") (12 Jul 2013, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S18ReccurrentAllocationBasic?t=1520337949 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S18ReccurrentAllocationBasic "Attach an image or document to this topic")

 [ItEr77S18ReccurrentAllocationBasic](/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic)
======================================================================================================================================================



|                        |                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------|
| Story summary          | Recurrent Allocation Basic                                                                         |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                                     |
| FEA                    | [ItEr77S18ReccurrentAllocationBasic](/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic) |
| Story Lead             |                                                                                                    |
| Next Story             |                                                                                                    |
| Passed acceptance test | No                                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

####  Data model to store the recurrent information

-- [JavierMoran](/twiki/Main/JavierMoran) - 28 Jun 2013

I start by saving the peridiocity. I use an enum type in Hibernate and will be incorporated in the class `Task` in the existent component called `recurrenceInformation`.

It was tried to create an internal class enum but the Hibernate framework was not able to locate it. Therefore, it was refactorized to an external class `org.libreplan.business.recurring.RecurrencePeriodicity`.

It was also added the Liquibase information to create the new database column. ![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) It was added a default value of 0 that has to validated as correct as default value for the `recurrencePeriodicity` column.

Next thing to start is to visualize and save the recurring information.

####  Save basic data for recurrent allocation

-- [JavierMoran](/twiki/Main/JavierMoran) - 12 Jul 2013

I browsed through the code to know where the introduction of the new behavior can be inserted. Notes of the code browsing:

-   `ResultAllocationModel`.
    -   It is invoked `accept()` to apply the resource allocations over the PlanningState
    -   It uses the class `AllocationRowsHandler` to do the allocations and it returns a `AllocationResult`.
    -   The `AllocationResult` is applied to the `PlanningState` and to the task of the `ResourceAllocationModel`

**Delay Causes**

**Final or Pending Considerations**

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S18ReccurrentAllocationBasic?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                | 100                                                                                                                                                               | 0                                                                                                                                                                   | 100                                                                                                                                                                 | Low                                                                                                                                                                |                                                                                                                                                                        | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                         | [Data model to store the recurrent information](/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic#TasK1)                                                      |                                                                                                                                                                          |                                                                                                                                                                            |                                                                                                                                                                         |
| Task                                                                                                                                                                | 100                                                                                                                                                               | 0                                                                                                                                                                   | 100                                                                                                                                                                 | Low                                                                                                                                                                |                                                                                                                                                                        | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                         | [Save basic data for recurrent allocation](/twiki/LibrePlan/AnA09S12ReccurrentAllocationBasic#TasK2)                                                           |                                                                                                                                                                          |                                                                                                                                                                            |                                                                                                                                                                         |


