---
id: "RsbKnsNt8Rs"
title: "Tosca Tutorial | Lesson 131 - Scroll Into View | Steering Parameter | Scrolling  | Obstacle 25 |"
url: "https://www.youtube.com/watch?v=RsbKnsNt8Rs"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 132
duration: 333
upload_date: "20240122"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:03Z"
status: "raw"
---

# Tosca Tutorial | Lesson 131 - Scroll Into View | Steering Parameter | Scrolling  | Obstacle 25 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our test automation obstacles topic with trien tosa let's look at our next obstacle which is called scroll into view now here the obstacle seems it's pretty simple that you need to enter tosa into text box but the catch here is the text will disappear once the text box is out of the visible area so here if you look here uh I cannot enter the text directly because currently this particular text box is not in view and something is blocking the UI now if I scroll this to the bottom then the text box is going to come into the view and then I I can enter some text here okay and then I can click on submit to complete this obstacle so this is what we need to do in tosa so let's see how we can perform this particular

[01:12] automation so coming back to tosa uh first of all we are going to scan this particular module so I'm going to scan the application here and now we are going going to add uh the particular text field and also we are going to uh select the submit button so these are the two objects which we want to add and as you can see the text field uh is uh embedded inside iframe and then there is an HTML document inside which there is the text field okay so these are the two controls which we need currently so I'm going to save and I'm going to to also rename this obstacle before I close it so I'm going to rename this module here then I'm going to save and I'm going to

[02:17] close now the next thing which uh we have to do is we need to add some more Properties or parameters into this particular text field because as you know we need to scroll in order to get this particular field into the view okay and for this uh we can use something called the steering parameter in tosa okay so when you right click on this particular field then uh you can add a steering parameter okay so that is an option to create steering parameter so click on that and we are going to rename this steering parameter property to scrolling Behavior okay so in this scrolling Behavior steering parameter we have got four different values uh which is top bottom center and none so what it does is it allows you to Define where the control should be positioned on the screen and for this it can scroll uh to top to

[03:18] bottom or to Center okay so what we are going to do uh we are going to mention the value here as top so that this particular uh scrolling Behavior helps us to bring this particular uh control uh to the right position on the screen okay once you do that then uh it's becomes very simple we just uh need to add the test case here so we are going here and we are adding a new test case Okay and then uh I'm going to add the module right here and then uh we just need to enter the text here so I'm going to enter tosa here and then um this is the first step the next step is to click on submit so I'm going to use another test step for that okay and I'm going to perform the click operation here using X now uh also

[04:19] what we can do is we can rename the steps so here I will say enter text and here I will say click submit okay so this is all we have to do in this particular obstacle uh we can set the work state to complete it and then uh we can try and run this particular test case now okay so let's go ahead and run this in scratchbook okay so as you can see uh the scrolling Behavior helped us to bring that control into the particular position so that it is visible and then uh it is in View and then we can type the text into that particular text box so similarly you can use different steering parameters to change the behavior of your particular controls uh in your application tosa provides a number of different steering parameters which can be used that's all for this particular

[05:20] video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
