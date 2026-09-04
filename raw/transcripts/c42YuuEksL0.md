---
id: "c42YuuEksL0"
title: "Tosca Tutorial | Lesson 61 - Synchronize Execution List with Test Cases | Execution Lists |"
url: "https://www.youtube.com/watch?v=c42YuuEksL0"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 61
duration: 330
upload_date: "20230827"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:02:45Z"
status: "raw"
---

# Tosca Tutorial | Lesson 61 - Synchronize Execution List with Test Cases | Execution Lists |

[00:06] foreign welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist in this session we are going to discuss how we can synchronize execution lists with the test cases but first let's understand why do we even need to synchronize this execution list with the test cases so whenever you make any changes to your test cases some of the changes are automatically synchronized with the execution list but some of the things are not synchronized automatically by Tosca and you need to synchronize them manually but first let's discuss what is synchronized automatically okay so any changes which you make directly to the test case whether you are changing any particular test step or you are changing any value here or if even if you are changing the name of the test case all these changes are synchronized

[01:09] automatically in your execution list so for example if I change the name of this test case now okay to Execute order you will see that the name is automatically changed in the execution list as well so the changes are getting synchronized automatically here but some of the changes like if I uh rename some of the test case folder or if I move the test case to another folder so these changes are not automatically reflected in the execution list so for example if now I move this test case to this particular new folder which is webshop from the demo webshop okay and if I look back at my execution list you will see that Execute order is still under the demo webshop folder it has not

[02:10] been moved to the other folder like we have done for the webshop right so if now I synchronize this okay so you will see that the test case is gone so that is how you can synchronize your execution list with your test cases changes so you have to right click on the execution list and then click on synchronize okay so it will automatically synchronize all the changes which you have made like here so now the test case fold the demo webshop does not have that particular test case right and that's what is being reflected here it has been moved to the other folder okay or if I am going to put this back into the demo webshop now okay and now let's go back and synchronize it again to see the change okay so it's still there also some of the changes like uh if I

[03:13] rename this folder from demo webshop to demo shop you will see that in the execution list that folder has not changed right so it is still demo webshop this is the test case folder which is it is referring to so it is still demo webshop not demo shop and if now I go ahead and synchronize this you will see it has changed to demo shop okay similarly if I add a new test case here on the demo shop okay so that particular new test case which is present in our test case folder is not automatically displayed under the execution list okay you need to synchronize whenever you are adding new test cases to your test cases folder so right click here again and do synchronize and you will see the new test case now appears here okay so all these changes are required if you

[04:13] have already created an execution list for your test case and then you are making those changes inside your test cases okay it is not required if you are still developing or if you have completely finished your test cases development and then you are creating an execution list so if you don't make any changes like adding new test cases removing the test cases from the folder or renaming the folders if you don't make these kind of changes then the synchronization is not required because all the remaining changes what you make in the test case would be synchronized automatically so you don't need to go and manually synchronize it is only required in these three scenarios when you change the folder names when you remove the folders or if you add more test cases to the test case folders so in all of these scenarios you to synchronize your execution list with

[05:14] your test case that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
