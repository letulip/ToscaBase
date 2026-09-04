---
id: "5kWTxvxcfXQ"
title: "Tricentis Tosca Tutorial Part-8: Tosca Business Parameters,Tosca Library,Reusable TestStepBlocks"
url: "https://www.youtube.com/watch?v=5kWTxvxcfXQ"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 8
duration: 380
upload_date: "20210919"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:02:07Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-8: Tosca Business Parameters,Tosca Library,Reusable TestStepBlocks

[00:05] Hello friends. Welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well.

[00:36] Let's start our today's session. Through this video, I will explain the overview of Tosca library, concept of reusable test step block, and business parameters. The explanation of reusable test step block creation will be done through demonstration. To understand the Tosca library completely, we need to understand few more related concepts in Tosca. Such as, test step block is a grouping of test steps to perform a specific task such as login, logout, create record, etc.

[01:15] The test step block can be created using the test case level folder. It helps to increase the readability and reduces the efforts for maintenance. Library is acted as a container of reusable test step blocks. The library can be created within any folder available in test case section. But, more than one library cannot be created within single folder. The icon of the library is similar to test case folder with symbol, L.

[01:49] Reusable test step block when we define a test step block within the library section, it's acted as reusable test step block. We can create it in two ways. Such as either, new reusable test step block creation in library or convert existing test step block by drag and dropping any existing test step block into library. Business parameter, it's an approach to pass test data into the reusable test step block through this parameter.

[02:20] With the help of business parameters, we can use the reusable test step block for a different set of test data. Now, I will show how to create the library reusable test step blocks with business parameters in an existing automated test case. We will create the reusable test step block with the test case which was created previously. First, we will select and check out the the parent folder for modification.

[02:52] Create the library component by clicking on create test step library icon with L symbol after right clicking on the parent folder. Now right click on library folder and create reusable test step block with a logical name. We are providing name as Google search as we are going to create reusable test step block for Google search functionality. We will add two test steps by dragging from test case for searching text in Google and wait for search result.

[03:23] We can place this reusable test step block in the test case by drag and drop method. The next step is to create the business parameter to pass the test data. In order to do that, first business parameters component to be added. Then we can create the parameter as search text to pass the search text from test case to reusable. Assign this newly created search text parameter to the test step in reusable test step block by drag drop to replace the hard coded test data.

[04:01] So, the creation of reusable test step block with business parameter is now completed. Go to the test case and pass the search text tricentistoska in the reference of reusable block. Now, we will see how to parameterize the test data using the test case configuration parameter and pass it as business parameter value. First, go to the test configuration section and create a test configuration parameter as search text.

[04:37] After that assign the value as tricentistoska to this parameter. Now go to test case details section and select the reference component of reusable test step block. Replace the hard coded value which was passed to reusable component with the newly created test configuration parameter search text.

[05:13] Similarly, we can create multiple test configuration parameters in a test case based based on the requirement. Thanks for watching this video. That's all about Tosca library, reusable test step block and business parameters to manage test data. We will learn more about Tosca buffers in next video.

[05:44] Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube trends, Twitter trends, scientific calculator and many more other tools. If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
