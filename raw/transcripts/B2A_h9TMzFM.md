---
id: "B2A_h9TMzFM"
title: "Tosca Tutorial | Lesson 132 - Escape Values | Click Method | Obstacle 26 |"
url: "https://www.youtube.com/watch?v=B2A_h9TMzFM"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 134
duration: 271
upload_date: "20240128"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:10Z"
status: "raw"
---

# Tosca Tutorial | Lesson 132 - Escape Values | Click Method | Obstacle 26 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the TSA automation playlist so continuing with our topic on test automation obstacles with trst tosa let's look our next obstacle which is called The Escape now in this particular obstacle we need to input the value click into the text box now you will think that why it is an obstacle we can directly type this value into the text box but when you scan this particular module and you are trying to enter click into the value then by default it will think that it is the click operation and what it will do is it will try to click on the text box rather than entering it as a value and that is why it is a little tricky but not that difficult so what basically we can do here is uh we can use something called Escape characters in tosa so this is basically used in case we want to escape some

[01:15] special characters but you can use it for any particular text so let's see how we can automate this particular obstacle in tosa now okay so going back to tosa the first step is always the same we need to scan this particular module so let's go ahead and scan this now okay and then U I'm going to scan this particular text box which is called the result text and I'm going to save this and close it let's go back here and I'm going to just rename this okay so now coming back to our tosa obstacle disc cases let's create a new one here and then uh let's add the module which we have scanned earlier okay so we have got uh the

[02:16] particular text box right here um and now we need to enter click into that particular text box now as I was mentioning if we directly try to use the click uh as this okay so it will by default become the click operation because tosa cannot tell that you are trying to click on it or you are trying to enter a particular text okay because this is a system defined operation and this is the expression which is used so tosa will always take it as the default click operation now if you want to make it a simple text right then we need to escape all the characters in this particular text and that can be done in two different ways so uh you can right click on this particular value and then you will get an option to escape the value okay or uh you can directly also uh enclose the whole text inside double

[03:19] quotes so this will basically Escape all your characters which are contained inside this double quotes Okay and then tosa will uh consider it as a normal text and not as a special expression uh which is related to any particular operation okay so now uh this is what we need to do here uh so we'll mark it as completed and we'll try to execute it in the scratchbook okay so as you can see uh it entered click uh as a particular text into the text box and the automation obstacle was marked as completed so this is how you can escape characters at different places uh in your test cases so that TSA consider it as a normal text rather than any special characters or any particular expression that's all for this particular video if you have any

[04:19] questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
