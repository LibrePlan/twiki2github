[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA08S16DefaultData](LibrePlan_AnA08S16DefaultData "Topic revision: 6 (03 Jan 2012 - 16:39:13)") (03 Jan 2012, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA08S16DefaultData?t=1520344051 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S16DefaultData "Attach an image or document to this topic")  

 [AnA08S16DefaultData](LibrePlan_AnA08S16DefaultData)
=====================================================

|                        |                                                      |
|------------------------|------------------------------------------------------|
| Story summary          | Create default data                                  |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)           |
| FEA                    | [AnA08S16DefaultData](LibrePlan_AnA08S16DefaultData) |
| Story Lead             |                                                      |
| Next Story             |                                                      |
| Passed acceptance test | No                                                   |

###  Tasks

####  Create default data in entities

This task is to improve current default data to insert more suitable values. These default data are inserted by `Bootstrappers` on application launching. If they find empty the entity they are initialization in the database they insert the default data.

The new default data will be the following:

***Criteria***

-   Location
    -   Africa
    -   America
    -   Asia
    -   Australia
    -   Europe

&nbsp;

-   Category
    -   Manager
    -   Senior worker
    -   Junior worker

&nbsp;

-   Skill

***Labels***

-   Priority
    -   High urgency
    -   Medium urgency
    -   Low urgency

***Hours Type***

-   Default
    -   30
-   Overtime
    -   50

***Work report model***

-   Name: Default
-   Resource: Line
-   Task: Line
-   Date: Line

***Exception types***

-   Resource Holiday
    -   Yellow
    -   Standard Effort: 0h
    -   Extra Effort: 0h

&nbsp;

-   Bank holiday
    -   Red
    -   Standard Effort: 0h
    -   Extra Effort: 0h

&nbsp;

-   Half-day holiday
    -   Orange
    -   Standard Effort: 4h
    -   Extra Effrot: 0h

&nbsp;

-   Leave
    -   Magenta
    -   Standard Effort: 0h
    -   Extra Effort: 0h

&nbsp;

-   Strike
    -   Purple
    -   Standard Effort: 0h
    -   Extra Effort: 0h

####  Insert empty conditions to insert default data

Now there is a problem. If a user does not like the default data and remove then, on stopping the application and starting it again the default data will be inserted again.

This provokes that people cannot erase never default data.

Therefore, the solution is to insert in each bootstrapper a condition to insert the default data just if the the entity it is reponsible for has not any value in the database.

###  User stoties

-   [ItEr75S29DefaultData](LibrePlan_ItEr75S29DefaultData)

###  Tasks in this story

| [Tasks](LibrePlan_AnA08S16DefaultData?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA08S16DefaultData?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA08S16DefaultData?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA08S16DefaultData?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA08S16DefaultData?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA08S16DefaultData?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA08S16DefaultData?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA08S16DefaultData?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA08S16DefaultData?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA08S16DefaultData?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA08S16DefaultData?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Task                                                                                             | 4                                                                                              | 4                                                                                                | 0                                                                                                | Low                                                                                             | [JavierMoran](Main_JavierMoran)                                                                     | [IgnacioDiaz](Main_IgnacioDiaz)                                                                      | [Create default data in entities](LibrePlan_AnA08S16DefaultData#TasK1)                               |                                                                                                       |                                                                                                         |                                                                                                      |
| Task                                                                                             | 4                                                                                              | 4                                                                                                | 0                                                                                                | Low                                                                                             | [JavierMoran](Main_JavierMoran)                                                                     | [IgnacioDiaz](Main_IgnacioDiaz)                                                                      | [Insert empty conditions to insert default data](LibrePlan_AnA08S16DefaultData#TasK2)                |                                                                                                       |                                                                                                         |                                                                                                      |

###  Total Hours in this Story

| [User](LibrePlan_AnA08S16DefaultData?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA08S16DefaultData?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA08S16DefaultData?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA08S16DefaultData?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz)                                                                 | 8                                                                                                             | 0                                                                                                             | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                              |
| Total                                                                                           | 8                                                                                                             | 0                                                                                                             | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                              |

------------------------------------------------------------------------
