[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr69S07PrintingSupportItEr68S08](LibrePlan_ItEr69S07PrintingSupportItEr68S08 "Topic revision: 11 (26 Nov 2012 - 12:18:04)") (26 Nov 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr69S07PrintingSupportItEr68S08?t=1520343656 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr69S07PrintingSupportItEr68S08 "Attach an image or document to this topic")  

 [ItEr69S07PrintingSupportItEr68S08](LibrePlan_ItEr69S07PrintingSupportItEr68S08)
=================================================================================

|                        |                                                                                  |
|------------------------|----------------------------------------------------------------------------------|
| Story summary          | Printing support                                                                 |
| Iteration              | [ItEr69week04To05](LibrePlan_ItEr69week04To05)                                   |
| FEA                    | [ItEr69S07PrintingSupportItEr68S08](LibrePlan_ItEr69S07PrintingSupportItEr68S08) |
| Story Lead             | [ItEr68S08PrintingSupport](LibrePlan_ItEr68S08PrintingSupport)                   |
| Next Story             |                                                                                  |
| Passed acceptance test | No                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Some JavaScript problems detected while running Xan's script.

-   timeline:

        ** Message: console message: http://localhost:8080/navalplanner-webapp/zkau/web/_zv10031815/_zcb/js/ext/timeline/api/scripts/util/graphics.js;jsessionid=1dnrqrvcj84ge @2: TypeError: Result of expression 'Timeline.Platform.browser' [undefined] is not an object.

&nbsp;

-   timeplot:

        ** Message: console message: http://localhost:8080/navalplanner-webapp/zkau/web/_zv10031815/_zcb/js/ext/timeplot/api/scripts/sources.js;jsessionid=90x3v5pitgyq @1: TypeError: Result of expression 'Timeline.DefaultEventSource' [undefined] is not an object.

        ** Message: console message: http://localhost:8080/navalplanner-webapp/zkau/web/_zv10031815/_zcb/js/ext/timeplot/api/scripts/processor.js;jsessionid=90x3v5pitgyq @1: TypeError: Result of expression 'Timeplot.DataSource' [undefined] is not an object.

I've just checked that Xan's script is asily compilable in Debian 6, Ubuntu 10.04 and Ubunut 10.10. So it could be a possible solution if we add the missing functionalities on it.

-- [ManuelRego](Main_ManuelRego) - 24 Jan 2011

Trying to create a JavaScript event when long operations finish in order to connect script to this event.

I modified `MultipleTabsPlannerController.java` to add the next lines at the end of `doAction()` inside `showWithFeedback()`:

    var onLongOperationFinish = new YAHOO.util.CustomEvent('long-operation-finish);
    onLongOperationFinishonMenuCollapse.fire();

Finally, it seems that there's some pending API to be implemented in WebKitGTK+, so maybe adding a delay is an easier solution right now.

I've modified Xan's script in order to receive different parameters and allow to specify a CSS file to be applied before taken the photo.

-- [ManuelRego](Main_ManuelRego) - 01 Feb 2011

Working wiht Xan's script. I've added timeout and it works with a simple HTML with JavaScript that hides some text after a seconds.

The script has worked during this morning several times printing a proper Gantt. But other times it shows just a blue image with logo in the top. Something is failing here.

Script is already integrated in LibrePlan for testing purposes, but the problem with blue image is still present.

-- [ManuelRego](Main_ManuelRego) - 03 Feb 2011

Script seems to work sometimes, so I've prepared Debian package and uploaded code to [gitorious](http://gitorious.org/wk2img) in order that the rest of the team could test it if they wish. For example [it worked in my last attempt](http://people.igalia.com/mrego/wk2img/navalplan.png).

Also Debian package for `wk2img`: [wk2img\_0.0.1-1\_amd64.deb](http://people.igalia.com/mrego/wk2img/wk2img_0.0.1-1_amd64.deb) & [wk2img\_0.0.1-1\_i386.deb](http://people.igalia.com/mrego/wk2img/wk2img_0.0.1-1_i386.deb)

Finally, I created a remote branch with printing using `wk2img`: <https://github.com/Igalia/libreplan/tree/printing-wk2img>

-- [ManuelRego](Main_ManuelRego) - 04 Feb 2011

Re-build Debian packages and tested in several distributions (Squeeze, Lucid & Maverick) and architectures (i386 & amd64).

[Sent mail](https://sourceforge.net/mailarchive/forum.php?thread_name=20110205192404.6ae1e7e3%40erizana&forum_name=navalplan-devel) with explanation of printing status.

-- [ManuelRego](Main_ManuelRego) - 05 Feb 2011

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

| [Tasks](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                           | 20                                                                                                           | 23.5                                                                                                           | 0                                                                                                              | Low                                                                                                           | [JavierMoran](Main_JavierMoran)                                                                                   | [ManuelRego](Main_ManuelRego)                                                                                      | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                                |                                                                                                                     |                                                                                                                       |                                                                                                                    |

###  Total Hours in this Story

| [User](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr69S07PrintingSupportItEr68S08?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                                 | 23.5                                                                                                                        | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |
| Total                                                                                                         | 23.5                                                                                                                        | 0                                                                                                                           | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                            |

------------------------------------------------------------------------
