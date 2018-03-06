## Features


* Resource management:

  * Two type of resources: machines and workers.
  * Flexible calendars easily reusable.
  * Resource configuration based on skills and roles.

* Planning:

  * Simple way to configure and estimate the work to plan. It is carried out
    through Work Breakdown Structures ([WBS](http://en.wikipedia.org/wiki/Work_Breakdown_Structure)).
  * Different detail levels during the planning.
  * Two ways to allocate resources:

    * Specific allocation: Concrete individuals.
    * Assisted generic allocation: Based on skills and roles fulfilled by the
      resources.

  * Templates to reuse work. Projects can be created based on templates for
    repeatable tasks being able to save time.

  * Automatic resource reallocation in order to minimize overload (overtime).

  * Advanced allocation. Manual configuration of daily work hours on a task
    when automatic allocation does not suit your needs.

  * Monte Carlo method. Statistical simulation to calculate the possibility to
    complete a project in a range of dates.

* Projects control and monitoring:

  * Company global analysis.

  * [Earned Value Management](http://en.wikipedia.org/wiki/Earned_Value_Management). Project management method to objectively
    measure progress and performance of a project.

  * Planning quality management. It is possible to control quality of the tasks
    to be performed through forms.

  * Projects cost analysis.

  * Reported hours: worked hours are assigned to each task to track costs during
    the planning

  * Progress measurement through different unit types.

* Outsourcing

  LibrePlan provides support for companies that do outsourcing:

  * Project tasks can be outsourced and sent to the LibrePlan installation of
    the supplier.

  * You can receive progress notifications of the subcontractors to know how
    outsourced tasks are evolving .

* Other features:

  * Materials. You can manage the materials that planned tasks need to be
    carried out.

  * Complete users system with permissions, LDAP authentication, etc.


***

## Requirements

* JRE 8 - Java Runtime Environment

  Project depends on Java 8 JRE is needed in order to run it

* PostgreSQL - Object-relational SQL database

  A database server is needed. You could use *PostgreSQL* or *MySQL* as you
  prefer.

* Tomcat 8 - Servlet and JSP engine

  Server to deploy the application. You could use *Jetty* instead.

* JDBC Driver - Java database (JDBC) driver for PostgreSQL

  To connect application with PostgreSQL database in *Tomcat*

* CutyCapt - Utility to capture WebKit's rendering of a web page

  Required for printing

* Xvfb - Virtual Framebuffer 'fake' X server

  Used by CutyCapt for printing

See [this link](https://github.com/LibrePlan/libreplan/wiki/LibrePlan-installation) for installation instructions.

See [this link](https://github.com/LibrePlan/libreplan/wiki/Compilation-requirements) and [this link](https://github.com/LibrePlan/libreplan/wiki/LibrePlan-compilation)file for compilation requirements and instructions.


***

## Availability

Released versions are available at
http://sourceforge.net/projects/libreplan/files/

***

## Webpage

You can find more information about LibrePlan at
http://www.libreplan.org/home/

For information related with LibrePlan development you can visit the wiki at
http://wiki.libreplan.org/twiki/bin/view/LibrePlan


***

## Reporting bugs

Please use the bug tracker to report bugs at http://bugs.libreplan.org/


***

## License


LibrePlan is released under the terms of the GNU [Affero General Public License](http://www.gnu.org/licenses/agpl.html) version 3.

Please read the ``COPYING`` file for details.


Authors
-------

This project was initially sponsored by [Fundación para o Fomento da Calidade Industrial e o Desenvolvemento Tecnolóxico de Galicia](http://gain.xunta.gal/).

Please see [this section](https://github.com/LibrePlan/libreplan/wiki/Authors) for more information about the authors.
