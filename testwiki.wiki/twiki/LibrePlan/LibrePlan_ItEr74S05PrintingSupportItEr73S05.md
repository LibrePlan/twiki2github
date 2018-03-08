[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr74S05PrintingSupportItEr73S05](LibrePlan_ItEr74S05PrintingSupportItEr73S05 "Topic revision: 13 (20 Aug 2012 - 09:52:53)") (20 Aug 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr74S05PrintingSupportItEr73S05?t=1520343672 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr74S05PrintingSupportItEr73S05 "Attach an image or document to this topic")  

 [ItEr74S05PrintingSupportItEr73S05](LibrePlan_ItEr74S05PrintingSupportItEr73S05)
=================================================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Printing support                                                                 |
| Iteration              | [ItEr74week14To24](LibrePlan_ItEr74week14To24)                                   |
| FEA                    | [ItEr74S05PrintingSupportItEr73S05](LibrePlan_ItEr74S05PrintingSupportItEr73S05) |
| Story Lead             |                                                                                  |
| Next Story             |                                                                                  |
| Passed acceptance test | No                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

After cleaning the cache, when entering a project for first time usually some timeline related errors happen. For example one of these errors that can happen is: Timeline.Platform.browser undefined in graphics.js. This object is defined in platform.js.

How did this come to happen? timelineapi.js is the responsible of loading all the dependencies related with the chart. For this uses the technique described here: <http://yuiblog.com/blog/2008/07/22/non-blocking-scripts/> This typical technique for adding dependencies consists on adding new

    <script>

tags to head. This has the effect on most browsers of loading the scripts in parallel. Normally the scripts are loaded sequentially to avoid potential pitfalls. At least in Minefield 4.0b13pre the scripts are executed as soon as are received. In this case graphics.js happened to be received before platform.js causing the error.

Possible solutions: Merge timeline dependencies in one file. Include dependencies dinamically but wait for the depenencies to be loaded. Listening to some event produced when the load of the script is finished and then load the next one.

-- [OscarGonzalez](Main_OscarGonzalez) - 05 Apr 2011

Once the scripts are in the cache, it seems that this error is much harder to reproduce since the scripts are added in the correct order and are immediately available. In the case of printing, the cached files are not preserved among executions causing random errors due to race conditions.

-- [OscarGonzalez](Main_OscarGonzalez) - 05 Apr 2011

Finally all timeline dependencies are merged in one file, timeplot.js

-- [OscarGonzalez](Main_OscarGonzalez) - 10 Apr 2011

Now printing seems to work properly, anyway it would be great to avoid CutyCapt because of the X server needed.

The best solution would be gnome-web-photo, but it doesn't have a parameter to delay the photo. But reported and if we're lucky they would add it soon: <https://bugzilla.gnome.org/show_bug.cgi?id=647434>

-- [ManuelRego](Main_ManuelRego) - 11 Apr 2011

It seems that alternatives to CutyCapt also requires a X server, as I'm getting the following error trying to rum them in a server:

    Gtk-WARNING **: cannot open display:

So, for the moment we're going to go with **CutyCapt**.

-- [ManuelRego](Main_ManuelRego) - 09 May 2011

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story

| [Tasks](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                           | 20                                                                                                           | 29                                                                                                             | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [OscarGonzalez](Main_OscarGonzalez)                                                                                | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                                | 21/03/2011                                                                                                          | 03/04/2011                                                                                                            |                                                                                                                    |
| Task                                                                                                           | 20                                                                                                           | 0                                                                                                              | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [LorenzoTilve](Main_LorenzoTilve)                                                                                  | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                                | 21/03/2011                                                                                                          | 03/04/2011                                                                                                            |                                                                                                                    |
| Task                                                                                                           | 8                                                                                                            | 8                                                                                                              | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [ManuelRego](Main_ManuelRego)                                                                                      | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                                |                                                                                                                     |                                                                                                                       |                                                                                                                    |

###  Total Hours in this Story

| [User](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr74S05PrintingSupportItEr73S05?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [LorenzoTilve](Main_LorenzoTilve)                                                                             | 0                                                                                                                           | 0                                                                                                                           | ![DONE](/twiki/pub/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                             |
| [ManuelRego](Main_ManuelRego)                                                                                 | 8                                                                                                                           | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |
| [OscarGonzalez](Main_OscarGonzalez)                                                                           | 29                                                                                                                          | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |
| Total                                                                                                         | 37                                                                                                                          | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |

------------------------------------------------------------------------
