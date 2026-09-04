---
id: "SZj-04A7aQA"
title: "Tosca Tutorial | Lesson 25 - Scroll Window | TBox Window Scroll Operation | Standard Module |"
url: "https://www.youtube.com/watch?v=SZj-04A7aQA"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 27
duration: 387
upload_date: "20231007"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:00:17Z"
status: "raw"
---

# Tosca Tutorial | Lesson 25 - Scroll Window | TBox Window Scroll Operation | Standard Module |

[00:07] hey everyone welcome back to this tosa automation playlist today we are going to talk about how you can scroll down a page uh which has got a lot of content and you want to view any control which is at the bottom of the page so you basically want to scroll down or up or you can also scroll horizontally using the horizontal and also vertically using the vertical axis so tosa provides you with automation module which is called the tbox scroll window operation and it is part of the standard subset so let's see how we can use that okay so for this purpose I have created a test case here and then I'm going to search and ADD test step here I'm going to search for the tbox scroll okay and then I'm going to add this particular module into the test case now going through the different module attributes or the parameters so the first module attribute is called caption now this is uh the

[01:09] caption of the application window uh which you want to scroll uh and caption would mean that uh it is probably the title of the page or the window okay then there is window index so you want to specify uh which window you want to scroll based on the opening order so if the are multiple Pages which have the same caption you can Define the window index using which uh tosa can then perform the operation on that particular window then uh there is vertical and horizontal so you have to specify uh what amount of pixels or lines you want uh tosa to scroll uh along the pach so it could be in terms of a vertical axis or in terms of horizontal axis in both cases either you have to specify it in pixels or the lines then there is something called uh the mouse policy and there are two options none or Center so this is

[02:11] basically tosa will position uh the mouse pointer uh during the scrolling so either it could be Center or it would not move the mouse pointer at all then there is the direction policy uh there are three options no Direction policy vertical uh first and horizontal first so it basically decides uh what tosa should scroll along either the vertical or horizontal axis first okay so if you mention the vertical first then it will scroll the vertically and if you mention horizontal first then it will scroll horizontally first okay and then there is also a delay you can mention the time in milliseconds uh this is basically when you have both horizontal and vertical defined then uh there will be a a delay between these two operations so tosa will wait for that amount of time before it does the other operation which could be horizontal or vertical scrolling okay so these are all the

[03:12] different module attributes uh which you need to Define not all of them are mandatory uh you need to define the caption uh if you require you can Define the index uh you have to Define either vertical or horizontal so how much you want to scroll and then uh the mouse policy can be left as Center and the direction policy you can choose between vertical and horizontal so for this particular example I have picked up this demo website uh where uh the infinite scroll has been implemented so as long as you are just scrolling it will keep on increasing okay so here we are going to scroll vertically okay uh it is currently at the top of the page but I want to scroll vertically downwards okay so uh let's implement this now um as you can see uh the title of this page is the internet right and that would be your caption right so uh I will mention the

[04:13] caption here as the internet and then I will put a regular expression as well so that if in future this particular title changes it will still work out okay uh I don't need to mention any window index because there's just one window uh and then I want to do a vertical scroll so I'm going to mention 500 pixel okay and that will vertically scroll the page to 500 pixel Mouse policy I will leave it at as Center and then Direction policy I will do vertical first although it's not required because we are not uh doing a horizontal scroll right and then we don't need any delay because uh we are just doing one scroll not both the Scrolls so let's go ahead and execute this test case and let's see if uh TSA is able to scroll the page vertically so let's run it in scratchbook and now you will see that uh tosa was able to scroll vertically okay

[05:16] now we are at the middle or at least somewhere down the page right if you want to scroll more then just increase the pixels okay and um in the results window also you will see that the test case has passed right so that's how you can uh vertically or horizontally scroll uh down the page it could be applied to either a application or even a Windows based application right so it basically needs to be a window which has got the scroll bars like horizontal or vertical and then you can scroll up or down using this uh tbox automation module which is known as tbox scroll window operation also do keep it in mind that uh this particular module is not available in older versions of tosa I'm currently using the tosa 16 version and it's available in this particular version that's all for this particular video if you have any questions then

[06:17] please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
