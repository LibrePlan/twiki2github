[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Documentation](LibrePlan_Documentation "Topic revision: 25 (15 Jan 2013 - 08:27:28)") (15 Jan 2013, [LorenzoTilve](Main_LorenzoTilve))[Edit](LibrePlan_Documentation?t=1520343626 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/Documentation "Attach an image or document to this topic")  

 Documentation
==============

-   [Users Documentation](LibrePlan_Documentation#Users_Documentation)
    -   [Installation & Update](LibrePlan_Documentation#Installation_Update)
    -   [Manual](LibrePlan_Documentation#Manual)
    -   [Web Services](LibrePlan_Documentation#Web_Services)
-   [I18n Documentation](LibrePlan_Documentation#I18n_Documentation)
-   [Developers Documentation](LibrePlan_Documentation#Developers_Documentation)
    -   [Code Conventions](LibrePlan_Documentation#Code_Conventions)
    -   [Database Conventions](LibrePlan_Documentation#Database_Conventions)
    -   [Commit Messages Format](LibrePlan_Documentation#Commit_Messages_Format)
    -   [License Header](LibrePlan_Documentation#License_Header)
    -   [Database Changes](LibrePlan_Documentation#Database_Changes)
    -   [Compilation](LibrePlan_Documentation#Compilation)
    -   [LibrePlan in Eclipse](LibrePlan_Documentation#LibrePlan_in_Eclipse)
    -   [Reports (JasperReports)](LibrePlan_Documentation#Reports_JasperReports)
    -   [Use Case Development](LibrePlan_Documentation#Use_Case_Development)
    -   [Hibernate Second Level Cache](LibrePlan_Documentation#Hibernate_Second_Level_Cache)
        -   [Activation](LibrePlan_Documentation#Activation)
        -   [Debugging](LibrePlan_Documentation#Debugging)
    -   [Performance Tunning](LibrePlan_Documentation#Performance_Tunning)
    -   [Git Version Control System](LibrePlan_Documentation#Git_Version_Control_System)

 Users Documentation
--------------------

###  Installation & Update

-   [LibrePlan installation instructions](http://www.libreplan.org/INSTALL.html)
-   [LibrePlan upgrade instructions](http://www.libreplan.org/UPDATE.html)
-   [HOWTO - Migration from LibrePlan 1.1.X to LibrePlan 1.2 for source and war deployments](LibrePlan_HowToMigrateNavalPlanToLibrePlan)

###  Manual

-   [Manual](http://libreplan.sourceforge.net/user-documentation/en/) \[[es](http://libreplan.sourceforge.net/user-documentation/es/)\] \[[gl](http://libreplan.sourceforge.net/user-documentation/gl/)\]

###  Web Services

-   [LibrePlan Web Services](http://libreplan.org/libreplan-web-services.html)

 I18n Documentation
-------------------

-   [Documentation](LibrePlan_I18nDocumentation)

 Developers Documentation
-------------------------

###  Code Conventions

-   Use 4-spaces to ident source code. Never use tabs.
-   Avoid trailing whitespaces.
-   Follow Java conventions (<http://java.sun.com/docs/codeconv/>)

###  Database Conventions

-   Always use lower-case for tables and columns names. E.g. `worker`
-   Use underscore to separate words on tables and columns names. E.g. `virtual_worker`
-   Add suffix `_table` when table name is a reserved word. E.g. `order_table`
-   Use prefix `idx_` for indexes. E.g. `idx_label_on_label_type`
-   Use suffix `_pkey` for primary keys: E.g. `stretch_template_pkey`
-   Use suffix `_fkey` for foreign keys: E.g. `stretch_template_stretches_function_template_id_fkey`

###  Commit Messages Format

-   Standard commit messages:

        Title (one line)

        Optional description (several lines)

-   If it fixes a bug:

        Bug #bug_number_at_bugtracker: Title (one line)

        Optional description (several lines)

-   You can also add tags in some situations, e.g.:

        doc: Title (one line)

        Optional description (several lines)

###  License Header

-   Add the next header at the beginning of each file filling the year and copyright holder:

&nbsp;

    /*
     * This file is part of LibrePlan
     *
     * Copyright (C) YEAR Copyright Holder (OOPS!)
     *
     * This program is free software: you can redistribute it and/or modify
     * it under the terms of the GNU Affero General Public License as published by
     * the Free Software Foundation, either version 3 of the License, or
     * (at your option) any later version.
     *
     * This program is distributed in the hope that it will be useful,
     * but WITHOUT ANY WARRANTY; without even the implied warranty of
     * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     * GNU Affero General Public License for more details.
     *
     * You should have received a copy of the GNU Affero General Public License
     * along with this program.  If not, see <http://www.gnu.org/licenses/>.
     */

###  Database Changes

We are using [LiquiBase](http://www.liquibase.org/) as tool to manage database migration and it is integrated with Maven so you just need to run `mvn clean install` in order to automatically apply migrations on database.

These database changelog files are under `libreplan-business/src/main/resources/` directory.

During the development if you need to modify the database you should add a change set to the database chagelog file corresponding to current version (before version 1.0 we will use the file `db.changelog-initial.xml`, a new file will be created for each version). Check all the possible database refactorings in the manual: <http://www.liquibase.org/manual/home#available_database_refactorings>

Some examples of common tasks to be added in database changelog:

-   Rename table:

&nbsp;

    <changeSet id="rename-table-worker-to-employee" author="mrego">
        <comment>Rename table</comment>
        <renameTable oldTableName="worker" newTableName="employee" />
    </changeSet>

-   Rename column:

&nbsp;

    <changeSet id="rename-column-nif-to-identify_number" author="mrego">
        <comment>Rename column</comment>
        <renameColumn tableName="worker" oldColumnName="nif"
            newColumnName="identity_number"/>
    </changeSet>

-   Add a column with a default value:

&nbsp;

    <changeSet id="add-has_children-column-with-default-value-false" author="mrego">
        <comment>Add new column with default value</comment>
        <addColumn tableName="worker">
            <column name="has_children" type="BOOLEAN" />
        </addColumn>
        <update tableName="worker">
            <column name="has_children" valueBoolean="TRUE" />
        </update>
    </changeSet>

***![ALERT!](/twiki/pub/TWiki/TWikiDocGraphics/warning.gif "ALERT!") Warning***: `id` must be unique for each author in the same file but can not exceed 60 characters. If you have collisions you can add `-1`, `-2`, ... at the end.

***![HELP](/twiki/pub/TWiki/TWikiDocGraphics/help.gif "HELP") Note***: Please add a comment explaining why you are modifying the database. You can add all the changes related with a commit in the same change set.

###  Compilation

-   [LibrePlan compilation instructions](http://www.libreplan.org/HACKING.html)

###  LibrePlan in Eclipse

-   [How To Start Development With Eclipse](http://www.libreplan.org/howto-start-development-with-eclipse.html)

###  Reports (JasperReports)

-   [How To Create A New Report In LibrePlan](http://www.libreplan.org/howto-create-a-new-report-in-libreplan.html)

###  Use Case Development

-   [How To Develop A Use Case In LibrePlan](http://www.libreplan.org/howto-develop-a-use-case-in-libreplan.html)

###  Hibernate Second Level Cache

####  Activation

In file `libreplan-business/src/main/resources/libreplan-business-hibernate.cfg.xml` change value of property `hibernate.cache.use_second_level_cache` to `true`.

####  Debugging

In order to see in the screen the output log of access, successes and failures of cache, it's needed to add following lines to file `src/main/jetty/log4j.properties`:

    # Enable to log cache activity
    log4j.logger.org.hibernate.cache=debug

###  Performance Tunning

-   [PerformanceTuning](LibrePlan_PerformanceTuning)

###  Git Version Control System

-   [How to use Git in LibrePlan](LibrePlan_LibrePlanGit)
