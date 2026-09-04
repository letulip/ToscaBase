---
id: "mFptsa3Wuts"
title: "Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper"
url: "https://www.youtube.com/watch?v=mFptsa3Wuts"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 6
duration: 516
upload_date: "20210904"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T08:57:56Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper

[00:15] Hello friends, Welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the different approaches of Tosca automated test execution. Also, I will explain the steps to enable and generates the document through DokuSnapper.

[00:51] Test execution is a process to verify the application functionality based on the test cases. The test execution can be done manually or through automated approach. In this video, I will guide you to perform automation test execution in Tosca. Tosca allows you to execute the test cases in two ways. Execute test cases in Scratchbook and Execute test cases from execution list.

[01:22] Tricentis advises using the Scratchbook for a dry run which means to to check the test case readiness. The Scratchbook execution results will not be available for future reference. We also could perform the execution of individual test steps. Let's see the execution from Scratchbook. We need to right click on the selected test case and select option run in Scratchbook to initiate the execution from Scratchbook.

[01:52] No need to check out the test case or containing folder for Scratchbook execution. The automated script will perform Google search and validate the Tricentis logo after opening the Tricentis official portal. The temporary execution logs will be appear in the screen which contains the logs for each of the steps including verifications. A green tick mark will be shown in each log step for success condition.

[02:23] In case of failure a red cross mark will be appeared. The execution segment provides a feature of selecting and preparing multiple test cases for execution. Execution performed in execution list will be available for future references. First, we need to understand the approach to create execution list. And enablement of docusnapper before initiation of execution. The enablement of docusnapper is an optional step which allows Tosca to create a detailed execution documents for each of the test case.

[03:01] The docusnapper contains the logs and the images of each step. Let's start with execution list creation step. The execution logs are kept permanently in execution list. It has to be created in execution section. First, we need to dock the execution section in Tosca commander for better visibility. The default and previously created lists are displayed here.

[03:35] Now, we will check out the route to create it our own execution list. The execution list cannot be created directly. First, execution list folder has to be created in the execution section. It can be done by selecting the create execution list folder icon after right clicking on checked out folder. We can change the list folder name accordingly. Now, we can create the execution list after right clicking on newly created execution list folder.

[04:10] Entering the name as sample execution list. The next step is to add the test case to the execution list. We can add the test cases into the execution list from the test cases section by the drag drop method. We will add the test case which was created previously. The multiple test cases can also be added in this way. The test configuration section contains the parameters which are defined during test case development. Any changes from here will be applicable to this list only.

[04:44] Initially, no logs are available here. By clicking on check-in button, we can save the same in the shared repository. Now, I will show how to enable to docusnapper to allow Tosca to create documents during the execution. Click on project tab which is available in Tosca commander header section and click on settings. The Tosca setting wizard will be appeared. Select the navigation engine and docusnapper which are available under settings in left section of the wizard.

[05:20] Now select the option docusnapper. We need to change the value of setting option enable snapper to yes. The different docusnapper configuration options including document paths can be customized from here. Now close wizard to enable the docusnapper. Now, I will show how to trigger the execution from Tosca execution list and view the document generated through docusnapper during execution. To execute the test case from execution list first, we need to check out the execution list.

[05:59] Now, we will be able to initiate the execution by clicking on run option after right-clicking on the selected test case. Multiple test cases or the entire suite can be selected for execution. The automated script will perform the defined test steps including Google search. Opening the Tricentus official portal from the search result displayed in the Google page and validate the Tricentus logo.

[06:31] After completion of execution, the execution logs will be available in the execution list which contains the logs for each of the steps including verifications. A green tick mark will be shown in each log step for success condition. In case of failure a red cross mark will be appeared, now perform the check in action to store the result permanently in the shared repository. The docusnapper generated report can be viewed from the path app data.

[07:03] Tricentus Tosca test suite 7.0.0 Docusnapper The report should be available as per the test case name. It will contains the execution logs and the screen shot for each of the test steps. This document will be very helpful for proofing the test executions. If the execution performed through scratchbook, the report name will be start with text scratchbook.

[07:42] Thanks for watching this video. That's all about Tosca automated test execution approaches. We will learn more about data parameterization and creation Tosca reusable test step block through library in next Tosca tutorial. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools.

[08:26] If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
