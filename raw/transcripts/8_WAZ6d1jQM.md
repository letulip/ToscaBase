---
id: "8_WAZ6d1jQM"
title: "Tosca Tutorial | Lesson 99 - Use limited Module Attributes | Categorize | Best Practices |"
url: "https://www.youtube.com/watch?v=8_WAZ6d1jQM"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 99
duration: 388
upload_date: "20230720"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:06:05Z"
status: "raw"
---

# Tosca Tutorial | Lesson 99 - Use limited Module Attributes | Categorize | Best Practices |

[00:08] hey everyone welcome back to our Tosca automation playlist and we are talking about Tosca best practices now prior to this I have already shown you two best practices and this is the third in the series now if you want to watch our previous videos or if you want to watch our next videos I would like you to subscribe to our Channel first so talking about the best practice number three and it is about module attribute usage now we have seen what is a module and what are the different module attributes related to that particular module in Tosca and you create a module by scanning your application right so as per this best practice you should limit your module attributes and categorize them based on the module functionality now what do you mean by this is you should not add all the module attributes into a single module you should divide

[01:11] your model attributes as per the module functionality so create different folders create different modules are based on the functionality of the application you are trying to scan so let's try to understand this with the help of an example so I'll go back to my Tosca and here I have put together two examples okay both are for the same screen okay so we are trying to scan this enter vehicle data and there are several Fields as you can see right and some of them are mandatory Fields some of them are optional Fields And there are some headers some Footers on this particular page okay and I have scanned uh this particular page to create my module now I have done it in two ways okay so in the first way I have categorized my module attributes which are the fields in the application in different

[02:12] modules so you can see there is a headers module and there is a enter vehicle data module which contains the fields in that particular page and then there is also a headers module which contains the auto by link which is what I'm trying to scan okay and these are all the fields for the automobile screen now on the right hand side I have created the same module but in a different way now what I have done is I have scanned that page and I have added all my controls together in this single module now you may think that if you go ahead and scan all the elements on your page so you may not required to go back and scan that application or that page again so you can reuse this module for all test cases but that is not an efficient way of doing it and there are specific reasons for this so if you go ahead and

[03:13] create modules like this where you scan all the controls of your application and put together in just a single module firstly your performance will be impacted also in the long run your workspace size will also increase okay because even if you're not using the controls you are still scanning all the controls and keeping it in the modules okay rather than this what presenters suggests is create the modules but only use the model attributes which you are going to use it in your test case now if you want to use more controls than this okay so some other test case requires some other controls which you have not scanned um first time so you can always go back and rescan that particular window and add your additional controls but you should not go ahead and put all the controls or scan all the controls in

[04:14] just one module okay also you should categorize your modules the reason is pretty simple once you categorize you create a structure in your modules and when you drag this into your test cases the same structure is maintained so there is a test case flow with all the different steps which are nothing but your modules right now if I have got just one module and I'm trying to use that module in every test step then maybe uh you have to rename all the test steps and also while executing Tosca has to go through all the module all the module attributes in order to find that particular module attribute which may not be efficient right so think like this if I just need to click on the automobile link I just need to pass this module which has got just one module attribute but if I have to do the same thing in this example then there are so many module attributes out of this Tosca

[05:15] has to click on the automobile link right so it affects the performance of your Automation and also it slows down your execution also um it impacts your workspace size so there are lots of disadvantages as you can see and also you can also make out which looks better right the structured way is much better than the non-structured way right so transcendus always recommends this that use your modules uh in different categories okay categorize your model attributes and also uh make it more efficient don't add all the module attributes together right so that's all for this particular video I hope you enjoyed it and you learned something new today if you want to continue learning about best practices keep watching for uh the upcoming videos so until the next video keep learning and keep watching our

[06:17] videos
