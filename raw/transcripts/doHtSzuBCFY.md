---
id: "doHtSzuBCFY"
title: "Tosca Tutorial | Lesson 122 - Close Window Popup | Window Operations |Obstacle 16 |"
url: "https://www.youtube.com/watch?v=doHtSzuBCFY"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 123
duration: 447
upload_date: "20231222"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:26Z"
status: "raw"
---

# Tosca Tutorial | Lesson 122 - Close Window Popup | Window Operations |Obstacle 16 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist now continuing with the topic on test automation obstacles let's look at our next obstacle which is called the popup windows so it's a pretty easy obstacle if you know how to uh solve this particular problem uh what we need to do is uh in order to complete this obstacle we need to click on this button okay which is called The Click me and what it will do it will open another window or a window popup uh and what we need to do we need to close this particular window to complete this obstacle okay so let's go ahead and see how we can uh solve this particular obstacle and tosa okay so uh going back to tosa and here as usual we will go to our obstacles folder and then we are going to scan

[01:13] this particular application now here I need to just uh add this particular control which is the click button now you will think that I might need to also scan the particular window which is opening up but it's not the case Okay so these popup windows can be handled using a standard automation tbox module and uh it is part of this Windows operations okay so when we add this Windows operation module I will show you how we can uh handle this particular window or maybe close it um using this standard module which is already present in tosa so we don't need to scan this particular window again okay so I'm going to save this and I'm going to close this I will just rename

[02:14] the module now okay and then uh we will create a new test case here and then I am going to add the respective module to this particular test case Okay so the first step is obviously to click on the button so that's pretty simple uh we need to use the click operation for that and after this um let's rename this particular test step to click button okay and after this the window will open and then we need to close that particular popup window right and as as I said we can use one of the standard modules okay so we'll go to modules standard modules and then under tbox automation tools okay we have got the basic window operations inside this we'll be using the tbox window operation

[03:17] okay so uh let's go here into the obstacle and I'm going to add this particular module here now uh as you know uh this dbox window operation has got lots of different operations which you can perform on the window right so you can see you can minimize maximize close um weight resize move to Center so all types of operations can be performed on a window- based uh popup or just a window okay now the only thing which we need to provide is the caption so that it can find the right window on which it can perform that particular operation okay and that can be done so when we click here it opens up this window and here you can see this is probably the window title right so tric centus at tric centus SLX all right so I cannot take the starting part of uh this particular title which is Tri centus because then

[04:19] my other window has also got tricentis right but what I can do is I can use this um X username which is at tricenter uh this would be unique and rest of it can be handled using the regular expression okay so that's what I'm going to do here in the caption I'm going to start with the regular expression and then uh add try sentus and again a regular expression okay so this will be static at resent but the remaining part can be dynamic uh it could be anything uh it will still be able to uh find this particular window using this particular title okay now coming to different operations as I said we can perform different operations on the window now we can directly go ahead and close it but sometimes uh if the window takes a little bit of time to appear then your test case may fail right because uh your TS automation will

[05:21] not fit it will directly go and search for the window and try to close it but if it is not present then the test case might fail so in these type of scenarios it is best to have a weight uh so we can use this weight on open right so this operation what it will do it will wait till this particular uh window is open right and then it is ready uh where we can perform some action on it right so in the next operation on the same test step uh we can perform a next uh operation which is the close window right so this will basically close that particular window okay so we are using two operations and then we are passing on the caption here in the tbox window operation okay I am going to call this close popup right and then uh we come here we change the work state to completed and

[06:23] finally we are ready to execute the test case okay so let me close all this okay and uh get it back to the initial State and now I can go ahead and execute this right okay so as you can see uh it was able to perform both the steps which is clicking on the button and then closing the window popup right using the two operations and uh this completed the obstacle right so this way you you can handle your window popups you can perform a lot of different operations using the standard Windows module so it's pretty easy if you know what to use uh in in a specific scenario that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I

[07:24] will see you in the next video
