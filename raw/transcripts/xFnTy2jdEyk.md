---
id: "xFnTy2jdEyk"
title: "TRICENTIS Tosca 16.0 - Lesson 46 | OBSTACLE#4 | Dynamically Changing ID Property |"
url: "https://www.youtube.com/watch?v=xFnTy2jdEyk"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 51
duration: 694
upload_date: "20240812"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:30:54Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 46 | OBSTACLE#4 | Dynamically Changing ID Property |

[00:12] hi everyone this is Ravi welcome to trien tasa Advanced Training as you all know I have already published 45 YouTube videos covering basic level intermediate level and advanced level Concepts from couple of videos have started publishing the realtime scenarios where you might encounter different types of obstacles and how can we solve those kind of obstacles by using trient TSA while automating your test cases this is our lesson 46 if you like the video please do like and share the video and don't forget to Subs to the channel so that you'll get notifications whenever I publish more videos thank you in this lesson I'm going to teach you a realtime scenario where you need

[01:13] to interact with dynamically changing ID property elements let us see what is the obstacle that we need to solve for so this is our fourth obstacle which is is two times so let's go for it so use one module creating two automated steps to click the button two times in a row sounds easier than it is so what do you mean by that so here whenever you click this button for the first time right so if you see the button name is Click me tox as soon as I click on this button see now your button name is changed click me once more right so once I click one more time that means your automation job is solved or your

[02:15] challenge is solved so let's try this again okay so you have a button once you click on this button it changes the name of your button so that's why the name of the button and property of the button gets changed for the second time so you need to click this button another time then you solve this automation problem right for that let's go back to tricenter stasa and as usual let's scan the application by using the folder obstacle right click on this folder scan click on application and this is our application select the application click on

[03:26] scan now let me maximize the window and what is the button the button is Click me 2x so this is the button that we need to click twice but the button changes let's see what is the properties of this button if you see here the property of button is you have some numeric portion _ 4 6576 right so remember this and then tag a you have numeric underscore sorry it's it's not numeric you have a characters underscore numeric value 4 657 six so let me close this I don't want to save this I just want to close this and let me click this button one time right now let me rescan this particular application right click click on

[04:29] application and select the application click on scan so if you see the button now and the properties of button now your button name is Click me once more let's see the property of this button so you can see here the property of button has changed see here numeric sorry your alphabets underscore now your numeric portion got changed 84 68 so how can we solve this this particular challenge to click the button twice so for that let's close this again so let me just click on this and then let's try this again okay so now let us go back to our trient tasa and now let me scan the application I would like to capture the object at initial

[05:30] stage itself before you click the button for the first time right click on scan and here let's select the button click me 2x as I told you the button has an ID and this ID gets changed to the another numeric portion here after underscore so that's why I cannot keep this as is instead remove that changing portion of your property and replace with hasri which is a regular expression this regular expression hasri is used Whenever there is a dynamic portion this can handle rmd uncore after that after

[06:33] underscore you can have any alphabet or numeric portion it doesn't matter it recognize the object even though you have any number or any character after underscore so I would like to replace that static value with a regular expression hasri and click on Okay so done now let's rename this module with the name of your obstacle this is my obstacle name copy this and rename this so it's a best practice to rename the module so that it makes a logical sense okay so now let's save the module so close your X scan so let's go back to

[07:34] renasa now you can see this is my new module that I have scanned click me 2x so let me create a new test case now under obstacle folder right click create a test case name this as your obstacle name double click on this so now let me drag and drop the new module that we scanned drag and drop here so here for the first time you need to click on click me 2x right for that pass this x now again I want to click on this same button right but the button property gets changed drag this same module and drop into the same test case one more

[08:35] time and here I would like to rename this as click button once more and this step is Click button for first time right so here again for the second time pass X so now this is done now let's save the test case and mark the test case work state as complete completed right and now let me run this test case and see if we can click the button twice see it clicked on once it clicked second time I would like to do one thing okay so let's do one thing let's go back here I would like to use the some other click function so

[09:37] that you can see whether it is clicking or not I would like to use click function which uses the keyboard action so that your cursor will be placed onto the button so let's run this again one more time see your cursor moved to the button and it clicked one more time so that means now you solve this automation problem so whenever you are automating your test cases during that time if you have any dynamically changing ID properties dynamically changing partial text value or partial value of your ID then you can solve the problem by using this approach this is medium level

[10:37] obstacle but going forward we'll move to hard categorization of obstacles so if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how can we solve an obstacle while automating your test cases where you have to interact with the elements for which the element properties are dynamically changing please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos please do like and share the video thank you
