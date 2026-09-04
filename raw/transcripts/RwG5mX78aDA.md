---
id: "RwG5mX78aDA"
title: "Tosca Tutorial | Lesson 93 - Backup & Restore Repositories | Multi-User Repositories |"
url: "https://www.youtube.com/watch?v=RwG5mX78aDA"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 446
upload_date: "20230907"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:30:34Z"
status: "raw"
---

# Tosca Tutorial | Lesson 93 - Backup & Restore Repositories | Multi-User Repositories |

[00:06] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. In this session, we are going to look at how we can backup and restore repositories on Tosca Commander. Now Tosca Commander allows us to backup and restore two types of items. One is the entire projects. It could be either a single user project or a multi-user project. It also allows us to backup and restore component folders, which are nothing but smaller projects inside your big project.

[00:43] So backing up a single user project is pretty simple. So for example, this particular single user project can be backed up by just exporting the subset. And then whenever you want to restore this project, then you can just import it again. So exporting a subset is pretty easy. Take one export subset and then here I can store some name like the same name. So it will store this as practice.tsu.

[01:17] So this way you can easily take a backup of your current single user project. And then whenever you need it, you just import the subset again, maybe in a different project. Just go ahead and import the practice.tsu. So click on open and then it is going to ask you to merge all the different objects because this is the same project. So don't do it on the same project, probably do it on a different project where you want to recover this.

[01:56] Now coming to the multi-user projects, it's a little different than single user projects. So for multi-user projects, the backup includes all the workspace objects, the project settings, properties and also if you have got any version data. The main prerequisites before you take a backup of your multi-user project is you You should make sure that you have got enough disk space because the backup file could be about 20% of the size of your backed up repository.

[02:33] And to restore the database repositories, you need create and drop rights. So let's go ahead and open a multi-user project now like this multi-demo. And then the process involves you to open the workspace as an admin user. So only an administrator can take a backup of a multi-user project. So we are going to sign in using the admin credentials. And after this you have to go to project and then info here there is an option to backup the currently used common repository.

[03:13] So click on that and then it will ask you to exclude object versioning history from the backup. You can click yes or you can click no. And then it will ask you for a folder where you want to store this particular backed up repository. So let's go ahead and create a backup folder here.

[03:46] And then I'm going to select that and click on OK. Now depending on your repository size, this could take minutes or hours. Since my repository doesn't contain much objects, so it was done in a quick instance. But it could be different based on your repository size. So that's how you can backup your multi-user project. It will be stored in the file extension of .tdp.

[04:19] So that's the file extension. And then in order to restore a particular backup, we don't need to go into any project. So we are going to close this. And Tricentis actually recommends that whenever you restore a backed up repository, it should always be in a newly created repository. Because if you restore your backup in an existing repository, Tricentis Tosca is going to overwrite all the existing data.

[04:53] So you should not be doing it in an existing repository. You should always do it in a new repository. So here we need to go into project, again info. And then we need to go into the restore option, which is now available because we have got a backup. So click on that restore and it will say that when restoring any existing data in the affected repository will be discarded. You will not be able to undo or roll back this transaction. OK, so make sure you are aware of this before you restore your particular project into this repository.

[05:32] OK, so here it will ask you for a restore db repository selected file. So we can go to that particular location where we stored this Tosca workspaces. And then in the backup folder. OK, so this is the file multi demo dump and it is dot dgp. Right. So after this, so after that you click on open. OK, and then it will ask you for the type of repository.

[06:07] OK, so it could be a new repository and actual database like Oracle MS SQL or DB2 or it could be SQLite. OK. And then the connection string. OK, so if you are using Oracle or SQL Server schema is optional and then you click on test connection and then click on OK. OK, so this is going to overwrite all the all the data in the particular repository.

[06:38] Right. So I am not going to do that. But this is always helpful when you have got regular backups of your repository or your projects, then in very rare scenarios where you lose any particular data due to any particular problem in your database or in your complete infrastructure, then you can always use this backup to restore your repository or project in a different repository.

[07:08] Right. That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching and I will see you in the next video.
