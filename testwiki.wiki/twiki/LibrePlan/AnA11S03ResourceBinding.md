[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA11S03ResourceBinding](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding "Topic revision: 6 (10 May 2012 - 09:42:38)") (10 May 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA11S03ResourceBinding?t=1520337852 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA11S03ResourceBinding "Attach an image or document to this topic")

 [AnA11S03ResourceBinding](/twiki/LibrePlan/AnA11S03ResourceBinding)
=======================================================================================================================



|                        |                                                                              |
|------------------------|------------------------------------------------------------------------------|
| Story summary          | Resource Binding                                                             |
| Iteration              | [AnA11UsersModule](/twiki/LibrePlan/AnA11UsersModule)               |
| FEA                    | [AnA11S03ResourceBinding](/twiki/LibrePlan/AnA11S03ResourceBinding) |
| Story Lead             |                                                                              |
| Next Story             |                                                                              |
| Passed acceptance test | No                                                                           |

###  Tasks

The idea to bind a resource to a user is to offer a way to interact with the application from the point of view of a resource. In this way a resource could have a user bound which allowed him to take part and see the planning from his role of resource.

The fact of being a resource has influence in several operations:

-   A resource could track his time, and not the time devoted to other resources.
-   A resource could track expenses belonging to him.
-   A resource could view the status of the tasks that he has assigned.

In this point it is suggested how to do the link between a resource and a user. There are several ways to do this:

-   From the user administration window.
-   From the resource window

The second chosen is to to use the resource administration window as the entry point for this operation. The rationale behind this is that in the planning flow of operations the natural way to proceed is the next one:

-   You create a resource in LibrePlan to be planned.
-   At the moment of creating a resource the LibrePlan administrator could decide to create a user for that resource or to use one of the existing users.



####  Add relationship between and Worker and User

It will be needed to create a relationship between the entities `Worker` and `User` according to the next diagram.

![user\_resource\_binding\_class\_diagram.png](/twiki/pub/LibrePlan/AnA11S03ResourceBinding/user_resource_binding_class_diagram.png)

-   A worker can be bound to 0..1 user
-   A user can be bound to 0..1 user.

The one-to-one relationship can be travelled from both sides.

Only **non limiting** workers can be bound to users.



####  Adapt resource administration window

In the ***Personal data*** tab of the resource administration window there will a new area called ***Bound user***. In this area the following fields will be rendered:

-   3 radio buttons with the next options: *Not bound*, *Existing user* and *Create new user*
-   Depending on the option chosen the behavior will be different:
    -   ***Not bound***
        -   No more fields are needed
    -   ***Existing user***
        -   A bandbox search to look for the user to be bound. The format would be `login (first_name last_name)` or only `login` if `first_name` and `last_name` are empty
        -   A label to show the e-mail of the user
        -   A link to the user administration window (we should show a warning message about losing unsaved changes when clicking this link)
    -   ***Create new user***
        -   Several textfields to gather the minimum data to create a user. This minimum data will be: *Username*, *Password*, *Password confirmation* and *E-mail*.

If the user press on the save button, depending on the option chosen different things will happen:

-   ***Not bound***
    -   The resource will be not bound to any resource
-   ***Existing user***
    -   The resource will be bound to the corresponding user
    -   The fields *First name* and *Last name* of the user will be updated with the worker info
-   ***Create new user***
    -   The new user will be crated using the data from the text fields and also the *First name* and *Last name* from worker info
    -   After saving it'll be marked the option *Existing user* with the new user created as the one selected

If a worker is deleted and is possible to do this operation (the worker has not been assigned to any project yet), there could be 2 situations:

-   The resource is bound to a basic user (without *Administration* role): Then a confirm dialog will be shown asking if do you want to delete the user too.
-   The resource is bound to an administrator: Then the user will be unbound but not deleted.

**NOTE**: It is not suggested to delete these fields from the User because there will be users not bound to any resource and because we have these fields already in the database and maybe are being used in old LibrePlan deployments.



####  Adapt user administration window

It will be created a new area called: ***Bound resource***. It will have inside the following fields:

-   Label: *Has bound resource?* Values: Yes | No
-   A link to the resource administration window. This link will be rendered when the user has resource bound.
-   *Unbound button*. This button will remove the binding of the user with the resource after pressing the save button of the page. It will also delete the render of the link to the resource administration window.
    -   The unbound operation must not be cascaded to the `Worker`. This means that the worker will not be deleted in all the cases: When a `User` is deleted or when the unbound button is pressed in a user.

It will be needed also to modify the following things:

-   If a user is bound to the resource, the fields ***First name*** and ***Last name*** will be read-only in the user edition window.
-   In the user list will be added a column with the title ***Bound resources***. It will include the ***name (ID)*** if the user is bound to it.

If a user is deleted and it's bound to a worker:

-   Then a warning dialog will be shown notifying that the user will be unbound

###  User stories

-   [ItEr76S27ResourceBinding](/twiki/LibrePlan/ItEr76S27ResourceBinding)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                     | 3                                                                                                                                                      | 5                                                                                                                                                        | 0                                                                                                                                                        | Low                                                                                                                                                     | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                             | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                | [Add relationship between and Worker and User](/twiki/LibrePlan/AnA11S03ResourceBinding#TasK1)                                                      |                                                                                                                                                               |                                                                                                                                                                 |                                                                                                                                                              |
| Task                                                                                                                                                     | 21                                                                                                                                                     | 10                                                                                                                                                       | 0                                                                                                                                                        | Low                                                                                                                                                     | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                             | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                | [Adapt resource administration window](/twiki/LibrePlan/AnA11S03ResourceBinding#TasK2)                                                              |                                                                                                                                                               |                                                                                                                                                                 |                                                                                                                                                              |
| Task                                                                                                                                                     | 14                                                                                                                                                     | 6.5                                                                                                                                                      | 0                                                                                                                                                        | Low                                                                                                                                                     | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                             | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                | [Adapt user administration window](/twiki/LibrePlan/AnA11S03ResourceBinding#TasK3)                                                                  |                                                                                                                                                               |                                                                                                                                                                 |                                                                                                                                                              |

[![](/twiki/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](#) [![](/twiki/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](#)

| [I](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Action](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=2;table=3;up=0#sorted_table "Sort by this column")                      | [Size](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=3;table=3;up=0#sorted_table "Sort by this column") | [Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA11S03ResourceBinding?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![png](/twiki/TWiki/TWikiDocGraphics/png.gif)png                                                                                                 | [user\_resource\_binding\_class\_diagram.png](/twiki/pub/LibrePlan/AnA11S03ResourceBinding/user_resource_binding_class_diagram.png)                           | [manage](/twiki/bin/attach/LibrePlan/AnA11S03ResourceBinding?filename=user_resource_binding_class_diagram.png;revInfo=1 "change, update, previous revisions, move, delete...") | 3.1 K                                                                                                                                                   | 02 May 2012 - 16:39                                                                                                                                     | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                        |                                                                                                                                                            |


