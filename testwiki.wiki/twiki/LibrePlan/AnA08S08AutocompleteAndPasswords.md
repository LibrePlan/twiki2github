[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA08S08AutocompleteAndPasswords](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords "Topic revision: 10 (20 Aug 2012 - 09:52:45)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA08S08AutocompleteAndPasswords?t=1520337844 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S08AutocompleteAndPasswords "Attach an image or document to this topic")

 [AnA08S08AutocompleteAndPasswords](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Autocomplete and passwords                                                                     |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)                                     |
| FEA                    | [AnA08S08AutocompleteAndPasswords](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

###  Tasks



####  Introduce warning change admin password

This task is to disable the autocomplete login and password with de pair admin/admin in the login screen.

The steps to change this situation is the following:

-   Introduce in the entity `Configuration` a field called `changedDefaultAdminPassword` with *FALSE* default value.
-   On doing login it will be implemented a procedure in which it will be checked if the configuration field `changeDefaultAdminPassword` is *TRUE* or *FALSE*.
    -   If the value is *TRUE*, then nothing is done.
    -   If the value is *FALSE*, the in the main layout will be added the following message with a suitable style (ask for it).

    The admin account default password was not changed ( click here ).

It is needed to add a link in the work *here* to the edition of the user **admin**

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) This option (`changedDefaultAdminPassword`) will not be managed through web interface.



####  Removal of warning of the need to change admin password

This task consists of saving in the field `changedDefaultAdminPassword` with *TRUE* default value when the following conditions happen:

-   User is trying to store de data for the user **admin**.
-   The new value which is going to be stored for the password of the user **admin** is different from the string **admin**.
-   The current value for the field `changedDefaultAdminPassword` is *TRUE*.



####  Add information in user list

In [LibrePlan](/twiki/LibrePlan/LibrePlan) there is a role which allows the users who have it to do all the operations under the menu option *Administration/Management*. They are regarded as *administrators*.

It is useful to know who users are administrators. To know it easily it is wanted to add a column to the accounts list which inform about this fact:

-   Column name: Is Administrator
-   Possible values: Yes/No



####  Warnings about need of password change for acounts user, wsreader, wswriter

It is wanted to add 3 fields in the entity `Configuration` to control if the user changed passwords for users *user*, *wsreader* or *wswriter*. Field will be:

-   **changedDefaultUserPassword**
-   **changedDefaultWsreaderPassword**
-   **changedDefaultWswriterPassword**

The three fields will have to be created with default `FALSE` value.

The fields will be saved from the account edition page if the next conditions are satisfied:

-   If it is being edited the account **user** and it is introduced a new password different from the string **user**. In this case it will be saved in the field **changedDefaultUserPassword** the value `TRUE`.
-   If it is being edited the account **wsreader** and it is introduced a new password different from the string **wsreader**. In this case it will be saved in the field **changedDefaultUserPassword** the value `TRUE`.
-   If it is being edited the account **wswriter** and it is introduced a new password different from the string **wswriter**. In this case it will be saved in the field **changedDefaultUserPassword** the value `TRUE`.

Finally, it will be needed to modify the accounts list in order to include new information in the **Actions** column for the rows linked with the accounts **user**, **admin**, **wsreader** and **wswriter**. If one of the those users have the associated field `changedDefaultYYYPassword` to `FALSE` then the following message will be displayed:

    Default password not changed

The message above will be displayed in a warning style. As for the appropiate design style.



####  Introduce warning for user other default users in layout

This task consists of displaying a warning message in the main layout, in the place where the warning for not having changed the password for the **admin** (***warning 1***) is.

This warning message will only be displayed if the ***warning 1*** is not showed, i.e., if the field **changedDefaultAdminPassword** is set to `TRUE`.

The message will be:

      [user][wswriter][wsreader] default password were not changed.

They will appear in the list only the account(s) which has(have) the associated **changeDefaultYYYPassword** set to `FALSE`. Each of the accounts names will be a link to the edition of that account.



####  Compiling option to disable the warning changing default admin password

It is wanted to have the possibility to compile the application with all the warning subsystem of the previous tasks disabled. The steps to implement this feature will be:

-   Use a maven property in the *pom.xml* file to allow the user disable the warning for default passwords subsystem. Requirements:
    -   Name: defaultPasswordsControl
    -   Possible values: **TRUE** or **FALSE**
    -   Value by default in the *pom.xml*: **TRUE**
-   That value could be disabled from Maven: `mvn -Ddefault.passwordsControl=false`
-   That value will be used in Spring files to initialize the value of the property of a singleton `Configuration` class.
-   Modify the tasks above to avoid the warning messages in the main layouts, in the accounts list and the mechanism to save the values of the **changeDefaultXXXPassword** fields.

###  User stories

-   [ItEr69S06AutocompleteAndPasswords](/twiki/LibrePlan/ItEr69S06AutocompleteAndPasswords)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 4                                                                                                                                                               | 4                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                     | [Introduce warning change admin password](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords#TasK0)                                                           |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 4                                                                                                                                                               | 5                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                     | [Removal of warning of the need to change admin password](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords#TasK1)                                           |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 2                                                                                                                                                               | 2                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                     | [Add information in user list](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords#TasK2)                                                                      |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 4                                                                                                                                                               | 3                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                     | [Warnings about need of password change for acounts user, wsreader, wswriter](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords#TasK3)                       |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 3                                                                                                                                                               | 4                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                     | [Introduce warning for user other default users in layout](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords#TasK4)                                          |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 5                                                                                                                                                               | 5                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                     | [Compiling option to disable the warning changing default admin password](/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords#TasK5)                           |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                | 23                                                                                                                                                                             | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |
| Total                                                                                                                                                            | 23                                                                                                                                                                             | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=1;table=4;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=2;table=4;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S08AutocompleteAndPasswords?sortcol=3;table=4;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [SusanaMontes](/twiki/Main/SusanaMontes)                                                                                                                | 23                                                                                                                                                                             | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |
| Total                                                                                                                                                            | 23                                                                                                                                                                             | 0                                                                                                                                                                              | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                               |

------------------------------------------------------------------------
