---
id: "KyyPVKyA60A"
title: "Tosca Tutorial | Lesson 137 - Select Random Combo Box Item | Random Text | Buffer | Obstacle 31 |"
url: "https://www.youtube.com/watch?v=KyyPVKyA60A"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 139
duration: 382
upload_date: "20240223"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:09:28Z"
status: "raw"
---

# Tosca Tutorial | Lesson 137 - Select Random Combo Box Item | Random Text | Buffer | Obstacle 31 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our topic on test automation obstacles let's look at our next obstacle which is called the obvious now this is one of the easy obstacles but the reason I'm showing you this obstacle is it's a pretty common scenario which you will encounter in your applications so it's quite useful to know how to get around this uh obstacle pretty easily right so in this particular obstacle we need to generate a random string by clicking on the button so once we click on the button it is going to generate a random string and then there is a dropdown okay and this drop- down contains one of these random strings okay so you don't know which random text will be generated but uh it is part of this particular list now you need to uh select a particular item from this list which matches that random text okay so in this case uh it starts with KY so if

[01:14] I select this and then I click on submit then the obstacle is completed okay so we have to automate this particular scenario using tosa so let's go to tosa and let's quickly see how we can automate this particular obstacle so first first of all uh let me quickly go ahead and create a module for this particular obstacle so I'm going to scan this application and we need couple of elements right here so we need the Generate random text then we need the text box and then uh we also need the select item box right so this is a select uh element which contains a lot of different elements right so these are the three uh Elements which we require and then we also require the submit button okay so actually four elements now let's go ahead and rename our module so to to match this particular obstacle

[02:16] ID and we are going to save this and uh we will close this okay so the next part is to add a test case so we are going here and and we are going to add a test case here okay and then let's add the particular module here with which we'll work with and now let's go ahead and look at the test steps right so the first test step is to click on this particular button so I will use uh X here to click on it and then uh it will generate a random text right now the next step is to store the random text into a buffer variable and for that we can use the action mode buffer so uh let's add another step into the test case okay and here we are going

[03:18] to use the buffer action mode I'm going to remove this particular module attribute because we have already uh clicked on this okay so we are going to now use the buffer action mode here and we are going to specify a buffer name let's call it R&D okay and then the next step is to uh select that particular uh randomly generated text in the select drop down okay so again uh we need this step where we will do this okay and we make sure that uh we remove any any other steps which have been uh included here or any other values okay and then in the select link we are just going to specify the buffer here okay so this is the buffer value which will be selected and then the final step is to click on the submit link

[04:18] okay so here we are again going to use the X to click on this so these are all the four steps okay so you need to use the module four times because we have got four different steps here and is always recommended to have just one action uh or one value selected in one of your modules right so uh you can always go ahead and rename all the steps so here it is to click on random uh button okay and then here uh we we are buffer random text and then here uh we select random text and finally we click on

[05:24] submit okay so now our test case is complete we will mark it as completed and uh now we will go ahead and try to run this in scratchbook okay so as you can see uh it clicked on the Generate random text it buffered uh the randomly generated text and then uh it used that buffer value to select it from the drop down and then it clicked on the submit okay it's a pretty simple obstacle as I mentioned earlier but it's a pretty common scenario which you will come across numerous times in your application so you should be comfortable uh with uh how to automate this particular scenario uh in your application using tosa that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
