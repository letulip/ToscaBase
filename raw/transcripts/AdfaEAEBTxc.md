---
id: "AdfaEAEBTxc"
title: "TRICENTIS Tosca 16.0 - Lesson 36 | Row Count and Column Count Of Excel Workbook | Excel Engine |"
url: "https://www.youtube.com/watch?v=AdfaEAEBTxc"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 41
duration: 539
upload_date: "20231211"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:29:06Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 36 | Row Count and Column Count Of Excel Workbook | Excel Engine |

[00:13] hi everyone this is Ravi welcome to price Anda automation tutorial as you all know I've already published 35 YouTube videos covering different topics of prentist tasa automation Concepts so in my previous session we learned about how can you create modify and then how can you manipulate the Excel range or Excel workbook by using Excel engine in triena so I would recommend you guys to go through my previous lesson 35 before you watch this session this is our lesson 36 in terms of overall tricentis TSA automation Concepts and this is our lesson 21 one in terms of Advanced Training so in this lesson I'm going to cover how can we calculate the row count and how can we calculate the column count of an Excel

[01:14] range within the Excel workbook which means if you store enormous data Excel sheet right and then how can we calculate the number of rows of data that is present in the Excel sheet and then how can we calculate number of columns of the data that is present in the Excel sheet please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you now let us jump onto the system and see how can we calculate row and column count of your Excel workbook this is my TSA so if you remember correctly we have learned all these oper operations in our previous session tbox delete file tbox open work book tbox create Excel worksheet and then tbox Define excel range tbox Excel range

[02:15] manipulation to modify the data tbox close or save workbook right so now let me create a new folder here I want to create a new folder called row and column count and then I'm going to create a new test case row column count here I want to copy some of the test steps as is from my previous session okay I want to copy open Excel workbook and then Define excel work range Excel range and then I want to copy close workbook copy all these steps and paste in the new test case okay now we have Define excel range

[03:20] correct and then open Excel workbook so let me just put it into chronical order so here first I'm going to open Excel workbook but in this case I don't want to create a new I want to use an Excel existing Excel workbook that we created in my previous session that's why I'm selecting create new as false so I want to use the same workbook that we created earlier so let me show that workbook okay in this workbook we can see this is this has almost like six rows and then two columns right so let me close this the same I'm using here now let me copy or let me create a new test step here so let me add a new test tip called tbox Excel range manipulation I want to insert a new step for Excel range

[04:23] manipulation and bring this prior to closing the Excel workbook and and here what is the range name the range name is same as my previous step I want to use the same range name right and I want to rename this as row calculation now I want to insert the same step one more time Excel range manipul and bring this Excel range manipulation again prior to closing your Excel workbook and I want to define the same Excel range because I'm calculating the column count for the same Excel range and now for row count how can I calculate the row count so you need to use the

[05:24] method called for the web table I'm talking about in the data table you need not to enter any row and column as we did in earlier session while manipulating the data because we are not manipulating the data here we are just calculating the row count that's why you just need to use the data table row here I want to calculate the row count so there is an inbuilt method called row count call that inbuilt method here R count equal Al to I'm going to store it into buffer called row count I'll do one thing to differentiate I'm going to call it as Excel row count right and here the action mode should be buffer need to store this into a buffer called Excel row count in the same way for column count

[06:24] also I have another method called column count column count no space equal to excel column count so here we are calculating the row count and column count of this particular Excel range that we defined right now here also you need to change into buffer so now let us understand the flow first what we are doing we are opening an Excel workbook which is an existing workbook I'm not creating new workbook and then we already defined the Excel range for the particular work book and then I am calculating the row count in the Excel workbook and then I'm calculating the column count I'm storing them into buffer so that I can see the value in the buffer and I can use that

[07:25] buffer value for my future test case automation and I'm closing the workbook and I'm saving the workbook while closing the workbook so now let us save this and let us run this particular test case right click and run it should calculate row and column count of your Excel workbook so let us see our test result so if you see here your data table row count is six correct and your column count should be two and that should store into a buffer called Excel column count has been set to six same way Excel row count has been set to six and the column count has been set to two right hope you all understand how

[08:28] can you you perform row count and column count for an Excel workbook by using trient to please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you
