[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr77S17AutomaticBudgeting](LibrePlan_ItEr77S17AutomaticBudgeting "Topic revision: 4 (07 Jun 2013 - 11:11:49)") (07 Jun 2013, [LorenzoTilve](Main_LorenzoTilve))[Edit](LibrePlan_ItEr77S17AutomaticBudgeting?t=1520343707 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S17AutomaticBudgeting "Attach an image or document to this topic")  

 [ItEr77S17AutomaticBudgeting](LibrePlan_ItEr77S17AutomaticBudgeting)
=====================================================================

|                        |                                                                             |
|------------------------|-----------------------------------------------------------------------------|
| Story summary          | Automatic budgeting based on task criteria requirement and hour estimations |
| Iteration              | [ItEr77Week34To44](LibrePlan_ItEr77Week34To44)                              |
| FEA                    | [ItEr77S17AutomaticBudgeting](LibrePlan_ItEr77S17AutomaticBudgeting)        |
| Story Lead             |                                                                             |
| Next Story             |                                                                             |
| Passed acceptance test | No                                                                          |

**Acceptance Criteria**

-   [AnA22S01AutomaticBudgeting](LibrePlan_AnA22S01AutomaticBudgeting)
    -   Implementation a link between criteria and cost categories.
    -   Configuration of the standard type of hours for the budget calculation.
    -   Creation of a new column of calculated budget per task on the WBS
    -   Inclusion of the project status of this new column

**Additional Specification Comments**

**Implementation Notes**

On top of the previously identified tasks, it's necessary to modify the gantt view in order that the methods that use the bueget now use the new calculated method, instead of the manual one. The same thing for the project details general data perspective, and the cost tab on the orderElement popup.

-- [LorenzoTilve](Main_LorenzoTilve) - 07 Jun 2013

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

| [Tasks](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr77S17AutomaticBudgeting?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Task                                                                                                     | 0                                                                                                      | 0                                                                                                        | 0                                                                                                        | Low                                                                                                     | [LorenzoTilve](Main_LorenzoTilve)                                                                           | [LorenzoTilve](Main_LorenzoTilve)                                                                            | Implementation                                                                                               |                                                                                                               |                                                                                                                 |                                                                                                              |
