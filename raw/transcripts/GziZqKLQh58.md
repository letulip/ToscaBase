---
id: "GziZqKLQh58"
title: "Tosca Tutorial | Lesson 39 - Use String Operations | Find length | Convert To Uppercase | Occurences"
url: "https://www.youtube.com/watch?v=GziZqKLQh58"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 511
upload_date: "20230817"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:16:57Z"
status: "raw"
---

# Tosca Tutorial | Lesson 39 - Use String Operations | Find length | Convert To Uppercase | Occurences

[00:05] Hey everyone, welcome back to this Tosca Automation Playlist and we are going to continue talking about different string operations which are present in Tosca. Now we have spoken about some of the operations where we did a string replace, we used the trim function to basically remove all the white space characters and we used the string replace to basically replace some part of the string with some other pattern or string, right? We have also seen how we can use the base64 string operation to encode and decode our strings and now we are going to talk about the remaining four string operations and these are the string to lower, string to upper, number of occurrences and string length.

[00:52] Now by the name you can think what a string length will do, it will basically provide you the length of the string, right? So it will count the number of characters and it will return you the length. The number of occurrences, this is a useful operation where you want to count all the occurrences of a defined input or pattern within a particular string, okay? Then string to upper, it converts the lower case characters to upper case and string to lower, it converts the upper case to lower case.

[01:28] Now this might seem very similar to you if you have worked on any programming language like Java, you can perform all of these operations directly in Java, right? But here Tosca has already given you different expressions through which you can perform the string operations. This could be useful especially when you are working in automation and you have to maybe format or change particular strings then you can use these different operations to carry out those particular automation, okay?

[02:03] So let's quickly see how you can do this, okay? So we will, remaining string operations we will do it here, so string operations, okay? For this I am going to use first a tbox set buffer and here I am going to create a buffer called str and this will contain something like trisntis.scar, okay?

[02:39] Now what we can do is we can now have another buffer, okay? Where we will return the length of the string. So here I am going to use the buffer of str. Actually we need to first use the string operation, so we will use string length and inside that we will use the buffer, okay?

[03:23] So I will close this, so this will return me the string length, okay? And we will store it in a buffer called length. Now if I want my string to be converted into uppercase, so let's create a buffer here called uppercase and here again the same way. First we will do the string operation, so type string to upper. Inside this we will then use the buffer, so we will use the buffer str, close the brackets, okay?

[04:07] And again for lowercase is the same. So lowercase I am going to just copy this just to make it a little faster. So I am going to make it string to lower and then the final one which is number of occurrences, right? So I am going to name it number and this time around we will be using not string but number of occurrences.

[04:41] You can see here inside this now we will give the actual string, so which is b of str buffer and then close this, okay? Also we need to pass the string for which we want the number of occurrences or the pattern, okay? So these will be your characters. So which characters do you want to find the number of occurrences?

[05:16] Let's say I want to find the number of occurrences for t, okay? So that's the character I want to find the number of occurrences for and then we can close this, okay? So here in the pattern, okay? It can be one character, it can be multiple characters. If you want to find the complete license, that also you can do, okay? So it is very useful to find the number of occurrences of any particular pattern or character, okay?

[05:51] So let's quickly go ahead and run this and see if it is working as expected, okay? So if I go into the logs now, I should be able to see my results. So you can see the length is 15 characters. It has converted into uppercase, then it has converted into lowercase and then the buffer is set to one, which is actually correct.

[06:23] Now you will ask me there are multiple t, but if you look at it, okay? So there are uppercase t and there is one lowercase t and that is what it has returned us. Now if you want all the t's, no matter if it is uppercase or lowercase, then you need to pass an optional parameter, okay? So here after the pattern, you also need to pass whether you want to ignore the case while finding the number of occurrences so that you can do using this ignore case parameter.

[07:00] So this is an optional parameter, which I did not give it first time, okay? But now I am providing it. So now the value should be three instead of just one, okay? So let's go ahead and run this and if I check the number is three now, okay? So no matter if it is uppercase or lowercase, it is going to find the number of occurrences. So this way you can use all of these different operations which are related to string so you can use them at different places of your automation whenever you are trying to extract some value from the application or you are trying to compare some expected versus actual results or you are trying to modify your strings, right?

[07:48] So there are lots of operations which are required when you are automating a particular application and this could be very useful. Although it is very simple, you should be able to use them within Tosca. So that's all about string operations. I hope you liked it and you learned something new today. If you like our videos, then do subscribe to our channel. We would be coming up with lots more videos. So until we speak again, keep learning and keep watching our channel.
