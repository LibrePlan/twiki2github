[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA08S12WBSTreeRefactoring](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring "Topic revision: 9 (22 Jun 2011 - 09:13:59)") (22 Jun 2011, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA08S12WBSTreeRefactoring?t=1520337846 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA08S12WBSTreeRefactoring "Attach an image or document to this topic")

 [AnA08S12WBSTreeRefactoring](/twiki/LibrePlan/AnA08S12WBSTreeRefactoring)
================================================================================================================================



|                        |                                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| Story summary          | WBS refactoring                                                                    |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)                         |
| FEA                    | [AnA08S12WBSTreeRefactoring](/twiki/LibrePlan/AnA08S12WBSTreeRefactoring) |
| Story Lead             |                                                                                    |
| Next Story             |                                                                                    |
| Passed acceptance test | No                                                                                 |

###  Tasks

This analysis is to test and refactor the wbs tree in order to make sure that the behaviour of the tree is correct on adding, removing and moving nodes with regard to the associated entities (advances, labels, quality forms, criteria).



####  Do the tests and implement things in order to satisfy operations

    ================================================================================
    OP-1 Moving one generic Order Element C2.1 from C2 parent to C1 OrderLineGroup parent
    ================================================================================

    Tree:

      (*) C1
         |-> OL1
         
      (*) C2
          -> C2.1 (Can be OrderLine or OrderLineGroup)
               -> ....
         
    Operations to perform in the tree:

    A) Operations affect C2 and ancestors

        A.1) If C2 does not exist => Do nothing => C2.1 is a root node.
        A.2) {For all the C2 AdvanceAssigment of type Calculated which are computed using only C2.1 node} = Set A-> Remove all
     the elements of set A in C2 and in ancestors of C2 if they exist.
        A.3) If C2.1 has no sibling => Convert C2 into OrderLine.
        
    B) Operations affect C2.1 node

        B.1) Set C2.1's parent to C1.
        B.2) Remove all the AdvanceAssigment in set {C2.1 and descendant nodes} which has a type belonging to set {C1 and 
    ancestor's nodes set of advance assignments}
        B.3) Remove all the labels in set {C2.1 and descendant nodes} belonging to set {C1 and 
    ancestor's nodes set of labels}
        B.4) Criteria changes for @each = set of {C2.1 node, descendats order elements of C2.1 and hours
     groups of OL descendants of C2.1}
        
            B.4.1) For every CR of type I included in set {CRs of C1} and not in {CR of @each} =>  Add it to 
    @each with the same status.
            B.4.2) For every CR of type D included in set {CRs of C1} and not in {CR of @each} => Add it to 
    @each as type I and status Valid.
            B.4.3) For every CR of @each of type I included in set {CRs of C2} => Remove in @each
            B.4.4) For every CR of @each of type I not included in set {CRs of C2} => Keep it in @eah with original state.
            B.4.5) For every CR of @each type D included in set {CRs of C1} => Convert it in CR of type I state Valid.
            B.4.6) For every CR of @each type D not included in set {CRs of C1} => Keep it.

    C) Operations affect C1 and ancestors

      C.1) Create AdvancedAssigment of type calculated for all the AdvanceAssigment included 
    in set {AdvanceAssigment of C2.1 after operation B.2}


    =================================================================
    OP2 - Moving one generic Order Element C2.1 from C2 parent to OL1
    =================================================================

    This is an adaptation of OP-1 for the case that the destination node for movement is an OrderLine.

    Steps are the same but it is needed to create a new node that will play the role of C1 and then 
    the OP-1 algorithm will be applied.

    Let's call C the parent of OL1

    (0) Create a node C1 of type OrderLineGroup
        0.1) Set te parent of C1 to C
        0.2) Set the parent of OL1 to C1.
        0.3) For every CR @each in set of CR of C. 
            0.3.1) If @each of type Direct => Add CR of type Indirect in C1.
            0.3.2) If @each of type Indirect => Add CR of type Indirect and same state [Valid,Invalid] to C1.
        0.4) For every AdvanceAssigment included in 
    set {OL1 AdvanceAssigment} add it as AdvanceAssigment of type Calculated in C.
        

    ===============================================================
    OP3 - One OrderLineGroup C1 selected and press add new OL OL1-2
    ===============================================================

    This is a simplication of OP1 being the OL1-2 created for the occasion. Simplifcations are:

    A) Operations affect C2 and ancestors

       Nothing to do because OL1-2 is new and has not original parent.

    B) Operations affect C2.1 node = OL1-2

    Only applies B.1), B.4.1) and B.4.2)
        
    C) Operations affect C1 and ancestors

    Nothing to do because OL1-2 has not AdvanceAssigment

    ===============================================================
    OP4 - One OrderLine OL selected and press add new OL OL1-2
    ===============================================================

    In this case is the same than OP2.

###  User stories

-   [ItEr74S07WBSTreeRefactoring](/twiki/LibrePlan/ItEr74S07WBSTreeRefactoring)



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                        | 20                                                                                                                                                        | 20                                                                                                                                                          | 0                                                                                                                                                           | Low                                                                                                                                                        | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                   | [Do the tests and implement things in order to satisfy operations](/twiki/LibrePlan/AnA08S12WBSTreeRefactoring#TasK1)                                  |                                                                                                                                                                  |                                                                                                                                                                    |                                                                                                                                                                 |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA08S12WBSTreeRefactoring?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ManuelRego](/twiki/Main/ManuelRego)                                                                                                              | 20                                                                                                                                                                       | 0                                                                                                                                                                        | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                         |
| Total                                                                                                                                                      | 20                                                                                                                                                                       | 0                                                                                                                                                                        | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                         |

------------------------------------------------------------------------
