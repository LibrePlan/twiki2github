[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA04S04NavalPlanVersion](LibrePlan_AnA04S04NavalPlanVersion "Topic revision: 3 (20 Aug 2012 - 09:52:44)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA04S04NavalPlanVersion?t=1520344035 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA04S04NavalPlanVersion "Attach an image or document to this topic")  

 [AnA04S04NavalPlanVersion](LibrePlan_AnA04S04NavalPlanVersion)
===============================================================

|                        |                                                                |
|------------------------|----------------------------------------------------------------|
| Story summary          | LibrePlan version                                              |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)               |
| FEA                    | [AnA04S04NavalPlanVersion](LibrePlan_AnA04S04NavalPlanVersion) |
| Story Lead             |                                                                |
| Next Story             |                                                                |
| Passed acceptance test | No                                                             |

###  Tasks

####  Add version to LibrePlan interface

This task is to show the LibrePlan version in the interface of the program.

The idea is to define the project version of the project and display in in the web interface.

To configure the version of LibrePlan the following steps have to be done:

1.  It is going to be used the parent pom.xml tag to get the version information. The first version it is needed to register is **0.9.0**. Change this.
2.  Change the pom.xml files in the subprojects to take the same version as the parent pom.xml version. Look to this link to get the parent pom version for use in the same way in the pom.xml of the subprojects. <http://docs.codehaus.org/display/MAVENUSER/MavenPropertiesGuide>
3.  Create a bean with Singleton scope called *VersionInformation* for a class with just a property called *versionName*. Configure the initialization of this variable of type String to ${project.version}. This will be filtered and substituted by the value configure, in our case, **0.9.0**.
4.  Include this version in the login page of the application, The location will be in the line of the browsers supported righ aligned.

###  User stories

-   [ItEr64S08NavalPlanVersion](LibrePlan_ItEr64S08NavalPlanVersion)
-   [ItEr65S03NavalPlanVersionItEr64S08](LibrePlan_ItEr65S03NavalPlanVersionItEr64S08)

###  Tasks in this story

| [Tasks](LibrePlan_AnA04S04NavalPlanVersion?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA04S04NavalPlanVersion?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA04S04NavalPlanVersion?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA04S04NavalPlanVersion?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA04S04NavalPlanVersion?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA04S04NavalPlanVersion?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA04S04NavalPlanVersion?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA04S04NavalPlanVersion?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA04S04NavalPlanVersion?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA04S04NavalPlanVersion?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA04S04NavalPlanVersion?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Task                                                                                                  | 0                                                                                                   | 0                                                                                                     | 0                                                                                                     | Low                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                          | [SusanaMontes](Main_SusanaMontes)                                                                         | [Add version to LibrePlan interface](LibrePlan_AnA04S04NavalPlanVersion#TasK1)                            |                                                                                                            |                                                                                                              |                                                                                                           |

###  Total Hours in this Story

| [User](LibrePlan_AnA04S04NavalPlanVersion?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA04S04NavalPlanVersion?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA04S04NavalPlanVersion?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA04S04NavalPlanVersion?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [SusanaMontes](Main_SusanaMontes)                                                                    | 0                                                                                                                  | 0                                                                                                                  | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                    |
| Total                                                                                                | 0                                                                                                                  | 0                                                                                                                  | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                    |

------------------------------------------------------------------------
