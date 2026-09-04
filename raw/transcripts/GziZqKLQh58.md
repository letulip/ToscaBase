---
id: "GziZqKLQh58"
title: "Tosca Tutorial | Lesson 39 - Use String Operations | Find length | Convert To Uppercase | Occurences"
url: "https://www.youtube.com/watch?v=GziZqKLQh58"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 41
duration: 511
upload_date: "20230817"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:01:20Z"
status: "raw"
---

# Tosca Tutorial | Lesson 39 - Use String Operations | Find length | Convert To Uppercase | Occurences

[00:07] hey everyone welcome back to this task automation playlist and we are going to continue talking about different string operations which are present in Tosca now we have spoken about some of the operations uh where we did a string replace we use the trim function to basically remove all the white space characters and we use the string replace to basically replace some part of the string with some other uh pattern or string right we have also seen how we can use the base64 string operation to encode and decode our strings and now we are going to talk about the remaining four string operations and these are the string to lower string to Upper number of occurrences and string length now by the name you can think what a string length will do it will basically provide you the length of the string right so it will count the number of characters and it will return you the length the number of occurrences this is a

[01:08] useful uh operation where you want to count all the occurrences of a defined input or pattern within a particular string okay then string to Upper it converts the lowercase characters to upper case and string to lower it converts the upper case to lower case now this might seem very similar to you if you have worked on any programming language like Java you can perform all of these operations uh directly in Java right but here uh Tosca has already given you uh different Expressions which through which you can perform just string operations this could be useful uh especially uh when you're working in Automation and you have to maybe format or change particular strings then you can use these different operations to carry out those uh particular automation okay so let's quickly see how you can do this okay so we will

[02:10] remaining a string operations we will do it here so string operations okay for this I am going to use first a t-box set buffer and here I'm going to create a buffer called Str and this will contain something like placentis.com okay now what we can do is uh we can now have another buffer okay where um we will return the length of the string so here I'm going to use the buffer of Str UCT actually we need to first use the string operation so we will use string length and inside that we will use the

[03:12] buffer okay okay so I will close this okay so this will return me the string length Okay and we'll store it in a buffer called length now if I want my string uh to be converted into upper case so let's create a buffer here called uppercase and here again the same way first we will do the string operation so type string to Upper inside this we will then use the buffer so we will use the buffer Str ose the brackets okay and again for lowercase is the same so lowercase I am going to just copy

[04:16] this just to make it little faster so I'm going to make it string to lower and then the final one which is number of occurrences right so I'm going to name it number and this time around we will be using um not string but number of occurrences you can see here inside this now we will give uh the actual string so which is B of Str buffer and then close this okay also we need to pass the string okay for which we want the number of occurrences or the pattern okay so this will be your characters so which characters do you want to uh find the number of occurrences

[05:16] uh let's say I want to find the number of occurrences for um t Okay so that's the character I want to find the number of occurrences for um and then we can close this okay so here um in the pattern okay it can be one character it can be multiple characters if you want to find the complete licenses uh that also you can do okay so it is very useful to find the number of occurrences of any particular pattern or character okay so let's quickly go ahead and run this and see if it is working as expected okay so if I go into the logs now I should be able to see my results so you can see the length is 15 characters uh it has converted into uppercase then it is converted into lowercase and then the buffer is set to one uh

[06:21] which is actually correct now you will ask me um there are multiple T but if you look at it okay so there are uppercase t and there is one lowercase T and that is what it has returned us now if you want all the t's no matter if it is uppercase or lowercase then you need to pass an optional parameter okay so here uh after uh the pattern you also need to pass whether you want uh to ignore the case while finding the number of occurrences so that you can do using this ignore case parameter so this is an optional parameter which I did not give it first time okay but now I am providing it so now the value should be 3 instead of just one okay so let's go ahead and run this and if I check the number is 3 now okay

[07:22] so no matter if it is uppercase or lowercase it is going to find the number of occurrences so this way you can use all of these different operations which are related to string so you can use them at different places of your automation whenever you are trying to extract some value from the application or you are trying to compare some expected versus actual results or you are trying to modify your strengths right so there are lots of operations uh which are required when you are automating a particular application and this could be a very useful although it is very simple you should be able to use them uh within Tosca so that's all about string operations I hope you liked it and you learned something new today if you like our videos then do subscribe to our channel uh we would be coming up with lots more videos so until we speak again keep learning and keep watching our Channel
