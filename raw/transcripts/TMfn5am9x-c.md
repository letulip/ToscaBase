---
id: "TMfn5am9x-c"
title: "Tricentis Tosca Tutorial Part-5 : Tosca Test Case, Tosca Test Case Design and Best Practices"
url: "https://www.youtube.com/watch?v=TMfn5am9x-c"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 5
duration: 738
upload_date: "20210829"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T08:54:50Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-5 : Tosca Test Case, Tosca Test Case Design and Best Practices

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the overview of Tosca TestCase. Also, I will guide to develop the test cases with the help of modules which are created during the last tutorial.

[00:53] TestCase is a set of instructions to ensure the quality of the software product. In other word, it is a combination of steps to walk through the application with verification. The test cases are written based on the software requirements. It can be designed for manual or automated testing. Here, we are going to discuss about test cases that are automated by Tosca. The Tosca test cases are created by using the both standard and user-defined modules with required test data.

[01:27] Two types of test cases are available in Tosca. Technical Test Cases. And Business Test Cases. The technical test case keeps all the technical information to steer the controls during execution. It can be created by right-clicking on any folder which are available in test case section and selecting the blue-colored circular arrow icon. The shortcut key for new test case creation are CTRL plus N and CTRL plus T.

[01:59] It is a collection of test steps which are created by the drag and dropping of modules. Test steps has different action modes such as. The input action mode is used while entering data, perform click operations. The insert action mode is used for insert purpose. The verify action mode is required to select this option during verification. In the value field, we need to provide the condition.

[02:31] The buffer action mode is used to set the value to buffer. The Walton action mode is used for synchronization purposes to wait until the condition is satisfied. The select action mode is used while hierarchy levels are available and need to work on child items. The constraint action mode is used for checking for a particular value, mostly used in the tables column. The test cases has three status.

[03:05] Planning. In-work and. Completed. The business test cases are the logical groups of technical test cases. Each of the business test case represents the functionality coverage which is designed based on the requirements. The business test cases are not executable. Only, we can monitor the testing coverage through this. Alright. Let's start the test case development process in Tosca.

[03:36] We will automate a simple scenario on Google search to understand the test automation development. The scenario involved with steps such as. Launch Google in Chrome browser. Search text Tricentus Tosca in Google. Click on first search result to open official portal. And verify that Tricentus official page has appeared. The required custom modules are already created with the reference of last video on Tosca modules.

[04:12] Alright. Let's start the test case creation process. Three user defined modules are already created for Google search screen, search results and the Tricentus Tosca official portal. We had added only the required controls during the module creation. Now, we will move to the project hierarchy and dock the component test cases as tabs.

[04:44] As we are working with the shared repository. First, we need to check out the test cases section. After that we need to create the folder structure. The proper folder structure creation is an optional task, but it's in best practice. We can logically segregate the test cases using folder. Now we will create new test case by right clicking on the new folder and provide a logical name.

[05:19] The technical test case is created now. It's an empty test case, which means no test steps are available. Our next task is to add test step by referring the modules based on the activity. Because our first step is launching the application, so we need to use the standard modules which is available under T-Box Automation Tools, Process Automation. We need to drag and drop this modules to the test case.

[05:56] This module help to launch any application. But Tosca provides a specific modules to launch any web browser with URL. So we delete this one and use the standard module open URL to launch web application. The standard module open URL is available under Module Folders, T-Box Engines, HTML. We need to drag and drop this module to the test case.

[06:31] We will now enter the URL as www.google.com and select the action mode as input. It's advisable to rename the test step logically as per the activity to be performed. The first test step is ready now. As per this step, the Google search will appear. Now, we will look for the second step. Here, we need to search the text Trisentis Tosca in Google.

[07:06] We will now add our first custom module. The custom module Google search screen will be used to create test step to perform Google search. Name the test step accordingly. Here we will use the WaitOn as action mode for the control Google icon to handle synchronization. We will check the Exist property as true for Wytton.

[07:42] Set the string value as Trisentis Tosca for the field QSearchText with action mode input. This step will enter the search text in Google search field. Now click operation has to be added as value for the control Google search button. Then the action mode should be input. This step will perform the click operation. The second test step is completed.

[08:13] It will enter the search text into Google and click on the search button. The next step is to click on the first result option to open the Trisentis official portal. Sometime Google search is not first enough due to the network condition. So it's a good practice to add a pause here. For this purpose, we will add the standard module Wait to perform the pause. We will configure the wait time as 5 seconds by entering value as 5000 as it allows milliseconds.

[08:54] Now we will add another custom module to perform the click operation on the first search result screen. Rename the step as per the activity. Then add the click operation to the link control. This operation will click on this link from Google search result.

[09:27] Here we need to add the final verification step to validate the Trisentis official portal. We will now drag another custom module into this test case. This module will be used to verify the logo of official Trisentis portal. Rename this step to verify Tosca official portal. Here we need to select the action mode as verify to perform the verification operation.

[10:00] The verification will be done based on the exist property value as true. See all the steps are created. Now we need to close the browser. To perform close operation, we will use the standard module close browser. The title of close browser standard modules refer the title of the web browser to be closed.

[10:31] We will use the string as Trisentis Tosca asterisk as the title of the test browser. Here asterisk denotes any string after the keyword Trisentis Tosca. The test case is ready now. By default, Tosca works with the Internet Explorer. But we are working with Chrome browser here. So, we will add one test configuration parameter as browser. The value for this parameter should be selected as Chrome.

[11:10] The test case is now completely developed and ready to execute. We will understand the process for test execution in next video. Also, we will discuss on usage of libraries and parameterization in upcoming videos. Thanks for watching this video. That's all about Tosca test case creation. We will learn more about Tosca data parameterization in next Tosca tutorial.

[11:42] Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools. If you like our video, please like, comment and share.

[12:12] If you have any questions, please comment and we will resolve your query.
