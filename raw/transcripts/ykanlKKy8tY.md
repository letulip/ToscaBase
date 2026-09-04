---
id: "ykanlKKy8tY"
title: "TRICENTIS Tosca 16.0 - Lesson 76 | OBSTACLE #34 | Table Baseline Comparison | Store Baseline Table"
url: "https://www.youtube.com/watch?v=ykanlKKy8tY"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 81
duration: 724
upload_date: "20250407"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:35:57Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 76 | OBSTACLE #34 | Table Baseline Comparison | Store Baseline Table

[00:13] Hi everyone, this is Ravi. Welcome to Tricentis Taska automation tutorial. As you all know, I have already published 75 YouTube videos covering beginner's level, intermediate level, and advanced level concepts of tricentis tasks. From few videos onwards have started teaching you the realtime scenarios where you might encounter different types of obstacles while automating the test cases and how can we solve those obstacles by using tricentis tasks. Please do subscribe to the channel click on bell icon you'll receive notifications whenever I publish more videos. Don't forget to like and share the video. Thank you. This is our lesson 76 in terms of overall tricentes tasks automation tutorial and this is obstacle 34 in terms of realtime scenarios. So in this

[01:15] lesson I'm going to teach you how can we solve an obstacle where you need to store the baseline table which will have n number of rows and n number of columns and then you need to compare this stored baseline table content with the same table but the content has been changed. So now how can I identify what kind of content and what content in which row and which column the content has been changed in the table. So that I'm going to do by using table baseline comparison. So now let us go and see in detail what is the obstacle that we are going to solve for.

[02:04] So here is the obstacle list that we keep working from past few videos onwards and today's obstacle is find the changed cell. This is the name of your obstacle and which is categorized as medium. Let us go for it to see the details of obstacle. What it is saying? Click show change table to change the value of one random cell. Find the cell and enter the row, column, original value and changed value into the text boxes showing here. Use task R to find this cell. So values can be entered manually. There is no need to automate this step. So what it is saying here if you see this is your original table which has n number of columns and then n number of

[03:06] rows. If I click on show changed table. So this is the same table but the content has been changed. What content that has been changed? randomly some specific cell content will be changed. If I click on show original table, there is one cell which has a different value compared to the original table and changed table. So now you need to identify what is the cell that has changed from these n number of cells. As soon as I show change table, so this is the table where one cell value has been changed. We don't know what cell value has been changed. It is very difficult to find with your human eye. So we can use tricentistosa to compare the tables

[04:07] between original table and change table. So for that let us go to tricestosca and let us start scanning the objects. So what are the objects that we need to scan in this case? In this case you just need to scan your table. So here right click on obstacles folder select scan application. Now select the application that you would like to scan and click on scan button. So now what is the table that we need to cap? What is the table that we need to capture? So this is the table that we need to capture. Select the table and do I need to capture all these edit boxes? So these you need not to

[05:08] capture. As soon as you identify which row, which column and what is your original value and what is your changed value in the cell, you can just enter this manually. So that's why I just need this table. And now change the module name with the obstacle name here. Copy this and then paste the obstacle name here. And now save your module. Then close your Xcan. Let us go back to Tricentesa and come down to bottom. So this is the new obstacle that we captured. Double click on this obstacle to make sure the objects are available. So I can see here now table row column I can see the table is available. Now let us go back to our obstacle test case folder left side right click on this obstacle folder and create test case and then here we

[06:11] already copied the obstacle name. I'm going to paste the same obstacle name and then double click on test case. Now let us start automating. To automate the test case, you need to drag this table and then drop onto your obstacle. And now let us expand this one. So to perform table comparison what we need to do first you need to capture the baseline table. How can I capture the baseline table? Let's again go to original table. Let me click on try again. First, I need to capture the original table. This is my original table, right? And this original table is my baseline table. What I'm going to do here to capture the baseline table, right click on this table and then select create baseline.

[07:14] As soon as you select create baseline, it's going to start capturing this entire table content. All rows, all columns. You can see it captured 10% of your table. It is basically capturing the entire content of this particular original table. It takes couple of seconds to complete capturing the entire table, rows, columns and the content.

[07:55] So now you can see here table baseline successfully created. Click on okay. If you go back here and expand this see now it says table compare. It says the baseline has been created at 15th March 8:24 sorry 15th March 108 p.m. So that means now to compare the table. Let's go back to the application as we captured the baseline table. Now I'm going to click on show change table. So now this is the change table where one of the cell value has been changed. So how can I identify which cell has been changed? Now let's go back to tricentistosa.

[08:49] You need to run this test case again. Why? Once it creates the baseline, now it is marked as table compare. So that means whenever you run this test case, it's going to compare the existing display table with the baseline table that we captured at this time stamp. So let me right click and run in scratchbook.

[09:24] So now it started comparing the original table with the changed table. So your test case is going to fail because when it compares both the tables, it's going to identify that one of the cell is not matching. So if you see here it says column this in row 23 was modified. What is the expected value? This is your original value and this is your actual value. So let's copy this entire thing into a notepad.

[10:04] Let's paste it here. So what is the row? Row number is 23. Let's go back to our obstacle. So here I'm going to enter 23 and what is the column that has changed? This is the column right? So basically these are the column headers somewhere we have that column here. Okay this is the column and what is your original value? This is your expected value. That means the baseline table has this value in the cell. And then what is the changed value? The changed table has this value in this cell. Now if I submit this should be able to solve the problem successfully. As soon as you submit it should say your automation problem solved successfully. But however it is

[11:05] not working right now. But that is how you can solve the obstacle to compare the tables with your baseline and the change table. So if you have any queries, leave your queries in the comment box. I'll try to respond to your queries. Thank you. Hope you all understand how to solve an obstacle where you need to store the baseline table and then compare the baseline table content with the changed table content. Please do subscribe to the channel, click on bell icon, you'll receive notifications whenever I publish more videos. Don't forget to like and share the video. Thank you.
