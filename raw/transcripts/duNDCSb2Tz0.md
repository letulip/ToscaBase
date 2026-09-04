---
id: "duNDCSb2Tz0"
title: "Tosca Tutorial | Lesson 90 - Create Multi-User Workspace | SQLite DB | CheckIn/Checkout | Repository"
url: "https://www.youtube.com/watch?v=duNDCSb2Tz0"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 905
upload_date: "20230321"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:34:57Z"
status: "raw"
---

# Tosca Tutorial | Lesson 90 - Create Multi-User Workspace | SQLite DB | CheckIn/Checkout | Repository

[00:05] In this Tosca session, we are going to talk about the multi-user workspaces in Tosca. Now, until now, we have seen how to create a single-user workspace and how to use it. Now, this single-user workspace can be used by only one user at a time, right? If multiple users want to use the same workspace, you have to create a multi-user workspace in Tosca. Now, you might think that multi-user workspace can only be created if you have got a database connection in place, but it's not always true, okay?

[00:40] So Tosca also provides you with an option where even if you don't have a particular database like Oracle or SQL Server or DB2, you can still create an in-memory database multi-user workspace and that can be done using the SQLite, okay? So there is an option to create a multi-user workspace using SQLite. You don't require any connection strings for that particular database type and you can use it to create a multi-user workspace to check out the functionality in Tosca.

[01:17] But one thing you have to remember is this SQLite workspace cannot be used in a real-time project, okay? It can be used for a demo or practice, as I said, to check out the functionality for multi-user workspace, but it is not a real solution where you can use it for a real project, okay? For real projects, you should have a dedicated database instance, either Oracle, MSSQL Server or a DB2 workspace, right?

[01:48] But for practice, we can still use this and that is what I'm going to show you how you can create a multi-user workspace and then probably you can check out all the functionalities which come up on this multi-user workspace, which is not available in the single-user workspace, okay? So the process is almost the same, okay? So not much changes if you're not using a particular database instance. Then you don't need to provide the connection string which contains the username, password and the DB connection string.

[02:22] But for SQLite workspace, if you're creating that, you don't require those, okay? So when you come to the Tosca Commander screen, there is a create new option, okay? And until now we have been using this type of repository as none, which will create a single-user workspace. But now we are going to go into the other option which is SQLite, okay? As I said, if you have a dedicated database instance, you can use Oracle, MSSQL Server and DB2.

[02:52] So if you look at the MSSQL Server, so you will have some additional fields which you need to fill, okay? The most important is the connection string. Now if you have this connection string and if you place it here, you can test the connection, okay? And once the connection is valid, then you can create your workspace in that particular database. So that is the process, okay? And it will be similar for Oracle or DB2, okay? So any kind of database you require, you have to at least give a connection string.

[03:27] Now schema is not mandatory, it's an optional field. So it's mostly the connection string and then testing the connection, okay? So for SQLite, as I said, you don't require the connection string or the schema, right? So as you can see, those fields are not available. But still it will create a multi-user workspace for me, okay? And that's what I'm going to do, okay? So it will create the new workspace in this folder. You can always change this to any particular folder.

[04:01] You have to give it a name, okay? So what I'm going to give is multi-demo, okay? So this is my multi-user workspace and you can also create a slim workspace. Slim workspace will take less amount of space, but if you have got a high data volume, right? Then you should use the slim workspace, which will basically speed up your whole repository.

[04:35] But if not, then I prefer not to use it, okay? Also if you have not created any other repository using this particular or any other workspace using this particular repository, then do remember to check out the use existing repository. Otherwise, you cannot proceed, okay? So let's check out this and now I can see that it has been enabled, okay? So once you have created a particular workspace using this repository, then you can click on this use existing repository, okay?

[05:11] Now click on okay and it will start creating a multi-user workspace for you. Once it is created, it will open that workspace. And now we can see some of the options which will be enabled, right? Which were not present or disabled when we are using a single user workspace, okay? Also one major difference, you will see that for single user workspace, there was never a login screen, right?

[05:43] But now you can see that there is a login screen. Now if you get this kind of a login screen when you create a multi-user workspace for the first time, okay, you would wonder what is the password for this workspace. But for now, Tosca has created a user for you, which is the admin, which is the default user and there is no password for it, okay? So don't enter any password and click on login. So now you can create different users in this kind of a workspace also when you go into your project, okay?

[06:18] So if I open my project and I put it here, you can see there is a green sign which is displayed and this green sign which is displayed for every particular section or object, right? Project tells you that these objects are checked out or the project is even checked out, okay? So there is a checkout and check-in process which is there for a multi-user workspace because multiple users are working on the same workspace.

[06:51] So there has to be a process of how the changes will get merged, right? When multiple users are working in a workspace. So when you create or open a multi-user workspace, right, the objects which are checked out, you can only work on those particular objects, okay? Now if you see any particular object with red color in the beginning, like a red stripe, then that means that object is checked out by some other user and you basically on that particular object or on that particular folder, right?

[07:33] Because somebody else is working on that. So this is how the checkout and check-in process works. So if a particular object or folder has been checked out by any particular user and he's working on it, no other user can basically make any changes to that particular folder or object, okay? So once you complete working on a particular folder or object, you have to check in your changes. And if other users are simultaneously working on other objects or other folders, right, and they check in something, then there is an option called update all, right?

[08:12] So when you click on this update all, what it will do, it will fetch all the changes from the repository or the database, right? And it will merge those changes into your particular workspace, right? So you will get all the changes which has been done by other users on different objects right into your repository before you work, right? So before you start working on a multi-user workspace, you should always do an update all.

[08:45] This process can also be automated using the Tosca TC shell commands, right? You can put a file which can update all the repositories before you start working on that, okay? Or else you can manually come and do it here. Just do an update all so that it fetches all the changes from the database if multiple users are working on that, okay? And if all the objects are checked out by you, then no other user will be able to work on this.

[09:17] So once you finish your work, you should always remember to check in all which will basically do a check in of all your changes, right? So there are basically four options when you are working within a team, right? So this section tells you that. So there is update all, as I said, there is check in all which will check in everything which has been checked out by you, okay? And then there is a checkout option and a checkout tree option. Okay, so let's see what is the difference between a checkout and a checkout tree option, okay?

[09:52] So checkout basically it it is related to just one single object, but checkout tree will basically check out all the objects which are contained inside that particular folder or inside that particular object, right? So if you look at any particular folder, right? So if I go into this execution folder and I right click on this, I will also get this option. So either you can check out from here or you can do a checkout tree from here, okay?

[10:26] Now if I do a checkout, so if I am doing this checkout, it will basically check out only the execution folder, but it will not check out the other objects which are contained inside this execution folder, right? So if you want to work on all the objects in this particular folder or say if you are working on a particular test case folder, right? So you will what you will want is you will want to check out the complete folder because currently you are working on it and you don't want anyone else to change that.

[11:01] So in those kind of scenarios, you should basically do a checkout tree so that all the objects are checked out which you are currently working on and then you can check in all once you finish working on that, okay? So that's how you should be working on see now if you have not checked out any particular object or folder like this test cases, okay, you can see there is option to either create a folder or a test case template or a test case, right?

[11:33] So it is not showing any options and that's what happens when you work in a multi user workspace. You have to first check out that particular object which is the test cases folder and when I right click on this, now I get all the options, right? So I can create a folder, I can create a test case, right? So if I create a test case folder like this, right? And then I create some test cases here, okay?

[12:04] And maybe another test case. So I have got these many test cases inside this folder, right? And now I do a check in all and it will basically check in everything inside my repository, right? So the execution folder was checked in, the test cases folder was checked in, okay? Now if I want to work on this folder in test case zero one and I don't want anyone else to make changes to this because I expect a lot of changes in all the different objects, okay?

[12:39] So in that kind of a scenario, I can do a checkout tree, right? So if I do a checkout tree, all the objects inside this folder will be checked out and nobody else can basically do any changes on this, right? And once I finish this, I can do a check in all which will basically check in everything which I have changed in my workspace and then other users can access these changes, okay? So as you can see, this is basically a check in checkout process.

[13:13] It is pretty much similar to any code repository if you have worked on Git or GitHub, you will also follow this check in and check out process where you check out your code changes and you do the code changes and then you check in into the repository so that other developers can or other testers can basically access those changes, right? And if there is any conflicts, then you have to resolve that conflicts and you have to merge your changes with other developers. So it's a similar process here in Tosca as well, right?

[13:47] There is basically just one difference is that whenever you are working on a particular object, it doesn't give access to other developers. They have to wait until you check in, right? So it's very important that once you are completed with your work, you do a check in all and before you start working, you do a update all so that you get all the changes. So it's pretty simplified so that if many users are working in a multi-user workspace, they don't get many conflicts and you don't have to spend time on resolving those conflicts and doing a merge, right?

[14:25] So Tosca simplifies this process. It's just every user will work on its own objects and then once they check in all or update all, those changes will be merged and available for everyone, okay? So this is one aspect of multi-user workspace when you work on a real time project, you have to follow this process of check in and check out and also the update all.
