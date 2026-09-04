---
id: "uR569h8qSKg"
title: "TRICENTIS Tosca 16.0 - Lesson 52 | OBSTACLE #10 | Extract Text | XBuffer | Dynamic Text"
url: "https://www.youtube.com/watch?v=uR569h8qSKg"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 57
duration: 781
upload_date: "20240909"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:31:58Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 52 | OBSTACLE #10 | Extract Text | XBuffer | Dynamic Text

[00:13] hi everyone this is Ravi welcome to trient tasa Advanced Training as you all know I've started publishing series of YouTube videos covering some of the realtime scenarios where you might encounter different types of obstacles and how can we solve those obstacles by using trient tasa while automating your test cases this is our obstacle 10 in terms of real time scenarios and this is our lesson 52 in terms of overall trient tosa automation training so in this lesson I'm going to talk about how can we solve an obstacle where you need need to extract the text while extracting the text you need to exclude the dynamic portion of the text and you need to buffer the dynamic portion of the text and enter the buffered Dynamic portion

[01:17] of the text into an edict box so this is our real time scenario please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you this is our 10th obstacle which is named as extracting text and categorized as easy so now let us go for it so let us first understand what is the challenge that we need to solve for please automate a test step taking the total amount shown in the success message and enter it into the text box so so this is your success message that displays whenever you land land on this page and we need to take the amount from this success message and you need to enter the same

[02:22] amount in this edit box right as soon as you enter you solve this automation problem so here the challenge is whenever I say let me retry then your amount keeps on changing so here partial text from here to here and then from here to here is static and the amount is dynamic so we need to capture this Dynamic amount and enter in the text box if you enter the correct amount then your automation problem solves successfully okay so now let us go back to our trient tasa and as you all know we are capturing all the objects under obstacles folder so for that let's now let us right click on this obstacles folder select scan and application so

[03:25] that we can capture the objects that are required to automate our test case so this is our application select the application click on scan and Here If You observe closely I can see enter total amount edit box here right but I'm not finding this object purchase completed so I'm not finding this object to find that object let us expand the filters how by clicking towards right this one right and some more okay now if you scroll down here you can see enter total amount this is our edit box see I highlight see it's highlighting here this is our edit box and then sorry when I'm highlighting this

[04:27] see the edit box is getting highlighted now what is our static text our static text is this one which is div container okay so let's select this and let me highlight this okay let's highlight this one see this is the static text okay remove the Highlight now if You observe closely here when I select this one says the selected item is unique and also the edit box where we are entering the amount that is also identified uniquely but one change we are going to do here what is that for this this is dynamic message right where the amount keeps on changing that's why what I'm going to do I'm going to rename this as purchase completed message that is one thing and if you see the identify by the

[05:29] properties right I can see ID is selected and inner text also selected but this inner text keep on changing right let's say if I take this property then whenever there is a change in the message then tasar cannot identify the object so for that what I'm going to do I'm going to remove this in text I'm going to remove this inner text I don't want to consider this inner text property because because this inner text property keeps on changing I'm considering ID and tag let us make sure still this object is uniquely identified see even though I remove this inner text still my object is uniquely identified done now let's go back to the top and let's rename this module the best practice is to rename the module every time let's copy this obstacle name

[06:30] and paste here name the module with the obstacle name okay so now save this particular module we saved it close the module let's go back to Tri and tasa so this is the new module that we captured okay so I can see here I have purchase completed message enter total amount both now let us come back to our blue section test case section right click on this obstacles folder let's create a new test case and name this as obstacle name that we copied earlier double click on this test case now to create test steps what we need to follow you need to Simply drag this module and drop onto your test case to form the test steps now let's expand this so now what is is our

[07:30] first action we need to do we need to capture this message first right and once you capture this message you need to extract the only amount from the captured message for that what I'm going to do I'm going to start using inner text property how come here this is my object open the drop- down select inner text equal to what is the inner text let me copy this entire inner text copy this and then paste here now as I told you earlier here the inner text whatever the inner text we have here right here this entire this entire portion is static until dollar and this is dynamic and this

[08:31] entire portion is again static so that's why what I'm going to do here here I would like to replace let me do one thing here okay let me expand this so here this static part I don't want to touch I'm doing now this is your Dynamic part right so I would like to verify this entire text here okay I'm going to select the action mode as verified but because this is a dynamic portion I would like to exclude this Dynamic portion while verifying it but while excluding this Dynamic portion I would like to store this Dynamic portion to a buffer so how can we do that by using X buffer concept how let's go here this Dynamic portion I would like to replace with open curly braces XB is X buffer see this is XB that means

[09:37] exclude this portion and buffer this Dynamic portion into a buffer name called amount so that's why open Square braces amount close Square braces and close your curly braces verify this entire text while verifying this text I would like to exclude this Dynamic portion but I would like to store this Dynamic portion into a buffer that's why I'm using a method called XB if you want to just buffer then you are going to use just B capital B but I would like to exclude this portion and buffer this portion into a buffer name called

[10:38] amount that's why I'm using the method XB so now here I'm storing the dynamic portion into a buffer right now our next action is I need to enter the stored buffer value in edit box so for that simply call the buffer name called amount here open curly braces capital B open Square Braes this is my buffer name amount close Square Braes close curly bra done and your action mode is input so let's save this let me do one thing let me run this and see what happens okay right click and run in scratchbook see now can see

[11:39] here we have entered the same number here 10657 now let me run one more time just keep this in mind 15 3199 okay so let's close this one run this again right click and run 15 3199 okay so I mean it's it's very fast you are not even able to see what it entered but it entered correctly see 1531 99 okay so hope you all understand the concept right so here you can see here now let me see the test result here if you expand the test result what is the we are storing XB amount where see here we are excluding this 15 3199 here and the same amount we

[12:41] are entering here okay so if you have any queries leave your queries in the comment box I'll try to respond your queries
