[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA05S11CacheTuning](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning "Topic revision: 3 (26 Mar 2012 - 18:26:13)") (26 Mar 2012, [DiegoPino](/twiki/Main/DiegoPino))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA05S11CacheTuning?t=1520337836 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA05S11CacheTuning "Attach an image or document to this topic")

 [AnA05S11CacheTuning](/twiki/LibrePlan/AnA05S11CacheTuning)
===========================================================================================================



|                        |                                                                      |
|------------------------|----------------------------------------------------------------------|
| Story summary          | Cache Tuning                                                         |
| Iteration              | [AnA04Architecture](/twiki/LibrePlan/AnA04Architecture)     |
| FEA                    | [AnA05S11CacheTuning](/twiki/LibrePlan/AnA05S11CacheTuning) |
| Story Lead             |                                                                      |
| Next Story             |                                                                      |
| Passed acceptance test | No                                                                   |

###  Acceptance Criteria

**Objetivo**

-   Mejorar la *performance* general de [LibrePlan](/twiki/LibrePlan/LibrePlan) a través de la activación de cachés y técnicas de recuperación de entidades de antemano.
-   Activar cachés para entidades que se utilicen habitualmente o que apenas se escriban: *Labels*, *Criteria*, *Resources*, *Calendars*.

**Notas de Jacobo**

<http://wiki.libreplan.org/twiki/LibrePlan/Documentation#Hibernate_Second_Level_Cache>

**Tipos de caches**

En Hibernate hay 3 tipos de cache

-   *First level cache* (*Session cache*). Activada por defecto. Cachea objetos dentro de una misma sesión.
-   *Query-level cache*. Cachea consultas y sus resultados. Recomendable para consultas que se ejecutan frecuentemente con los mismos parámetros.
-   *Second-level cache*. Cachea objetos entre sesiones.

**Second-level cache**

La second-level cache viene desactivada por defecto. Para activarla es necesario indicar un cache provider y configurar cada entidad con un tipo de estrategia de cache.

**Cache Providers**

En Hibernate hay 4 tipos de cache providers (módulos que implementa la second level cache):

-   *EHCache*. Para una sóla máquina JVM o un cluster. Cache en memoria o disco y soporta query result cache.
-   *OSCache*. Lo mismo que la anterior pero sin soporte para clúster. Ofrece un rico conjunto de polítcias de expiración.
-   *SwamScache*. Cluster caché basada en JGroups. No soporta query cache.
-   *JBoss Cache*. También basada den JGroups. Soporta replicación, invalidación, comunicación síncronca o asíncrona, y optimistic y pessimistic locking. Soporta query cache.

**Tipos de estrategias**

-   *read-only*. Para entidades que solo sea necesario leer, y nunca escribir.
-   *nonstrict-read-write*. Los datos se cachean pero la cache solo se refresca cuando ha vencido el tiempo de expiración de la cache.
-   *read-write*. Como el anterior pero la cache se invalida también cuando se escribe un dato que había en cache.
-   *transactional*. Proporciona soporte de cache para proveedores de cache totalmente transaccionales como JBoss TreeCache[?](/twiki/bin/edit/LibrePlan/TreeCache?topicparent=LibrePlan.AnA05S11CacheTuning "Create this topic") . Este tipo de cache solo se puede utilizar en un JTAenvironment.

**Relación Cache Providers - Tipos de cache**

|            |           |                      |            |               |
|------------|-----------|----------------------|------------|---------------|
| Módulo     | Read-only | Nonstrict-read-write | Read-write | Transactional |
| EHCache    | 1         | 1                    | 1          | 0             |
| OSCache    | 1         | 1                    | 1          | 0             |
| SwamCache  | 1         | 1                    | 0          | 0             |
| JBossCache | 1         | 0                    | 0          | 1             |

**¿Cómo saber que se está produciendo un acierto de caché?**

Una manera es usar *Hibernate SessionFactory* para obtener estadísticas acerca de los aciertos de cache. Para activar estadísticas de caché en el *SessionFactory*:

    <prop key="hibernate.show_sql">true</prop>
    <prop key="hibernate.format_sql">true</prop>
    <prop key="hibernate.use_sql_comments">true</prop>
    <prop key="hibernate.cache.use_query_cache">true</prop>
    <prop key="hibernate.cache.use_second_level_cache">true</prop>
    <prop key="hibernate.generate_statistics">true</prop>
    <prop key="hibernate.cache.use_structured_entries">true</prop>

Otras posibilidad es crear tests para ver si se producen aciertos de cache.

El libro de Hibernate dice: *"Your application should perform satisfactorily without the second-level cache. You've only cured the symptons, not the actual problem if a particular procedure in your application is running in 2 instead of 50 seconds wth the second level cache enbaled. Customization of the fetch plan and fetching strategy is always your first optimization step; then, use the second-vlevel cache to make your application snappier and to scale it to the concurrent transaction load it will have to hadle in production"*.

**NOTA:** Hacer profiling para ver si se produce rendimiento

**Batch-size**

**Problema de las n + 1 queries**

Cuando se tienen configurados objetos *lazy* y hace falta inicializarlos es necesario hacer n+1 queries. Es decir, una query para inicializar la colección y una query por atributo para inicializar el objeto. El libro de Hibernate comenta que hay varias estrategias para evitar esto (pág 587)

-   Especificar prefetching en lotes. En el hbm.xml se especifica hacer prefetching de una entidad si se accede a ella, por ejemplo:

    <set name="bids" inverse="true" batch-size="10">
       <key column="ITEM_ID"/>
       <one-to-many classs="Bid"/>
    </set>

-   Con un prefetch basado en una subselect. Se reduce a exactamente 2.

    <set name="bids" inverse="true" fetch="subselect">
       <key column="ITEM_ID"/>
       <one-to-many classs="Bid"/>
    </set> 

-   La ultima estrategia es deshabilitar la capacidad *lazy* y pasar a *eager*

    <set name="bids" inverse="true" fetch="join">
       <key column="ITEM_ID"/>
       <one-to-many classs="Bid"/>
    </set> 

Esta última estrategia es desaconsejable porque estas configuraciones son a nivel global. Con la última estrategia siempre se van a traer los objetos bid incluso cuando solo se accede al objeto que los contiene.

Otra posibilidad es hacer el fetching dinámicamente con una query.

    List<Item> allItems = session.createQuery("from Item left join fetch i.bids").list();

    List<Item> allItems = session.createCriteria(Item.class).setFetchMode("bids", FetchMode.JOIN).list();

El libro de Hibernate aconseja inicializar en batch process con un número de 3 - 15.

Pagina 591 *"Optimization step by step"*

-   Nosotros no utilizamos estrategias *fetch="join"* de hecho son desaconsejables porque trabajamos todo con *lazy*.
-   Ver parametro *hibernate\_max\_fetch\_depth*.
-   Aconseja *fetch="join"* en relaciones *one-to-one* y *many-to-one*. También aconseja en one-to-many si estamos totalmente seguros.

**Referencias**

<http://acupof.blogspot.com/2008/01/background-hibernate-comes-with-three.html> <http://blog.dynatrace.com/2009/02/16/understanding-caching-in-hibernate-part-one-the-session-cache/> <http://docs.jboss.org/hibernate/orm/3.3/reference/en/html/performance.html#performance-cache>

###  Additional Specification Comments

###  Implementation Notes

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=3;table=3;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=4;table=3;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=5;table=3;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=6;table=3;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=7;table=3;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=8;table=3;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=9;table=3;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=10;table=3;up=0#sorted_table "Sort by this column") |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                 | 0                                                                                                                                                  | 0                                                                                                                                                    | 0                                                                                                                                                    | Low                                                                                                                                                 | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                           | [DiegoPino](/twiki/Main/DiegoPino)                                                                                                              | Implementation                                                                                                                                           |                                                                                                                                                           |                                                                                                                                                             |                                                                                                                                                          |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=0;table=4;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=1;table=4;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=2;table=4;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA05S11CacheTuning?sortcol=3;table=4;up=0#sorted_table "Sort by this column") |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [DiegoPino](/twiki/Main/DiegoPino)                                                                                                         | 0                                                                                                                                                                 | 0                                                                                                                                                                 | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                   |
| Total                                                                                                                                               | 0                                                                                                                                                                 | 0                                                                                                                                                                 | ![DONE](/twiki/TWiki/TWikiDocGraphics/choice-yes.gif "DONE")                                                                                   |

------------------------------------------------------------------------
