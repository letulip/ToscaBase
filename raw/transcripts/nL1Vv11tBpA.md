---
id: "nL1Vv11tBpA"
title: "Tosca Tutorial | Lesson 51 - Create TestStep Libraries | Reusable TestStep Blocks | Parameters |"
url: "https://www.youtube.com/watch?v=nL1Vv11tBpA"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 813
upload_date: "20230325"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:58:33Z"
status: "raw"
---

# Tosca Tutorial | Lesson 51 - Create TestStep Libraries | Reusable TestStep Blocks | Parameters |

[00:05] Hey everyone, welcome back to our channel and today we are going to talk about another interesting topic in Tricentis Tosca. So today I'm going to discuss about how you can add different TestStep libraries and then how you can basically add different reusable TestStep blocks inside these libraries which can be used or reused across different test cases. Now what is the need for this? So in any test automation framework you always have different common reusable libraries.

[00:42] This increases the reusability factor which is very important for any framework and also it becomes easy for us to maintain our test cases because we will be using this reusable libraries which can be then changed at only one place rather than changing it everywhere. So it saves time, it makes our development more faster and more efficient. So in other frameworks you might have to do some customization or you have to build these reusable libraries, right?

[01:16] But in Tosca it already provides you a future where you can create these TestStep libraries and if you have already created your test cases you can just convert these into reusable TestStep blocks which will then be part of the library and then these blocks can be used as a reference in different test cases, right? So this is the flow how Tosca follows or how Tosca uses the TestStep libraries.

[01:46] It is part of the test cases section, right? So you can create this TestStep libraries anywhere and these libraries could be reused across different test cases, okay? So to demonstrate this particular feature I have created a folder called reusable libraries. I have two test cases, they are pretty similar with very limited functionality just to show you how this works. So one is logging with the valid user, one is logging with invalid user, there are just two steps.

[02:21] Open URL and login user, the first one is using a valid user and the second one is using a invalid user, okay? Now if I run them you will see there is not much difference, obviously I could have added lot more steps after these two steps, okay? But these are the two steps which I feel are common for my application, okay? And that is the reason I am going to use them as reusable TestStep blocks, okay?

[02:52] So you can see in the first test case it logged in with a valid user into the website then you can continue from there but in case of this invalid user it will give this message and we can also verify this and then we can continue moving forward with whatever test case scenario we have, okay? So these are the two examples where you see there are common steps, right? So the common steps are opening the URL and logging in with a user.

[03:24] So even though the TestStep data is different, right? So one is valid, one is invalid but still this can be handled in just one common reusable steps. So this makes a good case for using a library instead of having the same steps with different test data and two different test cases, okay? So how we can create them? We can create them inside the same folder, okay?

[03:54] So right click on this and then you will see a folder with L sign and that's what is a TestStep library, okay? So you can also use the shortcut control N and control L to create this. So click on this and this will create a library here, okay? And inside this library now I can create a reusable TestStep block, okay? Or I can also, if I have already created my test cases and I have the test steps, okay?

[04:29] I can also convert this into my reusable TestStep blocks, okay? So how I can do that is I can just drag it here, okay? And I can drag these two basically steps and make it a reusable TestStep blocks, okay? So you can see here now this has become a reusable TestStep block and in the test case it has now changed into an arrow sign.

[05:02] So which means it is just a reference, okay? So it is not the actual step, it is a reference to this particular steps, okay? And now how I can reuse the steps? So these reusable TestStep blocks, I can basically delete these steps in my second test case and now I can just drag these reusable TestStep blocks into my test case, okay?

[05:33] So you can see these are almost the same reusable TestStep blocks, okay? But they are not different, they are references to the same TestStep blocks. And this you can do it across all your test cases. So wherever your test cases are using these two steps which is opening the URL and logging in the user, you can use it anywhere, okay? In any test case you can just pull this references into a test cases and they will run them, okay?

[06:07] So that solves one of our problem where we are now using two common steps which are part of a library. But now you can think these values, right? These values are still the same. So it will basically do the same thing right now. It will log in with the same user which is present in this library, right? But I want it to be more customized so that I can use my own values, right?

[06:39] I can use the own invalid user in the second test case rather than invalid user so that my scenario is as per the expectations, okay? So for that you need to now convert, okay? This or you need to add business parameters. So whatever values you want to parameterize like the username, the password or the URL, okay? Which can change across different test cases. You can basically add business parameters for these, okay?

[07:12] And to do this you need to click on the reusable TestStep block and there is an option to create business parameter container, okay? So we can add that and we can create our business parameters here, right? Once you do that now I can add different parameters here as you can see. So first parameter would be username and the second parameter would be password.

[07:44] So these are the two values which can be parameterized, okay? In this particular TestStep block and then in URL also I can parameterize the URL part. So I will do that. So I will create a business parameter for URL, okay? You do not need to provide any values or action mode or data type for this business parameters. They are just parameters, okay? And what we need to do is now we need to delete these values, okay?

[08:20] Because we will not be using these values which are static in nature, right? We will be using these parameters instead of any particular value. So you have to replace them with these parameters, okay? Let me drag this again. So now once you drag these parameters into this TestStep, right? So it will become PL and then followed by that parameter name. So PL means the business parameter.

[08:54] So similarly for open URL I will remove this value and I will drag this URL parameter here, okay? So now you can see that our reusable TestStep blocks are actually reusable, right? Because they are not using any static values. It can be used across any test case. So any particular login test case where it has got these fields and you can enter any value from the test case itself, okay?

[09:26] So now our library and reusable TestStep blocks are ready. Now if I go back to my test case, right? You will see that the business parameters are already created, okay? And you will see all the TestStep values have now been removed from the references. You just need to pass a valid URL, a username and password. Now you can again configure it more. You can put a configuration parameter in your folder and you can use that here rather than putting the directly, rather than putting the URL directly here, right?

[10:07] Same you can do with username or password. But now you can see that even though I use it in two different test cases, I can enter different values based on my test cases, okay? So it is now actually using some reusable steps which can have their own values in different test cases, okay? So for this particular example, let's go to this URL and let's try to put different values here, okay?

[10:40] So just to complete these two scenarios. So these are the username and password which I'm going to use. So first one is the valid user, okay? So that's my first test case and in the second one, I'm going to use this locked out user so that it throws an error message, okay?

[11:14] And then the URL. So URL is, as you can see, it is same. And as I said, you don't need to enter it directly here. You can create a configuration parameter like we have done many times, okay? So create a test configuration parameter for URL and just use that here, okay? But as you can see, now we have got two test cases using reusable tester blocks from a library but having different values using the business parameters, okay?

[11:52] And now if I run them, they should still run as expected like we have seen before. There should be no difference, okay? So that's our first test case and if I now run my second test case, okay? So it should display this error message which can be verified, of course.

[12:25] But okay, so that's the results we have got, okay? So we haven't put any verifications but the purpose of this particular demo was to show you how you can use a library and the reusable tester blocks with business parameters. So a very useful way of reusing your test steps across your test cases, okay? So this could be used in many complex scenarios where you have got test cases with a number of different test steps.

[12:58] So find out which are the common ones and put it as a reusable tester blocks in your libraries. So that's all for this session but do tune in into our channel if you have not subscribed, do subscribe so that you get a notification whenever I come up with more interesting scenarios or interesting features available in Tracentist.com.
