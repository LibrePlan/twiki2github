[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA04S06LdapAuthentication](LibrePlan_AnA04S06LdapAuthentication "Topic revision: 11 (20 Aug 2012 - 09:52:44)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA04S06LdapAuthentication?t=1520344035 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA04S06LdapAuthentication "Attach an image or document to this topic")  

 [AnA04S06LdapAuthentication](LibrePlan_AnA04S06LdapAuthentication)
===================================================================

|                        |                                                                    |
|------------------------|--------------------------------------------------------------------|
| Story summary          | LDAP Authentication                                                |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)                   |
| FEA                    | [AnA04S06LdapAuthentication](LibrePlan_AnA04S06LdapAuthentication) |
| Story Lead             |                                                                    |
| Next Story             |                                                                    |
| Passed acceptance test | No                                                                 |

###  Tasks

Activity diagram with the LDAP authentication final process description:

![Activity\_Diagram\_LDAP\_Authentication.png](/twiki/pub/LibrePlan/AnA04S06LdapAuthentication/Activity_Diagram_LDAP_Authentication.png)

####  Develope/configure handler for LDAP authentication

This task consists of configure the SpringSecurity framework in order to be able to authenticate against the LDAP.

The LDAP is used for authentication but the [LibrePlan](LibrePlan_LibrePlan) database info for users is used too. So, it is required that there is a object user in the [LibrePlan](LibrePlan_LibrePlan) database with the login that the user is inserting in the interface. So, at this first step:

-   If the authentication with LDAP fails =&gt; The user is not allowed to enter the application.
-   If the authentication succeds with LDAP but there is not user in [LibrePlan](LibrePlan_LibrePlan) with the same login =&gt; The user is not allowed to enter the application.

In this first step the configuration will be set in the XML Spring files and, therefore, is set by the user before compiling the program.

####  Interface for configuring the the LDAP connection and authentication parameters.

This task consists of developing an interface in ZK in order to allow to configure the LDAP connection at runtime.

The features of the interface will be the following:

-   It will be placed in the Configuration Window placed in the menu option Administration/Management.
-   It will be created a tab with title Authentication.
    -   The screen will have an interface widget to select if you want to use LDAP or conventional database authentication. If the user selects LDAP then a second part of the interface with all the parameters for the connection with the LDAP will be activated.
    -   The section for the LDAP parameters will have two types of parameteres:
        -   Parameters to connect to the LDAP.
        -   Parameters to configure the authentication of the users. Here it will be chosen if there are several alternativas the most general method if possible.

The data of the interface will be stored in the `Configuration` entity. It will be studied if it is needed to create composite objets to encapsulate better this information or just to create new columns, one per parameter.

At this task has to be developed and configured a runtime configuration engine for configure the Spring beans (authentication handlers) to use the current one or use the LDAP new one developed in the task before.

![tip](/twiki/pub/TWiki/TWikiDocGraphics/tip.gif) It is possible to have just one handler but with a parameter of configuration saying if it is being using the database or the LDAP+Database behaviour implemented.

####  Develope a composite handler LDAP/Database

The idea now is to have a composite authentication handler that first tries to authenticate againts the LDAP and if it fails use the [LibrePlan](LibrePlan_LibrePlan) database password (current behaviour).

It will be studied if the most appropiate option for doing the authentication is to have:

So, the steps that will be done at this point are the following:

-   1) It is checked if there is a user with the login specified in the by the user in the database
    -   1.1) It there is not user =&gt; Login not allowed.
    -   1.2) If there is go to 2)
-   2) Authentication with LDAP is tried.
    -   2.1) Successfull =&gt; User in.
    -   2.2) Error (LDAP not reachable or bad user/password combination) =&gt; Go to 3
-   3) Try the database authentication.
    -   3.1) User in.
    -   3.2) Login not allowed.

####  LDAP import of users

This part is to allow to create users in the database of [LibrePlan](LibrePlan_LibrePlan) if the authentication with LDAP is sucessful and there is any user created in NavalPLan[?](LibrePlan_NavalPLan?topicparent=LibrePlan.AnA04S06LdapAuthentication "Create this topic") at the moment of doing login.

So, the steps now will be for the authentication:

-   2) Authentication with LDAP is tried.
    -   2.1) Successful.
        -   2.1.1) It is checked if there is the user in the database. If this user does not exist, it will be created.
        -   2.1.2) It is checked if the field "save passwords in database" is activated. If it is goes to 2.1.3, else goes to 2.1.4.
        -   2.1.3) It is checked if the password of the user in the database is the same as the one in the LDAP. If it is not will be updated in the database. This situation handles the possible changes of passwords in the LDAP.
        -   2.1.4) User in.
    -   2.2) Error (LDAP not reachable or bad user/password combination) =&gt; Go to 3
-   3) Try the database authentication.
    -   3.1) User in.
    -   3.2) Login not allowed.

####  Support for two types of users

This task will allow to have users just in the database and not in the LDAP. So, in order to have this feature the changes that are needed are the following:

-   To create an attribute in the entity `User` to configure if is a *LDAP based user* or a *Database user*. It will have a boolean type.
-   Change the interface for editing the users with the following points:
    -   Introduce an informative label in the user form saying the type of user.
    -   Modify the list of users window with a column with the information with the user type.
    -   Do read-only the *General User Data* panel for the edition window of users of type *LDAP based user*

At this point it has two be introduced a check in the process to create a normal database user. If the LDAP configuration is set on, it will be checked if there is a user already in the LDAP with that login. If that user exist, then an error will be given to the user.

It will be handled here the following situation too: On doing login a user if the LDAP connection is set on it is checked if there a user in the database:

-   Now it is checked if it has the type *LDAP based user*. If it has not this type, the type will be changed to be this.

###  Match the LDAP roles with the [LibrePlan](LibrePlan_LibrePlan) permissions

This task will be assesed if it is interesting later. It can have quite a lot of possibilities depending on the structure of the LDAP.

###  Do compatible the change password and user roles administration with LDAP users.

***Change 1***

In the version 1.2.0 of LibrePlan a change user password use case was added. A user can change his password if he remembers his old password.

Now, this use case does not do any distinction between LDAP users and conventional database users. This behavior has to be changed to:

-   If a user is an LDAP user and the database authentication is enabled, then the change password per user window must be put in read-only mode and a suitable informative message explaining this: *LDAP users cannot change their password in LDAP authentication is enabled. Talk to one of the administrators*

***Change 2***

In the window to manage users for the admin users - top menu entry `Administration/Management -> Users -> Accounts` - now an admin user can change the password of every user.

This change consists of putting in read-only the password change fields for the users of type LDAP when the *LDAP authentication* is enabled in the configuration window.

An informative message explaining why the password fields are disabled must be given. For instance: *Password cannot be managed for LDAP users because LDAP authentication is being used*.

***Change 3***

In the window to manage users for admin users - top menu entry `Administration/Management -> Users -> Accounts` you are able to change the roles and the profiles of the users independently of the type of users.

However, the two parts related to permissions in the edition window (roles and profiles) are needed to be configured in read-only mode if two conditions are fulfilled:

-   If the user is of type LDAP.
-   If the Use LDAP roles is activated.

An informative message must be given to the user if the roles and profiles are disabled (read-only). For instance: *Roles and profiles of LDAP users cannot be managed because LDAP roles are being used*.

###  User stories

-   [ItEr74S09LdapAuhentication](LibrePlan_ItEr74S09LdapAuhentication)
-   [ItEr76S12LdapAuhentication](LibrePlan_ItEr76S12LdapAuhentication)

###  Tasks in this story

| [Tasks](LibrePlan_AnA04S06LdapAuthentication?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA04S06LdapAuthentication?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA04S06LdapAuthentication?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA04S06LdapAuthentication?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA04S06LdapAuthentication?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA04S06LdapAuthentication?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA04S06LdapAuthentication?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA04S06LdapAuthentication?sortcol=7;table=2;up=0#sorted_table "Sort by this column")                    | [Start Date](LibrePlan_AnA04S06LdapAuthentication?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA04S06LdapAuthentication?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA04S06LdapAuthentication?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Task                                                                                                    | 20                                                                                                    | 29                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [Develope/configure handler for LDAP authentication](LibrePlan_AnA04S06LdapAuthentication#TasK1)                               | 13/05/2011                                                                                                   | 20/05/2011                                                                                                     | 20/05/2011                                                                                                  |
| Task                                                                                                    | 20                                                                                                    | 20                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [Interface for configuring the the LDAP connection and authentication parameters.](LibrePlan_AnA04S06LdapAuthentication#TasK2) |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 16                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [Develope a composite handler LDAP/Database](LibrePlan_AnA04S06LdapAuthentication#TasK3)                                       |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 12                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [LDAP import of users](LibrePlan_AnA04S06LdapAuthentication#TasK4)                                                             |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 10                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [Support for two types of users](LibrePlan_AnA04S06LdapAuthentication#TasK5)                                                   |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 20                                                                                                    | 20                                                                                                      | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [Match the LDAP roles with the LibrePlan permissions](LibrePlan_AnA04S06LdapAuthentication#TasK6)                              |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 7                                                                                                     | 7                                                                                                       | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                                   | [Do compatible the change password and user roles administration with LDAP users.](LibrePlan_AnA04S06LdapAuthentication#TasK7) |                                                                                                              |                                                                                                                |                                                                                                             |

###  Total Hours in this Story

| [User](LibrePlan_AnA04S06LdapAuthentication?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA04S06LdapAuthentication?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA04S06LdapAuthentication?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA04S06LdapAuthentication?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [IgnacioDiaz](Main_IgnacioDiaz) [CristinaAlvarino](Main_CristinaAlvarino)                              | 114                                                                                                                  | 0                                                                                                                    | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                     |
| Total                                                                                                  | 114                                                                                                                  | 0                                                                                                                    | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                     |

------------------------------------------------------------------------

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_AnA04S06LdapAuthentication#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_AnA04S06LdapAuthentication#)

| [I](LibrePlan_AnA04S06LdapAuthentication?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_AnA04S06LdapAuthentication?sortcol=1;table=4;up=0#sorted_table "Sort by this column")                            | [Action](LibrePlan_AnA04S06LdapAuthentication?sortcol=2;table=4;up=0#sorted_table "Sort by this column")                                                                           |  [Size](LibrePlan_AnA04S06LdapAuthentication?sortcol=3;table=4;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_AnA04S06LdapAuthentication?sortcol=4;table=4;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_AnA04S06LdapAuthentication?sortcol=5;table=4;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_AnA04S06LdapAuthentication?sortcol=6;table=4;up=0#sorted_table "Sort by this column") |
|:---------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
|                         ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                        | [ActivityDiagram\_LDAP\_NavalPlan.png](/twiki/pub/LibrePlan/AnA04S06LdapAuthentication/ActivityDiagram_LDAP_NavalPlan.png)              | [manage](/twiki/bin/attach/LibrePlan/AnA04S06LdapAuthentication?filename=ActivityDiagram_LDAP_NavalPlan.png;revInfo=1 "change, update, previous revisions, move, delete...")       |                                                                                                  34.0 K| 12 May 2011 - 14:57                                                                                    | [JavierMoran](Main_JavierMoran)                                                                       | LDAP authentication actividy diagram                                                                      |
|                        ![else](/twiki/pub/TWiki/TWikiDocGraphics/else.gif)xmi                       | [ActivityDiagram\_LDAP\_NavalPlan.xmi](/twiki/pub/LibrePlan/AnA04S06LdapAuthentication/ActivityDiagram_LDAP_NavalPlan.xmi)              | [manage](/twiki/bin/attach/LibrePlan/AnA04S06LdapAuthentication?filename=ActivityDiagram_LDAP_NavalPlan.xmi;revInfo=1 "change, update, previous revisions, move, delete...")       |                                                                                                  28.3 K| 12 May 2011 - 14:56                                                                                    | [JavierMoran](Main_JavierMoran)                                                                       | LDAP authentication activity diagram - Umbrello                                                           |
|                         ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                        | [Activity\_Diagram\_LDAP\_Authentication.png](/twiki/pub/LibrePlan/AnA04S06LdapAuthentication/Activity_Diagram_LDAP_Authentication.png) | [manage](/twiki/bin/attach/LibrePlan/AnA04S06LdapAuthentication?filename=Activity_Diagram_LDAP_Authentication.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                                  34.8 K| 24 May 2011 - 10:34                                                                                    | [IgnacioDiaz](Main_IgnacioDiaz)                                                                       | LDAP authentication activity diagram                                                                      |
