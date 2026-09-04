---
id: "ym1ewJCAAJk"
title: "Tosca Tutorial | Lesson 134 - Extract XML | Scan XML | Buffer Values | File Scan | Obstacle 28 |"
url: "https://www.youtube.com/watch?v=ym1ewJCAAJk"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 531
upload_date: "20240220"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:16:16Z"
status: "raw"
---

# Tosca Tutorial | Lesson 134 - Extract XML | Scan XML | Buffer Values | File Scan | Obstacle 28 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So continuing with our topic on the test automation obstacles, let's look at the next obstacle which is called the getSUSE number. Now this particular obstacle is related to XML file automation. So here what we need to do is we need to download the XML file which is attached here called catalog. And then we need to manually download and save it.

[00:43] And then we need to read the file and extract the complete number including prefix of this particular ID or name with Tosca. And once we extract it, we need to enter that into this particular text box. So if I go ahead and click on this particular catalog link, it's going to download the file and save it into my downloads folder. So once that is done, then we will see what this particular file contains and what do we need to extract and what we need to enter into this particular text box.

[01:23] Okay, so the file is downloaded and let's go and look at this downloads folder and you can see the catalog. This is an XML file. Now if I open this, here you will see the different nodes and everything is inside this catalog. Node inside this we have got number, ID, prefix, number, and gender. And we have got a couple of records here. Out of this, we need to look out for the ID which contains the name Sue.

[01:56] Then inside this we need to actually extract both prefix as well as the number. And then you need to write this together in that particular text box. So if I copied this prefix and then I come here, so that's one part of the number and then the second part is the number itself. So once you write the whole number along with the prefix, then this particular automation obstacle will be completed.

[02:29] And this we need to do using Tosca. So there are a couple of parts in this particular obstacle and we'll see how we can complete this particular obstacle in Tosca. So coming back to our Tosca workspace, first let's go ahead and create our modules. Now here there will be two different modules and the reason is one of the modules will be related to the XML file because we will scan the XML file and create a module and then the next module will be the application itself which is the text box.

[03:09] So here I'm going to create a folder to keep both these modules inside this folder and then I'm going to rename the folder name with this obstacle number. So come back here and we are going to rename this. Now inside this, first of all, let's scan the XML file. Now XML file can be scanned using a different option so you don't need to use the application option here.

[03:42] We need to go to more and here we'll find the file scan. So it can scan the XML file. So we select the file scan then it will come up with this dialog where we have to select the XML file. So we will select this and we'll click on open. So that will create the module. So this is the module which contains the XML file and its contents. Now the next module which we have to scan is the application itself.

[04:13] So we will scan the application option this time and we will select the Chrome browser here and then here we will select the text box. Okay, so that's all which we require here and then I'm going to call this the number text box. Okay, and then I'm going to close this.

[04:45] I will save this. Okay, so this is the file and this is the text box and then let's go ahead and create our test case now. So we will go to our obstacles and we will create our obstacles here and then we will drag both the modules right here. Okay, so first we will drag the catalog request.

[05:17] And then we will also drag our text box. Okay and then let's look at this test case. Okay, so here we need to enter the number but first we need to extract the number. Okay and even before that we need to also open the XML file because once it's open then only we'll be able to extract any particular node. Okay, so for that we need to add another module here and that is called open create XML file and this will be our first step so I will drag it right here.

[05:58] We need to give it a resource name so we'll call it the catalog and then we need to give the file path. So I will browse the file path and I will select it and then we can pass the same catalog as the resource reference. So here it will pass the reference after it's open and then we can go to the respective node. Here we need to go into the ID. Okay and we know that we are looking for ID with the name Sue.

[06:33] Right and instead of verify I'm going to make it constraint so that it will select that particular node right and then we require the prefix and the number. So here I'm going to call this pre and I'm going to call this num and I'm going to buffer both of these values. Okay so once you buffer both of these values then you have got those numbers and now I can just use them here to enter this into the text box.

[07:08] So I will have two buffers here. First it will be the prefix and then it will be the number. So it will basically concatenate both of these. It will enter one by one into the text box. So this is all we have to do in this particular obstacle. Now let's go ahead and change the work state to completed and now we are ready to run this particular test case.

[07:39] So let's run this and see if it is able to complete the automation on this particular text box. Okay so as you can see it entered both the prefix and the number into the text box and that completed the obstacle. So this is how you can use different modules related to the XML to browse through or to go to a particular node and extract the nodes.

[08:11] So you can use the scan feature to scan any particular XML file so that you automatically get all the nodes in your module and then you can easily go through all the different nodes and extract the required node or any particular child node where you need that particular information and then you need to enter that into your application. That's all for this particular video. If you have any questions then please leave it in the comments.

[08:43] If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
