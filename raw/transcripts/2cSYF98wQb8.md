---
id: "2cSYF98wQb8"
title: "Tosca Tutorial | Lesson 125 - Get Last Table Row Value | LastContentRow | Obstacle 19 |"
url: "https://www.youtube.com/watch?v=2cSYF98wQb8"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 126
duration: 405
upload_date: "20240104"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:39Z"
status: "raw"
---

# Tosca Tutorial | Lesson 125 - Get Last Table Row Value | LastContentRow | Obstacle 19 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist now continuing with our test automation obstacle topic let's look at our next obstacle which is called the last row now in this particular obstacle we need to uh verify that the last row in the table displays an order value and then we need to take this value and put it on the text field okay so for example if this is the table then we need to grab this particular value here and then we need to enter it right here and then the obstacle will be completed now take note that this table is dynamically getting changed so this value won't be constant neither the number of rows will be constant right so this is very similar to the last obstacle where we found uh the number of rows which are present in a particular table and then entered it into a text field here we need to uh verify and grab the last value of uh

[01:16] this particular table okay so let's see how we can do this in tosa so coming back to our tosa workpace uh let's go to our module section and here we will go to obstacle and here we will be adding a new module right so let's scan the application and here we'll be adding uh two elements one is the table itself and then the text box okay so these are uh the two elements which we want and then let's save it and let's close it it okay so I'm going to rename the module first okay and then uh we are going to create a new test case under our obstacles folder uh with the same test case name

[02:18] which is the obstacle number okay and then we are going to select our module so let's grab the module and let's add it here and now uh we have got a table and a text box okay so right now in this table you can see uh the row element and the column element now there are two uh ways you can do this okay so we need to select the last row of this particular table no matter how many rows are there we always want to select the last row right so for this uh what we can do we can use two types of um Elements which are present here uh one is the this last dollar okay so when you select this dollar last then it will always select the last row of this particular table okay so whatever value it will contain you can find it using this particular row so once this row is selected then uh we just need to select the particular

[03:19] cell okay and uh we know that it is in the value colum okay so what I can do I can um go here and I can check that uh in the value column I have got this particular value right so this is what I want to grab okay so here uh instead of verification what I can do I can buffer this particular value okay and then um I can also put something here called bore Val okay so this is my buffer name where this particular value will be stored okay and once this is stored then um I can just go ahead and enter it into the text box okay so I can use the buffer so bore Val okay and then um it will be entered into this particular text box okay so I'll show you the other way as well uh let's first run this and let's check whether it is working or not okay so

[04:20] I'll mark this as completed and then I am going to run okay so as you can see uh it grabbed that uh particular value and it entered it into the text box okay now the other way around is uh instead of dollar last we can also use uh the last content row okay so dollar last content row so this will also select the last row so you can use any of these two elements which are already part of the table row element element type okay so now if I go ahead and run this in scratchbook again it will exactly do the same thing okay so this is how you can uh basically uh play around with uh

[05:21] different row elements so especially for first and last row there is already a option which is present for the row element you can see dollar one is always the first row then dollar n you can enter any particular row number and then uh the last uh the last content row would always um contain the last row and then you can also put uh you can also verify the headers or you can also verify whether uh it is the first empty row okay so these are the different uh types of uh elements which are already present in the table element type for the row element okay so using this uh we can uh basically find out what values are present for any particular row and we can buffer them we can verify them um and then we can use it across different test steps uh for our test case Okay so

[06:22] this is how you can basically automate your Dynamic web tables uh in your application using tosa that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
