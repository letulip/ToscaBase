---
id: "NRzZcXaskvo"
title: "Tosca Tutorial | Lesson 101 - No Mouse or Keyboard Methods in Test Step Values | Best Practices |"
url: "https://www.youtube.com/watch?v=NRzZcXaskvo"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 101
duration: 349
upload_date: "20230722"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:06:16Z"
status: "raw"
---

# Tosca Tutorial | Lesson 101 - No Mouse or Keyboard Methods in Test Step Values | Best Practices |

[00:07] hey everyone welcome back to the stores automation playlist and we are talking about Tosca best practices now this is the fifth video in the series so if you have not watched the previous ones go to the playlist and watch all of these previous videos now coming to the best practice number five but before we start I would also recommend you to subscribe to our channel so that you don't miss out on all the future videos uh as soon as we upload them okay so this best practice is talking about no mouse or keyboard methods so minimize the methods which are related to mouse or keyboard and these are basically uh it could be any method it could be some key combinations from a keyboard or it could be a mouse click right and you can use them in some of the methods like the send Keys method okay and it is very common uh whenever you want to click on a button or a link you generally use this click method okay or you want to send some key key combinations through

[01:09] your keyboard you in your send Keys method you use all these key combinations right so you have to understand that Tosca is trying to simulate this uh keystrokes from your keyboard or the click buttons from the mouse right using this methods which is defined in the Microsoft Keys okay so these are basically Keys which are defined by Microsoft which works in a Windows based operating system right so uh that's what Tosca is doing and for that uh it needs to connect to different apis through which it can basically perform this particular operation all right but you have to understand due to the complexity of this uh it may not be the best way to do this okay so generally uh it is much slower and not so stable okay so you can still use this method but uh class centers recommends that you minimize the use of this or you use something else okay for example if

[02:12] you are using this click method instead of that you can put a x now this x is doing the same thing as a click method so it will perform the click on a button or on a link right but it is much faster and also considered more stable okay so you have to take care of these things whenever you are designing your test case and in your test steps I try to use the more efficient and more faster methods instead of the regular methods okay so let's try to look at an example okay a real-time example on how this can be done so in our last uh best practice we were talking about the sweet on method right and in this test case you can see I have used uh The Click method okay to click on this particular buttons like calculate and send and it works

[03:13] absolutely fine you may not even notice the difference if I use something else but uh in the long run when you are executing long lot of test cases a small change or a small Improvement in the execution could help you immensely right so it can speed up your execution your execution time could come down okay so you have to take care of a small things in order to make your uh test set more efficient Okay so so instead of this click method uh what we can do is we can write X here okay and the same I can do it here and as you can see uh it is going to perform the same operation okay so let's run this and let's verify this so I'm going to run this now and it should work exactly the same as it was working earlier okay so let's see uh if it is still working

[04:13] the same using um this particular method instead of the mouse or keyboard method right so it is clicked on the calculate button uh you've watched it the difference you will see that the mouse pointer has not moved to the button because Tosca is not actually simulating the mouse and keyboard movements okay so it is doing this internally and that's why I said this method is much faster because it is not a UI interaction right it is doing that internally so it is much faster than simulating the exact way a human does it right like we take the mouse pointer and then we click on a particular button right so that's the simulation which is performed when you use a keyboard or Mouse method but if you use something else then it will be much faster right because you don't need to do that on the UI okay so to conclude Transcendence

[05:15] recommends that don't use or minimize the use of uh the mouse and keyboard methods instead of this try to find a more efficient and faster method okay so that's all for this video I hope you like it and you enjoyed it um there are lots more videos coming up on our channel so keep watching and keep learning
