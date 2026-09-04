---
id: "ZnmDHKg7rrY"
title: "TRICENTIS Tosca 16.0 - Lesson 69 | OBSTACLE #27 | Steering Parameter | ScrollingBehavior"
url: "https://www.youtube.com/watch?v=ZnmDHKg7rrY"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 74
duration: 663
upload_date: "20250107"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:34:55Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 69 | OBSTACLE #27 | Steering Parameter | ScrollingBehavior

[00:14] hi everyone this is Ravi welcome to trienes tasa automation tutorial as you all know I already published 68 YouTube videos covering beginners level intermediate level and advanced level concepts of automation by using BST TSA from few videos onwards I have started teaching you the realtime scenarios where you might encounter different types of obstacles and how can we mitigate those obstacles while automating the test cases please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you this is our lesson 69 in terms of overall tricentis Taska training and this is abstral 27 in terms of realtime scenarios in this lesson I'm going to

[01:14] teach you how can we solve an obstacle where you need to interact with an object like edit Box by using steering parameter and the scrolling Behavior techniques so now let us see in detail what is the obstacle that we are going to solve for so this is the obstacle list that we have started working on from few lessons onwards so in today's lesson we going to start working on scroll into view obstacle which is categorized as medium let's go for it so here you can see the obstacle enter toss into the text box then submit text appears once text box is out of visible area so you can see here now it is not very

[02:15] straightforward text box to enter the value what we need to do is so this edit box is blocked by an i frame okay if I scroll scroll down to the bottom now I can access this edit box if I enter the text as TSA in edit box and submit it that means you solve the automation problem successfully so basically you cannot enter the value directly into this edit box so this edit box is being blocked by another object so to enter the information into the edit box you need to scroll down to see the text box and then enter the text task so this is the

[03:16] problem that we need to solve so now let us jump onto the prenta and start automating the test case so as usual in module section we are storing all the objects that are required to solve the obstacles so here we going to scan the objects that are required to automate today's obstacle what we need to do right click on this obstacles folder select scan application so this is the application that we would like to scan so I'm going to click on scan so here you can see I have a text field where we'll be entering the tasa

[04:16] as a text select this one and also I have another object called submit button which I need to click on where I'll be submitting the text that I have entered so if You observe closely see this text field is under HTML document basically this is under iframe and then HTML document under HTML document you have a text field that's why this text field is actually blocking by another object as well by an another object okay so now let us rename this module with the obstacle name copy and then rename this module renaming the module is very important so I'm renaming the module with the obstacle name and now save the

[05:26] module and then close your X scan so let us go back to our trient tasa now if you scroll down so this is the one that we have scanned just now obstacles double click on this so now you can see there is a submit button and there is a text field now let us create a new test case so that we can automate the test case come to the come to the left side of the blue section which is test case section right click on this obstacles folder and then select create test case and name this as with the same obstacle name now double click on this so to automate the scenario that I have explained you right you have to first scroll down and then enter the text so to perform scrolling operation we have to do some modification to our object properties what we are going to do come

[06:28] to text field for text field you have to open the properties by clicking on by clicking on this Arrow Mark okay open the properties so what we need to do we need to add a property to the text field scrolling Behavior property what is that property steering parameter property so if you see here these are all the properties of this text field now I would like to add a steering parameter what is that right click on this text field and this is your steering parameter create steering parameter select this now you need to now you need to rename this as scrolling Behavior scrolling Behavior the spelling should be same you should have capital S capital B and there is no space scrolling behavior and

[07:29] this scrolling Behavior we can provide four different values one is top bottom center or none okay in our case to get our text box to the focus our text box should be at the top so that means your scrolling behavior of this text field should be top so what I'm going to do here I'm going to specify it as top scrolling Behavior top now save the changes so now let us start automating the test case so this is my test case to automate the test case you need to drag and drop the module onto the test case now first what we need to do we need to enter the value to the text field so I'm going to enter a value as

[08:31] tasar as we already provided the steering parameter as stop now you need need not to perform any scrolling operation okay so that is important and now again I would like to drag this and drop here onto the test case and here I would like to click on submit button so let me so let me rename these steps I'm going to rename this as enter text and this click submit right now save your test case and let us Mark the test case as completed now let's run the test case and see how it works before that I would like to just click on try again so that application state will be ready

[09:32] for execution ready for execution now let's right click and run the test case in scratchbook see it entered the text you can see here it scroll down as well as it entered see here it performed the scroll down how it is performing scroll down by using the scrolling Behavior top so the edit box moved to the top and then it entered the text so this is how you can solve an obstacle which involves this scrolling behavior and steering parameters so if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how to solve an obstacle where you need to interact with an object by using the

[10:33] techniques like steering parameter and the scrolling Behavior Concepts please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you
