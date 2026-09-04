---
id: "PKNn-hsjh_Q"
title: "Tosca Tutorial | Lesson 112 - Multiselect ListBox | Cardinality | Explicit Name | Obstacle 6 |"
url: "https://www.youtube.com/watch?v=PKNn-hsjh_Q"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 113
duration: 443
upload_date: "20231130"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:07:31Z"
status: "raw"
---

# Tosca Tutorial | Lesson 112 - Multiselect ListBox | Cardinality | Explicit Name | Obstacle 6 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist now continuing with our obstacles topic so we are going to look at the next obstacle which is called the testing methods now this particular obstacle contains a multi- select test box which contains a lot of different testing methods which are supported by tosa and we need to select these testing methods from this particular list box okay so we need to select a functional testing and then we need to select GUI testing right and then we need to select end to end and exploratory right and then if all of them are selected then this particular obstacle will be solved now this this you need to do through automation right and to achieve this we need to uh use two different concepts in TOA so let's see what are these now to make it uh easier I have already scanned

[01:13] this particular module so I have selected these two controls which is the select drop-down or multibox and then the item itself right so you don't need to select all the items because they would be similar in nature right only the names are changing but all the properties will remain same for all the items so we don't need to select uh all the items separately that's not the ideal way of doing this uh we can just select one of the items and then as I said we need to use two different concepts here right so uh the first concept is uh we need to change the cardinality okay so the cardinality by default is is set to 0 to one which means uh you can only use this particular uh module attribute once right now here what we need to do is we need to uh click on this module

[02:15] attribute number of times uh for four different testing methods I need to click or I need to use this module attribute four times right so the cardinality uh helps you to basically um use the module attribute multiple times okay so if you change the cardinality if you increase the range then you can use it multiple times so what uh we can do here is we can just change the cardinality from 0 to 1 to 0 to n so I can use this particular module attribute n number of times okay the second thing which we have to do is we have to add a configuration parameter so right click on the item and then select create configuration parameter now here we need to use something called explicit name right now we have discussed about this earlier so what is explicit name

[03:15] and we need to set the value to true so what this will do is uh it will help me to rename this item in my test case itself okay so if I rename it in the module attribute then it will reflect it in the test case or test step but since I have to use uh different testing method names right like this so I want to change the item name uh in each test step okay so these are the two changes which you need to do at a module attribute level so you need to change the cardinality and then you need to add a configuration parameter which is explicit name set to True okay now uh let's build a test case out of this so let's go to our obstacles and here uh we are going to create a new test case I am going to use this particular obstacle as the test case

[04:19] name okay and then uh we can just drag the module right here okay so as you can see uh in the test step we have got the select drop-down and then we have got the item okay now uh as I said we need to use this particular item number of times right so what we will do is uh we are going to rename this item okay to different testing methods and then you will see that once you do that okay another item is already there so I can use this multiple times and this is due to the cardinality property right so since we have increased it to n number of times this will keep on adding this particular item as many times as you want okay uh so the action mode will by default set to input which means it is going to uh select or click on that particular item okay uh and now let's go ahead and add all the

[05:20] remaining ones so we need end to end testing okay so we also need to mention testing here otherwise it will not select it and then end to end testing right and then uh the GUI testing and finally uh we will add the explor okay and uh it can select all these module attributes based on these names and this is due to the explicit name okay so both the concepts are being used here and you can understand why we are trying to use this okay so this is all we have to do here so it will select that particular list box and then it will uh select all the items individually uh together and it will

[06:22] complete the rle okay so if I go ahead and execute this now okay so as you can see it selected all the items in the background and it was able to complete this particular uh ridle right so as you can see it selected all the different testing methods uh in the multi- select list box okay so couple of Concepts which was covered uh in this particular obstacle which was how you can select multiple items in a list box then um how you can use cardinality and also explicit name for a module attribute that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
