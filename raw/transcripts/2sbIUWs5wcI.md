---
id: "2sbIUWs5wcI"
title: "Tosca Tutorial | Lesson 126 - Random Mathematical Operations | Evaluation Tool | Obstacle 20 |"
url: "https://www.youtube.com/watch?v=2sbIUWs5wcI"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 613
upload_date: "20240105"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:34:23Z"
status: "raw"
---

# Tosca Tutorial | Lesson 126 - Random Mathematical Operations | Evaluation Tool | Obstacle 20 |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So continuing with our topic on test automation obstacles, let's look at our next obstacle which is called math. And as the name suggests, we need to perform a math operation here. Okay, so in order to complete this obstacle, we need to complete the operation listed below and we need to enter the result in the result box.

[00:40] Okay, so this might seem pretty simple in the first instance, but the challenge here is everything is randomized. Okay, so the two random numbers you can see here are randomly generated plus the operand here, which is this minus sign, this is also randomly changing. So if I refresh this page now, you will see that the numbers are changing and sometimes the operand is also changing.

[01:12] So it could be a multiplication, it could be addition, subtraction, or even a modular operation. Okay, so whatever the operation, you need to be able to handle that into your automation. Okay, so everything should be parameterized here in a way. And using some conditions, you need to handle these changing random numbers and operands. Okay, so once we enter the result here, like for instance here, the result is 80, this operation will be completed.

[01:48] Okay. Now the ideal way of doing this would be in any programming language or any automation tool, you can make use of the switch case, right? So if I talk about Java, you can make use of the switch case, where you can have different case and based on that case, you can have a specific calculation, right? So it will fit for this particular kind of problem. But Tosca doesn't have a switch case, okay?

[02:21] So we need to fall back upon the conditional statements. And we need to use the if condition in this particular scenario, okay? So let's see how we can do this in Tosca. So coming back here, I'm going to go back to my modules section and here we'll go to obstacles, here we will add another module, okay?

[02:53] And then here we need to have the numbers, the randomly generated numbers, the operation, okay? And then we need to have the result, okay? So these are the four elements which we have to add here. So I'm going to save it and close it now. I'm going to copy the obstacle numbers here and then we are going to rename this, okay?

[03:25] And then going back to test cases, we will add a new test case here now, okay? And then we are going to add the module right here, okay? Right, so the first step here is to basically buffer all the values, okay? So what we are going to do is we are also going to name these module attributes because these are randomly changing so it won't remain the same always, right?

[04:02] So we'll change the names here and we'll call it operand, okay? And now coming back to our test case, so now these are properly displayed here, so what I'm going to do is I will be buffering all these values, okay? I will be buffering the number one, the operand and also the number two, okay? So all of these will be stored in these different buffers, so that's our first step, okay?

[04:35] So we are going to name this buffer values. Now in the second step, as I said, we need to use some kind of condition because the operand is changing and depending on the operand, we need to perform the mathematical operation accordingly, right? So we are going to use the if statement here, okay? So I'm going to use the if statement here and in the condition, then we need to check what kind of operand it is, right?

[05:07] So for that, we'll be using another test step and that is called tbox evaluation tool, okay? So here we can put some expression which can be verified, okay? So that will be our condition. So in this eval, we will be putting an expression to check what is the operand, okay? So I'll be checking here B of operand, okay?

[05:40] And I'll be putting this in quotes. So whenever you are using the tbox evaluation tool and you are working with different types of expressions, you should always use single quotes so that everything is escaped properly, okay? And then equals will be using the first plus sign, so for addition, okay? So it will check whether this operand is plus and if it is, then we will be again adding the same module here, okay?

[06:21] And then in the then statement, in the result section, we'll be using something called the math expression. So it is used to perform any mathematical calculations. So inside this, we'll be then adding the buffers, okay? So num1 and then we'll be adding num2 here and then we'll be closing this, okay?

[06:57] So this is the math expression where it will perform the mathematical operation, okay? So this is for addition. Similarly, we need to make four different if statements, okay? For four different operations. So I will be pasting this four times, okay? And then here we'll be changing the conditions, okay? So we'll have one for subtraction and we'll change the operation here and then we'll multiplication and the final one would be for a modular operation, okay?

[07:52] So we'll put the operation here and then we'll go to the last one and we will add the mod symbol here, okay? So the mod and in the then we will do that, okay? So these are all the four different operations which we need to perform, okay? And everything is inside if else statement.

[08:26] Although it is not super efficient way of doing this, but there is no other way of doing this particular problem, right? So we need to use the if then else statements. So now we are going to mark this as completed. So that's all what we need to do and now let's go ahead and run this couple of times so that we can see it is working for all the different operations, okay? So I'm going to run this, okay?

[08:57] So as you can see, the result was populated with the correct value and the automation obstacle was completed, right? Now you can see now this particular sign has changed, okay? So it is a subtraction now. So what we'll do, we will go ahead and run this once more, okay? So as you can see, both of the times everything was changing, but still the automation was able to handle all those changes.

[09:30] And effectively, this is automating the calculator itself, right? Because we have been performing all the calculations which are part of the calculator. So this is how you can perform different mathematical operations using the math function and then using the if else statements, you can put conditions and you can check for different conditions and based on whatever condition it is, you can perform the respective operation. That's all for this particular video.

[10:01] If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching and I will see you in the next video.
