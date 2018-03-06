[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA12S01AllowExportOneEntity](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity "Topic revision: 5 (20 Aug 2012 - 09:52:46)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA12S01AllowExportOneEntity?t=1520337853 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA12S01AllowExportOneEntity "Attach an image or document to this topic")

 [AnA12S01AllowExportOneEntity](/twiki/LibrePlan/AnA12S01AllowExportOneEntity)
======================================================================================================================================



|                        |                                                                                        |
|------------------------|----------------------------------------------------------------------------------------|
| Story summary          | Allow Export One Entity                                                                |
| Iteration              | [AnA12WebServices](/twiki/LibrePlan/AnA12WebServices)                         |
| FEA                    | [AnA12S01AllowExportOneEntity](/twiki/LibrePlan/AnA12S01AllowExportOneEntity) |
| Story Lead             |                                                                                        |
| Next Story             |                                                                                        |
| Passed acceptance test | No                                                                                     |

###  Tasks



####  Add export operation for just one entity

Currently LibrePlan web services export all entities of each `IntegrationEntity` when you call export service.

This task is intended to add a new `GET` method in services for all `IntegrationEntity` in order to return just one item passing as parameter the entity code.

It's going to be needed modify the different web services adding a new method with something similar to the following lines:

        @GET
        @Path("/{code}/")
        public EntityDTO getEntity(@PathParam("code") String code) {
            return new EntityDTO(findByCode(code));
        }

The method `findByCode` should be implemented in the generic classes and DAOs used in web services implementation. In order to avoid repeat the same stuff in all the classes.



####  Add support to export scripts

Once web services have support to export just one entity we should modify export scripts inside `scripts/rest-clients/` to have a new optional argument (entity code) in order to test the new methods.

###  User stories

-   [ItEr75S12AllowExportOneEntity](/twiki/LibrePlan/ItEr75S12AllowExportOneEntity)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                          | 15                                                                                                                                                          | 6                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                        | [Add export operation for just one entity](/twiki/LibrePlan/AnA12S01AllowExportOneEntity#TasK1)                                                          |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |
| Task                                                                                                                                                          | 4                                                                                                                                                           | 4                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                     | [Add export operation for just one entity](/twiki/LibrePlan/AnA12S01AllowExportOneEntity#TasK1)                                                          |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |
| Task                                                                                                                                                          | 10                                                                                                                                                          | 3                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                        | [Add support to export scripts](/twiki/LibrePlan/AnA12S01AllowExportOneEntity#TasK2)                                                                     |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |
| Task                                                                                                                                                          | 1                                                                                                                                                           | 1                                                                                                                                                             | 0                                                                                                                                                             | Low                                                                                                                                                          | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                    | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                     | [Add support to export scripts](/twiki/LibrePlan/AnA12S01AllowExportOneEntity#TasK2)                                                                     |                                                                                                                                                                    |                                                                                                                                                                      |                                                                                                                                                                   |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA12S01AllowExportOneEntity?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CristinaAlvarino](/twiki/Main/CristinaAlvarino), [IgnacioDiaz](/twiki/Main/IgnacioDiaz)                                                   | 9                                                                                                                                                                          | 0                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                           |
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                | 5                                                                                                                                                                          | 0                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                           |
| Total                                                                                                                                                        | 14                                                                                                                                                                         | 0                                                                                                                                                                          | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                           |

------------------------------------------------------------------------