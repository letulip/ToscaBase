---
id: "WMatBr3w8UI"
title: "Tosca Tutorial | Lesson 127 - Search Table Cell Value | Constraint Action Mode | Obstacle 21 |"
url: "https://www.youtube.com/watch?v=WMatBr3w8UI"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 128
duration: 327
upload_date: "20240109"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:48Z"
status: "raw"
---

# Tosca Tutorial | Lesson 127 - Search Table Cell Value | Constraint Action Mode | Obstacle 21 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist continuing with our test automation obstacle topic let's look at our next obstacle which is called the table search now this particular obstacle contains a dynamic table with rows and columns and here we need to find whether a particular cell in this table contains this particular value which is 15 if it is present then uh the value should be true if not then false and accordingly we need to enter that into this text field so this particular table I can see there is 15 okay so I'm going to enter true here and then the obstacle will be completed so the same thing we need to perform using tosa so let's see how we can do this using tosa so coming back to our tosa workspace uh the first step as always is to create a new module so we will go to our

[01:12] obstacles folder here we will scan the application and from here we need to select just two elements one is the table okay and then the other is the text box so these are the two elements which uh we need to enter here and then I will copy this and change the module name here and then I will save it and close it okay and then uh coming to the test cases section so we'll go to our obstacles folder here we will create a new test case and then uh we are going to add the module here so here coming to obstacles and add the module here now uh we have got a table and we

[02:16] have got the text field right so uh what we can do here is in order to find any particular cell since this table is dynamic in nature so this 15 value can come anywhere right so any row any column so the best and the fastest way to do a search on all the rows and columns is to use the constraint action mode so we'll put a constraint action mode on this value which is 15 and depending on that it will filter out the row which contains this particular cell right once that is done then uh we can go ahead and we can buffer whether this particular element exists or not it will return a true or false so whatever value it returns it will be stored in a buffer and then that buffer value can be entered here okay so this is the whole process which we are going to follow so let's go back here uh and now we are

[03:16] going into the table so we need to find out the row and we know that the cell value is 15 right so this we are going to do a constraint so that the row will be filtered based on this constraint and then once that is done then uh we are going to say exist equals equals uh the buffer name so we are going to put this as bore exists okay and then we are also going to change this to buffer right so it will check on the row whether it exists okay if this cell exists then it will store that in the buffer whether it is true or false and once that is done then we can come to the text box and here we can enter the buffer

[04:18] value okay so that almost completes our obstacle so I'll change the bu state to complet it and now we are ready to execute so let's go ahead and execute this in scratchbook okay so as you can see in the background it entered uh true depending on whether that element was present or not and it will enter false if it is not present and the obstacle was completed right so this is how you can filter out rows based on the constraint action mode and also you can easily search any particular cell with any particular value using this constraint action mode and then you can use the buffer action mode to U basically buffer any particular value based on some condition for that particular row or column that's all for this particular video if you have any questions then please leave it in the comments if you

[05:19] like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
