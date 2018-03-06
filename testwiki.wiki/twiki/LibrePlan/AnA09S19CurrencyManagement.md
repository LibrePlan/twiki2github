[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[AnA09S19CurrencyManagement](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement "Topic revision: 1 (26 Apr 2012 - 13:35:32)") (26 Apr 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/AnA09S19CurrencyManagement?t=1520337850 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA09S19CurrencyManagement "Attach an image or document to this topic")

 [AnA09S19CurrencyManagement](/twiki/LibrePlan/AnA09S19CurrencyManagement)
================================================================================================================================



|                        |                                                                                    |
|------------------------|------------------------------------------------------------------------------------|
| Story summary          | Currency Managment                                                                 |
| Iteration              | [AnA08Usability](/twiki/LibrePlan/AnA08Usability)                         |
| FEA                    | [AnA09S19CurrencyManagement](/twiki/LibrePlan/AnA09S19CurrencyManagement) |
| Story Lead             |                                                                                    |
| Next Story             |                                                                                    |
| Passed acceptance test | No                                                                                 |

###  Tasks



####  Add option to choose LibrePlan currency in configuration window

1) Modify entity **Configuration** to add 2 new fields:

-   `currencyCode`: String (default value `EUR`). This will store the code of the configured [Currency](http://docs.oracle.com/javase/1.5.0/docs/api/java/util/Currency.html). For example: `EUR`, `USD`, ...
-   `currencySymbol`: String (default value ``). The symbol for the configured currency. For example: ``, `$`, ...

2) Add a new combo after *Company logo URL* entry with the following information:

-   Label: **Currency**
-   Data (alphabetically sorted):

        EUR - 
        USD - $
        ...

This combo will show as selected the currency matching with the new field `currencyCode`. Once, the combo is modified and the configuration saved **both fields** `currencyCode` and `currencySymbol` will be updated.

In order to extract the **list of currencies** we should use the following code:

        public static Map<String, String> getAllCurrencies() {
            Map<String, String> currencies = new HashMap<String, String>();
            for (Locale locale : Locale.getAvailableLocales()) {
                if (StringUtils.isNotBlank(locale.getCountry())) {
                    Currency currency = Currency.getInstance(locale);
                    currencies.put(currency.getCurrencyCode(),
                            currency.getSymbol(locale));
                }
            }

            return currencies;
        }



####  Replace use of euro for the configured currency

Review all the places (reports included) where **€ or EUR or euro/s** is used and replace it for the `currencySymbol` from configuration.

###  User stories

-   [ItEr76S25CurrencyManagement](/twiki/LibrePlan/ItEr76S25CurrencyManagement)

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/AnA09S19CurrencyManagement?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                        | 2                                                                                                                                                         | 2                                                                                                                                                           | 0                                                                                                                                                           | Low                                                                                                                                                        | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                   | [Add option to choose LibrePlan currency in configuration window](/twiki/LibrePlan/AnA09S19CurrencyManagement#TasK1)                                   |                                                                                                                                                                  |                                                                                                                                                                    |                                                                                                                                                                 |
| Task                                                                                                                                                        | 3                                                                                                                                                         | 3                                                                                                                                                           | 0                                                                                                                                                           | Low                                                                                                                                                        | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                  | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                   | [Replace use of euro for the configured currency](/twiki/LibrePlan/AnA09S19CurrencyManagement#TasK2)                                                   |                                                                                                                                                                  |                                                                                                                                                                    |                                                                                                                                                                 |


