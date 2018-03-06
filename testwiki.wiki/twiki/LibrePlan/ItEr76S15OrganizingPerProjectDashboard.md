[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S15OrganizingPerProjectDashboard](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard "Topic revision: 13 (01 Apr 2013 - 16:11:20)") (01 Apr 2013, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?t=1520337936 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S15OrganizingPerProjectDashboard "Attach an image or document to this topic")

 [ItEr76S15OrganizingPerProjectDashboard](/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard)
==============================================================================================================================================================



|                        |                                                                                                            |
|------------------------|------------------------------------------------------------------------------------------------------------|
| Story summary          | Organizing per project dashboard                                                                           |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                                             |
| FEA                    | [ItEr76S15OrganizingPerProjectDashboard](/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard) |
| Story Lead             |                                                                                                            |
| Next Story             |                                                                                                            |
| Passed acceptance test | No                                                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

-- [DiegoPino](/twiki/Main/DiegoPino) - 19 Apr 2012

I had some problems with my environment because I was using a different Maven plugin and it didn't work for compiling [LibrePlan](/twiki/LibrePlan/LibrePlan).

In the end I had to reinstall Eclipse and install the proper Maven for Eclipse plugin. After this, my Eclipse worked and I could deploy [LibrePlan](/twiki/LibrePlan/LibrePlan) from Eclipse.

I downloaded **jqPlot** and started reading the docs. I tried to include jqPlot in [LibrePlan](/twiki/LibrePlan/LibrePlan).

-- [DiegoPino](/twiki/Main/DiegoPino) - 20 Apr 2012

I kept on working trying to included jqPlot in [LibrePlan](/twiki/LibrePlan/LibrePlan). I first tried jqPlot standalone in a simple HTML page and later included in [LibrePlan](/twiki/LibrePlan/LibrePlan) and use it from a ZUL page.

-- [DiegoPino](/twiki/Main/DiegoPino) - 21 Apr 2012

I was porting the first chart, **Global Progress**, to jqPlot. jqPlot gave a big headache with a side-effect its inclusion was causing in other views. When I included or simply put some native HTML code right before the div that contains the window in the Dashboard page, the view rendered OK, but when I switched to other views, a big chunk of space appear on the top of the view. The cause was the native HTML code, it has to be place after the main **. I added a note in the code.

The initialization of the charts has to be done in defer mode, after everything it has been loaded. This gave some problems too in the beginning.

Apart from passing the data to be rendered to the chart, it's also necessary to pass all the labels already translated, since the Javasript code cannot access the I18n object. This implies to jsonify Java code. On the client side, jQuery can decode that JSON code easily. I think that maybe it will be worth to inclide a Java library for jsonify objects, for the moment I'm doing it by hand.

-- [DiegoPino](/twiki/Main/DiegoPino) - 30 Apr 2012

-   I continued recoding the charts. I recoded the following charts:
    -   Task Status
    -   Task Completation Lead/Lag
    -   Deadline Violation
    -   Margin with Deadline (pending absolute margin)

-   Added a new table with information about the status of tasks (Tasks Summary).
-   We discovered a Java library that acts a wrapper for jqPlot, so there's no need to code javascript.
    -   Added jqPlot4java
    -   Recoded all charts except 'Global Progress' using jqPlot4java

Pending:

-   Recode 'Global progress' chart
-   Implement 'Margin with deadline' absolute value
-   Revamp 'Resources' and 'Cost'

-- [DiegoPino](/twiki/Main/DiegoPino) - 02 May 2012

**Redo 'Global Progress' chart**

I tried to recode the *'Global Progress'* using **jqplot4java**. The main problem is that in the Jqplot4Java the class *BarChart* accepts any type of data that extends from *Number*.

To code this *BarChart*, the Javascript that I need to generate is something like this:

    global_progress.render('[[[90.58, 1],[90.38, 2],[91.59, 3]], [[15.94, 1],[16.92, 2],[14.79, 3]]]', 
    '["Critical path (duration)","Critical path (hours)","All tasks (hours)"]', 
    '[{"label": "Actual", "color": "#33c"},{"label": "Expected", "color": "#c33"}]');

The first parameter is the data. It's grouped in two arrays. Each array contains values for: *'All tasks (hours)'*, *'Critical path (hours)'* and *'Critical Duration'*. Each element contains a value that it's a pair of values (measurement, type). For example \[90.58, 1\] means 90.58 hours for the bar *'All tasks (hours)'*.

It's not possible to pass an array of values like this to Jqplot4Java *BarChart*. It's only ready for single values that extend from *Number*.

    public class BarChart<T extends Number> extends AbstractChart<BarData<T>> {
    ...
    }

Another possible solution is to pass an array with a wildcard to the *BarChart*, generate the javascript code and after that use a regular expression to substitute the wildcard with the array of values as we want it. The benefit of this is that it's not needed to spend an extra effort on the internationalization of labels (but this is already done).

-- [DiegoPino](/twiki/Main/DiegoPino) - 09 May 2012

![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!"): [Resources ratios moved to analysis](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#ResourcesRatios)

~~**Overtime Ratio**~~

-   Refactored code and isolate the code for calculating resource load values such as load, overload and capacity in a proper class.
-   This class can be reused to get the resource load values of an Order from the Dashboard view.
-   Calculate *overtime ratio* as *overload* + *load* / *load*:
    -   If *overload* = 0 =&gt; *overtime ratio* = 1
    -   If *overload* &gt; 1 =&gt; *overtime ratio* &gt; 1
-   Calculate *availability ratio* as load / capacity:
    -   If *availability ratio* &lt; 1 =&gt; there are blank spaces
    -   If *availability ratio* = 1 =&gt; resources are completely used
    -   If *availability ratio* &gt; 1 =&gt; resources have external load

-- [DiegoPino](/twiki/Main/DiegoPino) - 09 May 2012

-   Fixed bugs rendering 'Task Completation' chart when there's no data
-   Fixed bug refreshing 'Absolute Margin with Deadline'
-   Added feature to allow set colors in PieCharts[?](/twiki/bin/edit/LibrePlan/PieCharts?topicparent=LibrePlan.ItEr76S15OrganizingPerProjectDashboard "Create this topic")
-   Removed unused code in jqplot
-   Removed unused code in DashboardModel[?](/twiki/bin/edit/LibrePlan/DashboardModel?topicparent=LibrePlan.ItEr76S15OrganizingPerProjectDashboard "Create this topic")
-   Isolated 'Global Progress' chart code in different files

**Check how to move jqplot code to jqplot4java jar**

I moved the jqplot Javascript code to the *resources/* folder in jqplot4java source code and created a new jar. There are methods in java to extract resources from a jar file (*getResource()*). What I later did was to create a new task in maven than in is executed during the *prepare-package* phase. The task reads the jar, extracts the js files and copy them to the *src/* folder (js code should be in *src/* folder not *target/*).

The point was that I need to do this only for the *libreplan-webapp* subproject, so I put the code of this maven task into *libreplan-webapp/pom.xml*, however it didn't work. It only works if I put it in the superpom. When I put the code in the superpom this task is executed for every subproject which results in having the same jqplot Javascript source code copied in 3 different locations. In addition, as the code is copied to *src/* folder I needed to avoid git to track these files by adding new rules in *.gitignore*. The solution works but it's ugly IMHO.

The day I was coding this Óscar was at the office and I explained him what I was trying to do. He told me ZK has some built-in features to do the same thing. All the things I read were using the *getResource()* function, which I tried but I couldn't make it work successfully. I don't know if he meant this, I would like to ask him more before continuing with this task.

-- [DiegoPino](/twiki/Main/DiegoPino) - 19 May 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                                    | 4                                                                                                                                                                     | 8                                                                                                                                                                       | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                                 | [Solve the Java exceptions when the data for the charts are not available](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK1)                           | 23/04/2012                                                                                                                                                                   | 31/05/2012                                                                                                                                                                     |                                                                                                                                                                             |
| Task                                                                                                                                                                    | 14                                                                                                                                                                    | 23                                                                                                                                                                      | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                                 | [Revamping the layout for the project dashboard first section (progress)](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK2)                            | 23/04/2012                                                                                                                                                                   | 31/05/2012                                                                                                                                                                     |                                                                                                                                                                             |
| Task                                                                                                                                                                    | 20                                                                                                                                                                    | 26.75                                                                                                                                                                   | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                                           | [Revamping the layout for the project dashboard third section (Resources)](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK3)                           | 30/04/2012                                                                                                                                                                   | 31/05/2012                                                                                                                                                                     |                                                                                                                                                                             |
| Task                                                                                                                                                                    | 20                                                                                                                                                                    | 21.5                                                                                                                                                                    | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                                           | [Revamping the layout for the project dashboard forth section (Cost)](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK4)                                | 30/04/2012                                                                                                                                                                   | 31/05/2012                                                                                                                                                                     |                                                                                                                                                                             |
| Task                                                                                                                                                                    | 4                                                                                                                                                                     | 21                                                                                                                                                                      | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                                 | [Remove bottom tab Overall progress in Planning view](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK5)                                                | 07/05/2012                                                                                                                                                                   | 31/05/2012                                                                                                                                                                     |                                                                                                                                                                             |
| Task                                                                                                                                                                    | 14                                                                                                                                                                    | 0                                                                                                                                                                       | 0                                                                                                                                                                       | Low                                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                            | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                                 | [Create flags summing up the status of the project](/twiki/LibrePlan/AnA14S02OrganizingPerProjectDashboard#TasK6)                                                  | 07/05/2012                                                                                                                                                                   | 31/05/2012                                                                                                                                                                     |                                                                                                                                                                             |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S15OrganizingPerProjectDashboard?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LorenzoTilve](/twiki/Main/LorenzoTilve)                                                                                                                      | 48.25                                                                                                                                                                                | 0                                                                                                                                                                                    | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                     |
| [DiegoPino](/twiki/Main/DiegoPino)                                                                                                                            | 52                                                                                                                                                                                   | 0                                                                                                                                                                                    | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                     |
| Total                                                                                                                                                                  | 100.25                                                                                                                                                                               | 0                                                                                                                                                                                    | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                     |

------------------------------------------------------------------------
