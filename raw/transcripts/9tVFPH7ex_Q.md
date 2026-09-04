---
id: "9tVFPH7ex_Q"
title: "TRICENTIS Tosca 16.0 - Lesson 66 | OBSTACLE #24| Escape Values | Click Method"
url: "https://www.youtube.com/watch?v=9tVFPH7ex_Q"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 71
duration: 474
upload_date: "20241125"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:34:27Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 66 | OBSTACLE #24| Escape Values | Click Method

[00:12] hi everyone this is Ravi welcome to trient tasa Advanced Training as you all know I already published 65 YouTube videos covering beginners level intermediate level and advanced level Concepts from couple of videos onwards I've started teaching you the real time scenarios where you might encounter different types of obstacles and how can you solve those obstacles while automating your test cases by using tricentis TSA please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you this is our lesson 66 in terms of overall trient task Advanced Training and this is our obstacle 24 in terms of real time scenarios so in this real time scenario we're going to solve an obstacle where you need to pass the click

[01:13] method in trient tasa but while passing the click method you need to use the Escape values so that you can input the string as it is in the edit box instead of per performing click method so now let us see in detail what is the obstacle that we need to solve for so this is our obstacle list and our obstacle name is escape and which is categorized as easy let's go for it it says input the value open curly braces click and close curly braces into the text box that means you need to Simply enter open curly braces click close curly braces so once you enter that entire text or string that means you solve this problem whenever

[02:15] you provide this keyword as an input in tasa tasa understands that you're actually clicking on this edit box so if you pass this key in tasa as an input value then it's going to Simply come here and click on this box so then how can I enter this text in this edit Box by escaping click method so that's what we are going to see let us go to Tria let us go to trasa as usual we are going to scan the objects pertaining to this obstacle under obstacles folder right click can application and this is my application select the application click on scan and here I just need to capture

[03:19] this text box result text select this and make sure this object is uniquely identified yes this is uniquely identified now let us name the obstru module as obstacle name copy and name this obst and name this module as obstacle name and save it and close xcam so let's go back to trient tasa and you can see here this is your new module that we scan it should has it should have result text so now let us come to the left part of test case blue section so let us right click on this obstacles test case folder as usual I'm going to create a new test case here and name this as the obstacle name and then double click on this now

[04:19] to automate the test case we are going to Simply drag the module and drop onto test case and here so what is the obstacle I need to pass the value open curly Braes click close curly Braes into this text box generally what we do to enter any value let's say username if I provide this username let's say username usern name if I pass this value as username if I run this what it does it's going to enter username see it entered username but our automation challenge is not that we need to pass open curly braces click close curly braces if I pass this particular key and if I run this is it going to type open curly braces click close curly braces

[05:26] no see it is just going there and it is performing click operation instead of enter in the text or string so how can I solve this problem now so there are two ways one is you can simply right click on this and you can use Escape Value method as soon as I enter this Escape value see it is taking as a string by using double Cotes at beginning of this string and at end of the string I go here just specify the double codes here that means it's going to escape the keyword open is going to escape the click operation and it considers as a string input value so whenever you right click and then select Escape value it's going

[06:27] to escape the keyword method click operation and it considers as a string now I would like to run this particular test case right click so before run I would like to change the work state as completed save the test case right click and run in scratchbook see your automation problem is solved it entered this string entire string open curly braces click and close curly braces instead of Click operation so this is how you can solve the problem by using Escape Value method if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand the concept of this real time scenario where we solve an obstacle by using the Escape values concept

[07:30] while performing click method in tricentis tasa please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you
