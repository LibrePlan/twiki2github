[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA08S01ScenarioVisibility](LibrePlan_AnA08S01ScenarioVisibility "Topic revision: 2 (20 Dec 2010 - 10:37:06)") (20 Dec 2010, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA08S01ScenarioVisibility?t=1520344046 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S01ScenarioVisibility "Attach an image or document to this topic")  

 [AnA08S01ScenarioVisibility](LibrePlan_AnA08S01ScenarioVisibility)
===================================================================

|                        |                                                                    |
|------------------------|--------------------------------------------------------------------|
| Story summary          | Scenario as configuration option                                   |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)                         |
| FEA                    | [AnA08S01ScenarioVisibility](LibrePlan_AnA08S01ScenarioVisibility) |
| Story Lead             |                                                                    |
| Next Story             |                                                                    |
| Passed acceptance test | No                                                                 |

###  Tasks

####  Configuration of scenario support

This task is to allow to the application administrators to configure the scenarios support as optional. So, if the option is disabled, the concept of scenarios will be transparent to the users.

So, the steps to implement this task are:

-   To include a boolean field in the `Configuration` entity called *scenarioSupport* to register the option.
-   Manage this parameter through the configuration screen.
-   It won't be possible to deactivate that option if there are scenarios created, apart from master.
-   If the *scenario support* option is deactivated then the following interface options will be removed:
    -   The menu section called **Scenarios**.
    -   The button to change scenario which is showed in the top area of the application.
-   By default the *scenarios support* option will be desabled. So, this option has to be created with default vale false.

###  User stories

-   [ItEr65S07ScenarioVisibility](LibrePlan_ItEr65S07ScenarioVisibility)

| [Tasks](LibrePlan_AnA08S01ScenarioVisibility?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA08S01ScenarioVisibility?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA08S01ScenarioVisibility?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA08S01ScenarioVisibility?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA08S01ScenarioVisibility?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA08S01ScenarioVisibility?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA08S01ScenarioVisibility?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA08S01ScenarioVisibility?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA08S01ScenarioVisibility?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA08S01ScenarioVisibility?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA08S01ScenarioVisibility?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Task                                                                                                    | 3                                                                                                     | 3                                                                                                       | 0                                                                                                       | Low                                                                                                    | [JavierMoran](Main_JavierMoran)                                                                            | [LorenzoTilve](Main_LorenzoTilve)                                                                           | [Configuration of scenario support](LibrePlan_AnA08S01ScenarioVisibility#TasK1)                             |                                                                                                              |                                                                                                                |                                                                                                             |
