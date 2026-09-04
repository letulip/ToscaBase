---
id: "pfEIPPUBbo0"
title: "Tosca Tutorial | Lesson 147 - Common Problems & Fixes | Switch Browser Tabs | SendKeys |"
url: "https://www.youtube.com/watch?v=pfEIPPUBbo0"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 151
duration: 392
upload_date: "20240415"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:10:20Z"
status: "raw"
---

# Tosca Tutorial | Lesson 147 - Common Problems & Fixes | Switch Browser Tabs | SendKeys |

[00:02] now let's talk about a browser scenario where uh we have got multiple tabs and we need to move between this tabs uh for our different scenarios right so if I've got four five different tabs on this stenters vehicle insurance I want to switch between different tabs maybe I want to go to the third tab or the fifth Tab and again I want to go back to the third and the first tab so this is the scenario and now the question is um how can we do this so there is no direct way of uh switching uh the tabs there is no method in tosa which you can use to basically switch between different tabs right but whenever you don't find any direct method you can always fall back upon um how the user is basically uh doing this uh maybe from the keyboard or from the mouse and then you can emulate those actions uh from tosa now we know that we

[01:03] can emulate any particular action which we perform from the keyboard uh in tosa uh so uh in this particular scenario uh if we want to switch to a particular browser tab we can always use uh the tab option right so uh when you press control+ tab it is going to switch between different tabs like I'm doing right now and if I want to switch back to a previous tab I can also use control shift and tab okay so these are the keyboard shortcuts which can be used in scenarios where you don't have any other option like a direct method so you can basically send these keys from tosa and then you can um achieve what you want to do with your particular automation right so uh let's try and now uh replicate this in our test cases so let me quickly create a new folder I'm going to call

[02:05] this browser and here we will create a new test case called switch tabs okay here um I'm going to add a test step uh which is the tbox send keys and here uh we need to pass a caption and a key so caption uh it is we know the brows the title here so it T Trend this vehicle insurance throughout right so what I can do is I can use a part of the text here and then I can put a regular expression so I will use that t and this part here okay and now in the keys uh what I can do is I can pass the control key and in this case we can pass the carot sign uh so it implies the control and then we can pass the browser tab number okay so if you know where which browser tab you want to switch to you can directly pass the number here so if I want to switch to the third tab I can pass control+ 3

[03:09] okay now um if I go ahead and run this okay so we were already on the third tab so it will not make any difference so uh let me go ahead and switch back to the first tab now okay and let's go ahead and done this again okay so now you see that uh it switched to the third tab now in in cases where I don't know which particular tab is the next tab uh what is the number for that okay um so if I want to switch to the next tab but I don't know the number of tabs then um I can always use the control+ tab key right so what I will do I will just copy this and here instead of the number uh we will pass control and then we will pass

[04:12] tab okay so it will now uh switch to the next tab so let's go ahead and run this now okay so as you can see uh it switched to the fourth tab right now uh similarly if I want to switch to the previous tab okay uh without passing the number so again uh we can use a shortcut here so let's do that what we will do here is uh we will pass Control Plus shift plus tab okay and the shortcut for that is the plus sign so the plus sign implies the shift the Scot sign implies the control and this is the tab so in total it is contr plus shift plus tab now if I run this okay you will see it will move on to the third tab now if you're not sure about what

[05:13] are the shortcut for all the different Keys you can always go to the Microsoft send Keys page okay so there is a send Keys class uh which you can search for uh in Microsoft and that will actually give you all the different uh keys or the code for all the keyboard Keys uh which you want to use okay so these are all the code you can see here and these are the exact codes which we can use uh in tosa as well okay so we used the tab here you can see and then if I go a little bit down then you will see the code for shift it is plus for control uh it is this uh carot sign and and then for all it is percentage okay so these are all the codes uh which can be used uh for the different keyboard keys and you can always use them in scenarios where you don't have a direct V of

[06:16] automation using the default tosa modules then just use the keyboard keys and do the other way around like a normal user would do so just emulate that particular action using the send Keys module
