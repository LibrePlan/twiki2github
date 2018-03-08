[TWiki](Main_WebHome)&gt;![](/twiki/pub/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](LibrePlan_WebHome)&gt;[Documentation](LibrePlan_Documentation)&gt;[LibrePlanGit](LibrePlan_LibrePlanGit "Topic revision: 10 (01 Feb 2013 - 12:23:22)") (01 Feb 2013, [LorenzoTilve](Main_LorenzoTilve))[Edit](LibrePlan_LibrePlanGit?t=1520343710 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/LibrePlanGit "Attach an image or document to this topic")  

 How to use Git in LibrePlan
============================

-   [Requirements](LibrePlan_LibrePlanGit#Requirements)
    -   [Installation](LibrePlan_LibrePlanGit#Installation)
    -   [Configuration .gitconfig](LibrePlan_LibrePlanGit#Configuration_gitconfig)
-   [Developer profile](LibrePlan_LibrePlanGit#Developer_profile)
    -   [Clone repository](LibrePlan_LibrePlanGit#Clone_repository)
    -   [Create new branch](LibrePlan_LibrePlanGit#Create_new_branch)
    -   [Commit changes](LibrePlan_LibrePlanGit#Commit_changes)
    -   [Rebase](LibrePlan_LibrePlanGit#Rebase)
    -   [Send patch or patches](LibrePlan_LibrePlanGit#Send_patch_or_patches)
    -   [Working with remote branches](LibrePlan_LibrePlanGit#Working_with_remote_branches)
-   [Reviewer profile](LibrePlan_LibrePlanGit#Reviewer_profile)
    -   [Clone repository with write permissions](LibrePlan_LibrePlanGit#Clone_repository_with_write_perm)
    -   [Apply patch or patches](LibrePlan_LibrePlanGit#Apply_patch_or_patches)
    -   [Push changes](LibrePlan_LibrePlanGit#Push_changes)
    -   [Remote branches](LibrePlan_LibrePlanGit#Remote_branches)
        -   [Create a remote branch](LibrePlan_LibrePlanGit#Create_a_remote_branch)
        -   [Push changes in the remote branch](LibrePlan_LibrePlanGit#Push_changes_in_the_remote_branc)
        -   [Update remote branch with the last changes in master](LibrePlan_LibrePlanGit#Update_remote_branch_with_the_la)
        -   [Merge remote branch into master](LibrePlan_LibrePlanGit#Merge_remote_branch_into_master)
        -   [Deleting a remote branch](LibrePlan_LibrePlanGit#Deleting_a_remote_branch)
-   [Git tips and tricks](LibrePlan_LibrePlanGit#Git_tips_and_tricks)
    -   [Show branch name in prompt](LibrePlan_LibrePlanGit#Show_branch_name_in_prompt)
    -   [Avoid trailing whitespaces and tabs mixed with spaces](LibrePlan_LibrePlanGit#Avoid_trailing_whitespaces_and_t)
    -   [Iterative rebase](LibrePlan_LibrePlanGit#Iterative_rebase)

This guide explain how to use Git from a developer point of view in order to send patches to the project and the common way to work with it. It's also explained how is the reviewers work in order to integrate patches sent by other developers and push them to the central repository.

 Requirements
-------------

###  Installation

It's needed to install the following packages to use Git in your system:

-   Debian/Ubuntu:

        # apt-get install git-core git-email giggle

-   openSUSE:

        # zypper install git-core git-email giggle

-   Fedora:

        # yum install git git-email giggle

###  Configuration `.gitconfig`

Then any contributor should properly configure `.gitconfig` file in his home folder, with a content similar to:

    [user]
       name = Jonh Doe
       email = jdoe@domain.com
    [color]
       ui = auto
    [alias]
       br = branch
       ci = commit
       co = checkout
       st = status
    [sendemail]
       to = libreplan-devel@lists.sourceforge.net

This data is going to be used by Git in order to fill author information for each commit. Moreover, in this file each developer can define his own alias for the different Git commands.

 Developer profile
------------------

Developers will work in a local Git repository and don't have write permissions over central git project repository. Only project reviewers are going to apply patches on central repository.

Once a developer has implemented a software functionality he should create a patch or a list of patches and sent it to project development list ([libreplan-devel@lists.sourceforge.net](https://lists.sourceforge.net/lists/listinfo/libreplan-devel)). In order that patches are reviewed and pushed to central repository.

###  Clone repository

In order to start to work in the project, first of all the developer have to **clone Git repository** which is available anonymously via HTTP with the following command:

    $ git clone git://github.com/Igalia/libreplan.git

This will create a local copy of repository, in order to start to work it's recommended to create a new local branch for each functionality, use case, bug, ... using as branch name something related with functionality, use case to implement or bug to fix.

###  Create new branch

With following commands you will be **creating a new branch** `my-branch-name` and you will move to this branch with `checkout`:

    $ git branch my-branch-name
    $ git checkout my-branch-name

There is an alternative to do this in just one step:

    $ git checkout -b my-branch-name

You can check that you're in the new branch with the following command ([more info](LibrePlan_LibrePlanGit#Show_branch_name_in_prompt)):

    $ git branch
      master
    * my-new-branch

###  Commit changes

Once you're in the new branch and while you're developing you will do commit for changes done. You can do as many commits you think are needed to implement a functionality or fix a bug, it's better to divide your work in small chunks in order to make easier reviewers life and isolate errors.

Use the following commands to do a **commit**:

    $ git add <modified and new files separated by space or in different git add comands>
    $ git commit

It's important to write good quality **commit messages** in order to make easier the rest of contributors understand what patch does. As general rule commit messages start with a short line which describes the change in a concise way, followed by a blank line and a detailed explanation of the change. It's recommended to use present tense to write messages. Review [commit message format conventions in documentation section](LibrePlan_Documentation#Commit_Messages_Format).

First commit line will be used as commit short description and will be the name of patch file.

###  Rebase

Before sending the patch to mailing list you should check that it works against last upstream version. For that you need to **update you're local repository** with the following command:

    $ git checkout master
    $ git pull

In this moment you will have last version downloaded and you should again to your branch and **rebase** it:

    $ git checkout my-branch-name
    $ git rebase master

In that point you could have conflicts that have to be fixed before sending the patch.

To **fix conflicts** you need to review conflict files, fix the issue and use `add` when conflicts are fixed in a file. After that you should continue the rebase with `git rebase --continue`, if you prefer to stop the operation you can use `git rebase --abort`.

###  Send patch or patches

Once rebase is successfully finished and you check again that functionality is working right, you will **generate the patch or patches** with following command:

    $ git format-patch master

This will generate a `.patch` file for each commit. These files will be sent to [libreplan-devel@lists.sourceforge.net](https://lists.sourceforge.net/lists/listinfo/libreplan-devel), you can do it manually or using the following Git command:

    $ git send-email --to=libreplan-devel@lists.sourceforge.net <patch or patches files separated by space>

You can also use `--compose` which will allow you to write an introduction e-mail for your list of patches.

    $ git send-email --to=libreplan-devel@lists.sourceforge.net --compose <patch or patches files separated by space>

You can configure the mailing list by default in your `.gitconfig` file:

    [sendemail]
           to = libreplan-devel@lists.sourceforge.net

Then someone will review the patch and if everything goes right the patch will be pushed to central repository. In that moment developer could remove the local branch as it's not needed to keep local changes anymore.

###  Working with remote branches

All these examples are taking as example that you work against `master` remote branch, this mean that you're working with last developments done by all contributors. Sometimes you would like to work with a remote branch for example a stable branch, or a branch for a new feature that is big enough to be done in a separate branch.

In that case you should create a new local branch which corresponds to remote branch, it's recommended that local branch has the same name that remote branch to make you easier to detect the matchings. For example, for stable remote branch `libreplan-1.2` you would use the following command:

    $ git checkout origin/libreplan-1.2 -b libreplan-1.2

Then from local branch (which is the same than the remote one) you will create new branches to fix issues like [here](LibrePlan_LibrePlanGit#Create_new_branch) but rebasing against `libreplan-1.2` instead of `master`.

 Reviewer profile
-----------------

###  Clone repository with write permissions

People with total access to central repository should **clone it via SSH** to have write permissions:

    $ git clone git@github.com:Igalia/libreplan.git

###  Apply patch or patches

In order to apply a patch or patches sent by developers, these patches should be downloaded to filesystem.

Then the recommendation is to **create a new branch to review and test the patch**:

    $ git branch test-patch-xxxx
    $ git checkout test-patch-xxxx
    $ git am <patch or patches files separated by space>

If patch is not generated with `format-patch` and it's a simple `diff` file, you can apply it with following command:

    $ git apply <patch or patches files separated by space>

The preference is to have patches generated with `format-patch` and applied with `am` in order to **keep identity of original author**.

###  Push changes

If everything goes right and patch works fine, it's time to **push it to central repository**. Use the following commands sequence:

    $ git checkout master
    $ git merge test-patch-xxxx
    $ git push origin master

Then you can remove the temporal branch with following command:

    $ git branch -d test-patch-xxxx

Once a patch o list of patches is reviewed, even if it was or not applied. Reviewer should **reply to mailing list** ([libreplan-devel@lists.sourceforge.net](https://lists.sourceforge.net/lists/listinfo/libreplan-devel)) notifying developer about current state.

###  Remote branches

####  Create a remote branch

Sometimes it's needed to create a remote branch to develop a feature. In order to **create a remote branch** you should use the following command:

    $ git push origin origin:refs/heads/<branch_name>

In order to use this branch [see instructions below](LibrePlan_LibrePlanGit#Working_with_remote_branches).

####  Push changes in the remote branch

To push changes in this branch use the following command:

    $ git push origin <branch_name>

####  Update remote branch with the last changes in `master`

If you want to update the remote branch to last developments in the original branch (usually `master`) you should use the following commands:

    $ git co <branch_name>
    $ git merge master
    $ git push origin <branch-name>

This will create a merge commit and sometimes you'll need to solve some conflicts. The merge commit usually has the following message:

       Merge branch 'master' into <branch-name>

####  Merge remote branch into `master`

Once you have finished the work in the remote branch and it's already updated against `master` (see previous point) you should merge it into `master`:

    $ git co master
    $ git merge <branch_name>
    $ git push origin master

####  Deleting a remote branch

In case a remote branch is needs to be deleted for any reason, it can be removed from the repository with the next command:

    $ git push origin :<bad_remote_branch>

 Git tips and tricks
--------------------

###  Show branch name in prompt

In order to know in which branch you're, you can add the following line to your `.bashrc` to add **branch name in your prompt**:

    # Git prompt
    PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w$(__git_ps1 " (\[\033[31m\]%s\[\033[00m\])")\$ '

In Fedora you need to also add following line on `.bashrc`:

    source /etc/bash_completion.d/git

###  Avoid trailing whitespaces and tabs mixed with spaces

**Enable pre-commit hook**, that will automatically check if you don't have trailing whitespaces or tabs mixed with spaces before doing a commit. Use the following command to enable it:

    $ mv .git/hooks/pre-commit.sample .git/hooks/pre-commit

###  Iterative rebase

There is a very useful command to make an **iterative rebase** allowing you to merge some commits, remove some others and things like that. For example if you want to review and modify your lats 3 commits you would use the following command:

    $ git rebase -i HEAD~3
