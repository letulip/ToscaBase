---
id: "qeYPDWYYEX4"
title: "Tricentis Tosca Tutorial Part-14: Tosca User Management, Tosca User Group, Tosca Password Reset"
url: "https://www.youtube.com/watch?v=qeYPDWYYEX4"
channel: "LambdaGeeks"
playlist: "Tosca Tutorial from Scratch"
playlist_index: 14
duration: 553
upload_date: "20211107"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T09:26:53Z"
status: "raw"
---

# Tricentis Tosca Tutorial Part-14: Tosca User Management, Tosca User Group, Tosca Password Reset

[00:15] Hello friends, welcome back to our channel. I am your Tosca instructor and my name is Kumaresh. I have total 14 years of IT experience in software development and test automation. Thank you for connecting with us. Hope you are doing well. Let's start our today's session. Through this video, I will explain the steps to create and working Tosca Commander users.

[00:45] Working with groups and Process to disable the users. The entire explanation will be done through hands-on demonstration. Now, I will explain the detailed steps for create Tosca user. Set password by admin. User assignment to admin group and Change password by user. Alright. Let us start the demo.

[01:19] First, select the Tosca workspace root directory. And check out. Then, click on management tab to open user management section. The right section of the Tosca Commander window contains the users and group. By default, admin and all users groups are available. Right click on all users and click on create user icon to create a new user. The new entry represents the user name.

[01:50] Rename it accordingly. Here we are creating the user with name test. Enable field should be checked by default. Level represents the user proficiency which has three values basic, advance and expert. After creation, user has the empty password. So, it's advisable to set the password. Right click on user and choose the set password option. Then enter and confirm the new password.

[02:25] This option is only available for admin user. To provide the admin access to the newly created user, we need to drag and drop it into admins group. Though the user instance exists in both the groups. If we change in one place, same will reflects into all the instances. The password set option is available here for the admin user only. Which means an admin can set or change the password of any users through this option.

[02:56] Now, save the workspace. Click on check in all icon to save the newly created user information into repository. We will check the user now. First, close the workspace. Creating of workspace will take couple of seconds. After user creation, we can access the workspace using new user after performing the update all for existing or need to create new workspace using the shared repository.

[03:33] Now, reopen the workspace from here. Again it will takes couple of seconds to appears the user prompt. Once the prompt appears, we need to enter the new test user details and click on login button.

[04:10] The user credential is case sensitive. So, we will re-enter the user details properly. After validating the credential, Tosca will open the workspace for the test user with default view. We will open the project component and check out the root directory. Now, the logged in user can change the password by right clicking on root directory and selecting the change my password option.

[04:46] To change the password, we need to enter the old password first and click on OK button. Now, we will enter new password for the test user. We need to enter the new password again to confirm it. The password is now successfully changed. Check in the workspace to update the repository. The changed password can be used from the next time.

[05:26] Now, I will explain the detailed steps for create group. Assign user to group, grant access to group and disable user. Let us start the demo. First, check out the project root directory. Right click on top of the user management section and select the create user group option to create the new group.

[06:01] Rename the new group based on our choice. To assign users into this group, we need to drag and drop any existing users here. Let us drag the new test user. Now, we will grant access to this group in any components such as modules. We will check out the modules first. Open the property section of the modules component. Now navigate to the owning group property drop down from the property section, select the newly created group from here.

[06:38] This will grant the access on modules components to the new group and the users associated with it. Similarly, we can grant the access to other components as well. Now, we will understand how to disable the user. Navigate to user management section and select the user. To disable the user, we need to uncheck the enabled checkbox for this user.

[07:09] Same change is replicated to other instances as well. Perform check in all to update the changes in shared repository. We will now close the workspace and reopen it.

[07:54] Once the user pop-up appears, we will try login with the credential for the test user. It's not allowing as the user is already disabled through admin login.

[08:24] Thanks for watching this video. That's all about Tosca user management. Please stay tuned for more interesting videos on Tosca. Please visit our website lambdageeks.com for more articles on technology, engineering, mathematics and various other domain. You can check our other website as well. We have features like YouTube Trends, Twitter Trends, Scientific Calculator and many more other tools.

[09:03] If you like our video, please like, comment and share. If you have any questions, please comment and we will resolve your query.
