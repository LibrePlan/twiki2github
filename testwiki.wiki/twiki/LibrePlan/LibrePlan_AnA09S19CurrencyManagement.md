[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[AnA09S19CurrencyManagement](LibrePlan_AnA09S19CurrencyManagement "Topic revision: 1 (26 Apr 2012 - 13:35:32)") (26 Apr 2012, [ManuelRego](Main_ManuelRego))[Edit](LibrePlan_AnA09S19CurrencyManagement?t=1520344054 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/AnA09S19CurrencyManagement "Attach an image or document to this topic")  

 [AnA09S19CurrencyManagement](LibrePlan_AnA09S19CurrencyManagement)
===================================================================

|                        |                                                                    |
|------------------------|--------------------------------------------------------------------|
| Story summary          | Currency Managment                                                 |
| Iteration              | [AnA08Usability](LibrePlan_AnA08Usability)                         |
| FEA                    | [AnA09S19CurrencyManagement](LibrePlan_AnA09S19CurrencyManagement) |
| Story Lead             |                                                                    |
| Next Story             |                                                                    |
| Passed acceptance test | No                                                                 |

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

-   [ItEr76S25CurrencyManagement](LibrePlan_ItEr76S25CurrencyManagement)

###  Tasks in this story

| [Tasks](LibrePlan_AnA09S19CurrencyManagement?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](LibrePlan_AnA09S19CurrencyManagement?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](LibrePlan_AnA09S19CurrencyManagement?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](LibrePlan_AnA09S19CurrencyManagement?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](LibrePlan_AnA09S19CurrencyManagement?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](LibrePlan_AnA09S19CurrencyManagement?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](LibrePlan_AnA09S19CurrencyManagement?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](LibrePlan_AnA09S19CurrencyManagement?sortcol=7;table=2;up=0#sorted_table "Sort by this column")   | [Start Date](LibrePlan_AnA09S19CurrencyManagement?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](LibrePlan_AnA09S19CurrencyManagement?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](LibrePlan_AnA09S19CurrencyManagement?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Task                                                                                                    | 2                                                                                                     | 2                                                                                                       | 0                                                                                                       | Low                                                                                                    | [ManuelRego](Main_ManuelRego)                                                                              | [ManuelRego](Main_ManuelRego)                                                                               | [Add option to choose LibrePlan currency in configuration window](LibrePlan_AnA09S19CurrencyManagement#TasK1) |                                                                                                              |                                                                                                                |                                                                                                             |
| Task                                                                                                    | 3                                                                                                     | 3                                                                                                       | 0                                                                                                       | Low                                                                                                    | [ManuelRego](Main_ManuelRego)                                                                              | [ManuelRego](Main_ManuelRego)                                                                               | [Replace use of euro for the configured currency](LibrePlan_AnA09S19CurrencyManagement#TasK2)                 |                                                                                                              |                                                                                                                |                                                                                                             |
