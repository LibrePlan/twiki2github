[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S07PersonalTimesheetsPeriodictyConfiguration](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration "Topic revision: 6 (11 Sep 2012 - 06:13:37)") (11 Sep 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?t=1520337945 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration "Attach an image or document to this topic")

 [ItEr77S07PersonalTimesheetsPeriodictyConfiguration](/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration)
======================================================================================================================================================================================



|                        |                                                                                                                                    |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Story summary          | Personal Timesheets Periodicty Configuration                                                                                       |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                                                                     |
| FEA                    | [ItEr77S07PersonalTimesheetsPeriodictyConfiguration](/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration) |
| Story Lead             |                                                                                                                                    |
| Next Story             |                                                                                                                                    |
| Passed acceptance test | No                                                                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Created a remote branch called `personal-timesheets-periodicity` to work in these tasks.

####  Rename monthly timesheets to personal timesheets

From now on in the UI the users will see **personal timesheet** instead of *monthly timesheet* as they could change the periodicity.

Liquibase change for the work report type has been added too.

No refactorings in the source code names have been done so far.

####  Add new option to configure timesheet periodicity

Add new attribute in `Configuration` class, using a enum to store the different periodicity options.

Add option in configuration window.

Disable option if there's any personal timehseet already stored in the DB.

-- [ManuelRego](/twiki/Main/ManuelRego) - 27 Aug 2012

####  Modify list of personal timesheets in user dashboard

The list of personal timesheets in the user dashboard has been changed to take into account the periodicity.

The format to represent a personal timesheet depending on the periodicity is:

-   Monthly: July 2012, August 2012, ..., January 2013, ...
-   Twice monthly: July 2012 1st fortnight, July 2012 2nd fortnight, August 2012 1st fortnight, ..., January 2013 1st fortnight, ...
-   Weekly: Week 30 (July 2012), Week 31 (July - August 2012), ..., Week 1 (December 2012 - January 2013), ...

Most of the methods that need to be changed delegates its behavior in the new enum `PersonalTimesheetsPeriodicityEnum`, which is in charge to calculate the start and end of a personal timesheet depending on the periodicity and so on.

####  Change UI for editing a personal timehseet depending on periodicity

The UI to edit a personal timesheet has been adapted to work correctly depending on the periodicity. Again trying to delegate as much as possible in `PersonalTimesheetsPeriodicityEnum`.

Also the option to create a personal timesheet from work reports window has been reviewed and adapted accordingly.

Moreover, the source code has been refactored in order to change *monthly timesheet* for *personal timesheet* in order to avoid misunderstandings in the future.

-- [ManuelRego](/twiki/Main/ManuelRego) - 28 Aug 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S07PersonalTimesheetsPeriodictyConfiguration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                                | 2                                                                                                                                                                                 | 0.5                                                                                                                                                                                 | 0                                                                                                                                                                                   | Low                                                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                           | [Rename monthly timesheets to personal timesheets](/twiki/LibrePlan/AnA12S05PersonalTimesheetsPeriodictyConfiguration#TasK1)                                                   |                                                                                                                                                                                          |                                                                                                                                                                                            |                                                                                                                                                                                         |
| Task                                                                                                                                                                                | 2                                                                                                                                                                                 | 2                                                                                                                                                                                   | 0                                                                                                                                                                                   | Low                                                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                           | [Add new option to configure timesheet periodicity](/twiki/LibrePlan/AnA12S05PersonalTimesheetsPeriodictyConfiguration#TasK2)                                                  |                                                                                                                                                                                          |                                                                                                                                                                                            |                                                                                                                                                                                         |
| Task                                                                                                                                                                                | 5                                                                                                                                                                                 | 2.5                                                                                                                                                                                 | 0                                                                                                                                                                                   | Low                                                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                           | [Modify list of personal timesheets in user dashboard](/twiki/LibrePlan/AnA12S05PersonalTimesheetsPeriodictyConfiguration#TasK3)                                               |                                                                                                                                                                                          |                                                                                                                                                                                            |                                                                                                                                                                                         |
| Task                                                                                                                                                                                | 7                                                                                                                                                                                 | 4                                                                                                                                                                                   | 0                                                                                                                                                                                   | Low                                                                                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                           | [Change UI for editing a personal timehseet depending on periodicity](/twiki/LibrePlan/AnA12S05PersonalTimesheetsPeriodictyConfiguration#TasK4)                                |                                                                                                                                                                                          |                                                                                                                                                                                            |                                                                                                                                                                                         |


