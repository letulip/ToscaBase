---
id: "YOvThZyYOaM"
title: "Tosca Tutorial | Lesson 57 - Use condition in Test Case Instantiation | Test Case Templates |"
url: "https://www.youtube.com/watch?v=YOvThZyYOaM"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 517
upload_date: "20221001"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:34:00Z"
status: "raw"
---

# Tosca Tutorial | Lesson 57 - Use condition in Test Case Instantiation | Test Case Templates |

[00:00] Hey everyone, welcome to another lesson in this Tosca automation course. Now in previous videos I have shown you how you can create your test case design sheet, how you can link it to a template and then how you can create different template instances out of your test case design sheet and your test case template. Now today I am going to show you how you can conditionally create different test case template instances. Now what does it mean is depending on some condition some test step would be part of a particular instance and at the same time if that condition is not satisfied then that test step will not be part of a particular instance, right?

[00:44] So you need that flexibility because not all the test steps should be part of every instance. Okay, so let's look at a real example. So I am going to take up the same example which where we have developed this template instance for validate login. Now if I go to test case design and if we look at these two instances, right? So one is of valid user and one is locked user. Now in this scenario what we are doing is for locked user it will throw error message and we want to validate it.

[01:22] So we have put this verification but the same verification does not apply for a valid user because there is no error message and we don't want to validate this particular error message or any kind of verification for this valid user, right? But when you link this test case design sheet to your template, what will happen is it will create two instances, okay, but it will have the same steps irrespective of the fact that there is no validation error for a valid user but the step still exists.

[02:02] So during execution also although this there is no values here so it won't execute this step or it will execute this step but it will not perform any action and in the locked user it will go ahead and validate or verify this error message, right? But in real-world scenario you don't want when there are lots of different steps you don't want to confuse the tester and put all the all the test steps for all the different instances, right?

[02:34] You should be having some business logic based on which you will have different types of test cases or test instances, right? And the flow of those test case instances should be different based on some business logic, right? Now that is where condition comes into picture and you conditionally instantiate your test cases based on some business logic, right? So let's see how you can do this, right? How we can make this verification message test step to go away, right?

[03:09] In one of our template instance for valid user. So we don't require this valid error test step in a valid user test case. We just require it for locked user, right? So that's that's our scenario. That's what we want to achieve and I'm going to tell you how you can do that in Tosca. Okay. So the first step for this is to go to your test case template and here we need another column called condition. Okay now the same way we have to do we have to go to column chooser and here we have to find our column and we can drag and drop it or just double click it to add it to our test case template.

[03:52] Okay. Now we have got a condition column. Now we have to put some condition on our validate error desktop, right? So here either we can type the condition or we can do a drag and drop the recommended way of Tosca is to drag and drop the condition and not type it so so that you don't make any mistakes. Okay, so we have to drag it from the test case design sheet.

[04:23] So let me just pull this aside so that we can have a look. Okay, so let's open our test case template and here we want to put a condition in this particular step, right? What we want to do is we want to put some business logic here, right? So what would be our business logic? So in case of a user when it is the username standard user, the password remains the same, right? So it doesn't change but the username changes.

[04:56] So when it is a locked out user, it throws this error message and that's our business logic, right? So when the username equals to locked out user, then go ahead and verify or execute that particular step otherwise don't do it, right? If it is standard user, we don't want to do it, okay? So either you can have a step like not equals to standard user or you can have a step where username equals to locked out user, okay? For me, I will do the second one where I want to put this username locked out user, right into my test case condition or my test step condition.

[05:38] So to do that, you need to go to your instances, right? So expand the instances and then drag and drop this locked out user instance into our condition, okay? Now as soon as we drag this, so let me close or bring this to the center. Let's go to a test case template right now. If you look at this condition column, okay for this valid error and you will see here the logic here is process dot username equals equals locked out user.

[06:17] Okay, so I can also type this directly in this condition column, but I will follow the recommended way of dragging and dropping that particular instance into this column and that will create a condition for me automatically. Okay. So whenever this process dot username equals equals this then only it will go ahead and instantiate it. So while instantiating it it will either skip this or it will add this step. Okay, and whenever you see this particular arrow signs with two dots, then it is clear that this is a conditional test step.

[06:59] Okay for normal two arrows. It is a normal test step for two arrows with two dots. Then it is a conditional test step. Okay. So wherever you see this, you should be clear that this is a conditional test. Okay. Now we have made changes to our template right now. Now we have to reinstantiate our template instances so that it creates the right test cases for us. Okay, so let's go to our template instance.

[07:32] And now you can see there all the test steps are same but that's going to change. Okay, so right click and go ahead and reinstantiate the instance. And you will see that Tosca automatically removed the test step for the valid user, but the locked user still has that test step and that is because of our condition. Okay. So this is how when you are creating hundreds of test cases and you want to put some business logic by creating this test cases you have to use the condition column.

[08:10] Okay, so you should put it in your template and then reinstantiate your template so that the right kind of instances are created with the right kind of business logic. So that was all about reinstanciation of your test cases with condition. Look out for more videos on our channel related to Tosca coming up pretty soon.
