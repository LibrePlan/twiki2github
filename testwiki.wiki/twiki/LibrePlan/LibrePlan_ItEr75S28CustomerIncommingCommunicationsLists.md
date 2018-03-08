[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S28CustomerIncommingCommunicationsLists](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists "Topic revision: 8 (20 Aug 2012 - 09:52:54)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?t=1520343686 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S28CustomerIncommingCommunicationsLists "Attach an image or document to this topic")  

 [ItEr75S28CustomerIncommingCommunicationsLists](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists)
=========================================================================================================

|                        |                                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------------|
| Story summary          | Customer incomming communication lists                                                                   |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                                                           |
| FEA                    | [ItEr75S28CustomerIncommingCommunicationsLists](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists) |
| Story Lead             |                                                                                                          |
| Next Story             |                                                                                                          |
| Passed acceptance test | No                                                                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Add the external code when a whole order is imported as subcontrated task:

    order.setExternalCode(order.getCode)

although this operation is not permit by interfaz this one give us clarity on the code. All subcontrated task have filled the external code.

Also it is added the relationship from order entity (one-to-many) with its customer comunications in order to delete all the comunications if the associated order is removed.

-- [SusanaMontes](Main_SusanaMontes) - 03 Nov 2011

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

Update the commits to libreplan.

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                           | [Start Date](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                       | 7                                                                                                                        | 10                                                                                                                         | 0                                                                                                                          | Low                                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                                              | [Create a list of incoming projects accepted by customers and contracted with the company](LibrePlan_AnA15S01CustomerIncommingCommunicationsLists#TasK1) |                                                                                                                                 |                                                                                                                                   |                                                                                                                                |
| Task                                                                                                                       | 7                                                                                                                        | 8                                                                                                                          | 0                                                                                                                          | Low                                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                                              | [Mark the items of incoming projects communications as reviewed](LibrePlan_AnA15S01CustomerIncommingCommunicationsLists#TasK2)                           |                                                                                                                                 |                                                                                                                                   |                                                                                                                                |
| Task                                                                                                                       | 12                                                                                                                       | 11                                                                                                                         | 0                                                                                                                          | Low                                                                                                                       | [JavierMoran](Main_JavierMoran)                                                                                               | [SusanaMontes](Main_SusanaMontes)                                                                                              | [Include filter in the incoming projects communications list](LibrePlan_AnA15S01CustomerIncommingCommunicationsLists#TasK3)                              |                                                                                                                                 |                                                                                                                                   |                                                                                                                                |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S28CustomerIncommingCommunicationsLists?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](Main_SusanaMontes)                                                                                         | 29                                                                                                                                      | 0                                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                        |
| Total                                                                                                                     | 29                                                                                                                                      | 0                                                                                                                                       | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                        |

------------------------------------------------------------------------
