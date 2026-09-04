---
id: "l5SNsxfX9no"
title: "TRICENTIS Tosca 16.0 - Lesson 72 | OBSTACLE #30 | Click On Screen | Screen Width | XModules"
url: "https://www.youtube.com/watch?v=l5SNsxfX9no"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 77
duration: 743
upload_date: "20250130"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:35:20Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 72 | OBSTACLE #30 | Click On Screen | Screen Width | XModules

[00:12] hi everyone this is Ravi welcome to trient tasa Advanced Training as you all know I already published 71 YouTube videos covering beginners level intermediate level and advanced level Concepts from few videos onwards I've started teaching you the realtime scenarios where you might encounter different types of obstacle and how can you solve those obstacles while automating the test cases by using trient tasa so this is our lesson 72 in terms of overall tric TSA automation training and this is our obstacle 30 in terms of realtime scenarios please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you in this lesson I'm going to teach you how can we solve an obstacle where you need to click an object on the screen based on the screen

[01:13] width by using an inbuilt module within tricentis tasa so now let us go and see in detail what is the obstacle that we need to solve for so here is our obstacle the name of obstacle is red stripe which is categorized as easy let us go for it so you can see here click on button label generate and then click on red stripe that appears the number below the button informs you how far to the right from the edge of screen stripe has appeared so let us first click on generate button so now you can see a red line is appeared and this number represents how far this red line is to the right from the edge of

[02:16] your screen so that means the width of your screen until this red stripe is 62 let me generate again so now the width is 25 and this is your remaining 75 again now it is 66% so basically the red stripe is at the 66% of your width of your screen okay so now we need to click on this red color line so how can you click on this red color line that is what we need to automate so now to automate this scenario let us go to prent Tas so as usual we are going to capture the test objects under obstacles folder so right click on this obstacles folder select scan

[03:23] application so now select the application that you would like to scan and click on scan so here I don't see the number property here so now here I don't see the number here for that let us go to filter and expand the filter one click still I don't see the number another click now you can see here the number see this is your number which is your div element let us select this number you can see here the property of the number is ID number you should not select your inner text because this percentage keeps on changing whenever you click on generate button so this is not going to be constant so I'm going to select ID number Tag div right so these two are the elements that I

[04:23] would like to select one and two both of them are uniquely identified okay okay so now let us name this module as the name of your obstacle copy and paste it here and now save the module and close your X scan so let us go to chasa here now this is our latest module that scan this one double click on this now I should see two objects generate button and your number so let me rename this as number so now let us go to our left side section which is test case section which is in blue color so as usual I'm going

[05:24] to create a new test case under obstacles folder right click on this folder select create test case and name with the same name of your obstacle double click on this test case now to automate the test case or to automate the scenario drag this module and drop here so here what I'm going to do I'm going to name this as generate let's do one thing click and generate so what I'm going to do here I'm going to Simply click on generate Button as soon as I click on generate button I have to see what is the percentage of the width where your red stripe will appear so this is the percentage what I'm going

[06:25] to do I'm going to buffer this value into a variable here I'm going to say inner text equal to and store this into a buffer called num here your action mode should be buffer right now I have stored the buffer and then you need to click on this red button this red stripe you need to click on this red stripe to click on red to click on red stripe you have an inbuilt function called let's go here right click search and ADD test step and type click on screen so you have a click on screen HTML right so this is what you need to

[07:26] select there is another click on screen here which is mobile I don't want to select that one I want to select click on screen from HTML select this one and here you need to provide caption of the browser or window what is the caption you can see tricentis obstacle what I'm going to do here I'm going to enter trient UPS upster obstacle so I'm going to just enter partial information I'm going to enter the partial title and then I'm going to use the regular expression prent is obst and anything it can have right so the name is obstacle very big name basically it has obstacle do test automation obstacle right so I'm just using the regular expression to identify the caption and then what is

[08:28] your X coordinator and what is your y coordinator X means what is your width and what is your height or what is your horizontal component what is your vertical percentage R what is your horizontal percentage and what is your vertical percentage so here I'm going to call the buffer that I have stored here so for that Curly Braes open curly braces capital B and now your buffer name and close curly bra so here I'm specifying that your width is the 56 and what about this vertical coordinator do you want me to click on here here here here here where so probably I can leave this as I can provide any number I want because this vertical

[09:29] because this stripe is from bottom to top right so better I provide the same buffer name number here the same percentage that I'm storing under buffer I can keep the same or I can specify any number I want but however to avoid confusion I'm entering the same the value that I'm storing under buffer now let's save this let us mark this as completed so what we have done first by using the module that we captured I'm clicking on generate and then immediately I'm storing the value that is generated in the buffer and now by using that buffer value I'm using an inbuilt click on screen X module where I'm specifying the

[10:30] caption of your browser and then I'm calling the buffer value here so that I can exactly click on that red stripe now let's save the test case now let us regenerate this and then right click and run in scratchbook see now it has regenerated the red stripe and then he clicked on the red stripe let me try again okay let me try again so now there is no red stripe right now let us run this now again right click and running scratchbook now it clicked on generate and then

[11:33] which is 30 33% and then it clicked on red stripe at 33% of the width of the screen so if you go to your tricenter tasa and you can see here the buffer has been stored as 33 and then it is clicking on screen with that 33% so hope you all understand the concept if you have any queries leave your queries in the comment box I'll try to respond to your queries please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos and don't forget to like and share the video thank you
