[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr76S28UserDashboard](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard "Topic revision: 26 (20 Aug 2012 - 09:50:20)") (20 Aug 2012, [ManuelRego](/twiki/Main/ManuelRego))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr76S28UserDashboard?t=1520337942 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr76S28UserDashboard "Attach an image or document to this topic")

 [ItEr76S28UserDashboard](/twiki/LibrePlan/ItEr76S28UserDashboard)
====================================================================================================================



|                        |                                                                            |
|------------------------|----------------------------------------------------------------------------|
| Story summary          | User dasboard for bound users                                              |
| Iteration              | [ItEr76Week01To33](/twiki/LibrePlan/ItEr76Week01To33)             |
| FEA                    | [ItEr76S28UserDashboard](/twiki/LibrePlan/ItEr76S28UserDashboard) |
| Story Lead             |                                                                            |
| Next Story             |                                                                            |
| Passed acceptance test | No                                                                         |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

######  Configure dashboard page as home page for bound users

Trying to redirect user to user dashboard page after login if the user is bound.

The first idea has been try to do it with an `AplicationListener`:

-   Configuring `libreplan-webapp/src/main/resources/libreplan-webapp-spring-security-config.xml`:

            <!-- This bean is used to redirect user after login -->
            <beans:bean id="authenticationSuccessListener"
                class="org.libreplan.web.users.services.AuthenticationSuccessListener" />

-   And implementing the listener:

        public class AuthenticationSuccessListener implements
                ApplicationListener {

            @Autowired
            private IUserDAO userDAO;

            @Override
            public void onApplicationEvent(ApplicationEvent applicationEvent) {
                if (applicationEvent instanceof AuthenticationSuccessEvent) {
                    AuthenticationSuccessEvent event = (AuthenticationSuccessEvent) applicationEvent;
                    UserDetails userDetails = (UserDetails) event.getAuthentication()
                            .getPrincipal();

                    try {
                        User user = userDAO.findByLoginName(userDetails.getUsername());
                        if (user.isBound()) {
                            System.out.println("Redirect to user dashboard");
                        }
                    } catch (InstanceNotFoundException e) {
                        throw new RuntimeException(e);
                    }
                }
            }

But it's not possible to access the HTTP request to do the redirect from the `ApplicationListener`.

-- [ManuelRego](/twiki/Main/ManuelRego) - 11 May 2012

The second idea was try to define a `AuthenticationProcessingFilter` which was not easy ![frown](/twiki/TWiki/SmiliesPlugin/frown.gif "frown")

Describing the process:

1) First attempt:

-   Configuring `libreplan-webapp/src/main/resources/libreplan-webapp-spring-security-config.xml`:

            <authentication-manager alias="authenticationManager" />

            <beans:bean id="customAuthenticationFilter"
                class="org.libreplan.web.users.services.CustomProcessingFilter" >
                <custom-filter position="AUTHENTICATION_PROCESSING_FILTER" />
                <beans:property name="authenticationManager" ref="authenticationManager" />
                <beans:property name="defaultTargetUrl" value="/planner/index.zul" />
                <beans:property name="authenticationFailureUrl" value="/common/layout/login.zul?login_error=true" />
                <beans:property name="allowSessionCreation" value="true" />
            </beans:bean>

-   The problem here is that you get the following exception:

        Error creating bean with name '_filterChainProxy': ...

-   The reason of this problem is that you're setting a custom filter at `AUTHENTICATION_PROCESSING_FILTER` and this collide with the filter defined automatically by the tag `http/login-form`.

2) Second attempt:

-   Modify `http` tag in `libreplan-webapp/src/main/resources/libreplan-webapp-spring-security-config.xml`:
    -   Remove `http/login-form`
    -   Set `auto-config` to `false`. This implies that we have to add the next tags ([more info](http://static.springsource.org/spring-security/site/docs/2.0.x/reference/ns-config.html#ns-auto-config)):

                    <anonymous />
                    <http-basic />
                    <logout />
                    <remember-me />

    -   It's also needed to set `entry-point-ref` attribute pointing to an entry point:

            entry-point-ref="customAuthenticationEntryPoint"

-   The entry point configuration:

            <beans:bean id="customAuthenticationEntryPoint"
                class="org.springframework.security.ui.webapp.AuthenticationProcessingFilterEntryPoint">
                <beans:property name="loginFormUrl" value="/common/layout/login.zul"/>
            </beans:bean>

-   And then the `CustomAuthenticationFilter` implementation overriding method `onSuccessfulAuthentication`:

        public class CustomAuthenticationFilter extends AuthenticationProcessingFilter {

            private static String USER_DASHBOARD_URL = "/myaccount/userDashboard.zul";

            @Autowired
            private IUserDAO userDAO;

            @Override
            protected void onSuccessfulAuthentication(HttpServletRequest request,
                    HttpServletResponse response, Authentication authResult)
                    throws IOException {

                UserDetails userDetails = (UserDetails) authResult.getPrincipal();

                try {
                    User user = userDAO.findByLoginName(userDetails.getUsername());
                    if (user.isBound()) {
                        // Redirect to user dashboard
                        response.sendRedirect(response
                                .encodeRedirectURL(USER_DASHBOARD_URL));
                    }
                } catch (InstanceNotFoundException e) {
                    throw new RuntimeException(e);
                }
            }

        }

-   The problem here is that in the redirect you get a `java.lang.IllegalStateException` because of response header has been already sent to the user and you're trying to change it again.

3) Third and **final** attempt:

-   Instead of define a custom authentication filter, just configuring a target URL resolver changing configuration in `libreplan-webapp/src/main/resources/libreplan-webapp-spring-security-config.xml`:

            <beans:bean id="customAuthenticationFilter"
                class="org.springframework.security.ui.webapp.AuthenticationProcessingFilter" >
                <custom-filter position="AUTHENTICATION_PROCESSING_FILTER" />
                <beans:property name="authenticationManager" ref="authenticationManager" />
                <beans:property name="defaultTargetUrl" value="/planner/index.zul" />
                <beans:property name="authenticationFailureUrl" value="/common/layout/login.zul?login_error=true" />
                <beans:property name="allowSessionCreation" value="true" />
                <beans:property name="targetUrlResolver" ref="customTargetUrlResolver" />
            </beans:bean>

-   Configuring the target URL resolver:

            <beans:bean id="customTargetUrlResolver"
                class="org.libreplan.web.users.services.CustomTargetUrlResolver" />

-   And implementing `CustomTargetUrlResolver` overriding the method `determineTargetUrl`:

        public class CustomTargetUrlResolver extends TargetUrlResolverImpl {

            private final static String USER_DASHBOARD_URL = "/myaccount/userDashboard.zul";

            @Autowired
            private IUserDAO userDAO;

            @Override
            public String determineTargetUrl(SavedRequest savedRequest,
                    HttpServletRequest currentRequest, Authentication auth) {
                UserDetails userDetails = (UserDetails) auth.getPrincipal();

                try {
                    User user = userDAO.findByLoginName(userDetails.getUsername());
                    if (user.isBound()) {
                        return USER_DASHBOARD_URL;
                    }
                } catch (InstanceNotFoundException e) {
                    throw new RuntimeException(e);
                }

                return super.determineTargetUrl(savedRequest, currentRequest, auth);
            }
        }

-- [ManuelRego](/twiki/Main/ManuelRego) - 16 May 2012

Hide user dashboard page from menu if resource is not bound.

-- [ManuelRego](/twiki/Main/ManuelRego) - 06 Jun 2012

######  My tasks area

Implemented the new area using a simple grid this will need more work to improve the UI, review what happens with lots of tasks and maybe decide what should be the order.

-- [ManuelRego](/twiki/Main/ManuelRego) - 16 May 2012

Added operations column with link to time tracking for the task.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Jun 2012

Sorted tasks descending by start date.

-- [ManuelRego](/twiki/Main/ManuelRego) - 06 Jun 2012

######  Model for the Monthly timesheets

Created new work report type.

Modified work report type UI to hide the new type, and prevent to edit or remove it.

-- [ManuelRego](/twiki/Main/ManuelRego) - 22 May 2012

######  Monthly timesheet creation/edition

Created the list of monthly timesheets list for an user based on the activation date of the bound resource.

The code for the different parts of the user dashboard has been separated in different files (`.java` and `.zul` files).

First implementation of monthly timesheet grid, but there're lots of things pending:

-   It only shows the tasks where the resource is assigned
-   It is using the first TypeOfWorkHours found (we have to fix this in the future)
-   The work report code is not being generated correctly yet
-   ...

-- [ManuelRego](/twiki/Main/ManuelRego) - 23 May 2012

The `TypeOfWorkHours` for the monthly timesheets has been added as a new field in the configuration window. The analysis has been updated accordingly ([see more](/twiki/LibrePlan/AnA12S04UserDashboard#TasK4)).

-- [ManuelRego](/twiki/Main/ManuelRego) - 28 May 2012

Added capacity and total rows in the monthly timesheet. Created a new mini-class called `MonthlyTimesheetRow` to manage the different rows in order to render them in the timesheet.

Set a pink background in the columns with zero capacity.

Show a empty string when the effort is zero, and also accept an empty string to set a zero effort.

Added a *BandboxSearch* to allow add any task to the monthly timesheet.

Added **Previous** and **Next** buttons. These buttons check if the timesheet has been modified and in that case request the user to save before moving to a different month (the *Save & continue* button has been added). Moreover, as it was not hard to implement, the inputs that are modified by the user are marked with a red border.

-- [ManuelRego](/twiki/Main/ManuelRego) - 29 May 2012

The list of tasks in the monthly timesheets is sorted now (sorted by project name and if it's equal by task name). The list keeps sorted when adding new tasks.

The codes for the monthly timesheet work reports are generated properly now.

Added the missing columns in monthly timesheets area.

Added new **Extra** row.

-- [ManuelRego](/twiki/Main/ManuelRego) - 30 May 2012

Modified ***Time trakcing*** UI:

-   Changes in the list:
    -   Added information about resource for monthly timesheets
    -   Added *Total work* column from monthly timesheets area
-   Use new grid to create and edit monthly timesheets. In this case, the *Previous* and *Next* buttons won't appear and a warning about using the grid from the work reports page will be shown. After saving or canceling the user will go back to *Time tracking* page.

-- [ManuelRego](/twiki/Main/ManuelRego) - 01 Jun 2012

Modified work reports service to prevent wrong modifications of monthly timesheets.

Added message when using button *Save & continue*.

-- [ManuelRego](/twiki/Main/ManuelRego) - 05 Jun 2012

Added extra row and column called **Other**.

Created a summary box with info about the timesheet.

-- [ManuelRego](/twiki/Main/ManuelRego) - 06 Jun 2012

######  My expenses area

Fixed several things in expense sheets `.zul` and controller.

Modified the `ExpenseSheet` class to add the new field `personal` and implemented the tasks described in the analysis.

Add constraint in `ExpenseSheet` to avoid that a personal `ExpenseSheet` has different resources in each line. This is a way to protect wrong modifications from the web service.

-- [ManuelRego](/twiki/Main/ManuelRego) - 07 Jun 2012

|     |     |
|-----|-----|
|     |     |

**Delay Causes**

**Final or Pending Considerations**

-   **My tasks area**:
    -   Review UI of my tasks list (pagination)
-   **User dashboard**: Protect this page for unbound users (to be done in the permissions task)
-   **My expenses area**: Review permissions of the expenses sheet pages as the lines in the Spring security file has been commented out (due to the need to bound users are able to create expense sheets):

                <!-- FIXME review when role for bound users is set -->
                <!-- intercept-url pattern="/expensesheet/**" access="ROLE_ADMINISTRATION,ROLE_EXPENSE_TRACKING"/ -->

|     |     |
|-----|-----|
|     |     |

###  Commits

%RPSHOWGITCOMMITS%

###  Tasks in this story



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr76S28UserDashboard?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                    | 0                                                                                                                                                     | 6.5                                                                                                                                                     | 0                                                                                                                                                       | Low                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | Configure dashboard page as home page for bound users                                                                                                       |                                                                                                                                                              |                                                                                                                                                                |                                                                                                                                                             |
| Task                                                                                                                                                    | 4                                                                                                                                                     | 0.5                                                                                                                                                     | 0                                                                                                                                                       | Low                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | [Creation of the areas of the personal dashboard](/twiki/LibrePlan/AnA12S04UserDashboard#TasK1)                                                    |                                                                                                                                                              |                                                                                                                                                                |                                                                                                                                                             |
| Task                                                                                                                                                    | 7                                                                                                                                                     | 6                                                                                                                                                       | 0                                                                                                                                                       | Low                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | [My tasks area](/twiki/LibrePlan/AnA12S04UserDashboard#TasK2)                                                                                      |                                                                                                                                                              |                                                                                                                                                                |                                                                                                                                                             |
| Task                                                                                                                                                    | 7                                                                                                                                                     | 5                                                                                                                                                       | 0                                                                                                                                                       | Low                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | [Model for the Monthly timesheets](/twiki/LibrePlan/AnA12S04UserDashboard#TasK4)                                                                   |                                                                                                                                                              |                                                                                                                                                                |                                                                                                                                                             |
| Task                                                                                                                                                    | 20                                                                                                                                                    | 27.25                                                                                                                                                   | 0                                                                                                                                                       | Low                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | Monthly timesheet creation/edition[?](/twiki/bin/edit/LibrePlan/AnA1S04UserDashboard?topicparent=LibrePlan.ItEr76S28UserDashboard "Create this topic")      |                                                                                                                                                              |                                                                                                                                                                |                                                                                                                                                             |
| Task                                                                                                                                                    | 10                                                                                                                                                    | 9                                                                                                                                                       | 0                                                                                                                                                       | Low                                                                                                                                                    | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                            | [ManuelRego](/twiki/Main/ManuelRego)                                                                                                               | [My expenses area](/twiki/LibrePlan/AnA12S04UserDashboard#TasK7)                                                                                   |                                                                                                                                                              |                                                                                                                                                                |                                                                                                                                                             |


