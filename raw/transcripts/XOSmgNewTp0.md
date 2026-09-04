---
id: "XOSmgNewTp0"
title: "Tosca Tutorial | Lesson 22 - Compare PDF files | TBox Automation Module | 1:1 Compare"
url: "https://www.youtube.com/watch?v=XOSmgNewTp0"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 24
duration: 468
upload_date: "20230224"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T07:59:56Z"
status: "raw"
---

# Tosca Tutorial | Lesson 22 - Compare PDF files | TBox Automation Module | 1:1 Compare

[00:02] hey everyone welcome to another interesting Tosca lesson in this session I am going to talk about how you can compare two PDF files using a t-box module so you don't need to write any particular test cases or you don't need to create any modules a module is already provided in the standard subset which can be used to compare to PDF files okay so I've created uh already a test case folder called PDF comparison for this comparison I'm going to use two PDF files these are not exactly same there is some difference in both the files right so if you are going to compare these two files uh you will see that uh the test case will fail if you have provided a hundred percent accuracy now we'll talk about that uh when we open the module but just looking at the PDF file so it's a PDF file which is generated in one of the sample

[01:02] applications which is the vehicle insurance application so it looks like that so it looks like this it has just got one page okay but you can also compare multiple uh Pages uh in your PDFs okay okay um so let's go ahead and add our module now okay so let me add this case here and I'm going to call it compare PDF and then let's search for this compare PDF so when you type compare the first option is one is to one compare now we have already seen some of the other t-box modules like file compare you can also compare images right and also a Excel file so when you use this one to one compare okay we need to provide the reference and the target PDF so reference PDF is

[02:04] the PDF which will act as a reference for the comparison and the target would be uh the PDF which you want to compare this reference PDF with okay we can also if if your PDF is password protected you can also specify the password here and Tosca will automatically enter that password while comparing the PDF okay same for Target PDF now I was talking about uh the accuracy which is in percentage okay so we can Define our own accuracy so it's basically the percentage of uh accuracy which you want for your comparison okay uh you can specify 100 accuracy which means both the PDF should be exactly same you can also decrease the accuracy if you are not worried about uh so much about uh some of the things in the PDF which may not be same so it depends on uh what kind of accuracy you require for this comparison okay and then excluded pages so here you

[03:08] can specify which Pages you want to exclude uh from the comparison so if you have got multiple pages in your PDF files you can exclude some of the pages from the comparison okay so uh we have to provide a reference PDF as I said okay so this is the path of the file which you want to compare so let's provide that okay and don't forget to also provide the extension which is dot PDF uh we don't require a password for this and let's copy this for the reference and we'll just change the name here to code two okay I will just correct the name here to

[04:08] quote underscore 2. and then uh you need to specify our accuracy so first of all I'll provide a 80 accuracy okay and excluded Pages although I don't have multiple pages in my PDF but if you have then you can provide some values like this okay so what this will do is uh you can provide multiple uh page Pages which you want to exclude so in this case it will exclude the first page the three to four page and the five page okay so which has to be separated by semicolon uh you can also combine your pages like a range like this page to this page you want to exclude okay or individual Pages depends on you so this is how you can exclude your PDF pages from comparison and these are the module attributes which you need to pass okay now if I go ahead and compare or run

[05:10] this particular test case you will see that uh this test case will pass even though the PDF files are different okay uh the reason being uh the accuracy percentage okay since the accuracy percentage is 80 percent okay so in the results you can see uh in log info that it will say that the success condition was met and that is why this test case passed so each page of the Target and the Baseline document is at least a 80 percent match okay and we have not uh we have no Pages excluded from the comparison okay now uh to just to change it if I provide a hundred percent accuracy okay you want your comparison to be 100 accurate for both the PDFs and that's a fair uh Fair way of doing it right so just run and this time it should fail okay

[06:11] because both the PDFs are not 100 same okay and uh in the compare results in log info you will see that it will show you the differences okay so at least one difference was detected and in the top left area top right mid left mid right and bottom right area okay obviously it will not uh exactly tell you what is different in this particular pages but it's basically uh used for quick comparison of two PDF documents if you want to verify uh certain elements on the PDF then you need to use our you need to create your own test case and then you need to use the PDF scan okay we will see that in some of the coming up session but using the PDF scan then you can scan particular elements and you can verify whether they are same on the PDF or not but this module is meant for a quick comparison uh with a certain accuracy

[07:13] and you can also exclude pages so quite a useful module if you just want to compare to PDFs okay so that's that's all about uh how you can compare to PDF files using this one is to one compare the Box module in the next session uh we'll talk about the PDF scan how you can scan different elements in the PDF and how you can verify the values
