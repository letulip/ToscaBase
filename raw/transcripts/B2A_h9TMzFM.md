---
id: "B2A_h9TMzFM"
title: "Tosca Tutorial | Lesson 132 - Escape Values | Click Method | Obstacle 26 |"
url: "https://www.youtube.com/watch?v=B2A_h9TMzFM"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 271
upload_date: "20240128"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:42:25Z"
status: "raw"
---

# Tosca Tutorial | Lesson 132 - Escape Values | Click Method | Obstacle 26 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So continuing with our topic on Test Automation Obstacles with Tricentis Tosca, let's look at our next obstacle which is called the Escape. Now in this particular obstacle, we need to input the value click into the textbox. Now you will think that why it is an obstacle, we can directly type this value into the textbox.

[00:41] But when you scan this particular module and you are trying to enter click into the value, then by default it will think that it is the click operation. And what it will do is it will try to click on the textbox rather than entering it as a value. And that is why it is a little tricky, but not that difficult. So what basically we can do here is we can use something called escape characters in Tosca. So this is basically used in case we want to escape some special characters, but you can use it for any particular text.

[01:19] So let's see how we can automate this particular obstacle in Tosca now. Okay, so going back to Tosca, the first step is always the same. We need to scan this particular module. So let's go ahead and scan this now. Okay, and then I'm going to scan this particular textbox, which is called the result text. And I'm going to save this and close it.

[01:51] Let's go back here. And I'm going to just rename this. Okay, so now coming back to our Tosca obstacle test cases, let's create a new one here. And then let's add the module which we have scanned earlier. Okay, so we have got the particular textbox right here. And now we need to enter click into that particular textbox.

[02:24] Now as I was mentioning, if we directly try to use the click text as it is, okay, so it will by default become the click operation. Because Tosca cannot tell that you are trying to click on it or you are trying to enter a particular text, okay, because this is a system defined operation. And this is the expression which is used. So Tosca will always take it as the default click operation. Now if you want to make it a simple text, right, then we need to escape all the characters in this particular text.

[03:02] And that can be done in two different ways. So you can right click on this particular value, and then you will get an option to escape the value, okay. Or you can directly also enclose the whole text inside double quotes. So this will basically escape all your characters which are contained inside this double quotes. Okay, and then Tosca will consider it as a normal text and not as a special expression which is related to any particular operation, okay.

[03:39] So now this is what we need to do here. So we'll mark it as completed and we'll try to execute it in the scratch book. Okay, so as you can see, it entered click as a particular text into the text box and automation obstacle was marked as completed. So this is how you can escape characters at different places in your test cases so that Tosca consider it as a normal text rather than any special characters or any particular expression.

[04:16] That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching and I will see you in the next video.
