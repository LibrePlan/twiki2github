[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA07S03PrintingSupport](LibrePlan_AnA07S03PrintingSupport "Topic revision: 11 (24 Jun 2011 - 18:04:25)") (24 Jun 2011, [JavierMoran](Main_JavierMoran))[Edit](LibrePlan_AnA07S03PrintingSupport?t=1520344042 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA07S03PrintingSupport "Attach an image or document to this topic")  

 [AnA07S03PrintingSupport](LibrePlan_AnA07S03PrintingSupport)
=============================================================

|                        |                                                              |
|------------------------|--------------------------------------------------------------|
| Story summary          | Printing support                                             |
| Iteration              | [AnA07PlanningWindow](LibrePlan_AnA07PlanningWindow)         |
| FEA                    | [AnA07S03PrintingSupport](LibrePlan_AnA07S03PrintingSupport) |
| Story Lead             |                                                              |
| Next Story             |                                                              |
| Passed acceptance test | No                                                           |

###  Tasks

####  Improve printing support

Currently we have 3 different problems in printing:

-   Sometimes it returns a blank screen. We don't know why.
-   Others it returns "Changing perspective". This happens because of the render hasn't finished.
-   Sometimes CutyCapt doesn't generate the image or PDF so the URL is not accessible.

        gcc -o photo photo.c `pkg-config --cflags --libs webkit-1.0`

Possible solutions:

-   Fix current problems with CutyCapt.
-   Try wkhtmltopdf which have a more active development.
-   Try a script by Xan that we'll give us the full control for this part (<http://pastebin.com/m3ba4e165>).

####  Include filter options in printing

Now there are two visualization options of the Gantt for a project which are not being taken into account. These are:

-   The filter of the Gantt. If it is being applied a filter to the Gantt it is not being taken into account and because of this, there is not any way to print the result of filtering a Gantt.
-   Show only tasks. If you want to print the tasks avoiding the containers now this is not possible.

So, this task is to allow the two elements just cited. It will be done adding to the pop-up of window preferences two more options:

-   Include filtering values of screen.
-   Show only tasks.

###  User stories

-   [ItEr68S08PrintingSupport](LibrePlan_ItEr68S08PrintingSupport)
-   [ItEr69S07PrintingSupportItEr68S08](LibrePlan_ItEr69S07PrintingSupportItEr68S08)
-   [ItEr70S06PrintingSupportItEr69S07](LibrePlan_ItEr70S06PrintingSupportItEr69S07)
-   [ItEr72S05PrintingSupportItEr70S06](LibrePlan_ItEr72S05PrintingSupportItEr70S06)
-   [ItEr74S05PrintingSupportItEr73S05](LibrePlan_ItEr74S05PrintingSupportItEr73S05)
-   [ItEr75S10PrintingSupportItEr74S05](LibrePlan_ItEr75S10PrintingSupportItEr74S05)

| [Tasks](LibrePlan_AnA07S03PrintingSupport?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA07S03PrintingSupport?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA07S03PrintingSupport?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA07S03PrintingSupport?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA07S03PrintingSupport?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA07S03PrintingSupport?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA07S03PrintingSupport?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA07S03PrintingSupport?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_AnA07S03PrintingSupport?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA07S03PrintingSupport?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA07S03PrintingSupport?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Task                                                                                                 | 80                                                                                                 | 64                                                                                                   | 16                                                                                                   | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         | [ManuelRego](Main_ManuelRego)                                                                            | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                      |                                                                                                           |                                                                                                             |                                                                                                          |
| Task                                                                                                 | 30                                                                                                 | 22                                                                                                   | 8                                                                                                    | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         | [LorenzoTilve](Main_LorenzoTilve)                                                                        | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                      |                                                                                                           |                                                                                                             |                                                                                                          |
| Task                                                                                                 | 20                                                                                                 | 0                                                                                                    | 20                                                                                                   | Low                                                                                                 | [JavierMoran](Main_JavierMoran)                                                                         |                                                                                                          | [Include filter options in printing](LibrePlan_AnA07S03PrintingSupport#TasK2)                            |                                                                                                           |                                                                                                             |                                                                                                          |

###  Total Hours in this Story

| [User](LibrePlan_AnA07S03PrintingSupport?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_AnA07S03PrintingSupport?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_AnA07S03PrintingSupport?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_AnA07S03PrintingSupport?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                       | 64                                                                                                                | 0                                                                                                                 | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                  |
| [LorenzoTilve](Main_LorenzoTilve)                                                                   | 22                                                                                                                | 0                                                                                                                 | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                  |
|                                                                                                     | 0                                                                                                                 | 0                                                                                                                 | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                   |
| Total                                                                                               | 86                                                                                                                | 0                                                                                                                 | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                  |

------------------------------------------------------------------------
