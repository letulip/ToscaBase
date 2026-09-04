---
id: "RwG5mX78aDA"
title: "Tosca Tutorial | Lesson 93 - Backup & Restore Repositories | Multi-User Repositories |"
url: "https://www.youtube.com/watch?v=RwG5mX78aDA"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 93
duration: 446
upload_date: "20230907"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:05:27Z"
status: "raw"
---

# Tosca Tutorial | Lesson 93 - Backup & Restore Repositories | Multi-User Repositories |

[00:08] hey everyone welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist in this session we are going to look at how we can backup and restore repositories on Tosca Commander now Tosca Commander allows us to backup and restore uh two types of items one is the entire projects it could be either a single user project or a multi-user project it also allows us to uh backup and restore component folders which are nothing but uh smaller projects inside your big project so backing up a single user project is pretty simple so for example this particular single user project can be backed up by just uh exporting the subset and then whenever you want to restore this project then you can just import it again so exporting a subset is pretty easy click on export subset and then here I can store some name like the same name

[01:11] so it will store this as practice dot TSU okay so this way you can easily take a backup of your current single user project and then whenever you need it you just import the subset again maybe in a different project okay so just go ahead and import the practice dot TSU okay so I'll click on open and then it is going to ask you to merge all the different objects because this is the same project right so don't do it on the same project uh probably do it on a different project where you want to recover this now coming to the multi-user projects it's a little different okay than single user projects so for multi-user projects uh the backup includes all the workspace objects the project settings uh properties and also

[02:13] if you have got any version data the main uh prerequisites before you uh take a backup of your multi-user project is you should make sure that you have got enough disk space because the backup file could be about 20 percent of the size of your backed up Repository and to restore the database repositories you need create and drop rights so let's go ahead and open a multi-user project now uh like this multi demo and then the process involves you to open the workspace as an admin user so only an administrator can take a backup of a multi-user project so we are going to sign in using the admin credentials and after this uh you have to go to Project and then info here there is an option to backup the currently used common Repository okay so click on that and then it will

[03:15] ask you to exclude object versioning history from the backup you can click yes or you can click no okay and then it will ask you for a folder where you want to store this particular backed up a repository okay so let's go ahead and create a backup folder here and then I'm going to select that and click on OK now depending on your repository size this could take uh minutes or hours right uh since my repository doesn't contain uh much objects so it was done in a quick instance but uh it could be different uh based on your repository size so that's how you can backup your multi-user project it will be stored in the file extension of dot TDP okay so

[04:20] that's that's the file extension and then in order to restore a particular backup okay so we don't need to go into any project so we are going to close this and Crescent is actually recommends that whenever you restore a backed up repository it should always be in a newly created repository okay because if you restore your backup in a existing repository try sentence Tosca is going to overwrite all the existing data so you should not be doing it in existing repository you should always do it in a new Repository so here uh we need to go into project again info and then we need to go into the restore option which is now available because we have got a backup so click on that restore and it will say that when restoring any existing data in the affected repository will be discarded uh you will not be able to undo or roll

[05:21] back this transaction okay so make sure you are aware of this before you restore your particular project into this repository okay so here it will ask you for a restore DB repository selected file so we can go to that particular location where we store this dosca workspaces and then uh in the backup folder okay so this is the file multi demo dump and it is dot tgp right so uh after this after so after that you click on open okay and then it will ask you for the type of repository okay so it could be a new repository an actual database like Oracle Ms SQL or db2 or it could be a sqlite okay and then um the connection string okay so if you

[06:21] are using Oracle or a SQL Server uh schema is optional and then you click on test connection and then click on OK OK so uh this is going to overwrite all the all the data in the particular repository right so I am not going to do that but this is always helpful uh when you have got regular backups of your repository or your projects then in in very rare scenarios where you lose any particular data due to any particular problem in your database or in your complete infrastructure then you can always use this backup to restore your repository or project uh in a different repository right that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you

[07:22] in the next video
