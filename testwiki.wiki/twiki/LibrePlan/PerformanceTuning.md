[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[Documentation](/twiki/LibrePlan/Documentation)&gt;[PerformanceTuning](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/PerformanceTuning "Topic revision: 2 (20 Aug 2012 - 09:52:59)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/PerformanceTuning?t=1520337963 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/PerformanceTuning "Attach an image or document to this topic")

 Performance Tuning
==============================================================================================

-   [Installation and usage of Eclipse Test & Performance Tools Platform (TPTP) with LibrePlan](#Installation_and_usage_of_Eclips)
    -   [Dependencies](#Dependencies)
    -   [Install TPTP](#Install_TPTP)
    -   [Unit test profiling](#Unit_test_profiling)
    -   [Web application profiling](#Web_application_profiling)
        -   [Install TPTP Agent Controller](#Install_TPTP_Agent_Controller)
    -   [Related links](#Related_links)
-   [Installation and usage of Java Application Monitor (JAMon) with LibrePlan](#Installation_and_usage_of_Java_A)
    -   [Installation](#Installation)
    -   [Usage](#Usage)
-   [Installation and usage of Java Simple Monitoring API (javasimon) with LibrePlan](#Installation_and_usage_of_Java_S)
    -   [Installation](#Installation)
    -   [Usage](#Usage)

 Installation and usage of Eclipse Test & Performance Tools Platform (TPTP) with LibrePlan
---------------------------------------------------------------------------------------------------------------------------------------------

###  Dependencies

First of all, it's needed to install library called `libstdc++5`:

    # apt-get install libstdc++5

**NOTE:** libstdc++5 is not present in Hardy or Lucid. In order to install it in those systems it's needed to follow this post: <http://hsmak.wordpress.com/2009/12/01/how-to-fix-libstdc5-dependency-problem-in-ubuntu-9-10/>

It's also needed to install the following software inside Eclispe: Eclipse Modeling Framework (EMF) and XML Schema Definition SDK (XSD). In order to do that, go to menu *Help -&gt; Install New Software*, and select main Eclipse repository:

-   *Galileo*. URL: <http://download.eclipse.org/releases/galileo>
-   *Helios*. URL: <http://download.eclipse.org/releases/helios>

In the combobox *Work with*, in top part (if it doesn't exist add it clicking *Add*). We will use filter to search EMF and XSD. In order to install them it's only needed to check them and click *Next -&gt; Finish*.

###  Install TPTP

The easiest way is from Eclipse, also in menu *Help -&gt; Install New Software*. Select again main Eclipse repository (*Galileo* or *Helios*) and check the whole section *Test and Performance*.

**NOTE:** If we install TPTP using the main Eclipse repository, in Helios it downloads version 4.5.0 which is not the last available version. We could add TPTP repository in order to download last version. Click in *Add new* and add *TPTP* repository:

-   Name: TPTP
-   URL: <http://download.eclipse.org/tptp/updates/>

There're some problems with 4.5.0 in Lucid (profiling get frozen some times, and results don't appear doing double-click in *Open with* option of contextual menu). Solution is to install version 4.7.0. It's always recommended that *Agent controller* version matches with TPTP plugins version.

After install and reboot Eclipse, we should have a new button *Profile* in the toolbar, between *Run* and *Debug*. There're also a set of new sections inside *Run* menu. With current configuration, we could make profiling for desktop (not web) Java applications and unit tests.

There's an alternative installation method [in this url](http://www.eclipse.org/tptp/home/downloads/installguide/InstallGuide44.html), downloading software [here](http://www.eclipse.org/tptp/home/downloads/?ver=4.6.2).

###  Unit test profiling

Browsing till a unit test from *Project Explorer*, we will find new options in right button menu. Select *Profile As -&gt; JUnit Test*.

Configuration window will appear in order to execute this test. In *Monitor* tab we could mark which measurements we want to take. The basic ones are inside *Java profiling* (memory, execution time, etc.). In this window is also important visit *Java Profiling* options, clicking in *Edit Options* when it's selected ou double-clicking on it. Here we will define which classes are going to be filtered in order to take measurements. The best idea in or situation is disable *Automatically determine filtering criteria*, create a new set of filters (top *Add* button), use `LibrePlan Filter Set` as name, and select it. Then create a new rule (bottom *Add* button) for classes `org.navalplanner.*`, leave `*` in *Method Name* and *INCLUDE* in *Rule*. If we want to ignore the rest of classes, we could simple delete rules that already existed and add a new rule *EXCLUDE* for `*` classes. The include rule has priority by default, priorities could be modified with *Up* and *Down* buttons.

Click *Apply* and then *Profile* in the bottom part and profiling session will start. Once we already saved all this configuration we don't need to repeat it for this test; if we want to change anything later, we need to go to *Run -&gt; Profile configurations* menu. In order to see profiling results, we should change to perspective *Profiling and logging* (it it isn't automatic, go to *Window -&gt; Open Perspective -&gt; Other -&gt; Profiling and Logging*).

###  Web application profiling

Explained in previous point is valid to do profiling for a unit test, but not for a web application.

TPTP could be configured by default for web applications installed in Tomcat, but this is not valid for our development environment based on Maven that uses Jetty web server. The way to do it is using an external "Agent Controller", an application that stores application traces and send them through network in order to read and analyze them with an Eclipse client.

####  Install TPTP Agent Controller

The following instructions are a summary from [this webpage](http://www.jroller.com/RickHigh/entry/profiling_with_eclipse_and_remote).

-   Download Agent Controller Runtime. It's recommended that Agent controller version matches with TPTP plugins. \[\[http://www.eclipse.org/tptp/home/downloads/?ver=4.7.0\#agentController\] \[Download Agent controller 4.7.0\]\]. Select proper architecture and platform (Linux EM64T[?](/twiki/bin/edit/LibrePlan/EM64T?topicparent=LibrePlan.PerformanceTuning "Create this topic") , in 64 bits).

-   Uncompress for example in `~/tptp-agent`.

-   Add following lines to `.bashrc` (added to some of them that already exit for Maven):

        # TPTP Agent
        export TPTP_AC_HOME=~/tptp-agent
        export LD_LIBRARY_PATH=$TPTP_AC_HOME/lib:$LD_LIBRARY_PATH
        export LD_LIBRARY_PATH=$TPTP_AC_HOME/bin:$LD_LIBRARY_PATH
        export JAVA_PROFILER_HOME=$TPTP_AC_HOME/plugins/org.eclipse.tptp.javaprofiler
        export LD_LIBRARY_PATH=$JAVA_PROFILER_HOME:$LD_LIBRARY_PATH
        export MAVEN_OPTS="-Xms512m -Xmx1024m -XX:PermSize=256m -XX:MaxPermSize=512m -agentlib:JPIBootLoader=JPIAgent:server=enabled;CGProf:execdetails=true"

-   Start agent using command `~/tptp-agent/bin/ACStart.sh`. In the same folder there's also a command `ACStop.sh` to stop it. This step is optional, because of with previous MAVEN\_OPTS, agent should be automatically launched together with Jetty.

-   Now start LibrePlan compiling it, and running web server, from command line using Maven (remember to restart the terminal in order to load new `.bashrc` values):

        cd navalplan; mvn install; cd navalplanner-webapp; mvn jetty:run

-   With server running, start Eclipse and configure connection with external Agent Controller externo, going to *Run -&gt; Profile configuration*, double-click in *Attach to Agent*. We will set a name in the top part, for example "LibrePlan external agent". Go to *Agents* tab, where if everything is right will appear an element in *Available agents* list. We mark it and go to *Edit Options*, like in previous case of unit tests, in order to customize filtering, because of by default `org*` classes are not shown. It's needed to add an *INCLUDE* filter for `org.navalplanner.*` classes.

-   Once it's configured, start the new profiling clicking *Apply* and *Profile*. Now that we already saved a configuration with name "LibrePlan external agent", it should appear in *Profile* button and in *Run -&gt; Profile History* menu. Every time we open it, it will aks us to chose an agent in *Available agents* list.

###  Related links

<http://www.jroller.com/RickHigh/entry/profiling_with_eclipse_and_remote>

<http://dev.eclipse.org/viewcvs/index.cgi/platform/org.eclipse.tptp.platform.agentcontroller/src-native-new/packaging_md/linux/getting_started.html?root=TPTP_Project&view=co>

<http://locsoh.blogspot.com/2009/08/how-to-install-tptp-46-for-eclipse-35.html>

<http://www.eclipse.org/tptp/home/downloads/installguide/InstallGuide44.html>

<http://www.eclipse.org/tptp/home/downloads/?ver=4.6.2>

<http://wiki.eclipse.org/Install_TPTP_with_Update_Manager>

 Installation and usage of Java Application Monitor (JAMon) with LibrePlan
-----------------------------------------------------------------------------------------------------------------------------

###  Installation

Download `jamonall_27.zip` file from <http://sourceforge.net/projects/jamonapi/files/>, and extract it, for example, in folder `~/jamonapi`.

In order to install the library under Maven, use this command:

    mvn install:install-file -Dfile=~/jamonapi/jamon-2.7.jar -Dpackaging=jar -DgroupId=monitoring -DartifactId=jamon -Dversion=2.7 -DgeneratePom=true

Finally, in order to use it inside our project, we need to add it as dependency. Add following lines in file `navalplanner-webapp/pom.xml`, inside `dependencies` tag:

            <!-- JAMon - Java Monitoring -->
            <dependency>
                <groupId>monitoring</groupId>
                <artifactId>jamon</artifactId>
                <version>2.7</version>
            </dependency>

###  Usage

A simple use case is to measure the spent in the execution of a source code block. We will need to add the following lines to code:

            import com.jamonapi.*;

            Monitor monitor = MonitorFactory.start("myFirstMonitor");
            /* Code that you want to measure ... */
            monitor.stop();
            System.out.println(monitor);

If block is executed several times class `Monitor` is gathering all measurements, and when it's printed we will get additional data like number of calls and average execution time.

More documentation and examples at project webpage: <http://jamonapi.sourceforge.net/>

 Installation and usage of Java Simple Monitoring API (javasimon) with LibrePlan
-----------------------------------------------------------------------------------------------------------------------------------

###  Installation

Library is already supported in Maven. In order to integrate it we need to add following lines in root `pom.xml` file, and Maven will be in charge to download, install and update it if needed:

        <properties>
            ...
            <javasimon.version>2.2.0</javasimon.version>
        </properties>
        ...
        <repositories>
            ...
            <repository>
                <id>maven2-repository.dev.java.net</id>
                <name>Java.net Repository for Maven</name>
                <url>http://download.java.net/maven/2/</url>
            </repository>
        </repositories>
        ...
        <dependencies>
            ...
            <dependency>
                <groupId>org.javasimon</groupId>
                <artifactId>javasimon-core</artifactId>
                <version>${javasimon.version}</version>
            </dependency>
        </dependencies>

And the following lines in `dependencies` section at file `navalplanner-webapp/pom.xml` in order to use it (the same lines are needed for `navalplanner-business/pom.xml` if we want to use it in that module):

            <dependency>
                <groupId>org.javasimon</groupId>
                <artifactId>javasimon-core</artifactId>
            </dependency>

There're more javasimon modules that can be enabled adding them to dependencies list. More information in [this link](http://code.google.com/p/javasimon/wiki/MavenSupport).

###  Usage

Again, we're going to measure spent time in the execution of a source code block. In order to do that we will add the following lines to code:

            import org.javasimon.*;

            Stopwatch stopwatch = SimonManager.getStopwatch("stopwatch");
            Split split = SimonManager.getStopwatch("stopwatch").start();
            /* Código que quero medir... */
            split.stop();
            System.out.println(stopwatch);
            System.out.println(stopwatch.sample()); // Proporciona estatísticas adicionais

It also works in an accumulative way, like JAMon.

More documentation and examples in project website: <http://code.google.com/p/javasimon/>
