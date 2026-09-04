---
id: "ucnJlmkhs04"
title: "Tosca Tutorial | Lesson 139 - Common RealTime Tosca Problems & Fixes | Tosca Date Format |"
url: "https://www.youtube.com/watch?v=ucnJlmkhs04"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 142
duration: 512
upload_date: "20240308"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:39Z"
status: "raw"
---

# Tosca Tutorial | Lesson 139 - Common RealTime Tosca Problems & Fixes | Tosca Date Format |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the TSA automation playlist so today I'm going to talk about another problem or issue which is generally faced by many people when they are working with tosa especially around date formatting now uh every application has got its own format of date and many times uh we need to perform date calculations and we need to also change a date to a specific format but uh the issue which happens is sometimes uh tosa will not accept the date format which you are trying to convert to okay uh because tosa has got its own uh format where which is either defined by the system where it is installed or it is defined within tosa itself okay so sometimes the conversion even though uh you can use the dated function to make the calculations and to make the

[01:15] conversion to a specific format but the source format will not be accepted as a valid format by tosa and then it throws up an error okay so I have come across this scenario multiple times and that is the reason I thought I would share this particular solution which is a very simple solution uh which you can apply all the time whenever you are trying to convert uh some date format into another date format but the date format which you're trying to convert may be of different format than what tosa accepts currently okay so uh let's look uh at an example for this right so this is the example uh where uh this is the date which has been provided to us which is today's date okay uh it is in a specific format which doesn't match with the format which I have currently on my system uh my system has a date format of uh DD mm and yyy but I have provided uh

[02:19] date which is yyy MM and DD okay uh and then we need to convert this particular date into this format right so this is uh the scenario this is what we need to do so uh let's go ahead and create a new test case folder here and I will call it dates okay and then I'm going to create a test case here called format date okay so the first thing which uh uh I can do is uh I can set a buffer here okay so I'm going to use the tbox set buffer and I'm going to call it today date okay and uh I'm going to define the date which I have picked so uh which is in a specific format we know that right so I'm going to give it a value like

[03:22] 2024 and then 03 and then 07 okay so this is the value which I have provided and now uh I'm going to convert this date into the specified format so I'm going to call it new date okay so this is again a set buffer um and here uh I am going to call the date function okay so we already know about the date function um you can do different types of calculations you can also uh change it to a specific format right so inside this we are going to pick up the buffer of uh today's date right so the buffer which we have already created so I'm going to use it here and then uh we'll leave this empty okay we are not doing any offset and after that we are providing a format here right so that format would be DD

[04:25] and then mm which will be in capital and then y y y okay so this is the format which we want it to convert um and then I'm going to close this okay so this is the new date this is the today's date okay um so everything looks good now um and we have used the right date function to convert it into a specific format right okay so we would expect this to run so let's go ahead and run this and let's see whether tosa can actually convert this date or not okay so what you'll notice is this test case will fail okay and even though we have used the correct function um and we have used all the correct formats still uh it is failing and the reason is the value which we have provided cannot be interpreted by tosa as a date

[05:25] according to this particular format okay so in tosa this is the format which is currently set okay and it will always try to interpret this as the right format okay so from here it can convert it into a different format using the date function but if you're trying to put some other date okay which is in a different format then tosa cannnot interpret it as a date okay so we have to change that interpretation of tosa so that it considers this as a valid date okay and how we can do that is by defining a test configuration parameter for our test case Okay so uh go into the particular test configuration and then from here we will try to add a test configuration parameter here uh we have to choose

[06:26] something called the tosa date format okay so it is a system defined test configuration parameter and here uh we are going to choose any particular value right there are multiple values which you can choose from um and you can choose any particular format from here okay so uh we want to choose this particular format because this is the format uh which we have provided okay so I can choose this uh if you want any other format you can also choose that so once you define this test configuration parameter now tosa will be forced to uh consider this format as a correct valid date format now when we run this it should be running successfully okay so now you can see that it was able to set the buffer with

[07:26] this state and then it was able to convert into the specified format okay so uh this is how you can basically change uh the interpretation of tosa so that it considers a specific format as a valid date format okay because uh tosa will have its own date format which it will always try to interpret as the correct date so uh even though uh you know how to convert the dates using the different date functions this is also one aspect which you need to consider when you are working with different date formats and different applications have got a different date formats so this uh this way you can always work with those different formats that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to

[08:26] our Channel thanks for watching and I will see you in the next video
