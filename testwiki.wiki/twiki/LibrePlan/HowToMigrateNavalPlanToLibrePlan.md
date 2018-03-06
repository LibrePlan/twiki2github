[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[Documentation](/twiki/LibrePlan/Documentation)&gt;[HowToMigrateNavalPlanToLibrePlan](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/HowToMigrateNavalPlanToLibrePlan "Topic revision: 3 (20 Aug 2012 - 09:52:47)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/HowToMigrateNavalPlanToLibrePlan?t=1520337872 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/HowToMigrateNavalPlanToLibrePlan "Attach an image or document to this topic")

 HOWTO - Data migration from LibrePlan 1.1.X to LibrePlan 1.2 for compiled and war installations
---------------------------------------------------------------------------------------------------------------------------------------------------

If you are using Ubuntu or Debian packages there is a transitional package available to migrate all data from LibrePlan database to LibrePlan database. This migration essentially implies two phases: database renaming and schema updates.

This guide is intended to ease the migration for those running a manual installation of LibrePlan 1.1.x, i.e., those who installed the software through a WAR file (either downloaded from the Internet or created by compiling the source code from scratch).

Please note that in this guide it is assumed that the application database name is "navalplan". So, if this is not the case, *just replace "navalplan" in step 5* by the name of your *NavalPlan* database.

Besides, this procedure has been tested in Debian, but it probably can be used without any adaptation in other *GNU/Linux* distributions.

Go through the following steps **BEFORE** deploying *LibrePlan 1.2*. Create a **BACKUP** of your old database and stop Tomcat before proceeding.

###  STEPS

####  0) Switch to PostgreSQL administrative user and fire up the interactive terminal.

    root@hostname:~# su - postgres
    postgres@hostname:~$ psql
    psql (9.0.4)
    Type "help" for help.

    postgres=#

####  1) Create a new database for LibrePlan 1.2:

    postgres=# CREATE DATABASE libreplan;
    CREATE DATABASE

####  2) Create a new username:

    postgres=# CREATE USER libreplan WITH PASSWORD 'libreplan';
    CREATE USER

####  3) Grant privileges to the user:

    postgres=# GRANT ALL PRIVILEGES ON DATABASE libreplan TO libreplan;
    GRANT

####  4) Exit the interactive PosgreSQL session:

    postgres=# \q
    postgres@hostname:~$

####  5) Dump old database

    postgres@hostname:~$ pg_dump navalplan > /tmp/navalplan_1.1.x.sql
    postgres@hostname:~$

(You should use a different destination directory for the dump if you're sharing the machine with someone else and you don't want your data to be read)

####  6) Load the dump into the new database

    psql -U libreplan -h localhost libreplan < /tmp/navalplan_1.1.x.sql

####  7) Download the corresponding SQL file with the upgrade from SourceForge:

    wget http://sourceforge.net/projects/navalplan/files/LibrePlan/upgrade_1.2.0.sql/download -O /tmp/upgrade_1.2.0.sql

####  8) Apply it:

    psql -U libreplan -h localhost libreplan < /tmp/upgrade_1.2.0.sql

####  9) You can now deploy Libreplan 1.2 by dropping the war file directly into the webapps directory)

####  10) You're done.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) Don't remove the old database before making sure the upgrade was applied correctly and no data was lost.

![warning](/twiki/TWiki/TWikiDocGraphics/warning.gif) Also, don't forget to delete any temporary file created during the upgrade.
