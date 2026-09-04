---
id: "HhOPIJ-fwyI"
title: "Tosca Tutorial | Lesson 116 - Extract Text | XBuffer | Dynamic Text | Obstacle 10 |"
url: "https://www.youtube.com/watch?v=HhOPIJ-fwyI"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 438
upload_date: "20231211"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:28:24Z"
status: "raw"
---

# Tosca Tutorial | Lesson 116 - Extract Text | XBuffer | Dynamic Text | Obstacle 10 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. Now continuing with our topic on Test Automation Obstacles, let's look at the next obstacle which is called the Extracting Text. Now in this particular obstacle, we need to automate a test step where we need to take the total amount which is shown in the success message, which is here, right? And then we need to enter that amount into this particular text box, okay?

[00:42] So if I enter this particular amount here, okay, and then you will see that this obstacle is completed. So this is all we need to do here, right? Now the challenge here obviously is this particular text is dynamic, which means the amount keeps on changing, right? So you need to be able to extract this particular amount from this dynamic text and then you need to enter it into the text box. So let's see how we can do this in Tosca. Okay, so coming back to our Tosca and here let's go to our obstacles and here I am going to now scan this particular application, right?

[01:27] Okay, so here I can see the total amount text box, but I cannot see this success message, right? So I'm going to increase the filtered items so that I can see some of the underlying elements here, okay, and this is the text which contains the purchase completed and then the total amount, right?

[01:59] And then I need to also select the text box, okay? So these are the two elements which I want and then we are going to call this success message, okay, and we are going to call the module, but we will copy this obstacle here and we'll paste it here, okay? And then I'm going to save this and close the scan, right?

[02:33] So our module is created now. Let's go to our test cases section and here we are going to create a new test case, again with the same obstacle ID and then let's go ahead and add the module to this test case, right? So we have got a development which contains the text and then we have got a text box, right?

[03:03] Now, we need to extract the amount from the text and that amount is dynamic so it keeps on changing, right? So the only way I can think of is we can buffer that particular amount, right? But we cannot simply buffer the complete text, right? That text contains the dynamic element. So in this case, we have to use something called XBuffer, okay? So using the XBuffer, we can basically verify the dynamic text as well as we can buffer the dynamic element which is part of that text, okay?

[03:44] So let's see how we can do this. Now, before we do that, we need to look at this success message element, okay? So if we look at the properties, you will see that the inner text actually contains the complete text, right? So it contains the amount and some of other text, okay? So we can use this inner text property to extract this complete text and from there we will try to extract the amount, okay? So let's go back here and then here I am going to use the inner text, okay?

[04:26] And then in this, we are going to copy this particular text, but we are going to make it dynamic, okay? So I am going to copy this here and then we are going to remove this, I am going to put a regular expression here, okay? And then because this amount keeps on changing, so I am going to buffer this and in this case, I am going to use an X buffer, okay?

[04:59] So we are going to use XB as you can see, okay? And then inside this, we are going to provide the buffer name and I am going to call it amount, okay? And you will also change the action mode to verify, okay? So what this will do is it will verify this dynamic text and also it will buffer this particular amount, okay? Into the amount buffer name, right?

[05:33] Now we can easily use that particular buffer to enter it into this particular text box, okay? So here I can just use the buffer, the normal buffer and then I can call the amount here, right? So this is how you can extract a piece of text which is maybe dynamic in nature from the complete text using the X buffer. So you can buffer that particular text which you want to buffer and then you can use that buffered value to enter it into a text box, okay?

[06:10] So this is how you can solve this particular obstacle. So let's change the work state here and then let's try and execute this and let's see if it can enter that particular amount into the text box, okay? So as you can see, it was able to extract the text and also it was able to enter it into the text box, right? So that completed our obstacle, both the tasks were completed, right?

[06:42] So it did the verification here, you can see, and it was also able to enter that particular amount, right? So this is how you can use X buffer and buffer to basically extract some dynamic text and also use that text at various places in your test cases. That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel.

[07:13] Thanks for watching and I will see you in the next video.
