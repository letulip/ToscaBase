---
id: "8tXcwf0qLx8"
title: "Tosca Tutorial | Lesson 144 - Common Problems & Fixes | Cross Browser Testing | Multiple Browsers |"
url: "https://www.youtube.com/watch?v=8tXcwf0qLx8"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 422
upload_date: "20240326"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:40:42Z"
status: "raw"
---

# Tosca Tutorial | Lesson 144 - Common Problems & Fixes | Cross Browser Testing | Multiple Browsers |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So today we are going to discuss about a very common use case, which is called cross browser testing. Now in Tosca, we already know how we can execute our test cases on different browsers. So that can be easily done by going into the test configuration and then creating a test configuration parameter, choosing browser here, and then depending on what browser you want to execute, you can choose that particular browser here.

[00:47] So if I want to execute this test case on Chrome, I will choose Chrome. If I want to execute on Firefox, I will choose Firefox or any other browser, right? So this is how you can execute your test case on one single browser each time you execute. So every time you execute, you can change this particular value from your execution list or from your test case. But what if you have a requirement where you have to run the same test case in multiple browsers at the same time?

[01:23] Now, this is a popular interview question as well as this could be a requirement in your project, right? So rather than having different test cases which can execute on different browsers, you have to execute the same test case in multiple browsers at the same time. So like all other automation tools, it is also possible to configure it in Tosca. So let's see how we can do this. Now, I will be using this Swaglabs login test case for this particular demo.

[01:59] And here we have got a login process folder, okay, which has got two steps, open URL and close browser. And what I'm going to do is I'm going to copy this and I'm going to paste it here. So I will be having two login process, okay? And both login process needs to be run on different browsers, okay? Now, just for the sake of differentiation, I will just remove this close browser step from this login process one.

[02:34] And in login process two, it has got these two steps, right? So this is an example that you have got two different processes which needs to be executed on different browsers, okay? To verify that it is working as expected in both the browsers. Now, we have got these two different process. Now we can see how we can run this in different browsers from the same test case, okay? Now, instead of providing a value like a constant value for browser, what we can do is we can pass a buffer value here, okay?

[03:17] So what we will do is we will pass B underscore browser, okay? So this is basically the buffer name B underscore browser, okay? And we are referring to the value of B underscore browser. So whatever the value, it will use the same value here in the configuration parameter, right? Now, what you can do here is you can have a step here which is to set buffer, okay?

[03:55] And inside this, what we will have is we will have the B underscore browser buffer name and here we will pass the value which is Chrome, okay? Similarly, I can have this step again inside the login process too, okay? This will be always the first step and again, B underscore browser, but this time around, I will make it edge, okay?

[04:28] So like this, you can have a number of steps where you can set the buffer to a different browser value, right? And now what it will do is it will come here and it will set the buffer to Chrome, okay? And then while executing this test case, it is going to execute it on the Chrome browser because in our test configuration parameter, our value is set to B underscore browser, which is a buffer. So it is getting the buffer value from the test case itself, right?

[05:02] And similarly for the second process, it will pick up the value as edge and it will execute this particular login process in the edge browser. So let's go ahead and see whether this will work or not, okay? So I'm going to run this in Scratchbook, okay? So this is the Chrome browser, which is the first step and now this is the edge browser, okay?

[05:36] So here you can see the edge browser was closed as per our login process, but the Chrome browser is still running, right? So here on the Scratchbook results or logs, you can see here the browser value was set to Chrome in the first step and then it opened the URL in Chrome and then here the browser value was set to edge and then it opened the URL in edge and then it closed the browser, which is the edge browser tab, right?

[06:13] So this way you can run your test steps in different browsers from the same test case. You don't need to have different test cases to run it on multiple browsers or you don't need to have a distributed execution for choosing different browsers, okay? So this can be done simply within your test case by just providing a buffer value in your test configuration parameter, which is the browser parameter.

[06:48] That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching and I will see you in the next video.
