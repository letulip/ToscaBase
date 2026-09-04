---
id: "AX495tz4jIM"
title: "Tosca Tutorial | Lesson 107 -  IDs are not everything | Elements with same IDs | Obstacle 1 |"
url: "https://www.youtube.com/watch?v=AX495tz4jIM"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 108
duration: 415
upload_date: "20230920"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:06:58Z"
status: "raw"
---

# Tosca Tutorial | Lesson 107 -  IDs are not everything | Elements with same IDs | Obstacle 1 |

[00:08] hey everyone welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist starting with this session we'll be going through a number of different test automation obstacles which are part of this obstacle course uh web page which is defined by try centers now there are different obstacles which have been defined here which test your knowledge on different parts of Tosca this is a very good starting point if you want to test what you have learned until now in Tosca and where do you think you lack knowledge so that you can focus on those particular things within Tosca now I'm going to take you through all the different obstacles which are present in this particular obstacle course and we'll go through each of the test automation challenges which you will face in your real-time applications as well so I will tell you how you can solve this obstacles the best possible

[01:10] way using the different features of Tosca which is available so let's start with the first test automation obstacle which is named as IDs are not everything now as part of this obstacle we need to click on this click me button okay so seems pretty simple but um let's scan this module and then we will see what is the actual challenge in clicking on this button so let me open Tosca here and then I'm going to scan this particular module here okay so I'm going to select the application here and click on scan now and then I'm going to go to the advanced tab okay so here we can see there are the two links don't and click me right now let's see uh if we select this click me

[02:14] um Tosca is telling us that this particular item is not unique okay and the reason is using this ID and tag for this particular element it is not able to identify that uniquely okay now if you look at this don't link okay uh the ID and tag are exactly the same so these two are basically uh two similar controls two similar links which have got the same ID and obviously they are links so they will have the same tag right so the whole idea behind this obstacle is that you should not always stick to the ID property okay whenever you have uh controls which have got similar properties you should try to use different properties other than ID okay so you should also try to use a combination of different technical properties through which you can easily

[03:15] identify this any control uniquely okay so in this case you can see the ID and tag is not enough here right so what else we can use now if you look at both these controls you will see that the inner text right is different for both these controls so that could be a good starting point so we can look to use the inner text here and once we select the inner text in the technical property you will see that now this item is unique so that solves most part of the challenge because clicking on the link won't be difficult once you're able to identify it uniquely so let's go ahead and save this now and let's close this now we will use this to basically create a test case okay so I will just rename this module here

[04:28] okay and then I'm going to create a test case folder here called obstacles inside this I'm going to create my first obstacle I'll just name this with the particular obstacle number so that I can identify it later and then I'm going to drag this module here okay and the simple thing which we need to do here is to click on it here as you know we can use the click option but as per the best practice you should also look to not use this click method which is a mouse uh keyboard method right which is a slower in performance also it is not recommended by press centers right so we'll be using the other option which is the X okay it does the same thing it clicks on the particular link and then following the best practices I am going

[05:29] to name this click link okay so I am going to rename my test step so that I know what is going on here right so that's my test case and then I'm going to complete or change the workstate to completed so now I'm going to run this particular test case so let's go ahead and run it in scratchbook and now it should be clicking on the click mail link or button okay so as you can see uh Tosca was able to identify that control and click on it and then the obstacle was completed by all means this was a very easy obstacle to start off with but it is a very common scenario which you will face while doing automation on any web application you will come across different controls which have got same properties and then you need to fall back on different properties or you also

[06:31] need to try different identification mechanisms in order to identify these controls which are not unique on the application that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
