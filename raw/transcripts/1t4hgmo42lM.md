---
id: "1t4hgmo42lM"
title: "Tosca Tutorial | Lesson 146 - Common Problems & Fixes | Get Total PageCount of PDF | PDF Scan |"
url: "https://www.youtube.com/watch?v=1t4hgmo42lM"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 150
duration: 471
upload_date: "20240408"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:10:14Z"
status: "raw"
---

# Tosca Tutorial | Lesson 146 - Common Problems & Fixes | Get Total PageCount of PDF | PDF Scan |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so in this session we are going to talk about a challenging problem which uh you might come across uh when you are trying to test your PDF documents and you are trying to use the PDF scan in tosa so the problem here or maybe the challenge here is uh you need to count the number of pages in your PDF document right so you need to verify whether the PDF uh has got this many number of pages now the challenge here is if your PDF document doesn't have any particular element which tells you the page number then it will be difficult to count the number of P pages okay so I have opened a a sample PDF document and here you can see um there are no page numbers mentioned here right so if I go till down it uh shows me around 57 pages

[01:15] are there right and that uh you can count through the PDF uh application but the actual PDF doesn't have any header or footer mentioning the page numbers right so here we need to count the number number of pages uh which is 57 um and then maybe we can verify that or buffer that um and that's our requirement so let's go to tosa and let's see um what is the actual solution here right so coming back to a tosa workspace the first step is to scan the particular PDF right so we'll go to modules we'll choose scan and then choose the PDF option here and then in here in the PDF scan we are going to select that particular PDF document right so I'll select that and click on open it will open the document in the PDF scan now here the next step is to create a particular text area control

[02:17] okay so we are going to choose the control Type S text we are going to select any particular area in the page okay doesn't matter which area you scan I just want to create control okay so here the control has been created and then I'm just going to save this then uh we'll close this and we are going to rename this to sample PDF and then let's look at the sample PDF so here you can see uh this is the text area control and also a div element has been created now if you don't see this div element M then just select the module and press F12 which is the function F12 key in your keyboard and then this St element will be created okay once that's created um go to the properties for the St element here you can see the page value is one so we are

[03:18] going to change this to asri okay which is a regular expression value for this particular property and then we'll close this then we will go to the test cases section we'll create a new test case folder called PDF and here we will create a test case to count PDF pages okay and then uh we are going to add that particular module here now uh the first step is to provide the target PDF path so we'll go to our PDF document will copy the path here and paste it here okay and then um in this particular Dev elment we are going to choose the action mode buffer and we are going to provide a buffer name okay and that's page count so this buffer will contain the

[04:21] number of pages uh for this particular PDF document and then in PDF Area 1 we are going to where verify whether it satisfies the condition of value um ASC which is again a regular expression which means there is no specific uh text which we want to verify for this PDF area we are verifying that it is any particular text uh it doesn't matter we want to get the count of the pages in The PDF document okay so what it will do is it will go through each page uh it will try to uh get that PDF area with this particular value which is um Astic which is a regular expression no particular text so it can go through all the pages and then uh subsequently we can also store uh the page count in the buffer value okay so now let's see

[05:22] whether it's working or not so let's change the work state to completed here and then let's go ahead and run this in scratchbook now it might take some time depending on the number of pages in your PDF document right uh but once you get the success message if we go into the scratchbook logs so here you will see in the results uh it is storing the page count so first is set to one similarly it will go through all the pages and you will get the final value in your buffer page count which is 57 right um and then you will see verification was also successful here right because it is trying to verify this particular expression which will always be true okay uh we can also

[06:23] verify this uh in our buffer viewer so we can go to tools buffer viewer and here uh we can search for pH count okay so you will see the buffer value is 57 so this is one way of finding the number of pages in your PDF document you can either buffer it and then you can also verify it whether it matches your actual number of pages which was the requirement now the other way around to do this is if you have got a PDF document where your header or phot contains that particular page number for each page in your PDF document you can just scan that particular control okay and then uh you can buffer that particular value when you are going through each page so you can mark it as a repetitive area in your PDF scan document and then uh you can run that and that will provide you um the number of pages in your PDF document so these

[07:27] are two ways through which you can solve this particular problem where you have to verify the number of pages uh in your PDF documents that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
