[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Ana08S11RecurrentAllocationsSchemes](LibrePlan_Ana08S11RecurrentAllocationsSchemes "Topic revision: 3 (20 Jun 2013 - 18:34:39)") (20 Jun 2013, [LorenzoTilve](Main_LorenzoTilve))[Edit](LibrePlan_Ana08S11RecurrentAllocationsSchemes?t=1520343624 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/Ana08S11RecurrentAllocationsSchemes "Attach an image or document to this topic")  

 [Ana08S11RecurrentAllocationsSchemes](LibrePlan_Ana08S11RecurrentAllocationsSchemes)
=====================================================================================

|                        |                                                                                      |
|------------------------|--------------------------------------------------------------------------------------|
| Story summary          | Resource allocations schemes                                                         |
| Iteration              | [AnA07PlanningWindow](LibrePlan_AnA07PlanningWindow)                                 |
| FEA                    | [Ana08S11RecurrentAllocationsSchemes](LibrePlan_Ana08S11RecurrentAllocationsSchemes) |
| Story Lead             |                                                                                      |
| Next Story             |                                                                                      |
| Passed acceptance test | No                                                                                   |

###  Tasks

Nesta sección incorporaráse a documentación relativa ó desenvolvemento nos cambios que se desenvolven en [LibrePlan](LibrePlan_LibrePlan) relativos a permitiir asignacións de tipo recurrente.

####  Cambios no modelo

O modelo de datos de [LibrePlan](LibrePlan_LibrePlan), permite diferentes tipos de asignación, baseadas en asociacións con conxuntos de recursos individuais ou critérios xenéricos, e as cales se estructuran segundo o seguinte diagrama de clases, no que se pode observar a modularización das estructuras que se empregan internamente.

A idea para implementar **asignacións recurrentes** en [LibrePlan](LibrePlan_LibrePlan), consiste en facer modificacións no modelo, para que, xa que se posibilita manter coleccións de `ResourceAllocations` viculadas ás tarefas, éstas inclúan tamén unha ṕosibilidade de numeración para que deste modo, se almacenen tantas asignacións coma repeticións determine o patrón de recurrencia.

Polo tanto, tras analizar as implicacións dos diferentes tipos de cambios a realizar no modelo para extendelo e que permitise este tipo de novas funcións, identifícase como a máis adecuada, a de inicialmente incorporar na clase `ResourceAllocation.java` tanto unha propiedade para almacenar o índice da recurrencia, os métodos para acceder e manipular dita propiedade, e os cambios na estructura de datos e nos arquivos de `liquibase` para que se integren as sentencias xenéricas de modificación da base de datos.

-   Diagrama de clases de asignación de recursos:  
    ![resouce-allocation.png](/twiki/pub/LibrePlan/Ana08S11RecurrentAllocationsSchemes/resouce-allocation.png)

###  Interface

Ademáis dos cambios no modelo, é necesario incorporar unha vista que permita manipular os parámetros de configuración da recurrencia. A maioría das ferramentas existentes no mercado, empregan interfaces semellantes á seguinte <http://www.project-blog.com/?p=65>:

-   Exemplo de interface de configuración de recurrencia:  
    ![recurring-task.jpg](/twiki/pub/LibrePlan/Ana08S11RecurrentAllocationsSchemes/recurring-task.jpg)

Na mesma proporcionanse compoñentes para configurar dita recurrencia, cun grado alto de parametrización. Levarase a cabo unha versión incremental de aproximación á cobertura dunha parte representativa do nivel de configuración proporcionado por esta vista.

No caso concreto de LibrePlan, incorpórase unha pestana adicional na ventana emerxente de asignación, que permitirá configurar o número de repeticións **da asignación configurada na pestana principal**. Isto significa que os parámetros de horas, duración, recursos por día, etc, que se configuran no `popup` de asignación, fan referencia á primeira repetición. Isto é, por exemplo, que se configuramos que queremos unha tarefa de 4 horas que se repita diariamente 5 veces. Indicaremos na ventana de asignación as características relativas a unha das aplicacións (non ó total) e os algoritmos calcularán como estaban realizando, o resto dos parámetros relativos á primeira das ocurrencias; e todas as características da repetición (incluíndo as datas de inicio ou finais completas da tarefa) serán determinadas na nova pestana.

###  Modificacións nos algoritmos de creación das asignacións

O fluxo que debemos modificar, é o asociado a operación de aceptación das asignacións realizadas polo planificador. Éstas desencadénanse en:

`org.libreplan.web.planner.taskedition.EditTaskController.accept()`

Determínase se se produciron asingacións

    org.libreplan.web.planner.taskedition.TaskPropertiesController.stateHasChanged()
    this.originalState / org.libreplan.web.planner.taskedition.TaskPropertiesController.getSelectedResourceAllocationType()

    ----
    ( org.libreplan.web.planner.allocation.FormBinder.doApply().new IResourceAllocationContext() {...}.doInsideTransaction() Éste so cando se da a Apply) 

    Ó premer en aceptar, compróbase o seguinte:

    ensureResourcesAreReadyForDoingAllocation();  /* Fai simplemente reattach dos recursos */

    removeDeletedAllocations();  /*  Colle as que hai que eliminar de allocationRowsHandler.getAllocationsRequestedToRemove(); */

    #2# org.libreplan.web.planner.allocation.AllocationRowsHandler.doAllocation()
    Flagged<AllocationResult, Warnings> allocationResult = allocationRowsHandler.doAllocation();

    checkInvalidValues();

    if !currentRows.isEmpty() --> List<? extends AllocationModification> modificationsDone = doSuitableAllocation();

    Neste punto, temos en modificationsDone unha colección de:  [ResourcesPerDayModification$OnSpecificAllocation]
    --
    [0]
    beingModified : SpecificResourceAllocation (id=248)
     * assignmentfunction: null
     * assignmentstate : ResourceAllocation$TransientState
        * intraDayEnd
        * intraDayStart
     * derivedAllocations: []
     * intendednonconsolidatedeffort 4:00
     * intendedresourcesperday: 1.0
     * intendedtotalassignment: 4:00
     * intendedtotalhours: null
     * newObject: true
     * recurrenceAppliance : null
     * resource: ltilve
     * resourcesperday: 1.0
     * specificDayAssignmentsContainers []
     * task
    goal : resourcesPerDay (id=251) 1.0
    resourceAllocation : SpecificResourceAllocation (id=248)
    resourcesOnWhichApplyAllocation : [ltilve]
    -- h
    [1]
    beingModified : SpecificResourceAllocation (id=2xxx)
     * assignmentstate : ResourceAllocation$TransientState
        * intraDayEnd
        * intraDayStart
    goal : resourcesPerDay (id=2yy) 1.0
    resourceAllocation : SpecificResourceAllocation (id=2xx)
    resourcesOnWhichApplyAllocation : [jmoran]
    ---
    etc

    O método que constrúe a colección de ResourcesPerDayModifications (unha vez seleccionado o tipo de asignación, 
    por defecto END_DATE) é:

    org.libreplan.web.planner.allocation.AllocationRowsHandler.calculateEndDateOrStartDateAllocation()

    Posteriormente, será necesario modificar o comportamento da función:

    public IntraDayDate untilAllocating(Direction direction, EffortDuration toAllocate, final INotFulfilledReceiver receiver) {
                UntilFillingHoursAllocator allocator = new UntilFillingHoursAllocator(direction, task, allocations) {

    AllocationRow.loadDataFromLast(currentRows, modificationsDone);
    org.libreplan.web.planner.allocation.AllocationRowsHandler.createResult()
    org.libreplan.web.planner.allocation.AllocationResult.create(Task, CalculatedValue, List<AllocationRow>, Integer)
    org.libreplan.web.planner.allocation.AllocationRow.getNewFrom(List<AllocationRow>)

-- [LorenzoTilve](Main_LorenzoTilve) - 20 Jun 2013

After some changes, the recurring-task branch is creating N resource allocations when doing the specific assignment.

    mysql> select * from specific_day_assignments_container; select * from day_assignment; select * from resource_allocation;  select * from specific_resource_allocation;
    +------+---------+------------------------+----------+------------+-----------------------------+------------+----------------------+
    | id   | version | resource_allocation_id | scenario | start_date | duration_start_in_first_day | end_date   | duration_in_last_day |
    +------+---------+------------------------+----------+------------+-----------------------------+------------+----------------------+
    | 3661 |       3 |                   3560 |      909 | 2013-06-20 |                           0 | 2013-06-20 |                 7200 |
    | 3662 |       3 |                   3561 |      909 | 2013-06-20 |                           0 | 2013-06-20 |                 7200 |
    | 3663 |       3 |                   3562 |      909 | 2013-06-20 |                           0 | 2013-06-20 |                 7200 |
    +------+---------+------------------------+----------+------------+-----------------------------+------------+----------------------+
    3 rows in set (0.00 sec)

    +------+---------------------+---------+----------+--------------+------------+-------------+-----------------------+----------------------+----------------------+
    | id   | day_assignment_type | version | duration | consolidated | day        | resource_id | specific_container_id | generic_container_id | derived_container_id |
    +------+---------------------+---------+----------+--------------+------------+-------------+-----------------------+----------------------+----------------------+
    | 3791 | specific_day        |       3 |     7200 |            0 | 2013-06-20 |        1920 |                  3661 |                 NULL |                 NULL |
    | 3792 | specific_day        |       3 |     7200 |            0 | 2013-06-20 |        1920 |                  3662 |                 NULL |                 NULL |
    | 3793 | specific_day        |       3 |     7200 |            0 | 2013-06-20 |        1920 |                  3663 |                 NULL |                 NULL |
    +------+---------------------+---------+----------+--------------+------------+-------------+-----------------------+----------------------+----------------------+
    3 rows in set (0.00 sec)

    +------+---------+-------------------+----------------------+------+---------------------+----------------------------+---------------------------+----------------------------------+----------------------+
    | id   | version | resources_per_day | intended_total_hours | task | assignment_function | intended_resources_per_day | intended_total_assignment | intended_non_consolidated_effort | recurrence_appliance |
    +------+---------+-------------------+----------------------+------+---------------------+----------------------------+---------------------------+----------------------------------+----------------------+
    | 3560 |       3 |              1.00 |                 NULL | 4244 |                NULL |                       1.00 |                      7200 |                             7200 |                    2 |
    | 3561 |       3 |              1.00 |                 NULL | 4244 |                NULL |                       1.00 |                      7200 |                             7200 |                    1 |
    | 3562 |       3 |              1.00 |                 NULL | 4244 |                NULL |                       1.00 |                      7200 |                             7200 |                 NULL |
    +------+---------+-------------------+----------------------+------+---------------------+----------------------------+---------------------------+----------------------------------+----------------------+
    3 rows in set (0.00 sec)

    +------------------------+----------+
    | resource_allocation_id | resource |
    +------------------------+----------+
    |                   3560 |     1920 |
    |                   3561 |     1920 |
    |                   3562 |     1920 |
    +------------------------+----------+
    3 rows in set (0.00 sec)

However, they are not yet shifted, and they are being shown repeated on the list of allocations. It's necessary to 'hide' the allocations with a occurrence value.

###  Tasks in this story

| [Tasks](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|

[![](/twiki/pub/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](LibrePlan_Ana08S11RecurrentAllocationsSchemes#) [![](/twiki/pub/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](LibrePlan_Ana08S11RecurrentAllocationsSchemes#)

| [I](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Action](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=2;table=3;up=0#sorted_table "Sort by this column")                                                         |  [Size](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=3;table=3;up=0#sorted_table "Sort by this column")| [Date](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](LibrePlan_Ana08S11RecurrentAllocationsSchemes?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|:------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
|                             ![jpg](/twiki/pub/TWiki/TWikiDocGraphics/jpg.gif)jpg                             | [recurring-task.jpg](/twiki/pub/LibrePlan/Ana08S11RecurrentAllocationsSchemes/recurring-task.jpg)                     | [manage](/twiki/bin/attach/LibrePlan/Ana08S11RecurrentAllocationsSchemes?filename=recurring-task.jpg;revInfo=1 "change, update, previous revisions, move, delete...")     |                                                                                                          140.6 K| 14 May 2013 - 08:08                                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                              | Exemplo de interface de configuración de recurrencia                                                               |
|                             ![png](/twiki/pub/TWiki/TWikiDocGraphics/png.gif)png                             | [resouce-allocation.png](/twiki/pub/LibrePlan/Ana08S11RecurrentAllocationsSchemes/resouce-allocation.png)             | [manage](/twiki/bin/attach/LibrePlan/Ana08S11RecurrentAllocationsSchemes?filename=resouce-allocation.png;revInfo=1 "change, update, previous revisions, move, delete...") |                                                                                                           76.0 K| 14 May 2013 - 08:10                                                                                             | [LorenzoTilve](Main_LorenzoTilve)                                                                              | Diagrama de clases de asignación de recursos                                                                       |
