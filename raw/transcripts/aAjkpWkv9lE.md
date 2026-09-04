---
id: "aAjkpWkv9lE"
title: "Tosca Tutorial | Lesson 136 - Click On Screen | XModules | Screen Width | Obstacle 30 |"
url: "https://www.youtube.com/watch?v=aAjkpWkv9lE"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 476
upload_date: "20240222"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:49:12Z"
status: "raw"
---

# Tosca Tutorial | Lesson 136 - Click On Screen | XModules | Screen Width | Obstacle 30 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation Playlist. So continuing with our obstacle topic, let's look at our next test automation obstacle which is called RedStripe. Now here what we need to do is we need to click on the button which is label generate this button, okay. So once we click there, a number appears on the below, in this case it is 62. And then this particular number, it informs you how far to the right from the edge of the screen the RedStripe appears, okay.

[00:48] So there is a RedStripe on the screen, you can see it is appearing and this number is telling you how far to the right this particular RedStripe is appearing on the screen. So this particular value which is displayed, it is nothing but the percentage of your screen width, okay. Now what we need to do is we need to click on the RedStripe which appears on the screen, okay. So if it appears here, I need to go ahead and click here. And once I do that, then the automation obstacle is completed, okay.

[01:23] So we need to do this using Tosca. So let's see how we can automate this particular automation obstacle using Tosca. So coming back to our Tosca Commander and here let's go ahead and scan this particular application now, okay. So I need both the objects, first the generate button and then I also need this particular object which displays the number, right.

[01:55] So here we can see that the okay button is displayed so I can select that and that will get added into the module but I don't have the particular number which is displayed below the button, right. And that particular element is currently hidden. So what I can do is I can increase the filtered items level, okay. So let's go to the next level. Still I cannot see that and let's go one more level down. And now you can see this is the div element, okay.

[02:26] So this is the number which is a div element and when I select this, the item is unique. And if I go through the properties of this div element, you can see it has got an ID through which it can identify this and the inner HTML contains the number, the outer text as well contains the number and as well as the inner text, okay. So all these properties have that particular number. So once I identify this particular element, I can get the property value and that will contain that particular number, okay.

[03:02] So those are the two elements which we require in this particular module. So I'm going to rename this module and then let's save it and we'll close this. Now we'll go back to our Tosca and we are going to create a new test case here, okay. And then we are going to add the module right here, okay. So let's look at the test steps now. So the first step is obviously to click on the generate button.

[03:36] So you know we can do that using X or the click method. Here I will use the X, okay. And now we need to extract the number from this particular div element, okay. So for that we can use the action mode buffer and then we can get the inner text value and put it into a buffer which we call it num, okay. So that particular number which is displayed will be stored in this particular buffer and we can use that later.

[04:10] Now this particular step, okay. So it will click on the generate button and then it will grab that particular number. So now the remaining part of the automation is to click on the red stripe once it appears, right. So for that we need to use a different module, right. So let's go ahead and search for click on screen module, okay.

[04:40] So you can see this is the module which we can use, okay. It is part of the tboxx engines HTML and here you can actually pass the XY coordinates to click on a particular part of the screen, okay. And there are two methods. You can see one is HTML and one is related to mobile. So we need to select the HTML module, okay. So once you do that, you will see the click on screen, it has got three attributes.

[05:10] One is caption, one is the X coordinate and one is Y coordinate, right. Now the caption is basically your screen or your application title. So here you can see it is tracentous obstacle codes. So I can give the same here, okay. So I'm not going to type the whole title here. I'm going to put a regular expression which can cover the remaining part of the title. So that becomes my caption. And then the X and Y coordinate could be the number, okay.

[05:45] So the buffer which we have stored, so we are going to get that buffer value now here. And we are going to enter it, okay. So basically we can choose the X coordinate which is basically the width which is displayed as the number. But Y coordinate you can put any value but it will be better if we use the same value so that it clicks on a particular point in your screen.

[06:15] So this will basically complete your automation obstacle. Now I will mark this as completed. And let's see whether it is able to click on the button or not, right. So let's go ahead and bring this to the initial state. So let's go ahead and run this in Scratchbook. So as you can see it clicked on the generate button and then the 17 number appeared which means the width of the screen is 17.

[06:50] And then it went and it clicked on the red stripe, okay. So it took the width and it took the height as well, okay. So it was the same number. But as I said you can put any number for the height or the Y coordinate. But the X coordinate should be your number which is generated by the application. So this way you can use the click on screen module which is part of the T-Box extension to pass the X and Y coordinates and then you can click on any particular coordinate on your screen depending on the width and height, okay.

[07:27] So this is one more way of using the click method. Apart from using the regular click method you can also use the click on screen method whenever it is required as per your requirements. That's all for this particular video. If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
