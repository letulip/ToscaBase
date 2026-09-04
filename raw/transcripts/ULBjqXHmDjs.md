---
id: "ULBjqXHmDjs"
title: "Tosca Tutorial | Lesson 128 - Meeting Scheduler Table | Buffer Action Mode | Obstacle 22 |"
url: "https://www.youtube.com/watch?v=ULBjqXHmDjs"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 129
duration: 368
upload_date: "20240110"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:52Z"
status: "raw"
---

# Tosca Tutorial | Lesson 128 - Meeting Scheduler Table | Buffer Action Mode | Obstacle 22 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our topic on test automation obstacles let's look at our next obstacle which is called the meeting scheduler now this is another Dynamic table or a stat I table which has got some calendar like structure with some timings and then the days and then the status of uh the meeting room whether it is available or not and out of this uh we need to find a room on Thursday uh 11 to13 is the timing and we need to find whether it is open or closed okay so basically this particular status right so on Thursday we need to find this particular timing and then we need to find the status whether it is open or closed and then we need to type that particular status uh in this uh text box so for me it is open right now

[01:14] so if I type this then the obstacle is completed okay so it seems to be a pretty simple one uh considering we have done some complex tables and uh this one is pretty simple the reason why it is simple is because uh it has already provided us the row okay and also it has provided us the column so the THS day refers to the column header and the 11 to 13 timing is the row header so once you know which row or which column you have to work on then it becomes a little easier now in some other scenario this could be more interesting or a little difficult when you don't know the timing okay so in this case it is fixed but think that um it is a dynamic timing so you need to find the status of that particular timing and it keeps on changing then it becomes a little interesting but for us uh in this

[02:16] particular case it is static so we'll go ahead and automate this uh in tosa so coming back to tosa the first step is again to scan this particular module so we'll go to our obstacles and here we will scan this particular application okay and I basically need uh these two elements one is the time table and the other is the result text which is a text box okay and then I'm going to rename the module with this obstacle number and then I'm going to save this and close this okay now uh going back to tosa again uh going back to test cases section and obstacles we'll be creating a new obstacle test case and then uh we are going to add the

[03:20] module to this particular test case Okay okay so we have got the table and the text now what we need to do here is pretty simple so we need to select the row and the row here is this right so 11 to13 is the text which is present in this particular row right so we can take that text directly and tosa will be able to select it with this particular text right so we'll go back here and in the row we will put this particular text okay so it will uh select the the row based on this particular text if it is unique if it is not unique then um we need to make some more adjustments but right now it is unique okay and then in the cell uh we can check that these are all the column headers which are displaying here so we need to select Thursday here and uh then instead of verify we

[04:21] will do a buffer okay and uh in this I will say bore status so it will be stored uh in this particular buffer name which is bore status and then in the result text I can just use the buffer okay so this time around I will use the send keys and inside this I will use the buffer okay so bcore status so this is all we need to do in this particular test case um and now let's change the obstacle to complet it and then uh let's try and execute this and let's see whether it is able to grab the status and enter it into the particular text box right so run this in scratchbook okay so as you can see it

[05:22] was able to grab the status based on the row name and then uh based on the column it picked up status which is present in that particular cell okay and then it entered it into the text box which completed the obstacle so a pretty simple obstacle you just need to know how to steer the web tables based on different row heading or the column heading or you can use different types of action modes based on your specific scenario that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
