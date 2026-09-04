---
id: "glZeQF7BWNo"
title: "TRICENTIS Tosca 16.0 - Lesson 22 | Dynamic Comparison | XBuffer Syntax {XB}"
url: "https://www.youtube.com/watch?v=glZeQF7BWNo"
channel: "Ravikanth FicusRoot - Tech Videos"
playlist: null
playlist_index: null
duration: 591
upload_date: "20230327"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T14:37:48Z"
status: "raw"
---

# TRICENTIS Tosca 16.0 - Lesson 22 | Dynamic Comparison | XBuffer Syntax {XB}

[00:01] foreign Advanced Training so this is our lesson 22 in terms of overall try sentence Tasker training R it's a lesson 7 in terms of Advanced Training so I would recommend you guys to please visit my previous videos before you watch this session to understand the concepts very well so in this lesson I'm going to teach you how can you use a dynamic comparison or how can you perform Dynamic comparison while automating your test cases are while validating your test cases by using tricentish task automation so Dynamic for dynamic comparison we use x buffer so you're gonna learn X buffer

[01:03] Concept in this particular training session please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you okay so what is dynamic comparison so in this lesson you I'm gonna teach you how can you set up and then how to use Dynamic comparison and the dynamic comparison is a feature within Tosca that allows you to verify a portion of the string that is static so basically you can verify static portion of the string and you can buffer another portion of the string which is dynamic okay so let's assume once you order your product in any e-commerce site right it says your order has been successfully placed and it gives you the order number

[02:04] so in this case the order number is a dynamic and your order has been successfully placed that is a static text so now how can you validate this entire string part of string is dynamic and part of string is static so that is where this Dynamic comparison comes into picture okay so this is also represented as X buffer which is Curly braces XB in Tosca so basically this helps you to verify the string with Dynamic elements and as well as simultaneously you can buffer the element within the string which is a dynamic and you can utilize them later in your test validations okay so let's jump onto the system and see how can we perform this Dynamic comparison by using X buffer concept by

[03:05] using latest version try sentence task 16. so this is my task 16 okay where we are going to start working on Dynamic comparison so if you see I already explained you one end to end scenario where we go to if you see this is my demo web shop that is where we are working from past 21 sessions okay you log I mean you basically logged into demo webshop go to operation shoes so I'm gonna teach you I mean I'm gonna tell you what scenario we are automating here okay and go to Blue Jeans and add to cart quantity one okay and then go to shopping cart and here agree the terms check out and here billing address shipping address so this is all already I explained you okay guys okay so here once you complete your entire order once you confirm the order

[04:07] you will get an order number okay so if you see here this text order number 140912 correct so here order number is a static and 1401912 is dynamic text okay so that means now I want to verify this text how can I verify this text so that is where Dynamic comparison comes into picture so let's go here so I already automated that entire scenario logging in and then check out and verify so here if you see there is one module test case step called verify the order success where I am verifying the successful order your order has been successfully processed and here the order number okay what I'm gonna do here I'm gonna verify this also select verify

[05:11] and here inner text this is my object control related to this one okay here I'm gonna select inner text and my inner text is equal to my inner text is equal to what here copy this okay copy this and paste here sorry this one inner text equal to here this is my Dynamic part right that one I'm gonna specify as X buffer exclude the verification and buffer this particular text this particular part of the string and what I'm doing I am specifying verify this entire text from here to here and while verifying exclude this part and then store this in a buffer value okay so for that that's the reason I'm going to specify x b x buffer here I'm

[06:14] gonna tell this as order number what I'm doing this particular string after order number whatever exists exclude that in the verification and store it into buffer called order number that's it so now if you see I am verifying this entire State text entire string but I'm excluding the part of string and storing that particular order number into order number buffer okay so now we are done so basically before you make any changes it's recommended to resolve the references because this actually we created by using Library so Library functions and all these things I already explained you guys okay so now here I want to run this particular test case as it is okay let me first log out here

[07:22] okay now right click and run in scratchbook which opens your webshop and it logs into webshop so logging in providing the credentials and then go to appearance and choose and it orders the genes is going to add that into card see it's adding into the cut done 25 amount go to shopping cart agree terms so basically it is applying the coupon agree terms check out click on continue continue and then it is actually shipping method it's selecting payment method right and it's selecting the credit card and then it's click on confirm so once you click on confirm it's going to verify the success message and it's going to verify this also right and then it's going to log out okay it's done logged out so if you see here successfully completed so if I go to test results if I go to test results let's go to test results now if you see

[08:25] here under shopping cart procedure here verify order success if you see here it says this order number verification is successful and the order number is placed here okay so let me see the buffer how does it buffer stored okay let's go to tools and click on Buffer overview and if you see here order number see buffer called order number is stored with actual order number so you have to go to tools click on Buffer viewer see this is where I see the order number whatever the buffer I specified I can see here see this is the order number XB so that order number has been placed correct so now I can use this order number to verify the order number right so hope you all understand the concept of dynamic comparison how can you

[09:28] validate a message which is a dynamic some portion of the message is static and some portion of the message is dynamic okay so if you have any queries leave your comments in the comment box I'll try to respond to your queries please do subscribe to the channel click on Bell icon you'll receive notifications whenever I publish more videos thank you
