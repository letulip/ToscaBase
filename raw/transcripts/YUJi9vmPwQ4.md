---
id: "YUJi9vmPwQ4"
title: "TRICENTIS Tosca 16.0 - Lesson 48 | OBSTACLE #6 | Multiselect ListBox | Cardinality | Explicit Name |"
url: "https://www.youtube.com/watch?v=YUJi9vmPwQ4"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: "TRICENTIS Tosca Automation Tutorial"
playlist_index: 53
duration: 851
upload_date: "20240815"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:31:15Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 48 | OBSTACLE #6 | Multiselect ListBox | Cardinality | Explicit Name |

[00:14] hi everyone this is Ravi welcome to pren tasa Advanced Training as you all know I've already published 47 YouTube videos covering beginners level intermediate level and advanced level Concepts from past couple of videos onwards have started teaching you some realtime scenarios where you might encounter with different types of obstacles and how can we solve those obstacles while automating your test cases and this is our abstra six nothing but lesson six in terms of real time scenarios and lesson 48 in terms of overall trient tasa training please do subscribe to the channel Chanel click on Bell icon you'll receive notifications whenever I publish more videos and don't forget to like and share the video thank you in this lesson I'm going to teach you how can we solve

[01:16] for an obstacle where you need to select the list of items within multi select list Box by using cality and and explicit name Concepts so for that let us first understand what is the obstacle so this is our obstacle sixth obstacle testing methods which is categorized as hard so let's go for it so if you see here multi select list box select all testing methods that are supported by tasa if you see this is your multi select box where you can select all testing methods that are supported by Taska right so now I can select multiple options as well multiple

[02:18] options as well so now here you need to select these four options from this multi- select box so now for that let's go back to our trient tasa and here let's scan objects that are required to solve the problem okay so right click on obstacles click on scan and select application so this is the application click on scan so now let's see here let's expand this and you can see this is your multi select but but I don't see the items within the multi select I don't see items so for that let us expand the

[03:19] filter by clicking towards right so here if you see this is my multi select select your multi select object you can see here right side this is my ID multi select and tag select and let me select one of the item I don't want to add all the items instead I just want to add one item from the list of items okay let's select the functional testing here if you select the functional testing it says it is not uniquely identified so don't worry so if you see right side the properties right I can see here inner text tag if I select inner text it's going to uniquely identify but I don't want to do that because I would like to use only one

[04:20] item from the list and use the same item to select the rest of the items how by using explicit name I'm going to explain you okay so let's just keep only tag for the one of the item and multi select I selected ID and tag okay so now let's go back to your module and rename this module with abstrac name copy this and paste this and now save this and close xcan let's go back to trient toas so this is the new obstacle module that we added double click on this if you see here I can see there is multi select and functional testing in instead of functional testing I would

[05:21] like to name this as item so basically it's one of the item under multi select right I'm just naming that as item so here now let's go to properties click this right pin okay here so this shows you the properties of each element of your or each object if you see multi select I selected ID and tag for item I only selected tag so here because we need to select multiple items I have only one object captured means I can only select one item so to make sure I can use this item object multiple instances you have to look for coordin if you see here the coordin is showing

[06:24] as 0 to 1 that means you can use this attribute only once in the test step so now I would like to use this for how many times I have to use this for four times 1 2 3 4 right so that's why I would like to change this cality from 0 to 1 to 0 to N I don't want to only restrict for four times I want to put it as n multiple times n number of times you can reuse this object okay that is one thing and the other thing is you can use the explicit name concept here for that for item right click and add create configuration parameter I'll explain you how does this

[07:25] configuration parameter explicit name works okay explicit name so now you have to make this explicit name as true why I can start using the naming convention or index for this particular item object because I'm enabling the explicit name feature here or configuration parameter I'm enabling here okay so now let's keep it like this so what we did we have made two changes one is for item we changed the cordal from 0 to 1 to 0 to n because I would like to use the same item selection multiple times and also we added an explicit name because I would like to

[08:27] use this item to select different values as an item right one item is functional testing second is unit testing third is U GUI testing end to end testing right so the name of the value or the name of the item is different that's why I would like to use explicit name so that I can select different values from the multi select box okay so now let us go to obstacle and let me create a new test case and name this with the same obstacle name double click on this so now I would like to drag and drop this module to the test case to create our automation so basically now let us automate the test

[09:28] case for that I'm going to drag this module and drop onto the test case so now let us expand this you can see here now you have multi- select and item okay so here what I'm going to do here first I would like to use the explicit name here if you see first I would like to select one functional testing right copy this and here instead of item I would like to put functional is it small testing okay functional testing see as soon as I enter some other value a new item is displaying now that means a new attribute has been added let's say

[10:29] I'll do something here see here see it is adding one more I'm going to select this end to end like this okay but however so let's delete all this okay I mean let's rename this functional testing is one value second one is end to end testing the other one end to end testing you need to make sure the exact name match here okay and then GUI testing exploratory testing see as soon as I enter you will get one more so that means you can repeat this attribute multiple times n number of times so here I am first selecting action mode for multi select is select that means I'm

[11:32] just instructing tasar to consider multi select and then select the functional testing list item for that I need to use input and then select end to endend testing and then select GUI testing and then select exploratory testing so this coordin is used to repeat the attribute or this particular object multiple times and then I'm using explicit name to rename the attribute so that it selects item specified here from the multi list box okay so now let's chain work state as completed and save your test case now

[12:35] let's run the test case and see how it scratchbook you solve this automation problem see here it selected four values that we entered as an explicit name for your object so you can see here our test case is passed so if you have any queries leave your queries in the comment box I'll try to respond to your queries hope you all understand how can we solve an obstacle where you need to select the multiple items from multi select list Box by using

[13:37] cardinality and explicit methods by using tricentis tasa while automating the test cases please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos and don't forget to like and share the video thank you
