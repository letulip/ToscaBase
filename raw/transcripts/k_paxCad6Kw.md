---
id: "k_paxCad6Kw"
title: "Tricentis Tosca Tutorial Part-7: Tosca Parameters,Tosca Configuration Parameter"
url: "https://www.youtube.com/watch?v=k_paxCad6Kw"
channel: "LambdaGeeks"
playlist: null
playlist_index: null
duration: 353
upload_date: "20210915"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T07:41:46Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-7: Tosca Parameters,Tosca Configuration Parameter

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the overview and different approaches of Tosca parameters.

[00:45] Also, explain the approach of test configuration parameters. The explanation will be done through demonstration. The test case which was developed in last tutorial, we have provided the test data directly as a hard-coded value. The main disadvantage of this approach is whenever we need to change the data, we need to update the test case. So, to avoid this, we need to go for parameterization.

[01:17] Tosca allows different approaches to perform parameterization. The basic approaches are. Buffer which is similar to variables which holds values during the execution. Test configuration parameters. This is another way to parameterize the test data. The test configuration parameters can be created in TestCase, Folder or ExecutionList level. Business parameters which are used to parameterize the reusable test step blocks.

[01:50] We will discuss about this while creating libraries in Tosca. Apart from this, Tosca also provide advanced features such as test case design, test data management, test data services, etc. to handle complex test data. Now I will explain the concepts of test configuration parameter in short TCP. The TCP can be created in TestCase, Folder or ExecutionList level.

[02:20] If the test configuration parameters are defined in parent folder level, same parameter values can be retrieved from sub-folder and all the test cases available under that parent folder. The test configuration parameters are read-only during execution. So, it has to be defined before the execution. The syntax to read TCP parameter is the CP parameter name. The TCPs are visible in the test configuration section of every test case, folder or execution list.

[02:58] Ideally, we should use the test configuration parameters for the common or configuration related data which are applicable for throughout the test suites. The examples of the TCP are application path or URL, credential, environment details, reporting path, etc. Tosca provides default test configuration parameters as well that are used to customize test configurations. For an example, if we want to execute the test case in the Chrome browser, we need to add TCP as browser with value Chrome.

[03:34] Now we will create test configuration parameter in TestCase level. Select the test case and click on test configuration tab. Right-click on test name and click on option create test configuration in violet colored button. Provide a proper name to the newly created parameter. We use the name as MyTCP. Now we can assign any value to this new test configuration parameter. We will assign the value of this TCP to the existing test step for creation of buffer.

[04:10] We use the syntax, CP, MyTCP, as the buffer value. During the execution, the value of TCP 12345 will be assigned to buffer MyBuffer1. Execute the test case in Scratchbook to check the TCP parameter value assignment. Scratchbook log shows that TCP value assigned to buffer correctly. The new value of buffer MyBuffer1 can be checked from buffer viewer as well.

[04:44] Similarly, we can create the TCP in folder level and execution list level as well. If we create it in folder level, then the TCP can be accessed from all the test cases which are created under same folder. Thanks for watching this video. That's all about Tosca parameters and test configuration parameter. We will learn more about Tosca library, reusable test step block and business parameters to manage test data in next video.

[05:17] Please visit our website Landageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools. If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
