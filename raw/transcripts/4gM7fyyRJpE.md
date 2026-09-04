---
id: "4gM7fyyRJpE"
title: "TRICENTIS Tosca 16.0 - Lesson 45 | OBSTACLE#3 | Dynamically changing Table Elements – Not a Table |"
url: "https://www.youtube.com/watch?v=4gM7fyyRJpE"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 50
duration: 764
upload_date: "20240808"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:30:43Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 45 | OBSTACLE#3 | Dynamically changing Table Elements – Not a Table |

[00:13] hi everyone this is Ravi welcome to trien tasa Advanced Training till now I published 44 YouTube videos covering beginners intermediate and advanced level Concepts the past couple of videos I've started teaching you real time scenario and how can we automate your test cases whenever you encounter different types of obstacles so this is our third obstacle in this lesson I'm going to teach you how can we automate a test case when you encounter an obstacle where you have to interact with a dynamically changing table elements basically this is not a table but in your application this shows as a table and it has an objects within the cell which are dynamic in nature so you need to interact with those

[01:14] objects by using trient Tas so first let us understand what is the obstacle in detail so this is our third obstacle which is categorized as hard in nature so let's go for it so here let's assume your application under test generates an order ID every time you click on the button unfortunately it gets added to the table randomly the order ID gets added to the table randomly in any row find a way to automate a table test step that clicks on this button and buffers the value of your order ID generated within the table enter the same ID into the text

[02:16] box and now let's generate order ID here let's generate order ID I don't see any order ID in the table let's generate this so now you see your order ID is here third row from the bottom and your order ID is 10 14851 let me generate again so now if you see your order ID is in Middle now and your order ID is changed that means whenever you click on this particular button the order ID generates dynamically into any of the row now you need to capture this order ID and type the order ID in the text how can we do do that let's go back to trient tasar and let us scan your application right click on this folder click on scan application so this is my application click on

[03:27] scan so if you see here you don't see the table whatever we are discussing here right I don't see that so for that you need to expand the filter click on again one more time now you can see here this is your table see here Arana and then none AR none area busy and false area busy and false But If You observe closely see here this is not a table at all this is a container this particular table is under a parent container called div and these are all also containers see these are all containers and div containers right so now how can we capture this order ID so this is my order ID right here Order ID and this is my order ID so let's select this order ID here

[04:34] so if you select the order ID let's see the properties here because this order ID keeps on changing that means your inner text does not remain same so taking the property called inner text is wrong so that's why I'm going to uncheck this as soon as I uncheck now your object is not uniquely identified see here the selected object is not uniquely identified so then what we can do so in this case I can use identify by anchor method how what is the anchor if you see here this order ID whatever it is generating that is generating exactly in the same row where you have order ID as a text so whenever you generate every time this column and this column value goes hand in hand so that means I can uniquely identify this object by using the column order ID

[05:40] so let's select identify by anchor now I want to use this order ID as an anchor to identify this so for that you need to click on this and drag and drop onto anchor control see as soon as I drop now your order ID should be uniquely identified see now here my order ID is now uniquely identified so now let us rename this module with the obstacle ID right so this is my obstacle okay let's copy again copy this and paste it here but along with the order ID I also need to capture

[06:43] the button and the text so for that again go back to the filters and here this is my button which is uniquely identified and this is my edit box which is also uniquely identified right now save this module and close it so let's go back to trasa here this is my new module that has all the objects that we captured now let us create a new test case here on test case folder obstacle and name this as the same obstacle name sorry I need not to create a folder but I have to create a test case right click and select the test case paste it here now double click on this now I have to drag and drop my

[07:45] module onto the test case so now what is our actions sequence of actions my sequence of action is first I need to click on order ID right before before I capture the order ID here I need to click on button order ID generate order ID so but here the sequence of the objects are not proper so let me make them as logical order trag this and put it here so now click on this generate order ID button and then capture the inner text of this particular object so if you see here the object name is also not proper so it is a best practice to name the objects in logical manner because this order ID keeps on changing so I'm going to make this as order

[08:45] ID so now by default the object name also changes in the test case so here I need to capture the value into a buffer how can I do that I need to use use the action mode buffer and now I have to capture the inner text so for that click on this Arrow select inner text and I'm going to store this under order ID right done now I need to enter the order ID into text so here I'm going to call this buffer for that open curly braces capital b square curly braces order ID close Square braces and close curly

[09:46] braces so here now I'm entering the order ID from the buffer that I have stored that means I'm entering the value that stored under buffer called order ID so now let us mark this test case as complete now save this test case let us execute the test case and see what happens right click and run in scratchbook so it clicked on generate order ID and Order ID has been generated and see here 1081 1656 by8 so the same number it entered if you go back to your test results here here you can see your order

[10:46] ID 1081 1658 has been stored under buffer called order ID same thing we entered in the text box so now let let me execute one more time because whenever I click on this button this order ID generates dynamically in any row let's execute one more time and see if it is going to handle run one more time see now it clicked on order ID your order ID is changed unfortunately it is actually in the same row let me execute one more time quickly see it's clicked on button now your order ID is here not in third row

[11:47] still it is able to capture and 1069 786 10 69 786 so it is able to capture and type in into the edit box so if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how can we automate the test case where you need to interact with objects within the table that are dynamic in nature please do subscribe to the channel on Bell icon you'll receive notifications whenever I publish more videos thank you
