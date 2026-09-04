---
id: "IYGr51H7CIg"
title: "Tosca Tutorial | Lesson 157 - Module Properties | Configuration, Identification & Steering Params |"
url: "https://www.youtube.com/watch?v=IYGr51H7CIg"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 1681
upload_date: "20250620"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:45:42Z"
status: "raw"
---

# Tosca Tutorial | Lesson 157 - Module Properties | Configuration, Identification & Steering Params |

[00:08] Hey there, in this particular session, we are going to deep dive into the module properties. Now these module properties are created when you scan a particular module and these are applicable for both module and the module attributes. So these properties are on the right side of your window. So whenever I select any particular module, you will see the details in the middle pane and then on the right hand side, you can see the properties pane.

[00:40] Now if this is collapsed, you can expand this by clicking on this arrow and then here you will get all the module properties. Now these module properties are created by default when you scan any particular control, but you can also edit or create some of these properties on your own. So if we look at one of the module attributes, you will see these are again the properties. So the module itself will have some of its properties and then the module attribute will have some of the properties.

[01:17] So let's go through some of these properties. What are these and how they can be used when we are creating our automation scripts and also we should know what these properties are so that when we are working with different types of controls, we can work with these properties. Now although there are lots of different properties in a module or module attribute, I'm going to go through some of the important ones which we should know and also which could be useful during our automation.

[01:53] So the first one is the automation framework. Now this automation framework, it basically indicates which kind of framework you are using. So either this could be the T-box, which is the default engine for the Tosca and this is already available when you install Tosca, right? Or it could be the generic automation framework. Now this generic automation framework is when you create your own DLLs and then you deploy them into your Tosca and then they are basically the generic controls which you are using or which you have created on your own.

[02:31] So these are the two types of automation framework and then the business type parameter. So this is basically the technology specific root element. So on the X module level, this indicates the root element. Now either it could be HTML document or it could be an XML document. So we will see this when we look at an actual module attribute and then the cardinality. Now this basically specifies how often we will use a module attribute as an step value.

[03:09] Now by default, it is only one, okay? So the cardinality is defined as zero to one, which means whatever step value you have created could be used just once. Now we can increase it. So we can change it to zero to n, which means this value could be used n number of times. So example of this, we have already seen in our previous sessions when we need a particular attribute multiple times, either it could be a checkbox, it could be a button or anything, right, which you want to perform an operation on multiple times.

[03:50] So that you can do using the cardinality. Then we have got the node path. This is the unique part of the object in your workspace. So sometimes you would need to know where your object lies in the workspace, right? And then we have got the synchronization policy. Now this is basically the policy which defines what is the synchronization timeout for your modules or module attributes.

[04:21] So we can change this as well. The possible values could be, cannot be executed or customizable default is on, okay? So we can do this synchronization, enable or disable using the settings. But here you can define the policy for your module or module attributes. Then we have got the technical ID. Now this is a parameter which is to define a technology specific property. It will be mostly defined by Tosca itself.

[04:52] And then we have got the unique ID. This is the unique identification number in your workspace for your particular object. So this will also be defined by Tosca and you can use it to search your object in your workspace. Then we have got the viewing group name. Now this is the user group for whom this particular object is visible. And you can always change this based on whatever group you are giving permissions or access to. So these are some of the important properties.

[05:23] Some of them are automatically created. And some of them could be edited or modified by you based on your requirements. Now if we compare whatever we have discussed with an actual module attribute and its properties. These are all the properties. Some of them have the configuration parameter or any other kind of parameter which we will discuss in some time. But all these blue icons, these are the properties.

[05:54] Some of them have been created already. Some of them is modifiable. Some of them is not modifiable which means you cannot modify this. So the node path, it will give you the path of your object from your workspace. So you can see from the root element it is going to modules and then the swaglabs and then this username. Created by who has created this object, what time it was created, who modified it last time and what time it was modified.

[06:29] And then unique ID. So this is the unique ID to which I can easily search in my workspace. Then business type. So this is the technology type of this particular object. It is textbox currently. That's why it is defined textbox. Then cardinality we discussed. This is currently 0 to 1 so it can only be used once. But I can change it to n.

[07:04] And then it could be used multiple times, this particular module attribute. And then there are data type, action mode, interface type which is GUI which basically defines what kind of interface you are using. So it could be non-GUI, it could be GUI or implicit. And then the default value. There are some properties which we already discussed. So we discussed about synchronization policy.

[07:34] You can see these are the different values. So default is on, default is off. Cannot be excluded or cannot be excluded for the whole tree. So basically how you want to synchronize your objects across your workspace. That's what this property defines. And then the owning group name and the viewing group name. So these are the two things which we can define.

[08:07] And then the technical ID. This doesn't have a technical ID but most of the modules will have it if it is required. Tosca will grab it. And then the business type which is the HTML document. And then the automation framework which is tbox currently. So these are all the properties. As I said, some of them you can modify, some of them you cannot. But based on your requirements, you have to work out some of these properties or you have to modify them.

[08:40] So it's good to know what properties generally are defined for a particular module or a module attribute. Now moving on, we have discussed about the default properties. In addition to this, your modules or module attributes can also use specific parameters. And these parameters are defined in the properties pane or they can be created. They are case sensitive. And in Tosca, the four major types of parameters are configuration, identification, steering, and transition parameters.

[09:17] So how do you get to these? So whenever you select any particular module and go to properties, there you can create your own parameters. So when you right-click on this module, you will see the first option is to create a module attribute. Then we can create a configuration parameter. We can create a transition parameter. We can create a steering parameter. And then we can also create a business ID parameter.

[09:48] Then technical ID parameter. And then the reflected ID parameter. So this business, reflected, and the technical ID parameter all combined, they are basically the identification parameters. So these three are the identification parameters. This is the steering parameter. This is the transition parameter. And this is the configuration parameter. If you look at this module carefully, you will see that a configuration parameter is already created, which is called the engine, which is a STML.

[10:25] And then we have got three different steering parameters here, control framework, enabled slot content handling, and ignore ARIA controls. So these are basically created by Tosca itself. So we haven't created this. And then we have got a technical ID parameter, which is title, which Tosca is using, to basically identify or steer this particular control. And it has got a value. So some of these parameters Tosca will automatically create in order to steer a particular parameter.

[10:58] But then in some scenarios where you are not able to identify or if you are not able to steer a particular control, you can also create your own configuration steering or identification parameters. So let's discuss a little more about these parameters now. So let's start with the configuration parameters. Now what are these parameters that define which components should be used in order to steer a particular control?

[11:30] So some of the parameters, so there are lots of parameters again. We can go through the whole list. But these are some of the important ones and which are basically related to your web controls. Now some of these parameters could be specific to Vision AI or could be specific to a particular engine. So it depends on which particular platform you are working on. You should be using the specific configuration parameters. So let's look at some of them.

[12:01] So first is constraint index. Now this constraint index, it is used to specify the index which can uniquely identify a particular control. So if you have got multiple controls which have got the same properties in a particular web page and if you have to identify a particular control, then in this case, you can directly use the constraint index. You can put the index of that particular control and it will be able to identify it uniquely.

[12:33] Now the permissible values for this particular parameter is an integer. So you need to provide index. Then we have got can execute in parallel. Now this is basically for parallel execution when you are working with distributed execution. So you have got dex agents where you want to execute your tests parallelly. And then it is using the same module. So you want to run it in two different test cases. So in this kind of scenario, you can change the value of this parameter.

[13:07] And it could be either true or false. Then we have got the explicit name. Now by default, x-step value names cannot be changed. But if you set the value of this property to true, then you can edit the name of the x-step value. Now if you don't want to use the true or false for this particular parameter, you could also specify a value range for this particular parameter.

[13:38] So this could be useful in some scenarios where you want to identify a particular control using an explicit name. Then we have got external engine. Now this external engine is a parameter for the mobile engine modules. And it is mostly used for image-based automation. Then we have got the algorithmic association.

[14:09] Now these are the specific parameter which can be used for a search algorithm in a selected context. Now target objects are basically searched in the context. And then the logic of algorithm search query could also be used. This is a very specific scenario. So I would not talk too much about this. Then we have got the special execution task. Now using this parameter, you can perform specific tasks which could be used to steer your control.

[14:44] Then we have got the technical association. So this is a specific parameter for the search algorithm in the selected context. So a property of a test object is directly used at the context so that it can search an object easily. So it is basically engine-specific. And we can see this technical association in any of our module or module attributes. Then we have got the transition parameter. Well, this can be used to transition between technologies or contexts which could allow various engines to be used in the same test step.

[15:24] The value of the name of the transition is used for steering the control. And it could include some values like string property to XML or XPath to XML element. So if you are using XPath and then you want to transition to an XML, you can do this using this particular parameter. So these are some of the parameters which can be used in your module attribute. So coming back here, let's see how we can create a configuration parameter for maybe a module attribute.

[15:56] So we have to right-click on the module attribute in the properties pane. And then we need to select create configuration parameter. That will create the parameter. You need to use a proper name which we already discussed. So for example, I want to define the explicit name. So I will say explicit name. So it could be two faults or a particular range. So I will enter true here.

[16:28] So explicit name is true. I can even create a constraint index here. So if I create another configuration parameter and I name it constraint index, and then I can give it an index of one. So if there are multiple controls with this particular user name, it will select this based on the constraint index. And then I can even change the name of this attribute.

[17:02] So for example, when I create another test case here and then I drag this, you will see I cannot change the value of password and login because they don't have an explicit name set to true. But I can change this name of this particular module attribute, which is username.

[17:32] I can keep it user. Or I can keep it email, whatever value you want to put. So I can change the name of this because I have set a configuration parameter. Explicit name equals to true. So this is how you can create configuration parameters. And this is how it can be used to steer your controls in specific scenarios where the generic methods don't work. So now moving on, let's talk about the identification parameters.

[18:06] Now, what are identification parameters? They basically determine which properties should be used to search for a particular control to be steered. And you can combine any number of parameters using the AND links. Now there are three basic parameters which we already saw when we looked at the module attribute properties. So we can create a business ID parameter. And this can be used with specific control types.

[18:38] So these are the properties which can be used with specific control types. And these are the same for all technologies which you need to steer. So for example, each button has the property label and each text box has the property text. So you have to use it accordingly. Then we have got the reflected ID parameter. Now, what are these? These are the properties of test objects which are not included by default using Tosca can be retrieved from the target technology using reflection.

[19:18] So the technology itself needs to support the reflected object access. One thing to note here is if you are using this type of parameter, then reflected IDs are generally slower when compared to the default IDs. This parameter can be used for a very specific scenario, something like Internet Explorer, which is out of support. You can use this parameter for the language attribute. So then we have got the technical ID parameter.

[19:49] This is the more common one. It is provided by Tosca for technology specific controls. For example, value for HTML input controls, inner text for HTML elements, HTML declaration, and more. So these are all the different identification parameters which can be used to search a particular control. Now, if we come back here again, you will see we have got two technical ID parameters. One is ID, one is tag, and then it has got specific values.

[20:21] So these are added by Tosca for this particular model attribute. And accordingly, we can also create our own ID parameters. As you can see, so I can create a technical ID parameter. Again, I need to know what technical ID I am going to use and the value. Now, moving on to steering parameters. Well, steering parameters are generally used to specify the behavior for a control which is being steered.

[20:51] And there are multiple steering parameters. Some of them are very specific to specific modules like Vision AI or SAP modules or the mobile engines. So there are different types of steering parameters, but you need to use depending on what type of control you are trying to work with. Some of the important ones I have noted down here which we can look at. So one is bring to front parameter.

[21:22] Well, this will help you to bring the particular window to the foreground by default. Now the default value is true, but if you want to change it, you can change it to false, which means it will not allow the window to automatically be brought to the foreground. So it will run in the background. Then we have got the ignored invisible HTML elements.

[21:52] Now this is again a very specific scenario where in your application you have got invisible HTML elements which will be present in your application when you're doing the execution. Now it might slow the execution down. So what you can do, you can set the value to true and then Tosca will completely ignore these HTML elements. Then we have got the scrolling behavior. Now this can be used to define the control where you should position it on the screen.

[22:25] The values for this is top, bottom, center or none. So basically, once you put it on top, it will scroll from top. If you put it on bottom, it will scroll from bottom or center or if you don't put anything, it will start from a particular position. So it's basically when you are scrolling controls, you can specify the behavior of how you want to scroll it. Then we have got the send keys delay.

[22:56] Now this can be used to specify a time lag where individual characters of a keyboard command could be sent, but with a particular time delay. For example, I can set this to 100, which means it will wait for 100 milliseconds before it sends any keyboard commands through my script. Then we have got the synchronization timeout. Again, we can tell Tosca how long Tosca wants to wait before it looks out for a particular object or it throws an exception.

[23:31] So you can set this timeout right here. You can do it in the settings as well. You can do it using a configuration parameter, which you can set in a test case. So there are multiple ways of doing it. And the same for wait on. You can also set a steering parameter for that. Then we have got this user simulation. Now this is basically to click events or keyboard commands, which can be triggered using the action mode input. Now possible events could be selecting or deselecting checkboxes or radio buttons, pressing selecting links or entering text into text boxes.

[24:11] So you can either set the user simulation to true or false. The default is false. So if you want to do any of these events in your application, you can set the user simulation to true. So some of the things which you're not able to do through regular automation, you can do using this particular steering parameter. Then we have got two different wait parameters, wait after and wait before. Now these two parameters could be used to wait until a particular time, either before or after the control is tiered.

[24:49] This could be useful when you want to wait before the application is ready or a particular control is loading. So you can use the wait after or wait before. So these are all the different steering parameters. Now if you come back to Tosca and look at this module attribute, you can see there is already a steering parameter added, which is fire event, and the value is set to change. So similarly for password and then login, there is no steering parameter.

[25:21] And for this, the module itself, we have got control framework set to none. We have got enable slot content handling false and ignore audio controls false. Again, I can go ahead and add my own steering parameter. Now we can add the wait before, and we can set the value to 10.

[25:56] This will be for 10 milliseconds before it is going to perform any action on this particular control, which is the login button. So this is how you can play around with different types of parameters, which are the steering parameters. It is basically used to help you steer your controls, and you can specify a particular behavior of that particular control before or after it is being steered.

[26:28] The final type of parameter, which is present in Tosca, is the transition parameter. It is not a very frequently used parameter. As you can see here, this is the transition parameter. And we can use it, as I said, to transition between technology or context. So if you're working with mobile and x-browser engine, you can set this particular transition parameter, and then you can change your context from browser to the mobile engine.

[27:04] And you can use the same parameter, which is x-path. So I can use this for two different technologies. As I said, it is not very frequently used, but for very specific scenarios, you can also use this transition parameter. So these are all the different parameters and the properties for your module attributes. Now, although the information is lot, it is quite important to understand what properties you are working with and then what properties you can change for your controls or what additional parameters which you can add for your controls so that you can steer them as per your requirements.
