---
id: "-hceXOD_WB4"
title: "Tosca Tutorial | Lesson 152 - Tosca Distributed Execution Setup with AOS | DEX Agents| Test Events |"
url: "https://www.youtube.com/watch?v=-hceXOD_WB4"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 2495
upload_date: "20250505"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:24:16Z"
status: "raw"
---

# Tosca Tutorial | Lesson 152 - Tosca Distributed Execution Setup with AOS | DEX Agents| Test Events |

[00:00] Hey guys, welcome back. So now we are going to talk about distributed execution in Tosca, how we can set this up and how we can get it running. So basically triggering test events from our Tosca Commander and then they get executed on different agents, okay? So this is the architecture of the Dex with AOS. And now AOS stands for Automation Object Service. And you can see here on the Tosca server, which we have already set up, the AOS and the distribution service are already running.

[00:39] Okay, so the AOS has its own workspace and they act as the middleman between your Tosca Commander and the distribution agents. Okay, so whenever we trigger any test events from our workspace in Tosca Commander, it gets executed or it triggers the execution from the server and the server then distributes it to different agents, okay? So once this agent finished their execution, they will return the results back to server and the server will then communicate with the Automation Object Service workspace, which will again save the results back to the common repository, which is the database.

[01:26] It can also retrieve any test data, which is required from the workspace from Tosca Commander. And then it can pass it on to the distribution server, okay, which will be used for executing your test events. So this is how the whole flow of the distributed execution works in Tosca. And this is the whole architecture, okay? So one part of it we have already done, which is the Tosca server.

[01:57] Now our Automation Object Service and the distribution service are already running. Now we have to set up these agents, okay? And we have to also set up this workspace. Also, we have to do some configurations so that this whole setup can be replicated and we can start executing our test events on different Tosca distribution, or which are known as text agents, okay?

[02:29] So this is what we are going to do now. And there are many parts to it, so I'll be taking it slowly, each part, right? So first we are going to set up a AOS workspace that should be set up on the Tosca server. So wherever you have installed Tosca server, you have to create a separate workspace. That will be the Automation Object Service workspace. And you should not use it for your regular day-to-day work. You should always use the workspace which you have set up on the common repository on which are being used by the Tosca Commander.

[03:05] This will be used by the Automation Object Service and it should not be opened or used for any other purpose, okay? Otherwise your text will stop working. So yeah, so we will first set up this Tosca workspace. Then we will do some configurations. We'll create test events, okay? And we will create different configurations. We'll set up an agent. We'll connect it to our workspace, okay?

[03:37] And it will also be connected to the Tosca server or the Dex server. And then we'll trigger the events and it should be executed on that particular agent, okay? Now all of this I'm going to do again on my own machine because of lack of servers, but you can always go ahead and set it up on different Windows servers as I explained to you earlier or different machines even, okay? Right, so let's go ahead and open our Tosca Commander now.

[04:10] I'm going to use the multi-user workspace which is the multi-demo. So let's open this. Okay, actually we had to create a workspace so I don't even need to open this. But anyways, I will close this. So this is the workspace which we had created earlier. It is the multi-user workspace. So one thing to note, very important, is for distributed execution it will only work with multi-user workspaces, okay?

[04:48] So you have to create a workspace, multi-user workspace on a particular repository which could be any database, okay? So that's very important. So I'll cancel this. We are going to create a new workspace now. So let's click on create new, okay? Just a minute. Yeah, and then I'm going to use SQLite for now. Obviously it's not recommended for production environments.

[05:19] You have to use Oracle or SQL Server or DB2, okay? So I'll be using the existing repository which I have created already because it should be the same repository where you have created your multi-user workspace, okay? So that's also important. Don't create a new repository again. They both should be connected to the same repository as we have seen in this particular diagram. You can see this is the common repository and both are connected to this, okay?

[05:53] So branch will be master and I will create the new workspace in this particular part. I will going to create, or I will give a name here, something like multi-AOS, okay? And then you should not be creating a slim workspace for AOS. It doesn't work. So don't select this and let's go ahead and create this workspace.

[06:24] So this is the workspace which is specifically made for AOS, okay? And depending on how large your repository is or it will take very little time or very huge time if your workspace or your repository size is too big, okay? Because it has to update all the objects before it creates a new workspace. So it may take more time or it may take very less time like me because my repository is almost very, it's a very little size for my repository.

[07:01] I don't have many tests or anything, okay? So let's log into this. We will just verify this workspace and then we are going to close this because as I said earlier, you should not be using this workspace, okay? It will be used by the AOS service and let's just verify here. The project name is correct, multi-demo, okay?

[07:31] And we have got the same repository because we can see some of the similar objects which are present in my other workspace, okay? So this part is done now. We have created our AOS workspace. Now we can close this, okay? Now the next part is to configure some AOS workspace-related things on the server, okay?

[08:02] And for that, I'm going to also open my multi-demo workspace or project and let's go to our server now, okay? So on the server, you need to go to settings and here you need to go to automation object service, okay? Although it is in the running state, we need to add a workspace here. So the workspace which we have created, we have to add it here, okay?

[08:32] So click on add new and you need to provide a name, project root name for this, workspace name, workspace name, username and password, okay? Now you can create a maximum of 10 different workspaces which can work all in panel, okay? So if you've got different projects, you want to create different AOS workspaces for that, you can do that. So you can create a maximum of 10 right from here.

[09:02] So just click on add new and then add the details here, okay? So our project root name is multi, so let's check our project root name first, okay? I should not have closed that, but let's open this again so that we can just note down these, all these different settings which we need to provide for our AOS workspace, okay?

[09:34] So let me go here, workspace name, I know it's multi AOS, right? And our username is admin, password is admin, I just need to provide the root name, okay? So let me log in here.

[10:06] And as you can see, so our project root name is multi demo, but our workspace name is still multi AOS, okay? So the project name will remain same because we are using the same repository, so it is multi demo, but our workspace name is, you can see on the top, it's multi AOS, okay? So let's put multi demo here.

[10:43] So now go ahead and save this, okay? So these are all the changes we need to do. You can see once I click on save, it will restart all the services which are related to this, okay? So once it restarts, it will apply all these settings on that particular service before starting it, okay? Also it's recommended once this is all set up, you can also go ahead and restart the DeX server because the DeX server is connected to this AOS, so it's better we restart the DeX server from our services, okay?

[11:27] So let's go to services, and let's go to Tracentes services and we'll search for the distributed execution service, okay? And we'll restart it once this finishes off, okay? So ideally this should also restart the DeX server, but just in case it doesn't restart, you should restart it manually, okay?

[11:59] So this is now restarted and it should be running. I can also restart the monitor because it is connected, okay? Right, so it is in running state and if I go back to my dashboard, refresh it and then you will see everything is running again, okay? If I go to my monitor, which we will require later on, okay?

[12:33] Currently no agents are there, but we are going to set up a agent now, okay? So the work for this is now finally done, so we can close this multi AOS workspace and we can open our project, which is multi demo, and here we will be setting up our DeX events, DeX agents, right? So the next step is to connect a DeX agent. Now ideally this should be again a different machine where either a Tosca Commander or a Tosca Execution agent is running, okay?

[13:13] But since for this particular demo, I'm going to use the same machine. I have set up my Tosca server and Tosca Commander on, but ideally in ideal conditions, you should not use it. Either use a different machine or a different server where you have set up a Tosca Commander or a Tosca Execution agent, okay? So now we need to start the Tosca agent wherever you want to set it up, and for that we need to go to C, Program Files, and go to Tricentis, Tosca Server, Distributed Execution, so we have to go to DeX Server, okay?

[14:02] And actually not the DeX Server, just a minute. I think I went the wrong way. So we need to go to Tosca Test Suite and here Distributed Execution, and here you will find the DeX agent.exe which we need to run, okay? So this is the Tosca Distribution agent. So whenever you install Tosca Commander, this folder will be created and you can run this DeX agent on any machine where Tosca Commander is installed.

[14:37] There's also a separate installation provided, okay? So whenever you install Tosca Commander, right, on any particular machine, let me show you. You can also set it up as a dedicated, right? I cannot show you here because it's already installed, but whenever you start the installation, right, it will ask you an option whether you want to install the full Tosca Commander or you want to install a Tosca DeX agent, okay?

[15:13] So you can either, both ways are correct, but ideally you should just install the agent part, not the complete Tosca Commander as it is more memory efficient and also it will take less space for you, okay? So if you just want to use it as a distribution agent, then just install the agent on that particular machine or if you want to use both Commander and agent together, then you can go ahead and install the Commander and this agent will be available, okay?

[15:45] So this is the part that you need to go and then double click on this, okay? If we, ideally we should run it as an administrator, okay? And once it's done, right, so you will see a monitor which is displayed on your bottom task bar, right? You can see currently it is white, which means it is not running. If it is green, that means it is configured correctly.

[16:17] If it is yellow, that means it is executing. If it is red, then it means that it is something has not been set up correctly, okay? Now you can see it is green, so it has set it up correctly, automatically set up this agent for us, but if it is not, then we need to configure the agent. So right click on this and you will get the option to configure or stop the agent, okay? So let's go to this agent configuration.

[16:50] You can see here, operating system memory, operating system type, IP address and host name. It has picked up automatically, but you can always change this, okay? So we'll see where this setting lies and how we can change this. We don't need to set up the workspace here, okay? Because this is a AOS workspace, so we don't need to set up any workspace for an agent.

[17:22] Now this is the most important part, connect to server. You can connect to your DEX server where it is set it up, right? So for me, it is localhost and this is the port 5007. You can always go and verify this on your DEX server. Okay, so go to settings and go to automation object service. Here, you will find the distribution server address.

[17:54] So you can see it is localhost 5007, right? So this is the server and the port which you should give wherever you have set up your Tosca server or DEX server and this is the endpoint URL which this agent requires in order to connect, okay? Then authentication, if it requires an authentication, you can do that. So you can use RDP, okay? If this is running on a particular machine right now, it is running on my local, so RDP service is not available, but you can always use this RDP connection, okay?

[18:33] So why this is required? If you have set this up on a different machine or server, so if you enable RDP, then it can perform that all the mouse and keyboard actions on that particular machine, even if it is locked, right? Because if you don't use this and if the system gets locked, then your test will start failing, okay? So you have to give, choose this RDP connection and then provide username password, the desktop width, height, whatever is that for that particular machine, okay?

[19:09] And then logging, so this will be the log file. It is present in this same folder. You can see here, this is the log file Tosca distribution agent and ideally it should be set to debug so that if any problem comes, you can go ahead and debug that particular problem in your log file, okay? So go ahead and click this and as you can see green, that means our Dex agent is set up correctly.

[19:39] If you see it is red, then that means something is wrong and you should check or configure that particular agent, okay? Now you will see if we go back to our Dex monitor, right? So on the agent, you can see on the agent view one agent has popped up now, okay? So currently it is in the sleeping state or idle state. So this is the idle state, okay? So this means it is running.

[20:11] This means it is paused or this means, this means it is stopped. This means some error has happened, okay? I can restart my agent from here. I can do the configuration right from here. You can see the machine configuration here, the workspace, the RDP connection, the login, okay? So these things we can configure here. For the endpoint URL, you have to go to the agent and configure it there, okay? So this is all you can do from the agent view or the monitor, okay?

[20:45] So the Dex monitor, it will show all the agents which are configured right here. So if they are in running state, then they will be displayed here. If they are not, then they won't be available here, okay? So what this means is now we have got one agent, which is the Dex agent, where we can trigger our test events, okay? And that will be done through distributed execution, right? So this part is now complete. So we have set up our Rosca Dex agent successfully, and it is available on the monitor, right?

[21:24] Now we need to connect our commander to this particular agent, right? So that's the next step. So let's go back to our commander. And in commander, inside your project, when you go inside your execution, right, you will see configurations. So these are the configurations which are created by default, okay? And in any, right? That means whichever agent is available, if you use this configuration, that particular agent will be provided the task from the server, okay?

[22:02] So whenever we execute any test event. Similarly, there is RDP where useRDP is true and supports classic. So in properties, you can see it is true, which means it supports the classic modules, right? So these configurations, these three are available by default, but we can add as many as we want. Now what this means is these are the different configurations which will match the Dex agents, okay?

[22:32] So whatever configurations you require for your test to run, something like you want to run on a Chrome browser, on a Firefox browser, or on an Edge browser, or you want some specific machine configuration, like you want to run on a specific operating system, like you want to run on Windows 10, 11, or Windows 8, right? Or some specific RAM size, right? It depends on what kind of configuration, machine configuration you require.

[23:05] And that machine configuration or any other configuration can be set up here, okay? So we'll see that later, but first let's go ahead and execute some test events now, right? But before that, what you can also do is right click on these configurations and refresh the agents, okay? So what it will do, it will refresh the agents, but first we need to configure this, or we need to connect our Tosca Commander to the Dex server, right?

[23:38] So let's go ahead and do that. So go into settings for your project, and here we need to set some values, okay? So in settings, under Commander, under Distributed Execution, we need to set the monitor URL, okay? And we have already seen this. So if you don't know this monitor URL, you can go back here and this is the monitor URL, localhost 8080 slash monitor, okay?

[24:14] So copy and paste it here, and then the server. So here we need to also give the port if it is not the default port. Rest of the endpoint URL will remain same, distribution server service, manager service.svc. We just need to change the server IP address if it is not localhost and the port, okay? So for me, it is localhost 8080. If you have set it up on a different server, the port may be different, it may be 80, and it could be localhost, or you can give the IP address directly here, okay?

[24:54] So these two settings you need to change, and then the last one is tracendis services. So here we need to provide the server endpoint address, okay? So wherever we have set up the server, we need to provide the endpoint address, which is nothing but the localhost or the IP address. And with it, we also need to give the port, okay? So localhost and then the port, which is 8080. So we need to set up the distributed execution, monitor URL server, and the tracendis services.

[25:31] So these three settings you need to change here on your commander site. So wherever you are going to trigger any test event, you need to change the settings, okay? And go ahead and close this, it will save the settings, and let's try and refresh the agents now, okay? Once I refresh the agents, and you can also do update configurations from server if you have changed anything on the server side.

[26:02] We'll see that. Okay, so it is saying, error occur during creation of proper definition, check out the project route, okay. Yeah, we need to check out the project route before we update the configurations, but for now it's not required. I will show it when we change something on the configuration side. But as you can see, now this desktop vision, right? So which is my dex agent host name, it is now available under any, okay?

[26:33] So when you refresh the agents, all the agents depending on the configuration, how it matches, so all the agents will be available under any because it covers all the agents, okay? But any specific agent configuration which you have used, if it matches this configuration, so if useRDP is true for my agent, then it will appear here, right? Similarly, if it supports classic, it will appear here. So if I have a Chrome configuration, if it matches that configuration for that particular dex agent, then it will appear here, okay?

[27:09] So this is also important, the number of agents which are running on the configuration because we are going to use this configuration inside our test event, okay? So you can see test events by default under any execution folder you have created, okay? So, and again, as I said, it is not available in single user workspace, so we might not have seen it earlier, but when we created a multi-user workspace, this test event was created and this is used for distributed execution only, okay?

[27:44] So this test events will be available here and we can create different test events here, okay? What it requires? It requires a configuration and it requires an execution list which it can execute, okay? So first, let's go ahead and check out this and then I'm going to create a test event. So this is the test event, okay? And let's name it.

[28:16] We can give it any name, but let's give it dex event, okay? And we need to now drag the configuration. So what configuration you want to use for this event? I can use any or I can use any specific configuration, but let's use any for now, okay? Because it has got one agent, you can see here number of agents is one, so this event will be used in this agent. If there are 10 agents, the server will decide which agent is free and it will distribute it on that particular agent.

[28:54] If you want to run it on a specific agent, then create a configuration for that and then drag it for your test event and it will be only executed on that particular configuration, okay? Now, this configuration, it also requires an execution list. So I have created an execution list called dex test, okay? It contains this test, test which is very simple, test case. It opens the Google URL, okay?

[29:26] Obviously, you can do much more, but this test for this demo purpose I've used. So I have dragged the test case to here. I've created execution list. We already know how to do that. So I'm not going to repeat it, but we have to now drag this execution list into this configuration, okay? So this is the structure of a distributed execution. You require a test event. You require a configuration and you require a execution list.

[29:57] You can also create a test mandate or basically any kind of execution you can create and you can drag it down here so that it is at least configured so that it can be run for this particular event. Just thinking what else we require, but I think we are now ready to execute this test event on our dex agent. So let's go ahead and do that.

[30:28] You should always check whether the test agent is in running condition. You can do it in many ways as I've shown you. So we can execute it right from here, execute now, or we can execute it now, right? Obviously, if you want to run your test events, right, on a particular server at a particular time, you want to trigger them, you can always do that through some CI client, right?

[31:00] But we'll see that later. Now, once you have triggered the test event, okay, it should be available on the event view, right? Now, we can always go to the details of any particular event execution like we have done here. Currently, you can see the test event status is canceled because some error occurred, right?

[31:34] And it will show the details here. So you can see some, it failed to retrieve the needed automation objects, right, so I know why this has occurred, but I wanted to show you this, if some error occurs, how it will look and how you can go back to your details, right? But we forgot one thing before executing this test event, right? So one thing, very important thing to note is whenever you are executing a test event, you have to make sure that all your test events are checked in or any particular execution list which is linked to that test event should be checked in.

[32:18] Okay, so you can see here, our event is checked out and that is why it is not able to retrieve that test object from the workspace, okay? So always make sure you check in everything before or at least the test events which you are running before you execute the test event, okay? Otherwise, you will have issues like this. So let's try this again and let's go back here and execute it now.

[32:52] Okay, so since it is executing on this particular machine, we might see that a new browser will be opened here and the Google page will appear, right? So that means my execution list was executed, okay? Because this was a test case I was running and this is what will happen on your text agent machine, right? And you will see that the event view, that particular test event is now passed.

[33:24] We have one canceled, one passed, right? You can see the start time, the creator who is, if there are different users, okay? And the agent view will be back to idle but while it is running, you can also monitor the view and it will be in the execution state, okay? So this is how you can trigger test events and you can run it on different agents which are different remote machines which are running Tosca, okay?

[33:57] So you can distribute all the events even in parallel across these agents, okay? Now the last part which is there is we're talking about configurations, right? And where this configuration is coming from is right from, you can go to C program files and go to Tracentes, Tosca server and I think it is here under Dex server, right?

[34:29] Yeah, so if you look under Tosca server, Dex server, you will find configuration parameters and these are the configuration parameters which are defined by default, okay? And you can see all the different operating systems which are available here and the different memory configurations, different operating system type and then there is this additional configuration which is useRDP and support classic, right?

[35:08] And also IP address, okay? So you can define all different configurations right here, okay, so I can go ahead and change some configuration like this, okay? So here you can see operating system, we have got all the different operating system but we don't have 11, but I feel I want to execute a particular test on a configuration which has got Windows 11, okay? So I can edit any particular configuration, I can also add, you can just copy this whole XML key value pairs and you can create your own configuration.

[35:51] So I can add as many configurations I want, I can even add a test configuration parameter like this. So I need to put a name and then the parameter values, okay? So I can create easily for something like a Chrome or anything, okay? So now I have changed this Windows 11 right here. So what I need to do, if I've changed something, first of all I need to save it here and you need to be in admin mode to change this, okay?

[36:25] So first save it here so that it is saved on the server and then on the commander we need to retrieve that configuration change right here, okay? So for that we need to check out our root project, right click on the configurations and update configurations from the server, okay? So now that particular configuration is applied here and we can even check that by creating a new configuration.

[37:01] So we can create a new configuration here, okay? And here I can create a new configuration. So I can name it something like local, right? Because I'm executing on a local machine so I want something specific for my local machine, okay? And once you create this new configuration you will see all the properties, right? So all the configuration key values which will appear on the properties on the right hand side.

[37:33] So host name, IP address, memory, use RDP, operating system, operating system type, memory. So whatever configurations we had put there is available here. And I can then select a specific configuration, okay? So I can select Windows 11, memory 16 GB, operating system 64 bit. Now the essence of this is once you create a new configuration you have selected some new configuration key values for that in the properties, right?

[38:07] You have to now match this with your agent, okay? So let's go to this configure agent and here you can see Windows 11, 16 GB and 64 bit, right? So now this configuration of the agent is matching the configuration which I have just created, okay? So let's go ahead and check in all and what we'll do, we will go and refresh the agents. Now what is going to happen is now I'm going to see agent pop up on my new configuration because it matches the properties which I have defined here with the agent, okay?

[38:50] So whenever it matches that configuration it is going to put that agent under that particular configuration so that you can just use this configuration in your test event and then you can run it on specific configurations, right? So you can create like this different configurations here based on what you want to execute and what kind of machine configuration you require, right? So you can do that here and just change the configuration of the agents which should match with this particular configuration which you have defined in configuration parameters.xml, right?

[39:27] So these three things you need to match and then you need to refresh the agents and then it will appear here and you can use this configuration. Now I can remove this any here, okay? So if I check this out and if I remove this configuration here and I use my specific configuration which is local and I can now execute this event on here. I mean, there is no such change now because it is still executing on local, I've just got one agent but when you have got multiple agents and you want to run your event on specific configuration on a specific agent then this is how you can do this, okay?

[40:15] So this was all about distributed execution. It requires some level of configuration so you need to have some knowledge of your whole architecture, your infrastructure, right? How, where your Tosca server is, where you have set up that, your IP address port. You have to change a few things like I've shown you and then once you are all set up you can then start executing your test events or distribute it across different machines, different agents, depending on the configurations you choose.

[40:50] So there are lots of things to consider here, right? But it's very important, distributed execution is one of the most important things or most important components of Tosca because it provides you the ability to execute your test events in different machines, different configurations, even in parallel, okay? So this was all about distributed execution. Next we'll be talking about CI CD, how you can trigger this events that is also a Tosca CI client.

[41:27] So we'll look at all of them in the CI CD session.
