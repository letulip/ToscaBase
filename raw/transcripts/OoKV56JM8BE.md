---
id: "OoKV56JM8BE"
title: "Tosca Tutorial | Lesson 11 - Performing File Operations | TBox Automation Modules |"
url: "https://www.youtube.com/watch?v=OoKV56JM8BE"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 13
duration: 697
upload_date: "20230210"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T07:58:57Z"
status: "raw"
---

# Tosca Tutorial | Lesson 11 - Performing File Operations | TBox Automation Modules |

[00:11] welcome back uh so in this session we are going to talk about some additional topics and we are going to talk about the t-box automation modules now there are several automation modules which are present in the standard subset provided by Tosca and you can use them for many General operations when you are working with your test cases so these are kind of a library which is available to you and you don't need to write any additional tests for performing all these operations now we are going to talk about some file operations folder operations uh numeric operations and some process operations which are available in Tosca t-box automation module so uh let's get started uh first with the file operations so for that I have created a folder in my test cases t-box modules and in this um I'm going to create

[01:11] another folder called file operations okay so inside this we are going to see many operations which you can perform on different files using this dbox automation modules okay so uh we'll first start with image compare how you can compare two images right so t-box has provided a module for it and we can use that so let's add a test case here and we'll say it compare images okay and then I'm going to add a desktop which is nothing but a module so I'm going to search t-box image compare okay so that's the module and once you add them you will see uh you just need to provide uh two things here first image file path and second image file path okay so either you can

[02:13] browse it or you can directly copy paste the path so I'm going to browse the path I have a folder where I have two images you can see right both look different so I'm going to compare these two images using this particular module okay so that's all we need to do here and then I can directly go ahead and run this in scratchbook okay as expected uh the verification field uh because the images were not same right so that was the expected result and moving on to our next uh t-box module uh and that is on how you can create different files uh in a particular folder using the t-box module

[03:15] right so let's call it create files okay and then I'm going to add the test step so let's search for t-box create and that's the third one t-box read create file so you can use the same module to read or create new files okay so let's select the directory um I will use the same directory which I have created so this one and then we have to give a file name here okay so it is the name of the file so I am calling it test1 dot txt and what text do you require in this particular file you can even create that or you can write it to the text file okay so I will call it this is a test right for creating

[04:16] files and then we have to provide uh encoding so you can either provide utf-8 or utf-16 okay so let's go with utf-8 override I will set it to true and add byte auto mark I will set it to true okay so these are the values which you need to provide when you are going ahead and adding this particular module okay um and let's go ahead and run this now and once it is finished you will see uh it has created a test one file in this particular folder right scratchbook will show the past result and as you can see the folder where we have given the location as it has created a file with the text what we have provided right so it's easy to

[05:17] create any particular file using this right and let's go ahead and see what other modules are present for uh the t-box automation module for file operations right so the next automation module which I can use is copy file right so now I have created a file let's see how we can copy file using this t-box module so again um let me search for t-box copy file okay and I can give a source and a Target directory right so let's take this as the source okay and then let's go ahead and let's copy this into some other folder Okay so let's go into C samples

[06:25] and then uh I have to give a Target file name okay so I'll call it test2 dot txt and override I will set it to true right okay so let's go ahead and run this right let's uh go ahead and check this now I am in the C samples folder as you can see and now I can see that a test 2 file has been created here okay so that's how you can copy any particular file not only txt files you can also copy XML files right so any files uh within your directories and now uh let's see how we can compare to particular files using our t-box module right so this could be useful whenever you are trying to compare files right Force whether they have the same

[07:26] content or not it's a very common scenario in your test cases so this could be uh very useful right so let's see t-box compare file compare okay similar to what we have for images this is for files okay so I need to give a first file path and the second file path okay so let's copy this particular file and create a new file here right so that we can test it and let's go ahead with the same content here and let's rename this file to test two okay so let's compare these two files now test one and test two and we will keep this as the same folder so C

[08:27] and training okay so let's go ahead and run this now right uh so in the log info you can see it is showing that contents of the file are identical right so we can also go here okay so as you notice uh there is no report file generated because put the content are same right so let's go ahead and change uh something in our test1 file right and save it okay so let's go ahead and run this again and this time around we should see some reports saying that it's not matching and what's the difference okay obviously the test case will fail

[09:28] because the verification has failed okay but let's go ahead and check the report so you can see uh it's a HTML report and uh it will show you uh something highlighted in red that this is what is not matching okay so this is the additional content and or this is the missing content in the second file okay so it is showing in red so that's the kind of report uh you can get if you're comparing two files okay so our final test automation module in this file operations is how to delete a file so let's uh rename this test case to delete file and let's go ahead and add the test step so search for t-box delete file okay so let's give it a file name here

[10:35] and it should be test one dot txt that's the file I want to delete so let's go ahead and run this and that particular file should not be present here now okay so that's how you can delete files uh and that's how you can use different t-box modules in order to perform different file operations like comparing images comparing files creating files copying files deleting files there's also some other t-box modules which you can um try for on your own which are like you can read the files as I showed you you can also move rename and you can also append uh to a particular file okay
