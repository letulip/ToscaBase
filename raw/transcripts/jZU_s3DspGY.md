---
id: "jZU_s3DspGY"
title: "Tosca Tutorial | Lesson 123 - Enter Tomorrow's Date | Dynamic Date Expression | Obstacle 17 |"
url: "https://www.youtube.com/watch?v=jZU_s3DspGY"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 124
duration: 323
upload_date: "20231229"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:30Z"
status: "raw"
---

# Tosca Tutorial | Lesson 123 - Enter Tomorrow's Date | Dynamic Date Expression | Obstacle 17 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our topic on the obstacles let's look at our next obstacle which is uh again a dynamic date generation so in this particular obstacle we need to input tomorrow's date in that particular text box so what do you mean by tomorrow's datee is whatever date is today and then you need to add another day uh to today's date and then you need to enter that accordingly so as you know uh the date would be dynamically generated otherwise uh the dates could be a problem if you execute it on different days right so let's see how we can do this uh in tosa so coming back here I am going to add the module here we just need the text box here right so I'm going to scan this

[01:26] application and then I'm going to add the date field okay so I'm going to rename this also and also we will rename the module okay and then I'm going to save this and close this okay so now coming back to tosa and in test cases we will go to obstacles and we'll create our new obstacle here and then uh we are going to add the module here okay so now we have to use the dynamic expression uh for date to generate tomorrow's date okay so for me uh in my system the date is 29 December as you can see

[02:26] 2023 and the tomorrow's date will be December 2023 which I need to enter into the text field okay so for this we are going to use the date expression you can see in the date expression we can calculate uh using the base State uh along with some deviations and also in a uh defined format right so here uh if we don't provide any base date it will take today's date as the base date okay so that's what I'm going to do and then then I'm going to put a offset of + 1 D and then I'm going to put a format here okay uh which is uh in the format which the obstacle is expecting the date to be generated okay so um here uh I'm going to put two square brackets which means I'm putting it empty I'm not providing any base date so it will pick the default base date which is today's date okay and then I'm putting an offset of + 1D which means uh

[03:30] it will calculate uh the offset as + one uh and today's date okay then uh the format so for this uh we will give DD mm and then y y y okay so this is the format which the obstacle is expecting okay and this is our data expression now if you you want to check whether this expression is correct or not you can also right click and click on translate value and it should give you the correct date okay so the expression is working correctly it is generating the dynamic date which is tomorrow State okay so now uh I will change this to completed and now we are going to run this uh in scratchbook okay so as you can see it uh enter tomor State and then um the

[04:33] obstacle was completed obviously um it did not detect that uh we have entered the date so whenever this happens we have already discussed you can always use the send Keys uh expression to enter any particular text into the text box okay but this is how you can use the dynamic date expression to generate any uh dynamically generated date and then you can use the offset to calculate uh in terms of days months or years and then you can also generate it uh on a specific uh user defined format okay that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
