---
id: "zgqUoo_1tpM"
title: "Tosca Tutorial | Lesson 8 - Identify Controls By Index | Duplicate Controls |"
url: "https://www.youtube.com/watch?v=zgqUoo_1tpM"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 10
duration: 393
upload_date: "20221213"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T07:58:42Z"
status: "raw"
---

# Tosca Tutorial | Lesson 8 - Identify Controls By Index | Duplicate Controls |

[00:09] hey everyone welcome to another interesting lesson in this TOS automation course today we are going to talk about the last identification mechanism through which you can identify different controls on your web application so in tosa we have seen how we can identify controls by Properties by anchor control by image and the last option which is there is called the identification by index so we are going to talk about it uh it is also a useful mechanism when you are trying to or you are not able to identify controls uniquely using properties or a anchor control or even an image index could sometimes work out uh better for you so let's see uh we are going to use the same scenario uh since we were using it for all the other identification mechanisms uh we want to enter some text into the Google search and we want to click on this button which is not unique on this application

[01:10] right so we are going to uh use the index in order to identify this control and uh perform the operation which is the click so let's go to tosa and here again um I'm in my module section and I'm going to scan my application so that uh we can add the module using all the controls which we want uh for this particular module so uh again select the application which is Google Chrome application and click on scan so once we are on the advanced view um we are going to select our controls which is the text box and um the Google search button which is not unique um obviously uh and we are going to use a different mechanism for this Google search button right so go to the identify uh by option and here again um you will see the last option which is

[02:11] called index so select that and that will open up a new window on the right side which is called identify by index so as you can see here uh it is showing you a warning kind of sign uh and it is telling to use the index if you cannot choose the identification CR IIA to uniquely identify the control and the reason it is saying is uh it is not a good idea to always use index as identification mechanism it is not always fullprof because um you are not sure which index uh the particular control is because there are similar controls on the screen and it might happen that it may use uh different index than what you intend to use for a particular control right so that's the reason it shows you that um it is not a stable option but still if you want to use it you can right um and tosa automatically

[03:12] identifies which Index this particular control is on the screen or on the application so um you just need to select that particular index if you want to use it and as soon as you select it you will see uh the message will change that the selected item is unique so tosa is able to uniquely identify the control using the properties and the index right uh so this control uses a constraint index for identification right so uh that's how the two mechanisms are displayed here for Google search that's what we are using to uniquely identify it and we are going to save this module right so close it and that should build your module with the two controls which are uniquely identified and again the same procedure so this time uh we are going to use the index option so I'm going to change this

[04:15] name just to make it more clear right uh and add a particular test case here so Google search and then just add the module here to get it working and let's enter the values here which is the test step values uh again the same values which we have been using for all the other scenarios right and let's go ahead and run this now just to test whether this option is working as expected or not so as you can see it is able to perform uh the required operation and it has generated the required output right uh you will see the same thing on the scratchbook after um it has executed right so it will show the T step has

[05:17] passed so uh this was another option uh which is good or is a good option to use when you are not able to identify it using the other mechanisms but you should follow the hierarchy which is present in tosa right so in the identify by option you will see there is a particular hierarchy the first option is identify by properties then it goes to Anchor then it goes to image and the last option is Index right so generally uh you should follow this but depending on the application depending on your scenario you can always uh choose any of the options right um but uh choose your options wisely when you are trying to identify your controls because uh your whole automation execution could depend on that particular mechanisms which you are choosing while building your automation pack so this was all about uh how you can identify controls by index um hope

[06:20] this was useful uh we soon come up with more interesting Tsar lessons in the coming up weeks so keep watching and do subscribe be to our Channel and we'll see you in the next session
