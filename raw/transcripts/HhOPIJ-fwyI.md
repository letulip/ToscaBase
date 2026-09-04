---
id: "HhOPIJ-fwyI"
title: "Tosca Tutorial | Lesson 116 - Extract Text | XBuffer | Dynamic Text | Obstacle 10 |"
url: "https://www.youtube.com/watch?v=HhOPIJ-fwyI"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 117
duration: 438
upload_date: "20231211"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:07:59Z"
status: "raw"
---

# Tosca Tutorial | Lesson 116 - Extract Text | XBuffer | Dynamic Text | Obstacle 10 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist now continuing with our topic on test automation obstacles let's look at the next obstacle which is called the extracting text now in this particular obstacle we need to automate a test step where we need to take the total amount which is shown in the success message uh which is here right and then uh we need to enter that uh amount into this particular text box okay so if I enter this particular amount here okay and then you will see that this obstacle is completed so this is all we need to do here right now the challenge here obviously is uh this particular text is dynamic which means the amount keeps on changing right right so you need to be able to extract this particular amount from this Dynamic text and then you need to enter it into the text box so let's see how we can do this uh in

[01:18] tosa okay so uh coming back to our tosa and here uh let's go to our obstacles and here I am going to now uh scan this particular application right okay so here um I can see the total amount text box but I cannot see uh this success message right so I'm going to increase the filtered items so that I can see uh some of the underlying elements here okay and this is the text uh which contains the purchase completed and then the total amount right and then uh I need to also select the text box okay so these are the two elements which I want and then uh we are going to call this success message okay and we are going to call the module but we will copy this

[02:21] obstacle here and we'll paste it here okay and then I'm going to save this and close the scan right so our module is created now uh let's go to our test cases section and here we are going to create a new test case uh again with the same obstacle uh ID and then let's go ahead and add the module to this test case right so we have got uh a Dev element which contains the text and then we have got a textt box right now uh we need to extract the amount from the text and that amount is dynamic so it keeps on changing right so the only way I can think of is we can buffer that particular amount right but uh we cannot simply buffer uh the

[03:22] complete text right that text uh contains that Dynamic element so in this case uh we have to use something called X buffer okay so using the X buffer uh we can basically verify the dynamic text as well as we can buffer that Dynamic element which is part of that text okay so let's see how we can do this now before we do that uh we need to look at this uh success message element okay so if you look at the properties you will see that the inner text actually contains the complete text right so it contains the amount and uh some of other text okay so we can use this inner text property to extract this complete text and from there we will try to extract the amount okay so let's go back here and then here um I'm going to use the inner

[04:24] text okay and then uh in this we are going to call copy this particular text but we are going to make it Dynamic okay so I'm going to copy this here and then uh we are going to remove this I'm going to put a regular expression here okay and then uh because this amount keeps on changing so I'm going to buffer this and in this case I'm going to use a x buffer Okay so uh we are going to use XB as you can see okay and then inside this we are going to provide the buffer name and I'm going to call it amount okay and you'll also change the action mode to verify okay so what this will do is it will verify this Dynamic text and also it will buffer this particular

[05:26] amount okay uh into the amount buffer name right now we can easily use that particular buffer to enter it into this particular text box okay so here I can just use the buffer the normal buffer and then I can call the amount here right so uh this is how you can extract a piece of um text which is maybe dynamic in nature uh from the complete text using the X buffer so you can buffer that particular uh text which you want to buffer and then you can use that buffered value uh to enter it into a text box okay so this is how you can solve this particular obstacle so let's change the work state here and then let's try and execute this and let's see um if it can enter that particular amount into the text box okay so as you can see it was able

[06:29] to extract the text and also it was able to enter it into the text box right so that completed our obstacle uh both the tasks were completed right so it did the verification here you can see and it was also able to enter that particular amount right so this is how uh you can use x buffer and buffer to basically um extract some Dynamic text and also use that text uh at various places in your test cases that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
