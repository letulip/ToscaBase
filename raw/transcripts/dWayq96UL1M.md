---
id: "dWayq96UL1M"
title: "Tosca Tutorial | Lesson 111 - Complex Table Interactions | Dynamic Rows  | Obstacle 5 |"
url: "https://www.youtube.com/watch?v=dWayq96UL1M"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 112
duration: 351
upload_date: "20231128"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:07:24Z"
status: "raw"
---

# Tosca Tutorial | Lesson 111 - Complex Table Interactions | Dynamic Rows  | Obstacle 5 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the TOs automation playlist so continuing with the obstacles and coming on to the next obstacle which is on the complex table interactions so as per this obstacle we need to click the edit button for John do okay and this is the row as you can see now the complexity behind this and why it is a hard obstacle is because if I refresh this page you will see that uh the row will keep on changing so as you can see this particular row where John do exists it keeps on changing as I keep on refreshing the page so there is no guarantee that when you open the page uh this will still be in the same row right so it is dynamically changing and we need to use the constraint action mode to basically uh find out the row where this particular uh data exists and then

[01:12] uh we need to also click on the edit button okay so this is what we need to do so the first thing is obviously uh we need to scan that particular table so I'm going here and I'm going to scan the application okay so here uh I'm going to scan the application and then uh we are going to use the table here and also uh we are going to add this edit button okay so for now it will show that the selected item is not unique because there are lots of different edit buttons on the rows but don't worry about this we will take care of this automatically when uh we write the test case okay so I'm going to rename this module to this particular obstacle okay and then I'm going to save and I'm going to close right uh so now coming back here uh we have got our obstacle and then

[02:14] let's go to our test cases folder here I'm going to create a new test case and rename it with that particular uh ID of the obstacle and then um I'm going to drag the module right here so inside this you will see that we have the table and then we have got the edit button right now if you look back at this module uh you will notice that this table is not organized uh in the same manner as it is displayed on the web page why because every row has got these two buttons right and we need the edit button but uh it should be under this particular row right or any particular Row in the table but if you look at this module the edit button is outside the row or column it is inside the table which is not correct right because uh if I'm selecting any row then I want to click on that particular edit button right so we need to decide this dynamically um and to do this what we

[03:16] will do is we will uh change this position of uh this particular element and uh will put it from the table to a particular row okay so what we're going to do uh we are going to drag this edit control and put it inside the row so that along with the cell we have also got the edit button okay so you can rearrange the module attributes as you like within the module okay so here now if I come back and now you can see under the table we have got the row we have got the cell and we have got the edit button right so the first job is to obviously find out the the row uh which contains that particular value right and for that I'm going to the cell value here and I'm going to go with the first name uh now we know our first name is John and I'm going to change this action mode to constraint okay now also you will notice

[04:18] that uh John is not the unique first name there are two rows with the same name so we need to also put a constraint on the last name okay so here again um I will choose the cell as last name and again I will put this value here and put a constraint so using these two constraints it will be able to find out the row even though it is dynamically changing on the page okay and now we want to click on the edit button so that should be pretty simple so we will just use the click operation on the edit button once it is able to find or select this row based on these two constraints okay so that's the logic you need to apply uh in order to resolve this particular obstacle okay so now uh let's go back here we'll change the work state to complete it and now let's go ahead and run this in scratchbook so as you can see it is able to click on the correct edit button

[05:18] using the two constraint it was able to find out the row which contains the first name as John and last name as to and uh it was able to complete this obstacle so these are uh the particular actions which you need to perform in your test case in order to complete this particular obstacle that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
