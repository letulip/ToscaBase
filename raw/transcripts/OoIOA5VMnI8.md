---
id: "OoIOA5VMnI8"
title: "Tosca Tutorial | Lesson 78 - Steer Tosca Commander using Command Line | TCShell |"
url: "https://www.youtube.com/watch?v=OoIOA5VMnI8"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 611
upload_date: "20230228"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:04:46Z"
status: "raw"
---

# Tosca Tutorial | Lesson 78 - Steer Tosca Commander using Command Line | TCShell |

[00:00] Hey everyone, welcome to another interesting lesson in this Tosca course. Today I'm going to talk about how you can steer your Tosca Commander using the command line tool which is also known as TC Shell. This is provided by Tosca so that you can execute your scripts not only from Tosca Commander but from the backend using any command line tool. So for Windows we have got command prompt as you know and we can right away execute our Tosca TestCases right from here using this particular tool.

[00:35] So let's see how we can do that. In order to access this TC Shell which is the command line tool, it is present in the Tosca Commander installation folder. So when you are installing Tosca Commander it will be automatically set up for you. Okay, you just need to access it and use it. So to access it, we need to go to that particular folder and one of the shortcuts which you can use is commander underscore home. And it is basically the same folder which is your installation directory, program files, trisenters and Tosca Commander.

[01:14] This is where this particular command line utility is present. Now in order to access this command line tool you don't only need to call it but you also need to pass some parameters and these parameters are basically the workspace path with your credentials for logging into that workspace. Now if you are working in a single user workspace you don't require any credentials but in a multi-user workspace in a real-time scenario you will require a username and password as well.

[01:48] Okay, so you need to provide all of this and how you can do that is this. So it's basically calling the TC shell and passing the parameters workspace and the login. Okay, so in workspace I am giving the workspace path. Obviously you need to go till the TWS file which is the actual workspace file. Okay, also there are two ways of working with the TC shell which is the command line tool.

[02:19] One is the interactive way and one is the script way. We will look at both of them briefly. Okay, starting with the interactive way. In interactive way you can interact with the command line tool basically. So if the command line tool requires any input you can provide them right away in the screen. But in script, in the script process you just write the script and prepare the script once and then you just run the script. So there is no way to interact with the command line tool in between the execution.

[02:51] Okay, so to start off with the interactive mode we require this command TC shell and then we pass the workspace. So if I copy paste this path here and then it is going to check for the license and then it is trying to login into this workspace. Okay, for now it is stopped by another process which is basically the workspace opened in my Tosca commander.

[03:21] Okay, so do keep in mind that you cannot open the workspace in two places at the same time unless you are using a multi-user workspace and you have got different repositories. For this particular repository I cannot access it from the command line and also from the Tosca commander. I need to close one of them. Okay, so let's press yes here. Okay, since this is a single user workspace, so it doesn't require username and password and Tosca already recognizes that and that's the reason it didn't ask for any username and password.

[03:59] Okay, so when you see this prompt that means you have successfully logged in into the TC shell and it is connected to your workspace now. Okay, so now you can go ahead and run all the commands, but what commands are included in the TC shell that can be easily noted by this help command. Okay, so when you write this help command, it will show you all the different options or all the commands with all the different parameters. Okay, the important words are compact workspace, which will basically come compact to work space for performance reasons.

[04:37] You can change the node you can call a script. Right, you can get all options get option. You can set different parameters. You can do a health check. Okay, you can jump to a particular node. So this is what we will see later on. And you can save save options as I said set options at property and then you can also run a particular task.

[05:08] So task is basically something like execution. So if you want to execute your test cases, you can use it using this task. Okay, so we are going to look at some of these commands not all of them at least but the most important ones are the task. And if you want to perform some background checks like the health check or if you want to check in all so those things you can do using this command line tool. Okay, so this is the interactive mode and then if I can exit from this interactive mode as I said it asks for different inputs like so it will really ask you how you want to exit tissue or you want to log in into this your workspace is locked.

[06:00] So all of these are inputs which is asking from the user. So that's the interactive mode button script mode. You will not find all of these prompts. Okay, so I'm now exiting the interactive mode and let's clear this screen so that we can see it and then we are going to use the script mode. Okay, so in script mode apart from these parameters we can also pass a parameter which contains the script path to the script file.

[06:35] Okay, so the script or TCS this is the file which I have created and it contains some commands or some operations which I want to perform using the Tosca commander. Okay, and if I open this you will see there are four commands. Basically first is jump to node and it contains the node path where my execution list is present. So the execution list is PDF compare. Okay, so this will compare to PDF files and it is inside the execution and execution lists.

[07:11] Okay, so basically you have to just look at the path of your particular object and just pass it here. After that I'm calling the task command to perform some tasks like clearing the log of the execution and then running the execution list and then saving the results. So these are the four commands which I'm running together in this script dot TCS file. Okay. Now in order to run this I can copy this whole command.

[07:44] Okay, so this is the script mode as you remember and we can just paste it here and we can just start running our script right from here. So once the script is completed it will post the results back to Tosca commander and we can go into Tosca commander and verify there whether the execution was successful or failed. Now why this is important is this is the only way you can integrate your Tosca test cases with a CI CD tool like Jenkins, right?

[08:21] So in Jenkins if you have got a script which you can execute from Jenkins directly you can automate your whole execution process or you can even schedule your executions. Okay, so as you see it is showing all the steps which is it has performed and it is saying run finished. So let's go to Tosca commander and let's verify whether it actually executed that particular execution list. So if you remember we have given this path which is starts from the project right, which is the top node and then execution then it goes to execution lists.

[09:02] So the first step is to jump to this particular node, which is PDF compare right and as you can see the start time stamp. It has been executed just now. Okay, and the results is fail obviously because the compare results failed that was expected but this execution was performed from the backend which is from the command line tool right not from Tosca commander like the usual way we do it and this is more efficient and much faster obviously because you are doing it from the backend and you can even use this process to integrate your Tosca test cases or execution to CI CD tool.

[09:48] Okay, so that's our next topic and it will be very interesting to see how you can run your test cases right from Jenkins. So do look out for my next session which is much related to this and we'll talk more about how you can integrate your Tosca with Jenkins.
