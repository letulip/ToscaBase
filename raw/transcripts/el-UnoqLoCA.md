---
id: "el-UnoqLoCA"
title: "Tosca Tutorial Lession 63 -  Clear and Archive actual execution logs | Execution Lists | Logs |"
url: "https://www.youtube.com/watch?v=el-UnoqLoCA"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 63
duration: 421
upload_date: "20230819"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:02:53Z"
status: "raw"
---

# Tosca Tutorial Lession 63 -  Clear and Archive actual execution logs | Execution Lists | Logs |

[00:08] hey everyone welcome back to our Channel I am back with another interesting topic in the Tosca automation playlist in this session I am going to tell you how you can archive your execution logs in the execution list now we have already seen how we can execute our test case using an execution list so the results are always maintained in the execution lists which are nothing but the logs which are stored in the actual log right now for example this execution list has got an actual log which is storing the logs as we go ahead and execute this multiple times right so multiple execution entries will be uh stored here as we go ahead and execute this and everything is stored in this actual log so this particular execution list has got one execution entry and this was executed uh three months back okay so this is all fine but what if you are

[01:09] working on different releases which happens quarterly or which happens monthly or which happens weekly now for each release you need to execute this test cases again and again right because these are regression test cases and you want to test whether your changes in the application have not affected your regression test cases and you want the latest results to be linked to your requirements so that your release dashboard can show that these are the current results okay but for in order to do that we need to delete our previous execution logs okay because these are all logs and although we would like to keep it but we don't want to show these logs in our release dashboard right which is nothing but our requirements and this execution list they are linked to the requirements so if you don't clear this log then it is going to reflect it in the requirement

[02:11] section right so one way is to just clear this logs and it will delete this Old Log you cannot see this anymore okay so that you can do easily by right clicking on actual log and then clicking on clear lock so that will basically delete this but I don't want to do that right because what I want to do is I want to compare my results which is my current results versus my previous results so I want a way to store my previous results and also I want the log to have the current results and that I can do only by archiving my previous locks so that I have it in a safe place and I can always get it back okay so how you can do that um that you can do from the execution list okay so right click on the execution list and there you will find and archive actual execution log option okay so click on that it will ask you

[03:13] for a archive name so I'm going to give it RC okay and rc01 or something and then I'm going to click ok it is going to ask you whether you want to discard your actual log okay now if you want to remove uh the entries from the actual log then click on yes if you don't want to remove then click on no okay for my case I would click on yes because I want to remove my actual entries from the actual log okay so I'll click on yes and that will clear off my current actual log so for this execution entry you don't see any logs but you only see the archive log with this particular name okay um and the actual log is actually empty now okay it only contains the archive logs for this execution list now

[04:14] um how I can get it back okay uh so I can just if I want to get this back into my actual log then I just drag it and I drop it into the actual log okay so that way again you will see the actual log is green that means the actual log is still present okay so but I don't want to do that um so what I will do I will delete this and I will repeat the process just to show it one more time so I'm going to Archive the actual execution log um and I'm going to this time name it something like archive results okay I am going to discard all the entries so the actual log is empty now okay and we have got the archived results now I can go ahead and execute this okay although this time it's going to fail

[05:16] um that is because um I have not opened the web page which it is expecting so this will fail but that's fine uh I just want to show you how you can archive your previous looks and then you can get your latest logs for that particular execution list so that your requirement dashboard or your overall dashboard depicts the current picture of your test cases not the previous results okay also another benefit is you will always have the previous results with you okay so you can easily revert this results back as I showed you just drag and drop it into the actual log and that will revert back the results uh plus you can also see what failed okay which depth field uh which was passing previously so from the archived results I can see that this step had passed earlier and now this step is failing so

[06:18] I can easily make out what has changed in the application and I can debug it much easier rather than if I would have just deleted this right so this way you can maintain an archive of different results for your execution list and this is mostly helpful when you're working with different releases that's all for this particular video if you have any questions then please leave it in the comments if you like this video then please subscribe to our Channel thanks for watching and I will see you in the next video
