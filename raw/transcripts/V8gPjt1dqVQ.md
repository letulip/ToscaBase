---
id: "V8gPjt1dqVQ"
title: "Tosca Tutorial | Lesson 30 - What is WaitOn Action Mode? | Action Modes | Building Test Cases |"
url: "https://www.youtube.com/watch?v=V8gPjt1dqVQ"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 584
upload_date: "20230206"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:23:43Z"
status: "raw"
---

# Tosca Tutorial | Lesson 30 - What is WaitOn Action Mode? | Action Modes | Building Test Cases |

[00:10] hey everyone welcome back again to another interesting Tosca lesson today we are going to talk about the Last Action mode which is called wait on now we have discussed all the remaining action modes and in the last session I talked about how you can use the buffer action mode so what is this action mode weight on it is a way Tosca implements the dynamic weight in its test cases so the weight on action mode basically interrupts the execution of your test case until the indicated property has the specified value which means the condition which you have specified in your test step should be satisfied and then the execution will continue so it's a dynamic mechanism of waiting not a static mechanism and Transcendence recommends to use this particular action mode whenever you want to wait for any particular condition within your application or any particular control which is not visible so things like that

[01:13] now this wait time can be defined in the settings called synchronization timeout during weight on okay and to show you that let's go to settings okay so under settings you need to go into t-box and on the t-box you have to go to synchronization there you will find the setting called synchronization timeout during weight on so by default uh it will be around 20 000 milliseconds but you can either increase or decrease this okay so coming to the action mode weight on and how this can be used so we are going to pick up a placentis obstacle okay so this is the obstacle course uh website from test centers where you will find different uh challenges which you can work on and one of these obstacles is uh you have to click on the button

[02:14] calculate okay and after some time the send button gets visible or enabled so after that you need to click on it to complete this obstacle so it's basically clicking of two buttons but the thing is the send button is not enabled at the beginning okay so once I click on calculate you see this progress bar it's going to increase and after a certain point the send button is going to be enabled and when this will be enabled we need to click on the send button okay so here you can see that it's not a straightforward scenario right now the send button is enabled and I can click on it so that will complete my obstacle but as I said it's not a pretty simple or straightforward scenario because you cannot directly go ahead and click on calculate and then you can click on send obviously one way around is you can calculate the time it is taking to load

[03:17] or to enable the send button and you can put a static weight okay but that's not the efficient way of doing it the most efficient way of doing this is to put a weight on on this particular button okay and until this is enabled uh Tosca Will Wait So no matter uh if this particular bar or the time changes in the future your test case will still run but in the case of static weight your test case will always wait for that amount of time which is not at all efficient and also it increases the execution time in the whole uh scenario right so let's go ahead and work on this so first we need to create a module and I already have a obstacle folder so I'm going to insert a module inside this okay so let's scan this application we just need to add two controls in this

[04:19] module and those are the two buttons so we are going to select this application and then we are going to scan the controls so here you can see I've got two buttons calculate and send and I'm going to select both of them okay so that's all I need to do on the module section and I'm going to close this so that's going to create my obstacle right and let's give it a proper name so we will call it 33678 right okay so that's our module and let's go

[05:20] to the test cases section and here we have got our action modes right so we are going to create a new test case here and we are going to call it um the weight on okay wait on test and here um we are going to pull up that particular module which we have created so I'm searching for obstacle 33678 and now the first step is to obviously we just need to click on this particular calculate button so that's our first step uh and then we need to wait for this button to be enabled right so let's add another step here and here we will be using the action mode weight on okay so let's add this again and hit this time around I am going to

[06:22] use the action mode weight on okay and you will see uh the weight on action mode has got a different color it's yellow in the background okay also we need to put a condition here because the weight on depends on the condition being satisfied for the particular control okay so what we are going to do is we are going to say um enabled equals to true okay so since it is disabled now when it when this particular button is enabled the weight on will be satisfied and the execution will continue okay uh let's go ahead and first change just the steps so I will say click calculate and then wait for send enable

[07:25] okay and then we'll add our final step to click on it okay so let's go ahead and do that as well and here finally I am going to click on that particular button right so I will say click Send so this is um the whole test case you can see so there are basically three steps first we click on calculate then we use the weight on to wait for that button to be enabled and then we go ahead and click on it okay let's go ahead and execute this in scratch book and let's see if it works so it clicks on the calculate button and as you can see it is going to wait until this progress bar completes or the send button is basically enabled that's the condition we have put so it's going to wait until that and then once it's enabled it's going to

[08:27] click on it okay so it's a pretty simple obstacle or a scenario once you know how to use weight on but whenever or for whichever scenario you have to put some synchronization or you have to wait for some particular controls on the page uh no matter what just try to use this particular uh weight on mechanism or some other Dynamic mechanism available in Tosca rather than using uh the t-box weight which is a static bit so whatever time you provide in that weight it will wait for that time no matter even if your control is already available so which is not an efficient way of doing it and also it's not a best practice so keep this in mind when you are automating your scenarios in Tosca and try to use the weight on action mode um whenever you are working with synchronization or timeout issues

[09:29] so that's all for this particular session uh in the next session we'll be continuing with some more interesting features of Tosca
