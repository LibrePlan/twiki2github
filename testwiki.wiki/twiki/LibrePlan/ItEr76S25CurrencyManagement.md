[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S25CurrencyManagement](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement "Topic revision: 4 (20 Aug 2012 - 09:50:19)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S25CurrencyManagement?t=1520337940 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S25CurrencyManagement "Attach an image or document to this topic")

 [ItEr76S25CurrencyManagement](/twiki/LibrePlan/ItEr76S25CurrencyManagement)
===================================================================================================================================



|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | Currency Managment                                                                   |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                       |
| FEA                    | [ItEr76S25CurrencyManagement](/twiki/LibrePlan/ItEr76S25CurrencyManagement) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

To change the € symbol in the report it was need to add a new parameter with the currency symbol and change the way the text fields were formatted:

    -                               <textField pattern="###0.00 ;-###0.00 ">
    +                               <textField>
                                            <reportElement x="422" y="2" width="119" height="20"/>
                                            <textElement textAlignment="Right" verticalAlignment="Middle">
                                                    <font isBold="true"/>
                                            </textElement>
    -                                       <textFieldExpression class="java.math.BigDecimal"><![CDATA[$V{sumTotalCosts}]]></textFieldExpression>
    +                                       <textFieldExpression class="java.lang.String"><![CDATA[$V{sumTotalCosts}.setScale(2) + " " + $P{currencySymbol}]]></textFieldExpression>
                                    </textField>

-- [ManuelRego](/twiki/Main/ManuelRego) - 26 Apr 2012

Euro symbol was justs been used in 2 places at this moment:

-   Task tooltip in the Gantt view of a project
-   *Project Costs Per Resource* report

Two new methods in `Util` class has been created:

-   `getCurrencySymbol()`: Returns the currency symbol from `Configuration` class.
-   `getMoneyFormat()`: To be used in `Decimalbox` to show the currency symbol together with the value inside the input.

It has been reviewed all the places where a number representing money is used and the currency symbol has been added in:

-   *Materials Needs At Date* report
-   Cost Category
-   Type of Hours
-   Materials
-   WBS (projects and templates): list, *Imputed hours* tab, *General data* tab, *Details* tab, *Materials* tab
-   Gantt: *Task properties* tab, *Subcontract* tab

It was needed to escape some special chars (used in `DecimalFormat`) from the currency symbol. For example, `SFr.` needs to be escaped to `SFr'.'` in order to avoid problems using it as format of the `Decimalbox`.

In the reports it was needed to set a rounding mode to avoid problems:

    $V{sumTotalCosts}.setScale(2, RoundingMode.HALF_UP)

-- [ManuelRego](/twiki/Main/ManuelRego) - 27 Apr 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S25CurrencyManagement?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                         | 2                                                                                                                                                          | 2                                                                                                                                                            | 0                                                                                                                                                            | Low                                                                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                   | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Add option to choose LibrePlan currency in configuration window](/twiki/LibrePlan/AnA09S19CurrencyManagement#TasK1)                                    |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |
| Task                                                                                                                                                         | 3                                                                                                                                                          | 4                                                                                                                                                            | 0                                                                                                                                                            | Low                                                                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                   | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [Replace use of euro for the configured currency](/twiki/LibrePlan/AnA09S19CurrencyManagement#TasK2)                                                    |                                                                                                                                                                   |                                                                                                                                                                     |                                                                                                                                                                  |


