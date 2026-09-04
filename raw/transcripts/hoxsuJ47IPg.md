---
id: "hoxsuJ47IPg"
title: "TRICENTIS Tosca 16.0 - Lesson 43 | OBSTACLE#1 | IDs are not everything – Elements with Same IDs"
url: "https://www.youtube.com/watch?v=hoxsuJ47IPg"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 48
duration: 697
upload_date: "20240805"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:30:22Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 43 | OBSTACLE#1 | IDs are not everything – Elements with Same IDs

[00:13] hi everyone this is Ravi welcome to price and Taska Advanced Training till now I published 42 YouTube videos covering basic level Concepts intermediate level Concepts and advanced level Concepts from this lesson onwards I'm going to start publishing 40 different YouTube videos to cover some of the realtime scenarios while automating the test cases by using trient Taska basically in real time when you are working on a project in an organization you're going to face lot of obstacles while automating your test cases so I'm going to start publishing the YouTube videos to show you how can we automate the test cases whenever you encounter

[01:14] different types of obstacles in real time please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you this is lesson 43 in terms of percentage Taska overall training or this is lesson one in terms of realtime scenario automation so in this lesson I'm going to teach you how can we automate a test case when you encounter an obstacle with elements with same IDs let's first understand what is the obstacle and how can we solve that obstacle to automate your test case let's go back to our Chrome browser so this is your obstacle list that is provided by trient tasa I'm going to leave this URL in the comment

[02:16] box so that you can access this obstacle list so what is our first obstacle my first obstacle is this one so what does this obstacle means so we have to automate a test step that clicks on the button labeled click me if you see on the screen you have two buttons one is don't another one is Click me so these two buttons are on the screen and you need to click on click me right side button so here these two buttons have similar IDs and and how can we solve by using trient tasa to automate this test case so this is my trient tasa and here we're going to start scanning the application so I have created a module called obstacles so

[03:17] it's not a module it's a folder within the module so now I'm going to right click on this obstacles and then start scanning the application so here I'm going to select the application that I would like to automate so this is our application right so where we have to solve this problem and click on scan so let me expand this one if you see on the screen we have two buttons one is don't and click me right so these two are those buttons don't and click me if you select this click me you can see the properties of that button if you see the properties of that button ID is the property do not use ID and it also having a tag as the property right it is

[04:18] identifying this clickme object by using these two properties let's go and see don't button this don't button also have ID and and tag and if You observe closely the ID property is same as this earlier click me button do not use ID whereas in Click me button also has do not use ID that means if you capture this particular object by using tasar it's not going to uniquely identify let's select this click me button and if you see here this is highlighting in orange color that means the selected item is not unique so what should we do to make this button unique so there are two ways one is either you can start using

[05:18] the inner text if you see here this is your inner text for this what is the inner text click me let's go and see in don't button for don't button your inner text is don't that means I can add an additional property called inner text to make this button unique so let's add this okay let's add this inner text as soon as I add now you see here the selected item is unique that means now the selected item is unique whenever you have multiple objects objects having the same property you can use an alternative property to identify the object uniquely and here you can also expand the filters here to see their

[06:19] parent objects as well there is another way where you can also use the parent object but that concept I'm going to cover in our upcoming lessons so for now let's go with the alternative property to identify the object uniquely so now let us rename this module as obstacle name as same as your obstacle name the obstacle as225 so I'm going to play paste this one so it's good practice to rename the module so that you can identify the module easily and here your button name makes sense I need not to rename the button name if you want I can rename the button as well so the best practice is you should have the naming convention in a such a way that you

[07:20] should be able to identify the objects or naming of the objects very easily now let us say save this as soon as I save a module will be created and close this now let's go back to present stasa I can see here now click me button is added under a module called obstacle # 22505 so now let us create a test case for this right click and then create a folder called obstacles obstacles now under this folder let us create our first test case and then name this as obstacle # 22505 and now let's drag this module and drop

[08:25] here and now here to click this particular button on screen right there are two ways either you can select click keyboard option so what it does this actually takes the keyboard action that means it uses the mouse to click on that particular button so which is not recommended because it is very time consuming and your performance of the application comes down your performance of the tasar comes down and it is very slow so tritis recommends to not use click function here instead you can use this one you need to pass X to click on any object and now let us run this

[09:27] particular test case and see it's going to click on the button which is on the right side so just right click and run in scratch so now it's clicked on the button but we could not understand it clicked on which button right I can do one thing I can introduce click option here right click what it does it actually moves the cursor onto the button so that you can understand it is clicking on which button let's run this again so now you can see it is clicking on click me button so your automation problem is

[10:27] solved so you can you can see here your test results are passed so once you complete your test case design and automation it's a best practice to use the workstate column to mark it as completed and save your test case so this is how you can solve the challenge of elements that are having the same property if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how can we solve the challenge that you may encounter in real time while automating your test cases please do subscribe to the channel click on Bell icon you'll receive notification whenever I publish more videos thank you
