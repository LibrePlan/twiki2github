[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA08S16DefaultData](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData "Topic revision: 6 (03 Jan 2012 - 16:39:13)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA08S16DefaultData?t=1520337847 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S16DefaultData "Attach an image or document to this topic")

 [AnA08S16DefaultData](/twiki/LibrePlan/AnA08S16DefaultData)
===========================================================================================================



|                        |                                                                      |
|------------------------|----------------------------------------------------------------------|
| Story summary          | Create default data                                                  |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)           |
| FEA                    | [AnA08S16DefaultData](/twiki/LibrePlan/AnA08S16DefaultData) |
| Story Lead             |                                                                      |
| Next Story             |                                                                      |
| Passed acceptance test | No                                                                   |

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

-   Category
    -   Manager
    -   Senior worker
    -   Junior worker

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

-   Bank holiday
    -   Red
    -   Standard Effort: 0h
    -   Extra Effort: 0h

-   Half-day holiday
    -   Orange
    -   Standard Effort: 4h
    -   Extra Effrot: 0h

-   Leave
    -   Magenta
    -   Standard Effort: 0h
    -   Extra Effort: 0h

-   Strike
    -   Purple
    -   Standard Effort: 0h
    -   Extra Effort: 0h



####  Insert empty conditions to insert default data

Now there is a problem. If a user does not like the default data and remove then, on stopping the application and starting it again the default data will be inserted again.

This provokes that people cannot erase never default data.

Therefore, the solution is to insert in each bootstrapper a condition to insert the default data just if the the entity it is reponsible for has not any value in the database.

###  User stoties

-   [ItEr75S29DefaultData](/twiki/LibrePlan/ItEr75S29DefaultData)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                 | 4                                                                                                                                                  | 4                                                                                                                                                    | 0                                                                                                                                                    | Low                                                                                                                                                 | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                         | [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                          | [Create default data in entities](/twiki/LibrePlan/AnA08S16DefaultData#TasK1)                                                                   |                                                                                                                                                           |                                                                                                                                                             |                                                                                                                                                          |
| Task                                                                                                                                                 | 4                                                                                                                                                  | 4                                                                                                                                                    | 0                                                                                                                                                    | Low                                                                                                                                                 | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                         | [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                          | [Insert empty conditions to insert default data](/twiki/LibrePlan/AnA08S16DefaultData#TasK2)                                                    |                                                                                                                                                           |                                                                                                                                                             |                                                                                                                                                          |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S16DefaultData?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                                                                     | 8                                                                                                                                                                 | 0                                                                                                                                                                 | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                  |
| Total                                                                                                                                               | 8                                                                                                                                                                 | 0                                                                                                                                                                 | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                  |

------------------------------------------------------------------------
