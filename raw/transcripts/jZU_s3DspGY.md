---
id: "jZU_s3DspGY"
title: "Tosca Tutorial | Lesson 123 - Enter Tomorrow's Date | Dynamic Date Expression | Obstacle 17 |"
url: "https://www.youtube.com/watch?v=jZU_s3DspGY"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 323
upload_date: "20231229"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:51:40Z"
status: "raw"
---

# Tosca Tutorial | Lesson 123 - Enter Tomorrow's Date | Dynamic Date Expression | Obstacle 17 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So continuing with our topic on the obstacles, let's look at our next obstacle which is again a dynamic date generation. So in this particular obstacle, we need to input tomorrow's date in that particular text box. So what do you mean by tomorrow's date is whatever date is today and then you need to add another day to today's date and then you need to enter that accordingly.

[00:48] So as you know, the date would be dynamically generated. Otherwise, the dates could be a problem if you execute it on different days. Right. So let's see how we can do this in Tosca. So coming back here, I am going to add the module here. We just need the text box here, right. So I'm going to scan this application and then I'm going to add the date field.

[01:27] OK, so I'm going to rename this also. And also we will rename the module. OK, and then I'm going to save this and close this. OK, so now coming back to Tosca and in test cases, we will go to Obstacles and we'll create our new obstacle here.

[02:03] And then we are going to add the module here. OK, so now we have to use the dynamic expression for date to generate tomorrow's date. OK, so for me, in my system, the date is 29 December, as you can see, 2023. And tomorrow's date will be 30 December, 2023, which I need to enter into the text field.

[02:33] OK, so for this, we are going to use the date expression. You can see in the date expression, we can calculate using the base date, along with some deviations and also in a defined format. Right. So here, if we don't provide any base date, it will take today's date as the base date. OK, so that's what I'm going to do. And then I'm going to put an offset of plus one day.

[03:03] And then I'm going to put a format here. OK, which is in the format which the obstacle is expecting the date to be generated. OK, so here I'm going to put a two square brackets, which means I'm putting it empty. I'm not providing any base date. So it will pick the default base date, which is today's date. OK, and then I'm putting an offset of plus one day, which means it will calculate the offset as plus one and today's date.

[03:37] OK, then the format. So for this, we will give DDMM and then YYY. OK, so this is the format which the obstacle is expecting. OK, and this is our date expression. Now, if you want to check that this expression is correct or not, you can also right click and click on translate value. And it should give you the correct date.

[04:09] OK, so the expression is working correctly. It is generating the dynamic date, which is tomorrow's date. OK, so now I will change this to completed. And now we are going to run this in Scratchbook. OK, so as you can see, it entered tomorrow's date. And then the obstacle was completed. Obviously, it did not detect that we have entered the date.

[04:40] So whenever this happens, we have already discussed. You can always use the send keys expression to enter any particular text into the text box. OK. But this is how you can use the dynamic date expression to generate any dynamically generated date. And then you can use the offset to calculate in terms of days, months, or years. And then you can also generate it on a specific user defined format. OK, that's all for this particular video.

[05:11] If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching, and I will see you in the next video.
