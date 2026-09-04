---
id: "H5M6Y_Su4OQ"
title: "Tosca Tutorial | Lesson 156 - Test Configuration Parameters | Project Configurations |"
url: "https://www.youtube.com/watch?v=H5M6Y_Su4OQ"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 1381
upload_date: "20250613"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:25:38Z"
status: "raw"
---

# Tosca Tutorial | Lesson 156 - Test Configuration Parameters | Project Configurations |

[00:08] In this particular session, we are going to talk about test configuration, and then we'll talk about how to configure your tests in Tosca, and what are test configuration parameters, where you can set this configuration parameters, and then what types of configuration parameters are present in Tosca. But first, let's try to understand what is test configuration, and then why do you need it. So in any automation framework or any automation tool you are using, if you are building some automation tests, then you want to run that automation test multiple times with different set of values.

[00:49] For example, if you are running your tests in a particular environment, which has got a URL, right, and then you want to run the same test with a different URL the second time around. So you have to go back and either change your test value right in your script, or what you can do is you can create a configuration parameter, and then use that parameter in your test, so that you don't need to change the value at different places in your test script.

[01:23] That will only increase your test development time. Also it will increase your maintenance time when any of the tests which you have developed fail. So to make this easier and also less time consuming, we generally configure our tests. So every test framework has got some level of configurable values, and these values could be used in your test scripts, so that they could be developed much faster and also they could be maintained easily.

[01:59] Now, in Tosca, we can configure our tests using the test configuration parameters. So we can set values for these parameters, and then we can use them in our tests. Now these configuration parameters can be set for different Tosca objects, right from the root element to component folders, to configuration folders, to test cases, executions, and even the test case design folder, right.

[02:31] So everywhere you will find a tab, which is the test configuration. So when you go into the project root element, you will see there is a configuration tab. And then the same you will find for the test cases, and the same you'll find for execution, and also for test case design, right. So all of these places you can create this test configuration parameters. And then these configuration parameters, some of them are defined by the system, which is Tosca, and others you can define on your own.

[03:09] You can create your own custom configuration values, which you want to use in your test cases. So now let's talk about what are these test configuration parameters, and what are the types of test configuration parameters which are available in Tosca, and how can you use them to create different parameters which can be used at different places in your test scripts. Now although there are a lot of test configuration parameters, and the whole list is available on the Tosca support documentation, but I have listed down some of the important ones which you might come across while you are doing script development.

[03:49] Now these are also divided across different engines like the X-Browser engine, the T-Box engine, and the mobile engine. And depending on which type of test cases you are creating, we will be using these parameters, right. So generally for web applications we will be using the X-Browser engine, and the most common type of parameter we will use is the browser parameter. Now this browser parameter has got some default browser values which you can use. So it has got a list of all the different values which can be used, right, from Chrome, Firefox, Edge, Internet Explorer, and the list keeps on increasing, right.

[04:30] So you can use any browser value in this particular parameter, and then your test will be made configurable because you can run it in any particular browser, right. So similarly you can also set the browser version, and then we have got two other parameters which are related to accessibility. So one is whether you want to run the accessibility analysis, and one is if you want to run it in the fast mode, right. So these are some of the parameters for the X-Browser engine. Then when we are using the T-Box modules, we will also use some of the parameters, and these are some of the parameters.

[05:11] So we have got the avoid execution recorder. Now this will help you to either enable or disable the recording for a particular test case, right. Then we have got different configuration parameters for the recovery engine. So we can set the values here for the on dialogue failure, on exception failure, or on verification failure, what you want Tosca to do, right. So you can set that configuration here.

[05:42] Then we have got the page sync parameter, not the speed sync parameter, it is basically used for different Ajax requests, right. So if you don't want to continue with test execution, then you can set this to true. Then we have got the scrolling behavior. So using this, you can tell Tosca whether you want to scroll a vertical or horizontal. We have got the synchronization timeout. Now you can set the timeout value for synchronizing your elements with Tosca.

[06:18] So it will have a default value, but then you can change this in your configuration parameter. Then we have got the target date format and similarly we have got target time format. So you can set a particular format which you want to use for your particular test, if you set that parameter value. Then we have got the test step retries. Now this will define how many times you want to retry a particular step, so that you can define in this particular parameter.

[06:48] Similarly, we have got the test case retries. These are all part of the recovery engine. Then we have got some parameters which are specific to the mobile engine, and this will be separately covered in the mobile sessions. But we have got the APM server. We can set the browser. We can set the device model, device name. We can also set whether we want to enable the live view. We can also set whether it's an APM or it's a simulator. So all these parameters can be used in your mobile engine test cases.

[07:25] So these are some of the different parameters. Now if you want to look at the whole list, you can get it in the documentation, which I'm going to provide the link to. Now let's look at a very simple example on how we can create a test configuration parameter and how it can be useful while creating your test cases for particular test scenarios. So let's create a test case here and let's call this parameters. So here I'm just picking up an example, this particular website.

[08:08] So what I'm going to do is I am going to add a test step here and then we'll say navigate or we'll say open URL. And then I'm going to enter the URL here. So it is going to open this particular website using this particular test case. OK, and then we want to enter the username and password, right? So let's go ahead and scan this quickly.

[08:43] OK, so here I just need the username, password and the login button. I've already checked all these three are unique, so I don't need to make any changes here. I'll just go ahead and save this and I'm going to close it. OK, so this is the module which you can see here. And now we can go and drag it here. We can add it to our test case. So this is our second step. And this is our login step, right?

[09:16] So here we can use the username. It's provided here. So we'll go back here and put it here and then password is here. So we'll again use the password and then for button we will use click. Now this test case works fine when you execute it any number of times. But in a scenario where you have to test multiple scenarios for this particular page, like we have to test with different usernames.

[09:50] Like we have to test with logged out user, problem user, performance error, visual, right? So there are seven different types of usernames here and every particular username has got a different functionality, which we need to verify through automation. So basically you need to run this test for seven different test scenarios, right? Or you need to run the seven times with different values. Now, one way is you can create different tests like you can create seven tests, which has got different usernames.

[10:26] But then you need to execute it separately and also you need to maintain them separately, right? So the creation or the development time is more and the maintenance time is also more. And to reduce this, we can use configuration parameters, right? So we can use the configuration parameter for username. Probably we don't need it for password because this is not changing, but we can still have it. And then for URL, if we want to test this particular test case in different environments, like if this is the test environment, we can have multiple test environments, right?

[11:04] So the URLs might be changing. URL is probably also test configuration parameter. So all of these are different examples of test configuration parameter. So instead of using static values in your test steps, you should be using parameters wherever you think that these values could change or you could run them with different values. So the other parameter which you can create is for a browser because you need to first launch a browser. After that, only you can open any particular URL.

[11:40] So the most important configuration parameter for your web test is that browser, right? So now let's look at how we can create a test configuration parameter at a test case level. It is almost the same at any particular level. OK, so you have to go into the test configuration tab from the details tab. And from here, we need to right click on the main test case. There you will find an option to create a test configuration parameter.

[12:11] So once you do this, you will see there is a drop down for the parameter. So you can choose the default parameters here, which are defined by Tosca, or you can choose your own or you can define your own parameter, right? So here I'm going to choose the browser parameter. And then once you choose that, you will see a drop down of values with all the different browsers, right? So I can choose any browser here. I will go with the Chrome browser. So that's one test configuration parameter, which we just defined for this particular test case. Similarly, we can create for username.

[12:47] So these are all the custom configuration parameters. These are not defined by Tosca, right? And then we can also use URL. And then we can also add for password. So these are the four different parameters, which I can create for this particular test case. Now, depending on the test steps, there could be a number of different parameters, right? So we need to just replace the values here for each of these parameters.

[13:22] So I can just copy it from here and I can actually put it here. And for password, I can take it right from here and then I can paste it here, right? So I can change the data type as well. So if you're using a password, you can change it to password data type so that it is hidden. And then you can just replace these actual values with a particular syntax.

[13:53] So in Tosca, we use configuration parameters. So we have to use this curly brace and then CP, which stands for configuration parameter. And then once you do that, it will populate all the parameters which are defined for this particular test case. So I can go ahead and use them now. OK. And then here, similarly, I can use the username.

[14:26] And for password, I can change the data type to string. And then I can use password. Now, what it also does is it not only makes your test configurable, but it also makes it more secure and also abstract. So now the test is abstracted for a particular user who is trying to look at this particular test steps and just trying to execute it because he'll be only able to see these configuration parameters, which are defined here, but not the actual values.

[15:09] Those values are here in the test configuration. Now, whenever these values change, you don't need to change them in the test case or test steps. So if these are used multiple times in a test step or test case, then all of these are referring to these parameters and we can change the values here. So it will be directly reflecting in your test steps. So consider if you have got 1000 test steps, which are using the same values, you don't need to change these values 1000 times.

[15:43] So it is saving a lot of time and effort in order to configure and maintain your test steps. Now, the other thing which you need to remember when you're working with test configuration parameter is you cannot delete any particular value if you want to. So there is no option to delete this. But if you want to just change or delete this particular value, you have to use this option reset to default value.

[16:13] OK, so once you do that, it will be removed from this particular list. So this is how you can create any test configuration parameter and you can also remove them or reset them if you don't want to use them. And then you can replace the values in your test steps with those test configuration parameters. Now, the other thing which you can do is also you can create configurations at a project level. So if you have got this particular project, which I've got the training project.

[16:46] Now, inside this, if I've got multiple projects which are using the same configurations, then I have got a different section called configurations. And this is where I can create project level configurations. So let's see how we can do that. So here I can create a new configuration. As you can see, there are some default ones like the API mobile test data service. So I can create my own configuration.

[17:18] So it helps you to structure your test configuration parameters from a specific point in your repository. So if you've got different teams with different requirements, then you can maintain them inside different configurations. So here either I can create a configuration folder or I can create a structure. I can even create a virtual folder or I can create simply a configuration. So if you want to create a configuration for a different project site, so like project A and then project B.

[17:54] So we can do that. So we can have two different configurations for two different projects. And then inside that, I can have my own parameters. So I can have a project which is using the browser Chrome. And then for project B, I can create a parameter called browser, but they are using Firefox. Similarly, I can create a list of different configurations here. So I can create something called synchronization timeout.

[18:28] So this could be different for different projects. So for one, I can set it three thousand and for other. Well, here I can create and then I can set it to six thousand because maybe the synchronization is much more for this particular application. So similarly, you can have these created at project level and then it can be defined for each of the projects.

[19:00] It can have the same configuration parameters, but the values are different. So these are basically used to structure your test configuration parameters from a specific point. And then if you've got a very diverse repository, which has got multiple teams and multiple requirements, then it is very easy to maintain your configurations at this project level. Now, how do you use these configurations? So for example, I am running this parameters test case.

[19:32] And I want to use a particular configuration for this particular test case. So what I can do is I can drag this project A configuration directly into this parameters. Now, when you see this, this project A configuration has now been inherited from here. OK, and it is using a specific set of configuration parameters like the browser, the synchronization timeout.

[20:03] Now, this could be different for different test cases. So you can pull your individual configuration from this configurations folder into your test cases or into your folders or into executions. Right. So this is how you can make this more configurable and easy to maintain for different projects. Now, the other thing which you can also do is if you are an admin and if you don't want the other team members to change this project level configurations, then you can set it to read only. Right. So if you go into any particular configuration like this project A, you go into the properties and then you have to just change this predefined value to true.

[20:48] OK, so once you do that, this will be read only configuration. It cannot be changed or it cannot be deleted. It can be inherited, but it cannot be modified. OK, so now once we have defined this predefined property to true, if we go ahead and use this in a particular test case. So if I pull this again into this particular test case, which is parameters, you will see that even if I go ahead and change this.

[21:22] Right. So here it is set to Chrome. And if I go into my test case, it is set to Firefox or Edge. I can change it here. OK, and I can maybe save it, but it's not going to change the original configuration. Right. So it will reflect it in my test case so I can modify it and I can run my test case. But it is not going to change it in the original configuration. Right. So that's the point of setting this predefined to true so that nobody can change the original configuration, which is set at a project level.

[21:59] Right. They can change their individual test case, but then it will only be applied in that particular test case, not in other test cases. So that way, the maintenance becomes easier because you can maintain it at one place and you can have your own structure. And then the changes across test cases will not reflect directly at this level. So this can be locked down to just admins and they can only manage these configurations, which are at a project level.

[22:31] So this is all about configurations. What are the different test configuration parameters which are available in Tosca? How you can create them, how you can use them, how you can create configurations at a project level, and then how you can maintain them across different projects or teams.
