---
id: "9FwDDivrNT4"
title: "Tosca Tutorial - New features released in latest version of Tosca 16.0"
url: "https://www.youtube.com/watch?v=9FwDDivrNT4"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 1713
upload_date: "20230104"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:53:08Z"
status: "raw"
---

# Tosca Tutorial - New features released in latest version of Tosca 16.0

[00:00] Hey everyone, welcome again to another interesting Tosca lesson. In today's session, I'm going to talk about the new Tosca 16 features. Now recently, couple of weeks back, Tosca released its latest version which is 16.0 and along with it came some interesting features which are new and some improvements. So we are going to talk about few of them, not all of them. If you want to go through the list of all the features released in Tosca 16, you can go to the blog introducing new features in Tosca 16 and there you will find the list of all the different features which were released in this version.

[00:45] Now out of all these different features which includes the Tricentis Mobile Agent for seamless connectivity for Android and iOS, some of the important features which I would like to pick it up and explain it to you because I find it quite interesting and also quite useful if you are working in these applications. So we are going to talk about Enhanced Test Automation for Oracle and how Tosca has introduced the new Tosca ID Mapper along with the support for ARIA framework which helps you to build your automation for Oracle Enterprise applications.

[01:29] So we are going to talk about these two features in particular and then we are also going to look at their new UI. It's a little different, Tosca 16 compared to all the previous versions, there is a new theme which you can implement, a dark theme along with some other themes which are quite intuitive in terms of UI so we'll see how it looks like in this particular session. There is also cloud license supporting, it's mostly for Tosca admins and then we'll also talk briefly about this test case pre-execution approval which is quite interesting if you are looking for getting an automated flow of approval of your test cases before you go ahead and execute these test cases.

[02:24] So there is an automation flow through which you can request for approval for your test cases and also a group can basically review and approve your test cases before these go into the execution. So it's a very interesting feature, we'll talk about it and there are some other enhancements like improvements to file service, some SAP innovations, Q-test integration, DEX enhancements, improvements to PDF automation, very interesting if you are working with the PDF comparison, there is the mainframe improvements and also support for Java 17 and then support for the latest Windows 11.

[03:14] So all of these are different enhancements and features which have been released in Tosca 16. If you want to go through the whole list and details you can always hop into this link and go through the details but I'm going to focus on few of these features which I think is important and also useful if you are working in these enterprise applications and overall Tosca 16.

[03:44] So now let's get started with our first topic which is enhance test automation for Oracle. Now if you have been working with Oracle applications you know automated testing is quite critical for ensuring your business processes are reliable. But Oracle implementations are quite highly customized and they are integrated with many other systems which are under constant change. So testing end to end is quite crucial.

[04:17] But Oracle apps they all have like any other ERP system contain dynamic controls which are sometimes difficult to automate. So with Tosca 16.0 now Tosca has introduced the Tosca ID mapper and support for ARIA framework so that all the complex controls which are found in the Oracle applications can be identified easily and your automation could be more stable.

[04:50] So talking more about this ID mapper right so with the Tosca new ID mapper now we can select our own application under test uniquely identify controls by adjusting the properties and then save all the default IDs in a particular library which we can use for future use or if some someone else wants to use this particular library they can also use it for other applications.

[05:21] So it is a comprehensive way to identify various control types and also it lowers your efforts in terms of test customization and it also increases stability. So now let's head back to our Tosca 16.0 Tosca Commander and there we will look at how the new ID mapper functionality looks like how you can use it to implement different automation for your Oracle applications and how it is helpful in terms of identifying controls uniquely across your ERP systems.

[06:04] So now I have opened my Tosca 16.0 which is the latest version of Tosca. Now it's quite easy to upgrade or if you are installing Tosca 16.0 as a completely new version in one of your windows server or machine you just need to download the latest version of Tosca 16.0 from the Tricenter support portal where you have created an account and you have got a trial or a full license you can just download it and just go through the installation it's pretty simple and straightforward.

[06:40] So I'm not going to spend time on showing you how to install or upgrade the Tosca version which you are currently on or you are trying to install a completely new version. Now just to make sure that I am on the right version I can also go to my About Tosca and check whether this is the latest Tosca 16.0 so which it is right so the version is 16.0 and you can already notice there are some UI changes but we'll talk about it later.

[07:17] For now let's concentrate on our enhanced test automation for Oracle applications including the Tosca ID mapper. So for this I have already logged into one of the Oracle ERP application and here we are going to look at how we can use the Tosca ID mapper in order to uniquely identify controls in this particular application. So for this particular purpose let's go to create a new contact and once we reach this page we'll see different controls which are Oracle based and which are pretty dynamic in nature.

[08:04] If you look at their IDs they are all dynamic IDs. So as you can see on this page there are a couple of control types like text boxes drop downs and buttons. So there are different types of controls present on this particular page. So let's go back to our Tosca and here inside modules let's create a new folder so that we can scan this particular application.

[08:36] So here I'm going to create a folder called ERP cloud and inside this let's go ahead and scan this application. So once the application is identified just select the application and click on scan so that it starts or the X scan window appears with all the different controls which you want to scan for this particular application.

[09:11] So we'll go to the advanced tab once all the controls are loaded in this particular X scan window. OK so let's go back to the advanced window and here we can view all the controls which are present for this particular page. Now if you have worked previously in Tosca most of the things on this particular screen would look same. We have different controls we have different properties through which these controls are identified.

[09:44] But what Tosca has done in addition to this is for the Oracle applications now they have got a settings icon here. And in the settings icon you will see different options here we'll talk about the ARIA controls. You can turn on and off this ARIA controls. But let's focus on the Tosca ID mapper and for that you need to go to the unique application identifiers section.

[10:20] So here we can create our own application identifiers through which we can define default IDs for controls in a particular application. So for this Oracle application we can have our own default IDs for all the controls so that they can be uniquely identified using these default IDs. So for this what we have to do is we have to define an application name. So for here I will put Oracle.

[10:55] And you will see the application identifier is by default it is selected as title. You also have an option for URL and the value is automatically created for this particular page. So now this is a unique application identifier which is specific for a specific application which you have defined on your own. And now let's go ahead and save this. So once you save this it is going to save these default IDs.

[11:29] And then we'll look at one of the controls say for example first name which is a text box. So let's close this window and let's come here and here we'll see the different controls. We want this first name which is a text box we want to select this. So once you select this all the properties would start appearing here.

[12:00] And you will see that it has selected or it has scanned this control and it is able to identify using ID and some tag value. But the problem with the ID is as you can see it is pretty dynamic right. So you cannot basically depend on this ID which looks pretty dynamic and it can change anytime. So what we'll do we'll deselect this ID and instead of that what we'll select is we'll have a default name which is first name and then we will also select the visible property which is true.

[12:43] So these are the two properties through which we want to identify this control. And the other thing which we want to do is we want to define a default ID on the application level for this control. So this is the Tosca ID mapper. It maps your IDs with your controls. So now we can define our own default ID at an application level. So as you can see here once you select that option it comes as select application.

[13:16] So choose from previously configured applications where you want to save the default defined default IDs. And here we can select our application which we have created earlier in the settings. So here you will see there is an option called Oracle which we have created earlier. So select that and click on save and now the control would be reloaded. And you will see that it has got now a default ID at an application level and it will always select based on these two properties.

[13:55] Now the other good thing about this is it's not only applicable for this particular control but for all the other controls on this application. Like if I go to last name and you will see by default it has selected the default name and visible property. But if I would have not given ID mapper or I would not have selected ID mapper then it would have probably selected based on the ID and tag.

[14:27] But since we have defined default ID at application level so all the controls in this application will have this default ID through which it can uniquely identify all these controls. So this is how the Tosca ID mapper works. You need to go to the settings icon which is a new icon on the X-can window and you can define your own application name with a value.

[15:02] And then you can save it and then you can go to the control and you can select that particular value or that application ID which you have created and you can select it for all your controls in the application. This way it will be more stable and you don't need to customize it for every control. It will be automatically customized for all the controls in your application. So your customization time goes down and you can focus more on the automation rather than spending time on customizing each and every control in the ERP application.

[15:43] Now let's talk about the next feature which is available in enhanced test automation for Oracle in Tosca 16.0 which is the support for ARIA framework. But before that let's understand a little bit about what is ARIA and ARIA stands for Accessible Rich Internet Applications. It is a framework that makes it easy for users with disabilities to view, interact or access web content and applications. It is used by assistive technologies like screen readers, magnifiers or text-to-speech.

[16:20] And ARIA can be implemented across any mobile web or enterprise application like Oracle, Workday, Microsoft Dynamics 365, SAP and others. Now why this is important is because ARIA framework is going to be more and more used across all the applications. All the controls are going to be built using the ARIA framework to help users with disabilities to interact with these applications more easily. And this is being regulated by the European Union which is soon going to make it mandatory for most of the applications to have this ARIA framework implemented in their applications by 2025.

[17:04] So in Tosca 16.0, it provides you with inbuilt capabilities to automate these controls with ARIA labels. It decides based on the steering parameter if the native ARIA support should be considered or not. So now let's see how you can use this feature which is the support for ARIA framework in applications like Oracle to identify controls based on this particular feature.

[17:37] So let's go back to our ERP application and let's go to some other page to view some controls which we can link with the ARIA framework. So I'm going to go to a page and add absence here from the ERP application. That will take me to this page where I can select a value for my leave type and then I can proceed.

[18:13] But the thing to note here is these three buttons. Now these three buttons are built with the ARIA framework. And how I can tell that is let's add another module for this particular page. So let's scan the application. Now we can select the application and click on scan.

[18:43] So once the advanced view is displaying all the controls again the new settings icon which we already talked about. So click on that and then it will open a settings window where you can find general settings. There is an option to either ignore or enable the ARIA controls.

[19:15] So by default this option would not be checked out. That means the ARIA controls would be taken into consideration by Tosca. But if you want to ignore ARIA controls you can select this and click on save and that should basically turn off this feature which means all your controls would now be normally identified by the properties. But since we want to see how we can identify our controls using the new ARIA framework support provided by Tosca 16.

[19:49] So let's check this out and click on save and then just close the settings dialog box. Now let's shift our focus to the three controls which are on the top of this page right so which are the save and close submit and cancel. Now as you can see these three controls or buttons are within a table. Now if you have not enabled the ARIA support provided by Tosca then these three buttons would be mostly visible like a div elements and div elements are difficult to identify as you know since there would be a lot of div elements and there would not be any unique property through which you can identify them.

[20:37] So when you enable the ARIA framework support then these are displayed as buttons and if I select one of these buttons and I go to one of its properties we can see that this is ARIA framework control. So if you go to the adapter and you can see here it is showing up as trisynthes.automation.engines.adapter and .aria.aria button adapter right.

[21:15] So it is one of the ARIA framework buttons or controls through which Tosca is able to identify these controls as specific buttons right. If it is not if the support is not present or the ARIA framework is not supported then it would be difficult to identify these controls on the application. So I can select all these three buttons using the ARIA framework support and I can save it to my module and close this particular xcan to have my module ready and now I can work out with these three controls right.

[22:03] So this is how you can turn on and turn off the ARIA framework support if you are working with specific ARIA controls it's best to have that enabled so that you can easily identify those controls and start working on the automation of your application. Now the next feature which we are going to talk about is the new changed UI of Tosca. As you can see the buttons or the folders are a little different compared to the previous versions they have changed the folder icons a little bit the colors have changed the UI looks a little different right and they have also introduced a few other themes apart from the default theme.

[22:52] Now personally I really like this theme I've been working it's little dark right now but I personally prefer the default theme but if you go on the top you will see this window and right now I am on the light theme and there are other high contrast light and high contrast dark and also the popular dark theme. Now if you are used to working on dark themes specially on different IDs this could be ideal for you to get this dark theme enabled for your Tosca 16.0.

[23:34] So you can always change back your theme to the light default theme which is my personal favorite so that's a new feature a new theme which has been introduced in Tosca 16.0 and it provides you with a different UI layout which is better for different users depending on your personal choices and how you are used to working with different automation tools or IDs.

[24:07] Now talking about the final feature in this particular session so the test case is pre-execution approval which is an automated process being introduced in Tosca 16.0. Now let's talk about it what it is and how does it work. So Tosca pre-execution approval as I said it's an automated process to request and grant approval for your test cases. It allows us to validate our test cases before they are run so that the test cases are all validated and no unauthorized modifications can be done on these test cases if they are once validated and approved.

[24:55] The approval process is only for test cases. Now do remember that it doesn't include other objects like test case templates business test cases modules or execution lists. This is purely for your test cases. So how it is done the test case work state which you must have seen it has got three basically three stages planned in work and completed and with this pre-execution approval the test case work state can be used by Tosca to change the approval state of the test cases.

[25:35] So it lets users know how far along the test cases is either planned in work or completed. Now if we use pre-execution approval only Tosca can change the state automatically. So if for every new test case that's in progress has the state planned and when the user requests approval for a test case Tosca changes it to in work and then approved test cases get the state completed and rejected test cases go back to planned.

[26:09] So this is how the test cases pre-execution approval works. Now ideally I would have shown you how it works but it is not possible to show you this feature currently because I'm working on a single user workspace and this particular feature works when you are working within a team on a multi-user workspace so that it goes through different review process before the test cases can be approved and then go into the execution that would be a specific user group assigned and that user group will take care of reviewing the test cases and then approving them.

[26:49] But I can tell you that if you're working on a multi-user workspace you can go to root project level and right click and then you can enable that feature right from this particular menu. You can always create your own user group at this level so that that user group would be taking care of this whole approval and review process. So that's all about this particular feature it is very interesting to know.

[27:24] I wish I could have shown you more on this feature but maybe in the later sessions I would try to show you this new feature which is available in Tosca 16.0. So that's all for this session I hope it was interesting to know all the new features which are currently available in Tosca 16.0. I would highly recommend all of you to upgrade to the latest version of Tosca if you have not already done or if you are installing it completely new it's a good time to start installing Tosca 16.0 and interacting with all the different new features which are currently available. There are lots of different enhancements which would help you to increase your automation coverage and especially if you're working with ERP applications then there are lots of different features which can help your automation become more robust and also decrease the time you spend on customizing your automation for these applications. So keep watching we'll be coming up with more

[28:30] interesting Tosca lessons.
