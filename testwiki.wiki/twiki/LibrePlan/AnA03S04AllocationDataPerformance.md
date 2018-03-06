[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA03S04AllocationDataPerformance](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance "Topic revision: 10 (27 Nov 2012 - 09:02:33)") (27 Nov 2012, [JacoboAragunde](/twiki/Main/JacoboAragunde))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA03S04AllocationDataPerformance?t=1520337829 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA03S04AllocationDataPerformance "Attach an image or document to this topic")

 [AnA03S04AllocationDataPerformance](/twiki/LibrePlan/AnA03S04AllocationDataPerformance)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Improve performance on operations related to allocation data                                     |
| Iteration              | [AnA03PerformanceTuning](/twiki/LibrePlan/AnA03PerformanceTuning)                       |
| FEA                    | [AnA03S04AllocationDataPerformance](/twiki/LibrePlan/AnA03S04AllocationDataPerformance) |
| Story Lead             |                                                                                                  |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

###  Tasks

The goal of this tasks is defining an entity to store allocation data in a way they are easy to query, and use it in the places of the app where these data is needed instead of calculating them from the DayAssignments every time.



####  Crear entidade para datos de asignación (Create allocation data entity)

Orixinariamente pensamos no aproveitamento do modelo de datos relacionado coa vista de carga de recursos para implementar esas entidades que almacenarían os datos de carga de recursos de maneira persistente para fácil acceso. As clases coinciden con este diagrama:

-   [modelo-calculo-cargas.dia](/twiki/LibrePlan/AnA03S04AllocationDataPerformance/modelo-calculo-cargas.dia): Resource load calculation class diagram

Nembargantes, viuse a oportunidade de optimizar non só a vista de carga de recursos senón outras operacións relacionadas cos datos de asignación, e para iso necesitariamos un modelo de datos lixeiramente distinto, cunha granularidade máis fina.

Póñense dous modelos sobre a mesa, o primeiro deles correspóndese con este diagrama:

-   [effort-cache-model.dia](/twiki/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-model.dia): Data model proposed to cache allocation data

No que as únicas entidades persistente son DailyEffortSummary e as súas fillas. Implementaranse como unha única táboa para evitar as operacións de JOIN sobre a BD.

O outro modelo correspóndese con este diagrama:

-   [effort-cache-model-2.dia](/twiki/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-model-2.dia): Data model proposed to cache allocation data (B)

A entidade persistente é EffortSummary, que contén os datos de esforzo nun array de enteiros que se almacenará serializado nun único campo da BD. A herencia, do mesmo xeito que no caso anterior, implementarase sobre unha única táboa para evitar operacións de JOIN.

Para decantarse por un modelo ou outro, realízase unha implementación simplificada de ámbalos dous e realizaranse probas de rendemento sobre eles. Esta implementación simplificada ignora as dúas clases fillas (Criterion... e Resource...) e implementa só a relación con Resource na superclase. Escríbense dous test de unidade, nos que se realiza a operación de busca na BD cen veces e mídese o tempo por operación. Os resultados dos test son os seguintes:

Con DailyEffortSummary:

    Simon Stopwatch: [stopwatch INHERIT] total 59.5 s, counter 100, max 741 ms, min 293 ms
    StopwatchSample{total=59.5 s, counter=100, min=293 ms, max=741 ms, minTimestamp=121025-103336.141, maxTimestamp=121025-103432.615, active=0, maxActive=1, maxActiveTimestamp=121025-103431.874, last=741 ms, mean=595 ms, standardDeviation=73.0 ms, variance=5.384862156680421E15, varianceN=5.331013535113617E15, note=null}

Con EffortSummary:

    Simon Stopwatch: [stopwatch INHERIT] total 1.86 s, counter 100, max 34.7 ms, min 8.12 ms
    StopwatchSample{total=1.86 s, counter=100, min=8.12 ms, max=34.7 ms, minTimestamp=121025-103237.320, maxTimestamp=121025-103236.359, active=0, maxActive=1, maxActiveTimestamp=121025-103238.008, last=18.7 ms, mean=18.6 ms, standardDeviation=7.92 ms, variance=6.3403172556090664E13, varianceN=6.276914083052976E13, note=null}

Como pode verse, a implementación con arrays serializados é moito máis rápida, tardando uns 18.6 milisegundos de media en extraer os datos de esforzo entre dúas datas, mentres que a mesma operación cunha fila por data tarda 595 milisegundos de media.

A conclusión é que iremos adiante co modelo que emprega arrays serializados.



####  Implementar gardado dos datos de asignación (Implement save of allocation data information)

Unha vez que definimos un formato de acceso rápido para a información de asignación de horas a recursos, debemos asegurarnos de mantermos estes datos actualizados. Estes datos cambian cando se realiza en [LibrePlan](/twiki/LibrePlan/LibrePlan) alguna destas operacións:

-   Modificación da asignación de recursos dun proxecto
-   Modificación dos datos dun recurso (pode afectar á súa dispoñibilidade)

#####  Problemas de implementación

######  Algoritmo de serialización

Durante a implementación desta tarefa detectáronse problemas cos algoritmos de serialización por defecto. A solución foi implementar nós mesmos a serialización dos arrays para almacenalos en forma de texto na BD. Con este cambio, volvemos a medir o rendemento da operación de busca nas mesmas condicións que no apartado anterior, e o resultado foi o seguinte:

    Simon Stopwatch: [stopwatch INHERIT] total 2.34 s, counter 100, max 42.2 ms, min 12.1 ms
    StopwatchSample{total=2.34 s, counter=100, min=12.1 ms, max=42.2 ms, minTimestamp=121030-111239.918, maxTimestamp=121030-111241.042, active=0, maxActive=1, maxActiveTimestamp=121030-111241.696, last=28.8 ms, mean=23.4 ms, standardDeviation=8.42 ms, variance=7.169055643178661E13, varianceN=7.097365086746873E13, note=null}

A media subiu desde 18.6 a 23.4 milisegundos. A operación é algo máis lenta ca antes pero segue a ter un rendemento moi superior á implementación cunha fila por data.

######  Utilidade do modelo de datos plantexado

É interesante manter unha entidade cos datos agregados de tódalas asignacións a un recurso, pero non resulta útil de todo xa que cando os usuarios requiran incrementar o nivel de detalle estes datos non son suficientes. Na propia vista de carga de recursos móstranse datos dun nivel de detalle maior (asignacións a nivel de tarefa). Polo tanto, decidimos engadir esta modificación ao modelo:

-   [effort-cache-model-3.dia](/twiki/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-model-3.dia): Data model proposed to cache allocation data (C)

Engadimos unha relación opcional cun obxecto Task. A idea é que na BD de EffortSummary poida convivir:

-   A información xeral de asignación de un recurso. Nese caso, o valor da relación con Task é nulo.
-   A información específica de asignación de un recurso a unha tarefa.

######  Dificultade de actualización

Manter este modelo de datos actualizado resulta máis complexo do esperado. Hai que ter en conta que os datos de asignación debidos a distintas tarefas están gardados de xeito acumulativo, cando os datos dunha tarefa cambian hai que substraer a asignación anterior e sumar a nova asignación.

Por outra banda, hai que ter especial coidado os borrados en cascada. O comportamento por defecto é que cando se borre unha tarefa (ou un proxecto enteiro), as entidades 'débiles' asociadas a esa tarefa se borren tamén. Nembargantes, non podemos permitir que se borre un obxecto EffortSummary asociado a unha tarefa sen substraer o seu peso tamén do EffortSummary de información xeral asociado ao mesmo recurso.

 Solución proposta

Implementáronse operacións de adición e substracción na entidade EffortSummary para dar soporte a diversos casos de actualización. Sen embargo a casuística volveuse extremadamente complexa e non é desexable, polo que parece necesario unha visión de máis alto nivel para permitir unha implementación máis sinxela e, polo tanto, mantible.

Proponse o seguinte modelo de datos:

-   [effort-cache-virtual-model.dia](/twiki/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-virtual-model.dia): Data model proposed to cache allocation data with non persistent helper objects.

Ao modelo proposto anteriormente engádese unha capa de obxectos non persistentes que proporcionan unha visión máis global dos datos implicados, para simplificar a súa actualización. Os obxectos EffortSummary seguen a ser consultables directamente para acceder rápidamente aos datos que almacenan, que é a prioridade desta tarefa, pero non se manipulan directamente para as operacións de actualización.



####  Implementar vista de carga de recursos empregando o novo modelo dos datos de asignación

Para pór a proba o valor dos cambios que estamos a realizar, debemos implementar un caso de uso real. A vista de carga global de recursos de [LibrePlan](/twiki/LibrePlan/LibrePlan) fai un uso intensivo dos datos de asignación de recursos polo que é un gran candidato para a proba.

Tras implementar a vista de carga global de recursos empregando o novo modelo de datos de asignación, faremos probas e tomaremos medicións de rendemento en comparación coa implementación orixinal.

Para as probas partimos dun conxunto de 1000 tarefas repartidas entre 50 proxectos. Este conxunto de datos supón un exemplo significativo de uso de [LibrePlan](/twiki/LibrePlan/LibrePlan) nunha organización mediana/grande.

Os resultados indican que o algoritmo orixinal necesitaba unha media de 30.2 segundos para construir a carga global de recursos; coa nova implementación os resultados melloran moito e acadan os 2.02 segundos de media.

Resultados completos, algoritmo orixinal:

    Simon Stopwatch: [buildTimeLines INHERIT] total 160 s, counter 5, max 33.7 s, min 30.2 s
    StopwatchSample{total=160 s, counter=5, min=30.2 s, max=33.7 s, minTimestamp=121120-122826.603, maxTimestamp=121120-122944.698, active=0, maxActive=1, maxActiveTimestamp=121120-123205.861, last=30.9 s, mean=32.0 s, standardDeviation=1.24 s, variance=1.91147596224665754E18, varianceN=1.52918076979732608E18, note=null}

Resultados completos, algoritmo novo:

    Simon Stopwatch: [buildTimeLines INHERIT] total 10.1 s, counter 5, max 2.29 s, min 1.67 s
    StopwatchSample{total=10.1 s, counter=5, min=1.67 s, max=2.29 s, minTimestamp=121121-111728.678, maxTimestamp=121121-111551.732, active=0, maxActive=1, maxActiveTimestamp=121121-111727.010, last=1.67 s, mean=2.02 s, standardDeviation=202 ms, variance=5.1014395019862888E16, varianceN=4.0811516015890312E16, note=null}

O algoritmo novo mellora drásticamente os resultados, pero ten un custo á hora de salvar os proxectos porque ten que actualizar os datos das asignacións. Medimos este custo tamén para que a comparación sexa axeitada, e obtemos que a operación de gardado tarda agora 2.28 segundos máis de media para un proxecto dunhas 20 tarefas. Non é un incremento moi elevado, e ademáis pódese facer que non teña impacto na experiencia de usuario trasladándoo a unha operación en segundo plano.

Resultados completos operación de salvado:

    Simon Stopwatch: [updateAssignments INHERIT] total 25.0 s, counter 11, max 3.34 s, min 1.07 s
    StopwatchSample{total=25.0 s, counter=11, min=1.07 s, max=3.34 s, minTimestamp=121120-202957.188, maxTimestamp=121120-201620.181, active=0, maxActive=1, maxActiveTimestamp=121120-202956.118, last=1.07 s, mean=2.28 s, standardDeviation=542 ms, variance=3.2284608496745734E17, varianceN=2.9349644087950669E17, note=null}

Podemos concluir que este modelo de datos ten un impacto moi grande no rendemento da aplicación e polo tanto é interesante que este traballo forme parte de [LibrePlan](/twiki/LibrePlan/LibrePlan) nas próximas versións.

####  Seguintes pasos

Na implementación destas tarefas leváronse a cabo varias simplificacións para poder chegar máis rápido á fase de probas e comprobar se este esforzo era interesante para [LibrePlan](/twiki/LibrePlan/LibrePlan).

Para que este algoritmo poida formar parte de [LibrePlan](/twiki/LibrePlan/LibrePlan) imos precisar levar a cabo as seguintes tarefas:

-   Gardar EffortSummary para criterios. Agora mesmo só se estan gardando EffortSummaries para recursos.
-   EffortSummary.createFromResourceAllocations() ten que soportar GenericResourceAllocations.
-   Solucionar os problemas durante a creación dos EffortSummaries cando se salva o proxecto. Resumo dos problemas:
    -   Cando se borran unha tarefa ou unha asignación, o EffortSummary relacionado bórrase a través dun *cascade*, pero a tupla global de EffortSummary non se actualiza.
    -   O algoritmo de actualización é bastante complexo, como se comenta máis arriba, e é propenso a erros. Quizais sería mellor levar a cabo reemprazar a implementación actual coa a solución proposta.
-   "Enganchar" a nova implementación en LibrePlan, xa que para as probas enganchouse cun hack. Ten relación co seguinte punto.
-   O código para a vista global de carga de recursos está compartido co da vista de carga de recursos para un proxecto. Sen embargo, a implementación actual non serve para a vista de carga de recursos dun proxecto porque os EffortSummaries só se actualizan no momento en que se salva o proxecto. Hai que decidir entre:
    1.  Actualizar os EffortSummaries non só cando se salva senón tamén cando se abre a vista de carga de recursos dentro do proxecto.
    2.  Manter as dúas implementacións, unha para a vista global e outra para a específica.
-   Na vista global de carga de recursos, orixinalmente había unha fila por cada proxecto e na implementación actual non está.

###  User stories

-   [ItEr77S11AllocationDataPerformance](/twiki/LibrePlan/ItEr77S11AllocationDataPerformance)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 40                                                                                                                                                               | 40                                                                                                                                                                 | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                 | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                  | Create allocation data entity                                                                                                                                          |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |
| Task                                                                                                                                                               | 30                                                                                                                                                               | 30                                                                                                                                                                 | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                 | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                  | Implement save of allocation data information                                                                                                                          |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |
| Task                                                                                                                                                               | 40                                                                                                                                                               | 40                                                                                                                                                                 | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                 | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                                  | Implement resource load screen with the new allocation data model                                                                                                      |                                                                                                                                                                         |                                                                                                                                                                           |                                                                                                                                                                        |

[![](/twiki/TWiki/TWikiDocGraphics/toggleopen.gif)Attachments](#) [![](/twiki/TWiki/TWikiDocGraphics/toggleclose.gif)Attachments](#)

| [I](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Attachment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Action](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=2;table=3;up=0#sorted_table "Sort by this column")             | [Size](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=3;table=3;up=0#sorted_table "Sort by this column") | [Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Who](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Comment](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA03S04AllocationDataPerformance?sortcol=6;table=3;up=0#sorted_table "Sort by this column") |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![else](/twiki/TWiki/TWikiDocGraphics/else.gif)dia                                                                                                         | [effort-cache-model-2.dia](/twiki/pub/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-model-2.dia)                                                             | [manage](/twiki/bin/attach/LibrePlan/AnA03S04AllocationDataPerformance?filename=effort-cache-model-2.dia;revInfo=1 "change, update, previous revisions, move, delete...")       | 2.5 K                                                                                                                                                             | 25 Oct 2012 - 08:47                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | Data model proposed to cache allocation data (B)                                                                                                                     |
| ![else](/twiki/TWiki/TWikiDocGraphics/else.gif)dia                                                                                                         | [effort-cache-model-3.dia](/twiki/pub/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-model-3.dia)                                                             | [manage](/twiki/bin/attach/LibrePlan/AnA03S04AllocationDataPerformance?filename=effort-cache-model-3.dia;revInfo=1 "change, update, previous revisions, move, delete...")       | 2.7 K                                                                                                                                                             | 07 Nov 2012 - 10:35                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | Data model proposed to cache allocation data (C)                                                                                                                     |
| ![else](/twiki/TWiki/TWikiDocGraphics/else.gif)dia                                                                                                         | [effort-cache-model.dia](/twiki/pub/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-model.dia)                                                                 | [manage](/twiki/bin/attach/LibrePlan/AnA03S04AllocationDataPerformance?filename=effort-cache-model.dia;revInfo=1 "change, update, previous revisions, move, delete...")         | 2.7 K                                                                                                                                                             | 16 Oct 2012 - 15:34                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | Data model proposed to cache allocation data                                                                                                                         |
| ![else](/twiki/TWiki/TWikiDocGraphics/else.gif)dia                                                                                                         | [effort-cache-virtual-model.dia](/twiki/pub/LibrePlan/AnA03S04AllocationDataPerformance/effort-cache-virtual-model.dia)                                                 | [manage](/twiki/bin/attach/LibrePlan/AnA03S04AllocationDataPerformance?filename=effort-cache-virtual-model.dia;revInfo=1 "change, update, previous revisions, move, delete...") | 4.3 K                                                                                                                                                             | 13 Nov 2012 - 09:28                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | Data model proposed to cache allocation data with non persistent helper objects.                                                                                     |
| ![else](/twiki/TWiki/TWikiDocGraphics/else.gif)dia                                                                                                         | [modelo-calculo-cargas.dia](/twiki/pub/LibrePlan/AnA03S04AllocationDataPerformance/modelo-calculo-cargas.dia)                                                           | [manage](/twiki/bin/attach/LibrePlan/AnA03S04AllocationDataPerformance?filename=modelo-calculo-cargas.dia;revInfo=1 "change, update, previous revisions, move, delete...")      | 4.1 K                                                                                                                                                             | 16 Oct 2012 - 14:53                                                                                                                                               | [JacoboAragunde](/twiki/Main/JacoboAragunde)                                                                                                            | Resource load calculation class diagram                                                                                                                              |


