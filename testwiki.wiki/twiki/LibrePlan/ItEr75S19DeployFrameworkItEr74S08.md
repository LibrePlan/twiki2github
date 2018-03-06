[TWiki](/twiki/Main/WebHome)&gt;![](/twiki/TWiki/TWikiDocGraphics/web-bg-small.gif) [LibrePlan Web](/twiki/LibrePlan/WebHome)&gt;[ItEr75S19DeployFrameworkItEr74S08](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08 "Topic revision: 4 (03 Jan 2012 - 15:16:30)") (03 Jan 2012, [JavierMoran](/twiki/Main/JavierMoran))[Edit](http://wiki.libreplan-enterprise.com/twiki/bin/edit/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?t=1520337925 "Edit this topic text")[Attach](/twiki/bin/attach/LibrePlan/ItEr75S19DeployFrameworkItEr74S08 "Attach an image or document to this topic")

 [ItEr75S19DeployFrameworkItEr74S08](/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08)
====================================================================================================================================================



|                        |                                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| Story summary          | Deploy framework                                                                                 |
| Iteration              | [ItEr75week25To52](/twiki/LibrePlan/ItEr75week25To52)                                   |
| FEA                    | [ItEr75S19DeployFrameworkItEr74S08](/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08) |
| Story Lead             | [ItEr74S08DeployFramework](/twiki/LibrePlan/ItEr74S08DeployFramework)                   |
| Next Story             |                                                                                                  |
| Passed acceptance test | No                                                                                               |

**Acceptance Criteria**

**Additional Specification Comments**

**Implementation Notes**

*jMeter cookies issue*

The way cookies (containing authentication tokens) are set vary depending on the application server being used. When an user hits the authentication URL and presents login credentials for the first time, two cookies are issued by the server: the anonymous session ID and the authenticated user session ID. Whereas Jetty provides separate Set-Cookie headers for each cookie, Tomcat pushes both tokens within a single header.

    HTTP/1.1 302 Found
    Date: Tue, 09 Aug 2011 13:35:21 GMT
    Expires: Thu, 01-Jan-1970 00:00:00 GMT
    Set-Cookie: JSESSIONID=t7onkwud0t2r1ep62uww9xqs9;Path=/navalplanner-webapp
    Set-Cookie: JSESSIONID=eaz1xhva4f96zi3whlo6z972;Path=/navalplanner-webapp
    Location: http://masterplan.libreplan.igalia.com:9901/navalplanner-webapp/;jsessionid=eaz1xhva4f96zi3whlo6z972
    Content-Length: 0
    Server: Jetty(6.1.24)

    HTTP/1.1 302 Moved Temporarily
    Server: Apache-Coyote/1.1
    Set-Cookie: JSESSIONID=F5644AE4355EF2BBF1B289ECAC308CF8; Path=/navalplanner-webapp
    JSESSIONID=E9FC4376392902BC8E25F9CE96EE77C6; Path=/navalplanner-webapp: 
    Location:
    http://masterplan.libreplan.igalia.com:9901/navalplanner-webapp/;jsessionid=E9FC4376392902BC8E25F9CE96EE77C6
    Content-Length: 0

In case equal cookies are set in the same header (particularly JSESSIONID), jMeter Cookie Manager stores just the first one, ignoring subsequent assignments. That behavior causes jMeter to store the anonymous token instead of the authenticated user one, causing successive requests to fail as the inappropriate session ID is sent to the server.

A simple way to work around this problem, is to issue an initial GET per client to collect an anonymous session ID first, to ensure that when the user authenticates only one cookie is issued and jMeter doesn't have any trouble storing the proper session ID.

I'm not sure if this should be considered as a bug or a feature. It depends on what HTTP's RFC says about this matter, specifically what the user agent should do if a cookie that was previously set is assigned again while continuing parsing Set-Cookie.

-- [NachoBarrientos](/twiki/Main/NachoBarrientos) - 16 Aug 2011

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



| [Tasks](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=0;table=2;up=0#sorted_table "Sort by this column") | [Est](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=1;table=2;up=0#sorted_table "Sort by this column") | [Spent](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=2;table=2;up=0#sorted_table "Sort by this column") | [To do](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=3;table=2;up=0#sorted_table "Sort by this column") | [Risk](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=4;table=2;up=0#sorted_table "Sort by this column") | [Reviewer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=5;table=2;up=0#sorted_table "Sort by this column") | [Developer](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=6;table=2;up=0#sorted_table "Sort by this column") | [Task Name](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=7;table=2;up=0#sorted_table "Sort by this column") | [Start Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=8;table=2;up=0#sorted_table "Sort by this column") | [Est End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=9;table=2;up=0#sorted_table "Sort by this column") | [End Date](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=10;table=2;up=0#sorted_table "Sort by this column") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Task                                                                                                                                                               | 35                                                                                                                                                               | 35                                                                                                                                                                 | 0                                                                                                                                                                  | Low                                                                                                                                                               | [JavierMoran](/twiki/Main/JavierMoran)                                                                                                                       | [NachoBarrientos](/twiki/Main/NachoBarrientos)                                                                                                                | [Stress load tests for the application](/twiki/LibrePlan/AnA04S05DeployFramework#TasK3)                                                                       | 0                                                                                                                                                                       | 0                                                                                                                                                                         | 0                                                                                                                                                                      |

###  Total Hours in this Story

| [User](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=0;table=3;up=0#sorted_table "Sort by this column") | [Spent in XpTracker](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=1;table=3;up=0#sorted_table "Sort by this column") | [Spent in phpReport](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=2;table=3;up=0#sorted_table "Sort by this column") | [Ok?](http://wiki.libreplan-enterprise.com/twiki/LibrePlan/ItEr75S19DeployFrameworkItEr74S08?sortcol=3;table=3;up=0#sorted_table "Sort by this column") |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NachoBarrientos](/twiki/Main/NachoBarrientos)                                                                                                           | 35                                                                                                                                                                              | 0                                                                                                                                                                               | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                |
| Total                                                                                                                                                             | 35                                                                                                                                                                              | 0                                                                                                                                                                               | ![ALERT!](/twiki/TWiki/TWikiDocGraphics/warning.gif "ALERT!")                                                                                                |

------------------------------------------------------------------------
