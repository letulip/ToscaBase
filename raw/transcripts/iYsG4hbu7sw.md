---
id: "iYsG4hbu7sw"
title: "TRICENTIS Tosca 16.0 - Lesson 63 | OBSTACLE #21 | Search Table Cell Value | Constraint Action Mode"
url: "https://www.youtube.com/watch?v=iYsG4hbu7sw"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 68
duration: 860
upload_date: "20241112"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:33:56Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 63 | OBSTACLE #21 | Search Table Cell Value | Constraint Action Mode

[00:12] hi everyone this is Ravi welcome to tricentis tasa Advanced Training as you all know I already published 62 YouTube videos covering beginners level intermed level and advanced level concepts of trien Tas from couple of videos onwards I've started teaching you the realtime scenarios where you might encounter different types of obstacles and how can we solve those obstacles while automating your test cases please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos this is our lesson 63 in terms of overall tricentis TSA automation training and this is obstacle 21 in terms of real time scenarios in this lesson I'm going to teach you how can we

[01:13] solve an obstacle where you need to interact with a dynamic web table and you need to search for a specific cell value in this particular Dynamic web table by using constraint print action mode and by using search table cell value methods so now let us see in detail what is the obstacle that we need to solve for this is the obstacle list and this is our obstacle that we are working on the name of obstacle is table search and which is categorized as hard let us go for it so let us see what is the obstacle enter true or false depending on whether the table contains a cell with value 15 you see the below table let's see if you

[02:13] have any value 15 here so in the cells I do not see a value 15 any in any of the cell so that's why I'm going to enter as false see as soon as you enter false you solve the automation problem now let me try again so this time again I don't see any 15 value in any of in any of the cell so that's why again I'm going to enter as false so let me try again now you can see here there is value 15 in one of the cell so this table is dynamic and all the values are dynamic DC in the table so now I can just enter true so that means to solve this problem you need to search for a specific value in each row and each colum so how can we

[03:17] achieve this for for that let us go to trentos as usual we're going to scan the objects that are required to automate the scenario this is my obstacle folder I'm in modules section right click in right click on obstacle folder select scan application now this is the application that I would like to select and click on scan so now to automate this particular scenario we need to add this web table and also you need to add the text box correct so if you can see here this is my web table select the web table and then you can select the text box also where we'll be entering the true or false so now you can see these

[04:21] two objects are uniquely identified you can see here selected item is unique in the same way table also selected item is unique now let me name the module as obstacle 41 0 36 this is my obstacle name let me copy this obstacle let's copy the obstacle and then name the module with the same obstacle name and then save the module now now close the X scan so let us go back to trient tasa and you can see here the latest module whatever we added this is the latest module 41036 double click on this so you can see these two objects that we added so now let us go back to our test case

[05:24] section the blue section we are creating the test cases under folder obstacle right so all these test cases that we already worked on almost like 20 obstacles now right click on this folder and select create test case and name this test case with the same obstacle name now double click on this test case so to automate your scenario drag the module that we scanned and dropped on and drop onto test case let's expand this so here what is the step that we need to follow so what is our first step I need to First search for number 15 in every row and every column of this particular web table how can we do that so to search number 15 and filter out all other values or filter out all other

[06:27] cell values you have to use constraint mode so I have already published another video on constraint mode how can we use constraint mode in our in my previous video sessions I would recommend you guys to visit those sessions so now let us go back to the trient stasa and here under cell what I would like to use here I would like to use the constraint option so if this cell has a value of 15 I would like to I don't want to verify this instead I would like to introduce a constraint One Thing If You observe I'm not providing any row number here because I would like to verify this value of 15 in every row and every cell correct so that's why I'm not providing

[07:27] any value here I'm simply entering the value 15 and action mode constraint what it does it goes every row by row and every cell it searches for the 15 if it exists right then it considers that particular row so whenever it finds let's say in this particular example when it comes to row 15 sorry when it comes to Row three it verifies each row sorry it verifies each cell and that means at Row three tricentis will be able to identify the value 15 that means is using the constraint it filters out rest of the rows as soon as it reaches this 15 row now I would like to store one value here I would like to validate one thing what

[08:30] if this row exists that means the row containing the cell value 15 okay if that exist then I would like to store that into a buffer I'm going to make this as bore result and here I would like to change the action mode as buffer so what happens it first takes the row one it then verifies if any of the cell in row one contains 15 it does not because I'm using constraint mode then again it goes to row two it does not contain 15 so it filters out and then it goes to row three and it

[09:32] verifies each and every cell value then it finds the 15 value in the cell that means it considers this particular row now if this Row the third row exists value 15 right now I'm instructing tasa if row exists with value 15 then store the result exists true or false result into a buffer called bore result right so in this case I'm going to get exists as true for the row three right I would like to enter the result true or fault result into this particular text box that's why I'm going to call the above buff buffer whatever we are storing here to call the

[10:33] buffer open curly braces capital B open Square braces Capital bore result this is my buffer name close Square braces close curly braces done now let's save the test case and change the work state change the work state as completed and now let's run the test case with the existing values here right for this particular scenario it should return True Value and it should enter true right let me right click and run in scratchbook it entered true because it finds a row with value 15 hence it

[11:36] returns as true let's go here now I can see here see it received value of true so if I go here I can see here the bore result has been set to Value true now let me just try again okay let me try again so here now you can see I don't have value 50 I would like to run the test case again and see if I return the value of false right click and run scratchbook it searches see now the value has been

[12:36] entered as false you can see here it searched the first row could not find 15 value by using constraint it filters out it searches second row it could not find 15 value it filters out and third row it could not find it filters out that means the row exists will be false hence it entered the value as false so this is how you can search the value within the table cell by using constraint mode and with the combination of buffer to enter the result in edit box if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how can we solve an obstacle where you need to interact with the dynamic web table and you need

[13:39] to search a specific table cell value without knowing the specific column and without knowing a specific row by using the constant action modes and search table C value methods please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos and don't forget to like and share the video thank you
