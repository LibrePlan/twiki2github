[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S16JiraAndTimConnectorContributionIntegration](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration "Topic revision: 9 (05 Apr 2013 - 10:32:32)") (05 Apr 2013, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?t=1520337949 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration "Attach an image or document to this topic")

 [ItEr77S16JiraAndTimConnectorContributionIntegration](/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration)
========================================================================================================================================================================================



|                        |                                                                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Story summary          | Jira And Tim Connector                                                                                                               |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                                                                       |
| FEA                    | [ItEr77S16JiraAndTimConnectorContributionIntegration](/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration) |
| Story Lead             |                                                                                                                                      |
| Next Story             |                                                                                                                                      |
| Passed acceptance test | No                                                                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

We've created a new remote branch called `jira-integration` in order to upload all the patches related to JIRA connector, before pushing them in the `master` branch.

Some mails have been sent to the mailing list `libreplan-devel` in order to discuss different issues detected during the review. You can take a look to the thread in the following link: <http://sourceforge.net/mailarchive/forum.php?thread_name=5108E045.3030705%40igalia.com&forum_name=libreplan-devel>

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 Jan 2013

The `jira-integration` branch has been tested again a JIRA server and some changes has been done. Everything has been discussed in the same thread of the mailing list.

-- [ManuelRego](/twiki/Main/ManuelRego) - 01 Feb 2013

The `jira-integration` is merged now into `master`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Feb 2013

Created a new remote branch `tim-connector` and upload there the patches related to Tim connector after fixing minor issues like trailing whitespaces, tabs, ...

-- [ManuelRego](/twiki/Main/ManuelRego) - 08 Feb 2013

The first review of the Tim patches is done, but there're some issues pending note down in a pad: <https://etherpad.igalia.com/935>

-- [ManuelRego](/twiki/Main/ManuelRego) - 15 Feb 2013

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                                 | 40                                                                                                                                                                                 | 47                                                                                                                                                                                   | 0                                                                                                                                                                                    | Low                                                                                                                                                                                 | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                            | Review and integration of Jira and Tim connector                                                                                                                                         |                                                                                                                                                                                           |                                                                                                                                                                                             |                                                                                                                                                                                          |


