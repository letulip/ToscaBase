---
id: "hBRAnB_3iBc"
title: "Tosca Tutorial | Lesson 35 - Multilingual Testing | Multiple Languages | Regular Expressions |"
url: "https://www.youtube.com/watch?v=hBRAnB_3iBc"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 580
upload_date: "20231014"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:49:30Z"
status: "raw"
---

# Tosca Tutorial | Lesson 35 - Multilingual Testing | Multiple Languages | Regular Expressions |

[00:05] Hey, everyone. Welcome back to another lesson in this Tosca automation playlist. Today, I'm going to tell you how you can do multilingual testing using Tosca. Now what does it mean? So if your application or your website has got multiple languages, so this particular website is from Nikon and it is a Canadian website, but it has got two languages. As you can see, this is the English language. And then there is also an option for French, right?

[00:37] So if I click on the French link, then it converts everything on this page to the French language. Now, this is a very common scenario which you come across web applications when there are multiple languages supported by that web application. Then you need to test with every language. Now how you can do this easily with Tosca? So let's get started. I'm going back to English. Now what I have done in Tosca is I have already added a module for this page.

[01:12] And what we want to do is just want to click on this camera's link. So I have added the module for the English page you can see here. And then I have identified this particular link, which is cameras, and then we are going to click on it. So this is all fine. But what if then we need to test it in the French language, right? So if we change this page to French, then this particular text is going to change. Now it will work if there is unique properties like ID, which is unique even if the language changes, then you can still work with that particular ID.

[01:56] But this particular link, it has not got any particular ID. As you can see in the properties, it is identified by the inner text and the tag. These are the two properties with which it is using. So if we change the language to French, then the inner text is going to change. And then our test case is going to fail. Now one way is obviously you can create multiple modules for multiple languages, but that's not an efficient way of doing it, right?

[02:30] So let's see how we can resolve this particular problem. So first of all, let's go ahead and create a test case under this multilingual test case folder, okay? So I'm going to say click cameras. So that's what our test case is. And then I'm going to drag this module right here, okay? And then we are going to click on this, right? So this is all fine if I execute this and it's going to click on the cameras link.

[03:05] But since I already changed the language to French, now this will not work. So let's see, first let it fail and then we'll see how we can fix this particular problem. Okay, so there are two problems right now. First of all, Tosca is not able to find that particular link. But before that, before going to the link, the title of the page has also changed. So currently, the title which Tosca is trying to find was in English.

[03:36] But right now, the title has changed to French, right? And how you can see that you can even go to inspect in Chrome, and then you can search for title, okay? So this is the title which is currently there for this particular page. So you need to fix two things. One is the title and one is the link itself, okay? So let's see how we can do this. So this can be resolved by using regular expression in your module attributes, okay?

[04:10] So the two things which we need to change is the title of this particular module. Okay, so here you can see it is in English. So what we can do is we can use regular expression where we can use the or condition. Okay, so we can put two titles, okay? So whichever title is present on the page, it will use that and it will identify the element. And the same we can do for the link control as well. Okay, so we can put two different texts, which can be in different languages.

[04:43] Now this you can replicate for multiple languages, not only two, but any number of languages which you want to support, right? So for every control, you need to use the regular expression where you need to verify that particular control in multiple languages. So let's do this, okay? I am going to first of all cut this, and this will basically start with an expression called regex, okay? Because we are going to write a regular expression, so you need to write a regex, which is the expression starting with curly brace, and then we'll put a square bracket.

[05:23] And then inside this, we are going to write our multiple text in different languages, okay? So we are going to start off with the English language, and I'm going to reduce this text, okay? I'm going to cut it, and then I'm going to put a star, which means any character after this text will be recognized, okay, no matter what it is. But the cameras from Nikon will remain constant, okay? Then we need to put the or sign, which is this particular state bar.

[05:58] And after this, you can put the text which you want to identify in French, okay? And that I have already shown you. So using this title, we can find out this. So I'm going to use the initial part of the text, which is this, okay? And then come back here, and then we are going to put it here. Again, we are going to use the star so that the remaining text can be used as regular expression. Then we are going to do double quotes, and then close the square bracket, and then close the curly braces, okay?

[06:37] So that will identify the title. Now coming to the cameras link, right? So we need to change the inner text. We need to use regular expression here. So the first text is in English, and then we need to put or condition, and then put it in French, okay? So the same case like we did for title. Again, I will take it out, and I will start with regex, okay? And then square brackets, double quotes, then put it across, or the or condition.

[07:10] And then we need to write this particular inner text in French, okay? So this is the inner text, as you can see. So I'm going to write this particular text, which is displayed here. So it will be April, and then photo, okay? And then I will also use the star, so that if that particular text changes, then also it should work, okay?

[07:42] So let me just verify, so it's April, and then photo, okay? And then we'll put double quotes, and the square bracket, and the curly brace, okay? So this is the inner text using which this control would be identified, both for English as well as French language. Now coming back to our test case, so now it can be executed. So let's see whether it works for both the languages, okay?

[08:13] So we'll start off with the French language. So let's run this. So as you can see, it clicked on the cameras link, and then it came to this particular page. So both the title and the link worked in French language, even if we had written two different texts there, right? There was the regex, which helped us to identify this control in this particular language. Now let's change back to English, and let's see if this still works, okay?

[08:47] So I'm going to the home page, and now I'm going to run this again, okay? So let's go ahead and run this in Scratchbook again. And this time as well, it should click on the cameras link, okay? So it clicked on the cameras link. And this is how you can extend your automation testing for multiple languages which are supported by your web application. So this is known as the multilingual testing, and it is supported by most of the test automation tools, and the same can be done in Tosca as well.

[09:26] That's all for this particular video. If you have any questions, then please leave it in the comments. If you like this video, then please subscribe to our channel. Thanks for watching, and I will see you in the next video.
