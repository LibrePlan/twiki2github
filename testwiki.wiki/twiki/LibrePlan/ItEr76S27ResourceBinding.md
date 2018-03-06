[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S27ResourceBinding](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding "Topic revision: 3 (20 Aug 2012 - 09:50:19)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S27ResourceBinding?t=1520337941 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S27ResourceBinding "Attach an image or document to this topic")

 [ItEr76S27ResourceBinding](/twiki/LibrePlan/ItEr76S27ResourceBinding)
==========================================================================================================================



|                        |                                                                                |
|------------------------|--------------------------------------------------------------------------------|
| Story summary          | Resource binding                                                               |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                 |
| FEA                    | [ItEr76S27ResourceBinding](/twiki/LibrePlan/ItEr76S27ResourceBinding) |
| Story Lead             |                                                                                |
| Next Story             |                                                                                |
| Passed acceptance test | No                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

**One-to-one** mapping between **Worker** and **User** has been configured with the following relationships:

-   In the **Worker** side:

                <many-to-one name="user" cascade="save-update"
                    class="org.libreplan.business.users.entities.User"
                    column="user_id" unique="true" />

-   In the **User** side:

                <one-to-one name="worker" property-ref="user"
                    class="org.libreplan.business.resources.entities.Worker" />

Fixed problem in **BandboxSearch**, in order that `selectedElement` calls both `get` and `set` methods:

-   In order to do this a change has been done in **BandboxSearch**, adding the last line to the next method:

<!-- -->

        public void pickElementFromList() {
            final Object object = getSelectedItem().getValue();
            bandbox.setValue(finder.objectToString(object));
            setSelectedElement(object);
            Util.getBinder(this).saveAttribute(this, "selectedElement");
        }

-   Moreover is needed to use `access='both'` in the `.zul`:

<!-- -->

         <bandboxSearch id="userBandbox" finder="UserBandboxFinder"
              model="@{controller.possibleUsersToBound}"
              selectedElement="@{controller.boundUser, access='both'}" />

It was needed to fix entry points for users and workers as it was not working properly:

-   For users:
    -   In `UserCRUDController.doAfterCompose` moved to the bottom the part needed for entry points
-   For workers:
    -   In `WorkerCRUDController.doAfterCompose` moved to the bottom the part needed for entry points
    -   In `CriterionsController.forceSortGridSatisfaction` add checking to prevent `NullPointerException`

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                      | 3                                                                                                                                                       | 5                                                                                                                                                         | 0                                                                                                                                                         | Low                                                                                                                                                      | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                              | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                 | [Add relationship between and Worker and User](/twiki/LibrePlan/AnA11S03ResourceBinding#TasK1)                                                       |                                                                                                                                                                |                                                                                                                                                                  |                                                                                                                                                               |
| Task                                                                                                                                                      | 21                                                                                                                                                      | 10                                                                                                                                                        | 0                                                                                                                                                         | Low                                                                                                                                                      | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                              | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                 | [Adapt resource administration window](/twiki/LibrePlan/AnA11S03ResourceBinding#TasK2)                                                               |                                                                                                                                                                |                                                                                                                                                                  |                                                                                                                                                               |
| Task                                                                                                                                                      | 14                                                                                                                                                      | 6.5                                                                                                                                                       | 0                                                                                                                                                         | Low                                                                                                                                                      | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                              | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                 | [Adapt user administration window](/twiki/LibrePlan/AnA11S03ResourceBinding#TasK3)                                                                   |                                                                                                                                                                |                                                                                                                                                                  |                                                                                                                                                               |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S27ResourceBinding?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                            | 21.5                                                                                                                                                                   | 0                                                                                                                                                                      | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                       |
| Total                                                                                                                                                    | 21.5                                                                                                                                                                   | 0                                                                                                                                                                      | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                       |

------------------------------------------------------------------------
