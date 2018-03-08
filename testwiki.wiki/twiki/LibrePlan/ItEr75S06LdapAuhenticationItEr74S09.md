[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr75S06LdapAuhenticationItEr74S09](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09 "Topic revision: 9 (20 Aug 2012 - 09:52:54)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?t=1520343676 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S06LdapAuhenticationItEr74S09 "Attach an image or document to this topic")  

 [ItEr75S06LdapAuhenticationItEr74S09](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09)
=====================================================================================

|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | LDAP authentication                                                                  |
| Iteration              | [ItEr75week25To52](LibrePlan_ItEr75week25To52)                                       |
| FEA                    | [ItEr75S06LdapAuhenticationItEr74S09](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

We added a method(getLoggedUser()) in the class SecurityUtils[?](LibrePlan_SecurityUtils?topicparent=LibrePlan.ItEr75S06LdapAuhenticationItEr74S09 "Create this topic") that retrieves the user logged in the application.

-- [CristinaAlvarino](Main_CristinaAlvarino) - 24 Jun 2011

Updated branch to work with current master.

-- [ManuelRego](Main_ManuelRego) - 30 Jun 2011

Refactorized `retriveUser` method in `LDAPCustomAuthenticationProvider`.

-- [ManuelRego](Main_ManuelRego) - 05 Jul 2011

Updated branch to current master.

-- [ManuelRego](Main_ManuelRego) - 07 Jul 2011

Merged LDAP branch in master.

-- [ManuelRego](Main_ManuelRego) - 11 Jul 2011

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

| [Tasks](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                             | 10                                                                                                             | 10                                                                                                               | 0                                                                                                                | Low                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                     | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                            | [Match the LDAP roles with the LibrePlan permissions](LibrePlan_AnA04S06LdapAuthentication#TasK6)                    |                                                                                                                       |                                                                                                                         |                                                                                                                      |

###  Total Hours in this Story

| [User](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr75S06LdapAuhenticationItEr74S09?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                       | 10                                                                                                                            | 0                                                                                                                             | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                              |
| Total                                                                                                           | 10                                                                                                                            | 0                                                                                                                             | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                              |

------------------------------------------------------------------------
