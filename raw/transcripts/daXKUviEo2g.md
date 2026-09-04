---
id: "daXKUviEo2g"
title: "Tosca Tutorial | Lesson 113 - Autocomplete TextBox | ResultCount | InnerText | Obstacle 7 |"
url: "https://www.youtube.com/watch?v=daXKUviEo2g"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 114
duration: 433
upload_date: "20231201"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:07:36Z"
status: "raw"
---

# Tosca Tutorial | Lesson 113 - Autocomplete TextBox | ResultCount | InnerText | Obstacle 7 |

[00:12] hey everyone welcome back to our Channel I am back with another interesting topic in the tosa automation playlist now continuing with our obstacles topic let's look at our next obstacle which is called and Counting so in this we have got a autocomplete text box so when we type this particular text which is DDD here right you can see that uh it contains a list of different text right so as you uh keep typing it will search and find out all the similar uh text uh in this particular list right so uh we need to count the entries in this list and then we need to enter the number of that particular entries uh in this particular text box right so for DDD you can see there are five entries so we need to enter here five and when you enter five uh this automation obstacle

[01:14] will be completed so that's what we need to automate using tosa Okay so let's go ahead and do this in tosa now now to make this a little bit easier I have already uh scanned this particular module okay so let's go through what are the different elements which are present here so this is the span element okay uh and it represents this particular text which we have to enter okay so it is a span element and we will use the inner text to basically grab this text right and then we have got uh this text box we have got this text box and then we have also got a list here right so that's uh the elements we have scanned uh you can see this is the autocomplete text box then this is the list okay so you can see the list uh item here and this is the underlying list and then uh we have got the text

[02:14] box which is the entry count right now if I go ahead and look at the properties uh one of the things which you need to take care is the title uh that may be dynamic so always try to use regular expressions in your title okay and then uh coming to the list item now uh we have already seen and talked about cardinality so since uh these you can see there are lots of different items here right and uh we are not going to scan each and every item in this list right so uh we can scan just one element type and then we can use the cardinality 0 to n right so we have increased the cardinality here because we want to count all the elements in that particular list right so uh yeah so that's that's all you need to do in the in your module attributes and then let's go ahead and create a new test case here

[03:15] now okay so I'm going to rename this to uh this particular obstacle number okay and then then uh I'm going to drag this module right here okay now uh this span as I said we will be taking the inner text value which is contains the actual text right for that uh we will choose your inner text and here we will see or give uh text as the value and what we'll do we'll change the action mode to buffer so what it will do it will uh grab the inner text and then it will store it in this text value okay and then uh coming to this autoc complete so here we need to uh type the text right and although you can directly enter the text uh that won't work out because uh it's a autocomplete text box

[04:16] so in this case you can use the send keys right so what it will do it will send one key from the keyboard into that particular text box right so uh here uh we have to use the buffer which we have stored earlier so we'll we use a buffer of text here okay and this will be our input right now uh coming to the list item here what we'll do is we'll use another property of a list through which we can count the number of items and that is called the result count okay so here we can type the result count property and here we can again buffer this to a particular buffer value okay I will change the action mode to buffer so the result count of this particular list will be stored in this count right and once we get the count then we

[05:16] can directly enter it uh with the buffer so buffer of count right so couple of things uh we have seen uh we have to use the send Keys instead of uh directly inputting the text here because uh it's a autocomplete text box so we have to enter Keys one by one right then we are buffering uh the inner text uh from the span element which becomes our text and then we are using the result count property for the list uh items so that we can uh get the count of all the items right and then we are storing it in a buffer and then we are entering that uh account value into the text box right so let's go ahead and execute this now so as you can see it uh entered the text which is CCC and then um it counted how many uh C CC are present in that

[06:19] particular list and then it entered two which is the number of uh text which is present in the count here right and then this particular op CLE was completed so this is how you can use different concepts to basically solve uh your automation problem right so you can use the action mode buffer you can use some properties like the inner text the result count uh to get the count of uh the list of items and then you can also use the send keys to enter some keys into a autocomplete text box that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
