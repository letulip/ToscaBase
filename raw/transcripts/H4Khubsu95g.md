---
id: "H4Khubsu95g"
title: "Tricentis Tosca Tutorial Part-11: Tosca Action Modes-Input,Verify,Constraint, Dynamic Buffer"
url: "https://www.youtube.com/watch?v=H4Khubsu95g"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 11
duration: 665
upload_date: "20211001"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:12:55Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-11: Tosca Action Modes-Input,Verify,Constraint, Dynamic Buffer

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the usage of frequently used basic Tosca automation action modes such as Input, Verify, Dynamic Buffer, Constraint, etc.

[00:51] The explanation will be done through hands-on demonstration. Here, we will understand the basic automation steps such as handling of text box, drop downs, radio options, click operations, etc. First, we need to scan the web page to create the module. We will select the desire application window during the application selection and proceed.

[01:27] We will add all the controls including drop downs, text fields, radio option, button, etc. from the web page using select on screen option from the scan wizard. We will now check and verify that the controls are identified uniquely through the default properties. After that we need to save to create the module and close the scan window. The module is created successfully with the required controls.

[02:10] Next we will understand the approaches to perform basic automation activities. First, we will navigate to test case section and create a new sample test case in. Then we will drag and drop the newly created module into this test case. For data entry, we need to provide the test data in test step value column and select the input action mode.

[02:44] The options for any drop down columns are available in step attributes value which are loaded during scanning. We can select the required option from here. By default, this action mode is auto-populated as input for any input or clickable controls. For any text field, we need to enter the data in the value attribute. Similarly, we will provide the input data for rest of the input fields.

[03:29] To perform click operation in button, next, we will provide the keyword click with curly brackets or we will use capital X in value with input action mode. The first option will perform the mouse movements. Now, the test step is completed. Now we will execute the step in scratch book to perform the data population in the application and click on next button through automation. It will take few seconds to complete the execution of this step.

[04:06] It's all about the data entry and click operation. Now, we will understand the action mode verify by performing verification of first name field. Also, we will create a dynamic buffer to store version number from verification step which is available in header section of the application. In order to create automated verification step, we need to create the module for enter insurance data web page.

[04:49] During the scanning, we will add two controls. First one is the link control from the top section which contains the version number. We will rename it to branding instead of big texts and verify the uniqueness of the controls and the properties. Then, we will select to add the first name label control.

[05:20] Now, save the scan wizard to create module and close it. We will now drag and drop this new module into the sample test case as test step. We will rename the test step as it performs the verification operation. Now, we will perform the existence verification of the step attribute first name. Select the action mode as verify.

[05:52] There is multiple verification properties are available in value. Here we will select the exists property with binary true value. The step will be marked passed if condition satisfied. Similarly, we will add the verification step for the branding attribute. Here, we will verify the exact text of the link against the inner text property. To create dynamic buffer to store version, we will replace the version numbers with the keyword curly bracket xb then buffer name buffer version if in third brackets and end the curly bracket.

[06:27] During execution, it will create and store the extracted version number into this dynamic buffer. We will execute this verification step in the scratchbook. It will take few seconds to be completed. After the execution, the scratchbook execution logs will be appeared.

[06:57] It will contains the verification step details. As though the expected and actual values are matched. Both the verification steps are passed. If we navigate to the buffer viewer section, we can see the new buffer with name buffer version has been created with the version number. The action mode constraint is used for checking of a particular value which is mostly used in the tables column. In this particular tutorial, we will find row of text worldwide cover from the first column and then capture the corresponding value from the column gold.

[07:36] Same thing can be done using a loop which is a more complex approach. First, we need to scan the web page to create the module. We will select the correct application window during the application selection. And click on scan button to proceed. From this xcan window, we will select the corresponding price table control and check the uniqueness.

[08:10] Also, we will add the next button which may require in future. Click on save to create the module and close the xcan window. Now, we will navigate to test case section and create a sample test case and rename it. Then we will drag and drop the newly created module into this test case.

[08:45] Here the first step would be, we need to search the text worldwide cover from first column using the action mode constraint. From the price table attribute, we will select the cell label as $1, enter cell value as worldwide cover. And change the action mode as constraint for the cell attribute which is available within row attribute. We will keep the row label as is. Now, we need to capture the value of column gold.

[09:18] So, we will select the next cell as the gold which represents the column name, change the action mode as buffer which will be used to store the column value and enter the buffer name as buffer gold in value. Test step is now completed. We will execute this test step in the scratch book. It will take few seconds to be completed.

[09:52] After the execution, the scratch book execution logs will be appeared. From the execution logs, we can see that the buffer buffer gold is created with the extracted cell value. That's all about constraint. Thanks for watching this video. That's all about basic usage of action mode input, verify and constraint.

[10:24] We will learn more about Tosca features in next video. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools.

[10:55] If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
