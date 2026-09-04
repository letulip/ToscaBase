---
id: "646CwrhT93k"
title: "TRICENTIS Tosca 16.0 - Lesson 71 | OBSTACLE #29 | Future Date| LDay | Date Expressions| Offset"
url: "https://www.youtube.com/watch?v=646CwrhT93k"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 76
duration: 672
upload_date: "20250128"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:35:12Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 71 | OBSTACLE #29 | Future Date| LDay | Date Expressions| Offset

[00:12] hi everyone this is Ravi welcome to tricentis tasa Advanced Training as you all know I already published 70 YouTube videos covering beginners level intermediate level and Advan level concepts of prent tasa test automation from QV videos onwards I've started teaching you the realtime scenarios where you might encounter different types of obstacles and how can we solve those obstacles while automating your test cases so this is our lesson 71 in terms of overall tricentis tasa Advanced Training and this is our lesson 29 are obstacle 29 in terms of real time scenarios please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you in this lesson I'm going to teach

[01:12] you how can you solve an obstacle where you need to interact with the application and you need to enter the long day or the full name of the we or the full name of of the week day of future date by using date expression with the help of tricentis tasa so now let us go and see the obstacle in detail what is the problem that we need to solve for so this is our obstacle the name of the obstacle is future Christmas and which is categorized as easy let us go for it so it says you need to calculate on which day Christmas Falls in 2 years WR it as a word like Monday so let's

[02:13] assume our 25th December 2025 falls on Thursday but we need to calculate which day of the Christmas Falls after 2 years that means your 2027 2627 so in the year 2027 the Christmas falls on which day so in 2027 the Christmas falls on Saturday see that means you have solved your automation problem successfully so how can I calculate the day of the Christmas that falls in 2 years so let us go to triena and let us automate this scenario as usual we're going to capture

[03:14] the objects or elements of the application under modules so this is the folder that we are capturing obstacles folder under obstacles folder right click on this obstacles folder select scan application and then select the application that you would like to scan and click on scan so you can see here now we need to enter the full day of weekday in this edit box so that's why I'm going to select the edit box enter the day so this is the only object that we need to automate this scenario and then I'm going to name the module with the obstacle number copy

[04:16] this and paste it here so you can see this enter the day edit box is uniquely identified so done now let us save the module and close the X scan so let's go back to trient tasa you can see here the new obstacle that we captured this is the new obstacle that we have this is our new obstacle so now let us go to the left section let us go to the left section test case section so here under folder obstacles let me create a new new test case right click on this obstacles folder and then select create test case name this as same as the obstacle number and now double click on this test

[05:19] case so let us automate the test case to automate the test case we need to drag and drop your module onto your test case and now let us expand this one so here we need to calculate the day on which the Christmas Falls in 2 years so for that let us go to Trenta so here so there is one function called L day inasa so to call any function you need to open curly braces now type l d a see you can see here now L Day Day according to the current system settings so what is the syntax to calculate the long day you need to enter the date and then your offset and then in which format you need the output so

[06:21] basically L day your date expression your offset and then your format so this is the format so what I'm going to do here l d a y now let us write the expression within the square braces and close curly braces so here first you need to enter your date expression open curly braces date and what is the date I would like to enter current year Christmas date that is is 25 do 12 do 2025 this is my current year Christmas date and now what is your offset my offset is 2 years because I need to calculate from I need to calculate the Day falls

[07:21] in 2 years right so I'm going to put a I'm going to enter the offset as place to y and then what is the format that you need I don't want to enter any format because I need a full day that's it I don't want to change the format this expression by default gives you the full name of the weekday right so once that is done close curly braces so here now let me explain again what we have done L day is a function which returns the full name of the week day so here I have entered the date expression where I have entered the date of this year Christmas and then I'm providing the offset of offset as 2 years that means it's going to return the full name of

[08:22] the week day for the Christmas date in the year 2027 right so once that is done so now let us run this test case and see if it works correctly so let me change the work state to completed and save the test case let's go back to our application let's click on try again now let's run the test case in scratchbook right click and run in scratchbook it should enter the four full day of Christmas in the year 2027 which is Saturday yep see you can see here now it entered Saturday that means our test case is passed so if you want to understand if it is calculating correctly or not before even you run the

[09:24] test case what you need to do you have to come back to your prent Taska there is another way right click on this and you can select translate value this way you can understand if it is calculating the correct day or not so you can see the output value is Saturday let's do one thing let me do one thing okay so let me do one thing if I want to calculate the day of Christmas in the next here I'm going to put it as + 1 y let's translate this right click right click and then translate value it should be Friday this is Friday which is correct and let's say if I want to calculate this here what is the I can just remove the offset okay I'm just

[10:24] calculating the day of this date this year Christmas date right click translate value it should be Thursday right so this is how you can calculate the day of weekday for any given date so if you have any queries leave your queries in the comment box I'll try to respond to your queries please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you
