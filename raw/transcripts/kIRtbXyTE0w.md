---
id: "kIRtbXyTE0w"
title: "TRICENTIS Tosca 16.0 - Lesson 44 | OBSTACLE#2 | Duplicate Elements with Same Properties |"
url: "https://www.youtube.com/watch?v=kIRtbXyTE0w"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 49
duration: 617
upload_date: "20240806"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:30:33Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 44 | OBSTACLE#2 | Duplicate Elements with Same Properties |

[00:13] hi everyone this is Ravi welcome to tricentis tasa Advanced Training as you all know I've already published 43 YouTube videos covering beginners intermediate and advanced level Concepts so in my previous video on words I started teaching you some realtime scenarios how can we automate your test cases whenever you encounter different types of obstacles while automating your test cases by using trient Tas this is our second lesson pertaining to real time scenarios in this lesson I'm going to teach you how can we automate your test case when you ENC cter an obstacle where you have a duplicate elements with same properties same multiple properties so let us go back to our

[01:14] Chrome browser let us understand what is the obstacle that we are going to solve for so we're going to solve our second obstacle which is automate a test step that clicks on the button labeled I am the one the second one on the right hand side I can see I am the one I am the one there are two buttons with the same name so we have to click on the button which is located on right side for that let's go back to trient Tason and here let us scan the application and the objects that are required to automate so here let's right click on obstacles folder click on scan and select the

[02:14] application so here is our application let's select the application and click on scan so let me maximize this and if you see here there are two buttons or two links I am the one I am the one so we are interested in these two buttons let's check the properties of these two buttons the first button on right side which is using ID and tag and ID is ID tag is a let's go back to another button which has an ID property as ID and tag as a value so that means both the properties are same and let's see what is the inner text it says I am the one your inner HTML says I

[03:15] am the one your inner text says I am the one let's go back here so even this button has same inner text and all other properties are same so in this case how can we solve automating our test case so there are two methods so if I select this button here now you can see this says your selected item is not your so how can we make these buttons as unique buttons there are two ways the first one is by using index go to identify and select index so if you see here the first button has an index of null and second has an index of two if you see here the selected item is not unique as soon as I

[04:15] select this so now your button is uniquely identified but I don't want to use that method because what if in future you introduce another button in middle or somewhere right side then what happens the index of this button becomes three that means your test case is going to fa so what we can do there is another method we can use the parent object to identify this button for that we have to expand the filter to see additional objects let's go and expand here expand some more but here if you see this button is under I am the one and this button is under I the one container so basically this is one container and this is another container let's see if these containers are uniquely identified

[05:17] if you select this container let's go back to identify by properties so here the container pertaining to the first button has ID this is this one is the right and let's see the container pertaining to the other button here this one this one says the inner text is empty that means these two containers are uniquely identified the first button has an ID this is the right and this one has an IDE of empty so that means I can use the container parent container to identify this particular button let us

[06:18] select this parent container as soon as I select so now it says you I am the one button is uniquely identified see whenever I remove this here see this is not uniquely identified if I select this container now your object is uniquely identified so now let us rename this particular module as the obstacle name copy and here rename this it is a best practice to rename your modules in a logical way now let's save this particular module and close this let us go back to trient TOS so this is our new obstacle module and here I can see this button so now let me

[07:21] create a new test case here right click and create a test case name this as abstract 1 129 Y2 and here let's double click on this test case and I would like to drag and drop this module onto the test case and expand this so it is very easy for us to automate this test case once you solve the unique identification of the object so here you can see it has a container also and it has the button so this particular button is under a container called this one and which is uniquely identified right so here to click on this button I would like to use again click which is not recommended you need to use x but I want to see the cursor so that I can

[08:22] observe closely on which button we are clicking by using this particular test case so now let us run this particular test case and see if we can click on the button which is on right side see it is clicking on the button which is right side good job you solve this automation problem so you can see the the test result here your test result is passed once you complete automating the test case it's best practice to mark this as completed and save this hope you all understand how can we solve the obstacle where two identical objects having same

[09:24] properties if you have any queries leave your queries in the comment box I'll try to respond respond to your query oh you all understand how can we solve our second obstacle whenever you try to automate your test cases by using triena where you have multiple objects and both the objects has the same properties please do subscribe to the channel click on Bell IC on you'll receive notifications whenever I publish more videos thank you
