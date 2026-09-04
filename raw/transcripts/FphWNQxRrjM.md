---
id: "FphWNQxRrjM"
title: "Tosca Tutorial | Lesson 33 - Use Do & While Loops | Building Test Cases | Control Flows |"
url: "https://www.youtube.com/watch?v=FphWNQxRrjM"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 695
upload_date: "20221021"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:13:54Z"
status: "raw"
---

# Tosca Tutorial | Lesson 33 - Use Do & While Loops | Building Test Cases | Control Flows |

[00:00] Hey everyone, welcome back to another lesson in this Tosca automation course. In this particular video, I am going to talk about conditional loops and how you can use them in your Tosca test cases. The first loop which we are going to talk about is the while loop. Now this is a pretty common loop statement which is used in all the different languages and if you have worked in this already, you would know what a while loop does. The logic is pretty much the same in Tosca.

[00:30] So in Tosca, if it checks for the condition and if it is fulfilled, test steps within that loop object are run repeatedly until the condition is no longer satisfied. So we are going to look at it using an example and this is how it will look like. So what basically I am doing is I am trying to do the repetitions logic using a while loop. We have seen how we can use the repetition property to repeat our test steps number of times.

[01:01] So we can do that using loop statements. So what I am doing here is I am setting a repetition buffer and then I am using the while loop to check a condition whether that repetition is less than 5. If it is not less than 5, then it will exit the loop. If it is less than 5, then it will do some calculation and repeat the loop. So this looping will continue until this condition is not satisfied or the repetition becomes more than 5.

[01:32] It will exit the loop and it will go into the next test step. So this is what basically we will be doing using the while loop. Another important thing to note here is while loop also has a property called maximum repetitions. Now this is to avoid infinite loops and Tosca by default sets this value to 30, but you can change it. So this is what is about while loop. Now, let's look at our example where we will try to build a test case using this while loop and it will be based on this particular flow chart.

[02:05] Okay, so I'm going to create a new test case here and I'm just going to call it a while loop. Okay. And here I am going to demonstrate how you can use your while loop. So as we saw in our flow chart that we want to set a variable or you can in Tosca terms it is known as buffer. Okay, we are going to talk about buffer in a different video. I'm not going to explain a lot about it, but it is like a variable which you can use throughout your test case.

[02:38] Okay, so I'm going to add a test up here to set a buffer value and this is the T box set buffer module. So here you have to provide a buffer name. I am going to call it R. Okay, and I'm going to set the value to zero. So this is my T box set buffer and after this I am going to add or create a while loop. Okay, and that you can do right click on this test case and there you will find create a while statement.

[03:13] Okay, so that will create the while statement with a condition and with a loop. Okay, so in the condition we have to specify some condition and that is to check whether the repetition buffer is less than a certain value. Okay. So again, I'm going to add a test up here. I am going to say evaluate. Okay, so I'm going to use the T box evaluation tool where I can put an expression and which will be evaluated or verified.

[03:46] Okay. So in this case, I'm going to use my buffer. Okay, so I will say B of R and I will say this will be less than five. Okay, so as you can see, this is the expression which will be evaluated by the T box module. So this is our condition and then in loop if this condition is satisfied, we need to add something. Okay. So here again, I'm going to use the set buffer.

[04:18] Okay, so what I'm going to do is do some calculation here. So I'll put it R and I'm going to use a function called math. Okay, so this is a Tosca function which you can use to do some calculations basically and inside this I'm going to use my buffer which I have created. So B of R, okay. And then I am going to add one to this particular buffer every time this loop is executed.

[04:52] Okay. And then let's close this and let's close this. Okay, so this is our calculation which we are doing we are using the math function to basically add a number or plus one to this buffer every time this loop is executed. Okay. So this is our loop and this is our condition and this is the buffer. Okay, you can change these names here which I have set so you can give some useful names here.

[05:26] Okay. So I can call it set repetition. Okay. And here I can say check repetition less than five and here I can say calculate repetitions. Okay, so this is how our flowchart looked and that is what I have done here.

[06:01] Okay, just a minute I have to give the test step not the so I will say here set repetition. Okay, so this is the step name I mistakenly I have put it in my buffer so that buffer should be R otherwise this expression won't work. Okay, the other thing I wanted to show you is for this while statement.

[06:31] So if you go to properties you will see there is a property called maximum repetitions whose value is 30 I can change it. Okay, let's go ahead and execute this test case. So go and run in Scratchbook and it should hardly take a few seconds to do this. It's not doing much here, right? So here we are setting the repetition buffer. It will go into the while loop and you can see there are six repetitions, right?

[07:02] So the loop is continuing it is going to check for this condition. Yeah, it's evaluated to true. So it will go into the loop and it will basically do that calculation right in the last repetition. The expression would be evaluated to false and hence it will exit out of the loop. So this is how you can use while loop. You can use it inside your test case to basically do any kind of configuration or basically put some logic around your test cases or test scenarios.

[07:37] Now let's talk about the next step of loop, which is called the do while loop. Now it's pretty similar to while loop, but there is a little difference the way it works. Okay, so in this the test steps within the loop object are run repeatedly until the condition is no longer fulfilled and the major difference between a while loop and a do while loop is the statement would be at least executed once in a do while loop even if this condition is not satisfied because the condition would be satisfied later on, right?

[08:14] So this calculate repetition would at least execute once before it checks the condition, but it's the other way around in the while loop. Okay, so this is how the flow chart looks like pretty similar. Only thing is the loop begins by doing the calculation and then it checks for the condition. Here also the maximum repetitions property is present to avoid infinite loops and the default value is set to 30.

[08:45] Now coming back to Tosca, you can easily do the same thing using the do while loop with what we have done with the while loop, right? So I would just show you how you can do this, right? So let's create another test case and we can give it a do while loop name. Okay, in inside this right again, you can set the buffer and you can do things like set repetition here. So I will just copy the step here, right?

[09:19] Because it's the same thing with what we want to do. We want to set the buffer for repetition and then basically we need to add a do while statement here. Okay, so how you can do that? Right click and you can see here create do statement. You can also use the shortcut control and then control D. Okay, so I'm going to add a do while loop here. So it will have a do loop and a do condition. Okay, and basically again, you can set this check repetition.

[09:55] You have to put it under condition. Okay, and this calculate repetition you have to put under loop. So that's how quickly you can create the same test case basically using the do while loop. Okay, so I have just copied the steps here. This will calculate the repetition and this will check for the repetition. Okay, so let's quickly execute this and check the results would be pretty much similar.

[10:30] Okay, the only difference being the way it is executed. Okay, so you can see here it is calculating and then it is going into the condition. Right, so it is evaluating that expression and it will repeat until this expression is false. Okay, so in the last repetition it is going to say five is less than five evaluated to false. So it will exit the loop and go into the next test step.

[11:00] Okay, so the number of repetitions are different in a do while loop and so depending on your test scenario, you have to decide which one you want to use. Okay, but these are two different conditional loops which you can use in Tosca to make your test cases more flexible and to handle more scenarios. So this was all about conditional loops. Stay tuned for more Tosca videos coming up pretty soon. We are trying to upload a new Tosca video every Friday. So watch out for these videos or every Friday on our channel.
