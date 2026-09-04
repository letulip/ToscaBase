---
id: "ucnJlmkhs04"
title: "Tosca Tutorial | Lesson 139 - Common RealTime Tosca Problems & Fixes | Tosca Date Format |"
url: "https://www.youtube.com/watch?v=ucnJlmkhs04"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 512
upload_date: "20240308"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:12:19Z"
status: "raw"
---

# Tosca Tutorial | Lesson 139 - Common RealTime Tosca Problems & Fixes | Tosca Date Format |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So today I'm going to talk about another problem or issue which is generally faced by many people when they are working with Tosca, especially around date formatting. Now every application has got its own format of date and many times we need to perform date calculations and we need to also change a date to a specific format.

[00:44] But the issue which happens is sometimes Tosca will not accept the date format which you are trying to convert to. Because Tosca has got its own format which is either defined by the system where it is installed or it is defined within Tosca itself. So sometimes the conversion, even though you can use the date function to make the calculations and to make the conversion to a specific format, but the source format will not be accepted as a valid format by Tosca and then it throws up an error.

[01:27] So I have come across this scenario multiple times and that is the reason I thought I would share this particular solution which is a very simple solution which you can apply all the time whenever you are trying to convert some date format into another date format. But the date format which you are trying to convert may be of different formats than what Tosca accepts currently. So let's look at an example for this.

[01:57] So this is the example where this is the date which has been provided to us which is today's date. It is in a specific format which doesn't match with the format which I have currently on my system. My system has a date format of DD, MM and YYY but I have provided a date which is YYY, MM and DD. And then we need to convert this particular date into this format.

[02:30] So this is the scenario. This is what we need to do. So let's go ahead and create a new test case folder here and I will call it dates. And then I am going to create a test case here called format date. So the first thing which I can do is I can set a buffer here. So I am going to use the tbox set buffer and I am going to call it today date.

[03:09] And I am going to define the date which I have picked which is in a specific format. We know that. So I am going to give it a value like 2024 and then 03 and then 07. So this is the value which I have provided. And now I am going to convert this date into the specified format. So I am going to call it new date.

[03:39] So this is again a set buffer. And here I am going to call the date function. So we already know about the date function. You can do different types of calculations. You can also change it to a specific format. So inside this we are going to pick up the buffer of today's date. So the buffer which we have already created. So I am going to use it here and then we will leave this empty.

[04:15] We are not doing any offset. And after that we are providing a format here. So that format would be dd and then mm which will be in capital and then yyy. So this is the format which we want it to convert. And then I am going to close this. So this is the new date. This is the today's date.

[04:45] So everything looks good now and we have used the right date function to convert it into a specific format. So we would expect this to run. So let's go ahead and run this and let's see whether Tosca can actually convert this date or not. So what we'll notice is this test case will fail. And even though we have used the correct function and we have used all the correct formats, still it is failing.

[05:18] The reason is the value which we have provided cannot be interpreted by Tosca as a date according to this particular format. So in Tosca this is the format which is currently set. And it will always try to interpret this as the right format. So from here it can convert it into a different format using the date function. If you're trying to put some other date which is in a different format then Tosca cannot interpret it as a date.

[05:56] So we have to change that interpretation of Tosca so that it considers this as a valid date. And how we can do that is by defining a test configuration parameter for our test case. So go into the particular test configuration and then from here we will try to add a test configuration parameter. Here we have to choose something called the Tosca date format.

[06:29] So it is a system defined test configuration parameter. And here we are going to choose any particular value. There are multiple values which you can choose from. And you can choose any particular format from here. So we want to choose this particular format because this is the format which we have provided. So I can choose this if you want any other format you can also choose that.

[07:01] So once you define this test configuration parameter now Tosca will be forced to consider this format as a correct valid date format. Now when we run this it should be running successfully. So now you can see that it was able to set the buffer with this date and then it was able to convert it into the specified format.

[07:34] So this is how you can basically change the interpretation of Tosca so that it considers a specific format as a valid date format because Tosca will have its own date format which it will always try to interpret as the correct date. So even though you know how to convert the dates using the different date functions this is also one aspect which you need to consider when you are working with different date formats and different applications have got a different date format.

[08:11] So this this way you can always work with those different formats. That's all for this particular video. If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
