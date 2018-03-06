[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S06LdapAuhenticationItEr74S09](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09 "Topic revision: 9 (20 Aug 2012 - 09:52:54)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?t=1520337920 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09 "Attach an image or document to this topic")

 [ItEr75S06LdapAuhenticationItEr74S09](/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09)
========================================================================================================================================================



|                        |                                                                                                      |
|------------------------|------------------------------------------------------------------------------------------------------|
| Story summary          | LDAP authentication                                                                                  |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)                                       |
| FEA                    | [ItEr75S06LdapAuhenticationItEr74S09](/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09) |
| Story Lead             |                                                                                                      |
| Next Story             |                                                                                                      |
| Passed acceptance test | No                                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

We added a method(getLoggedUser()) in the class SecurityUtils[?](/twiki/bin/edit/LibrePlan/SecurityUtils?topicparent=LibrePlan.ItEr75S06LdapAuhenticationItEr74S09 "Create this topic") that retrieves the user logged in the application.

-- [CristinaAlvarino](/twiki/Main/CristinaAlvarino) - 24 Jun 2011

Updated branch to work with current master.

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 Jun 2011

Refactorized `retriveUser` method in `LDAPCustomAuthenticationProvider`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Jul 2011

Updated branch to current master.

-- [ManuelRego](/twiki/Main/ManuelRego) - 07 Jul 2011

Merged LDAP branch in master.

-- [ManuelRego](/twiki/Main/ManuelRego) - 11 Jul 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                 | 10                                                                                                                                                                 | 10                                                                                                                                                                   | 0                                                                                                                                                                    | Low                                                                                                                                                                 | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                         | [IgnacioDiaz](/twiki/Main/IgnacioDiaz) [CristinaAlvarino](/twiki/Main/CristinaAlvarino)                                                                | [Match the LDAP roles with the LibrePlan permissions](/twiki/LibrePlan/AnA04S06LdapAuthentication#TasK6)                                                        |                                                                                                                                                                           |                                                                                                                                                                             |                                                                                                                                                                          |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](/twiki/Main/IgnacioDiaz) [CristinaAlvarino](/twiki/Main/CristinaAlvarino)                                                           | 10                                                                                                                                                                                | 0                                                                                                                                                                                 | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                  |
| Total                                                                                                                                                               | 10                                                                                                                                                                                | 0                                                                                                                                                                                 | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                  |

------------------------------------------------------------------------
