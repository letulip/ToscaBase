---
id: "bhuotHSk12Q"
title: "Tosca Tutorial | Lesson 73 - Using Tosca Query Language(TQL) Search with Virtual Folders | Reporting"
url: "https://www.youtube.com/watch?v=bhuotHSk12Q"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 613
upload_date: "20230308"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:01:55Z"
status: "raw"
---

# Tosca Tutorial | Lesson 73 - Using Tosca Query Language(TQL) Search with Virtual Folders | Reporting

[00:01] Hey everyone, welcome back to another interesting Tosca lesson. Today, I'm going to talk about how you can perform a TQL search and how you can store them in different virtual folders. Now coming to TQL, it stands for Tosca query language and using this you can basically construct different complex queries. Using this TQL search, you can do complex search on your workspace and it will return you with all the different objects which matches that search criteria. Okay, so talking about search in Tosca, there are obviously two options.

[00:41] When you go into the menu on the top, you will see there is the search and everything is integrated in this one window. So you have got two types of search here, Simple and TQL and you have also got an option to directly store your TQL search into a virtual folder on the right hand side. So when you do a simple search, it is just entering some text and then trying to find what objects are associated or are a match for this particular text.

[01:13] So if I click on search now, it will return me all the objects which are a match for this particular text. So that's simple search, nothing too spectacular about it. But when you come to TQL search, that simple search is now converted into a query language, which is defined by Tosca. It has its own grammar and operators. So if you want to use this, you have to understand some things about this particular query language. Now the TQL search queries tend to consist of many sub-expressions. So you can see this is an expression, then subparts is an expression and then this is like a logical expression where we are comparing or we are using this operators equals to question mark where it searches for all the different objects which contain this particular text. Okay, so if I want to change this search a little bit

[02:13] and if I make this name equals equals Google, you will see the lesser number of results which are displayed now and that is because it will try to search for an exact match. Previously it was not an exact match, it was just any particular object which contains this particular text. So that's how you can basically play around with this TQL search query. Now let me show you another example where a search could be useful in terms of your executions.

[02:45] So if you want to find out if your executions, all the test cases have passed or failed or does the execution list contain any test cases or not. So things like these you can easily search through a TQL. So these are basically some logical kind of search and not any typical search which you can do through a simple search. So for this, let's try and use this subparts. We are in the root folder so it will display all the subparts which contain this particular or which basically satisfy this search criteria.

[03:25] So we are going to look for execution list here. And then here you can see that it shows me all the execution lists which are present in this particular workspace using the subparts and these are all the execution list which are present currently. So if I want to filter out these results which is currently shown here you can see there are a number of different options and there I can see number of test cases failed, number of test cases passed. So what I can do, I can do the search like number of test cases passed is greater than one.

[04:05] And then if I search it will return me this result where this particular test case or execution list has got a number of test cases passed greater than one. Okay. And similarly I can say number of test cases failed equals to zero or I can say less than one. Okay. And it will give me three different execution list where number of test cases failed is less than one which means most of the test cases have passed.

[04:42] Okay. So things like this you can do a tql search based on you can do it on requirements on modules on test of values on execution lists on test cases. Right. So whatever you want to do you can do it using this tql search. You just need to get used to this structure how this doskar query language is structured with different sub expressions and operators. So you just need to take care of that and then it will find you all the objects for you. Okay. Now the next thing is virtual folder now virtual folders as the name suggests it it doesn't have any linked to any particular or any assigned objects.

[05:32] It only contains the search function. Okay. So whatever results you are getting from the tql search it will be displayed in a virtual folder so you can save the results in this particular folder and then whenever you want you can go there and you can fetch the latest results from the workspace. So it's basically it's easier to access your search results rather than going into the tql search and always entering a particular search query and then looking for the results you can go to that virtual folder and you can directly open that. Okay.

[06:08] So let's go ahead and see how we can basically create a virtual folder at any place so you can create a virtual folder except the root folder or the root project right you can create it at any folder level baby beat execution modules requirements test cases now reason I cannot save this as in directly into virtual folder is because I am in the root project. Okay, so you cannot save it here. So the other way around is go to a particular folder like test cases and then here let's create a virtual folder. So when you right click on any particular folder there will be a option to create a virtual folder click on that and then it will ask you to rename it you can or you it's not necessary to rename that virtual folder, but if you have many virtual folders, it's better to rename it. Okay. Now the most important part of virtual folder or the most important requirement is

[07:08] to enter a query which is basically your TQL query right? So when you go to properties and open that it will ask you to enter a particular TQL query right? So let's see what we can build here. Okay, so I am in the test cases folder. So I will use the subparts. And then I will use this time the test case. Okay. And inside test case what I want to see is what test cases were created by me. Okay. Now this will be useful when you have got a number of different users in your workspace. Okay, if you want to see who has created how many test cases so that could be a good report for the management team, right? So you can provide this report directly from this virtual folder. Okay, so you can easily see who has created how many test cases and

[08:08] you can even see when it was created by just editing this query. Okay, so here it is I am the admin user here. So I will say created by equals equals admin and then I will click on okay and you will see a list of different test cases being shown here. Okay, so you can see there are so many test cases which are now contained in this virtual folder. Okay, now I can even modify this. Okay, you can also always get the latest results by right clicking and clicking on this refresh virtual folder. So if something has changed it will not automatically change in the virtual folder. You need to refresh it.

[08:56] Okay, so once you refresh it you will get the latest results here. You can always edit the query from here. You can also create a report from virtual folder. We will see that later but if you have a virtual folder you can create a report. There will be an option to do that. Okay, so that's all the usage of a virtual folder how you can create it and how you can use it. Okay, now you can do a lot of other things as I said you can even filter this results based on if the test cases was marked as complete, if it was a template, if it has not been completed, how many has been completed, so many things you can do with this virtual folders. So you can create a number of different virtual folders and then for analyzing the results or reporting the results you can use this virtual folders which you can then bring into your reports. Okay, so that's all about

[09:57] the TQL search and how to create virtual folders and how to use it. Hope it was helpful and look out for more interesting videos coming up very soon.
