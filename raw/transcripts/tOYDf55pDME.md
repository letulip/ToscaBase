---
id: "tOYDf55pDME"
title: "Tosca Tutorial | Lesson 135 - Future Date | LDay | Date Expressions | Offset | Obstacle 29 |"
url: "https://www.youtube.com/watch?v=tOYDf55pDME"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 137
duration: 325
upload_date: "20240221"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:21Z"
status: "raw"
---

# Tosca Tutorial | Lesson 135 - Future Date | LDay | Date Expressions | Offset | Obstacle 29 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our topic on test automation obstacles let's look at our next obstacle which is called future Christmas now this is related to a date format and here what we need to do is we need to calculate on which day Christmas 25 December falls in the next 2 years which means after two years what day would Christmas fall on it could be a Monday Tuesday Wednesday Thursday or Friday right so we have to write it as a word okay so in this Christmas is near and there is a text box enter the day so here we need to write the day and uh if we calculate then the ch Christmas after 2 years would fall on a Friday okay so that's basically the answer and that will solve the obstacle but we need to do this using tosa so let's see how we

[01:13] can achieve this particular automation using the date Expressions so coming back to our TSA workspace uh the first step is to get that uh module which contains that text box so I'm going to scan this quickly so here I'm going to just select the text box uh that is all uh what we need and I will also rename the module here and then save this and close it okay um so that is done next uh we need to add a test case so I'll go to our obstacles folder and I will create the test case here and then I'm going to add the respective module right here okay so here uh we need to use some

[02:15] Expressions uh which is the date expression but we also need to find out the day on which that particular date falls on right so for that uh we need to use some expression like uh the L day okay so what it does it uh provides you with the day according to the current system settings okay so the result could be a day uh which is stated in words okay so inside this you can then put your own date expression as given in this particular syntax and example right and the result would be a day so that's what this particular expression does okay now inside this we are going to write the date expression and as you know uh we can put a base date we can put a offset and we can also put a format but uh we don't require uh the format in this case we just require the base date and then we require the offset

[03:16] which is uh plus two years right because we are trying to find the date uh after 2 years right so we are going to write this particular expression so in this uh we are going to write the date uh so we know that it is the Christmas so 25 December so I'm going to write 2512 and then I'm going to write the current date or current year right in this 2024 and then um we are going to write the offset here which is plus 2 years right uh we will leave the format empty because we don't want to change the format here and then let's close this expression and this expression okay so that's all uh we need to do here we just need to write the correct expression which will provide us the result now one way to verify this is you can verify it right here so you can right click on this expression and click

[04:16] on translate value and uh it will provide you with the correct value which is Friday right and now we can use this to enter it into the particular text box right so uh this uh will input it into the text box so let's go ahead and run this now I'll change the work state to complete it and then let's try and uh run this in scratchbook okay so as you can see U the day which was Friday was entered into the text box and the automation obstacle was completed so you can use the different date expr questions to manipulate your dates based on the requirements of your test case and then you can run them um as per the requirements that's all for this particular video if you have any questions then please leave it in the comments if you like this video then

[05:18] please subscribe to our Channel thanks for watching and I will see you in the next video
