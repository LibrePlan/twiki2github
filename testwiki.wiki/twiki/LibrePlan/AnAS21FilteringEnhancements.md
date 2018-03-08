[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnAS21FilteringEnhancements](LibrePlan_AnAS21FilteringEnhancements "Topic revision: 2 (01 Feb 2013 - 08:30:19)") (01 Feb 2013, [LorenzoTilve](Main_LorenzoTilve))[Edit](LibrePlan_AnAS21FilteringEnhancements?t=1520343624 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnAS21FilteringEnhancements "Attach an image or document to this topic")  

 [AnAS21FilteringEnhancements](LibrePlan_AnAS21FilteringEnhancements)
=====================================================================

|                        |                                                                      |
|------------------------|----------------------------------------------------------------------|
| Story summary          | Filtering enhancements                                               |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)                           |
| FEA                    | [AnAS21FilteringEnhancements](LibrePlan_AnAS21FilteringEnhancements) |
| Story Lead             |                                                                      |
| Next Story             |                                                                      |
| Passed acceptance test | No                                                                   |

###  Tasks

####  Adding configuration parameters in user preferences for projects planning and projects list perspective

Three new configuration variables will be added in the LibrePlan users:

-   Label to use in projects lists. It will save the label that will be use to filter the projects planning and the projects list.
-   Ahead planning horizon. Integer number specified in months to specify the projects that from current day want to be included in the filtering result.
-   Backwards planning horizin. Integer specified in months to specify the project that want to be included in the results before the current date.

These options will be managed in the user preferences window. By default users will not have any configuration of this filters.

####  Including per user filtering in projects planning and project lists perspective

It will be implemented a mechansim to fill the filters in the projects planning and projects lists perspective when a user enters them with the next values:

-   Label filter. It will be included the configured label (if any) that the user has selected in his configuration parameters.
-   Start date filter. It will be filled with the value: Current date minus backwards planning horizon
-   End date filter: It will be filled with the value: Current date plus ahead planning horizon.

With the regard to the label filter, the query will get all the projects that have assigned the label in the root of the project.

####  User session store of the last value of the filters used in the projects planning and projects list view

It will be implemented a mechanism so that, on filling some value in the filters of the projects planning or the projects list perspective and the filter is exectued, in that moment, they will be saved in the user session those values.

The specific filters that will be soaved are:

-   Criteria and labels sequence. Combination with one or more label values and criterion that the projects can have assigned.
-   Start and end date.

It will be implemented also a mechanims so that when the user visits the projects planning or the project list screens, if there are some filtering values stored in the user session, a filtering is executed with those parameters.

####  Adding configuration parameters for filters in user preferences for resource load window

Three new variables will be added:

-   Criterion to be used in resource load. It will track the specific criterion that will be used for filtering in the resource load. It will allow to filter by a single criterion, I mean, it will not be possible to configure several criteria.
-   Ahead horizon in resource load. Integer number specified in months to specify the start of the interval to show the resource load in the filtering result.
-   Backwards horizon in resource load. Integer specified in months to specify the end of the interval to show the resource load in the filtering result.

These options will be managed in the user preferences window. By default users will not have any configuration of this filters.

####  Including the per user filtering in the resource load view

It will be implemented a mechanism to fill the filters in the resource load view with the next values:

-   Criterion filter. It will be included the criterion configured in the connected user parameters.
-   Start date. It will be filled with the value: Current date minus backwards horizon in resource load
-   End date. It will be filled with the value: Current date plus ahead horizon in resource load.

With regard to the filter, the query will get all the resources and their bounded load that satisfy the criterion configured during the filtering time interval specified.

####  User session store of the last value of the filters used in resources load view

It will be implemented a mechanism so that, on filling some value in the filters of the resources load perspective and the filter is exectued, in that moment, they will be saved in the user session those values.

The specific filters that will be soaved are:

-   Criteria and resources sequence. Combination of one or more criteria value which the resource have to satisfy and resources names to be included in the load analysis.
-   Start and end date.

It will be implemented also a mechanims so that when the user visits the resource load view, if there are some filtering values stored in the user session, a filtering is executed with those parameters.

####  Memory mechansim for filters used in the project planning

This task consists of implementing a memorazing mechanism to keep the filtering values in the project planning in the perspectives of projects planning and project details.

The filters values that will be memorized are:

-   *Task filter*. Text string which has to be part of the activity name to be selected.
-   *Label filter*. Label(s) which has to be assigend to the task through the bounded order element (wbs element). If there are several labels, all of them have to be assigned to the task to be selected.
-   *Criterion*. Criterio(s) which are used in any of the resource allocation of the tasks. If there are several criteria all of them have to be assigned in the allocation to satisfy the filtering.
-   *Date from*. Tasks to be selected in the output have to have a start date after the filtering date.
-   *Date up to*. Tasks to be selected in the output have to have an end date before the filtering date.
-   *Labels without inheritance*. It tracks if in the label filtering they are selected in the output tasks which inherits a label or if only the tasks which have the labels directely assigned appeared in the output.

The memorizing mechansim to be implemented will consist of that, on asking for a filtering, the elements that can be memorized are stored in the user session.

The memorized values will be project specific. This means that they will be saved as many filtering different values as projects the user visits during his session.

As part of this task will be implemented too a procedure to fill the filtering and execute it with those value when a user enters a project in the planning perspective or the project details perspective.

###  User stories

-   [ItEr77S15FilteringEnhancements](LibrePlan_ItEr77S15FilteringEnhancements)

###  Tasks in this story

| [Tasks](LibrePlan_AnAS21FilteringEnhancements?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnAS21FilteringEnhancements?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnAS21FilteringEnhancements?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnAS21FilteringEnhancements?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnAS21FilteringEnhancements?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnAS21FilteringEnhancements?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnAS21FilteringEnhancements?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnAS21FilteringEnhancements?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                                            | [Start Date](LibrePlan_AnAS21FilteringEnhancements?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnAS21FilteringEnhancements?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnAS21FilteringEnhancements?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| Task                                                                                                     | 4                                                                                                      | 0                                                                                                        | 4                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [Adding configuration parameters in user preferences for projects planning and projects list perspective](LibrePlan_AnAS21FilteringEnhancements#TasK1)  |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 5                                                                                                      | 0                                                                                                        | 5                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [Including per user filtering in projects planning and project lists perspective](LibrePlan_AnAS21FilteringEnhancements#TasK2)                          |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 7                                                                                                      | 0                                                                                                        | 7                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [User session store of the last value of the filters used in the projects planning and projects list view](LibrePlan_AnAS21FilteringEnhancements#TasK3) |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 4                                                                                                      | 0                                                                                                        | 4                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [Adding configuration parameters for filters in user preferences for resource load window](LibrePlan_AnAS21FilteringEnhancements#TasK4)                 |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 5                                                                                                      | 0                                                                                                        | 5                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [Incluing the per user filtering in the resource load view](LibrePlan_AnAS21FilteringEnhancements#TasK5)                                                |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 4                                                                                                      | 0                                                                                                        | 4                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [User session store of the last value of the filters used in resources load view](LibrePlan_AnAS21FilteringEnhancements#TasK6)                          |                                                                                                               |                                                                                                                 |                                                                                                              |
| Task                                                                                                     | 7                                                                                                      | 0                                                                                                        | 7                                                                                                        | Low                                                                                                     | [JavierMoran](Main_JavierMoran)                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                            | [Memory mechansim for filters used in the project planning](LibrePlan_AnAS21FilteringEnhancements#TasK7)                                                |                                                                                                               |                                                                                                                 |                                                                                                              |
