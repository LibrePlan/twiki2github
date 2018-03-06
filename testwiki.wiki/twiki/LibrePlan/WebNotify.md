[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[WebNotify](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/WebNotify "Topic revision: 8 (15 May 2012 - 17:07:09)") (15 May 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/WebNotify?t=1520337987 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/WebNotify "Attach an image or document to this topic")
This is a subscription service to be automatically notified by e-mail when topics change in this **LibrePlan** web. This is a convenient service, so you do not have to come back and check all the time if something has changed. To subscribe, please add a bullet with your [WikiName](/twiki/TWiki/WikiName) in alphabetical order to this list:

-   [ManuelRego](/twiki/Main/ManuelRego): \*

###  Web Changes Notification Service

Each TWiki web has an automatic e-mail notification service that sends you an e-mail with links to all of the topics modified since the last alert.

Users subscribe to email notifications using their [WikiName](/twiki/TWiki/WikiName) or an alternative email address, and can specify the webs/topics they wish to track, WWhole groups of users can also be subscribed for notification.

The general format of a subscription is:

*three spaces* `*` *subscriber* \[ `:` *topics* \]

Where *subscriber* can be a [WikiName](/twiki/TWiki/WikiName), an E-mail address, or a group name. If *subscriber* contains any characters that are not legal in an email address, then it must be enclosed in 'single' or "double" quotes.

*topics* is an optional space-separated list of topics:

-   ... **without** a *Web.* prefix
-   ...that exist in this web.

Users may further customize the specific content they will receive using the following controls:

-   You can use `*` in a topic name, where it is treated as a [wildcard character](http://en.wikipedia.org/wiki/Wildcard_character). A `*` will match zero or more other characters - so, for example, `Fred*` will match all topic names starting with `Fred`, `*Fred` will match all topic names *ending* with `Fred`, and `*` will match *all* topic names.
-   Each topic may optionally be preceded by a '+' or '-' sign. The '+' sign means "subscribe to this topic". The '-' sign means "unsubscribe" or "don't send notifications regarding this particular topic". This allows users to elect to filter out certain topics. Topic filters ('-') take precedence over topic includes ('+') i.e. if you unsubscribe from a topic it will cancel out any subscriptions to that topic.
-   Each topic may optionally be followed by an integer in parentheses, indicating the depth of the tree of children below that topic. Changes in all these children will be detected and reported along with changes to the topic itself. *Note* This uses the TWiki "Topic parent" feature.
-   Each topic may optionally be immediately followed by an exclamation mark ! or a question mark ? with no intervening spaces, indicating that the topic (and children if there is a tree depth specifier as well) should be mailed out as **complete topics** instead of change summaries. ! causes the topic to be mailed every time *even if there have been no changes*, and ? will mail the topic only if there have been changes to it. This only makes sense for subscriptions, and is intended for mailshotting regular newletters.

For example: Subscribe Daisy to all changes to topics in this web.

       * daisy.cutter@flowers.com

Subscribe Daisy to all changes to topics that start with `Web`.

       * daisy.cutter@flowers.com : Web*

Subscribe Daisy to changes to topics starting with `Petal`, and their immediate children, WeedKillers and children to a depth of 3, and all topics that match start with `Pretty` and end with `Flowers` e.g. `PrettyPinkFlowers`

       * DaisyCutter: Petal* (1) WeedKillers (3) Pretty*Flowers

Subscribe StarTrekFan to changes to all topics that start with `Star` **except** those that end in `Wars`, `sInTheirEyes` or `shipTroopers`.

       * StarTrekFan: Star* - *Wars - *sInTheirEyes - *shipTroopers

Subscribe Daisy to the full content of NewsLetter whenever it has changed

       * daisy@flowers.com: NewsLetter?

Subscribe buttercup to NewsLetter and its immediate children, even if it hasn't changed.

       * buttercup@flowers.com: NewsLetter! (1)

Subscribe GardenGroup (which includes Petunia) to all changed topics under AllnewsLetters to a depth of 3. Then unsubscribe Petunia from the ManureNewsLetter, which she would normally get as a member of GardenGroup[?](/twiki/bin/edit/LibrePlan/GardenGroup?topicparent=LibrePlan.WebNotify "Create this topic") :

       * GardenGroup: AllNewsLetters? (3)
       * petunia@flowers.com: - ManureNewsLetter

Subscribe `IT:admins` (a non-TWiki group defined by an alternate user mapping) to all changes to Web\* topics.

       * 'IT:admins' : Web*

A user may be listed many times in the WebNotify topic. Where a user has several lines in WebNotify that all match the same topic, they will only be notified about *changes* that topic *once* (though they will still receive individual mails for news topics).

If a *group* is listed for notification, the group will be recursively expanded to the e-mail addresses of all members.

\_\_![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!") Warning: Because an email address is not linked to a user name, there is no way for TWiki to check access controls for email addresses. A user identified by an email address will only be sent change notifications if the topic they are asubscribed to is readable by guest users. You can limit what email addresses can be used in WebNotify, or even block use of emails altogther, using the `{MailerContrib}{EmailFilterIn} setting in =configure`.

***![TIP](/twiki/TWiki/TWikiDocGraphics/tip.gif "TIP") Tip:*** List names in alphabetical order to make it easier to find the names.

***Note for System Administrators:*** Notification is supported by an add-on to the TWiki kernel called the MailerContrib. See the [MailerContrib](/twiki/TWiki/MailerContrib) topic for details of how to set up this service.

***Note:*** If you prefer a news feed, point your reader to [WebRss](/twiki/LibrePlan/WebRss) (for RSS 1.0 feeds) or [WebAtom](/twiki/LibrePlan/WebAtom) (for ATOM 1.0 feeds). Learn more at [WebRssBase](/twiki/TWiki/WebRssBase) and [WebAtomBase](/twiki/TWiki/WebAtomBase), respectively.

***Related topics:*** [WebChangesAlert](/twiki/TWiki/WebChangesAlert), [TWikiRegistration](/twiki/TWiki/TWikiRegistration)
