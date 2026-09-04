---
id: "ym1ewJCAAJk"
title: "Tosca Tutorial | Lesson 134 - Extract XML | Scan XML | Buffer Values | File Scan | Obstacle 28 |"
url: "https://www.youtube.com/watch?v=ym1ewJCAAJk"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 531
upload_date: "20240220"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:29:30Z"
status: "raw"
---

# Tosca Tutorial | Lesson 134 - Extract XML | Scan XML | Buffer Values | File Scan | Obstacle 28 |

[00:10] Hello everyone, welcome back to our channel. I'm back with another interesting topic on the TSA Automation Playlist . So let's continue our topic on test automation barriers . Let's look at the next obstacle, called 'get s number' . Now this particular restriction is related to XML file automation . So what we need to do here is download this XML file called catalog , save it manually, then read that file and extract the integer including the prefix of this particular ID or name through TSA . Okay. Once you have it, you need to enter it into this specific text box . Okay.

[01:04] So if I click on this catalog link , it will download the file and save it to my Downloads folder. Once that's done, let's see what's in this file, what we need to take out, and what we need to enter into this text box. Okay. The file has been downloaded , now let's look at our Downloads folder, there we can find the catalog file. This is an XML file. Now if I open this up, you'll see there are different nodes, all within this catalog .

[01:43] The node inside this has a number ID, a prefix number, and a jer (jer ), and there are some records here. In this, we need to search for an ID with the name sue, then we need to take the prefix and number within it. Okay. Then you need to write this together in that specific text box . Okay. If I copy this prefix and come here.

[02:15] Okay. This is part of the number. The second part is that number . Okay. So if you write the whole number with the prefix, this particular automation ban will be lifted , which we need to do using TSCA . Okay. So there are two parts to this ban , let's see how to complete this in TSCA. Okay. Now let's return to our TSA workspace.

[02:47] First, let's create our modules . There will be two different modules here . Okay. The reason for that is that a module is associated with an XML file, because we will scan the XML file and create the module , the next module will be the application i.e. that text box. Okay. I'm going to create a folder to put these two blocks in , then I'm going to rename this folder with the number of this block . Okay.

[03:26] Now we're going to come here and rename this . Now let's scan the XML file first . Okay. Now you can scan the XML file using a different option . So, you don't need to use the 'application' option here. We need to go to 'more' , where we will see 'file scan' . Okay. This will allow you to scan the XML file . So, we select 'file scan' . Then this dialog box will come up, in which we need to select the XML file . So, let's select this and click 'open' . Okay.

[04:00] It will create a module. Okay. This is the module containing the XML file and its contents . Now the next module we need to scan is the application. So, this time we will scan the 'application' option and select the Chrome browser here . Then we will select the text box here . Okay. That's all we need here . Then, I'm going to call this 'number' . Text box. Okay.

[04:43] Then, I'm going to close this. I'm going to save this. Okay. So this is the file and this is the text box, now let's create our test case . So, let's go to our obstacles and create them here . Then, let's drag these two blocks here . Okay. First we'll drag ' catalog request' , then we'll drag our text box . Okay.

[05:25] Now let's look at this test case. Okay. Here we need to enter the number, but before that we need to extract the number. Okay. Before that, we need to open the XML file , because only if it is opened can we extract any specific node. Okay. For that we need to add another module here, it is called ' open create XML file' , this will be our first step . So, I'll pull this here .

[05:57] This requires a resource name . So, let's call it 'catalog', then we need to give the path to the file. So, I will search for and select the file path , and then I can pass the same 'catalog' as a resource reference. Here, it will send the note after it is opened , after which we can go to the respective node, here we have to go into the ID . Okay.

[06:28] Also, we know we're looking for an ID named Sue, right? Instead of verifying, I'm going to turn it into a constraint so that it selects that specific node , right? Then we need a prefix and a number, so I'm going to call this 'pre'. I'll call this ' num' , and I'm going to buffer these two values . Okay. After buffering these two values , you will have those numbers , and now I can use them to enter them into the text box . Okay. So here I'm going to have two buffers .

[07:12] First there will be a prefix, then there will be a number. Okay. So this will basically concatenate these two. This will be entered into the text box one by one . Okay. That's all we have to do in this particular task . Now let's change the work state to 'completed' . Now we are ready to run this particular test case . Okay. Let's run this and see if we can complete the automation in this text box.

[07:52] Okay. As you can see, it has completed the task by inputting both the prefix and the number into the text box . This way you can browse through various XML-related modules or extract nodes by going to a specific node . Also, you can use the scan feature to scan any XML file , so that all the nodes are automatically available in your module, then you can easily check all the nodes and extract the required node or a specific child node , where you can get the information you need and enter it into your application.

[08:39] That's all for this video. If you have any questions , please ask in the comments . If you liked this video , please subscribe to our channel. Thanks for watching, see you in the next video
