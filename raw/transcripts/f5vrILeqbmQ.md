---
id: "f5vrILeqbmQ"
title: "Tosca Tutorial | Lesson 84 -  Authorize API requests using Digest Authentication | API Testing |"
url: "https://www.youtube.com/watch?v=f5vrILeqbmQ"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 427
upload_date: "20230425"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T13:44:12Z"
status: "raw"
---

# Tosca Tutorial | Lesson 84 -  Authorize API requests using Digest Authentication | API Testing |

[00:05] Hey everyone, welcome back to this Tosca playlist and today we are going to talk about another authentication type which is digest authentication. Now this authentication mechanism may be used with some API messages or requests and you need to make sure that you are using the correct authentication type for your API message before you send them, right? Now in the previous session, we already looked at how you can use the basic authentication using a simple username and password.

[00:36] So if you have not watched, the video URL is on the top. So go ahead and watch that before you start watching this particular video which is the next authentication type which is digest authentication, okay? So before we get into digest authentication, let's first understand what's the difference between basic authentication and digest authentication. On the front end, when I use this particular API message, you will not see any difference which I mean is I'll be sending this request with another username and password but as I said, there will be no difference because in basic auth, also we send a username and password and in the digest auth, also we are sending a username and password.

[01:23] But the difference is digest authentication is much more, you can say, advanced authentication type, rather than just sending the username and password, internally a lot of other things happen, okay? So let's try and understand this little better with this particular diagram, okay? And here you can see that there are multiple requests and responses which are coming and going back instead of just one request and response in the case of basic authentication, right?

[01:58] Where you send a GET request with a particular username and password and the server authorizes that request and sends back the response, okay? But that's not the case with digest auth. So in this particular authentication mechanism, right, what happens is when we send a particular GET request from any HTTP client, right, like our Tosca in this case, okay, so the server will respond back with a 401 unauthorized, okay?

[02:29] But even if it is 401 unauthorized, in the header we get some authentication information, okay? So which is the www authenticate, okay, this will be the header name and then inside you will find two values which is a realm and nonce values which will be used to hash the subsequent requests, okay? So a hashing mechanism is applied to protect the particular request which is being sent to the server and which will be authenticated using a particular username and password and so in the next request which will be sent by the client, it will include this authorization header with the information which was sent by the server which was this www authenticate header, okay?

[03:24] So when we send this hashed information from the client to the server, then the server can authorize this particular request and it will send back a 200 okay response with the particular response payload, okay? So instead of just two or request and response, there are four, okay? So there are two requests and two responses coming back from the server, okay? And that's the difference between basic authentication and digest authentication but as I said you will not see any difference in the front end on the HTTP client side because internally Tosca is able to do all of this for you, okay?

[04:09] So now let's go back and let's try to use or create another API message where we can use this digest authentication, right? So I'm going to create a new message here and I'm going to call it digest, okay? And here again in the endpoint, I'm going to use a particular endpoint, right? And for this I'm going to use API which is available with Tosca, okay?

[04:45] One of the sample APIs which is the secure employee version 2, okay? And this is protected by digest authentication, right? So it's webservice.tosca.cloud.com that's the API secure employee version 2, okay? Now if I just send this particular request without any authentication obviously we are going to get 401 unauthorized, right? But if I go back to my request and I now select digest authentication and for this I'm going to pass the username and password, okay?

[05:26] And then I'm going to send this particular request, okay? And this time around you will see that we got a status code 200, okay? With the particular payload which is the employee information, okay? But as I said, internally Tosca is sending two requests but you cannot see that in here, okay? So that's how you use the digest authentication for any particular API requests which are protected by this particular mechanism, okay?

[05:57] So this was all for this particular video where we looked at the digest authentication type, okay? There are many other authentication types which we may look in our other sessions but hopefully this was helpful for you and helped you learning something new. So do tune into our channel to watch more interesting videos on API testing with Tosca and we'll also keep adding more videos on other topics if you have any topic in your mind then do share it in the comment section and we'll pick up that particular topic for learning Tosca.

[06:36] Also if you have not subscribed, please do subscribe so that you get a notification whenever a new video is added related to Tosca and this will help you to keep learning Tosca in a continuous manner. So thank you for watching and until the next video keep watching and keep learning Tosca.
