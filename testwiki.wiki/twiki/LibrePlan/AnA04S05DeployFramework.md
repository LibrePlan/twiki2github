[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA04S05DeployFramework](LibrePlan_AnA04S05DeployFramework "Topic revision: 10 (20 Aug 2012 - 09:52:44)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA04S05DeployFramework?t=1520344035 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA04S05DeployFramework "Attach an image or document to this topic")  

 [AnA04S05DeployFramework](LibrePlan_AnA04S05DeployFramework)
=============================================================

|                        |                                                              |
|------------------------|--------------------------------------------------------------|
| Story summary          | Deployment Framework                                         |
| Iteration              | [AnA04Architecture](LibrePlan_AnA04Architecture)             |
| FEA                    | [AnA04S05DeployFramework](LibrePlan_AnA04S05DeployFramework) |
| Story Lead             |                                                              |
| Next Story             |                                                              |
| Passed acceptance test | No                                                           |

###  Tasks

The purpose of these tasks is to have a better installation of the application.

####  Servlet container installation

Currently the servlet container that it is being used in the Debian packages and in the deployment of the application is Tomcat 6.

In the development environment it is being used Jetty.

This task consist of studying if it is better to choose Jetty over Tomcat assessing the variables which may have an influence over the application. The most important one is performance (in number of requests/second it is able to serve and in terms of the latency of each request).

It is important to configure the following things:

-   Memory configuration for the Tomcat. Now in the installations there are out of memory errors after some time with the application running.
-   Configure the logs. Decide what log implementation is going to be used. Review how the logging is done in [LibrePlan](LibrePlan_LibrePlan) and configure properly the levels of logging. It is possible to suggest some change if needed.

####  Set on second-level hibernate cache

Currently in the application is the second level cache configured for some entities and relationship. However, it is set off.

Configuration:

-   [Documentation\#Hibernate\_Second\_Level\_Cache](LibrePlan_Documentation#Hibernate_Second_Level_Cache)
-   [PerformanceTuning](LibrePlan_PerformanceTuning)

Study if other Hibernate optimizations can be applied or are worth. For instance:

-   Use second level cache for some queries.
-   Configure the batch size.

####  Stress load tests for the application

The performance of the application has to variables that have to be taken into account:

-   The performance for single user in certain screens. These screens are the resource load screen and project planning screens (project details WBS, gantt window and advance allocation window). The resource load screen performance depends on the amount of projects in the application and the performance of the project planning screens depend on the size of the project. More size, less performance.
-   The performance for number of simultaneous users connected to the application.

It is wanted to analyse both variable and to have an idea of the hardware requirements that we have to say or recommend to do a LibrePlan deployment. Questions needed to ask are:

-   What is the number of simultaneous users who can connect to [LibrePlan](LibrePlan_LibrePlan) and use it fluenty in CRUD screens and medium size projects ?
-   What are the number of projects for which the resource load window has a reasonable load time ?
-   What is the size of a project for which a small of users connected to the server has a reosonable response time?

####  Backups, reloading tomcat, mechanism to uload data for the application

For real environments it is needed to configure several things like:

-   A way to do backups daily.
-   If the thing of having tomcat unsteady create a script which configures the tomcat restarting after certain periods of time.
-   It is needed to design and analyse to unload data before a date. In this case this data will be backed and unloaded from the running database of the application and the app would have to be configure to avoid plan anything in the periods that have been closed and unloaded. For future.

####  Debian packages, Rpm packages

This task consists of having better debian packages for the application in one side. On the other side, it is wanted to have rpm packages too.

###  User stories

-   [ItEr74S08DeployFramework](LibrePlan_ItEr74S08DeployFramework)
-   [ItEr75S19DeployFrameworkItEr74S08](LibrePlan_ItEr75S19DeployFrameworkItEr74S08)

###  Tasks in this story

| [Tasks](LibrePlan_AnA04S05DeployFramework?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA04S05DeployFramework?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA04S05DeployFramework?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA04S05DeployFramework?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA04S05DeployFramework?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA04S05DeployFramework?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA04S05DeployFramework?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA04S05DeployFramework?sortcol=7;table=2;up=0#sorted_table "Sort by this column")          | [Start Date](LibrePlan_AnA04S05DeployFramework?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA04S05DeployFramework?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA04S05DeployFramework?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Task                                                                                                 | 35                                                                                                 | 0                                                                                                    | 35                                                                                                   | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         | [OscarGonzalez](Main_OscarGonzalez)                                                                      | [Servlet container installation](LibrePlan_AnA04S05DeployFramework#TasK1)                                         |                                                                                                           |                                                                                                             |                                                                                                          |
| Task                                                                                                 | 20                                                                                                 | 0                                                                                                    | 20                                                                                                   | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         | [NachoBarrientos](Main_NachoBarrientos)                                                                  | [Set on second-level hibernate cache](LibrePlan_AnA04S05DeployFramework#TasK2)                                    | 0                                                                                                         | 0                                                                                                           | 0                                                                                                        |
| Task                                                                                                 | 70                                                                                                 | 35                                                                                                   | 0                                                                                                    | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         | [NachoBarrientos](Main_NachoBarrientos)                                                                  | [Stress load tests for the application](LibrePlan_AnA04S05DeployFramework#TasK3)                                  | 0                                                                                                         | 0                                                                                                           | 0                                                                                                        |
| Task                                                                                                 | 100                                                                                                | 0                                                                                                    | 100                                                                                                  | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         |                                                                                                          | [Backups, reloading tomcat, mechanism to uload data for the application](LibrePlan_AnA04S05DeployFramework#TasK4) | 0                                                                                                         | 0                                                                                                           | 0                                                                                                        |
| Task                                                                                                 | 100                                                                                                | 0                                                                                                    | 100                                                                                                  | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         |                                                                                                          | [Debian packages, Rpm packages](LibrePlan_AnA04S05DeployFramework#TasK5)                                          | 0                                                                                                         | 0                                                                                                           | 0                                                                                                        |

###  Total Hours in this Story

| [User](LibrePlan_AnA04S05DeployFramework?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA04S05DeployFramework?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA04S05DeployFramework?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA04S05DeployFramework?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
|                                                                                                     | 0                                                                                                                 | 0                                                                                                                 | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                   |
| [OscarGonzalez](Main_OscarGonzalez)                                                                 | 0                                                                                                                 | 0                                                                                                                 | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                   |
| [NachoBarrientos](Main_NachoBarrientos)                                                             | 35                                                                                                                | 0                                                                                                                 | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                  |
| Total                                                                                               | 35                                                                                                                | 0                                                                                                                 | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                  |

------------------------------------------------------------------------
