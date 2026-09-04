---
id: "3QNlHZLmelw"
title: "Tosca Tutorial | Lesson 133 - Click Position | OffsetHorizontal | OffsetVertical | Obstacle 27 |"
url: "https://www.youtube.com/watch?v=3QNlHZLmelw"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 374
upload_date: "20240130"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:38:03Z"
status: "raw"
---

# Tosca Tutorial | Lesson 133 - Click Position | OffsetHorizontal | OffsetVertical | Obstacle 27 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So continuing with our topic on Test Automation Obstacles with Tricentis Tosca, let's look at our next obstacle which is called Halfway. Now this is a pretty simple obstacle if you know how to steer this particular control. So here we need to click in the right half of the button. So it's quite a long button and here we need to click it on the right half of this.

[00:45] So if I click it here, you will see that the automation obstacle is completed. If I click here then nothing will happen. So this is what we need to do. Now in order to do this, we need to use something called offset for the click operation. So what this particular offset is, right? So we can define offsets for two types of click operations. And these are for the click method and also for the long click method.

[01:23] Okay, so we know already what the click operation does. The long click using this particular operation. You can basically click with your left mouse click and it will remain for at least two seconds. So if you want to click on a button for a longer amount of time then you can use this long click. And then we can also define offset for both of these click operations for clicking and also long clicking.

[01:58] Now this offset syntax, how you can do this is you need to first right click. And then you need to mention either the offset horizontal or offset vertical. Okay, so this is basically offset position either in your horizontal axis or in the vertical axis. Okay, so this is how the syntax looks like. Now, how can we basically use this here, right?

[02:32] So since we have to click on the right hand side of this particular button, we can provide either an offset in terms of pixels. Okay, or we can also provide it in terms of percentage. Okay, so in this case, we will go ahead and we will try to use percentage. So that we can click on the right half of this particular button. So let's see how we can do this in Tosca.

[03:04] Okay, so first let's create our module here. So we'll scan the module as usual. We'll go to obstacles folder and go to scan application. So here I just need to scan this particular control, which is the button itself. And then I am going to close this and save this module. Okay, so now we can create our test case to automate this particular step. So we will create a new test case here.

[03:49] And then I'm going to add that particular module right here. Okay, as I said, it's a pretty simple one. We just need to make sure that we are using the offset here. Okay, instead of simple click operation. So here we are going to write the expression. As I said, we have to use the click operation. But then inside this we need to mention the offset.

[04:22] Okay, and what I'm going to do is I'm going to mention something like 90%. Okay, so what it will do is it will try to click on the right hand side of the button. Okay, to complete this particular obstacle. So let's go ahead and mark it as completed. And then let's go ahead and try to run this. Okay, so as you can see, it is trying to click on the right hand corner of this particular button, which will be like a percentage of the complete area of the button.

[05:05] And I am clicking on the 90% which is more on the right hand side. If you want to click on the left hand side, then it will be more of in the range of 10 to 50% and if you want to just click on the center, then you can directly use the normal click operation. It will be enough to click on that particular button. So the same offset operation can also be applied to the long click method. These are for buttons where you have problems clicking on it or it takes more time to click on those particular buttons, or you have to click on a particular position of any particular button or a link, right?

[05:46] So this is how you can use the offset position on your click operations to solve this particular automation problem. That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching and I will see you in the next video.
