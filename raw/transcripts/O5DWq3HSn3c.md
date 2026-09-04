---
id: "O5DWq3HSn3c"
title: "Tosca Tutorial | Lesson 46 - Verify Row and Column Count of a Web Table | Table Controls |"
url: "https://www.youtube.com/watch?v=O5DWq3HSn3c"
channel: "QASCRIPT"
playlist: "Tosca Tutorial | Tricentis Tosca Automation Tool | End-to-End Test Automation | Model Based Testing |  Codeless Automation Tool | Tosca Certification"
playlist_index: 46
duration: 369
upload_date: "20230818"
source: "youtube-subs"
language: "en"
transcribed_at: "2026-09-04T08:01:38Z"
status: "raw"
---

# Tosca Tutorial | Lesson 46 - Verify Row and Column Count of a Web Table | Table Controls |

[00:07] hey everyone welcome back to this Tosca automation playlist and we'll talk about another interesting feature today so today we are going to discuss about one of the features which is available uh on the web tables so if you want to verify the row and column count of a particular web table then there is a method which you can use to get the total row count and the total column count very easily from any particular web table so let's look at an example now we have used this many times we have seen how we can steer this table uh using the constraints action mode on different columns right but see for example you have got a web table and you have to verify how many rows are there and how many columns are there okay for verification purpose so how are you going to do that so for that uh there is a property called row count and column count okay

[01:09] and we'll see how we can get this and also verify it so for this uh I have already scanned this module so I'm going to create a couple of test cases here okay so coming here I want to verify row count okay and uh the second test case is to verify the column count now I'm going to drag this module here in verify row count and what we need to do is we need to go to the table object okay so this is our table object and here we need to as I said specify a property called row count okay and then we are going to assign this row count uh into a buffer variable okay so we are going to call it row count

[02:12] and in the action mode we are going to select buffer okay so what's going to do it's going to get the row count using this particular property and then it is going to assign the value to the rocon buffer okay so uh that's done and then what we are going to do is we want to verify that this particular table has got the specific row count right so for that uh let's do a verification then and for that we are going to use the t-box evaluation tool okay and then I just need to do a verification here so I will be verifying uh buffer of row count okay equals equals uh five so I need to close this and then equals

[03:14] equals five right so this is a verification I want to do and then let's move on to our next test case which is the column count okay so let me drag this module again here and this time around the method is same but the name is different so we need to get the column count okay and then I'm going to also create a particular buffer called column count and then change the action mode to buffer here okay um also after this uh what we can do we can add another test step here again t-box evaluation tool and here we are going to verify so we are going to verify the column count okay and equals equals four right

[04:17] so we have got four columns and we have got four rows okay or actually the five rows because the first row is the header so it should uh actually verify correctly okay so if our methods are correct so let's quickly go ahead and execute this and check if this test case passes or it fails okay so the test case has passed and let's see what are the values which has been captured here okay so here uh the buffer with name row count is set to 5 and then in the evaluation um the expected was equal to actual so it evaluated to true and then here column count was four and the actual versus expected was also true so the verification has passed right

[05:18] as a best practice don't forget to rename all your test steps and also the test case names which I have already done and then you should also ask that the work state to complete it right so as you can see it's very easy to verify the row count and column count this might be useful in some scenarios where you have to put a verification on these particular values so that's all for this particular video I hope you enjoyed it and you learned something new today if you want to watch more videos please subscribe to our Channel and we'll come up with lots more videos so keep watching and keep learning Tosca
