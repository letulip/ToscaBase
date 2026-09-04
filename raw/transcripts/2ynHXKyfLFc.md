---
id: "2ynHXKyfLFc"
title: "Tosca Tutorial | Lesson 87 - Send Attachments in API Messages using Tosca API Scan | API Testing |"
url: "https://www.youtube.com/watch?v=2ynHXKyfLFc"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 258
upload_date: "20230429"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T10:35:54Z"
status: "raw"
---

# Tosca Tutorial | Lesson 87 - Send Attachments in API Messages using Tosca API Scan | API Testing |

[00:05] Hey everyone, welcome back to this Tosca Automation playlist and we are talking about API testing. Now we have looked at many features available in the Tosca API Scan and today I am going to show you how you can add different attachments to your API message through API Scan. So let's go ahead and create a new message here, API message and I am going to call it Test Attachment and for this we are going to use Endpoint.

[00:42] This is a sample endpoint which is available in Postman. It is the EcoService which is used to test different features of Postman. It's a sample API service which is available with Postman. So I am going to use this endpoint and we have to change the method to post and then we need to go to the Attachments tab. So from the payload you will see there is Attachments tab here and here you can specify the name, file, content type and here you can also load from a file.

[01:23] So when you click on file there will be a load button which will appear here with three ellipses. Click on that and it will ask you to upload the file which you want to attach. Say for example I want to attach this JSON source file. So I am going to click on open and then the content type will be automatically displayed here. Tosca EPS scan will automatically detect what is the content type and then the name will also appear here.

[01:56] Obviously I can change this but let it be for now. So you can see you can load the file from here and then automatically all the other fields will be provided here. Now there are some additional options here like content transfer, encoding, content type, omit file name. So you can do that. You can omit the file name and you can also enable MTOM. Now frankly I am not aware what is this but I can check back and provide this in the comments if you require this.

[02:34] But for now this is what we are going to do. We are going to attach this file with this particular API message and we are going to run this now. And you will see that in the status code we will get a 200 okay and in the payload so this particular API message it just gets back the complete content of your attachment file. Okay so this is the file content of the file which we have attached.

[03:05] Obviously it is encoded so you cannot see what is there in that particular content which is being returned by the response. But this is how for API messages where you need to send maybe a file, image or anything. You can attach that file or you can send an attachment right from your request. You can just browse for the file and then you have some additional options and after that you can just send the message and you will get back the response.

[03:45] So it's a very simple way of basically attaching different files which are required for your particular API message and that's all for this short video. I hope you enjoyed it and you learned something new. Do tune in to our channel to watch more videos on Tricentis Tosca and API testing using the Tosca API scan.
