## Profile description

There are different compilation profiles. Check ``<profiles>``
section in root `pom.xml` to see the different profiles (there are also some
profiles defined in `pom.xml` of business and webapp modules).

* *dev* - Development environment (default)

  It uses databases `libreplandev` and `libreplandevtest`.

* *prod* - Production environment

  Unlike *dev* it uses database `libreplanprod` and `libreplanprodtest`.

  It is needed to use it in combination with *postgresql* or *mysql* profiles.

  This is usually used while testing the stable branch in the repository. This
  allows developers to easily manage 2 different databases one for last
  development in master branch and another for bugfixing over stable branch.

* *postgresql* - PostgreSQL database (default)

  It uses PostgreSQL database server getting database names from *dev* or *prod*
  profiles.

* *mysql* - MySQL database

  It uses MySQL database server getting database names from *dev* or *prod*
  profiles.

* *reports* - JasperReports (default)

  If it is active *LibrePlan* reports are compiled.

  It is useful to disable this profile to save compilation time during
  development.

* *userguide* - User documentation (default)

  If it is active *LibrePlan* help is compiled and HTML files are generated.

  User documentation is written in *reStructuredText* and it is generated
  automatically thanks to this profile.

  Like for *reports*, it is useful deactivate this profile during development
  to save compilation time.

* *liquibase-update* - Liquibase update (default)

  If it is active Liquibase changes are applied in the database.

* *liquibase-updatesql* - Liquibase update SQL

  If it is active it is generated a file with SQL sentences for Liquibase
  changes needed to apply on database.

  This is used to generate upgrade files in releases.

* *i18n* - Internationalization (default)

  It uses gettext to process language files in order to be used in *LibrePlan*.

  Like for *reports* and *userguide*, it is useful deactivate this profile
  during development to save compilation time.

***
## How to use profiles

Profiles active by default are used always if not deactivated. In order to
activate or deactivate a profile you should use parameter ``-P`` for Maven
command. For example:

* Deactivate *reports*, *userguide* and *i18n* to save compilation time:

   ` mvn -P-reports,-userguide,-i18n clean install`

* Use production environment:

    `mvn -Pprod,postgresql clean install`

***
## Compilation options

In LibrePlan there are two custom Maven properties, which allow you to configure
some small bits in the project.

* *default.passwordsControl* - Warning about default passwords (``true`` by
  default)

  If this option is enabled, a warning is show in LibrePlan footer to
  application administrators in order to change the default password (which
  matches with user login) for the users created by default: admin, user,
  wsreader and wswriter.

* *default.exampleUsersDisabled* - Disable default users (``true`` by default)

  If true, example default users such as user, wsreader and wswriter are
  disabled. This is a good option for production environments.

  This option is set to ``false`` if you are using the development profile (the
  default one).

* *default.deleteAllProjectsButtonDisabled* - Disable "Delete all projects" button (``true`` by default)

  If true, "Delete all projects" button is disabled and you don't see it.

  This option is set to `false` if you are using the development profile (the
  default one). 

***
## How to set compilation options

Maven properties have a default value, but you can change it using the parameter
``-D`` for Maven command to set the value of each option you want to modify. For
example:

* Set `default.passwordsControl` to ``false``:

    `mvn -Ddefault.passwordsControl=false clean install`

* Set `default.passwordsControl` and `default.exampleUsersDisabled` to `false`:

    `mvn -Ddefault.passwordsControl=false -Ddefault.exampleUsersDisabled=false clean install`

* Set `default.emailSendingEnabled` to `false`:

    `mvn -Ddefault.emailSendingEnabled=false clean install`

* Set `default.deleteAllProjectsButtonDisabled` to `false`:

    `mvn -Ddefault.deleteAllProjectsButtonDisabled=false clean install`

***
## Tests

*LibrePlan* has a lot of JUnit test that by default are passed when you compile
the project with Maven. You can use ``-DskipTests`` to avoid tests are passed
always. Anyway, you should check that tests are not broken before sending or
pushing a patch.

  `mvn -DskipTests clean install`

***
## MySQL Database

Note: The default LibrePlan database used is PostgreSQL. This is also the main focus of development.
If you insist on using MySQL that is possible, but again, it is not the main focus of development.

Strongly preferred to use 5.6+ version.

For MySQL users here are specific instructions.

* SQL sentences to create database:

    `CREATE DATABASE libreplandev;`              
    `CREATE DATABASE libreplandevtest;`                   
    `CREATE USER 'libreplan'@'localhost' IDENTIFIED BY 'libreplan';`                      
    `GRANT ALL PRIVILEGES ON libreplandev.* TO 'libreplan'@'localhost' WITH GRANT OPTION;`                 
    `GRANT ALL PRIVILEGES ON libreplandevtest.* TO 'libreplan'@'localhost' WITH GRANT OPTION;`               

* Compile project:

    `$ mvn -Pdev,mysql clean install`

* Launch application:

    `$ cd libreplan-webapp/`               
    `$ mvn -Pdev,mysql jetty:run`                        

