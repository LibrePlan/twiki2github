[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA09S01CriteriaLoadRefinement](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement "Topic revision: 5 (07 Feb 2011 - 12:05:03)") (07 Feb 2011, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA09S01CriteriaLoadRefinement?t=1520337849 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA09S01CriteriaLoadRefinement "Attach an image or document to this topic")

 [AnA09S01CriteriaLoadRefinement](/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement)
============================================================================================================================================



|                        |                                                                                            |
|------------------------|--------------------------------------------------------------------------------------------|
| Story summary          | Resource load by criteria refinement                                                       |
| Iteration              | [AnA09ResourceLoadWindow](/twiki/LibrePlan/AnA09ResourceLoadWindow)               |
| FEA                    | [AnA09S01CriteriaLoadRefinement](/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement) |
| Story Lead             |                                                                                            |
| Next Story             |                                                                                            |
| Passed acceptance test | No                                                                                         |

###  Tasks



####  Include specific allocation load to criterion load analysis

This task is related to the resource load view filtered by criteria. In this case, now it is not included in the computed allocated hours the load because of the specific resource allocation.

So, the changes to introduce are the following:

-   Add a last second level per criterion called "specific allocations". This second level wil be an aggregation of all the specific allocations of the resources fulfulling the criterion.
-   The third level will be composed of all the specific allocations of the resources satisfying the criterion represented by the first level.

The query to get the specific allocations of the resources satisfying the criterion should follow the following guidelines:

-   Get the time axis which is being displayed in the resource load screen.
-   Get the resources which satisfy the criterion in any of the points of the time axis.
-   Get the resource allocations of those resources in the time period of the time axis.
-   Check that each in any of the points of the specific resource allocation the resource satifies the resource.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) About the guidelines, think of how to do the querys or these steps in the more effective way from performance point of view.

###  User stories

-   [ItEr69S10CriteriaLoadRefinement](/twiki/LibrePlan/ItEr69S10CriteriaLoadRefinement)
-   [ItEr70S08CriteriaLoadRefinementItEr69S10](/twiki/LibrePlan/ItEr70S08CriteriaLoadRefinementItEr69S10)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                            | 9.75                                                                                                                                                          | 4.75                                                                                                                                                            | 5                                                                                                                                                               | Low                                                                                                                                                            | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                    | [OscarGonzalez](/twiki/Main/OscarGonzalez)                                                                                                                 | [Include specific allocation load to criterion load analysis](/twiki/LibrePlan/AnA09S01CriteriaLoadRefinement#TasK1)                                       |                                                                                                                                                                      |                                                                                                                                                                        |                                                                                                                                                                     |


