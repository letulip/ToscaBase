---
id: "1khI-I1gonk"
title: "Tosca Tutorial | Lesson 106 - Handle multiple browser tabs | Configuration Parameter | Obstacles |"
url: "https://www.youtube.com/watch?v=1khI-I1gonk"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 517
upload_date: "20230330"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:27:38Z"
status: "raw"
---

# Tosca Tutorial | Lesson 106 - Handle multiple browser tabs | Configuration Parameter | Obstacles |

[00:06] Hey everyone, welcome back to another interesting Tosca lesson and today we are going to look at a scenario where you have got two different tabs which are basically the same web page and you are trying to perform or automate some scenario in this particular web page. So the challenge here is as there are two tabs which are exactly the same, they have got the same properties, same controls and even the same page title.

[00:39] So when you execute any test in this type of scenario, either you have to close one of the tabs so that you have just got one single tab open or you have to always make sure that you are closing all your browser tabs before opening a new page and then performing your test. Otherwise, if you execute your test with this particular scenario, it is always going to fail because Tosca is never going to decide where it is going to perform that click because there is no property through which it can decide which one is the unique one and which one it should click.

[01:21] So first, let's see the scenario. So if I have opened these two tabs and I have this test case which just clicks on the automobile link, this one, right? So if I run this, it's always going to fail. So once the execution starts, you will see that it is trying to switch between two different tabs and it is trying to find out maybe some control, I can find a different property, but it is not able to, right?

[01:56] So it will continue like this for some time and then it is going to fail with error message saying that multiple tabs are open, which has the same name. And hence, it is not able to execute this particular test or it is just going to fail it, right? So as you can see here in the log info, right? So if I expand this, you will see that it is saying more than one matching tab was found and hence it has failed this particular step, right?

[02:32] Now, to resolve this kind of issues, Tosca provides you with an option where you can add a particular configuration parameter which is known as constraint index, okay? And that can be added to the module and then it can decide which particular index it should consider while performing that particular operation on control, right? So it is pretty similar to when we scan different elements, right?

[03:03] And if we have got the same element a number of times on that particular page, then we provide an index, right? And based on that index, then Tosca can decide which particular control to click if there are multiple controls, right? Similarly, this situation is quite similar, but instead of me going back and scanning this module, right, with two different pages and then putting indexes there or putting some other scanning mechanism, rather than that, the easier way is to just modify the module and put an extra property here, okay?

[03:43] So if I go to this particular module, here is my module attribute, right? And I can right-click on the module and there you will find different types of parameters I can add. One of them is the configuration parameter. So I'm going to create this, okay, so here the name you have to replace it with constraint index and in value you have to provide the value. So basically on which page you want to perform this operation on, right?

[04:18] So if I say 2, so it is going to select the second tab, okay, so let's go ahead and verify this quickly. So if I'm going to run this again, right now, you will see that it is go on to the second tab and it has executed our script, which is clicking on that automobile link, right? So basically this is how you can tell Tosca on which particular tab index it can go and it can perform that particular operation.

[04:53] Okay, so I can change it to any particular value. Okay in my particular module. I can change this to one or two or three, right? But this is not the ideal way of doing it. Okay, because I don't want any static value and I don't want to keep it changing from the module level, right? So I should put some mechanism through which it can be changed automatically right from the test.

[05:24] Okay. So how can we do that? Let's add another test step here and we are going to use a buffer right now. So we'll say t-box set buffer and we'll put it previous or prior to this particular operation, right? So in this t-box set buffer, we are going to put index. Okay, and we are going to put a value here. Okay, so we'll be basically controlling the flow of this test case right from here.

[05:57] Okay. So if you want to click on the first tab, we will do that from here. If you want to do it on the second tab, we can do it from here. Okay. So once you create a buffer value, right like a variable which has got this value 1 now, we want to use it in the module. Okay, so let's go back here in the module and instead of this static value, I'm going to replace it with a buffer value. Okay, is the same way you do it in your test cases or test steps which is start with curly brace and then put B and then square bracket and then the particular variable.

[06:34] Okay, so which is index for us. So now it is going to refer to that particular value which will be putting in this particular test case right now. I can drive multiple values here from my test case design sheet or from a configuration parameter, but you can configure it easily like but you can basically control the execution right from here rather than going and changing every time on the module level. Okay.

[07:05] So now if I run this it should basically click on the first tab, okay, but before that let me bring the state of both the application to the same level. Okay, and now let's go ahead and run this so as you can see it is now clicked on the first step instead of the second tab. Okay, similarly you can handle multiple tabs if they are open on your web page still you can run your automation on a single tab using this particular configuration parameter with a constraint index.

[07:49] Okay, so hope this short video was helpful in resolving one of your issues which you might face while executing your tests and multiple tabs are open for your application also for watching more interesting videos do tune in into our Channel if you have not subscribed yet do subscribe so that whenever we come up with a new video you will be getting notified about it. So I will see you next time with another interesting Tosca lesson in the coming up video pretty soon.
