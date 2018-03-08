[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[ItEr77S08ReportsFonts](LibrePlan_ItEr77S08ReportsFonts "Topic revision: 2 (11 Sep 2012 - 08:49:58)") (11 Sep 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_ItEr77S08ReportsFonts?t=1520343704 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S08ReportsFonts "Attach an image or document to this topic")  

 [ItEr77S08ReportsFonts](LibrePlan_ItEr77S08ReportsFonts)
=========================================================

|                        |                                                          |
|------------------------|----------------------------------------------------------|
| Story summary          | Reports Fonts                                            |
| Iteration              | [ItEr77Week34To44](LibrePlan_ItEr77Week34To44)           |
| FEA                    | [ItEr77S08ReportsFonts](LibrePlan_ItEr77S08ReportsFonts) |
| Story Lead             |                                                          |
| Next Story             |                                                          |
| Passed acceptance test | No                                                       |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

We need to add the dependency with `jasperreports-fonts` to fix the issue with the fonts in the PDFs and change the font type to use **DejaVu**.

Due to the dependency with `jasperreports-fonts` we have to upgrade JasperReports to version 4. So it was upgraded to the last version available 4.7.0.

Then the dependency with `jasperreports-fonts` has been added:

                <dependency>
                    <groupId>net.sf.jasperreports</groupId>
                    <artifactId>jasperreports-fonts</artifactId>
                    <version>4.0.0</version>
                </dependency>

And the reports have been modified to use the **DejaVu Sans** font:

       <style name="dejavu-sans" isDefault="true" fontName="DejaVu Sans" fontSize="8"/>

Updated documentation and dependencies in Debian and RPM packages to change **Free fonts** for **DejaVu fonts**.

Updated guide about how to create a new report with the previous changes: <http://www.libreplan.org/howto-create-a-new-report-in-libreplan.html>

-- [ManuelRego](Main_ManuelRego) - 11 Sep 2012

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

| [Tasks](LibrePlan_ItEr77S08ReportsFonts?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_ItEr77S08ReportsFonts?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_ItEr77S08ReportsFonts?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_ItEr77S08ReportsFonts?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_ItEr77S08ReportsFonts?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_ItEr77S08ReportsFonts?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_ItEr77S08ReportsFonts?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_ItEr77S08ReportsFonts?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_ItEr77S08ReportsFonts?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_ItEr77S08ReportsFonts?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_ItEr77S08ReportsFonts?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Task                                                                                               | 2                                                                                                | 3                                                                                                  | 0                                                                                                  | Low                                                                                               | [ManuelRego](Main_ManuelRego)                                                                         | [ManuelRego](Main_ManuelRego)                                                                          | [Fix problem with fonts in reports exporting to PDF](LibrePlan_AnA22S01ReportsFonts#TasK1)             |                                                                                                         |                                                                                                           |                                                                                                        |
