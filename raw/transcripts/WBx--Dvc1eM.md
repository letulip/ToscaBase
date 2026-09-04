---
id: "WBx--Dvc1eM"
title: "Tosca Tutorial | Lesson 150 - Common Issues | Download & Verify File | Curl | PowerShell |"
url: "https://www.youtube.com/watch?v=WBx--Dvc1eM"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 154
duration: 502
upload_date: "20240422"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:10:34Z"
status: "raw"
---

# Tosca Tutorial | Lesson 150 - Common Issues | Download & Verify File | Curl | PowerShell |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so now we are going to talk about a scenario where uh we have to download a particular file and maybe we have to perform some other things on that like maybe verifying a PDF file or verifying a image file or any particular file from your application right so this is the scenario now there are two ways of doing this either uh you can go ahead with the normal way of downloading a file which is when you click on that file then it downloads it into the downloads folder from there uh you can then uh transfer it into a separate folder or you can go ahead and verify in the downloads folder right um but this might be a lengthy process and sometimes it may be a little complicated there's a more easy way of uh getting this done uh using the curl

[01:14] command and uh you can use the Cur command in tosa as well okay so let me show you how you can do that now for this U I picked up um a sample application which has got a number of different download links you can can see here right so these uh all these download links we have to uh download this file maybe sample media. file.png okay and then uh we can also verify whether this file exists or not so um this is the scenario now how you can do that um as I said the usual way is to click on that and then it downloads and then you can go to the downloads folder but there is the other way um and that is using curl okay what is curl um it is a open source Tool uh it is a command line tool uh to transfer data using different uh Network protocols okay so uh the name stands for

[02:15] client for URL and that is called curl right you can download it for free um for Windows uh operating system right from here and uh it will get installed into your command line tool okay uh once it's downloaded uh you can go to uh CMD and here you can check whether it is downloaded or not okay so just type c and then help if it returns all this options that means uh it is installed on your system and uh you can use it now um we are going to use one of the parameters here which is this output parameter and uh in this output parameter it will download the file into this particular file location which we specify okay and there are other options also here so let's pick up an example okay so here uh if I come here and I can pick up some link I

[03:19] will copy the link address here and then come back here so here I'm going to type curl and then uh we need to put the link here of that particular file and then we have to type the parameter d o and then uh we can type the file path here okay so if I want to download it into a specific folder like this CM folder so I'm going to specify this followed by this file name so I'm going to keep it spectrum.png okay and then uh you will see that it has completed a download I can verify that going to my CM folder you will see spectrum.png is downloaded right so uh that's the way uh how you can download a particular file directly from your command line tool now uh we are going to do the same thing uh with tosa Okay so

[04:21] let's go to test cases and let's create a folder here we are going to call this download and then I am going to add a test case called download file okay and then we need to add a test step here which is called the tbox Start program so here uh we are going to start a program with some arguments and that program is the powershell.exe okay so we were going to execute this command in Powershell so I will start this and then um in the arguments the first argument would be Cur okay and then um we'll follow the same way how we have done it earlier this time let's pick up a different um

[05:21] file which we want to download I am copying the link address here and then come back here I am going going to pass this link here then the third argument is- o That's the uh parameter and then uh we are going to pass uh where we want to download it right so again I'm going to download it in cm file and I am going to specify the file name media.png okay so these are all the arguments also in wait for exit I will specify true here so it will wait for exiting the application and then let's go ahead and let's execute this okay so I'm going to execute this test case

[06:31] now and you will see here um it executed the powershell.exe with this arguments and then process stopped so how to verify whether it was downloaded well you can go back to the temp folder the media.png is saved here now coming to the next step uh which is to verify whether the file exists um not manually but through tosa so that can be done easily by adding another test step and here you can check for file existence so tbox file existence that's the module and here I just need to pass the directory where that file exists and I need to pass the file name here okay um and then the action mode will be verify now uh if I go ahead and just run this

[07:36] okay so you will see uh verification was successful and expected value found one match for this particular file okay so this is how it works uh you can use the curl command uh to download any particular file uh you can use the powershell.exe or the command line tool for Windows and then uh you can perform uh the verification whether that file exists or not okay so end to end scenario where uh you can download the file and then you can also verify the file that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
