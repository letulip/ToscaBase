---
id: "GFVCsjV-8_w"
title: "Tosca Tutorial | Lesson 89 - Run Tosca Commander Tasks from Jenkins | CI/CD | DevOps |"
url: "https://www.youtube.com/watch?v=GFVCsjV-8_w"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 89
duration: 410
upload_date: "20230301"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:05:05Z"
status: "raw"
---

# Tosca Tutorial | Lesson 89 - Run Tosca Commander Tasks from Jenkins | CI/CD | DevOps |

[00:03] hey everyone welcome back again so today uh we are going to continue from where we left in our last session where we are talking about how we can execute or steer our Tosca Commander using uh the command line tool which is known as the TC shell we have also seen how we can even execute a particular execution list right from the command prompt using this DC shell right without opening the Tosca Commander now we are going one step further so here we still have a manual process like we are opening command prompt and we are entering some commands here uh to do some execution but what if we want to automate this whole process we don't want to open command prompt or don't want to enter in commands we just want to click um on a particular link or button and it should just execute right or even schedule our events at a certain time at a certain day or depending on some other conditions right so all of this is possible uh obviously with uh continuous

[01:06] integration tool like Jenkins so today we are going to see how you can perform all of these tasks in Jenkins right before I jump uh into Jenkins uh we will need a batch file Windows batch file in order to execute our script.tcs right so the script.tcs contains uh the commands which we want to execute but uh to execute this particular script uh we would require a batch file which can call this particular script right because we cannot execute this script file directly in Jenkins so I have created a execute.bat file and if I edit this particular file you will see that it contains the same commands which we have seen earlier okay so the First Command will open the commander home folder and then the TC cell command which will basically call the dot TCS file right so those are the

[02:07] two commands which are present in this patch file you can always create a batch file using a notepad just type the commands and then dot then just save it as a DOT bat file okay so let's go into our Jenkins now I have already logged it into my Jenkins local instance right if you are using a server instance the steps will still remain same there might be some minor changes or you have to maybe configure a little bit more but still you can follow the same process okay so for this uh I will create a new project here I will choose freestyle project I can also choose a pipeline right so let's give it a proper name here I will say Tosca execute underscore CI okay and click on OK now there are a lot of configuration

[03:07] which is present in Jenkins which you can configure for your project right you can give it a description you can do all this discard old builds right uh you can integrate it with the source code management tool like get you can schedule your bills using the build triggers uh either periodically or with get the same polling or pole SCM right so if you want to look at how to configure all of this in Jenkins you can go to my Jenkins playlist you will find all different videos present on these different options okay we don't require to configure all of this since we are running it on a local Jenkins instance I just need the build step okay so here I will do add build step and then I will say execute Windows patch command since I'm working on a Windows machine um and here I need to pass some commands so that I'm able to run that Windows batch file okay so for that it's pretty

[04:09] simple uh I just need to change the directory first to this particular uh directory and then I need to call execute dot bat which is the name of my batch file okay and then I just need to save it once I save it just make sure that Tosca Commander is not open with the workspace okay if it's normally open that's fine but if you have logged into the workspace then just make sure you have closed the workspace otherwise you will get uh some funny issues in Jenkins okay so after this uh just click on Bell now and the bill will start so we can even look at the console output here so the output in the console would still be very similar to what we have seen earlier uh in while executing it from the command prompt right so it will basically log into the workspace it will

[05:11] start the tasks what we have provided in that script file so no matter what you want to do you can just make your script file and then just run this patch file so it will just perform all the tasks which is present in that script file okay so as you can see the build is successful and that's how easy is to integrate Jenkins with your Tosca Commander right you can directly run your test cases or perform some other tasks write on your Tosca Commander using Jenkins you can even schedule your bills as I said earlier right so that's all about how you can run or steer your Tasker Commander using the command line tool which is TC shell and you can do it directly from Jenkins you just have to create a batch file which will be referring to the uh TCS script file and which will in turn perform all

[06:13] the different actions or tasks which um are there for the Tosca Commander right so uh if you have any questions just put them in the comments and I will certainly try to get back to you uh do look out for more videos uh which are coming up uh in Tosca there are lots of different topics which I want to cover so keep looking out for those videos in the coming updates
