---
id: "dAx-dE1xf-I"
title: "TRICENTIS Tosca 16.0 - Lesson 59 | OBSTACLE #17 | Dynamic Date Expression | Tomorrow’s Date"
url: "https://www.youtube.com/watch?v=dAx-dE1xf-I"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 64
duration: 565
upload_date: "20241017"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:33:16Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 59 | OBSTACLE #17 | Dynamic Date Expression | Tomorrow’s Date

[00:13] hi everyone this is Ravi welcome to tric Centrist tasa Advanced Training as you all know I have already published 58 YouTube videos covering beginners intermediate and advanced level Concepts from couple of videos onwards I've started teaching you the realtime scenarios where you might encounter with different types of obstacles and how can we solve those obstacles while automating your test cases by using trient tasa this is our obstacle 17 in terms of real time scenarios and this is our lesson 59 in terms of overall tricentis TSA training please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you so in this lesson I'm going to teach you a real time scenario where you need

[01:16] to solve an obstacle by using Dynamic date expression in the scenario we need to enter tomorrow's date in an edit box and where we'll be using the methods like Dynamic date Expressions so let us go to our obstacles list and see what is the obstacle that we need to solve for this is my obstacle which is named as tomorrow and categorized as easy let us go for it so here is the obstacle in order to complete this obstacle you need to input tomorrow's date in the text box so this is your text box you need to enter tomorrow's days tomorrow's date so what is our today's system day so you can see here at the bottom my system date is 13th October 2024 which means I need to enter tomorrow's datee which is 14th October

[02:19] 2024 right so it's dd.mm.yy y format so what I'm going to do here 14 dot 10 do 2024 see as soon as I enter tomorrow's date your automation problem is solved okay so how can we achieve this one let us go to Tri andest tasa and and as usual we are going to capture the objects for this particular obstacle in this folder obstacles folder right click scan select application so this is the application

[03:21] that we would like to scan select the application and click on scan for this obstacle we need to capture the edit box right so go here and this is my and this is my edit box where I'll be entering the date tomorrow's datee select this and now let us go back to our obstacle copy the obstacle name and then name the module as obstacle name so this is the only object that we need right now let us save the module and close X scan go to trient tasa you can see here this is your

[04:23] obstacle module that we captured so let's go back to again left side section which is test case section and this is where we are creating all the test cases for each and every obstacle that we are working from past 16 YouTube videos so here right click on this obstacles folder create test case and name the test case with the same obstacle name that we copied earlier double click on this and now to automate our test case we need to drag the module that we captured drag and drop onto your test case so here to enter tomorrow's date as I told you as I told you what is our system date our system date is 13th October 2024 so here what we are going to do we are going to use the date Expressions Dynamic date

[05:24] Expressions open curly braces enter date so you you can see here the syntax date and time values can be calculated by using base date we can calculate any date by using base date along with some deviations that you can display them in user defined format so you can see here this is your date function you need to specify the base date if you have any base date you can specify sample base date like this but if I don't specify any base date is going to take your system date you can leave this blank and then you can use offset offset in our case our offset is + one day plus one day and then what is your format my format is dd. mm. y y y y right that is our obstacle right so here you need to enter dd.mm.yy y y okay I

[06:26] can use that format here okay so now let's go back here now select this and then what is our base date our base date is system date I'm going to leave this as blank and then specify your offset within square brackets what is the offset what is the offset + 1 D Plus 1 day that is my offset and again specify the format within Square braces what is the format DD do mm do y y y y this is my format and then close curly braces as soon as you click somewhere else see now you this particular this particular date expression is correct to validate the date expression you can right click on the expression translate the value let me translate

[07:27] this see here now now my system date is 13th October and this is displaying 14th October 20124 in the format that we require right now let us change the work state as complete and now let's save the test case and let me run this particular test Quest right click and run in scratchbook see it entered 14 October 2024 and you solve this automation problem successfully so this is how you can calculate the date so this is how you can calculate

[08:28] the date as per your requirement by using date Expressions Dynamic date Expressions so if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand the concept how can we solve an obstacle where you need to enter tomorrow's date in an edit Box by using the concepts called Dynamic date expressions and calculate tomorrow's datee please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you
