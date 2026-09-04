---
id: "jZvsxD41Iuw"
title: "Tosca Tutorial | Lesson 130 - Hidden Element | Click Element |  Obstacle 24 |"
url: "https://www.youtube.com/watch?v=jZvsxD41Iuw"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 133
duration: 302
upload_date: "20240119"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:06Z"
status: "raw"
---

# Tosca Tutorial | Lesson 130 - Hidden Element | Click Element |  Obstacle 24 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our topic on the test automation obstacle with trst tosa let's look at our next obstacle which is called the hidden element now this is an interesting one uh here it is saying who turned off the lights click the hidden element and as you can see there is no way to find out where that particular element exists okay so visually I'm not able to see the element and you will think that it is impossible to click the hidden element but in reality I don't need to know where that particular element is until I am able to identify that using the tosa scanner okay so if a tosa is able to scan that particular element using its properties and it's able to identify it on the page then uh no matter if it is visible actually on the page or not it

[01:13] can still perform the required operation okay so let's go ahead and try to scan this and let's try to find this element which is currently hidden so coming back to tosa uh going back to the modules and here going back to the folder here let's try and scan this particular application okay so here as you can see we need to do a little bit of digging around so that we can find this particular hidden element and uh here in the filtered items uh you can see that I cannot see any particular hidden element so I'm going to increase the filtered items now okay until I'm able to see all the elements which are on this HTML page okay so now coming back here uh we'll try to find this element by looking at where uh this particular element may be present okay and that you can tell by

[02:14] looking at some of the other elements okay like this text uh which is the easy okay so I can see this uh easy element is right here under this div section so probably you will have that click element where we need to click inside this particular div element okay and uh going a little further I can see that there is a click this uh element which is again like a span element okay and if I look at its properties the it has got a ID so that's very good it can easily identify this and then uh the tag type is span so it is a span element right now here um I'm able to identify this using the ID which is unique so I don't need to add any other properties here right so once I'm able to do this and I'm able to add it into the module then tosa will be able to identify this no matter if it is

[03:16] visible or not visible uh to The Naked Eyes okay so uh let's go ahead and close this and let's go ahead and rename the module okay so now uh we will go back to our test cases section and we will create a new test case now okay so now uh let's go ahead and add the specific module here and then uh we will look at this particular test case so what we need to do we need to just perform a click operation on this particular element right and that you know we can do in two ways we can either use the click operation or we can also use something called X which does the same thing okay so this is all we have to do uh so most of the work will be done in this

[04:16] particular case while scanning the module rather than um designing the test steps okay so I'll will mark it as completed and then let's try and run this in scratchbook now okay as you can see it is uh able to click on that particular hidden element although we cannot see it still tosa could identify it and then perform the click operation on it so that the obstacle is completed for us that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
