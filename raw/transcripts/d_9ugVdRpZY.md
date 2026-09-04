---
id: "d_9ugVdRpZY"
title: "Tosca Tutorial | Lesson 49 - Create Recovery Scenarios | Handle Unexpected Errors | Recovery Engine"
url: "https://www.youtube.com/watch?v=d_9ugVdRpZY"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 1105
upload_date: "20221028"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:27:10Z"
status: "raw"
---

# Tosca Tutorial | Lesson 49 - Create Recovery Scenarios | Handle Unexpected Errors | Recovery Engine

[00:00] Hey everyone, welcome to another lesson in the Tosca Automation course. Today, we are going to talk about an important concept known as recovery scenarios. Now, no matter which automation tool you work on, you have to think about how you can recover from unexpected failures or errors. Now in some tools this recovery feature is already present or in some customized automation you have to write your own scripts to do that. So if you have been working with Selenium, you have to write something like a try-catch block in order to come out of unexpected errors or exceptions.

[00:39] In Tosca, there is a recovery engine which already provides you with that feature. So you have to provide a collection of test steps which are called recovery scenarios and they will kick in whenever a test case fails. So let's see how you can configure this recovery scenario in Tosca. So there are basically three steps in order to configure a recovery scenario. The first step is to enable it in Tosca and you can do it in two ways.

[01:11] So the first way is to go to the settings dialog and apply it to all the objects in the workspace. But if you want to specify it for a particular object, then you have to do it via configuration parameters. And this will be applicable for individual test case folders. Now I'll show you how you can do this. But let's first go through all the different steps here. The next step is to create the recovery scenarios.

[01:44] And you can do it at the test case level. So either you can create it for test case folder or the individual test cases. And the last step is to specify when this recovery scenario should be applied for your test cases. And that you can do using this property which is called retrial level. Once you have created your recovery scenario, you can go and change this property. Now it may be by default set to test case, but you can also put other values like the step value, the step and the test case.

[02:23] So what does it mean? It means this recovery will kick in when a test step value or a test step or a test case fails. Now you can change it based on your scenario or your requirement, but you have to put something on this property retrial level. So all of these three steps are important. And this is how you can configure your recovery scenario for your test cases. Now let's go to Tosca and see this in real time how you can apply this coverage scenario, how you can enable them and how you can create them in your test cases.

[03:06] So I've now launched my Tosca commander and let's see how we can enable recovery at a global level, which is for all the objects in the workspace and that you can do by going to your settings. And inside the settings you need to go to T box inside T box. You need to go to recovery and here you will find different options in order to configure or enable your recovery scenarios. So you can enable recovery scenario at three levels.

[03:38] The first is on dialogue failure. Second is on exception failure and the third is on verification failure. So the first one is related to your failure with respect to your specific application. So if Tosca is not able to interact anymore with the application due to some unexpected failure, then you can specify a certain value here. So choose what Tosca should do in this case.

[04:12] So let me expand this and here you can see all the values and the comments. So there are four different values either you can halt the execution completely. You can execute the next test case. And you can continue with the execution or you can just do a recover. Now these are all the four values. If you want to work with recoveries you have to select a recover in this particular case.

[04:45] And similarly you need to change all of these if you want to recover from all of these different types of failures. So on dialogue failure on exception failure and on a verification failure in all these cases Tosca should run the recovery scenarios. So that's what we are currently setting this. Now there are three other properties called test case retries, test step retries and test value retries. Now what are these?

[05:15] These are the maximum number of recovery attempts Tosca will do in order to recover a particular test case, a particular test step or a particular test step value. Now you can choose any value or enter any value here. You can do a two or three or you can set different values for all the different types or you can have the same values here. So this is where you enable your recovery at a global level for all your objects in the workspace.

[05:47] Once you do that just close this window and it will enable the recovery for all the objects. Now say for example you don't want to apply the same level of recovery for different objects on your workspace. In that case what you can do is whenever you are creating a test case folder you can go to test configuration. So I have created this recovery folder and here under test configuration you can add different test configuration parameters.

[06:22] So click on create test configuration parameter and here you can select on dialogue failure. And you can select a value. So I want to recover. Similarly again I can add another test configuration failure and I will say on exception failure and I will say recover. And the last one which is on verification failure. And here also I will say recover.

[06:53] So this is how you can set the recovery at a folder level. Once you do this the global settings will be overwritten. So whatever you specify here will apply and not the global settings. And similarly you can do it for how many times you want to do this reattempt. So that again you have to add a configuration parameter. So let's search for them.

[07:24] So these will be test case retries. Okay, and I have to specify some value I'll specify one for now and then. You can also add the other ones like test step retries. And the last one which is called the test step level retries or it should be. Let's search for them.

[07:57] Okay set the step value retries. So here I can specify just two and two. Okay, so these are all the parameters which we have set at a test case level. Okay, and this will overwrite the global entries. So our first step is now complete. We have enabled recovery at our test case folder level right and now we want to create a recovery scenario right and how you can do that as I said earlier you have to do it at a test case level.

[08:32] So go to a test case folder and here right click and then go here and select create recovery scenario collection. Okay, you can also use the shortcuts control and control R. Okay, so let's do this right now and you will see here it will create a folder called recovery scenarios, right? So this is the parent folder again. You need to right click on this and you need to now select create recovery scenario. Okay, so you can create multiple scenarios inside this and this is our recovery scenario folder, right?

[09:08] The difference is this is a white plus and this is a red plus. Okay, now inside this we need to create a collection of test steps, right? So which can be executed when this recovery is triggered by doska. But first let's understand where we will apply this recovery and why would apply this right? So to do this I have made a very dumb test. Okay, so what I have done is I want to click on this submit button here, right?

[09:43] But now what has happened is there has been a development change, right? So if I refresh this page, you will see now the submit button is disabled for around 13 or 14 seconds, right? So after this time is gone, then only the submit button would be enabled, right now consider for this example. This is the change and our test is going to fail right because the previous functionality was submit button was always enabled and now the current functionality is it is enabled after some time is spanned, right?

[10:17] So now we have to think about how we can recover out of this failure, right? I can go and directly change my test. But if I don't want to do that every time there is a functionality change like this, right? So I need to think of a way where I can recover out of unexpected errors in my executions so that my executions are not halted because of some change or some unexpected error, right? So for this particular example, I have created this three test steps, right?

[10:50] So it will open the URL it will click on the submit button and it will close the page now here what I have done is I'm also checking for whether that button is enabled or not before I click on that button, right? So ideally it should feel here because it won't be enabled as soon as I launch the page, right? It has to wait for some time and that's where we have to enable our recovery scenario, right? Now, let's first see how this execution will fail and then we'll see how we can apply a recovery scenario to make this pass.

[11:27] Okay, so let me close this and let's go ahead and run this and scratchbook now while this is executing another important thing to note as recovery scenario only works when you run your test using an execution list. Okay, so if you run it using a scratchbook the recovery scenario won't So it will execute just as a simple test the recovery scenario won't work.

[11:59] Okay. So as expected the test has failed as you can see and that is what we expected out of this. Okay, so the submit enabled the verification has failed now here. I can also apply two types of recoveries, right? I can either do it at a test case failure level or I can also do it at on verification failure, right? So I can basically enable it at any of these places, right?

[12:31] So before we add a recovery, right? We need to also do the third step, which is the retry level property, right? So we have to set some retry level property value here. So when you create a recovery scenario go to the properties here, you will find the retry level and we have to specify some level where this retry should be kicked in. So it either it could be a test step the step value or test case, right?

[13:01] So for this example, I will keep it as test case. Okay. And now what I'm going to do is I'm going to search and add a test up here so that this test up would be kicked in whenever the recovery scenario is enabled. Okay. So here what I want to do is I want to check or I want to wait for this particular button to be enabled before it goes and clicks on it.

[13:32] Okay. So that's what I want to do. So I'm going to change this action mode to wait on and I will wait for it to be enabled. Okay, so this wait on action mode it will ask Tosca to wait until this particular value is achieved for this particular object. Okay, so I will rename this I will say check submit. Okay. So this is my recovery scenario as you can see and this is my test step inside the recovery scenario.

[14:08] Now what will happen is when this particular test case which is the submit when this fails this retrial level will kick in and it will identify that my test cases field and it will ask the recovery engine to start the recovery scenario, right? So it will go into this recovery scenario and then it will execute this particular step which is to wait till that particular button is enabled and then again, it will execute the test case, right?

[14:38] So it will again come here and it will again check whether it is enabled and it will click on it and then it will go to the other steps, right? So this is the flow now, let's see whether it actually works or it doesn't work, right? So as I said, we have to do it in execution list, right? So let me track my execution list here and I have already created a execution list folder. So I'm going to drag this recovery folder into my execution list folder so that execution list is created here.

[15:15] I will say here recovery, right? And this contains my recovery test case. Okay, so let's go ahead and run this so that our recovery scenario can now kick in when there is a failure and it can recover out of that failure so that the test cases pass. Okay, so let's see this in action now. So at this point the test case is failing but it has already kicked in the recovery scenario where it is asking Tosca to wait till this particular button is enabled and then it will again execute the test case will see this all in our results where it will be more clear what is actually happening, right?

[16:08] So if I go back to my execution list here and I go to my execution here, the open URL is working fine, right? And if you go into the submit if you look carefully here, the first step has failed right? The submit enabled has failed because the submit button was not enabled and hence it failed and then what Tosca did is it kicked in this recovery scenario, right? So where it is waiting for that button to be enabled, right?

[16:42] It is executing this particular step and after that again, this step is getting executed here, right? And this is where it is coming and it is now enabled. So it is clicking on the button and that's where this particular test case has passed, right? So it has attempted just once because I had put in one one attempt, right? If there are scenarios where you want Tosca to attempt more than once, right you can increase the test case retries right or the retry levels so you can do it here.

[17:22] On the test configuration parameter. So test case retries you can increase this to any value, right, but in my case it should be done at one retry, but in some other scenarios it might take more retries, right so you can set any values, but if the test case passes it won't go into the other retries. Okay, if it fails then it will continue retrying until this value is reached. Okay.

[17:52] So this is how you can use recovery scenario to recover your test cases from unexpected failures or unexpected exceptions. Now there is also another concept called cleanup scenarios. Okay, and that I would be explaining in the next session. So keep watching our channel for more Tosca lessons coming up every Friday. So see you next Friday with another new Tosca lesson.
