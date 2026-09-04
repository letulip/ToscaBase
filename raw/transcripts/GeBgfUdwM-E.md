---
id: "GeBgfUdwM-E"
title: "Tosca Tutorial | Lesson 124 - Count Number of Rows | Dynamic Web Table | RowCount | Obstacle 18 |"
url: "https://www.youtube.com/watch?v=GeBgfUdwM-E"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 125
duration: 297
upload_date: "20240103"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:34Z"
status: "raw"
---

# Tosca Tutorial | Lesson 124 - Count Number of Rows | Dynamic Web Table | RowCount | Obstacle 18 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our obstacles topic let's look at our next test automation obstacle which is called lots of rows now in this obstacle uh we need to count the rows in the table and we need to input the count into the text field which is called the row count and after that uh we need to click on the button okay so these are the three tasks which we need to perform as you can see uh this table has got around five rows so you can count them and then uh we need to uh write five here in the row count and then click me okay so this is what uh we need to do through Automation and as you can see the table is dynamic so once I clicked on clickme the number of rows again changed right so you cannot just uh go ahead and do a static way of counting the rows you need to put a dynamic way of counting the rows and

[01:14] then you need to enter it into the row count so let's see how we can do this uh in tosa so coming back to tosa uh let's go ahead and now create our module so I'm going to scan this application and here we are going to select all the three um objects which we require so we require the table we require the text box and then we require the button or link which is called click me okay and then let me also rename this uh so that we we can find the obstacle and here and then save and close it okay and now coming back to our test cases so let's create another test case

[02:15] here for the obstacle and then we are going to add the module into this particular obstacle test case so let's go back here and drag our module here we you can see the table uh the text box and the button right so here what we need to do is use a property called row count okay so tosa provides you uh two properties one is row count one is column count uh in a table element using which you can easily find the number of rows and number of columns in the table okay so for this uh we will use the row count property here which which will be equals to a buffer because we'll be buffering that particular value okay so that uh we don't have any static values here it will always be dynamic okay so I'm going to call this rows and then uh I'm going to make this

[03:18] buffer okay so you can see uh it will calculate the row count and then it will pass it on to the buffer which is called Rose okay and then we can use that buffer to enter it into the text Fields so we'll use B of row and then finally we are going to click on this particular link okay so it's a pretty simple obstacle um you just need to know that you can use the rowon property to count the number of rows in any particular table okay so now I'm going to change this work state to complete it and now we can go ahead and execute this okay so as you can see it counted the number of rows which is 10 and then it entered it into the text box and then it clicked on the button and this completed the particular obstacle okay so this is how you can use uh the property row

[04:19] count or column count to count the number of rows and columns uh which are present in the table it may be a dynamic or a static table TOs will anyway count the number of rows and return the number of rows which can be buffered and stored in a buffer uh value which can be used uh in later steps in your test cases that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
