---
id: "Hy7xq4YP-Eo"
title: "Tosca Tutorial | Lesson 6 - Identify Controls By Anchor | Scan Modules |"
url: "https://www.youtube.com/watch?v=Hy7xq4YP-Eo"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 634
upload_date: "20221125"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:32:59Z"
status: "raw"
---

# Tosca Tutorial | Lesson 6 - Identify Controls By Anchor | Scan Modules |

[00:00] Hey everyone, welcome again to another interesting lesson in this Tosca Automation course. Today, we are going to talk about a new identification mechanism provided by Tosca. Now, until now, all our controls which we have used in earlier sessions have been identified by the properties present in the web application. But what if two controls are present in a web page which have got similar properties and you cannot find a unique property to identify a particular control.

[00:35] Now this is a very common scenario which you will face while automating any web application. So Tosca provides you a way of identifying your controls in different ways. So identifying by properties is just one mechanism. There are many other mechanisms which are present in Tosca in order to help you to identify controls uniquely on the web pages. So let's look at an example on how a control can look similar to another control having the same properties and why you cannot identify it uniquely using the properties.

[01:15] So for this, I have gone to google.com and if you look here, there is a button called Google search. So if we type anything here and now we want to click on this Google search button. So this is our scenario, a very simple scenario. But what will happen is when you try to automate this, you will find that Google search is not unique. Now how I can tell I will show it in Tosca, but before that I can also show it using the inspect element, right?

[01:50] So when I do inspect on this and I can show you using the properties that this particular value or this button is not unique, right? So let's see. So this is the input class right and it has got a value Google search. You can see there is a name which looks like a unique right and let's try and used it. Okay, so I'm going to manually type this X path so that we can see that this is not a unique control, right?

[02:25] So I'm going to say at name equals BTNK right and ideally this should be identified using this X path. But if you look carefully, there are one of two controls using the same X path, right? So if although it's not visible on this page, there are two controls having the same properties which are exactly similar. So it's very difficult to uniquely identify this Google search button, right?

[03:00] One way is you can use the index right index of this button to identify this. The other way around is to use a anchor. Now anchor is basically a control which is present within the range of this particular control which you are trying to identify, right? So it's basically a relationship with this button, right? Anything which is unique within the range of this particular button, right? So I can either use this text box as a anchor or I can use this another button.

[03:35] I am feeling lucky as the anchor for this particular button, right when we come to Tosca. Okay. So let me go ahead and scan this module and show it to you how it looks like. So I am going to create another folder here. So let's go ahead and scan our application. So right click on the folder and select scan select application.

[04:07] Now select the application which you want to scan for us. It is the Google Chrome with the Google web page. So select that and click on scan. Now this opens the basic view window where I can select my controls and add to my module, right? So I'm going to select this text box and this Google search button, right? Now once I do that, you will see a orange highlighted bar on the Google search button, right?

[04:38] And that will tell me that this particular button is not unique, right? So this item was not uniquely selected by Tosca using the properties which are present on the web page. Now to look a bit deeper, we need to go to the advanced window right to the advanced view where we get all the different controls which are present on this web page with their properties. Okay. Now as this item is not unique our first attempt should be to add more properties right to make it unique.

[05:13] So let's try to add some more properties to see whether we can make this control unique using additional properties, right? So let's select type and value. But as you see even adding these two properties is not making this control unique right in situations like this as I explained there are other ways of identifying a particular control, right? So if I go to the advanced view on the top menu, you will see identify by option and this is the properties option, which we are using right identifying controls by properties, but Tosca provides you with different other mechanisms.

[05:55] Okay. So one is identified by anchor. It also provides you identify by image and identify by index. Now we are going to talk about how we can identify controls by image and index but your second option after properties should always be anchor. Right. So let's go ahead and select this and you will see on the right side. There is a window called identify by anchor now Tosca will sometimes automatically select anchor control for you, right?

[06:32] So it has got this relative algorithm and there are different options here. Right? So we are not going to go deep into this algorithm which Tosca uses but for just for your knowledge, you can select auto always and it will automatically select anchor control for you or you can also choose shortest path and coordinate, right? So it will try to find anchor control based on three different algorithms, but I have selected auto right?

[07:05] So it is not able to identify automatically or anchor control at the same time. I can add my own anchor control, right? So the easiest way is to just drag a particular control into this text box. Okay, so I have dragged this I am feeling lucky button into this anchor control and here you will get the message that the target control was successfully identified right and we can also add another anchor control, right?

[07:36] So you can just click on select on screen and select that particular control to add as your anchor control. So we can have multiple anchor controls if it is not able to identify with a single control. Okay. Now if you see on this Google search button, the message has changed to select item is unique and that orange bar is also disappeared, which means all our controls are now unique in this module and we can go ahead and create our test case, right?

[08:08] So let me go ahead and save this and close this window. So that will create my module here. And I'm going to rename this to something useful which is Google search, right? And we are going to create a test case now. Okay, so I've created a new folder here. I'm going to add a test case called Google search and then I'm going to add my test step which is basically the module.

[08:41] So I'm going to search my Google search module. I am going to double click on this so that it can add that right and here I'm going to enter some text say Tosca, right? And here I'm going to click on this. So I can select the click option here, right? So it's going to enter Tosca into the text box and it is going to click on it. Okay, so that's that's our scenario.

[09:12] So let's go ahead and run this for now and see if it's working or not. So it's going to type Tosca into the text box. It's going to click on the Google search button and it is going to display the results, right? So this is how you can identify controls using anchor control if there are scenarios where you are not able to identify uniquely any control using all the properties present on the screen, right?

[09:43] So this is another way of identifying your controls. So that's all about how to identify controls in Tosca using the anchor property or anchor control. Hopefully this was useful. I'm going to talk about all the different mechanisms which are still present in Tosca to identify controls like identify by image and identify by index. So keep watching and do subscribe to our channel will bring up another new Tosca lesson next Friday until then keep learning and have a nice day.
