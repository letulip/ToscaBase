---
id: "cW_JhVahFpE"
title: "Tosca Tutorial | Lesson 24 - Desktop Automation | Save As Dialog Box | TBox Automation Module |"
url: "https://www.youtube.com/watch?v=cW_JhVahFpE"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 444
upload_date: "20231010"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:26:29Z"
status: "raw"
---

# Tosca Tutorial | Lesson 24 - Desktop Automation | Save As Dialog Box | TBox Automation Module |

[00:08] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist and today we are going to discuss how we can automate the save as dialog box which is uh like a Microsoft Windows dialog box and this cannot be steered like any other web application uh because you cannot scan this particular application through the normal X engine right uh since it's like a desktop based dialog box so you need to use some other modules now uh here uh as you can see this dialog box appears whenever you are trying to save any particular file it could be any Microsoft Office file uh like a Word document so if you want to make some changes and after that you want to save this file so basically you need to steer all these elements right so you need to enter the file name uh the save as type uh then where do you want to save this or what name you want

[01:10] to put and then click on save or cancel right so these kind of uh dialog boxes can be steered okay using the save as uh module which is part of the t-box automation modules uh part of the standard subset which comes uh with tosa Commander so you can easy easily automate this particular scenario using that particular module so let's look how you can do this okay so I am here uh in my tosa test case section and I have created a test case here called save file so here I'm going to search and ADD test step and then go to tbox save as okay and then I'm going to add this here and here you can see there are a couple of module attributes uh which you can call them as parameters for this particular module so here uh the first module attribute is caption okay so this caption is basically U the caption of

[02:11] the window which you want to steer uh it could be mostly the title of the window so for example here uh the caption of this particular window is save as right so we need to enter the same here so I'm going to enter same as here so coming to the second module attribute is the file name label this what you see here so this is the label of the file name right um and if by default it is file name then tosa will automatically steer it you don't need to mention it separately but if it is something else if it is a some custom uh edit box then uh it has got a different label then also you can mention it but if you want you can still mention this okay so so I can say file name here okay and then uh the file path so where do you want to save this particular file and that will be entered

[03:12] right in the file name okay along with the path you will have the name of the file so uh we can enter this here the file path so I'm going to enter this uh c training and then uh the file file name actually okay so I'm going to call it test. do right so this will be saved here uh under the training folder and then the button so this button refers to uh all the buttons in this particular dialog box so either want to click on save or cancel we want to click on save so I'm going to do that now so I'm going to write here save right and then there are two more attributes called confirmation popup caption and Confirmation popup button now these are basically the popups which might appear after you click on Save

[04:14] right so sometimes um some popup will appear whether uh you have changing the name of an existing file so it will ask you for a confirmation or you are making some other changes right so any popup which uh comes up after you click on Save could be handled with these two attributes so again we need to provide the caption and then uh we have to provide the button name which we want to click so I will tell you uh we'll see uh what kind of popup comes up after we perform this uh steps and then I will tell you how you can uh enter the remaining two attributes to handle that popup okay so let's go ahead and execute this now and as you can see uh it entered the path okay and it clicked on Save but after that there is a new popup from Microsoft Word you can see that it is

[05:15] mentioning your document will be upgraded to a a new file format okay and it is asking for your confirmation so this is a popup uh which comes up right uh we were not aware of this but uh if it comes up then it can be handled using the two attributes okay so here uh we need to provide a caption again so what's the caption it's Microsoft Word so I'm going to mention this Microsoft Word and then uh what button we want to enter here right so we want to click on okay to go over this so I'm going to say okay here right so these are uh the two changes which we need to do here to save this particular file now let's run this complete uh test step again for that I

[06:16] need to bring this back to the original state okay so I'm going to click on cancel and that will bring to this particular savest dialog box it will not be saved until you click on okay on that particular pop up right so again um I will going to run this complete step now so that it runs through the whole step okay so now you will see that uh this file has been saved okay uh with the name test. talk and in the exact location where we mentioned it so it went through all the steps right so this is how you can easily uh automate any save as stal box whenever it appears maybe it is from your desktop application or it is from some file which you are trying to automate that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to

[07:17] our Channel thanks for watching and I will see you in the next video
