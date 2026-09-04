---
id: "OATubSuVee8"
title: "Tosca Tutorial | Lesson 14 - Use TBox Start Program | Open Application | Executable File |"
url: "https://www.youtube.com/watch?v=OATubSuVee8"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 16
duration: 564
upload_date: "20230215"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T07:59:13Z"
status: "raw"
---

# Tosca Tutorial | Lesson 14 - Use TBox Start Program | Open Application | Executable File |

[00:03] now we are going to look at some of the other t-box modules which could be useful when you are working with different process or you want to do some performance checks the first is the process operations and part of this you have the Start program which is a t-box module so using this you can start any particular application be it a exe a desktop application or even a browser okay so let's go ahead and look at this let me create open or a Start program right so let's create a new folder here and I'm going to call it process operations inside this let me create another test case and let's call it open notepad Okay so this is the application

[01:06] which I want to open to Tosca and let's see how we can do that so let's go ahead and add the t-box module now and we'll say open or Start program okay and here we have to give some parameters for notepad.exe we just require the path okay so I'm going to give the path here which is C window and notepad.exe okay uh similarly you can pass the path for any particular application um you can also pass arguments um and wait for exit and also run as which will have the username and password if uh it's a secure application right so these are all the different parameters which you can pass you can use whichever application you require okay but for us it is notepad.exe so let's go

[02:09] ahead and run this as you can see the step has passed and in the background uh Tosca has opened a Notepad application or the notepad.exe right so that's what uh how you can start a particular program or application uh using Oscar okay using the steebok Start program module to show another example out of it right um I can also add another devox module here so and this time around we are going to open uh the Chrome browser okay with some parameters so let's go ahead and browse the Chrome browser okay and that you will find here in C program files Google Chrome application okay if

[03:09] it's a 64-bit if it's uh not a 64-bit you will find it in the x86 folder so here I have got the chrome.exe so I'm going to browse to that path right and then um I will also add some arguments okay so inside the arguments uh I'm going to first add a argument for Incognito because I want to start this browser in in computer mode and then I'm going to pass the URL which it should go once it opens okay so I'm going to go to google.com so those are the two arguments uh which I have passed right it should open in the incognito mode and it should open this URL right and let's go ahead and run this so as you can see the test has passed and Google

[04:10] .com is opened in Chrome in Incognito mode okay so that's how powerful this particular t-box module is it can open any particular application with parameters or with arguments or even if it's a username and password protected application okay now um coming to our last module which we are going to look in this particular session is for timing okay so some modules which are related to timing and I'm going to add here a test case called start timer right and then I am going to add in the test case called stop timer okay and what I'm going to do is I am going to bring in this particular uh start Chrome right so let's actually rename this

[05:11] and this one is for notepad right so start Notepad okay um so I'm going to add in the test case here called uh open browser right and I'm going to put it between the start timer and the stop timer and then I'm also going to copy this step into the open browser test case right so it's basically going to do the same thing it's going to open the Chrome browser but what I will get here is I will get um the time it takes to execute this particular step okay how we can do that uh we will add a module here called The Box start timer okay and here we need to provide ID which is just nothing but the name of that particular timer so I will say it is a

[06:15] timer one okay and the same thing here but we will have a different t-box module so stop timer and we'll be using the same ID here so that this runs and calculates how much time it is taking right in terms of the timer running for this particular test case so we have got the start timer and stop timer and let's go ahead and run this whole folder okay just executed now and in the results you can now see that the log info it has got a start timer which was started okay um the application was launched as expected but in the stop timer you will also find something called measured

[07:15] value okay and that's the time it took to execute this particular test step which is in between these two timers and that was 28 milliseconds okay so it's quite useful if you want to know how much a particular step uh is taking to execute right and what also you can do in the stop timer is you can put a maximum duration so this could be useful in doing a performance test for your uh testing right so if that particular step or a particular test case is not completing in that particular time then you can mark it as failed right it did not uh meet up to the performance expectations of the particular test okay so what I can do here is I can put a maximum duration of just 10 milliseconds and put a verify action mode and when I execute this again

[08:24] okay so this time around it's going to fail uh because the verification field okay and you can see in the stop timer it is saying that the verification is filled expected value was less than 10 seconds uh actually took 43 seconds so it's basically a performance check or a performance test right which you can perform using this uh two t-box modules uh start timer and start stop timer okay so these are um all the commonly used t-box modules uh which are generic in terms of how you can do different operations on files folders uh on your applications starting and stopping and also some performance tests now there are many other modules which are present uh in the standard subset but these are the most commonly used okay so that's all for this session uh which covered the key box automation modules
