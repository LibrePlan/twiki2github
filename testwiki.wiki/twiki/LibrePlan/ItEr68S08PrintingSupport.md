[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr68S08PrintingSupport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport "Topic revision: 5 (24 Jan 2011 - 16:24:05)") (24 Jan 2011, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr68S08PrintingSupport?t=1520337898 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr68S08PrintingSupport "Attach an image or document to this topic")

 [ItEr68S08PrintingSupport](/twiki/LibrePlan/ItEr68S08PrintingSupport)
==========================================================================================================================



|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Printing support                                                               |
| Iteration              | [ItEr68week02To03](/twiki/LibrePlan/ItEr68week02To03)                 |
| FEA                    | [ItEr68S08PrintingSupport](/twiki/LibrePlan/ItEr68S08PrintingSupport) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Tested wkhtmltopdf tool but it's not working properly when adding a delay (`--javascript-delay 10000`). I'm not able to get a Gantt printed from command line.

Also compiled and tested Xan's script, but it's not working right now (even for simple pages, I'm not talking about a Gantt). It seems like an infinite loop or something like that.

-- [ManuelRego](/twiki/Main/ManuelRego) - 20 Jan 2011

Xan's script finally seems to work (not for igalia.com but yes for other webpages). In order to try it you need to compile with the following command.

    gcc -o photo photo.c `pkg-config --cflags --libs webkit-1.0`

The script lacks 2 features:

-   Delay parameter in order to wait some time before take the photo.
-   CSS parameter to pass a stylesheet that could modify the final result.

Doing more tests and trying to find out some JavaScript problems.

-- [ManuelRego](/twiki/Main/ManuelRego) - 24 Jan 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                      | 20                                                                                                                                                      | 12.75                                                                                                                                                     | 0                                                                                                                                                         | Low                                                                                                                                                      | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                              | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                 | [Improve printing support](/twiki/LibrePlan/AnA07S03PrintingSupport#TasK1)                                                                           |                                                                                                                                                                |                                                                                                                                                                  |                                                                                                                                                               |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr68S08PrintingSupport?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                            | 12.75                                                                                                                                                                  | 0                                                                                                                                                                      | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                       |
| Total                                                                                                                                                    | 12.75                                                                                                                                                                  | 0                                                                                                                                                                      | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                       |

------------------------------------------------------------------------
