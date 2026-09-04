---
id: "8tXcwf0qLx8"
title: "Tosca Tutorial | Lesson 144 - Common Problems & Fixes | Cross Browser Testing | Multiple Browsers |"
url: "https://www.youtube.com/watch?v=8tXcwf0qLx8"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 148
duration: 422
upload_date: "20240326"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:10:05Z"
status: "raw"
---

# Tosca Tutorial | Lesson 144 - Common Problems & Fixes | Cross Browser Testing | Multiple Browsers |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so today we are going to discuss about a very common use case which is called cross browser testing now in tosa we already know how we can execute our test cases on different browsers so that can be easily done uh by going into the test configuration and then creating a test configuration parameter choosing browser here and then uh depending on what browser you want to execute you can choose that particular browser here so if I want to execute this test case on Chrome I will choose Chrome if I want to execute on Firefox I will uh choose Firefox or any other browser right so this is how you can EX execute your test case on one single browser each time you execute so every time you execute you can change this particular value from your execution list or from your test case but what if

[01:14] uh you have a requirement where you have to run the same test case in multiple browsers at the same time now this is a popular interview question as well as uh this could be a requirement in your project right so rather than um having different test cases which can execute on different browsers you have to execute the same test case in multiple browsers at the same time so like all other automation tools it is also possible to configure it in tosa so let's see how we can do this now I'll be using this swag Labs login uh test case for this particular demo and here uh we have got a login process folder okay which has got two steps open URL and close browser and what I'm going to do is I'm going to copy this and I'm going to paste it here so I will be having to

[02:16] login process okay and the both login process needs to be run on different browsers okay now just for uh the sake of differentiation I I will just remove this Clos browser step from this login process one and in login process two uh it has got these two steps right so this is an example where you have got two different processes which needs to be uh executed on different browsers okay to verify that it is working as expected in both the browsers now uh we have got these two different process now we can see how we can run this in different browser ERS from the same test case okay now instead of uh providing a value like a constant value for browser what we can do is uh we can pass a buffer value here okay so

[03:17] what we will do is we will pass uh bore browser okay so this is basically uh the buffer name bore browser okay and we are referring to the value of bore browser so whatever uh the value it will use the same value here in the configuration parameter right now uh what you can do here is you can have a step here which is uh to um set buffer okay and um inside this what we will have is we will have the bore browser buffer name and here we will pass the value which is Chrome okay similarly um I can have this step again inside the login process to okay this will be always the first

[04:20] step and again bore browser but this time around I will make it Edge okay so like this you can have a number of steps where you can set the buffer to a different browser value right and now what it will do is um it will come here and it will set the buffer to Chrome okay and then while executing this test case it is going to execute it on the Chrome browser because in our test configuration parameter our value is set to bore browser which is a buffer so it is getting the buffer value from the test case itself right and uh similarly for the second process it will pick up the value as Edge and it will execute this uh particular login process uh in the edge browser so let's go ahead and see whether uh this will work or not okay so I'm going to run this in

[05:27] scratchbook okay so this is the Chrome browser which is the first step and now this is the edge browser okay so here you can see uh the edge browser was closed as per our login process but the Chrome browser is still running right so uh here um on the scratchbook results or logs you can see here the browser value was set to Chrome in the first step and then it opened the URL in Chrome and then here the browser value was set to Edge and then it opened the URL in Edge and then it closed the browser uh which is the edge browser tab right so this way you can run your test steps in different browsers from the same test case you don't need to have different test cases to run it on multiple

[06:27] browsers or you don't need you have a distributed execution for choosing different browsers okay so this can be done simply uh within your test Case by just providing a buffer value in your test configuration parameter which is the browser parameter that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
