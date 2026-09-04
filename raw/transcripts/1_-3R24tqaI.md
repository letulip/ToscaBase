---
id: "1_-3R24tqaI"
title: "Tosca Tutorial | Lesson 40 - Use Base64 String Operations | Encode and Decode text |"
url: "https://www.youtube.com/watch?v=1_-3R24tqaI"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 42
duration: 551
upload_date: "20230816"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:01:24Z"
status: "raw"
---

# Tosca Tutorial | Lesson 40 - Use Base64 String Operations | Encode and Decode text |

[00:07] hey everyone welcome back to the store score automation playlist and today I am going to talk about another interesting topic uh which our feature which is available in Tosca now many a times uh we need to encode or decode some text or some value in our test automation suit right so something like the passwords the usernames or the environment details the DB password or the username right so there are many things which uh you probably need to encode or decode as part of your security concerns around the whole test automation suit or even maybe you need to encode or decode some test data right so in this kind of cases you can use one of the string operations uh which is available in Tosca to encode and decode any particular text so let me show you how you can do this in Tosca so for this purpose I'm going to use

[01:09] this particular page okay and it has got some username and password right and to login we need this username and password and what I'm going to do is I'm going to encode this username and encode this password and then I'm going to decode it okay so first of all what I have done I have stored this a username and password right here okay and it is stored in the configuration parameters for this particular test case so first of all I'm going to create a test step and I'm going to use the t-box set buffer okay so this will set a buffer value for the encoded values okay and I'm going to name this to encode underscore username and in this value we need to now write the expression which can basically encode a particular string which is in

[02:10] our case is a username okay so let me explain you what I have done here so we are using this base 64 expression okay which basically allows us to encode that is also at the end of this expression there is a parameter called encode and what we want to encode so that's our text which is a configuration parameter in terms of the username okay so using this it is going to encode it in the base64 format okay uh what I need to do is just copy this or I can also type it but to just make it more faster I'll just copy it and change it to password okay so this is basically going to encode our username and password so let's quickly run this and see if it is working or not

[03:17] okay so the test has passed and now in the log info you will be able to see the encoded value of this username okay so this is the encoded value it's some random string which has been generated to basically mask the particular username okay so when this data travels over or when it is used for test automation you will be seeing this encoded username and then there is also encoded password so you don't need to actually show your actual password you can use this encoded password right um now in order to use it in a particular test right we need the actual values otherwise if I go ahead and use it in this particular login form it is probably going to fail right so uh for that again I can add the same test step which is t-box set buffer okay and then I'm going to name this

[04:18] buffer as decode user name and I will again have another one for decode password okay and the expression okay so it will be pretty much similar let me show you how you can write this so you write base64 and then you start the square brackets and under this we are not going to use the configuration parameter because we need to pass a string which is already encoded okay so we have to use this particular buffer so we'll use encode underscore username and then we need to pass the parameter decode here so that it will be decoded okay so that's what we have to do again for password we have to do the same

[05:23] and password okay uh so that's that's the thing that you need to do let's run this quickly to check whether it is working or not okay so it failed let's check what's wrong here okay um so instead of the buffer I used a text okay so which is not a encoded text so obviously that will fail so let me correct this uh be unders so we'll start with the buffer which is B and then square brackets and we will use the encode username here okay and then this the same we will do for password

[06:27] okay so let's try one more time this time it should pass okay so this is now going to decode our actual encoded username and password and it's going to return us the same value which we stored in the configuration parameter okay uh maybe I did not change this sorry about that let me change it to password okay so it has decoded the username and password and we have seen how it encodes the username and password now you will ask me uh why do we need to do this right so this is not uh the best possible example I could give you but I wanted to show you how you can encode and decode strings in Tosca this could be useful in some scenarios

[07:28] in real time scenario you would not be encoding and decoding the same strings in the same test probably you should have some encoded text okay which is maybe a buffer or some other value which has been provided to you and then you are going to use that in the test so at that time you can maybe use the decode function right and sometimes maybe um after you uh get some values from the application right maybe you are testing an application and the application has returned you some order ID or some um some customer information right which you need to encode and store it so that time you can use the encode function okay so don't take this example as literally what you need to do you need to apply this functions at different places okay so you need to apply and code where you want to encode a particular string and you need to apply the code when you want to decode a

[08:30] particular string okay so this I find it a very useful function because we need this at some places during test automation so that's all for this particular video I hope you liked it and you learned something new today if you have any questions please leave them in the comment section if you want to watch more similar videos please do subscribe to our Channel and until we meet again keep learning Tosca and keep watching our Channel
