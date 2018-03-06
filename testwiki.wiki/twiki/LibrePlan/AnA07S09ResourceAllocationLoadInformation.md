[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA07S09ResourceAllocationLoadInformation](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation "Topic revision: 1 (13 Oct 2012 - 10:16:03)") (13 Oct 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA07S09ResourceAllocationLoadInformation?t=1520337841 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S09ResourceAllocationLoadInformation "Attach an image or document to this topic")

 [AnA07S09ResourceAllocationLoadInformation](/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation)
====================================================================================================================================================================



|                        |                                                                                                                  |
|------------------------|------------------------------------------------------------------------------------------------------------------|
| Story summary          | Calculate and represent load status of resources in resource allocation                                          |
| Iteration              | [AnA07PlanningWindow](/twiki/LibrePlan/AnA07PlanningWindow)                                             |
| FEA                    | [AnA07S09ResourceAllocationLoadInformation](/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation) |
| Story Lead             |                                                                                                                  |
| Next Story             |                                                                                                                  |
| Passed acceptance test | No                                                                                                               |

###  Tasks

This analysis story contains a set of task that have the purpose of providing the user with information about the load status of the resources on doing the resource allocation. Now, there is not any type of information that can be displayed in the resource allocation window. To know the resource load status the user needs to go to the resource allocation always.



####  Calculate load ratios in the advanced search of the resource allocation

This first task consists of calculating the load ratios of the resources that are being found using the **Advanced Search** option in the resource allocation pop-up.

There are two load ratios that want to be calculated:

-   **\*Overload ratio\***. Overload ratio is calculated as `overload/(load+overload)`. It calculates how much overtime has been allocated to a resource.
-   **\*Availability ratio\***. The availability ratio is calculated as `min(0, 1-load/capacity)`. It calculates how much free time has a resource available to be allocated.

Both the *overload ratio* and the *availability ratio* are calculated over a period of time. So, this is the case for this task to. They will be calculated between a start date and an end date.

The interface for representing these load ratios will have the following characteristics:

-   There will be two dateboxes to choose the start date and the end date to calculate the *overload ratio* and the *availability ratio*. These dateboxes will be initialized to the following values by default:
    -   Start filtering date: 1 month before the task start date. The task is the one that is being allocated.
    -   End filtering date: 1 month after the task end date.
-   If the user changes the start filtering date or the end filtering date a recalculation is launched so that the ratios are always the correct ones according to the period defined by the dateboxes.
-   The validations that will be implemented in the filtering dateboxes are the next ones:
    -   They cannot be empty.
    -   The start filtering datebox must have a date before the end filtering datebox.
-   The resource listing listbox currently has one column with the resource name. This listbox is wanted to be extended with two more columns:
    -   **\*Availability\***. This column will contain the availability for each found resource in the period specified by the filters.
    -   **\*Overload ratio\***. This column will contain the overload for each found resource in the period specified by the filters.

It will be done a graphical representation of the availability ratio. It will consist of representing each availability value with a ***progress bar*** with values between 0% and 100%.

-   An availability of 0% informs that in the filtering period all the capacity specified by the resource calendar is already allocated.
-   An availability of 100% informs that in the filtering period all the capacity specified by the resource calendar is free.

To allow an easy and prompt identification of the availability status of a resource the ***progress bar*** will have a color code:

-   ***Good availability ratio***. A value &gt; 50% is regarded a good availability ratio. The resource is a good candidate to be allocated. The progress bar will be painted in **\*green\***.
-   ***Intermediate availability ratio***. A value &gt; 25% and &lt; 50% is regarded an intermediate availability ratio. The progress bar will be yellow.
-   ***Bad availability ratio***. A value &gt; 0% and &lt; 25% is regarded a bad availability ratio. The bar is painted in red.

With regard to the ***overtime ratio*** it will be highlighted with a warning icon if it has a different value from zero. An ***overtime ratio*** different than zero is always bad. It contains a situation that is a potential case to solve.

It will be appraised at the moment of the implementation if it is possible to merge the ratios calculation with the memory status or not.

-   A basic implementation can take into account only the allocations saved in the database.
-   An advanced implementation could merge the load gathered in the database with the load modifications made in memory by the planning state not persisted.

###  User stories

-   [ItEr77S10ResourceAllocationLoadInformation](/twiki/LibrePlan/ItEr77S10ResourceAllocationLoadInformation)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                       | 40                                                                                                                                                                       | 0                                                                                                                                                                          | 40                                                                                                                                                                         | Low                                                                                                                                                                       | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                                 | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                                | [Calculate load ratios in the advanced search of the resource allocation](/twiki/LibrePlan/AnA07S09ResourceAllocationLoadInformation#TasK1)                           |                                                                                                                                                                                 |                                                                                                                                                                                   |                                                                                                                                                                                |


