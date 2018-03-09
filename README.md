# Converting code for LibrePlan Twiki to GitHub Wiki+markdown

Using Python to extract all current pages from Twiki

1. Call WebTopicList
1. Loop for every page
1. (optionally) loop for every history
1. convert from Twiki to Markdown
1. Add to local wiki git repo

## Sources of inspiration
- Getting list of all Twiki pages: https://wiki.libreplan.org/bin/view/LibrePlan/WebTopicList

# Change page width:

https://userstyles.org/styles/97661/wide-my-github

@namespace url(http://www.w3.org/1999/xhtml);

@-moz-document domain("github.com")
{
  .container
  {
    width: 97% !important;
  }

  .pagehead
  {
    margin-left: 40px !important;
  }

  .gh-header-back
  {
    margin-left: 0px !important;
  }

  .container > .repository-content,
  .container > .repo-container > .repository-content
  {
    width: 96% !important;
  }

  .container > .with-full-navigation > .repository-content,
  .pull-request-composer .discussion-topic
  {
    width: 88% !important;
  }

  .column-main,
  .repo-settings-content,
  .settings-content,
  .js-new-issue-form > .discussion-timeline-cols > .main
  {
    width: 84% !important;
  }

  .new-discussion-timeline .discussion-timeline,
  .timeline-new-comment
  {
    width: 90% !important;
    max-width: 100% !important;
  }

  .news
  {
    width: 78% !important;
  }

  .list-group-item-meta .branch-name .css-truncate-target
  {
    max-width: 100% !important;
  }

  #comments,
  .comment-holder
  {
    max-width: 1100px !important;
  }
}

@-moz-document domain("gist.github.com")
{
  .column
  {
    width: 91% !important;
  }

  .file-contents
  {
    width: 98% !important;
  }

  .gist-content
  {
    width: 88% !important;
  }
}


