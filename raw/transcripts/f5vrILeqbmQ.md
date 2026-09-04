---
id: "f5vrILeqbmQ"
title: "Tosca Tutorial | Lesson 84 -  Authorize API requests using Digest Authentication | API Testing |"
url: "https://www.youtube.com/watch?v=f5vrILeqbmQ"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 84
duration: 427
upload_date: "20230425"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:04:40Z"
status: "raw"
---

# Tosca Tutorial | Lesson 84 -  Authorize API requests using Digest Authentication | API Testing |

[00:07] hey everyone welcome back to this Tosca playlist and today we are going to talk about another authentication type which is digest authentication now this authentication mechanism may be used with some API messages or requests and you need to make sure that you are using uh the correct authentication type for your API message before you send them right now in the previous session we already looked at how you can use the basic authentication using a simple username and password so if you have not watched the video URL is on the top so go ahead and watch that before you start watching this particular video which is the next authentication type which is digest Authentication okay so before we get into digest Authentication uh let's first understand what's the difference between basic authentication and digest authentication because on the front end when I use this particular API message you will not see any difference which I mean is I'll be sending this

[01:08] request with another username and password but as I said there will be no difference because in basic auth also we send an username and password and in the digest art also we are sending a username and password but the difference is digest authentication is much more uh you can say Advanced authentication type okay rather than just sending the username and password internally a lot of other things happen Okay so let's try and understand this little better with this particular diagram okay and here you can see that there are multiple requests and responses which are coming and going back instead of just one request and response in the case of basic authentication right where you send a get request with a particular username and password and the server uh authorizes that request and sends back the response okay but that's not the

[02:09] case with Digest auth so in this particular authentication mechanism right what happens is when we send a particular get request from any HTTP client right like our Tosca in this case okay so the server will respond back with a 401 unauthorized okay but uh even if it is four zero one unauthorized in the header we get some authentication information okay so which is the www authenticate okay this will be the header name and then inside this you will find uh two values which is um a realm and nonce values which will be used uh to Hash the subsequent requests okay so a hashing mechanism is applied to protect uh the particular request which is being sent to the server and which will be authenticated using a particular username and password and so in the next

[03:11] request uh which will be sent by the client it will include this authorization header with the information which was sent by the server which was this ww authenticate header Okay so so when we send this highest information from the client to the server then the server can authorize this particular request and it will send back a 200 okay response with the particular response payload okay so instead of just 2 or request and response there are four okay so there are two requests and two responses coming back from the server okay and that's the difference between basic authentication and digest Authentication but as I said you will not see any difference in the front end on the HTTP client side because internally Tosca is able to do all of this for you okay so now let's go back and let's try to

[04:12] use uh or create another API message where we can use this digest authentication right so I'm going to create a new message here and I'm going to call it Digest okay and here again in the end point I'm going to use a particular endpoint right and for this I'm going to use um API which is available with Tosca okay one of the sample apis which is the secured employee version 2.

[04:50] okay and this is protected by digest authentication right so it's webservice.cloud.com rest API secure employee version 2. okay now if I just send this particular request without any authentication obviously we are going to get 401 on authorized right but uh if I go back to my request and I now select uh digest Authentication and for this I'm going to pass the username and password okay and then I'm going to send this particular request okay and this time around you will see that we got a status code 200 okay okay with the particular payload which is the employee information okay but as I said internally Tosca is sending two requests but you cannot see that in here okay so that's how you use the digest authentication for any

[05:53] particular API requests which are protected by this particular mechanism okay so this was all for this particular video where we looked at the digest authentication type okay there are many other authentication types which we may look in our other sessions but hopefully this was helpful for you and helped you learning something new so do tune in to our channel uh to watch more interesting videos on API testing um with Tosca and we'll also keep adding more videos on other topics if you have any Topic in your mind then do share it in the comment section and will pick up that particular topic for learning Tosca also if you have not subscribed please do subscribe so that you get a notification whenever a new video is added uh deleted and this will help you to keep learning Tosca in a continuous manner so thank you for watching and until the

[06:55] next video keep watching and keep learning Tosca
