---
id: "Zk3-J0TxUEc"
title: "Tosca Tutorial | Lesson 38 -  Generate, calculate and format date and time values | Date Expressions"
url: "https://www.youtube.com/watch?v=Zk3-J0TxUEc"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 671
upload_date: "20230815"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:45:22Z"
status: "raw"
---

# Tosca Tutorial | Lesson 38 -  Generate, calculate and format date and time values | Date Expressions

[00:05] Hey everyone, welcome back to this Tosca Automation playlist and today we are going to talk about how you can handle different date expressions in Tosca. Now in your application, you can come across different scenarios where you may need to enter some date, maybe it is the current date or maybe you need to do some calculations based on some months or days you have to add them or you have to remove them, right? So there are several types of date related scenarios which comes up whenever we try to automate some application.

[00:41] So generally in other automation tools you need to write something either on Java or .NET to get these dates which may be a customized date or maybe the current system date or something like that. And in Tosca already the TBox modules are present and the date expressions are also present through which you can easily get the system date or any other date format which you want and you want to enter them into your application.

[01:15] So you can use these expressions to basically format your dates and use it according to your application. So let's see at some of the examples. So I have prepared this test case which basically gets all the different types of dates and also days and times and all the other things, right? So I have completely used the expressions the date expressions which are available in Tosca.

[01:45] So for this I just used a TBox set buffer module and then for now I am just setting the buffer to all of these different dates, okay, date types. So let's go through each of them. Keep in mind that there are more expressions. I have just used some of them but you can go ahead and explore all the different types of expressions and see which one fits your requirements, okay? Also to write these expressions well it's very simple.

[02:16] You just type the curly brace and then you will see a list of different expressions are available and out of that some of them are related to the date types, okay? So for this I have used something like the date, okay? And in the description you can see it returns the full current date, okay? And the date and time values can be calculated also using the base date along with deviations and this we will see in a later example, okay?

[02:47] So this will basically return me the current full date, okay? And then if you want to have the timestamp then you can use the date time expression. If you just want the time then you can use the time expression. Similarly if you want the current day or current month or current year, okay? Then you can use these respective expressions which is day, month and year. Now sometimes it happens that you would require the first day of the month or the last day of the month.

[03:19] For that also there is an expression called month first and month last. And then there are some specific date requirements which you need to fulfill like the system date, okay? So this will return the full date based on your system specification. So like the date is defined in your system, the date format, it will display the same date here, okay? Then if you want the days, the month or year in a specific format like in a two digits format, right?

[03:55] So even if there is just one digit in the day then it is going to add a zero, okay? It will prefix a zero into that to make it two digits. So if you want all these day, month and year in two digits you can use these expressions which is end day, end month and end year. Similarly if you want the letters only for the day or the month, okay? So you can use these expressions a day and a month, okay? So this will return you some days like mon or month like mar for March, right?

[04:35] Now coming to the calculations, okay? So if you want to have a date which is based on some calculations, okay? So you can use the same expression date but along with that you can also do some deviations, right? So if I want to add two months to my current date or I want to subtract one day from my current date, okay? So you can pass the format on which you want to get this output.

[05:07] So if you want in this format yyymmdd then you have to write it in this particular date expression, okay? So it allows you to do deviations from the current date and also it allows you to change the format, okay? So your expression will look like this. It will start with date and then I have passed the full date which is a buffer value, right? So which I am capturing in the first buffer value full date. So that's my date, okay?

[05:39] And then this is my deviation. So I have added two months and I have subtracted one day from this full date, okay? And then I am returning the final date in this particular format which is yyymmdd. So this kind of deviations you can do easily which can fit your requirements for your application, okay? So let's go ahead and run this and see what are the output values for all of these different date expressions, okay?

[06:13] So now if I go in the scratch book and in the log info, I should have received all the output values, right? So you can see the first one full date. So this is the date or current date, right, 14-8-2023. Then we have got the current timestamp. So it comes with the date and the time, right? So this is like a timestamp which you can use. This is the current time. This is the current day, okay? So 14 is the day today.

[06:45] And then this is the current month, current year, all is in the numeric format, okay? And this is the first day of the month, okay? So it took the current date and then it set the current date to the first day of the month, okay? Similarly it also set the last day of the month and then this is the system date. So it's in a specific format as you can see. This is the two-digit format which I told you about.

[07:19] So everything is in two-digit. You can see, although the month 8 is just one digit, okay? So this is the current month. You can get it in two digits using this particular format, okay, or this expression. Similarly as I said, if you want the particular output in three letters like the day or the month, you can use this particular expression and then the calculated date, right? So our current date is, you can see, 14A2023.

[07:53] It's in a specific format which we have defined plus it has added two months, okay? So the month is now 10 and also it has subtracted one day from 14, it went to 13, right? So this is the calculated date which we got from the expression. So you can see you can get any type of date or any type of format right from the expressions, okay? And you can also do some deviations in terms of changing the date based on some particular calculations.

[08:31] Now let's look at a real-time application with a very small example of how we can use this date expressions to automate some scenarios in the application. So I have opened this obstacle where you have got a field, a text field where you need to enter the tomorrow's date and it should be in this particular format which is DDMM and bye bye bye, right? So it's a very simple dynamic date expression which you need to fill using the expressions in Tosca and fill in to this particular text field, right?

[09:06] So let's create another test case here and let's see get tomorrow's date. I've already scanned this module so I'm going to place it here, okay? And you can see there is this date field, okay, where we need to provide the value. So for this what we are going to do is we are going to use this particular expression which is the date expression.

[09:36] So if you're not entering any particular date then you need to enter the square brackets which is empty and also if you're not entering any particular format then you have to keep the square brackets and in the middle I need tomorrow's date so I'm doing a plus one D, okay? So which will basically give me the tomorrow's date, okay? So this is what you need to use in the expression for your date value and let's go ahead and run this now, okay?

[10:08] So it should be entering tomorrow's date in that particular text field, okay? As you can see the test case passed so it was able to enter the tomorrow's date, okay? And since the default format was DDMM bye bye bye so we didn't have to change the format. So this was a very simple example of where you can find these kind of fields, date fields where you need to either enter today's date or in some specific format or you need to do some deviations, right?

[10:46] So that's all for this particular video. I hope you enjoyed it and you learned something new today. If you want to watch more videos then please subscribe to our channel. Also if you have any questions then please leave them in the comments. So until we meet again, thank you and see you next time.
