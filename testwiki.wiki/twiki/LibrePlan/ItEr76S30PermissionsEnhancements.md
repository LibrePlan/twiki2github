[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S30PermissionsEnhancements](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements "Topic revision: 17 (20 Aug 2012 - 09:50:20)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S30PermissionsEnhancements?t=1520337942 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S30PermissionsEnhancements "Attach an image or document to this topic")

 [ItEr76S30PermissionsEnhancements](/twiki/LibrePlan/ItEr76S30PermissionsEnhancements)
==================================================================================================================================================



|                        |                                                                                                |
|------------------------|------------------------------------------------------------------------------------------------|
| Story summary          | Permissions Enhancements                                                                       |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)                                 |
| FEA                    | [ItEr76S30PermissionsEnhancements](/twiki/LibrePlan/ItEr76S30PermissionsEnhancements) |
| Story Lead             |                                                                                                |
| Next Story             |                                                                                                |
| Passed acceptance test | No                                                                                             |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

######  Fix issues in web services permissions

Moved subcontracting web services to path `/ws/rest/subcontracting/`.

Created new role `ROLE_WS_SUBCONTRACTING` and protected that path with this role in Spring Security file.

Keeping `/ws/rest/` path accessed by `ROLE_WS_READER` and `ROLE_WS_WRITER`.

Created a new default user **wssubcontracting** wiht password **wssubcontracting** that will be an example for testing the subcontracting operations.

-- [ManuelRego](/twiki/Main/ManuelRego) - 11 Jun 2012

######  Menu refactoring

Refactored LibrePlan menu using the new structure.

-- [ManuelRego](/twiki/Main/ManuelRego) - 15 Jun 2012

Reviewed page titles and other strings due to menu revamp.

-- [ManuelRego](/twiki/Main/ManuelRego) - 21 Jun 2012

######  Create new architecture of permissions

Review alternatives to `intercept-url` in Spring Security config file. Tried the following approaches without success so far, so coming back to original plan and use `intercept-url`:

-   Use `=[http://static.springsource.org/spring-security/site/docs/2.0.x/apidocs/org/springframework/security/annotation/Secured.html][@Secured]]` annotation. After reading some documentation it seems that it only works for Spring beans and LibrePlan controllers are not Spring beans.
-   Define a new annotation (like `@OnConcurrentModification`) but again it only worked in Spring beans.

Renamed current roles (take advantage to rename column `elt` to `role` in both `roles_table` and `profile_roles`):

-   `ROLE_ADMINISTRATION` to `ROLE_SUPERUSER`
-   `ROLE_READ_ALL_ORDERS` to `ROLE_READ_ALL_PROJECTS`
-   `ROLE_EDIT_ALL_ORDERS` to `ROLE_EDIT_ALL_PROJECTS`
-   `ROLE_CREATE_ORDER` to `ROLE_CREATE_PROJECTS`

Configured basic permissions for the new roles. Show or not menu entries depending on user roles.

Manage special role `ROLE_BOUND_USER` from worker and user windows. All bound users must have this role.

Configured properly permissions for `ROLE_BOUND_USER`:

-   Only bound users will have access to page *Personal Area &gt; Home*
-   Moreover bound users will have access to expenses sheet edition form, even if they don't have access to *Cost &gt; Expenses* page
-   Finally users with role `ROLE_SUERUSER`, `ROLE_BOUND_USER` or `ROLE_TIMESHEETS` will have access to monthly timesheets edition page.

Disabled buttons to go to edit user from workers window and edit worker from users windows if user doesn't have the required permissions.

Remove role `ROLE_BOUND_USER` from the list of roles to be added to a user or profile. As this role is managed automatically by the application and not manually by any administrator.

-- [ManuelRego](/twiki/Main/ManuelRego) - 15 Jun 2012

Configured `ROLE_PROJECT_PLANNING` to restrict access to company perspectives. However, company Gantt and projects list is also accessible for users that have read/write permissions over any project.

Changed initial page depending on user roles (modified class `org.libreplan.web.users.services.CustomTargetUrlResolver`):

-   `ROLE_SUPERUSER`: *Planning &gt; Company view* (or the URL specified if any, keeping how it worked in the past)
-   `ROLE_BOUND_USER`: *Personal Area &gt; Home*
-   `ROLE_PROJECT_PLANNING` or read/write permissions over any project: *Planning &gt; Company view*
-   Other: *Personal Area &gt; Preferences*

Due to this change it was also needed to review the behavior when users clicks in LibrePlan logo.

-   Modified `web.xml` to redirect to a new `index.zul` page

<!-- -->

        <welcome-file-list>
            <welcome-file>/common/index.zul</welcome-file>
        </welcome-file-list>

-   Implemented the controller for this new page `org.libreplan.web.common.IndexController` redirecting user to different pages depending on roles (like specified above).

Protect some things related to roles:

-   Do not allow to create *Labels* from project edition if the user has not the proper role
-   Do not allow to create *Templates* from project edition if the user has not the proper role

-- [ManuelRego](/twiki/Main/ManuelRego) - 19 Jun 2012

Protect some special pages:

-   Protect page *Cost &gt; Expenses* to avoid that a user with `ROLE_BOUND_USER` knows the URL and try to edit or remove other expenses sheet (not their own personal sheets). Entry points in *Cost &gt; Expenses* can only be used by `ROLE_BOUND_USER`, moreover in edition it's checked that the expenses sheet is personal and belongs to the worker bound to current user.
-   Protect page for monthly timesheets in order to prevent wrong editions. A `ROLE_BOUND_USER` can only edit its own personal monthly timesheets. A `ROLE_SUPERUSER` or `ROLE_TIMESHEETS` has to set the resource in the URL to be able to edit a monthly timesheet.

Create a new page to manage HTTP 403 forbidden status code.

-- [ManuelRego](/twiki/Main/ManuelRego) - 20 Jun 2012

######  Profiles

Created the default profiles with the defined roles.

-- [ManuelRego](/twiki/Main/ManuelRego) - 15 Jun 2012

######  Default users

Modified `MandatoryUser` to add the new users and allow to specify profiles.

Having a hard time fighting with tests like `DBUserDetailsServiceTest` due to some Hibernate issues. Finally I fixed these problems marking as `@Rollback(false)` the method `org.libreplan.web.test.users.bootstrap.UsersBootstrapInDBTest.testMandatoryUsersCreated()`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 20 Jun 2012

Modified `admin` user edition, as it's not allowed to add/remove roles or profiles in that user, change the username or disable it. Moreover, it's not allowed to remove `admin` default user.

Changed the behavior of `UsersBootstrapInDB` to create users only if the users table in the database is empty. This makes it works like the other bootstraps. If someone decides to remove some default users like `manager` or `wswriter`, the bootstrap is not going to create them again.

-- [ManuelRego](/twiki/Main/ManuelRego) - 21 Jun 2012

######  Fix reports

Fixed models of reports using the next method to get the list of projects `org.libreplan.business.orders.daos.OrderDAO.getOrdersByReadAuthorizationByScenario(String username, Scenario scenario)`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 21 Jun 2012

######  Review entry points

For the first case, the entry point in *Timesheets Lines List Report* was not really an entry point. The file `workReportQuery.zul` has the edition form part copied from `workReport.zul`, moreover this part was not properly updated as we usually only fixed bugs in `workReport.zul`. So, a new specific controller has been created for `workReportQuery.zul` removing the part for the edition form and using an entry point to edit the work report.

Later the entry point has been protected depending on user permissions.

Protect also the rest of cases specified in the analysis.

-- [ManuelRego](/twiki/Main/ManuelRego) - 26 Jun 2012

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S30PermissionsEnhancements?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                              | 4                                                                                                                                                               | 3.75                                                                                                                                                              | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Fix issues in web services permissions](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK1)                                                             |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 4                                                                                                                                                               | 20.25                                                                                                                                                             | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Create new architecture of permissions](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK2)                                                             |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 3                                                                                                                                                               | 1                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Profiles](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK3)                                                                                           |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 3                                                                                                                                                               | 7.75                                                                                                                                                              | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Default users](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK4)                                                                                      |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 3                                                                                                                                                               | 5                                                                                                                                                                 | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Menu refactoring](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK5)                                                                                   |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 7                                                                                                                                                               | 2.25                                                                                                                                                              | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Fix reports](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK6)                                                                                        |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |
| Task                                                                                                                                                              | 4                                                                                                                                                               | 7.75                                                                                                                                                              | 0                                                                                                                                                                 | Low                                                                                                                                                              | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                      | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                                         | [Review entry points](/twiki/LibrePlan/AnA20S01PermissionsEnhancements#TasK7)                                                                                |                                                                                                                                                                        |                                                                                                                                                                          |                                                                                                                                                                       |


