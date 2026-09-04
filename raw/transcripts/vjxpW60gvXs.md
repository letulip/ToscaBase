---
id: "vjxpW60gvXs"
title: "Tosca Tutorial | Lesson 115 - Drag and Drop Table Rows | Repetition | Obstacle 9 |"
url: "https://www.youtube.com/watch?v=vjxpW60gvXs"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 449
upload_date: "20231208"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:29:19Z"
status: "raw"
---

# Tosca Tutorial | Lesson 115 - Drag and Drop Table Rows | Repetition | Obstacle 9 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist so continuing with our topic on the test automation obstacles let's look at the next automation obstacle which is called the to-do list and here we have got two tables one is the the to-do tasks and one is the completed tasks now the challenge here is we need to drag and drop each row from these twoo tasks into the completed tasks in a certain order okay so we need to drag uh in the numerical order so we'll first drag the first task then uh the second one and then the third one okay and then the fourth one and then the the fifth and then the sixth okay and then the obstacle will be completed so that's what you need to do using tosa now we have already seen how we can drag and drop elements okay so we

[01:13] can use that in the table also we can drag and drop the rows but here we need to do this uh number of times as you can see six times right and in a certain order so that's the challenge here right so let's see how we can do this in tosa so first of all we need to scan uh our page okay so let's go ahead and do that I'm going to scan the application now and basically we need to scan uh the two tables which uh we'll be working on right so here if I scan this page you can see these two tables the to-do task and the completed tasks okay so these are the two tables which I need to scan so let me rename this module to this particular obstacle and I am going to do it right here okay and then I'm going to save this and close the module right so our module is created here with both the

[02:15] tables and now let's go back to our test case folder and here we are going to create a new test case again with the same obstacle uh number okay and here we are done going to use our module which we have scanned earlier right so uh once you drag this module here so what we need to do is uh we need to drag each row from the too task table to the completed task table right but before we do that we also need to use another uh functionality here or another feature which is called the reputation property right so that uh we need to do for for our table right and in order to do that uh we need to create a folder okay so I'm going to create a folder inside my test case and uh we are going to rename this okay so we'll re rename

[03:16] this to repetition okay and then uh we are going to drag our test step inside this now what this will do is it will basically repeat it the number of times which we will uh Define for this particular folder right and as you know we have to repeat our drag and drop step six times so I'm going to set this repetion to six okay so that's what you need to do and then uh this particular test step will be executed six times okay now if we go inside the table uh and we'll look at this page you can see that uh we need to drag a according to the ID right so we need to drag the first uh task which has got id1 and then the second task which has got the id2 so we need to work around this ID column right so what we'll do uh we'll go to the column and we'll select the ID here okay and then

[04:19] in the cell value uh we are going to put something called reputation okay so this is an expression which returns you the value of the reputation property okay so whatever reputation uh value is being set here uh which means if uh we are running this for the first time the repetition property value or the repetion expression value would be one and then two then three like that it will keep on changing this particular value of the cell right so uh that will decide the ID which will be 1 2 3 4 5 six and that is what we want right we want to drag um each task with a different ID each time right now um in the value U again we will put the drag operation here because we want to drag this particular row with this particular ID and we will change

[05:21] the action mode to input okay now once that is done we just need to drop it into the completed task table right so here we can use the drop expression okay uh we don't need to select any row and colum because we just want to drag it into the table right so now this will be repeated uh six times because we have set the property to six for the reputation folder and then it will get this particular value of reputation and uh it will select the ID based on that okay and then it will drag it and drop it into the completed tasks so let's see if it works or not but this is how we can uh complete this particular obstacle okay so let's run this in scratchbook so as you can see it has started dragging the first row and then dropped it into the completed task table it will do it for each of the task based

[06:23] on the ID so this is running on a repetition six times and it will drag and drop all the six rows right okay and you can see uh the obstacle was successfully completed right so this is how you can drag and drop a rows from a table and drop it into another table and then using the repetition property you can put your test steps inside a folder and then you can select uh some unique column like the ID which has got the numbers 1 to six so you can put the reputation property value inside that so that uh these tasks are dragged and dropped in a certain order that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to

[07:23] our Channel thanks for watching and I will see you in the next video
