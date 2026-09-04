---
id: "hJ395Eb3dng"
title: "Tricentis Tosca Tutorial Part-12: Tosca Api Testing and TOSCA Scan | Tosca Api Automation"
url: "https://www.youtube.com/watch?v=hJ395Eb3dng"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 12
duration: 515
upload_date: "20211013"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:16:24Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-12: Tosca Api Testing and TOSCA Scan | Tosca Api Automation

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the overview of API testing, purposes, and API scanning using Tosca.

[00:47] The explanation will be done through hands-on demonstration. API is the shorter form of application program interface. It's working as an interface which allows two applications to communicate with each other through common message formats such as, XML, JSON, etc. Let's consider this figure to understand more on API. Assume, we have four different applications, SAP, mobile apps, web portal, and billing system which are integrated by common interface as API.

[01:25] Here API is working as an interpreter. Each of the system interacting with each other by sending an API request and receiving the API response. Basically, each system is communicating with API and, based on the request, API routes the messages to the target system. The goal of API testing is to ensure that the core functionalities of the application work is expected without interacting in the UI layer.

[01:57] To perform the API testing, always, we need to take help from any third party tools like Postman, UFT, Tosca, etc. Nowadays, Tosca is one of the best automation tools for API testing. The main purposes or benefits API testing in Tosca are such as, API testing can be used to validate the core functionalities even when the UI hasn't been developed slash modified.

[02:27] Hence testing can be initiated much before actual functional testing, UI-based, is done. Frequent application changes can be tested quickly. It is easy to create and maintain test cases in Tosca. The API testing in Tosca can be done much faster. Standalone Tosca API scanning wizard is available to scan the API in the simplest way.

[03:00] Process flow overview of API testing in Tosca as explained through this diagram. Here API services are used to identify the API details and functional flow for automation. API scan wizard is used to scan the API and create Tosca modules. Create test case step, generate the test cases and perform cleanup with parameterization. Run is to execute the test cases and share the reports to stack holders.

[03:36] All right. Now we will learn how to scan API, create basic test cases and run through the API scan wizard. We will demonstrate the steps using the sample Tosca API. HTTP colon slash slash web service dot Tosca cloud dot com slash rest slash swagger slash doc slash V2. First, we will move to the API testing tab.

[04:08] Here, all the API test automation related options are available. We can open the API scan wizard by opting the start API scan option. It will take few seconds to appear the API scan wizard. Now clearing the default folder structure.

[04:40] Two options for API scanning is available in the left top corner of the wizard. One is for file scanning, i.e. if we have the JSON file which contains the API details. We are going to use another option to scan the API URL. We will select or enter the API endpoint address of sample swagger application. The advanced options such as authentication, proxy can be configured here which are not required for our case.

[05:15] Clicking on OK button to start scanning. The API scan components are appeared in left navigation section. The components are grouped based on the functional modules such as auth, coffees, employee etc. The auth modules contains the API related to authentication of the application. The payload tab of request contains request data like user and password. Click on run to receive the response of this API request for authentication.

[05:49] It returns the token and the expires time stamp. The token can be used for any other transactions. Now we will check another scanned API to retrieve all the coffee information. Move to folder coffee n. Select get coffee's components. Here payload of request should be empty as no input data is required.

[06:20] Perms tab, we will provide the token number which was received during the authentication. Run to receive the responses of this API. After successful API call, the status code should be returned as 200 and the entire coffee list will be available in JSON format. Similarly, we can create coffee using post post coffee API. Here we need to provide description, ID and name in payload section of request. The other can be used to delete a coffee or search a specific coffee.

[06:55] In each of the cases, the ID is the mandatory field in payload section. So we can get a picture that the API can be called with data and the response can be viewed from API scan wizard. But here the main problem is that this components cannot be handled as a Tosca test cases, data cannot be parameterized or verification cannot be performed. It can be used for manual testing similar to postman tool.

[07:30] So for API test automation, we need to move this components in the test case section. In the next video, we will create the Tosca API test case. That's all about API scan. Thanks for watching this video. That's all about API scanning using Tosca. We will learn more about API test automation approach in next video. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain.

[08:08] You can check our other website as well. We have features like YouTube trends, Twitter trends, scientific calculator and many more other tools. If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
