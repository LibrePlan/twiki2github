[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA22S01AutomaticBudgeting](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting "Topic revision: 1 (07 Jun 2013 - 08:29:51)") (07 Jun 2013, [LorenzoTilve](/twiki/Main/LorenzoTilve))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA22S01AutomaticBudgeting?t=1520337868 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA22S01AutomaticBudgeting "Attach an image or document to this topic")

 [AnA22S01AutomaticBudgeting](/twiki/LibrePlan/AnA22S01AutomaticBudgeting)
================================================================================================================================



|                        |                                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| Story summary          | Automatic budgeting based on task criteria requirement and hour estimations        |
| Iteration              | [AnA22AutomaticBudgeting](/twiki/LibrePlan/AnA22AutomaticBudgeting)       |
| FEA                    | [AnA22S01AutomaticBudgeting](/twiki/LibrePlan/AnA22S01AutomaticBudgeting) |
| Story Lead             |                                                                                    |
| Next Story             |                                                                                    |
| Passed acceptance test | No                                                                                 |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

2.1. Asociación entre criterios y categorías de coste Para poder realizar la presupuestación de las tareas de forma automática tenemos que permitir asociar un criterio a una categoría de coste. De este modo tendremos un precio por hora para el criterio requerido por la tarea, el cual nos permitirá calcular el presupuesto de forma automática. Para esto se modificará la interfaz de gestión de tipos de criterios, permitiendo seleccionar una categoría de coste para cada uno de los criterios. De modo que dicha asociación quede almacenada en la base de datos. En caso de que una tarea no requiera ningún criterio, el valor del presupuesto calculado será 0. Esto se implementará, sin ser parte de este presupuesto, a través de una categoría de coste por defecto, que se configurará con un precio por hora de 0 para obtener el efecto deseado.

2.2. Configuración del tipo de horas para el cálculo del presupuesto Una categoría de coste define uno o varios precios por hora (dependiendo de las fechas) para cada tipo de horas definido en [LibrePlan](/twiki/LibrePlan/LibrePlan). Para poder realizar una presupuestación automática, tenemos que decidir que tipo de hora se va a utilizar en el cálculo. Se añadirá un nuevo campo en la ventana de “Ajustes principales” que permita la selección del tipo de horas para la presupuestación automática.

2.3. Creación nueva columna de presupuesto total en el árbol de tareas Se modificará el árbol de tareas de un proyecto para añadir una nueva columna con el presupuesto calculado. De forma que para cada tarea tendríamos las siguientes columnas (que interfieren en el cálculo del presupuesto): Horas: Representa las horas estimadas para cada tarea. Este campo ya existe actualmente y su comportamiento no se modificará. Gastos: En esta columna se va a establecer el presupuesto de gastos para cada tarea (en el caso de SOMABE serían los gastos de materiales). Tendrá el mismo comportamiento que tiene ahora mismo la columna “Presupuesto”, pero cambiará su significado pasando de ser el presupuesto para toda la tarea (incluyendo las horas) al presupuesto referente a gastos. Presupuesto: Está será la nueva columna, que representará el presupuesto total de la tarea. La cual será de sólo lectura por lo que el usuario no podrá modificar su valor. El valor de esta columna se calculará de forma automática dependiendo de las dos columnas anteriores (“Horas” y “Gastos”) y el criterio requerido por la tarea.

Para establecer el valor de la columna de “Presupuesto” se realizará el siguiente cálculo: Se obtendrá el precio por hora para la tarea a partir del criterio requerido por la misma, la categoría de coste asociada a dicho criterio y el tipo de horas para la presupuestación automática configurada. En caso de que no haya ningún criterio se utilizará la categoría de coste por defecto (que como se explicó anteriormente en este caso estará configurada a 0). Una vez tengamos el precio por hora se multiplicará el valor de la columna “Horas” y tendremos el presupuesto de horas. La columna “Presupuesto” se rellenará con la suma del presupuesto de horas (calculado en el punto anterior) y el presupuesto de gastos (obtenido de la columna “Gastos”).

2.4. Inclusión en el informe de estado el proyecto información sobre esta nueva columna La información de esta nueva columna será incluida en el informe de estado del proyecto. De manera que el informe permita comparar el coste total, de horas o de gastos con el presupuesto correspondiente. Para esto se modificará el informe para que tenga las siguientes columnas: Presupuesto total: El presupuesto total que se corresponde con la nueva columna “Presupuesto” en el árbol de tareas. Presupuesto de horas: El presupuesto de horas calculado a partir de las horas estimadas y el criterio requerido por la tarea. Presupuesto de gastos: El presupuesto de gastos establecido en la columna “Gastos” del árbol de tareas. Coste de horas: El coste real de horas según los partes de trabajo. Esta columna se comparará con el “Presupuesto de horas” para indicar si se ha superado el valor presupuestado de horas. Coste de gastos: El coste real de los gastos según las hojas de gasto. En este caso la comparación se hará contra el “Presupuesto de gastos”. Coste total: El coste total de la tarea que será la suma de las dos columnas anteriores. La comparación aquí será contra la columna de “Presupuesto”.

-- [LorenzoTilve](/twiki/Main/LorenzoTilve) - 07 Jun 2013

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA22S01AutomaticBudgeting?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                        | 0                                                                                                                                                         | 0                                                                                                                                                           | 0                                                                                                                                                           | Low                                                                                                                                                        |                                                                                                                                                                |                                                                                                                                                                 | Implementation                                                                                                                                                  |                                                                                                                                                                  |                                                                                                                                                                    |                                                                                                                                                                 |


