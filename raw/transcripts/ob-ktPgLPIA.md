---
id: "ob-ktPgLPIA"
title: "Tosca Tutorial | Lesson 74 - Import Folder Structures from Microsoft Excel Sheet |"
url: "https://www.youtube.com/watch?v=ob-ktPgLPIA"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 466
upload_date: "20230630"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:05:32Z"
status: "raw"
---

# Tosca Tutorial | Lesson 74 - Import Folder Structures from Microsoft Excel Sheet |

[00:06] Hey everyone, welcome back to this Tosca Automation playlist. In this short video, I'm going to show you how you can import folder structure right from a Microsoft Excel sheet. Now if you use Microsoft Excel to basically build your automated tests, then you can import your tree structure directly into Tosca Commander. So you don't have to manually build all the folders into your component folder in Tosca.

[00:37] You can directly use whatever you have in Microsoft Excel or what you have already built in Microsoft Excel and write it straight into your Tosca component folder. So let's see how we can do this. The only thing to keep in mind is that you need to follow some requirements in order to import your tree structure from Microsoft Excel to Tosca. So let's see an example of what we are going to import, right?

[01:08] So I have got this particular folder structure, okay? So this is from the vehicle insurance website. We have used this many times to automate some test cases. And this is how my test case folder structure should look like, okay? So I've got the main folder and then there are subfolders like pre-processing, process and post-processing. So this is following the best practices to build our test cases. And then inside pre-processing, we have open application.

[01:39] Inside the process, we have the actual test case, okay? So the flow of the application like selecting vehicle data and then entering vehicle data, entering personal data, entering insurance data and then choosing the product and doing the premium calculation and then checking the premiums like insurance tax according to the payment, okay? And then in post-processing, we have the close application, okay? So you can see in this structure, we have got different levels of folders, right?

[02:14] And these folders will contain different test cases, right? So this is the folder structure I want to build in Tosca. So instead of going to Tosca and building these folders one by one, which will take some time, right? So if I've got this or if I want to build this in Excel quickly and then directly import it into my Tosca, right? So I can do that by just having a structure like this, okay? So the minimum requirements you need to fulfill when you are building your Excel, right?

[02:48] If you want to import the tree structure from Excel to Tosca, the objects which you are building, they should be hierarchically structured, okay? In columns from left to right, okay? So you can see there is a hierarchy here. So the vehicle insurance offer, so this is the parent object. Inside this, we have got pre-processing and you can see this is in first column and pre-processing process and post-processing. So these are in the second column, okay?

[03:21] And then there is another subfolder, which is open application. Similarly, there are other folders here as well. So these are in the third column. And finally, the final folder is in the fourth column, okay? So this is the hierarchical structure which you need to follow in Excel the way you want to build it in your Tosca component folder, okay? So you need to put it in different columns, okay, or rows and that should be from left to right, okay?

[03:55] So objects of the same hierarchical level are in the same column, okay? So you can see here, these are all the same levels. These objects are at the same level, right? So they are present in just one column. And similarly for this, they are present in another column. So you need to make sure that objects at the same level have to be in the same column. Also you need to make sure that there can be only one value per row, okay? So you cannot have two values in the same row.

[04:28] So make sure of that. And the structure should have less than 15 levels, okay? So you cannot have more than 15 levels in the structure, right? So these are the things you need to take care of when you are trying to import your tree structure from Microsoft Excel to Tosca, okay? Now coming to the actual steps on how to import this particular structure which I built on Excel sheet into my Tosca Commander, right?

[05:02] So for this, what we need to do, first come here and select all the rows which you have in your structure and click on Ctrl plus C to copy it, okay? And then go back to Tosca Commander. Here I can export it into any folder. But it's best practice to basically build a component folder, okay? So I will name it vehicle or I will name it import from Excel, okay?

[05:33] And then inside this, right, when you right click on this, you will see there is an option called create folder structure. You can also use shortcuts like Ctrl N and Ctrl S, okay? And that will basically build a structure from the copied cells of your Excel sheet, okay? So if I right click on this and I click on this create structure, you will see the structure will be automatically created inside this folder, okay?

[06:06] So you can create it inside any folder. You can create a test case folder and then put this inside that or you can put it inside a component folder. You can do it anywhere you like. Now if I want to see all my folders beneath this level, then I can do expand all here and you will see that all the folders which were present in our Excel sheet structure has been created here, okay, with the hierarchical structure which we had, okay, with all the levels.

[06:37] So you can see here there is process, reprocessing and post-processing. Obviously they are not in the right order, but you can always change them, okay? Okay so that's how you can create any folder structure or basically import your folder structure right from your Excel sheets. So if you are building or if you are maintaining your test cases before Tosca in some Excel sheet, you can build a structure like this and put it together or import it into your Tosca project.

[07:11] Okay, so this could be useful in some cases, but I just wanted to show you in the short video how you can do this. So that's all for this video. I hope you enjoyed it and you learned something new today. There are lots more videos coming up. So do remember to subscribe to our channel and until the next video keep watching and keep learning Tosca at our channel QA script.
