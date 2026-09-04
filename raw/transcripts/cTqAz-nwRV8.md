---
id: "cTqAz-nwRV8"
title: "Tricentis Tosca Tutorial Part-9 : Tosca Buffer"
url: "https://www.youtube.com/watch?v=cTqAz-nwRV8"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 9
duration: 415
upload_date: "20210922"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:04:59Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-9 : Tosca Buffer

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the overview of Tosca buffers and standard modules which are used to manage buffers.

[00:49] The explanation of usage of Tosca buffers will be done through demonstration. Buffer is acted like variables to store the values during execution. The stored values are also available after completion of execution. The scope of buffer is restricted to the local workspace only as the buffer value cannot be updated to shared repository. The syntax of buffer to read the value is, b, buffer underscore name. Buffer can be created by using action mode as buffer for any test step where buffer name should be the test step value instead of using set buffer module.

[01:27] Also, using xb, buffer underscore name, buffer can be created from a verification test step dynamical. Tosca provides four standard modules to works with buffers which are available under the path standard modules, buffer operations in modules section. The standard modules are T box set buffer. This module is used to create the buffer as per the name provided in the attribute section. The value provided in the attributes value section will be stored in the buffer.

[02:00] We can create more than one buffers using this module. T box name to buffer, this module is used to store the test case name into the buffer for which name is provided in the attribute value field. We need to execute the test case from the execution list to store the test case name. Otherwise, it will store as scratch book. T box partial buffer, this module is used to extract the partial text and store it to another buffer.

[02:33] T box delete buffer, it's used to delete the existing buffers. The buffer name should be mentioned in the attributes value section. I will now show how to work with buffers. We will start with box set buffer to create and assign values. First we will go to the buffer operation folder in module section. All the standards modules which are related to buffers are listed here.

[03:04] Now selecting T box set buffer module and drag and drop it to the test case. Inside the name of buffer as mybuffer1 by renaming the test step attribute. We can enter any text in value column of the test step to assign it to the buffer. Now we will execute this step in scratch book to create the buffer as mybuffer1 and assign value as abcde. The temporary execution log shows the creation of buffer with value assignment.

[03:38] It can viewed from buffer viewer wizard. Now we will understand the module T box name to buffer. First, we will drag and drop it to our test case. Entering the buffer name in value column which will be assigned the test case name. Let's use the buffer mybuffer1 which was just created. We will execute this step in scratch book to store test case name into buffer mybuffer1. In this case text scratch book will be assigned as it was executed from scratch book.

[04:12] We need to execute an execution list to assign the actual test name. Next, we will see the usage of the module T box partial buffer. We will drag and drop it to our test case. We need to provide values for four attributes. The buffer which will be assigned the extracted text has to be provided in buffer attribute. We are providing mybuffer2. The value attribute should be the source from which we are going to extract partial texts.

[04:46] We can use the previously created buffer mybuffer1 as the source of string which contains abcde. The syntax to use the existing buffer as the input value is, b, mybuffer1. Start denotes the start position and end denotes the end position of the text to be extracted. We will execute the test in scratch book to store the extracted values to buffer mybuffer2. Here extracted text should be bcd which is starting from second to fourth position of the source value abcde.

[05:22] We can check it from buffer viewer. Here the last attribute is used alone to extract the text from the end of source value. Now, we will drag and drop the last module T box delete buffer to remove any existing buffer. Entering the existing buffer mybuffer2 in value column. We will execute this step in scratch book to delete the existing mybuffer2 from the workspace. The the log scratch book shows that the buffer is deleted successfully.

[05:58] If we see the buffer viewer, the buffer name mybuffer2 is not available now. Thanks for watching this video. That's all about Tosca buffers and its usage. We will learn more about Tosca test case design features to manage test data in next video. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well.

[06:32] We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools. If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
