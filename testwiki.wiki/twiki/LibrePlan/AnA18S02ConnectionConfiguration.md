[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA18S02ConnectionConfiguration](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration "Topic revision: 2 (26 Apr 2012 - 20:23:03)") (26 Apr 2012, [JavierToja](/twiki/Main/JavierToja))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA18S02ConnectionConfiguration?t=1520337864 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA18S02ConnectionConfiguration "Attach an image or document to this topic")

 [AnA18S02ConnectionConfiguration](/twiki/LibrePlan/AnA18S02ConnectionConfiguration)
===============================================================================================================================================



|                        |                                                                                              |
|------------------------|----------------------------------------------------------------------------------------------|
| Story summary          | Connection configuration                                                                     |
| Iteration              | [AnA18MantisIntegration](/twiki/LibrePlan/AnA18MantisIntegration)                   |
| FEA                    | [AnA18S02ConnectionConfiguration](/twiki/LibrePlan/AnA18S02ConnectionConfiguration) |
| Story Lead             |                                                                                              |
| Next Story             |                                                                                              |
| Passed acceptance test | No                                                                                           |

###  Tasks



####  Configuration data fields to activate and store the connection parameters with Mantis

This task consists of allowing the administrator to configure in the interface if LibrePlan is going to use Mantis and if so, the parameters to connect and interoperate with it.

The information will be stored in a new Hibernate component in the entity `Configuration`. The parameters will be:

-   mantisIntegrationEnabled
-   url
-   user
-   password

The interface to mange this values will be the following. It will be added a new tab in the page that is accessed clicking on: Administration/Management -&gt; LibrePlan Configuration.

There will be two areas:

-   Activation. It will have inside the field: Enable Mantis Integration
-   Parameters.
    -   URL
    -   User
    -   Password

###  User stories

-   [ItEr76S20ConnectionConfiguration](/twiki/LibrePlan/ItEr76S20ConnectionConfiguration)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                             | 16                                                                                                                                                             | 20                                                                                                                                                               | 0                                                                                                                                                                | Low                                                                                                                                                             | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                     | [JavierToja](/twiki/Main/JavierToja)                                                                                                                        | [Configuration data fields to activate and store the connection parameters with Mantis](/twiki/LibrePlan/AnA18S02ConnectionConfiguration#TasK1)             |                                                                                                                                                                       | 22/04/2012                                                                                                                                                              | 22/04/2012                                                                                                                                                           |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA18S02ConnectionConfiguration?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [JavierToja](/twiki/Main/JavierToja)                                                                                                                   | 20                                                                                                                                                                            | 0                                                                                                                                                                             | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                              |
| Total                                                                                                                                                           | 20                                                                                                                                                                            | 0                                                                                                                                                                             | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                              |

------------------------------------------------------------------------
