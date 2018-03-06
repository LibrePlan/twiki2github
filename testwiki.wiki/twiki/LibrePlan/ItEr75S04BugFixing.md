[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S04BugFixing](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing "Topic revision: 22 (28 Mar 2012 - 11:06:24)") (28 Mar 2012, [SusanaMontes](/twiki/Main/SusanaMontes))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S04BugFixing?t=1520337919 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S04BugFixing "Attach an image or document to this topic")

 [ItEr75S04BugFixing](/twiki/LibrePlan/ItEr75S04BugFixing)
========================================================================================================



|                        |                                                                    |
|------------------------|--------------------------------------------------------------------|
| Story summary          | Bug fixing                                                         |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)     |
| FEA                    | [ItEr75S04BugFixing](/twiki/LibrePlan/ItEr75S04BugFixing) |
| Story Lead             |                                                                    |
| Next Story             |                                                                    |
| Passed acceptance test | No                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Functional review of calendar patches

-- [JavierMoran](/twiki/Main/JavierMoran) - 23 Jun 2011

Testing patches about language settings

-- [JavierMoran](/twiki/Main/JavierMoran) - 24 Jun 2011

Testing ZK5 merge. List of fixes: [AnA05S07MigrationZK5\#TasK2](/twiki/LibrePlan/AnA05S07MigrationZK5#TasK2)

-- [JavierMoran](/twiki/Main/JavierMoran) - 29 Jun 2011

Fixed issue with scroll in all windows without ZK5 (modifying `template.zul`).

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 Jun 2011

Fixed to use EffortDuration[?](/twiki/bin/edit/LibrePlan/EffortDuration?topicparent=LibrePlan.ItEr75S04BugFixing "Create this topic") in JasperReports[?](/twiki/bin/edit/LibrePlan/JasperReports?topicparent=LibrePlan.ItEr75S04BugFixing "Create this topic") . To do this we must implement an Scriptlet used in each jrxml, where we must put the methods to convert from EffortDuration[?](/twiki/bin/edit/LibrePlan/EffortDuration?topicparent=LibrePlan.ItEr75S04BugFixing "Create this topic") to one of the allowed jrxml data types (String, BigDecimal[?](/twiki/bin/edit/LibrePlan/BigDecimal?topicparent=LibrePlan.ItEr75S04BugFixing "Create this topic") , Long, Integer...). We make the calculations in this Scriptlet classes, which are suffixed with "Scriptlet" in reports package.

-- [IgnacioDiaz](/twiki/Main/IgnacioDiaz) - 15 Sep 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                | 50                                                                                                                                                | 313.25                                                                                                                                              | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                           | Bug fixing                                                                                                                                              |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 50                                                                                                                                                | 50                                                                                                                                                  | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                     | Bug fixing                                                                                                                                              |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 50                                                                                                                                                | 55                                                                                                                                                  | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                       | Bug fixing                                                                                                                                              |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 25                                                                                                                                                | 25                                                                                                                                                  | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                         | Bug fixing                                                                                                                                              |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 25                                                                                                                                                | 25                                                                                                                                                  | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [CristinaAlvarino](/twiki/Main/CristinaAlvarino)                                                                                               | Bug fixing                                                                                                                                              |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 0                                                                                                                                                 | 156.25                                                                                                                                              | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                   | Bug fixing                                                                                                                                              |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |
| Task                                                                                                                                                | 40                                                                                                                                                | 8                                                                                                                                                   | 0                                                                                                                                                   | Low                                                                                                                                                | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                         | Application testing                                                                                                                                     |                                                                                                                                                          |                                                                                                                                                            |                                                                                                                                                         |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S04BugFixing?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                      | 313.25                                                                                                                                                           | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                    | 25                                                                                                                                                               | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                | 50                                                                                                                                                               | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                  | 55                                                                                                                                                               | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| [CristinaAlvarino](/twiki/Main/CristinaAlvarino)                                                                                          | 25                                                                                                                                                               | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| [JavierMoran](/twiki/Main/JavierMoran)                                                                                                    | 8                                                                                                                                                                | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                              | 156.25                                                                                                                                                           | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |
| Total                                                                                                                                              | 632.5                                                                                                                                                            | 0                                                                                                                                                                | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                 |

------------------------------------------------------------------------