---
id: "iOh_KgFyhWU"
title: "TRICENTIS Tosca 16.0 - Lesson 64 | OBSTACLE #22 | Table Search | Dynamic Table | Buffer Action Mode"
url: "https://www.youtube.com/watch?v=iOh_KgFyhWU"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 69
duration: 626
upload_date: "20241113"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:34:05Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 64 | OBSTACLE #22 | Table Search | Dynamic Table | Buffer Action Mode

[00:12] hi everyone this is Ravi welcome to tricentis tasa Advanced Training as you all know I already published 63 YouTube videos covering beginners level intermediate level and advanced level concepts of tricentis tasa from couple of videos onwards have started teaching you the realtime scenarios where you might encounter different types of obstacles and how can we solve those obstacles while automating your test cases please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos this is lesson 64 in terms of overall tricentis tasa automation training and this is obstacle 22 in terms of realtime scenarios in this lesson I'm going to teach you how can we solve an

[01:12] obstacle to interact with the dynamic table and how can you perform table search for a specific cell value based on your row and the column values by using the buffer action mode and table search methods now let us see in detail what is the obstacle that we need to solve for so this is our obstacle that we are going to solve for the obstacle name is meeting Schuler and which is categorized as easy so let us go for it to understand the obstacle so if you see here is the room available on Thursday 11 to 1 p.m. WR open or closed so you can see here this table has the time schedules 9

[02:13] to 11 11: 1 1 2 3 and 3 to 5 so this so this particular column values are constant these are not changing and you also have The Columns Monday Tuesday Wednesday Thursday Friday but but the values either the time slot is open or closed for this particular day on this particular time is dynamic so let me refresh again okay if I refresh so you can see here now on Thursday from 11: to 13 now I can see the schedule is open so it keeps on changing it is not constant so basically you need to enter whether the schedule on Thursday from 11: to 13 is open or closed so that's what we are going to

[03:15] validate so now it is very easy to automate the scenario why because we already know that we have to consider a row which has the time period between 11 to 13 that means the row is constant and also you have to search for the availability on Thursday itself that means your column is also constant you know the row and you know the column so it is very easy to validate the schedule whether it is open or closed on particular day so for that let us go back to our trient tosa and here as usual you need to right click on obstacles folder select scan and click on application so this is the application I would like to select select the application click on

[04:20] scan so here for this particular test case we need to capture the web table and edit box so this is my Tim table is a web table and this is my result text select both of them now name the module with the obstacle name simply copy this obstacle name and paste the obstacle name as module name now save the module and close your X scan so let us go back to Tri and tasa so you can see here now the new module whatever we scanned which is this one 41 037 can see here you have time table and then result text so let us go back to our test case section now as you all know we are capturing every test case under obstacle folder so

[05:21] in the same way for this obstacle as well right click on obstacle folder test case folder and select create test test case and name this test case with the same name as obstacle okay and now double click on this and go to your test case so to start automating your test case I need to drag this module and drop onto your test case now let's expand the test case so here we already know that we need to validate the the row which contains the value 11 to 13 so I would like to copy this value and here you need to Simply provide the row name as 11 to13 so let's do this 11 to 13 so I'm instructing

[06:21] tasar to select the row which has the value 11 to 13 so action mode is Select and now what is the column that you need to verify expand this cell you can see here it is showing Monday Tuesday Wednesday Thursday as per our use case you need to see the availability on Thursday so select the cell as or the column as Thursday right I'm selecting the column as Thursday and now as soon as it meets the criteria I would like to store the value into a buffer what I'm going to do here I'm going to specify the buffer name here bore status what is the

[07:22] status whether it is open or closed so bore status is the buffer but here here I'm not verifying it instead I'm actually buffering it so I would like to buffer the value which is available in row 11 to 13 and column Thursday right so storing that into your buffer and now I need to enter the same thing here whether it is open or closed I'm going to call this buffer into a edit box I'm going to enter the buffer value in the edit box so open curly braces capital B open Square braces bore status close Square bra close curly braces and your action mode is

[08:25] input so now let us chain the work state as completed and save your test case now let me execute the test case and see if it works right click and run in scratchbook it entered open because on Thursday 11 to 13 it is open that's why it entered open hence your automation problem solved successfully so let me try this again so now you can see here now 11 to13 on Thursday your schedule is closed let me run this if it works or not we'll see right click and run in scratchbook now it entered as closed you

[09:29] can see here now it entered as closed and your automation problem is solved successfully so if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how can we solve an obstacle where you need to interact with the dynamic table and you need to perform a table search for a specific cell value based on the row and column by using buffer action mode and table search method please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video
