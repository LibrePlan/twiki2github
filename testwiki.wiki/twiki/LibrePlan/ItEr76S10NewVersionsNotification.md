[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S10NewVersionsNotification](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification "Topic revision: 2 (20 Aug 2012 - 09:50:16)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S10NewVersionsNotification?t=1520337934 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S10NewVersionsNotification "Attach an image or document to this topic")

 [ItEr76S10NewVersionsNotification](/twiki/LibrePlan/ItEr76S10NewVersionsNotification)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | System to notify users about new versions being published                                      |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                                 |
| FEA                    | [ItEr76S10NewVersionsNotification](/twiki/LibrePlan/ItEr76S10NewVersionsNotification) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

In order to implement this feature the class `VersionInformation` has been modified.

This class will be in charge to store the cached value if a new version is detected.

The method used to make the GET request is java.net.URL.openStream()

Patches were pushed to `libreplan-1.2` branch too, because of conversation in the forum with an user: <http://sourceforge.net/projects/libreplan/forums/forum/1085570/topic/4933213>

-- [ManuelRego](/twiki/Main/ManuelRego) - 13 Jan 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S10NewVersionsNotification?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 3                                                                                                                                                               | 2                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Show notification to admins when a new version is released](/twiki/LibrePlan/AnA08S17NewVersionsNotification#TasK1)                                         |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 2                                                                                                                                                               | 2                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Add option to disable notification](/twiki/LibrePlan/AnA08S17NewVersionsNotification#TasK2)                                                                 |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 2                                                                                                                                                               | 2                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Add option to request permissions to collect stats](/twiki/LibrePlan/AnA08S17NewVersionsNotification#TasK3)                                                 |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |


