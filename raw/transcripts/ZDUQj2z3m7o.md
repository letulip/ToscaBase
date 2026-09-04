---
id: "ZDUQj2z3m7o"
title: "Tosca Tutorial | Lesson 83 - Authorize API requests using Basic Authentication | API Testing |"
url: "https://www.youtube.com/watch?v=ZDUQj2z3m7o"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 83
duration: 307
upload_date: "20230424"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:04:33Z"
status: "raw"
---

# Tosca Tutorial | Lesson 83 - Authorize API requests using Basic Authentication | API Testing |

[00:14] testing now in all the previous sessions we have already seen how you can work with API testing in Tosca using API scan and also the Tosca Commander to create API test cases and also verify your apis but today uh we are going to look at some of the different options which are now available especially on the authentication side right so we have looked at some of the authentication mechanisms which are available in Tosca but today I'm going to show you with specific examples on how you can use this authentication types okay so the authentication type which is the basic one or the first you can say also is the basic authentication right and as the name suggests this uh authentication is used for apis where you have to pass a username and password before you can authenticate a particular request okay

[01:14] so for this purpose um I'm going to create a API message okay I have already created a folder you can see authentication and then this is the new message okay I'm going to name it basic uh auth okay and then um in this end point I'm going to use a particular API message okay and for this purpose I'm going to use one of the sample apis or provided by Postman and this is to test the basic Authentication obviously you can use any API okay where you need a basic authentication which is basically a username and password okay any API which is protected by a username and password you can use that endpoint but I'm going to use this particular endpoint so it is called Postman eco .com and slash basic auth

[02:19] okay so I'm going to use this particular endpoint and then let's first check whether we get any response back when we send this without any authentication okay let's see whether it is protected or not so let's try and run this and let's see what is the response for this particular request okay so it's expected uh I'm getting a 401 unauthorized right for status code and in the payload I'm getting unauthorized which means I'm not authorized to basically access this particular API right and I need to provide uh some authentication which should be present in the request okay and it will be sent back to the server so that it can authorize that particular request and then send the response back okay so now let's go back to the request and this time around let's try with authentication basic okay you will find it here and in the username and password so I'm

[03:23] going to pass the username and the password okay so uh now we have provided the authentication now let's go ahead and run this again once more and let's see whether this time around it can authorize this particular request okay so as you can see this time around uh the status quote was 200 okay and also we got a response uh payload which is authenticated true okay so this way you can use the basic authentication in Tosca API scan to authenticate your requests using a username and password so this is one of the most common uh authentication mechanisms used for apis right and then there are other API messages which you different types of authentication mechanisms okay so in the next session I'm going to also

[04:25] show you how you can use another authentication type and which is the digest Authentication okay so that's all for this session hope it was useful and you learned something new so in the next session as I said I will be talking about another authentication type which is digest authentication so do tune into our channel to watch the new video and if you're not subscribed then do subscribe so that you get notified whenever I add this particular video Until then keep watching and keep learning
