[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr77S16JiraAndTimConnectorContributionIntegration](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration "Topic revision: 9 (05 Apr 2013 - 10:32:32)") (05 Apr 2013, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?t=1520343707 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S16JiraAndTimConnectorContributionIntegration "Attach an image or document to this topic")  

 [ItEr77S16JiraAndTimConnectorContributionIntegration](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration)
=====================================================================================================================

|                        |                                                                                                                      |
|------------------------|----------------------------------------------------------------------------------------------------------------------|
| Story summary          | Jira And Tim Connector                                                                                               |
| Iteration              | [ItEr77Week34To44](LibrePlan_ItEr77Week34To44)                                                                       |
| FEA                    | [ItEr77S16JiraAndTimConnectorContributionIntegration](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration) |
| Story Lead             |                                                                                                                      |
| Next Story             |                                                                                                                      |
| Passed acceptance test | No                                                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

We've created a new remote branch called `jira-integration` in order to upload all the patches related to JIRA connector, before pushing them in the `master` branch.

Some mails have been sent to the mailing list `libreplan-devel` in order to discuss different issues detected during the review. You can take a look to the thread in the following link: <http://sourceforge.net/mailarchive/forum.php?thread_name=5108E045.3030705%40igalia.com&forum_name=libreplan-devel>

-- [ManuelRego](Main_ManuelRego) - 30 Jan 2013

The `jira-integration` branch has been tested again a JIRA server and some changes has been done. Everything has been discussed in the same thread of the mailing list.

-- [ManuelRego](Main_ManuelRego) - 01 Feb 2013

The `jira-integration` is merged now into `master`.

-- [ManuelRego](Main_ManuelRego) - 05 Feb 2013

Created a new remote branch `tim-connector` and upload there the patches related to Tim connector after fixing minor issues like trailing whitespaces, tabs, ...

-- [ManuelRego](Main_ManuelRego) - 08 Feb 2013

The first review of the Tim patches is done, but there're some issues pending note down in a pad: <https://etherpad.igalia.com/935>

-- [ManuelRego](Main_ManuelRego) - 15 Feb 2013

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

| [Tasks](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr77S16JiraAndTimConnectorContributionIntegration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                             | 40                                                                                                                             | 47                                                                                                                               | 0                                                                                                                                | Low                                                                                                                             | [JavierMoran](Main_JavierMoran)                                                                                                     | [ManuelRego](Main_ManuelRego)                                                                                                        | Review and integration of Jira and Tim connector                                                                                     |                                                                                                                                       |                                                                                                                                         |                                                                                                                                      |
