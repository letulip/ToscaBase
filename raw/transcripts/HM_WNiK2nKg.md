---
id: "HM_WNiK2nKg"
title: "Tosca Tutorial | Lesson 28 - Open and Verify XML Files | XML Engine"
url: "https://www.youtube.com/watch?v=HM_WNiK2nKg"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 30
duration: 439
upload_date: "20230831"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:00:34Z"
status: "raw"
---

# Tosca Tutorial | Lesson 28 - Open and Verify XML Files | XML Engine

[00:08] hey there welcome to another interesting lesson on this Tosca automation playlist today I'm going to show you how you can verify XML files using the Tosca automation modules now for this particular example I'm going to use this books.xml it has got a some information related to different books it's a catalog of books with different um properties like ID author title general price and some other information now we are going to use the Tosca modules to basically scan this XML file and also do some verification like if you want to verify um whether some title of a particular book ID is as per our expected result or not okay so that's what we are going to do and for this I'm going to use two modules both are part of the XML engine so let's create a test case here called verify XML

[01:16] and then I am going to search for this modules so let's search with XML and I'm going to use the open create XML file and I'm going to use verify XML okay so these are the two modules which we can use uh the first module is to open or it can also create a new XML file so for this we need to give a resource now research could be anything uh for me I will just give it a name called books XML and then the file path okay so let's copy the file path here and let's come here and then paste it here so this is the file path now while verifying the XML file we need to provide the same resource which we used while opening it so we'll mention books XML here now we need to give the X path

[02:18] okay so in an XML file if you want to access any particular node you need to provide the path of that node in the XML tree okay so for example if we are looking at this XML file okay so if we want to Traverse to a certain book okay book ID we need to give the path of this particular node okay so whatever node we are trying to access we need to provide the path of it so the easiest way to do this um is either use um some tool to generate the expert or you can write your own expert if you know how to write it okay so that's what I'm going to do okay so to do that I will first go to this XML file and then I will click on right click and click on inspect okay so that will give me a kind of an XML tree okay with all the different nodes you

[03:19] can see here so here I can then press Ctrl F and then you will see there is a find by a text box okay where I can write and I can also verify my XPath okay so for example I want to verify the title of this particular book which is microsoft.net so in order to access this I need to write a relative expert so I'll start off by writing book okay so that will probably give me all the list of nodes which start with the book tag okay and then I'm going to say at ID equals I'm going to give it a value here so it's pk110 okay so this will filter it down to that specific book with this particular ID okay and then I'm going to access the title here so I'm going to write title and that will filter it out again to

[04:21] highlight the title here okay so this is probably the expat for if you want to access this particular node okay so as I want to verify the title I will take this node I will go back to Tosca and now I will paste it here now you need to take care of this particular Expressions because there are some special characters in this particular expert okay and you need to tell Tosca to escape the special characters otherwise it will throw some errors so you can go and right click on this and you can say Escape value okay uh that will escape the special characters here but again we need to escape this particular string value for ID okay so better we provide some quotes double quotes here okay so you need to put two double quotes one

[05:24] is for the X path and one uh it is still in Tosca to basically consider this as a string okay so this is how your expert should look like and now we want to verify something in the value okay so um if you look at this value it's microsoft.net and then the programming Bible um I don't want to write the whole text so I can use some regular expression here so I can write Microsoft and then I can put a star so that whatever text after that it can just verify that okay so any text which is uh starting with Microsoft and then um it can be anything after this okay so this way I want to verify the value of that particular title so I can do any number of verifications by giving the X part and then the value okay

[06:24] so let's go ahead and run this quickly and you will see that it will show you all the steps which it has performed and on the X path it will say verification was successful so expression was this actual value was this right so this is how you can verify any particular XML file using these two modules which are part of the XML engine and one is the open create XML file and the other is verify X summary that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
