---
id: "_WKauyXPI8g"
title: "Tosca Tutorial | Lesson 18 - Window Operations | TBox Automation Module |"
url: "https://www.youtube.com/watch?v=_WKauyXPI8g"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 20
duration: 505
upload_date: "20230218"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T07:59:34Z"
status: "raw"
---

# Tosca Tutorial | Lesson 18 - Window Operations | TBox Automation Module |

[00:10] in this Tasker session we are going to talk about the key box window operation now this is one of the t-box automation tools modules and using this module you can send specific commands to a particular window these are mostly useful for window based applications and we are going to look at some of the operations which you can perform there are lots of different operations which this module provides like you can bring the window to front you can close the window maximize minimize move to Center normal which is restoring the window to its original size you can resize the window you can check whether that particular window is open or not and then wait on close and wait on open right so these are all the different operations which you can perform using this particular module we are not going to look at all of them but we'll be looking at some of them which could be

[01:13] useful when you are working with this windows in your automation test suit okay so for this particular example I'm going to use a the notepad Okay and as you can see I have already created a particular test case called window operations and inside that my first step is to start or open the notepad now if you remember we have talked about process operations where you can have the where you can use the t-box Start program and that's what I'm using I have given the path which is the notepad path and when I'm going to run this it is just going to open the notepad for me okay so okay so the notepad is open we have used the t-box Start program right it's not part of the window operations but this

[02:14] is required in order to open this particular application okay and then now I'm going to add few other steps which are related to the window operations module okay and we are going to use the t-box window operation so let's search for this right and there are basically four parameters here or um that's the values which you can pass right so you can pass a caption a caption is nothing but a name for that particular window okay then window index if you have multiple windows open you can put a index to it and then the operation the operation which I was talking about there are lots of operations but uh we are going to use some of them and this operation is a drop down list okay so you can see uh we talked about bring to front close maximize minimize

[03:14] um resize move to Center and verify window access so all of these operations are present here which you can perform on your window okay so uh coming to caption right so in this caption this is a notepad right so the text is notepad on this particular window but there is also a Untitled text in this right so what we can do we can use some regular expression so that even if the text changes it will always be able to identify with this particular caption okay although I have got just one window open right now I can still use a index um for instance if there are other windows open for notepad then this will only consider the first index okay and then coming to operation right so what we are going to do first is we are going to maximize it right so let's rename this to maximize

[04:21] okay now what I can do I can copy and paste this okay and I can just change the operation now I will change it to minimize so it will minimize that particular window okay and the caption and window index will still remain the same and then let's copy this again we'll try to use some operations and then I will say we can bring that or to the normal size okay so let's change it to normal okay and then um in this final step we are going to close this particular window okay and I'm going to use another operation here okay but I'm going to drag this to the beginning okay here um I'm going to say bring to front right so if

[05:22] it is somewhere in the background then it is going to bring it to the front Okay so we are going to use this operation and that will be all the steps which will be um or all the operations which will be performing using this window operation module you can try out all the remaining options but these are the ones uh which we can try right now okay now let's try and run all of these different operations on our notepad right before that I'm just going to adjust this particular operation I'm just going to put it after minimize so that when it is minimized you can bring that particular window to the front right and if I run this whole test case together you might not be able to see anything because it will be too fast so what I'm going to do is I'm going to execute a step one step at a time right so first I'm going to

[06:22] execute the maximize so that the window is maximized right you can see uh the window size is not changed it is uh to the maximum maximum screen size right and let's go back here and the scratchbook you can see it is passed now let's try and run the minimize window and let me put the scratch book uh to a second window so that we can see that okay right uh now let's try and run uh the bring to front because our window is minimized let's try and do that so you can see now it is showing it in front right

[07:28] and then let's run this normal operation so that it will bring back the window to its normal size okay and then finally we'll close the application and you will see that uh the notepad is closed now okay so these are all the operations uh which can be performed on a window you can try out all the remaining operations which I showed you um on the same window or a different window so it's a quite useful module if you want to perform some operations on a particular window especially window based applications and that's all for this particular t-box window operation module
