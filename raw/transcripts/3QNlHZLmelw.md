---
id: "3QNlHZLmelw"
title: "Tosca Tutorial | Lesson 133 - Click Position | OffsetHorizontal | OffsetVertical | Obstacle 27 |"
url: "https://www.youtube.com/watch?v=3QNlHZLmelw"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 135
duration: 374
upload_date: "20240130"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:13Z"
status: "raw"
---

# Tosca Tutorial | Lesson 133 - Click Position | OffsetHorizontal | OffsetVertical | Obstacle 27 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the TSA automation playlist so continuing with our topic on test automation obstacles with trient tosa let's look at our next obstacle which is called halfway now this is a pretty simple obstacle if you know how to um steer this particular control so here we need to click in the right half of the button so it's quite a long button and here we need to click it on the right half of this okay so if I click it here you will see that uh the automation obstacle is completed if I click here then nothing will happen Okay so this is what uh we need to do now in order to do this we need to use uh something called called offset for the click operation so what this particular offset is right so uh we can uh Define offsets for two types of Click

[01:14] operations okay and these are for the click method and also for the long click method okay so uh we know already uh what the click operation does the long click using this particular uh operation you can basically click with your left Mouse click and it will remain for at least 2 seconds okay so if you want uh to click on a button for a longer amount of time then you can use this long click and then we can also Define offset for both of this click operations for clicking and also long clicking right now this opt ET uh syntax how you can do this is you need to first right click okay and then you need to mention uh either the offset horizontal or offset vertical okay so this is basically a offset position either in your

[02:16] horizontal axis or in the vertical axis okay so this is how the syntax looks like now um how can we uh basically use this here right so since we have to uh click on the right hand side of this particular button we can provide um either an offset in terms of pixels okay or uh we can also provide it in uh terms of percentage okay so in this case uh we will go ahead and uh we will try to use um percentage so that we can click on the right half of this particular button so let's see how we can do this in tosa okay so uh first let's create our module here so we'll scan the module as usual we'll go to obstacles folder and

[03:19] go to scan application so here I just need to uh scan this particular control which is the button itself and then um I am going to close this and save this module okay um so now uh we can create our test case to automate this particular step so we will create a new test case here and then uh I'm going to add that particular particular module right here okay as I said uh it's a pretty simple one um we just need to make sure that we are using the offset here okay instead of simple click operation so here uh we are going to write the expression uh as I said we

[04:19] have to use the click operation but then inside this uh we need to mention the offset okay and uh what I'm going to do is I'm going to mention something like 90% okay so uh what it will do is uh it will try to uh click on the right hand side of uh the button okay to complete this particular obstacle so let's go ahead and Mark it as completed and then um let's go ahead and try to run this okay so as you can see it is trying to click on the uh right hand corner of this particular button which will be like an uh percentage of uh the complete area of the button and I am clicking on the 90 percentage which is more on the right hand side if you want to click on the left hand side then it will be more of uh in the range of 10 to 50

[05:20] percentage and if you want to just click on the center then you can directly use uh the normal click operation it will be enough to click on that particular button so the same offset operation can also be applied to the long click method uh these are for buttons where you have problems clicking on it or it takes more time to click on those particular buttons or you have to click on a particular position of any particular uh button or a link right so this is how you can use the offset uh position on your click operations to solve this particular automation problem that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
