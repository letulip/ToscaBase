---
id: "epE3kZJjoP0"
title: "Tosca Tutorial | Lesson 72 - Generate Reports and Create Report Definitions | Reporting |"
url: "https://www.youtube.com/watch?v=epE3kZJjoP0"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 696
upload_date: "20230916"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:40:58Z"
status: "raw"
---

# Tosca Tutorial | Lesson 72 - Generate Reports and Create Report Definitions | Reporting |

[00:06] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation. In this session, I am going to take you through some of the reporting options which are available with Tosca. Now we have already seen in some of the other videos that we can directly using the print view option, we can directly capture or we can directly create a report for our specific section or folder as it is.

[00:36] So if I have got this execution and if I want to look at this login user execution with all the objects expanded here. So if I click on print view and then I can directly print it as a page. But apart from that, there are other options. You can generate a report in any of these formats. So for example, if I want to generate it in the PDF format or the Word, Excel format or the HTML format.

[01:08] So I need to select that format and then click on start. And then Tosca will generate a HTML file and then it will be displayed or opened in the browser. So it's exactly the same snapshot of whatever you have opened on your Tosca screen. So it's not the most effective report, but at least you have got a report in just a few seconds by just going to the print view option. But apart from that, you have also got the reporting section, so where you can generate some reports.

[01:44] Now if you're not able to see this reporting section, then you can always go to the section and click on reporting and it will open this section called reporting. Now in the reporting section, there are some default reports which you can generate and they are listed here. So there is execution list. And here you can see you can generate execution entries with actual log, execution entries with actual login issues, with detailed logs, similarly for requirements and for test cases.

[02:19] So these are some of the default report definitions and data definitions which have been already provided by Tosca. So you can always use this to generate your own report. So say for example, let's take this particular scenario, the end-to-end scenario, which we looked earlier, right? So we have built this business test case with our execution list linked to it, right? And then if you want to kind of generate a report out of it.

[02:51] So what we can do is we can generate it from the demo web shop. Or any particular folder right from here also we can generate. So right click on any particular execution list folder and go to print report. And you will see all those default report definitions which are present here for the execution entries. So if you do it for test cases, it will be for test case. For requirements, it will be the requirements. So these are the four types of report definitions which have been provided already.

[03:26] And I can choose any of these. So for example, if I choose execution entries with actual log or execution entries with detailed logs. So if I choose this, it will basically generate a report. It will again take you to this print option screen. But the report will be a little bit different because it is based on a report definition rather than just printing out whatever is present on this page. So if I click on start now, again, it will export a document.

[04:01] And then it will ask you for some options like do you want only field test cases to be shown? I said no. Then it is asking do you want screenshots included? I will say yes in between. And then it will generate a proper report. Now you can always change this logo which is displaying currently tricenters, but you can also change this in the report section. And then it will show you an execution test report.

[04:32] It was created on this particular date. And then it will show you a summary with how many test cases failed with a pie chart. And then what was failed. So everything is displayed here. Similarly, you can generate it for any particular document. So I can generate it for the whole execution list as well. So if I go here, print report and then execution entries with detailed logs.

[05:04] And then start again, save. And then OK. And yes. OK. So it will export it into a proper document now. And now you can see a proper view of all the execution lists. OK. So all the test cases like written 19 test cases and 3 passed 14 no result and 2 failed. Sum up pie chart and then the individual execution list of what were the results of these execution lists.

[05:39] Right. So here you can see for a register user, it is showing all the steps as well when it's when it was started, when it ended and who executed it with all the log in for as well. Right. With screenshots whenever there is a failure. So it's a proper report which you can generate right from any particular folder or any particular object for that matter. OK. So this is where you can use the default reporting definitions which are already provided in your workspace.

[06:13] But if you want to also generate your own report definition that also you can do. So right click on the reporting folder and there you will find a create report definition. So click on that and you will see that there is an exclamation mark on the report definition which means that something is not configured properly. Right. So first we need to select a data set definition. OK. And it should be linked to a particular object. So what kind of object you want to link it to.

[06:46] So I can basically select one of the execution list if I wanted to link it to an execution list. If I want to link it to a test case I can select any test case object or requirement or module whatever you want to do. OK. So if I select this and drag it to report definition folder you will see the link. Now it is the object type has been updated to execution list. OK. But still there is an exclamation mark which means we also need to provide a designer definition.

[07:19] Now to assign a designer definition right click here and then in create designer We have got three different options. So the first is default and this allows you to design your report with the report designer. So there is a third party tool through which you can design your own report basically change the text or change the header headers or footers and logo. So all those things you can do with the report designer.

[07:52] So that will only be possible if you choose this default option that is also XML report. So this will create an XML document containing all generated information and then the Excel report will create a worksheet in Microsoft Excel with all the information for every data definition. So if you select default now you will see the exclamation mark is gone. So this is a proper report definition. This is pretty similar to what you see which are currently present here.

[08:23] So these are built for execution entries with actual log. Now keep in mind that you need to also provide more specially objects. So here this is just the object type which has been set. After this you need to create another data set definition and there you need to provide a proper TQL query which can identify or which can search that object on the bug space or else you can select this link and then the object type here so that it is able to search that particular data set.

[09:05] So for example like this end to end scenario which is a business execution list. So if I say end to end scenario and then execution list. So here we can now define our own query. So for that you also need to choose the TQL query column chooser in the column chooser.

[09:35] So here you can define your own TQL query or else you can use this link and object type and constraint to basically build that. So choice is yours for example if I go here in subparts and then object type. Okay so I choose object type as execution list and then in constraint I need to put a constraint something like name equals equals and then I will provide end to end scenario in this.

[10:15] So that will build a constraint and this will basically act as a TQL query. You can see that TQL query is built as you keep on selecting the required object type constraint and link. So this way you can build your report definition your own report definition and then you can print the report based on this report definition rather than using some of the default ones. But if you quickly want to generate a report like I showed you you can use this default report definitions which are good enough for execution lists or for requirements or test cases.

[10:57] But if you want something of your own customized report then you can build your own report definition. Okay so this was a quick overview about the reporting section. You can quickly generate reports using the default report definitions and you can also generate your or create your own report definitions. That's all for this particular video. If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel.

[11:31] Thanks for watching and I will see you in the next video.
