---
id: "IasTOBRqL2Y"
title: "TRICENTIS Tosca 16.0 - Lesson 51 | OBSTACLE #9 | Drag & Drop Dynamic WebTable Rows | Repetition |"
url: "https://www.youtube.com/watch?v=IasTOBRqL2Y"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 56
duration: 817
upload_date: "20240822"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:31:48Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 51 | OBSTACLE #9 | Drag & Drop Dynamic WebTable Rows | Repetition |

[00:13] hi everyone this is Ravi welcome to tricentis tasa Advanced Training as you all know I already published 50 YouTube videos covering beginners intermediate and advanced level Concepts from past couple of videos onwards have started teaching you the realtime scenarios where you might encounter with different types of obstacles and how can we solve those obstacles while automating your test cases by using tricentis tosa so I have already published eight realtime scenarios explaining the resolution for eight different types of obstacles this is our lesson 9 in terms of real time scenarios and this is our lesson 51 in terms of overall tric tasa training please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish

[01:15] more videos thank you in this lesson I'm going to teach you a real time scenario where you need to interact with web tables and you need to drag and drop the rows from the web table to the new empty web table so basically the rows within the web table are Dynamic and you need to drag those rows in sequence order to the new empty table so this is the obstacle we are going to solve so let us first see and understand in detail what is the obstacle we are solving for so this is our obstacle to-do list this is categorized as medium but I can say it has hard okay so now let us go for

[02:16] it so if you see here so move all tasks from to do to completed in the order of their given task ID so which means I have to drag the row from this table and drop here but while dragging I need to make sure that I drag in sequence order one this first row is first and then row with id2 is second and row with ID3 is thir 4 5 6 okay so track the row with ID 1 to the empty table and drag row with id2 to the empty table then ID3 ID 4 id5

[03:17] id6 and your automation problem is solved so this is what we need to automate if you see here the rows keep on changing see this is dynamic it's not like static rows see now you have id1 it almost like bottom right so this keep on changing okay so we need to track the rows in sequence order with ID number and drop into an empty table so how can we do that for that let's go back to trient tasa so now let us scan the objects okay right click on the obstacles select scan and application now select the application click on

[04:25] scan so if you see here this is one table which is to do tasks and this is another table which is is completed task right so we need to drag all the rows from to-do task table and we need to drop on completed task table right so here to do task table and completed task table these two we need to select so now these two are uniquely identified and I'm not seeing any orange color that means these two tables are now uniquely identified so now let us rename this module with the name of obstacle copy and paste it here now save the module let's close the X scan so let's go back to trient tasa so this is the new module that we scanned so you have

[05:26] two tables this is your Source table and this is your target table so now let us create a new test case let's go back to blue color section which is test case section right click on the folder and create test case name this with the same abstral name that we copied earlier double click on this so now you need to drag and drop your module onto test case now let's observe carefully so expand these all okay so here if you see I need to drag the row with the ID number that starts with one now let's select column and if you see what is the column that ID exist the column name is ID so now what I'm going to do select column Name ID and now what is the sell value that I need

[06:29] to sell the cell value is one so let me drag my first row what I'm going to do here I'm going to specify here simply one okay the cell value one and here I'm going to call a method called drag that we used in earlier lesson drag and change your action mode as input okay I'm dragging my first row which starts with ID 1 and where do I need to drop I need to drop in this table completed task table this is my completed task so I can directly drop here open curly braces drop close curly braces and here your action mode should be input so let me Simply Save this we have not completed automating everything okay

[07:29] I just want to test this one okay right click and run in scratchbook it is dragging the row with ID number one right done but now how can we drag rest of all the rows in sequence order so what we can do here I'm going to apply a method called repetition okay how so let me go back to my test case right click and create a new folder here what I'm going to do I'm going to name this as repetition and I'm going to bring my entire test case into this repetition folder I'm just dragging and dropping in

[08:31] repetition folder now select repetition folder and expand the properties of folder okay test case folder if you see here the repetition how many rows we have total we have total six rows right right total six rows what I'm going to specify here the repetition as six now instead of specifying the value one now I want to delete this I want to use repetition that we declared here see we declar repetition here right so simply copy this and here instead of one I'm going to use open curly braces repetition close curly braces what it does plus first when I

[09:31] execute your repetition value is 1 right it comes here here it takes one it drags the row which has ID 1 and drops here and this entire folder repeats six time and second time it again comes here this time your repetition value is two it comes down here now the repetition value we already passed as two it's going to drag the row with id2 right and drops in the table like this it's going to repeat for six times with 1 2 3 4 5 6 as your value within the column cell okay I have selected column as ID and here I'm repeating the values from 1 to 6 so now let me run this particular

[10:33] test case and see what happens okay right click and run in scratchbook first it's dragged and dropped number one now dragged and dropped number five six so you solve this automation problem so let me just repeat this again what we did okay so if you see here all my repetitions are passed so you can see here repetition one repetition 2 repetition 3 right so here the

[11:34] repetition value it passed here okay so let me explain what we did okay first we have selected a column as ID now what is the cell that I want to select I want to select a cell with ID 1 2 3 4 right those are the Val values in the cell so those values are coming from this repetition folder repetition six times for the first time it comes as one it drags and drops for the second time it comes as two so basically you need to use repetition folder if you don't use repetition folder then you have to repeat the same step six times and then you need to hard code these values as 1 2 3 4 5 6 so which does not make sense so you can simply use repetition folder to repeat six times drag and drop all

[12:37] the rowes from Source table to the Target table so if you have any queries leave your queries in the comment box I'll try to respond to your queries thank you hope you all understand the obstacle where you need to interact with web table and you need to drag each and every Row from web table which are dynamic in nature and drop onto a new empty web table by using repetition drag and drop methods please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you
