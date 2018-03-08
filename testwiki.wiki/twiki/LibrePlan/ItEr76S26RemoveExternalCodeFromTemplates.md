[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr76S26RemoveExternalCodeFromTemplates](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates "Topic revision: 6 (20 Aug 2012 - 09:50:19)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?t=1520343699 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates "Attach an image or document to this topic")  

 [ItEr76S26RemoveExternalCodeFromTemplates](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates)
===============================================================================================

|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Remove external code from templates                                                            |
| Iteration              | [ItEr76Week01To33](LibrePlan_ItEr76Week01To33)                                                 |
| FEA                    | [ItEr76S26RemoveExternalCodeFromTemplates](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

The task has a bit more of of work than expected, because there is a problem in the model: the class *OrderElement* receives the *code* element from two classes: its parent class *IntegrationEntity* and the related class *InfoComponent*. See diagram:

![ItEr76S26RemoveExternalCodeFromTemplates.png](/twiki/pub/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates/ItEr76S26RemoveExternalCodeFromTemplates.png)

My solution will be removing the *code* attribute from *InfoComponent* class. It requires some changes in the *hbm* definitions of the involved classes.

-- [JacoboAragunde](Main_JacoboAragunde) - 28 Apr 2012

It looks like the solution proposed above is invalid. The *code* attribute is part of *InfoComponent* class for a good reason: it's needed in the copy mechanism, happening when elements in the WBS are indented, and also when templates are created from *OrderElement* objects. The second case is not important any more, but the first one is.

The solution proposed now is leaving *OrderElement* class as it is, and just ignore the code attribute in *OrderElementTemplate*. It will be part of the object but it won't appear in the interface nor will be saved to the DB.

-- [JacoboAragunde](Main_JacoboAragunde) - 28 Apr 2012 (later)

After I had taken over other tasks, I found a regression related to this. You cannot edit and save an existing template containing some tasks. The message says "code not specified".

Why is this happening? Because, before saving, `LibrePlanClassValidator` checks every field with annotations for every object being saved, and in the case of `OrderElementTemplates`, `InfoComponent.getCode()` still exists and has a `@NotEmpty` annotation. Some more work on this topic is needed...

-- [JacoboAragunde](Main_JacoboAragunde) - 02 May 2012

Proposed implementation of the solution:

![ItEr76S26RemoveExternalCodeFromTemplates-solution.png](/twiki/pub/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates/ItEr76S26RemoveExternalCodeFromTemplates-solution.png)

-- [JacoboAragunde](Main_JacoboAragunde) - 03 May 2012

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

Task completed. TODO: template finders still have a 'code' column (the finder is reused for *OrderElements too*) (see commit 47ccb4d2576512bfb392520b84828312d577a842). We have to remove that column, maybe refactoring the code of the finder.

-- [JacoboAragunde](Main_JacoboAragunde) - 28 Apr 2012

Fixed regression using the solution exposed in the class diagram above.

-- [JacoboAragunde](Main_JacoboAragunde) - 03 May 2012

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                  | 3                                                                                                                   | 4                                                                                                                     | 0                                                                                                                     | Low                                                                                                                  | [ManuelRego](Main_ManuelRego)                                                                                            | [JacoboAragunde](Main_JacoboAragunde)                                                                                     | [Remove the code attribute from templates (interface and entity)](LibrePlan_AnAS20RemoveExternalCodeFromTemplates#TasK1)  |                                                                                                                            |                                                                                                                              |                                                                                                                           |

###  Total Hours in this Story

| [User](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [JacoboAragunde](Main_JacoboAragunde)                                                                                | 4                                                                                                                                  | 0                                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                   |
| Total                                                                                                                | 4                                                                                                                                  | 0                                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                   |

------------------------------------------------------------------------

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates#)

| [I](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=1;table=4;up=0#sorted_table "Sort by this column")                                                   | [Action](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=2;table=4;up=0#sorted_table "Sort by this column")                                                                                        |  [Size](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=3;table=4;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=4;table=4;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=5;table=4;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_ItEr76S26RemoveExternalCodeFromTemplates?sortcol=6;table=4;up=0#sorted_table "Sort by this column") |
|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
|                                ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                               | [ItEr76S26RemoveExternalCodeFromTemplates-solution.png](/twiki/pub/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates/ItEr76S26RemoveExternalCodeFromTemplates-solution.png) | [manage](/twiki/bin/attach/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates?filename=ItEr76S26RemoveExternalCodeFromTemplates-solution.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                                                15.4 K| 03 May 2012 - 08:11                                                                                                  | [JacoboAragunde](Main_JacoboAragunde)                                                                               | Diagram with involved classes and proposed solution (png).                                                              |
|                               ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)dia                              | [ItEr76S26RemoveExternalCodeFromTemplates.dia](/twiki/pub/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates/ItEr76S26RemoveExternalCodeFromTemplates.dia)                   | [manage](/twiki/bin/attach/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates?filename=ItEr76S26RemoveExternalCodeFromTemplates.dia;revInfo=1 "change, update, previous revisions, move, delete...")          |                                                                                                                 2.2 K| 03 May 2012 - 08:10                                                                                                  | [JacoboAragunde](Main_JacoboAragunde)                                                                               | Diagram with involved classes and proposed solution                                                                     |
|                                ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                               | [ItEr76S26RemoveExternalCodeFromTemplates.png](/twiki/pub/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates/ItEr76S26RemoveExternalCodeFromTemplates.png)                   | [manage](/twiki/bin/attach/LibrePlan/ItEr76S26RemoveExternalCodeFromTemplates?filename=ItEr76S26RemoveExternalCodeFromTemplates.png;revInfo=1 "change, update, previous revisions, move, delete...")          |                                                                                                                12.6 K| 28 Apr 2012 - 10:40                                                                                                  | [JacoboAragunde](Main_JacoboAragunde)                                                                               | Diagram with involved classes (png).                                                                                    |
