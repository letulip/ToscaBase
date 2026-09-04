---
id: "zFHcStTuHbI"
title: "Tosca Tutorial | Lesson 96 - Use Test Mandates to execute same tests simultaneously | Multiple Users"
url: "https://www.youtube.com/watch?v=zFHcStTuHbI"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 96
duration: 390
upload_date: "20230914"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:05:47Z"
status: "raw"
---

# Tosca Tutorial | Lesson 96 - Use Test Mandates to execute same tests simultaneously | Multiple Users

[00:09] everyone welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist in this session we are going to talk about test mandates which is part of the execution section and it is only present uh in a multi-user workspace now we'll also try to understand why do we need test mandates and what is the importance of a test mandate so there will be scenarios when you are working in a multi-user environment where multiple users need to execute the same execution list which has been created and they should be able to execute it simultaneously also without overwriting each other's results now this would be a problem if multiple users are just using the same execution list then they will be overwriting each other's results so in order to avoid this problem Tosca provides you with another option which is known as test mandate it can be created in the execution section and then it can be linked to a particular test object which

[01:11] could be a execution entry execution list or execution folder so any of these objects can be linked to a test mandate so by using a test mandate then multiple users can run their execution simultaneously without overwriting any results so let's see how we can use this and how it can be linked to different test objects and then um how should you look at the results when it is linked to a particular test mandate so here in the execution list folder we can create a dust mandate so let's go out and check out this whole tree and then we'll be using this login test to link it to a test mandate and then I will go ahead and execute it so inside the execution list folder when you right click you will find there is an option called create test mandate so click on that and this is our test mandate so we'll say login mandate

[02:14] okay and then in order to link any particular object to a mandate you just need to drag and drop it into the Mandate what Tosca will do it will create a copy of your execution list okay as a folder here as you can see and then it will contain the test case also in the execution list you will see that on the log there will be a blue arrow okay which will tell you that this is linked to a particular uh mandate test mandate okay Now using this test mandate multiple users can execute this test mandate without even checking out the actual execution list so they don't need to execute the execution list but instead they will be executing this login mandate which will in turn give you the results back in the test object which is the execution list right so finally what will happen is once everybody is done

[03:17] their executions and the results are checked in then all the results will be collated together and displayed in the test mandate so now if I go ahead and check in all right and now you can see this is our login mandate which contains the login execution so we can go ahead and check out this now I can go ahead and run this test mandate okay without even checking out the login test which is the execution list so let's go ahead and run this so once the execution is completed you will see whether it is passed or failed right and then you can also go to your execution list and let me first check in all and then here you will see that the latest execution is linked to the test

[04:19] mandate okay so the results of the test mandate is also shown here okay in the execution list so without even executing the execution list by executing the test mandate you got the results back here so if multiple users are going to execute the test mandate it is never going to rewrite the results it will it will collate all the results and store it in the execution list also if you go to the execution list and if you want to go to your test mandate entry then from the logs itself you can jump to the test mandate entry there is an option here okay so click on that and it will take you to the test mandate entry now if finally if you don't want uh to keep the link between your test execution list and the test mandate then you can even remove that link so uh go to your execution list and then check this out

[05:20] and then right click on the actual log and there you will find there is a clear Auto merge list okay so when you click on the clear Auto merge list it will clear out the link between the test mandate and the execution list so you will see now that uh the latest execution log is no mode linked to the test mandate okay so the link has been taken off so now the test mandate result will not be shown here okay so this is how you can use the test mandate in a multi-user environment where multiple users can execute the test mandate without overwriting any results and then you can collate all your results in the execution list without even checking out the execution list or without even executing it you just need to link the execution list to your test mandate that's all for this particular video if you have any questions then please leave it in the comments

[06:21] if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
