---
id: "c-VgJF2i1mU"
title: "Tricentis Tosca Tutorial Part-3 : Tosca Initial Project Setup, Tosca Workspace Overview & Creation"
url: "https://www.youtube.com/watch?v=c-VgJF2i1mU"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 3
duration: 580
upload_date: "20210826"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T08:46:00Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-3 : Tosca Initial Project Setup, Tosca Workspace Overview & Creation

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the overview of Tosca workspaces and guide you to create different types of Tosca workspaces to start our hands-on for test automation.

[00:45] Alright, let's starts with the concepts of Tosca workspace. The Tosca workspace is nothing but a repository to store different components which are required for test automation. To develop, maintain or execute the test cases, we need to connect the workspace first. The Tosca workspace stores the information of important components such as modules, test cases, data, execution, requirement, etc. for test automation.

[01:19] The workspace has to be defined in local work system. But, the data of Tosca workspaces can be synced to different databases such as SQLite, SQL Server, DB2, Oracle etc. which can be acted as a shared repository. Let's discuss on classifications of Tosca workspaces. New types of workspaces are available. Single user and multi-user workspace. In a single user workspace, only one user is able to connect and work with Tosca.

[01:53] So, the central repository is not required here. In a multi-user workspace more than one users are able to access the workspace. So, the Tosca workspace has to be created in central repositories. Tosca allows to create the workspace in different databases such as Oracle, SQLite, DB2, SQL Server, etc. In the multi-user workspace, the data management is more simple and easier as the data are stored in shared databases which are known as common repositories.

[02:32] To perform any transaction such as add, edit, delete in a multi-user workspace, we need to lock the corresponding records first. It will restrict any other users to manipulate the same records. After completion of the transaction, W need to unlock the records. In Tosca, locking of data is known as checkout and unlock is known as check-in. Before starting of workspace creation, we need to understand the different values of repository type.

[03:02] Based on the selection of this field, the single or multi-user workspace will be created. It has five different values such as none, SQLite, Oracle, MS SQL Server and DB2. If we select the value as none, single user workspace will be created. For other values, multi-user workspace will be created and the selected database will be used as a central repository. Once we select the appropriate repository name, the database related field will be appeared such as schema name, connection type, etc.

[03:42] In this video, we will learn how to create single user workspace and multi-user workspace with the help of SQLite database. Alright, now we will learn how to create the single user workspace. First of all, we need to open the Tosca Commander and click on create new option to open workspace creation screen. Prior to Tosca version 14.x, workspace creation new option was available in project tab. Now, we need to enter the mandatory fields in this screen.

[04:15] As we are creating single user workspace, the central repository is not required. So, we will select the option none for the field type of repository. The path for the new workspace can be provided here. We will keep the default path and proceed. After that we have to enter the name of the workspace which we are going to create. We are using the name as single user workspace. The use workspace template option allows us to include additional components such as default modules, reusables, report templates etc. which will helps for automation activities.

[04:54] We can include our own components or the default one. Here, we will use the default option which is required for test automation. Now, we are ready to create the single user workspace by clicking on OK button. It will take few seconds to configure and create the single user workspace. After creation of the workspace, success message will be appear and the close button will be enabled.

[05:27] After closing the window, Tosca loads the newly created workspace which contains the different components of Tosca. The default view of Tosca workspace contains the sections such as test cases, modules, requirements, test case design, execution, etc. We will discuss on each of the sections later.

[05:59] Now, to view the workspace hierarchy, we need to click on project option which is available in home tab of the Tosca header. It's all about single workspace creation. Now we will learn how to create the multi-user workspace. First of all, we need to open the Tosca commander and click on create new option to open workspace creation screen. As we are creating multi-user workspace, the central repository is required.

[06:31] So, we will select the option based on our database. If select Oracle, then we need to provide the additional schema and connection string. Here, we will SQLite option and provide the corresponding repository path. We will keep the default path and proceed. For first time, use existing repository checkbox should be unchecked. After that we have to enter the name of the workspace which we are going to create.

[07:03] We are using the name as multi-user workspace. We can include our own components or the default one. Here, we will use the default option which is required for test automation. Now, we are ready to create the multi-user workspace by clicking on OK button.

[07:33] It will take few seconds to configure and create the single user workspace. After creation of the workspace, success message will be appeared and the close button will be enabled. While creating the multi-user workspace, we need to connect the workspace through The default user is admin with empty password.

[08:09] Here, to update any component, first, we need to perform the checkout. And after completion of update, we need to perform check-in to save the details in repository. We can view the project and reset the password by right-clicking on hierarchy.

[08:42] That's all about creation of multi-user workspace. Thanks for watching this video. That's all about Tosca workspace related topic. We will learn more about Tosca test case automation in next Tosca tutorial. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain.

[09:13] You can check our other website as well. We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools. If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
