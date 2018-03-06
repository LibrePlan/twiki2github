[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA11S01UserSettings](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings "Topic revision: 5 (20 Aug 2012 - 09:52:45)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA11S01UserSettings?t=1520337851 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA11S01UserSettings "Attach an image or document to this topic")

 [AnA11S01UserSettings](/twiki/LibrePlan/AnA11S01UserSettings)
==============================================================================================================



|                        |                                                                        |
|------------------------|------------------------------------------------------------------------|
| Story summary          | User settings                                                          |
| Iteration              | [AnA11UsersModule](/twiki/LibrePlan/AnA11UsersModule)         |
| FEA                    | [AnA11S01UserSettings](/twiki/LibrePlan/AnA11S01UserSettings) |
| Story Lead             |                                                                        |
| Next Story             |                                                                        |
| Passed acceptance test | No                                                                     |

###  Tasks

This analysis is to describe the creation of several options to allow the user configure several things related to his user.



####  Create language configuration option for user

At present the language of the app is set depending on the language in which the browser is configured. If the browser is not configured with any of the languages currently supported by the app, the default language is English.

However, it has been received feedback that this way of configuring the language is a bit hidden and many users do not know where they can configure this feature.

Because of this a task to allow to configure the language of the application is going to be introduced in the app.

**Behavior**

Create an attribute in the entity User called "applicationLanguage" to save the value for the language that will be used for the application for each user.

Study the convenience of using an enum type with the languages for which there are translations. This enum will be used to store the value in the database and show the name of the language in the interface (properly internationalized).

**Interface:**

Location of the interface:

-   Create a new top level menu entry with name "My account".
-   Create a first menu entry called "Settings"

Create a new page with the following ui elements:

-   Title: Edit setting
-   Create a panel with a tab and with title: Data
-   Create a group box with title "Application settings"
-   Create a combo to select the language which is going to be used for the interface for the user on log in the app. The combo will have the following options:
    -   Use browser language configuration
    -   Galician
    -   Spanish
    -   English
-   Button "Save" to persist changes to database



####  Refactoring options about planning charts expanded to value per user

Now in the Configuration window there are three flags which coltrol if the resouce load charts are unfolded by default or they aren't. These flags are:

-   Planning charts expanded in company view.
-   Planning charts expanded in project view.
-   Planning charts expaneded in resource load view.

This task consists of moving them to the `User` entity.

They will be administrated through the interface for [Create language configuration option for user](/twiki/LibrePlan/AnA11S01UserSettings#TasK1) inside the groupbox *Application settings* where the combo to configure the language was created.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) Take into account delete with liquibase the previous columns for storing the flags in the `Configuration` entity.

In this task it will have to be changed the application to read this configuration values in a per user basis in the interface.



####  Incorporate new fields to the user

This task consists of adding to the `User` entity two new fields:

-   FirstName. First name of the user
-   LastName. Last name of the user

**Interface**

They will be administrated through the interface for [Create language configuration option for user](/twiki/LibrePlan/AnA11S01UserSettings#TasK1) in a new group box called *Personal Data* created above the group box *Application setting*.

It will be needed to modify the current user management window, located in *Administration/Management -&gt; Users -&gt; Accounts* to add the fields FirstName and LastName.



####  Incorporate password and mail to settings window for each user

This last task consists of incorporating fields that are managed at present in *Administration/Management -&gt; Users -&gt; Accounts* and add them too the *My account -&gt;Setting* window for the current window in the group box *Personal Data*

Fields are:

-   Login. Add the login with informative purposes with a label.
-   Password. Allow to chage the password for the user here too.
-   E-Mail.Allow to view/edit the e-mail address for the connected user.

###  User stories

-   [ItEr75S07UserSettings](/twiki/LibrePlan/ItEr75S07UserSettings)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                  | 24                                                                                                                                                  | 20                                                                                                                                                    | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [CristinaAlvarino](/twiki/Main/CristinaAlvarino) [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                 | [Create language configuration option for user](/twiki/LibrePlan/AnA11S01UserSettings#TasK1)                                                     |                                                                                                                                                            |                                                                                                                                                              | 24/06/2011                                                                                                                                                |
| Task                                                                                                                                                  | 16                                                                                                                                                  | 14                                                                                                                                                    | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [CristinaAlvarino](/twiki/Main/CristinaAlvarino) [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                 | [Refactoring options about planning charts expanded to value per user](/twiki/LibrePlan/AnA11S01UserSettings#TasK2)                              |                                                                                                                                                            |                                                                                                                                                              | 03/07/2011                                                                                                                                                |
| Task                                                                                                                                                  | 8                                                                                                                                                   | 10                                                                                                                                                    | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [CristinaAlvarino](/twiki/Main/CristinaAlvarino) [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                 | [Incorporate new fields to the user](/twiki/LibrePlan/AnA11S01UserSettings#TasK3)                                                                |                                                                                                                                                            |                                                                                                                                                              | 07/07/2011                                                                                                                                                |
| Task                                                                                                                                                  | 8                                                                                                                                                   | 7                                                                                                                                                     | 0                                                                                                                                                     | Low                                                                                                                                                  | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                          | [CristinaAlvarino](/twiki/Main/CristinaAlvarino) [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                 | [Incorporate password and mail to settings window for each user](/twiki/LibrePlan/AnA11S01UserSettings#TasK4)                                    |                                                                                                                                                            |                                                                                                                                                              | 15/07/2011                                                                                                                                                |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S01UserSettings?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [CristinaAlvarino](/twiki/Main/CristinaAlvarino) [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                            | 51                                                                                                                                                                 | 0                                                                                                                                                                  | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                   |
| Total                                                                                                                                                | 51                                                                                                                                                                 | 0                                                                                                                                                                  | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                   |

------------------------------------------------------------------------
