---
id: "sZ4uO5o26Kc"
title: "Tosca Tutorial | Lesson 110 - Two Times | Dynamically changing ID Property | Obstacle 4 |"
url: "https://www.youtube.com/watch?v=sZ4uO5o26Kc"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 111
duration: 338
upload_date: "20230923"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:07:18Z"
status: "raw"
---

# Tosca Tutorial | Lesson 110 - Two Times | Dynamically changing ID Property | Obstacle 4 |

[00:08] hey everyone welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist continuing with our obstacle topic we are in our fourth obstacle so let's see what this obstacle is all about it is called two times uh and what we have to do is we have to create a automation test step where it can click on this button two times in a row so when you click on this particular button first time it is Click me to X and the second time it changes to click me once more okay and when you click on this again then uh this particular obstacle is completed so that's what we need to do uh let's go ahead and get started now let's create a module for this particular control so let's scan this application and record these modules so let's go ahead and go to the scan application

[01:13] and then scan this application and let's have a look at this particular control okay so here what you can see is this particular control is unique okay so it is Tosca is able to identify this using the different properties and the two properties which it is taking is the ID here okay and the tag which is a and here it is r d underscore some random number now uh let's go ahead and click so we are not going to save this okay because I want to show you what happens when we click on this once and then now if we go ahead and scan this again okay and now if we go ahead and select this particular control this time also it is unique because it is also able to

[02:16] identify using the properties but you will see that uh the ID right has changed so it's a different ID for this particular control now so once we click on this the later part of or the numerical part of the ID is changing for the same control so we need to handle that in our modules right and the way we can do this is using regular expression uh so that we can handle this Dynamic part of the ID right so what we can do simply here is we can put a star which stands for a regular expression for one or more occurrences right so any numerical digits uh would be handled by this regular expression no matter if it changes right or it remains same it will work both ways so uh this we can do the ID we can change that right and now uh it doesn't

[03:19] matter if the ID changes or it should still work so let's go ahead and save this module now and we are going to come here and we are going to rename this module first okay and then we are going to create a test case so that we can see how it works right so let's go ahead and create a test case here I'm going to rename this again and then we are going to drag this particular module here and we are going to click on this so again we'll use the x value here and we are going to name this step okay so click once and then again we are going to drag this module another time because we have to click it two times right so we are going

[04:21] to rename this step again click twice okay and then we are going to click on this particular control okay so ideally it should click uh two times even though the ID is changing because of our regular expression in the module properties okay so I will change the workstate to completed and then on the application I need to go back to the initial state right so come back to the screen where it shows click me to X okay so now I'm going to execute this test case and see if it still works okay so yeah as you can see it was able to click the link two times and the obstacle was completed so using regular expressions in your model properties you can handle Dynamic elements which have got properties which

[05:21] are changing dynamically that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
