---
id: "tOYDf55pDME"
title: "Tosca Tutorial | Lesson 135 - Future Date | LDay | Date Expressions | Offset | Obstacle 29 |"
url: "https://www.youtube.com/watch?v=tOYDf55pDME"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 325
upload_date: "20240221"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:09:10Z"
status: "raw"
---

# Tosca Tutorial | Lesson 135 - Future Date | LDay | Date Expressions | Offset | Obstacle 29 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So continuing with our topic on test automation obstacles, let's look at our next obstacle which is called future Christmas. Now this is related to a date format and here what we need to do is we need to calculate on which day Christmas 25 December falls in the next two years, which means after two years, what day would Christmas fall on?

[00:42] It could be a Monday, Tuesday, Wednesday, Thursday or Friday. So we have to write it as a word. So in this Christmas is near and there is a text box enter the day. So here we need to write the day and if we calculate then the Christmas after two years would fall on a Friday. So that's basically the answer and that will solve the obstacle. But we need to do this using Tosca. So let's see how we can achieve this particular automation using the date expressions.

[01:19] So coming back to our Tosca workspace, the first step is to get that module which contains that text box. So I'm going to scan this quickly. So here I'm going to just select the text box that is all what we need. And I will also rename the module here and then save this and close it. Okay so that is done.

[01:53] Next we need to add a test case. So I'll go to our obstacles folder and I will create the test case here. And then I'm going to add the respective module right here. Okay so here we need to use some expressions which is the date expression. But we also need to find out the day on which that particular date falls on.

[02:24] So for that we need to use some expression like the LD. So what it does, it provides you with the day according to the current system settings. So the result could be a day which is stated in words. So inside this you can then put your own date expression as given in this particular syntax and example. And the result would be a day.

[02:54] So that's what this particular expression does. Now inside this we are going to write the date expression. And as you know we can put a base date, we can put an offset and we can also put a format. But we don't require the format in this case we just require the base date and then we require the offset which is plus two years. Because we are trying to find the date after two years. So we are going to write this particular expression.

[03:27] So in this we are going to write the date. So we know that it is the Christmas, so 25 December. So I'm going to write 25-12 and then I'm going to write the current date or current year in this 2024. And then we are going to write the offset here which is plus two years. We will leave the format empty because we don't want to change the format here.

[03:57] And then let's close this expression and this expression. So that's all we need to do here. We just need to write the correct expression which will provide us the result. Now one way to verify this is you can verify it right here. So you can right click on this expression and click on translate value. And it will provide you with the correct value which is Friday. And now we can use this to enter it into the particular text box.

[04:30] So this will input it into the text box. So let's go ahead and run this now. I will change the work state to completed. And then let's try and run this in Scratchbook. So as you can see the day which was Friday was entered into the text box and the automation obstacle was completed. So you can use the different date expressions to manipulate your dates based on the requirements of your test case.

[05:06] And then you can run them as per the requirements. That's all for this particular video. If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
