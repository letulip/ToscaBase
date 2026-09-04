---
id: "SLWKhb4igB0"
title: "TRICENTIS Tosca 16.0 - Lesson 11 | Test Case Automation | Run your First Automated Tests | TCP |"
url: "https://www.youtube.com/watch?v=SLWKhb4igB0"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: null
playlist_index: null
duration: 830
upload_date: "20230105"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:57:57Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 11 | Test Case Automation | Run your First Automated Tests | TCP |

[00:10] Hi, everyone. This is Ravi. Welcome back to Tricentis Tosca automation tutorial. So, as you all know, I have published three lessons, my previous three lessons that covers how to automate test cases in Tricentis Tosca. So, as you all know, to automate test cases by using Tosca, we need to follow a series of steps. So, in my previous three lessons, I have covered step 1, step 2 and step 3. Step 1, where we have created test case structure. Step 2, where we have created test steps for your test case structure.

[00:56] And step 3, where we have populated the values for the test steps. Now, this is our fourth step and last step, where we will be running our first automated test by using Tosca. Please do subscribe to the channel, click on bell icon, you will receive notifications whenever I publish more videos. Thank you. Okay, run your first automated test. So, before we run your first automated test, we need to do some configurations. That is called test configuration parameters in Tricentis Tosca world. What is this TCP, test configuration parameter? This is a parameter you can set for the Tosca object. Example, test case should run on a specific browser.

[01:54] Then you can specify a TCP of browser. If you want to run the test in different releases, then you can provide the configuration of release number. If you want to run in the various test environments, you can set up test configuration parameters. And if you want to have a different connection identifiers in different environments, and then you can configure different URLs. So, basically, this simplifies maintenance of your tests and avoids the repetitions. And how to populate, so basically the populate a specific test case with test configuration parameter. So, populate different levels, basically TCP or test configuration parameter can be populated at different levels like test case level, test case folder level, and at execution list level. If assume, if you provide a test case configuration at test case

[03:03] level, and some different test case configuration at execution list level. So, execution list I did not cover, but just assume that there is an execution list where you provided configuration as a different value. And in test case, you provided a configuration as one value. So, both are different. Then when you run test case by using execution list, then the test configuration parameter whatever you specified in execution list will override the TCP that you specified in test case. And then I am going to teach you how to run automated tests in scratch book. So, let me, let us jump on to the system and show you how can you perform all these activities by using latest Tosca 16 version. So, this is my Tosca 16.

[04:10] In my previous session 10, session 9 and 10, we have created a separate folder, and then we have populated test steps under your test case structure, and also we have populated all the values for your test steps. So, now let us use the same folder. Let us copy this folder, right click and click on copy and paste into your parent folder.

[04:47] And then rename this as session 10, sorry, session 11, run automated test. And now, so, this is my test case. So, earlier we already right click and expand, we already populated all the test steps and all the test step values in my previous sessions. Now, it is time for us to run the test. So, before you run the test, as I explained you in my previous slide, slide, you need to perform some test configuration. So, if you want to run this test in Chrome, you need to provide test configuration parameter called browser and provide the browser name.

[05:55] For that, so, you need to click on your test case. So, as I told you, you can specify your test configuration parameters at test case level, folder level and at test step level. So, right now I am at test case level, go to test configuration, right click on your test case. If you see here, there is a menu called create test configuration parameter, select that. And here, you need to select parameter called browser and then you need to select the browser name that you would like to run on. So, now for today's session, I would like to run your test in Chrome browser, select that, done. Now, go back to details. Now, I want to run this particular test case,

[06:59] this entire test case. There are two ways, either you can run your test from your details tab. So, basically, we are going to run the test in scratch book. So, as I told you, scratch book is a temporary test runs. Your trial runs can be performed on scratch book, so that you can debug your automated scripts very easily. And the scratch book will give you the temporary results, which will not be saved in the system.

[07:38] Okay, so now let's say I want to run this entire test. So, now, let's run our test, right click and click on run in scratch book. As soon as you click on run in scratch book, it is going to open your web browser and it enters the URL and it is going to execute every step that we specified. Clicked on login, clicked on apprentice shoes, it is going to click on blue jeans and then it is going to enter the quantity and then click on add cart, right and then check out. So, it enters all the payment, billing information, shipping method and everything. Let's continue entering.

[08:26] It is done. It is now entering the credit card details and then checked out, confirm, click on continue, log out and then close the browser. So, if you see, it gives you a temporary result, so that you can analyze the results, if all the results are successful or not. If you see here, these are all the, if you see everything is marked in green color, that means every step, whatever we automated is pass, correct. So, this is one way.

[09:03] So, how to debug your test case? So, if I want to run, let us assume, I just automated precondition. If I want to run only these three steps, what should I do? You have to select the steps that you would like to run by using shift button. I selected this, right click and run in scratch. So, it is going to run only these three steps. So, now let us see, that means it just performs your login. That is it.

[09:40] If you see, it gives you the results. See, only login. So, that is one way of running and another way of running the test cases. So, you can use your existing scratch book, if you see on top ribbon, there is an option called scratch book. And keep this scratch book and let us say, I want to run probably, let us assume, I want to run these steps.

[10:15] Let us login and keep it ready. For this, I am going to login and keep it ready. So, now I want to run from here. You just need to drag and drop. Let me just close. Open your scratch book. Let me again. So, open your existing scratch book and you need to just drag and drop the steps. Let me clear entries.

[10:55] Let me clear entries. Now, what you can do is, so let me just open the scratch book. Take the scratch book to the right of your pane. Now, let us say, I want to run these three steps. Drag and drop these three steps here to the existing scratch book and then right click and run. So, that means, I am using my existing scratch book and then I am running the test.

[11:34] Correct. So, that way you can perform your test, I mean, trial runs by using scratch book. So, earlier actually, what happened actually, there are two tabs that are open. That is why it got failed. Let me run it again. So, it opens the browser. It clicks on login and then it enters your username and password. That is it. So, this way, if you see, this is the all steps got passed and then again you can close your scratch book.

[12:14] So, this way, you can basically use from, let us say, I want to run from here. You can directly select this checkout process, for example. You can directly select this checkout process and run scratch, run in scratch book. That means, it is going to run only these steps, steps that are involved in checkout process folder. So, you can run at folder level, you can run at the step level or you can run at entire test case level also. Okay. So, hope you all understand how to run your test in scratch book and how to analyze the temporary test results and how can you configure your test configuration parameters for a specific test case. So, if you have any queries, please provide your comments in the comment box. I will try to respond to your queries.

[13:10] Thank you. Hope you all understand the concepts of test configuration parameters in Trisantistoska and how can you run your first automated test by using Trisantistoska in scratch book. If you have any queries, leave your queries in the comment box. Please do subscribe to the channel, click on bell icon, you will receive notifications whenever I publish more videos. Thank you.
