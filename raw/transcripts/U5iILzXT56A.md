---
id: "U5iILzXT56A"
title: "Tosca Tutorial | Lesson 12 - Performing Folder Operations | TBox Automation Modules |"
url: "https://www.youtube.com/watch?v=U5iILzXT56A"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 14
duration: 428
upload_date: "20230213"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T07:59:02Z"
status: "raw"
---

# Tosca Tutorial | Lesson 12 - Performing Folder Operations | TBox Automation Modules |

[00:10] now we are going to see how we can do different folder operations using the kbox automation modules so let's create another test folder here called folder operations where we'll create all our test cases inside this let's create our first test case which is to create a folder okay so let's create this test case and let's quickly add our ebox module so we'll call it t-box and create okay so that will appear as the Box create module or the Box create folder module okay and we have to give a path here so we'll use the same folder which we have been using for our testing so this is the c training folder and in override will set it to true but in the part I need to extend it so that I can create a subfolder inside that particular folder right otherwise

[01:12] it's going to just overwrite that particular folder so I'm going to call it folder one okay so a new folder should be created here as you can see in this particular training folder there is a folder one okay there is no files obviously but there is a new folder so our next operation folder operation is to copy a particular folder okay so let's say t-box or let's call it copy folder so let's add the module here quickly so we are going to search for t-box and copy right so there are two modules copy file and copy folder we are going to use copy folder here we are going to give the source path

[02:13] so our source path will be c training right let's copy this folder into somewhere else okay and I will probably use the other folder which I've been using which is the C samples so I'll copy this here as a subfolder right I can give the over right as true and let's go ahead and quickly run this okay so as you can see uh the contents of uh the training folder are now copied into the samples okay so the folder one is created or copied and the files are also copied right so that's how you can copy um a folder and its content from One path to another path okay and let's go to our third operation now so let's create a new test case here

[03:14] and we are going to call it to delete a folder okay so we'll see how we can delete a folder and inside this again let's add our module so t-box delete and we are going to select folder okay so it is asking for a path again give the path where you want to delete this so let's go ahead and delete this folder one okay and um if you want to delete everything inside that particular folder right so you can also give the recursive value as true okay so we don't have any files inside inside folder one but if we have and if it is set to true then it will delete everything okay otherwise it won't delete anything inside the folder one so uh let's go ahead and run this

[04:20] okay so let's go to the c training folder and there should not be any folder one because we have deleted it okay right um so what we are going to do is we are going to check for our final folder operation so that is to check for a folder existence Okay so check folder existence now this could be a interesting one because this could be a common one which you will use probably to check a particular folder is present maybe a reports folder or some test data folder before you run your test cases right so this could be a useful one for that let's go ahead and add the t-box module so check or it could be t-box folder existence okay so this is the module and here we just need to give the path of the folder

[05:22] which we want to verify right and that will just verify it okay so uh I think you cannot browse it so let's go ahead and give this particular path okay and let's go ahead and run this so the verification has passed uh verification was successful as usual it will give you an expected and actual value folder does exist expected value was this right should exist so this is uh in scenarios where you want to check uh whether that folder exists before any performing any operations in that right so what you can also do is basically have this test case right inside uh or the first test case

[06:23] in your folder operations okay so first you verify then you create right or and then you copy and then you delete what you can also do you can put if condition and put all this into one particular test case if you want to run through one test case with all different steps right so that also you can do but these are the different uh t-box automation modules which you can use for different folder operations and as we have seen earlier you can also use them for file operations okay
