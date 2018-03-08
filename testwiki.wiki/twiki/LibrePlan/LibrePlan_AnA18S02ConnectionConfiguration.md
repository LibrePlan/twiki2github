[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA18S02ConnectionConfiguration](LibrePlan_AnA18S02ConnectionConfiguration "Topic revision: 2 (26 Apr 2012 - 20:23:03)") (26 Apr 2012, [JavierToja](Main_JavierToja))[Edit](LibrePlan_AnA18S02ConnectionConfiguration?t=1520343618 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA18S02ConnectionConfiguration "Attach an image or document to this topic")  

 [AnA18S02ConnectionConfiguration](LibrePlan_AnA18S02ConnectionConfiguration)
=============================================================================

|                        |                                                                              |
|------------------------|------------------------------------------------------------------------------|
| Story summary          | Connection configuration                                                     |
| Iteration              | [AnA18MantisIntegration](LibrePlan_AnA18MantisIntegration)                   |
| FEA                    | [AnA18S02ConnectionConfiguration](LibrePlan_AnA18S02ConnectionConfiguration) |
| Story Lead             |                                                                              |
| Next Story             |                                                                              |
| Passed acceptance test | No                                                                           |

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

-   [ItEr76S20ConnectionConfiguration](LibrePlan_ItEr76S20ConnectionConfiguration)

###  Tasks in this story

| [Tasks](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                         | [Start Date](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                         | 16                                                                                                         | 20                                                                                                           | 0                                                                                                            | Low                                                                                                         | [JavierMoran](Main_JavierMoran)                                                                                 | [JavierToja](Main_JavierToja)                                                                                    | [Configuration data fields to activate and store the connection parameters with Mantis](LibrePlan_AnA18S02ConnectionConfiguration#TasK1) |                                                                                                                   | 22/04/2012                                                                                                          | 22/04/2012                                                                                                       |

###  Total Hours in this Story

| [User](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA18S02ConnectionConfiguration?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [JavierToja](Main_JavierToja)                                                                               | 20                                                                                                                        | 0                                                                                                                         | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                          |
| Total                                                                                                       | 20                                                                                                                        | 0                                                                                                                         | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                          |

------------------------------------------------------------------------
