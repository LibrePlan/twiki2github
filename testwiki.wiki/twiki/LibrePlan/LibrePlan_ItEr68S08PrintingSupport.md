[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr68S08PrintingSupport](LibrePlan_ItEr68S08PrintingSupport "Topic revision: 5 (24 Jan 2011 - 16:24:05)") (24 Jan 2011, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr68S08PrintingSupport?t=1520343653 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr68S08PrintingSupport "Attach an image or document to this topic")  

 [ItEr68S08PrintingSupport](LibrePlan_ItEr68S08PrintingSupport)
===============================================================

|                        |                                                                |
|------------------------|----------------------------------------------------------------|
| Story summary          | Printing support                                               |
| Iteration              | [ItEr68week02To03](LibrePlan_ItEr68week02To03)                 |
| FEA                    | [ItEr68S08PrintingSupport](LibrePlan_ItEr68S08PrintingSupport) |
| Story Lead             |                                                                |
| Next Story             |                                                                |
| Passed acceptance test | No                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

Tested wkhtmltopdf tool but it's not working properly when adding a delay (`--javascript-delay 10000`). I'm not able to get a Gantt printed from command line.

Also compiled and tested Xan's script, but it's not working right now (even for simple pages, I'm not talking about a Gantt). It seems like an infinite loop or something like that.

-- [ManuelRego](Main_ManuelRego) - 20 Jan 2011

Xan's script finally seems to work (not for igalia.com but yes for other webpages). In order to try it you need to compile with the following command.

    gcc -o photo photo.c `pkg-config --cflags --libs webkit-1.0`

The script lacks 2 features:

-   Delay parameter in order to wait some time before take the photo.
-   CSS parameter to pass a stylesheet that could modify the final result.

Doing more tests and trying to find out some JavaScript problems.

-- [ManuelRego](Main_ManuelRego) - 24 Jan 2011

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

| [Tasks](LibrePlan_ItEr68S08PrintingSupport?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr68S08PrintingSupport?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr68S08PrintingSupport?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr68S08PrintingSupport?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr68S08PrintingSupport?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr68S08PrintingSupport?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr68S08PrintingSupport?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr68S08PrintingSupport?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr68S08PrintingSupport?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr68S08PrintingSupport?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr68S08PrintingSupport?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Task                                                                                                  | 20                                                                                                  | 12.75                                                                                                 | 0                                                                                                     | Low                                                                                                  | [JavierMoran](Main_JavierMoran)                                                                          | [ManuelRego](Main_ManuelRego)                                                                             | [Improve printing support](LibrePlan_AnA07S03PrintingSupport#TasK1)                                       |                                                                                                            |                                                                                                              |                                                                                                           |

###  Total Hours in this Story

| [User](LibrePlan_ItEr68S08PrintingSupport?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](LibrePlan_ItEr68S08PrintingSupport?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](LibrePlan_ItEr68S08PrintingSupport?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](LibrePlan_ItEr68S08PrintingSupport?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [ManuelRego](Main_ManuelRego)                                                                        | 12.75                                                                                                              | 0                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                   |
| Total                                                                                                | 12.75                                                                                                              | 0                                                                                                                  | ![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                   |

------------------------------------------------------------------------
