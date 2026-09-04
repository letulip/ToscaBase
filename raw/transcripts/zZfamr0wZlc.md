---
id: "zZfamr0wZlc"
title: "Tosca Tutorial | Lesson 26 - Execute JavaScript | Verify JavaScript call | TBox HTML Modules |"
url: "https://www.youtube.com/watch?v=zZfamr0wZlc"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 28
duration: 425
upload_date: "20231021"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:00:23Z"
status: "raw"
---

# Tosca Tutorial | Lesson 26 - Execute JavaScript | Verify JavaScript call | TBox HTML Modules |

[00:07] Hey everyone, welcome back to another lesson in this TSCA automation playlist. Today I'm going to show you how you can execute JavaScript on your browser using one of the TSCA automation modules. So there are some standard modules inside the T-Box X engines and HTML where you can find the modules called the execute JavaScript and verify JavaScript result. So using these two modules you can either execute a particular JavaScript or you can also verify the result of a JavaScript. Okay.

[00:39] So let's see how we can use this modules uh to execute a javascript and then verify the result of it. So u I am in my test cases folder and I have already created a test case called execute javascript. Now inside this we are going to drag the module or add the module. Okay. So as I said uh it is under standard modules tbox x engines and then html. Here we'll find the two modules execute JavaScript and verify JavaScript result. Okay.

[01:11] So, uh let's add these modules into our test case. So, I'm going to drag the execute JavaScript here first. And uh then coming to module attributes for this module uh we need to provide a title of the window. uh this is the browser window and then uh the JavaScript the actual JavaScript which you want to execute. Okay. So in title I'm going to use a regular expression uh which means it can be any title. Okay.

[01:42] And then I'm going to write some JavaScript right here. So I'm going to use window dot location dot href. Okay. And then I'm going to use uh the actual web page here. Right. So I've already copied this website uh source demo. This is what I want to open. And this is the JavaScript which we want to execute. So let's go ahead and execute this now. So run this in scratchbook.

[02:17] And now uh we will get an error here. Okay. So in the log info you can see uh that it is asking to define a test configuration parameter for browser and also enter the actual browser on which we want to perform this. Okay. So this is a mandatory requirement. If you don't do this then you will get this uh invalid operation exception. Okay. So let's go into our test case. Go to the test configuration tab here. Uh we are going to add a new test configuration parameter called browser.

[02:48] And then uh we are going to choose the Chrome browser right here. Okay. Now let's go ahead and execute this again. Now you can see in the background it has uh redirected your web page to source demo.com on the Chrome browser and our test case has actually passed. So it was able to execute the particular JavaScript. Right? So this is how you can execute any particular JavaScript. uh either it is to move to a particular web page or performing some actions on your web elements. So any JavaScript uh which can be done on the browser uh you can execute it right here using this module.

[03:30] Now the next module which we want to check is the verify JavaScript result. So let's add another test case here to verify JavaScript. Okay. And then I'm going to add the module here called verify JavaScript result. And here again um you need to provide a title. Uh then the JavaScript and then the result. Okay. Which has got an action mode verify. So it is going to perform a verification. Okay. So let's first see what we want to verify here.

[04:02] Okay. So what I want to do is I want to verify uh some cookies from the website. Okay. So let's check on the website what cookies are available here. Okay. So I'm going to go to uh developer tools and uh right here uh I'm going to find the cookies for this particular website. Okay. So currently there are no cookies. But if I'm going to enter some standard user right here and uh the password.

[04:34] Now if I login into this website you will see that a session cookie has been created called session username and the value for this is standard user and that is what I want to verify from the JavaScript. Okay. So let's go back here and in the title I'm going to give a star again and then in the JavaScript I am going to say return document dot cookie. Okay. So what it is going to do is it is going to return uh the cookie which is present in that HTML document and then I want to verify whether that cookie contains uh the username. Okay. So we have to give the cookie name here which is session username and value standard user. Okay. So let's go here and then uh we are going to say session username equals uh and then we are going to copy

[05:35] this standard user. Okay. So write here standard user. So this is the cookie which is present here and this is what we want to verify. Okay. So let's go ahead and execute this now. Okay. Uh the same error again. Uh I should have done this at the folder level not at the test case level. Okay. So let's do one thing. Uh for now I will just add it here as well. But ideally we should have done that at a folder level.

[06:14] Okay. So, browser and Chrome and then let's go ahead and execute this now. And you will see the verification was successful. Uh this was the expected value and this was the actual value. Okay. So, this way you can also verify some results uh which is returned from your JavaScript using this particular module. So these are the two modules which are present in the TSCOA automation modules under HTML engine and this you can use to execute in JavaScript or verify the result of the JavaScript.

[06:51] That's all for this particular video. If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
