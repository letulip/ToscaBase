---
id: "G-1TF7oLe8g"
title: "Tosca Tutorial | Lesson 121 - Multiple Interactions | While Loop | Obstacle 15 |"
url: "https://www.youtube.com/watch?v=G-1TF7oLe8g"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 122
duration: 405
upload_date: "20231220"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:08:22Z"
status: "raw"
---

# Tosca Tutorial | Lesson 121 - Multiple Interactions | While Loop | Obstacle 15 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist now continuing with our topic test automation obstacles let's look at our next obstacle which is called again and again and again right now why is this so in this particular obstacle we need to complete uh the obstacle where we need to click uh the following button which is called click me and what will happen is after a few clicks the button will change its name to enough okay and once this is done then uh you should click that button finally to finish this particular obstacle so let's try it out here so I click here one twice Thrice four times and after that it is enough right right now you don't know how many times you need to click uh in order for this to be uh appearing right so it's it's nothing fixed it is more Dynamic so you have to put some logic through which

[01:13] uh you can find out what's the name of the button and when you should stop clicking and when you should finally click so that you can complete this particular obstacle right so uh let's see how we can uh complete this particular obstacle uh in tosa so coming back to our tosa workspace as usual uh we are going to scan this particular module so let's go to our obstacles folder here go to scan application and then um going to the scan window uh the scanning is Prett simple uh we just need to uh select this particular button right and then um I'm going to rename the module and put the name here and save it and close

[02:21] this okay um now let's go back to our test cases uh we'll be creating a new obstacle here uh a new test case with that particular obstacle okay and then uh we are going to add the module back here so let's try to search our module here is the module okay so the logic which we need to implement here is we need to uh use a looping object right now which Loop you want to use uh completely depends on the scenario but here uh it would be most appropriate to use the while loop okay because uh we have got a condition here right so we are waiting for the name of the button to change from something to something else right so we have to Loop uh until that change happens and then we should stop okay so this is an ideal case for a while loop so let's go ahead

[03:21] and Implement that so when I right click and I can say uh create while statement okay and then uh I'm going to drag this uh here because we want to do this okay here we need to put or check the condition um and then here I'm going to change this to click button because that's what we are going to do finally once we check the name has changed to enough okay so this is the final step but uh we also need to put this under the condition okay and what condition uh we will do here let me change the name here first so we'll say check button okay and here instead of the click operation uh we are going to do a verification and uh here inside this we are going to check for the inner text and whether the inner text is equals equals click me okay so this is basically the initial

[04:25] uh state of the button right so uh when I refresh this page you will see the initial name of the button is Click me okay so I'm checking here uh whether this particular button name is Click me and if it is then I want to perform a loop where I'll be clicking on this button continuously until the name is not equal to click me okay so what it will do it will in the condition it will check whether the button name is this if it is yes then it will go into the loop and it will click on that now this will continue to happen until this inner text uh changes to something else and then uh this uh condition will become false so it will come out of the while loop okay and when it comes out of the while loop uh at that point of time we'll make our final click okay uh which will basically complete the obstacle right so it's a pretty simple logic uh which you need to implement uh and this is one way of

[05:26] doing it there are many other ways of doing this right so let's change the work state to complete it and now we are going to run this okay so let's see if it works so as you can see now it has started uh clicking the button multiple times and it will stop until uh it looks for the inner text whiches uh changes to enough and once it does then it will do the final click and after that the automation obstacle will be completed so this is where you can some times use the loop function uh which is available in tosa either the do Loop or the Y Loop you can also use the IFL statements although these are not recommended ways of um doing automation within TSA because it's not a programming language uh it's an automation tool but sometimes uh if the situation guarantees that you have to put some looping logic then uh you can very well use uh the looping

[06:27] objects which are available in tosa that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
