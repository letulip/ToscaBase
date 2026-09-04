---
id: "4V0ygehvBAk"
title: "Tosca Tutorial | Lesson 21 - Verify  RowCount & ColumnCount of Excel WorkBook | Excel Engine |"
url: "https://www.youtube.com/watch?v=4V0ygehvBAk"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 456
upload_date: "20230708"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:16:05Z"
status: "raw"
---

# Tosca Tutorial | Lesson 21 - Verify  RowCount & ColumnCount of Excel WorkBook | Excel Engine |

[00:07] hey everyone welcome back to this task automation playlist and today we are going to continue with another Excel feature which is available in Tosca now we have already seen how you can create this particular Excel workbook with a new uh Excel worksheet and even you can enter different values into your Excel cells right so just like we have prepared this employee worksheet okay with some employee names and salaries and total salary we have also verified it using different Excel modules present in the standard subset now if you have not watched this video I would recommend to go back to our Channel and watch this video first and then come back to this video where I'm going to explain you how you can use the same t-box modules to basically find the row count and column count for your Excel sheet okay so for this particular Excel sheet you can see there are four rows right and there are two columns so

[01:09] that is what we want to verify or we want to find out after we create some Excel sheet or for an existing Excel sheet okay so let's go back to Tosca and here you can see I have got already two test cases one is to compare to Excel files and one is to create uh an Excel sheet with some values in it right now I'm going to create a third test case and I'm going to show you how you can get the row count and column count of your Excel sheet using the Excel modules present in Tosca okay so I'm going to name it get row count and column count okay and we are going to reuse some of the test steps okay so these are basically the tree box modules which we have used earlier so I'll be using the open Excel bug book I'll be using Define excel range okay and a close Excel

[02:10] workbook so these three modules I'll be reusing here we need to make some changes quickly okay so I don't want to create any new um Excel workbook I will be using the same Excel workbook which is already created so I will change it to false and then Excel range okay so workbook name worksheet name and the range name will remain same here close Excel workbook so that's also fine right now I'm going to add one more module here so let's go out to our test step and here we will try and find Excel range manipulation okay the last one and uh we are going to drag it before the close Excel workbook here I'm going to change this name and name it to get row count okay and then I'm going to copy this and paste it again okay and again I'm going

[03:13] to place it here and I'm going to change this to get column count okay so these are the two test steps built from the same module which is the Excel range manipulation right so in this we have got the range name so we'll keep it so that it can find that particular range okay which we have defined already and we're going to paste it here in the data table we just need to uh get the row count okay and how you can do that so under the value just click on this Arrow okay and here you will see you can Define some property and some value right so here I'm going to uh make it row count okay and here I'm going to give some value called RC or variable name okay and I'm going to change this action mode to buffer so what it is going to do is it is going to get the row count okay so it's a

[04:15] special property which can get the row count from a table in Tosca and then it will assign that value to RC okay similar thing you need to do it here you can also directly type this okay but let's do it this way so again column count and then uh in the value we'll put it CC okay and then we'll change this to buffer right so RC and CC are the buffer values so that will contain the actual row count and column count of this particular table right so that's all you need to do uh to get the row count in column count for your Excel workbook right let's go ahead and run this now okay so this is going to fail because my file is already open right so whenever

[05:16] you run uh any anything with an Excel sheet or Excel workbook you need to make sure that the Excel is not in use okay so let's go ahead and close our Excel okay save it so let's try and run it again but before that I just noticed that we missed one thing okay so in the get column count test tip we did not give the range name so let's give this employee data and just just verify okay so both the range names are present and let's try and run this again hopefully this time it will pass okay so the test case has passed and if I look at the results right if we go into the log info you can see uh range employee data is updated successfully and then in the row count you will see that the RC has been set to

[06:17] Value 4 okay so that's our buffer and then the column count uh okay it has been set to two so we had four rows and we had two columns and that's what it is storing in the buffer now if you want to verify a certain row count and column count you can just use this buffer values and put a verification step later on okay so that we already know so I'm not going to do it I will leave it for you to do it okay so that's how easy it is to find the row and column count of a particular Excel workbook it may be an existing one or if you are creating a new one you can still add the steps and then you can verify the row count and column count so that's all for this video I hope you enjoyed it and you learned something new today if you have got any questions just leave it in the comments and do share it with others who might find it useful also don't forget to subscribe to our channel

[07:18] so that you don't miss out on any new videos being uploaded to our Channel until the next video keep watching and keep learning
