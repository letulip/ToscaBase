---
id: "1t4hgmo42lM"
title: "Tosca Tutorial | Lesson 146 - Common Problems & Fixes | Get Total PageCount of PDF | PDF Scan |"
url: "https://www.youtube.com/watch?v=1t4hgmo42lM"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 471
upload_date: "20240408"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:30:52Z"
status: "raw"
---

# Tosca Tutorial | Lesson 146 - Common Problems & Fixes | Get Total PageCount of PDF | PDF Scan |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So in this session, we are going to talk about a challenging problem which you might come across when you are trying to test your PDF documents and you are trying to use the PDF scan in Tosca. So the problem here, or maybe the challenge here, is you need to count the number of pages in your PDF document, so you need to verify whether the PDF has got this many number of pages.

[00:47] Now the challenge here is if your PDF document doesn't have any particular element which tells you the page number, then it will be difficult to count the number of pages. Okay, so I have opened a sample PDF document and here you can see there are no page numbers mentioned here, right? So if I go till down, it shows me around 57 pages are there, right? And that you can count through the PDF application, but the actual PDF doesn't have any header or footer mentioning the page numbers, right?

[01:28] So here we need to count the number of pages which is 57 and then maybe we can verify that or buffer that and that's our requirement. So let's go to Tosca and let's see what is the actual solution here, right? So coming back to our Tosca workspace, the first step is to scan the particular PDF, right? So we'll go to modules, we'll choose scan and then choose the PDF option here and then in here in the PDF scan, we are going to select that particular PDF document, right?

[02:05] So I'll select that and click on open, it will open the document in the PDF scan. Now here the next step is to create a particular text area control, okay? So we are going to choose the control type as text. We are going to select any particular area in the page, okay? Doesn't matter which area you scan, I just want to create a control, okay? So here the control has been created and then I'm just going to save this.

[02:38] Then we'll close this and we are going to rename this to sample PDF and then let's look at the sample PDF. So here you can see this is the text area control and also a div element has been created. Now if you don't see this div element, then just select the module and press F12, which is the function F12 key in your keyboard and then this div element will be created, okay?

[03:11] Once that's created, go to the properties for this div element. Here you can see the page value is 1, so we are going to change this to asterisk, okay? Which is a regular expression value for this particular property. And then we'll close this, then we will go to the test cases section, we'll create a new test case folder called PDF. And here we will create a test case to count PDF pages, okay?

[03:47] Then we are going to add that particular module here. Now the first step is to provide the target PDF path. So we'll go to our PDF document, we'll copy the path here and paste it here, okay? And then in this particular div element, we are going to choose the action mode buffer and we are going to provide a buffer name, okay? That's page count.

[04:19] So this buffer will contain the number of pages for this particular PDF document. And then in PDF area 1, we are going to verify whether it satisfies the condition of value asterisk, which is again a regular expression, which means there is no specific text which we want to verify for this PDF area. We are verifying that it is any particular text. It doesn't matter.

[04:50] We want to get the count of the pages in the PDF document, okay? So what it will do is it will go through each page. It will try to get that PDF area with this particular value, which is asterisk, which is a regular expression, no particular text. So it can go through all the pages and then subsequently we can also store the page count in the buffer value, okay?

[05:21] So now let's see whether it's working or not. So let's change the work state to completed here and then let's go ahead and run this in Scratchbook. Now it might take some time depending on the number of pages in your PDF document, right? But once we get the success message, if we go into the Scratchbook logs, so here you will see in the results, it is storing the page count.

[05:57] So first is set to 1. Similarly, it will go through all the pages and you will get the final value in your buffer page count, which is 57, right? And then you will see verification was also successful here, right? Because it is trying to verify this particular expression, which will always be true, okay? We can also verify this in our buffer viewer. So we can go to Tools, Buffer Viewer, and here we can search for page count, okay?

[06:36] So you will see the buffer value is 57. So this is one way of finding the number of pages in your PDF document. You can either buffer it and then you can also verify it whether it matches your actual number of pages, which was the requirement. Now the other way around to do this is if you have got a PDF document where your header or footer contains that particular page number for each page in your PDF document, you can just scan that particular control, okay?

[07:07] And then you can buffer that particular value when you are going through each page. So you can mark it as a repetitive area in your PDF scan document and then you can run that and that will provide you the number of pages in your PDF document. So these are two ways through which you can solve this particular problem where you have to verify the number of pages in your PDF documents. That's all for this particular video.

[07:39] If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
