[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Documentation](LibrePlan_Documentation)&gt;[I18nDocumentation](LibrePlan_I18nDocumentation "Topic revision: 27 (14 Mar 2015 - 14:46:14)") (14 Mar 2015, [JeroenBaten](Main_JeroenBaten))[Edit](LibrePlan_I18nDocumentation?t=1520343627 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/I18nDocumentation "Attach an image or document to this topic")  

 I18n Documentation
===================

-   [Introduction](LibrePlan_I18nDocumentation#Introduction)
-   [Current languages](LibrePlan_I18nDocumentation#Current_languages)
-   [FAQ](LibrePlan_I18nDocumentation#FAQ)
-   [HOWTOs](LibrePlan_I18nDocumentation#HOWTOs)
    -   [For translators](LibrePlan_I18nDocumentation#For_translators)
        -   [How to update a translation](LibrePlan_I18nDocumentation#How_to_update_a_translation)
        -   [How to add a new language](LibrePlan_I18nDocumentation#How_to_add_a_new_language)
    -   [For maintainers](LibrePlan_I18nDocumentation#For_maintainers)
        -   [How to update keys.pot file](LibrePlan_I18nDocumentation#How_to_update_keys_pot_file)
    -   [For developers](LibrePlan_I18nDocumentation#For_developers)
        -   [How to i18n .java files](LibrePlan_I18nDocumentation#How_to_i18n_java_files)
        -   [How to i18n .zul files](LibrePlan_I18nDocumentation#How_to_i18n_zul_files)
            -   [Webapp package](LibrePlan_I18nDocumentation#Webapp_package)
            -   [Ganttzk package](LibrePlan_I18nDocumentation#Ganttzk_package)
        -   [How to i18n .jrxml files (Reports)](LibrePlan_I18nDocumentation#How_to_i18n_jrxml_files_Reports)
        -   [How to translate Enums](LibrePlan_I18nDocumentation#How_to_translate_Enums)

 Introduction
-------------

**LibrePlan localization files are uploaded to [Transifex](http://www.transifex.net/projects/p/libreplan/)**, you can directly translate there the different files.

LibrePlan uses [GNU gettext](http://www.gnu.org/software/gettext/) tools to support internationalization, which means that translators will just need to take care of `.po` files.

There are 2 `keys.pot` files in LibrePlan:

-   `ganttzk/src/main/resources/i18n/keys.pot`
-   `libreplan-webapp/src/main/resources/i18n/keys.pot`

 Current languages
------------------

[Language](LibrePlan_I18nDocumentation?sortcol=0;table=1;up=0#sorted_table "Sort by this column")

[Code](LibrePlan_I18nDocumentation?sortcol=1;table=1;up=0#sorted_table "Sort by this column")

[Translator](LibrePlan_I18nDocumentation?sortcol=2;table=1;up=0#sorted_table "Sort by this column")

[Comments](LibrePlan_I18nDocumentation?sortcol=3;table=1;up=0#sorted_table "Sort by this column")

English

`en`

 

*Default language*

Czech

`cs`

Zbyněk Schwarz

 

Spanish

`es`

Jacobo Aragunde Pérez, Manuel Rego Casasnovas, Diego Pino García

 

French

`fr`

Stephane Ayache, Guillaume Postaire, Philippe Poumaroux

 

Galician

`gl`

Jacobo Aragunde Pérez, Manuel Rego Casasnovas, Diego Pino García

 

Italian

`it`

Giuseppe Zizza

 

Dutch

`nl`

Jeroen Baten

 

Polish

`pl`

Krzysztof Kamecki

 

Portuguese

`pt`

Lena Grosso, Joaquim Rocha

 

Russian

`ru`

Pavel Rudensky

 

 [FAQ](LibrePlan_FAQ)
---------------------

[String](LibrePlan_I18nDocumentation?sortcol=0;table=2;up=0#sorted_table "Sort by this column")

[Explanation](LibrePlan_I18nDocumentation?sortcol=1;table=2;up=0#sorted_table "Sort by this column")

`h`

Stands for *hour*

`unl`

Stands for *unlimited*

`en`

Stands for *English*, which needs to be translated into destination code (see table above) for generating help links

`userDn`

Stands for *User domain name* on LDAP preferences

`Inh`

Stands for *Inherited*

`Op`

Stands for *operations* which is usually displayed as the last column in the grid with edit, delete, etc. buttons

Planning points

`F`

Stands for *Fully scheduled*

`P`

Stands for *Partially scheduled*

`U`

Stands for *Unscheduled*

Earned Value Chart

`BCWS`

Budgeted Cost Work Scheduled

`ACWP`

Actual Cost Work Performed

`BCWP`

Budgeted Cost Work Performed

`CV`

Cost Variance

`SV`

Schedule Variance

`BAC`

Budget At Completion

`EAC`

Estimate At Completion

`VAC`

Variance At Completion

`ETC`

Estimate To Complete

`CPI`

Cost Performance Index

`SPI`

Schedule Performance Index

 HOWTOs
-------

###  For translators

####  How to update a translation

1.  Get LibrePlan code from Git repository.

        $ git clone git://github.com/Igalia/libreplan.git
        $ cd libreplan/

2.  Go to folder `ganttzk/src/main/resources/i18n/`.

        $ cd ganttzk/src/main/resources/i18n/

3.  Update `.po` file. For example:

        $ msgmerge -U es.po keys.pot

4.  Review `.po` file translation using a text editor or a specific translation tool like [Gtranslator](http://live.gnome.org/gtranslator/) or [Lokalize](http://userbase.kde.org/Lokalize).

        $ gtranslator es.po

5.  Do the same for folder `libreplan-webapp/src/main/resources/i18n/`.

        $ cd ../../../../../libreplan-webapp/src/main/resources/i18n/
        $ msgmerge -U es.po keys.pot
        $ gtranslator es.po

6.  In order to update LibrePlan reports translations go to `libreplan-webapp/src/main/jasper/` folder.

        $ cd ../../../../../libreplan-webapp/src/main/jasper/

7.  Review folders with `_Bundle` suffix and update `.properties` files for your language.
8.  Send the new files or a patch to [us](https://sourceforge.net/mail/?group_id=302765).

####  How to add a new language

1.  Get LibrePlan code from Git repository.

        $ git clone git://github.com/Igalia/libreplan.git
        $ cd libreplan/

2.  Go to folder `ganttzk/src/main/resources/i18n/`.

        $ cd ganttzk/src/main/resources/i18n/

3.  Generate new `.po` file. For example:

        $ msginit -i keys.pot -o fr.po

4.  Translate new `.po` file using a text editor or a specific translation tool like [Gtranslator](http://live.gnome.org/gtranslator/).

        $ gtranslator fr.po

5.  Do the same for folder `libreplan-webapp/src/main/resources/i18n/`.

        $ cd ../../../../../libreplan-webapp/src/main/resources/i18n/
        $ msginit -i keys.pot -o fr.po
        $ gtranslator fr.po

6.  In order to translate LibrePlan reports go to `libreplan-webapp/src/main/jasper/` folder.

        $ cd ../../../../../libreplan-webapp/src/main/jasper/

7.  Review folders with `_Bundle` suffix and create new `.properties` files for your language.
8.  Send the new files or a patch to [us](https://sourceforge.net/mail/?group_id=302765).

###  For maintainers

####  How to update `keys.pot` file

1.  Go to scripts folder `scripts/`.

        $ cd scripts/

2.  Execute `libreplan-all-keys-generator.sh` script:

        $ ./libreplan-all-keys-generator.sh

3.  Review changes done in `keys.pot` files to check that everything is right:
    -   Avoid addition of empty strings.

            msgid ""
            msgstr ""

    -   Keep header and copyright information right.

4.  Push changes.

###  For developers

####  How to i18n `.java` files

1.  Import `I18nHelper` class depending on module:

        import static org.libreplan.web.I18nHelper._;

    or

        import static org.libreplan.business.i18n.I18nHelper._;

    or

        import static org.zkoss.ganttz.i18n.I18nHelper._;

2.  Call `_(String str)` method:

        _("my string");

    or with parameters

        _("Project {0} saved", projectName);

####  How to i18n `.zul` files

#####  Webapp package

1.  Add *taglib* (optional):

        <?taglib uri="/WEB-INF/tld/i18n.tld" prefix="i18n" ?>

    This *tablib* is already added in file `template.zul` which is usually used in most of `.zul` pages, so this step is not always needed.

2.  Call `i18n:_(String str)` method:

        <button label="${i18n:_('Add')}" />

    or with parameters

        <i18n value="Confirm deleting {0} ?" arg0="@{controller.worker.name}">

    or

        <window title="${i18n:__('Error: {0}', requestScope['javax.servlet.error.status_code'])}">

#####  Ganttzk package

1.  Import GanttZK.I18nHelper and set prefix as `ganttzk_i18n`:

        <?xel-method prefix="ganttzk_i18n" name="_" class="org.zkoss.ganttz.i18n.I18nHelper" signature="java.lang.String _(java.lang.String name)" ?>

2.  Call `ganttzk_i18n:_(String str)` method:

        <button label="${ganttzk_i18n:_('Add')}" />

**NOTE:** Currently localization of strings with parameters is not supported in ganttzk.

####  How to i18n `.jrxml` files (Reports)

Reports are localized in the same fashion Jasper Reports are localized. Briefing, there's a `XXX.properties` file for each localized language.

1.  Create a new report or edit an existing one with *iReport*. Once opened, click on it to see its properties. In the property *Resource Bundle* set the name of the folder which will contain your `XXX.properties` files.
2.  Create a new folder for storing the `XXX.properties` files. The folder must end with suffix `_Bundle`.
3.  Create your `XXX.properties` file, one for each language you would like to support. The format of each file should be: `XXX_lang_country`. For instance: `hoursWorkedPerWorker_en_US.properties` (lang: en; country: US). In general, it's a good idea to also have a plain `XXX.properties` (without *lang* and *country*), for being used as default.

In case of doubt, check folder `libreplan-webapp/src/main/jasper/` for examples.

####  How to translate Enums

If your Enum is in the **webapp layer**, mark the literals you would like to translate with \_(). Example:

    public enum ProgressType {

        SPREAD_PROGRESS(_("Progress with all task tasks by hours")),
        CRITICAL_PATH_DURATION(_("Progress with critical path tasks by hours")),
        CRITICAL_PATH_NUMHOURS(_("Progress with critical path tasks by duration"));

        private String value;

    }

It's a good idea to implement `toString()` and return `value`.

    public String toString() {
       return value;
    }

If your Enum is in the **business layer**, do the same as in the previous case, however this is not enough.

The \_() from the business layer is a fake function, it does nothing. It's only used to mark the texts you would like to translate, but the function that really does the translation is the \_() function from the webapp layer. That means that apart from marking the texts in the business layer you also need to filter those values through a \_() function in the webapp layer.

A common source of error is marking the literal in the business layer but retrieving those values in the webapp directly, using a zul component and a model attribute for instance.

    <listbox id="lbTypeProgress"
       model="@{configurationController.progressTypes}"
       selectedItem="@{configurationController.selectedProgressType}"
       mold="select" />

In cases like this you'd need to implement a controller that explicitly filters the literal you need to translate.

    public ProgressTypeRenderer getProgressTypeRenderer() {
       return progressTypeRenderer;
    }

    private class ProgressTypeRenderer implements ListitemRenderer {

       @Override
       public void render(Listitem item, Object data) throws Exception {
          ProgressType progressType = (ProgressType) data;
          item.setLabel(_(progressType.getValue()));
       }

    }

And now use the renderer in your component

    itemRenderer="@{configurationController.progressTypeRenderer}"                   
