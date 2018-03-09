# Converting code for LibrePlan Twiki to GitHub Wiki+markdown

Using Python to extract all current pages from Twiki.
The program itself contains lots of trial and error code.
Basically it's crap, but it did get the job done (sort of).

Basic program flow:

1. Call WebTopicList
1. Loop for every page found
1. Change the text
1. Convert from Twiki to Markdown
1. Add to local wiki git repo

## Sources of inspiration
- Getting list of all Twiki pages: https://wiki.libreplan.org/bin/view/LibrePlan/WebTopicList

# Change page width:

The current github page styling is sub-optimal to say the least. There are options, but we chose not to use them.

https://userstyles.org/styles/108591/github-wide


