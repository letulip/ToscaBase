---
id: "2ynHXKyfLFc"
title: "Tosca Tutorial | Lesson 87 - Send Attachments in API Messages using Tosca API Scan | API Testing |"
url: "https://www.youtube.com/watch?v=2ynHXKyfLFc"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 87
duration: 258
upload_date: "20230429"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:04:55Z"
status: "raw"
---

# Tosca Tutorial | Lesson 87 - Send Attachments in API Messages using Tosca API Scan | API Testing |

[00:07] hey everyone welcome back to this Tosca automation playlist and we are talking about API testing now we have looked at many features available in the Tosca API scan and today I am going to show you how you can add different attachments to your API message through API scan okay so let's go ahead and create a new message here API message and I'm going to call it test attachment okay and for this we are going to use a endpoint this is a sample endpoint which is available in Postman okay it is the Eco service which is used to test different features of Postman it's a sample API service which is available with Postman okay so I'm going to use this endpoint okay and we have to change the method to post okay and then we need to go to the

[01:09] attachments tab okay so from the payload you will see there is a attachments tab here and uh here you can specify the name file content type right and here you can also load from a file okay so when you click on file there will be a load button which will appear here with three ellipses click on that and it will ask you to upload the file which you want to attach okay say for example I want to attach this Json source file okay so I'm going to click on open and then the content type will be automatically uh displayed here so Tosca EPS can will automatically detect what is the content type and then the name will also appear here I can obviously I can change this but let in V for now okay so you can see you can load the file from here and then automatically all the other fields will be provided here okay

[02:09] now there are some additional options here like content transfer encoding content type omit file name okay so you can do that you can omit the file name and you can also enable m2om now frankly I am not aware what is this but I can check back and provide this in the comments if you require this okay but for now uh this is what we are going to do we are going to attach this file uh with this particular API message and we are going to run this now and you will see that in the status code we'll get a 200 okay and in the payload so this particular API message it just gets back the complete content of your attachment file okay so this is the file content of the file which we have attached obviously it is encoded so you cannot see what is there in that particular content which is

[03:12] being returned by the response right but uh this is how uh for API messages where you need to send Maybe a file a image or anything right you can attach that file or you can send an attachment right from your request okay you can just browse for the file and then uh you have some additional options and after that you can just send the message and you will get back the response so it's a very simple way of uh basically attaching different files which are required for your particular API message and that's all for this short video I hope you enjoyed it and you learned something new do tune into our channel to watch more videos on trash and testoster and API testing using the Tosca API scan
