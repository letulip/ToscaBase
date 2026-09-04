---
id: "NnuHH_OkwpA"
title: "TRICENTIS Tosca 16.0 - Lesson 57 | OBSTACLE #15 | While Loop | Multiple Interactions"
url: "https://www.youtube.com/watch?v=NnuHH_OkwpA"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 62
duration: 669
upload_date: "20241003"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:32:56Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 57 | OBSTACLE #15 | While Loop | Multiple Interactions

[00:15] hi everyone this is Ravi welcome to trienes tasa Advanced Training as you all know I already published 56 YouTube videos covering beginners intermediate and advanced level Concepts from couple of videos onwards I've started teaching you the realtime scenarios where you might encounter with different types of obstacles and how can we solve those obstacles by using trient tasar so this is our obstacle 15 in terms of realtime scenarios and this is our lesson 57 in terms of overall tricentis tasa training please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank

[01:15] you in this lesson I'm going to teach you a realtime scenario where you need to solve an obstacle by using the methods while loop and multiple interactions so now let us see what is the obstacle in detail so here is our obstacle again and again and again this is categorized as medium let's go for it so what is the obstacle that you need to solve in order to complete this obstacle you need to click the button labeled click me after few clicks the button will change to enough and then again click that button to finish the exercise so you need to click this click me button once second time third time fourth time see now after four clicks this Chang it to

[02:17] enough now you click one more time now your automation problem solved so let me retry and this button turns to enough not only for the fifth time so it is dynamic it might turn after one click or it might turn after three clicks so it is dynamic so again let me try one two see now this button turned into enough after two but after two clicks click now your automation problem solved so how can we solve this for that let's go to tasa and this is my trient tasa and this is the obstacle folder where we are scanning all our objects pertaining to each obstacle so right click on this folder click on scan and select

[03:49] scan and here I would like to capture an object of clickme right click me is the button so this is the button I would like to capture select this button and then rename the module with the name of your obstacle so let's go back here copy the obstacle name and then here paste the obstacle name here and now we completed capturing all the objects that are required to solve the obstacle now save this one and then close your xcam so let us go back to trentos so this is the the new obstacle that we captured which has only one object right so now let's now concentrate on left side blue section which is creation of test cases right click on obstacles folder create new test case and name this as the same name that we copied

[04:51] earlier double click on this now to automate the test case simply drag the module that we capture and drop onto your test case so now what we need to do we need to click on this button multiple times until the button turns into enough so how can we achieve this we can achieve this in different methods but the appropriate method is using while you can use if condition you can use do conditions right but in this case the appropriate method is to use while condition okay so now what I'm going to do here I'm going to right click on this particular test case and then I'm going to start using this is my create while statement and now I'm going to bring

[05:53] this to the Top This is my vo statement here what is the condition my condition is you have to click this button until the button title is Click me now I would like to copy this same module or you can use the same module drag here and drop on to the condition right so what is the condition my condition is the inner text the inner text of this particular button equal to click me click me right so you can see here now this is my capital letters click me and here I would like to verify this I want to verify if the inner text of this button is Click me or not so if this condition is meeting that

[06:55] means if this condition met then I would like to click on the button so that's why again I would like to use the same button under Loop that means once this condition is satisfied it enters into the loop what it is going to do it is going to click on the button so I'm clicking on the button until this condition satisfies so what it does it enters the loop it again comes back it checks for the inner text click me then what happens again it clicks so like that it keeps on repeating until the inner text changes to enough if the ner text changes to enough it comes out but what we need to do once it turns into enough again you need to click that's why I'm adding another new Step here basically I'm keeping the same old step here and then I'm going to click another time that's it so let me explain

[07:59] one one more time okay so what we are doing we are using the same object again and again I'm using this object to verify the condition if the inner text is Click me and then I'm entering into the loop it clicks on the button again it checks the condition if it meets again it clicks again checks the condition if it meets it again clicks so again comes back if this does not meet the condition then comes out of it and it clicks once and then your test case is done so now let us change the test case status or work status as completed and now let's save this particular test case and let us run this test case right click and run in scratchbook

[09:04] so it is clicking once twice three times see now enough is changed it changed to enough and it clicked one more time your automation problem is solved let me again run again okay let me run again to see if while condition works correctly or not okay so right click and run in scratchbook so this time your button might turn into enough within two clicks or three clicks let's see if it handles so it's clicked once twice done so it turned in and then it again clicked now your automation problem is solved so hope you all understand the concept of solving the obstacle by using while condition right so anytime if you encounter this kind of

[10:05] scenarios you need to use while condition for interacting multiple times with the same object oh you all understand the concept to solve an obstacle where you need to click the button labeled click me how many times we need to click that we need to click few times the same button until the button name changes to enough we have used the concept of while loop and multiple interactions to solve this obstacle please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos don't forget to like and share the video thank you
