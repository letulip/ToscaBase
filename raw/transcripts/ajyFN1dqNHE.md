---
id: "ajyFN1dqNHE"
title: "Tosca Tutorial | Lesson 148 - Common Issues | Remove Special Characters | String Replace | Escape |"
url: "https://www.youtube.com/watch?v=ajyFN1dqNHE"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 662
upload_date: "20240417"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T12:54:21Z"
status: "raw"
---

# Tosca Tutorial | Lesson 148 - Common Issues | Remove Special Characters | String Replace | Escape |

[00:09] Hey everyone, welcome back to our channel. I am back with another interesting topic in the Tosca Automation playlist. So let's look into another common issue which you might encounter while working with Tosca and especially around a string manipulation. So let's pick up a scenario. This is the Swaglabs demo website where I have added two products into the cart. And these are two products which have got different prices.

[00:40] Now the scenario here is I want to calculate the total price for these two products which are added into the cart. So I want to verify that the total price is as per the expected results. And for that I need to add these two values which are in dollars and also there are some decimal points here. So how can we do that? What is the problem here? Let's look at this.

[01:13] So for this, first we will go ahead and we will scan these two elements from the application. For now we are not able to see any elements with those price. So we are going to increase the filtered items here until we see those price elements and these are the two price elements here. And for now these are both unique so we don't need to add any additional properties or we don't need to change the identification mechanism.

[01:48] So we are just going to add this module now. I'm going to call this cart and then save it. And let's close this. So we have got our module now. So let's go to our test case folder here called string and then here we will create a new test case. We will call this calculate total price.

[02:18] And then we are going to add our module here which is the cart. Now the first step is to store these values into the buffer which is the price of these items. We could also change the module attributes here so that we don't actually see the price here but we will rename it to item 1 and item 2.

[02:50] Now if I go back to my test steps I can see item 1 and item 2. Here we have to use some property which is the inner text and we will store it into a buffer. So we will call this price 1 and we will change the action mode to buffer here. So we will give the inner text and then price 2. And then we will change it to buffer.

[03:22] So now we have buffered both the prices. Now we need to calculate the total which is we need to sum these two different price items. Now if I go ahead and use another test step here called set buffer and we are going to name this buffer as the sum. And here we need to calculate the sum here so we can use an expression called calc which basically can calculate any particular mathematical operation.

[04:02] Inside this we will use the buffers. So we have got two buffers here price 1 and price 2. So this is the calculation expression where we can add two different prices here.

[04:34] So until this it looks fine but will it give the expected result. So let's see that. First let's go ahead and execute this before that I will just rename this to add prices. Okay and then let's go ahead and run this. So now if I look at the scratch book here you can see in the first step it passed so it was able to capture the price and store it into a buffer you can see this was the first price and this was the second price.

[05:19] But when we try to add these two prices you will see that it will throw an error for the expression. So it will say that it is not a valid expression which can be used in this particular calc expression. So this doesn't work. So we cannot directly add these two prices which contains a dollar sign. Now what can we do here. So let's make some changes.

[05:50] So let's go ahead and remove this step and here let's make some changes to the price one and price two buffer which has got that particular price value with the dollar. So here first we need to remove that dollar from those price items. And how we can do that is by using the string replace method. So in this string replace first of all I need to pass the text which we want to replace so that is our buffer.

[06:26] So I'm going to use that be price one here and then we need to pass the expression. So what do we need to replace and that is the dollar sign here. So we will mention the dollar here and then what we want to do with this. So either we can put a zero before the price or we can just leave it empty. So we'll replace it with a white space. So this is the expression.

[06:58] So this is the text which we want to replace then what we want to replace and then with what we want to replace. So these are the three things which we need to mention here. And then I'm going to close this. But there is still a problem here. You think this will work. So how we can check that is we can right click on this expression and we can do a translate value. And you will see that it was not able to replace that dollar sign.

[07:30] It was not able to remove that dollar sign. OK. Now whenever you are using some kind of special characters you always need to escape these characters otherwise it will not work in Tosca. So what we need to do here is we need to replace the special character by adding a backslash. OK. Let's put it inside the double quotes and then let's add a backslash here and then the dollar sign.

[08:01] So what this will do is it will escape this particular character. OK. Now if I go ahead and translate the value again this time around you will see that it has removed or replaced that dollar with a white space. So that's no more there in this particular value. OK. So this way we can do a replace using the string replace expression and the same we can do for the price too.

[08:33] So I will just use this expression here and I will replace it with price too. That should give me the new price if I just check this again. So this is the OK. Now what we can do is now we can calculate the total here and we can use the same expression which we used earlier which is calc which is the calc function. And inside this we are going to use the buffer which has got now the new values right.

[09:07] So we are going to use the price one and then plus the price two. OK. So now let's go ahead and try this again and let's see if we can get that total price. So let's try and run this. OK.

[09:38] So you can see the execution has passed this time. And if we go ahead and look at the logs. So the price was set and then it calculated the total price which was 39.98. Right. Now if you have got this total price somewhere on the application or in your requirements you can put verify action mode and verify this total price as well. Right. So this way you can use the buffer action mode to buffer different values from your application and then you can use the different string methods like the string replace to replace some of the special characters or some characters which you want to remove from the values before you perform some calculations and also do some verifications on them.

[10:30] Right. So this is very helpful and it's a very common scenario you can come across not only for calculating the total price in a shopping cart but it could be a scenario in several other situations related to your web applications. That's all for this particular video. If you have any questions then please leave it in the comments. If you like this video then please subscribe to our channel. Thanks for watching and I will see you in the next video.
