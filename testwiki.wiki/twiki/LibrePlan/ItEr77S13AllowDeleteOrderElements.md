[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr77S13AllowDeleteOrderElements](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements "Topic revision: 2 (06 Nov 2012 - 12:32:40)") (06 Nov 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr77S13AllowDeleteOrderElements?t=1520337947 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr77S13AllowDeleteOrderElements "Attach an image or document to this topic")

 [ItEr77S13AllowDeleteOrderElements](/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Allow Delete Order Elements From Web Services                                                    |
| Iteration              | [ItEr77Week34To44](/twiki/LibrePlan/ItEr77Week34To44)                                   |
| FEA                    | [ItEr77S13AllowDeleteOrderElements](/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

The delete operation has been implemented, but some problems appeared.

The main problem was related with removing all the data depending on the `OrderElement) to be removed: =TaskElement`, `TaskSource`, assignments and also the data related with scenarios.

The final solution was to use directly `OrderModel` which delegates the saving in `SaveCommand` and now everything seems to work properly. Some special stuff that was done:

-   It was needed to set as non-lazy the association between an `OrderElement` and its parent
-   We make optional the param `Desktop` in `OrderModel.initEdit`, as we were calling it from the web service
-   We need to create a new method `OrderElement.detachFromParent` in order to set parent to `null` and avoid problems removing the element (and removing the parents too). Another option could be to change the mapping between `OrderElement` and its parent in order to set it as `cascade="none"`, however it could cause other unexpected errors in other parts of the application so it doesn't seem a good idea to be done at this moment.

A new script to test the new service has been included into examples folder (`scripts/rest-clients/`). The new script is called `remove-order-element.sh` and it'll receive the code of the element to be removed as parameter.

Finally, a new DTO called `ErrorDTO` has been created, to show the error message if it's not possible to remove the `OrderElement` because it (or any of its children) has been already used in a timesheet or a expenses sheet. In this case the server returns the status code [403 FORBIDDEN](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4).

-- [ManuelRego](/twiki/Main/ManuelRego) - 06 Nov 2012

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr77S13AllowDeleteOrderElements?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 7                                                                                                                                                                | 8                                                                                                                                                                  | 0                                                                                                                                                                  | Low                                                                                                                                                               | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                          | [Add delete operation for order elements from web services](/twiki/LibrePlan/AnA12S03AllowDeleteOrderElements#TasK1)                                          |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |


