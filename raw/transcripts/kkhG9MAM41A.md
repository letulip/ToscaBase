---
id: "kkhG9MAM41A"
title: "Tosca Tutorial | Lesson 95 - View Latest Change Details | Checkout Details | Revoke Checkout |"
url: "https://www.youtube.com/watch?v=kkhG9MAM41A"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 348
upload_date: "20230912"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:28:49Z"
status: "raw"
---

# Tosca Tutorial | Lesson 95 - View Latest Change Details | Checkout Details | Revoke Checkout |

[00:08] hey everyone welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist in this session we are going to look at some of the options which are available to the normal users and the admin users in a multi-user workspace apart from checking in checking out and update all which we have already seen so some of the other options which we are going to talk about is a way to look at all the changes which have been done to any particular object it could be from any particular user if you are a user or admin user it doesn't matter you can still see the changes which have been done by other users then we can also look at the checkout details so this will basically tell you if that object has been checked out by someone else and who has actually checked out that particular object and if you are an admin user you can even revoke the checkout on a particular object so that it is made available to all the users again

[01:10] so let's see how we can do all of this uh for this particular purpose I have created another user under all users which is called test okay and we are going to log in with this particular user now so let's go ahead and close this workspace and now I am going to login with the test user so here I am going to enter the username and password and then click on login and now what we are going to do is basically check out a particular folder here so let's say we check out this tc01 okay so I'm going to check out this folder and then I'm going to close this particular workspace without checking in this changes okay so I'm going to close this and subscribe Commander will ask me if I want to check in and I will say no this is on purpose and then we are again going to login

[02:11] with another different user which is like an admin user and then we will see how we can revoke the changes on that particular object and whether we can see the checkout details for that particular object and the change details so here instead of test I am going to login as admin and again admin click on login now let's go to that particular folder and here you will see the difference that in tc01 a red bar is shown on the left hand side which means it has been checked out by a different user now uh until that user doesn't check in those changes into this folder I cannot actually perform anything here so I cannot create any test case any folder or anything else okay so now uh the options which we are talking about now if I right click on this uh there is an option called show latest change details so when you click

[03:12] on this you will see that it will show you the name the time the change was done and the user who made this change okay so that will show you uh the change details and then show checkout details the second option so it will show you what time it was checked out by which user and the name of the folder or the object so these options will basically help you to find out if some changes have been made by some other user or if some object has been checked out and if you want to work on that particular object you can reach out to that particular user if you know uh who has actually checked out this particular folder right now since this is an admin user I can also go ahead and revoke this checkout now few things to remember before you revoke a particular checkout that the changes will be discarded okay so no matter uh if you try to check in later on uh these changes will not be merged

[04:13] or available in the workspace once this is revoked so if you want you can still revoke the checkout as an admin user it is not available with any other user okay you need to have the admin permissions in order to perform this change now right click on the particular object which you want to revoke the checkout and there you will find an option called Reebok checkout now click on this and Tosca will then warn you that all changes in this object will be discarded so click on OK and then you will see that now this folder is no more checked out and you can now perform all the different operations which you want to but first obviously you need to check this out right so now I can check out this folder and now I can create a test case um or a test case folder inside this particular test object right and then I can check in all the changes which I have done and then everything

[05:15] becomes normal again so these are all the options which are available to a particular user and admin user on a multi-user workspace and this is how you can revoke checkouts you can look at the checkout details or you can even look at the latest change details that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
