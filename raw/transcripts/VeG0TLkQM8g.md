---
id: "VeG0TLkQM8g"
title: "Tricentis Tosca Tutorial Part-10 : Tosca Test Case Design, Tosca Class"
url: "https://www.youtube.com/watch?v=VeG0TLkQM8g"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 10
duration: 797
upload_date: "20210924"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:09:22Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-10 : Tosca Test Case Design, Tosca Class

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the detailed overview and implementation approaches of Tosca TestCase design.

[00:47] The explanation will be done through hands-on demonstration at the previously developed TestCase. Tosca TestCase design is an approach to isolate the test data from the technical sections of test cases. So, the data and test cases are kept separately. In short, it is also known as TCD. The Tosca TestCase design section has the capability to break our test cases into a logical structure. It is also help us to plan and design the test cases in an efficient and structured way to reduce the development and maintenance efforts.

[01:25] The primary activities of TCD are. Create the test sheets, which is a combination of all possible test cases for any particular scenario or template. Basically, test sheets are holding the data for different combinations. The concept of class-in-test-case design approach helps to reuse the common data across the test cases which reduce the efforts of data management. With the help of instances, we can create the specific data for test sheets, TCD attributes or TCD classes.

[02:02] Create test case templates and assign the test sheets. We need to instantiate or reinstantiate templates to generate the instance test cases as per the test sheets. It manages test data in test sheets and execute the instance test cases. Before starting of TCD implementation, we need to familiar with some TCD objects which are mostly used in TCD. I am explaining them one by one. Folder Test case design folder is used to group the test sheets or classes in a logical way.

[02:41] Test sheet. Is a list of data for all possible combinations of TOSCA test cases. Each data set represents one unique test case. Attribute Is referred to as the different data parameters corresponding to each application field. Attribute which are not business relevant. Are used for comment or description purposes. The result attribute. Is used for result purposes.

[03:13] Instances collection. Holds the instances i.e. all possible values available for particular attribute. Instances Is the value of each attribute slash parameter. It can be created test sheets, attributes or class level. Instances of test sheets are basically a test case name. Class This is similar to test sheets but it's used for the reusable purpose. All the common data are stored here which can be reused in multiple test sheets.

[03:50] Class reference. Is acting as a link of classes from test sheets. We can create it with the drag drop method. The object hierarchies in test case design are. A test sheet may have attributes, instances, test steps and class references. A class may be the combinations of class attributes and instances. Again, an attribute can keeps further attributes and instances.

[04:21] A step can keeps more steps and attributes. Advantages of TCD approach are. Handling of dynamic test data and objects are very easy. It helps to reuse of data in different test cases. No scripting is required to implement TCD. Data and technical components are kept separately. In the case of data change, no need to modify the test cases.

[04:54] The main disadvantages of TCD is that the test case design section are. Thus approach is very complicated and little expensive. Also, the UI takes time to understand. Alright. Let's start the demonstration on test case design. I will guide you the step by step approaches to implement TCD in an existing test case. First, we need to create the test data sheet in test case design section.

[05:29] We will implement TCD in this test case which was developed previously. Now we open the test case design section as a floating window on top of test case section. Check out the TCD section. To create the data sheet, we need to right click on the TCD folder. We rename it to data set one. Now we will create the attribute of the data sheet as the test data parameter such as URL.

[06:01] After that, we need to create the instances of URL attribute which will be treated as test data. We are adding two URLs for Google as values. Similarly, we will add another attribute as search value which will represent the data parameter to store values of Google search text.

[06:32] And created two instances as test data. Next, we need to create the instances of data sheet. This instances will be represented as the test case name later.

[07:04] Here, we create two instances test case underscore zero one and test case underscore zero two. After creation of data sheet instances, we need to assign assign attribute values for each of the instances. We can do it from details section. We will select the values from attribute drop down. For two instances, we will select different set of data which are defined during attribute creation. The test data sheet is now created successfully.

[07:41] Now I will demonstrate the approach to create a template test case and assign the data sheet. First, go to the corresponding test case and perform checkout operation to make it editable. Right click on the test case and select the option convert to template to make two as template test case. Now, drag the data sheet data set one and drop it to the template test case after the data sheet assignment.

[08:19] Same can be viewed from the property section against the property name as schema path. Now, we will assign or replace the data parameter in the template test case by dragging the attribute from the test data sheet into the value field of the test case. Instead of drag drop method, we can directly type the syntax in the value field. We will replace all the hard coded value from the test case. The data sheet assignment is now completed.

[08:51] Next, we will generate the instance test cases by right clicking on the template test case and selecting the create template instance option. After confirming the process, it will take few seconds to generate the instance test cases with the data defined in TCD. Here, two test cases will be created as per the definition in the data sheet instances. We can also see that the data will be updated as per the data provided in our data set one data sheet.

[09:23] The implementation test case design is now completed. We will now execute the instance test case from execution list to ensure the correctness of the implementation. Dock or close the test case design section and go to execution section. Create a new execution list with name TCD. We can assign any name here. Now we need to drag and drop the newly generated instance test cases here.

[09:55] We can execute entire execution list. But to save time, we are selecting first test case and run it. The automated script will perform the defined test steps, including Google search, opening the official portal from the search result displayed in the Google page and validate the logo.

[10:25] After completion of execution, the execution logs will be available in the execution list, which contains the logs for each of the steps, including verifications. The implementation test case design is now completed. I will show how to create class in TCD to reuse data in multiple data sheets. First, navigate to test case design section. To create class, right click on any desire folder and then click on create class option available in menu with icon C.

[11:00] We can rename it. We will now follow the same approach to create the class instances and the attributes which was used during data sheet creation. Here we will create two class instances, set one and set two. Also, we will create one attribute as data parameter, which represents the URL. Two instances as the value of this attribute will be created.

[11:45] Now we need to assign assign attribute values for each of the instances of the class. It can be done from the details section by selecting the value from attributes drop down. We will now assign this class to data sheet by drag and drop it to data sheet. Now we will select the corresponding instance, which represents the data set from the class reference. By selecting this, the corresponding URL will be assigned to the test data sheet.

[12:18] The same class can be assigned to multiple data sheets to reuse the data. We can now assign this attributes of class reference to the template test case as the data sheet attributes. Thanks for watching this video. That's all about Tosca test case design. We will learn more about Tosca features in next video. If you have any questions, please comment and we will resolve your query.
