---
id: "2xPO0SHEHLo"
title: "Tosca Tutorial | Lesson 50 - Add Cleanup Scenarios to Test Cases | Recovery Engine |"
url: "https://www.youtube.com/watch?v=2xPO0SHEHLo"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 50
duration: 526
upload_date: "20221104"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:01:53Z"
status: "raw"
---

# Tosca Tutorial | Lesson 50 - Add Cleanup Scenarios to Test Cases | Recovery Engine |

[00:02] Hey everyone, welcome to another lesson in the Stoska automation course. In the previous session, we talked about recovery scenarios. How you can recover your test cases from an unexpected failure or error. But before I continue, I must say you have to watch the previous session in order to understand this session better because these two topics are quite related. So if you don't understand how recovery scenarios work, you won't understand how cleanup scenarios would be working. Right? So coming back to recovery scenarios, when we employ a recovery scenario and the application state now changes so that it can recover out of unexpected failure, right? But what if this recovery also fails? So tosska is not able to recover out of that error and now it is stuck in a state from where it cannot continue.

[00:55] So your all your test steps which continue after this uh failed test step would also fail because the application is in a state from where it cannot execute those test steps. Right? So to resolve this problem toka also provides you an additional option called cleanup scenarios. Now it is also part of the recovery engine. So when the recovery scenarios fail, it goes into this cleanup scenarios and you can define your own test steps to bring the application back to the original state.

[01:31] So for example, if um you are closing and opening the application in your recovery scenario, right? And uh it is not able to open the application. So all your test steps of continuing after this will fail. Right? So in this case what you can do you can put some test steps which can go back and launch the application login into that page and go to that particular page from where it will continue the next steps. Right? So all these test steps you can mention in the cleanup scenarios.

[02:07] So let's uh take it little further and let's try to understand with our original example where we employed our recovery scenario right so we employed our recovery scenario on this page where we were trying to click on the submit button and it takes around few seconds to enable this right so we had put a recovery scenario to wait on this button until this is enabled and then it will click right so that way we were able to recover uh from an unexpected failure.

[02:39] Okay. Now think of a scenario. We want to click on the next link, right? Which is open new page. So on clicking this link, it opens the same page in a different tab. Okay? But uh what is the scenario is if the submit button is still not enabled, right? You cannot go ahead and click on this link unless you reopen the application and then you will be able to directly click on this open new page.

[03:10] Okay. So that's that's the kind of scenario which is present in front of you. Now I'm just trying to relate uh to this recovery and cleanup scenarios so that you can understand uh this scenarios better and you can employ it same into your application whenever you face this kind of scenarios right. So uh in this kind of scenario what we can do is even if our recovery fails to click on this button right uh we go ahead and put two steps where we close the page and reopen this page so that this open new page link is now enabled and we can click on it directly. Okay.

[03:51] So we don't have to go through this loop. We uh do a different way of clicking on this page. So we bring back the application to its original state. Okay. So this is what our scenario is. Now let's go to TSA and see how we can implement a cleanup scenarios. Okay. So you have to have a recovery scenario in order to add a cleanup scenario. Okay. So when you have created this recovery scenarios folder right the parent folder right click on it and you will see there is a icon where it tells create cleanup scenario okay you can also use the shortcuts CtrlN and Ctrl C okay so click on that and then it will create a cleanup scenario okay and inside this we can add our steps so what I want is I want to close the page and I want to reopen on the page. Okay. So

[04:52] I can directly go here and I can copy this test steps into this cleanup scenario. So I first want to close the URL and then I want to open the URL. So I will just copy it here and paste it here. Right? So I have two test steps now in cleanup scenario. Close URL and open URL. And this will bring back my application to its original state from which then it can continue to execute the other test steps. Right? Which is to open new page and then it will uh finally close it or any other test steps. Right? The main idea is if the recovery scenario fails, we also have a cleanup scenario where we can bring back our application to its original state.

[05:41] Okay. So that's the main idea. Now uh let's go ahead and execute this right and see whether it works or not. Now if you have created your execution list and you are making some changes to your test cases right just to be sure that these changes are also reflecting in your execution list. You can right click on it and click on synchronize. Right? So it will synchronize the changes between the test cases and the execution list. Okay. Now let's go ahead and click on run. Okay. And let's see whether it works or not.

[06:22] So in this particular scenario, it is going to fail the test step and the recovery scenario. And in that particular case, it is going to employ the cleanup scenario. If you have noticed in the screen, it has reopened this application, right? And after that, it is going ahead and performing the test steps which could have been blocked if there was no cleanup scenario. Okay. So, let's go ahead and look at these logs, right? So, let's go into this submit log and this is the current execution. So, you see this submit enabled this uh this is failed this test step. The recovery scenario has also failed. Okay.

[07:08] But after this recovery scenario has failed, it has now enabled this cleanup scenario. Right. So it has gone into this cleanup scenario and it has closed the URL, opened the URL. Basically, it has executed this test steps. Okay. After this was done, now it went ahead with the remaining test steps. Right. So combining both cleanup scenarios and recovery scenarios, you can ideally come out of unexpected failures or errors from which your execution can still continue. Even if there are failures, your execution will not stop, right? So that way you can have a better execution cycle because uh then you can look at those failures and go ahead and fix them. But at least your execution will go ahead and it is not stuck if your recovery scenario fails or if your test step fails. Right?

[08:10] So this was all about cleanup scenarios. Hope uh it was useful for you. We would come up with another interesting topic next Friday. So keep watching and do subscribe to our channel. We also have a webinar on uh tricentis tosskut live training going ahead on this Sunday the 6th of November. So if you are interested please go ahead and register at our site www.qascript.com.
