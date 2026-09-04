---
id: "o1b8cACf4Hs"
title: "Tosca Tutorial | Lesson 138 - Common RealTime Tosca Problems & Fixes | Synchronization Policy |"
url: "https://www.youtube.com/watch?v=o1b8cACf4Hs"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 502
upload_date: "20240307"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T14:02:04Z"
status: "raw"
---

# Tosca Tutorial | Lesson 138 - Common RealTime Tosca Problems & Fixes | Synchronization Policy |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So today I'm going to talk about a common issue which people face, especially when they are new to Tosca or they are working in a project and they are using a multi-user workspace which has got a common repository. Now in these kind of projects, you will come across scenarios when there will be folders or there will be objects which you are not able to access.

[00:46] Even though I have done an update all, which means all the objects are already updated from the repository. So I have got the latest changes here in my current workspace, but still I'm not able to access some objects. For example, this vehicle insurance folder. It looks like a common component folder, but actually it is grayed out. And also the objects inside these component folders are also grayed out.

[01:21] And there you can see there is a cloud sign here for configurations and test events. So when I click on these configurations and test events, they get somehow enabled for me. The remaining are still showing as disabled. And if I right click on this and go to the context menu, I don't see a checkout option. The checkout option is grayed out. Now if you notice, there is also another option, which is the checkout tree option, which seems to be enabled.

[01:56] So let's go ahead and try this. So when I click on this, you will see that Tosca will tell me that there are no objects to check out, but I've got lots of objects which are currently not accessible to me. So why Tosca is telling me that there are no objects to check out? So why it is like this and what's the solution for this? Because I cannot access this folder, so I cannot create any object inside this.

[02:26] I cannot edit it or I cannot check it out, right? So basically, this folder is inaccessible to me, even though I am working in a workspace, which is connected to the correct repository and I have already done an update all. Okay. Now, first, let's understand what is the reason for this, okay? The reason for this is this folder and all of its objects are currently excluded from synchronization.

[02:58] Now, what is synchronization? So synchronization is a process where all the objects from your current workspace is synchronized with the changes made in the repository, okay? So the repository and the workspace will synchronize all the changes. So your local workspace will be up to date with the repository changes, okay? But if you're working in a project, sometimes some folders will be excluded from synchronization and that is done on purpose, especially for large workspaces where you have got lots and lots of objects.

[03:37] This is to make the workspace more efficient because the processing time will increase if you have got lots of objects to synchronize every time you open a new workspace. And that is why some of the folders are excluded from synchronization so that it can save some time for the automation testers when they are opening the workspace and they will include only the folders which are required for their own work and they will include them for synchronization if they are not already synchronized, okay?

[04:12] But initially, these folders will be inaccessible for them. So the solution for this is simply go to that particular object and just do either select include all necessary items for tree or include for synchronization, okay? So when you select this particular option, so what Tosca will do is it will include that particular object for synchronization and then it will synchronize it with the common repository, okay?

[04:44] So now this particular folder will be accessible. So this is how you can include your objects for synchronization. If you want to exclude any particular object for synchronization, then this is the option, okay? So you can right click on that particular object and exclude from synchronization. You can also exclude the tree from synchronization, which means the parent object and all the child objects are also excluded, okay?

[05:16] So if I now select this, you will see that the execution folder will be grayed out, okay? So next time when I check in, this particular object will not be synchronized with the common repository, okay? And that's what is meant by exclude from synchronization. You can also exclude the tree from synchronization. And what that will do is it will exclude all the child objects from the synchronization and everything will be grayed out, okay?

[05:49] Now, there are a few other things also, like if you go to any particular object and if you check it out, okay? Then in the properties section, you will find a property whose name is synchronization policy. Now, by default, all the objects are set to this particular value, which is customizable default is on, which means by default, all the objects are included for synchronization, okay?

[06:19] But you can also set this off, which means it will not be included for synchronization. You can also set it to cannot be excluded, which means anybody cannot just exclude that folder for synchronization or object for synchronization. And also you can choose this option, which is cannot be excluded for whole tree, which means all the child objects can also not be excluded from synchronization, okay?

[06:49] So all of these different options you can choose whenever you are creating a new object in your project, depending on the situation and depending on what you want to do, you can select any of these options. But when you export or import any particular objects, then it is reset back to this particular property value, which is customizable default is on, okay? Also, if the customizable default is on for one particular object, then all the child objects which you create under that object will also get the same value, which is set for the parent object, okay?

[07:30] So this is how you can set different synchronization policy, and this is a common issue, as I said, especially with newcomers who are new to Tosca or who are just starting to work in their respective projects, who are working on a multi-user workspace, which is connected to a common repository. So this issue is very common and very frequently occurred. And that's why I thought I would talk about this so that you are aware of this particular problem and you know why it happens and also what is the workaround for this.

[08:08] That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching, and I will see you in the next video.
