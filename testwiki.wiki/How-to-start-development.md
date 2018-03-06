# How To Start Development With JetBrains Intellij IDEA

## Download LibrePlan source code

You need to download LibrePlan source code to start hacking on it. You have two options:

a) Clone Git repository (recommended):

    `git clone git://github.com/LibrePlan/libreplan.git`

b) Download last version source code [here](http://sourceforge.net/projects/libreplan/files/LibrePlan/libreplan_*.tar.gz)
    
* Download latest libreplan_*.war file for your database (PostgreSQL or MySQL) [here](http://sourceforge.net/projects/libreplan/files/LibrePlan/)

You should review [this section](https://github.com/LibrePlan/libreplan/wiki/Compilation-requirements) to check that you have installed all the requirements.

***

## Import LibrePlan project

* Run Intellij IDEA

* Select Import Project

* Select directory with source code of Libreplan (e.g.`C:/Users/PC-User/IdeaProjects/libreplan`)

* Select `Import project from external model` > `Maven` and click `Next`

* Then leave all as default

* Then select profiles: `dev` and for PostgreSQL `users - postgresql` / Mysql `users - mysql`

* Then leave all by default

* Then choose your JDK(SDK), 1.8 strongly preferred

* Then define project name or leave default name

* Make `mvn clean install` in command line

***
## Configure project to run

* Go to `Run` > `Edit Configurations...`

* Create a new `Maven Build` called `MavenConfig`

* Change the following values:

  * Working directory: Choose ``libreplan-webapp`` folder in your workspace
  * Command line: ``jetty:stop jetty:run``
  * Profiles (optional): ``-userguide -reports -i18n``
    (to disable userguide,reports and i18n profiles to save compilation time
    as they are not mandatory to run LibrePlan)
  * Mark the following checkboxes (recommended):

>`Resolve Workspace artifacts`

>In `Before launch` section choose `+` and add `Build Artifact` (war file)

>Click `Run` and application will be available at http://localhost:8080/

***

## Develop LibrePlan in Intellij IDEA using MySQL

* The main development focus is on PostgreSQL and this tutorial focusses on PostgreSQL, but if you want to develop LibrePlan using MySQL you have to do 2 small changes:

  * In section `Configure project to run`_ you have to set the *Profiles* to:
    ``dev mysql -userguide -reports -i18n``

* Remember that the three last profiles that are being disabled is just to save
  compilation time and not mandatory. However, to develop using MySQL you have
  to set at least the first two: ``dev`` and ``mysql``.

***
# How To Start Development With Eclipse

***

Download LibrePlan source code

You need to download LibrePlan source code to start hacking on it. You have two
options:

a) Clone Git repository (recommended):

    `$ git clone git://github.com/Igalia/libreplan.git`

b) Download last version source code:

    `$ wget http://downloads.sourceforge.net/project/libreplan/LibrePlan/libreplan_1.2.0.tar.gz`
    `$ tar -xzvf libreplan_1.2.0.tar.gz`

You should review [this section](https://github.com/LibrePlan/libreplan/wiki/Compilation-requirements) to check that you have installed all the requirements.

***

## Download Eclipse Java EE

* Go to download Eclipse [page](http://www.eclipse.org/downloads/)

* Download Eclipse IDE for `Java EE Developers` for your architecture

![Eclipse downloads webpage](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-download-eclipse.png?raw=true)

***

## Install Ecliplse


* Go to ``/opt/`` (or any other folder when you want to install Eclipse): `# cd /opt/`

* Uncompress downloaded file and set proper permissions:

  `# tar -xzvf ~/Downloads/eclipse-jee-indigo-SR1-linux-gtk-x86_64.tar.gz`                   
  `# chown -R root:root eclipse/`                  

* Add symbolic link to launch Eclipse:

  `# cd /usr/local/bin/`         
  `# ln -s /opt/eclipse/eclipse`                      


***

## Install Eclipse Maven plugin (m2e)

* Run Eclipse: `$ eclipse`

* Choose your workspace folder (or accept the default one) and mark to don't ask
  about it again

* Go to `Help` -> `Install New Software...`

* Click in option `Add` and set the following values and click `Ok`:

  * Name: `m2e`
  * Location: `http://download.eclipse.org/technology/m2e/releases/`

* Click `Next` to install plugin

![Instal Eclipse Maven plugin (m2e)](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-m2e.png?raw=true)

* Accept license agreements and click `Finish`

* Restart Eclipse once plugin installation has finished

***

## Import LibrePlan project

* Go to `File` -> `Import`

* Select as import source `Maven` -> `Exising Maven Projects` and click `Next`

![Import LibrePlan as Maven project](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-import-maven.png?raw=true)

* Set as `Root Directory` the path where you downloaded LibrePlan source code

* Then mark all projects and click `Finish`

![Import LibrePlan from existent path](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-poms.png?raw=true)

* It is recommended to close ``libreplan`` project (right click over the project
  and choose `Close`)

***

## Configure project to run

* Go to `Run` -> `Run Configurations...`

* Create a new `Maven Build` called `New_configuration`

* Change the following values:

  * Name: `LibrePlan`
  * Base directory: Choose ``libreplan-webapp`` folder in your workspace
  * Goals: ``jetty:stop jetty:run``
  * Profiles (optional): ``-userguide,-reports,-i18n`` (to disable userguide,
    reports and i18n profiles to save compilation time as they are not
    mandatory to run LibrePlan)
  * Mark the following checkboxes (recommended):

    * Resolve Workspace artifacts
    * Update Snapshots
    * Skip Tests

    ![Configure how to run LibrePlan in Eclipse](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-run-configurations.png?raw=true)

* Click `Run` and application will be available at http://localhost:8080/

***

## Configure Maven profiles

* For each opened project in the *Project Explorer* (``ganttzk``,
  ``libreplan-business``, ``libreplan-webapp``) configure Maven profiles to save
  compilation time (this is not mandatory):

  * Right click over the project and go to `Properties`

  * Look for `Maven` and set `Active Maven Profiles`:
    ``-userguide,-reports,-i18n``

![Project properties window](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-maven-profiles.png?raw=true)

***

## Configure Eclipse to follow coding style guidelines

* Go to `Window` -> `Preferences`

* Look for the different options to use always spaces instead of tabs and use 4
  spaces size for indentation

![Eclipse Preferences window](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-preferences-tab.png?raw=true)

* Create new profile to follow the coding style guidelines

![New profile based on Eclipse default one](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-eclipse-profile.png?raw=true)

* Configure `Save Actions` marking the following options:

  * Perform the selected actions on save
  * Format source code
  * Format edited lines
  * Organize imports

![Save Actions configuration](https://github.com/LibrePlan/libreplan/blob/master/doc/src/technical/img/libreplan-preferences-save-actions.png?raw=true)

***

## Develop LibrePlan in Eclipse using MySQL

* This tutorial works properly with PostgreSQL, but if you want to develop
  LibrePlan using MySQL you have to do 2 small changes:

  * In section `Configure project to run`  you have to set the *Profiles* to:
    ``dev,mysql,-userguide,-reports,-i18n``

  * In section `Configure Maven profiles`  you have to set *Active Maven
    Profiles* to: ``dev,mysql,-userguide,-reports,-i18n``

* Remember that the three last profiles that are being disabled is just to save
  compilation time and not mandatory. However, to develop using MySQL you have
  to set at least the first two: ``dev`` and ``mysql``.