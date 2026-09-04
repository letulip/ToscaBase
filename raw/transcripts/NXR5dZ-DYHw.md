---
id: "NXR5dZ-DYHw"
title: "Tricentis Tosca Tutorial Part-13: Advance Tosca Api Testing And Tosca API Test Case"
url: "https://www.youtube.com/watch?v=NXR5dZ-DYHw"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 13
duration: 785
upload_date: "20211031"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:22:27Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-13: Advance Tosca Api Testing And Tosca API Test Case

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the creation of Tosca API Test Cases. Create a parameterization, verification, and execution of Tosca API Test Cases.

[00:51] The explanation will be done through hands-on demonstration. Alright. Let's start with the API test case creation. Two options are available to create the API test cases. First, we can choose the export to API test case option to create modules and basic test cases from the API Scan Wizard. The second approach is to create the test cases using the modules which are created during the export.

[01:28] Now I will guide you to create the test cases by opting the export API test case option. Select the root folder and click on export option under API test case option to generate test cases and modules. Oops, this error appeared as I forgot to check out the Tosca workspace. Let me please check out the project folder first and do the same step again.

[02:00] Once the process done, close the API Scan Wizard. Now, we can see that modules and test cases sections are created in new component folder with the name API Scan underscore import. The modules section contains all the modules which are created during the scanning. The modules are available within the respective functionality wise created folders. For each of API, two modules are created.

[02:33] One for request and another for response. We can use these modules later to create the test cases. Now, let's see the test case section which contains the basic test cases for each of the APIs which are scanned previously. Each of the test case has two steps. One for sending the request and another for receiving the responses.

[03:03] These are the default test cases which are generated based on structured in API Scan Wizard. Now, I will guide you to create the test cases with the help of API modules which are created during the export. This is similar approach to create Tosca test cases for any UI application. Here we will perform a sample test scenarios for Swagger application.

[03:39] The steps are, 1, authenticate using valid user credential, 2, add coffee item, 3, search and verify the new coffee item. Let's start the demonstration now. As per the test scenario, we will use request and response modules related to authentication and coffees. The input data of default API modules are hard coded. So, first we need to create the modules attributes to make it parameterized.

[04:12] We will click on, buffer module attributes with dynamic list items, option to open attribute assistant. Select password and username attributes and click on add to create attributes. Two module attributes are created for username and password. Similarly, we will create attributes for post post login data response module for the response field status code and token. Next, we will create the attributes for module post PUST coffee request.

[04:44] The attributes need to be created for name, description and authorization field. From the attribute assistant screen, we will select the corresponding fields and click on add. We need to create attributes for post post coffee response module for the response field status code and ID of newly created coffee item. The other respond fields are not required.

[05:18] Next, we need to create attributes for modules to find the coffee using the coffee it. Here, we will create attributes for the authorization and ID field for the get GT coffee by ID request module. Finally, we will now create attributes for get GT coffee by ID response module for the response field status code and name. This name attribute will be used for verification.

[05:52] All the required modules are now parameterized. Post PUST login data request has two required attributes. Post PUST login data response has attributes. Similarly, the attributes are also created for other required modules. All right, we will now create the test case using these modules. We will first navigate to test cases section and create a new test case with name add coffee.

[06:36] Next, we will create three test step folders with the name authentication. Post coffee and verify new coffee. Next we need to pull the required modules.

[07:07] First, we will drag and drop login data request and response modules to the test step folder authentication. Next, we will drag and drop post coffee request and response modules to the test step folder post coffee. Finally, we will drag and drop GT coffee by ID request and response modules to the test step folder verify new coffee.

[07:46] We need to update the test step with data and action. In post login data request step, we will provide the valid password and username to generate the session authorization token. This token will be used to perform any transaction such as add coffee or search by coffee ID. For post login data response step, we verify the success code 200 OK for status code attribute to check the authentication.

[08:19] Then we will store the token number in off token buffer that will be used later. Now we will enter the new coffee details to the step post coffee request. Enter name as test one. Enter the value of description attribute as test coffee. Enter value of authorization attribute as token space off token buffer.

[08:52] Now we will check if the coffee successfully created or not. So we need to perform verification against the status code attribute for post coffee response step and store the value of ID in a buffer. Next step is to find the newly created coffee. To perform this, we will update the ID attribute of the GT coffee by ID request step with the ID buffer, which holds the ID of newly created coffee item.

[09:33] Also, the authorization attribute has to be updated accordingly. Now we have to perform the final verification in step get coffee by ID response. First perform verification for status code attribute with success code 200 OK. After that, we will verify the name which was provided during the coffee creation. The API test case is created and ready for execution.

[10:08] It looks like this. This test case can be executed through the scratch book by selecting run in scratch book option. Here we will execute it through the execution list. First check out the execution section.

[10:39] Create execution list folder with name API suite and create a execution list with name swagger app. We will drag and drop the newly created API test case add coffee into the execution list swagger app. Now execute this execution list by selecting the run option after right clicking on it.

[11:09] It will take few seconds to complete the execution. No UI will be appeared during execution as it will be done through API interface. We can now view the execution logs to check the status of all API transactions. All the buffer are created successfully.

[11:40] Also, we can view the final verification of coffee creation has been done successfully. The buffers which are created during the execution can be seen from buffer viewer section. Save and check in the workspace to store the test case in repository.

[12:15] Thanks for watching this video. That's all about API scanning using Tosca. We will learn more about API test automation approach in next video. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube trends, Twitter trends, scientific calculator and many more other tools.

[12:55] If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
