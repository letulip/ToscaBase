---
id: "OATubSuVee8"
title: "Tosca Tutorial | Lesson 14 - Use TBox Start Program | Open Application | Executable File |"
url: "https://www.youtube.com/watch?v=OATubSuVee8"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 564
upload_date: "20230215"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:00:26Z"
status: "raw"
---

# Tosca Tutorial | Lesson 14 - Use TBox Start Program | Open Application | Executable File |

[00:01] Now, we are going to look at some of the other T-box modules which could be useful when you are working with different process or you want to do some performance checks. The first is the process operations and part of this. You have the start program which is a T-box module. So using this you can start any particular application be it a exe a desktop application or even a browser. Okay, so let's go ahead and look at this.

[00:32] Let me create open. Or start program, right? So let's create a new folder here and I'm going to call it process operations inside this. Let me create another test case and let's call it open.

[01:03] Not bad. Okay. So this is the application which I want to open to Tosca and let's see how we can do that. So let's go ahead and add the T-box module now and we'll say open. Or start program. Okay, and here we have to give some parameters for notepad dot exe. We just require the path. Okay, so I'm going to give the path here, which is see window and notepad dot exe.

[01:41] Okay, similarly you can pass the path for any particular application. You can also pass arguments and wait for exit and also run as which will have the username and password if it's a secure application, right? So these are all the different parameters which you can pass you can use whichever application you require. Okay, but for us it is notepad dot exe. So let's go ahead and run this as you can see the step has passed and in the background Tosca has opened a notepad application or the notepad dot exe, right?

[02:27] So that's what how you can start a particular program or application using Tosca. Okay using the t-box start program module. To show another example out of it, right I can also add another t-box module here. So and this time around we are going to open the Chrome browser. Okay with some parameters. So let's go ahead and browse the Chrome browser.

[03:01] Okay, and that you will find here in C program files Google Chrome application. Okay, if it's a 64-bit if it's not a 64 bit, it will find it in the x86 folder. So here I have got the Chrome dot exe. So I'm going to browse to that part right and then I will also add some arguments. Okay, so inside the arguments. I'm going to first add argument for incognito because I want to start this browser in incognito mode.

[03:39] And then I am going to pass the URL which it should go once it opens. Okay, so I'm going to go to google.com. So those are the two arguments which I have passed right? It should open in the incognito mode and it should open the C URL right and let's go ahead and run this. So as you can see the test has passed and Google.com is opened in Chrome in incognito mode.

[04:14] Okay, so that's how powerful this particular a t-box module is it can open any particular application with parameters or with arguments even if it's a username and password protected application. Okay. Now coming to our last module which we are going to look in this particular session is for timing. Okay, so some modules which are related to timing and I'm going to add here test case called start timer.

[04:47] Right and then I am going to add in the test case called stop timer. Okay, and what I'm going to do is I am going to bring in this particular start Chrome, right? So let's actually Rename this and this one is for not bad, right? So start not bad. Okay, so I'm going to add in the test case here called open browser and I'm going to put it between the start timer and the stop timer and then I'm also going to copy this step into the open browser test case, right?

[05:39] So it's basically going to do the same thing. It's going to open the Chrome browser. But what I will get here is I will get the time it takes to execute this particular step. Okay, how we can do that will add a module here called the box start timer. Okay. And here we need to provide ID which is just nothing but the name of that particular timer.

[06:12] So I will say it is a timer one. Okay, and the same thing here, but we will have a different the box module. So stop timer and we'll be using the same ID here so that this runs and calculates how much time it is taking right in terms of the timer running for this particular test case. So we have got the start timer and stop timer and let's go ahead and run this whole folder.

[06:54] Okay, it is executed now and in the results you can now see that the log info it has got a start timer which was started. Okay, the application was launched as expected but in the stop timer, you will also find something called measured value. Okay, and that's the time it took to execute this particular test step which is in between these two timers and that was 28 milliseconds.

[07:26] Okay, so it's quite useful if you want to know how much a particular step is taking to execute right and what also you can do in the stop timer is you can put a maximum duration. So this could be useful in doing a performance test for your testing, right? So if that particular step or a particular test case is not completing in that particular time, then you can mark it as failed, right?

[07:58] I did not meet up to the performance expectations of the particular test. Okay. So what I can do here is I can put a maximum duration of just 10 milliseconds and put a verify action mode and when I execute this again, okay, so this time around it's going to feel because the verification failed. Okay, and you can see in the stop timer.

[08:30] It is saying that the verification is field expected value was less than 10 seconds actually took 43 seconds. So it's basically a performance check or a performance test right which you can perform using this to t-box modules start timer and start stop timer. Okay, so these are all the commonly used t-box modules which are generic in terms of how you can do different operations on files folders on your applications starting and stopping and also some performance tests.

[09:10] Now, there are many other modules which are present in the standard subset, but these are the most commonly used. Okay, so that's all for this session which covered the t-box automation modules.
