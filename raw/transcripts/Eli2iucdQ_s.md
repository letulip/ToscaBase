---
id: "Eli2iucdQ_s"
title: "Tosca Tutorial | Lesson 154 - Test Data Management with Tosca | Test Data Services | TDS Modules |"
url: "https://www.youtube.com/watch?v=Eli2iucdQ_s"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 4152
upload_date: "20250519"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:09:03Z"
status: "raw"
---

# Tosca Tutorial | Lesson 154 - Test Data Management with Tosca | Test Data Services | TDS Modules |

[00:00] Hey guys, welcome back in this session. We are going to talk about how you can do test data management and TDS which is test data services in Tricentis Tosca. Okay, but before we move into how Tosca helps you with the whole test data management, let's first understand what is test data management and why it is so important in test automation. Now if you have worked with any test automation tool or any test automation framework, test data plays a major part.

[00:35] And in some of the test automation frameworks, the whole framework is driven by test data and these type of frameworks are also popularly known as data-driven frameworks. Now in most of the automation tools or frameworks, we generally use external data sources to manage our test data and this management is mostly manual, right? So we can create test data from different tools or different techniques.

[01:05] But in order to manage the test data, either we have to write some code on our own or we have to do it manually. Okay, and these external data sources could be anything. It could be Excel, it could be a database, it could be XML, right or JSON. So there are multiple data sources which can be used to store that test data and then to create test data, something like you can use random test data generators or different tools to generate this test data, right?

[01:39] So the storing and creating of test data is still not a problem that can still be done, but management is a time-consuming and also quite challenging process, right? So identifying the correct test data for your execution or your test cases is very important, okay? And test data management is this process of identifying and managing the right test data for any system you are going to test, okay?

[02:12] You have to make sure that for each test execution, you have got unique test data because if you are using a particular test data in one test execution cycle and then again in the second test cycle, if you use the same test data, there are high chances that your test will fail because the application may not accept the same test data, right? So for example, if you are going to create account or a registration form you're filling and you are using the same email address, right?

[02:48] The application may not accept the same email address for the registration because that registration has been completed by that user using that particular email address, right? So this is one example where you can see that you cannot repeat that test data next time. So it's very important that you use a unique test data and you manipulate the test data in a way that every test execution run has a unique set of test data. Okay, also there are lots of scenarios when you work with different applications, right?

[03:25] So whenever you are testing any particular application, it is not just a web application, right? So there is a back-end application then there could be some other front-end applications which are communicating with this web application, right? So generally a process comprises of multiple applications and we need to test that particular process. Okay, so when we are using test data, we have to make sure that all these applications can process this test data and the data can flow from one application to another seamlessly without any problems.

[04:03] Okay, also as I said, manually maintaining all this test data and managing it is not very efficient. It's a very slow process and it's also time-taking, right? So all of these points you see highlight the importance of test data management, right? So if a tool can help you with this test data management process, then your job becomes much easier. You can use unique test data. You can use test data across different applications and you can also track and update your test data accordingly.

[04:41] Okay, and this is where Tosca comes into the picture, right? So Tosca has this way of managing test data, which is called the test data management. And for this it uses the TDS, which is called the test data services. Okay, now it overcomes all the challenges which we discussed earlier and it provides a central place where you can register your test data well after you created it and then you can use the right test data in all your test cases.

[05:21] You can track and update state of every test data throughout your whole life cycle and you can also manage your data so that it can be shared across different applications. Okay, so test data services has different standard modules which are available part of your standard.tsu where you will find all of these different steps or you can perform all of these different steps. Okay, so as you can see in this picture, this is the test data management and then these are the different processes, which could be different applications which are basically processing this test data.

[06:07] So the first process it will create some test data and that it will be stored or registered in the TDM and then this test data will be used by a process second process right which will modify the test data. And then again, it will be stored in TDM and then it will be again used across the process 3 and that continues right and the test data management. It takes care of all the other things like you are using the right test data.

[06:39] You are tracking and you can update your test data and you can also share it with different processes. Okay, so all of this could be done by test data services which is TDS and it's a Tosca server component. You can set it up on the Tosca server. Okay, and the backend would be a database or you can also store it in your local memory, but this is where you can create different repositories and you can create different data in this particular repository.

[07:18] So let's go to our Tosca server and let's look at how this test data services work and how we can use different modules to work with our test data. So now when I open my Tosca server landing page, which is localhost 8080. This is where we had set up our Tosca server. So the test data services is part of the Tosca server installation. So once you are installing Tosca server TDS will also be installed automatically.

[07:53] Okay, so don't need to do anything additional to install or set up TDS or test data management in Tosca server. It will be part of your Tosca server installation. Now to access it you have to go here under test data management in your server landing page. Now the test data management or TDS it has got a web interface like you can see here. Okay, and here you can create repositories. You can create test data types.

[08:25] You can also create your test data. You can delete you can manage you can do all kinds of stuff right on the web interface. But all of this could also be done on using the standard modules in Tosca commander. So we'll try to have a look both ways first. We will try to see how you can do it in the web interface like right here and then we'll see how you can go to Tosca commander and you can automate this whole process so that it can be integrated with your whole testing process.

[08:59] Okay, so test data management or TDS has got its own repositories like we had repositories for a workspace in Tosca commander. We have repositories for test data management. Okay, and as you can see these are the three repositories which I have created I can go ahead and edit them. I can go ahead and also delete them right? So there is a delete and edit button here.

[09:29] So I can go ahead and delete this repository right from here also and also you can delete the database which is which is linked with this particular repository. Okay, so that will delete that particular repository as I said I can also edit the name and description for this particular repository. Okay, the data repository so let me remove this and then I will explain so this data repository. This is the default repository for tedious and it is already present once you open this page.

[10:04] You will see this data repository obviously it will not contain anything inside this but we can always go ahead and add our type. Okay, so the most important part of your test data services or test data management is a type and a repository right? So the first step is to create a repository and then inside that you will have different types. Okay, now these types or the test data types could be anything.

[10:36] Okay, it can be divided based on your functionality of the application or different parts of your application different processes of your application or it could be just different teams or different applications in itself. Okay, so it completely depends on you how you want to define your types, but you need to have a particular type before you can create any test data. Okay, so we'll look at an example. So after we create a type then you can create different test data inside this type.

[11:10] Okay. Now if I can go back here first, let me show you how you can create a repository like this default repository or the other repositories which represent already in my tedious right? So you have to click on this create repository and then it will ask you for some details which you can fill and then you can save so that will basically create your own repository. Okay. Okay. So to start off we need to give it a name first, right? So I can call it test first or test repository.

[11:44] Obviously the name cannot contain any spaces or any special characters. So do take care of it. Okay. And then you can also enable authorization if you want but that can be done on the Tricent is service configuration side. We are not going to look at it. There are different types of repository which you can create the default one is SQLite, but this will be basically stored in a local folder. You can see the location of this C program data Tricent is Tosca server test data service and then it will create a DB file.

[12:21] Okay. So this is basically if you don't have a database for your test data, then you can create it in this particular folder on this using this SQLite DB. But if you have something like mssql or Oracle you can use them. You can provide all the details for your database server like the server URL the database the username password the schema and then click on test connection right and then you can just go ahead and save it.

[12:52] You can also just use the connection string if you want just pass the connection string here and the schema if it is required. Okay. Similarly for Oracle it is the same you need to provide a connection string then test connection and then you can save it. Okay, but we'll be using for this session will be using the SQLite. Okay, so it will be stored in this particular location and I can click on test connection so that it will connect it and you will see this connected sign, right?

[13:25] So if you get this that means there is no problem with your connection, but if you don't get this then there is a problem. Okay. After this you can provide a description for this repository. Okay, and I can do that just this is a test repository. Okay. Now sometimes you will see that this save button is not enabled. This might be because either the previous database file is already present in your in your local in your local folder or maybe you just need to refresh the TDS service.

[14:08] Okay, but let's go ahead and try this again. Okay, so this time you can see after refresh the page it again got enabled so I can test the connection and then I can again put the description here. So this is test repository. Okay, and then click on save so that's going to create our test repository. You can see here. This is the test repository.

[14:39] I can delete and edit as I said earlier and click on it and then you can add a type here now this type as I said it can vary depending on what type of application you are testing what functionalities you are testing right so you can basically divide your types of test data so that it can be recognized while you are trying to use this test data, right? So for example, if I need different test users, right with some information of this users like their names the last name first name email or some other details, right?

[15:17] So it could be like a users file which contains a list of different users. So I can create a type called users. Okay, I can always go ahead and import this data to type or I can create it from the modules from in our tosco commander, right? So either way I can do it if I have a file I can browse it and I can just import that file so that all the data will be imported into this particular type.

[15:48] Okay, if I have copied it from somewhere then also I can paste it here and I can import it and then you can also use some sample files which are provided by tosco. So for names it is already there names International 500 on Jason and then traffic is airlines torches, right? So this will create some sample data, right? So we can see that so just select the category and select the type and then just click on add.

[16:23] Okay, and this will basically import some sample test data into your type users. So as you can see I have imported this data for this particular type from a sample Jason file. You can do it with different file formats. I haven't checked but it should be available for Excel for maybe TXT CSV or Jason, right? So you can see here. It just looks like a database table right with different rows and columns and then you have got these different records, right?

[17:00] So there are around 500 records on this particular type and it has got this name surname gender region, right? So you can also add your own item here once you click on add item. You will see that it pops up this row where you can enter your details, right? So for example, I can create this test data here a new row I can add into this test data, right?

[17:31] So I can add all the details here and okay, I can create a new row like this and then just click anywhere and then that row will be added into your table, right? So this is how you can also delete and you can see here this lock sign.

[18:02] You can also lock this particular row so that it cannot be used by any other process trying to use this test data while it is in use. Okay, so we can lock and unlock the item right from here or we can also delete this particular record from this particular type. Okay, so you can consider a type as a particular table inside your database and then that table contains different records inside this.

[18:36] So I am trying to explain it in a more database like convention, right? It works pretty similar. Okay, so I can also export this data. You can see all these into different output files like CSV Excel and Jason and then I can import it back into a different type. Okay, I can put the encoding I can put line break and a separator and I can export it. Okay, so this will basically export it into a CSV file as you can see here and then I can easily import the same data.

[19:15] Okay, so if I add another users one type, okay, and here I can just import that particular data as we talked earlier. Okay, so I can select that file and I can import it back. Okay, so as you can see you can easily import and export data right from this user interface you can add items you can add types you can manage everything for your repository inside the test data services.

[19:52] Okay, so all of this functionality is available on the web interface when you go into your Tosca server landing page and you go into test data management. Okay, but all of this can also be done through Tosca commander and that is the ideal way of doing it. Like so you don't want users to go to your server landing page and create test data there it should be created on the fly when you are running your test automation. So before you run your actual test cases, your test data should be already created, right?

[20:27] So let's see how we can use the standard modules to create types or to enter data into a particular type how we can manage them how you can attract them and update them right? So all of this can be done using the standard modules and let's see how we can do that. So for this demonstration, I'm going to still use our application which we have been using throughout this whole course. So that is the vehicle insurance application, right?

[20:59] So we have already developed automation test cases for this. Now, let's see how we can create the test data for this and maybe we can integrate it back to our test cases so that the test data is automatically created and we can use the test data instead of us generating the test data within the test cases like we have done earlier. Okay. So for this, let me create another repository here. I'm going to call it sample app.

[21:31] Okay, and I'm going to create this sample app and inside this I'm going to now create a type and I'm going to call it vehicle. Okay. So we can actually create different types here. I can create it for automobile. So let's do that. Okay, and click on add to create this type currently. There are no items, but that's fine. I don't want to add items from here.

[22:02] I want to add items from our test cases. Okay. So let's go back to our Tosca commander and let's go back to our project. Let me open the project here so that we can create a new folder where we can create all this test data. Okay, so this is our project. So first let's look at how we can use the different modules and what different modules are present inside your TDS standard modules and how we can use them to basically manage our test data and then we will see how we can generate the test data and also use it in our application.

[22:47] Okay, so for that purpose, let me create a new component folder here. I'm going to call it test data. Okay, and inside this I'm just going to create another test cases folder and inside that I'm going to create a test case. So generate test data. Okay, and then inside this we are going to add different modules. So once you go into your add test step and here you need to start searching for test data.

[23:23] Okay, and once you search for test data, you will see all the different modules standard modules which are available, right? So these are all the test data modules. We have got update type, update item, delete item, import items, export items. We have got expert module which contains all the different modules like move item to type, find and provide item, create and provide new item, right?

[23:55] So we'll be using some of them, right? So we'll be starting off by creating and providing a new item. Okay, so this can be done. So here what it will do it will create a new item inside our type which we have created right which is called vehicle. Okay, so in this you have to pass three parameters basically existing or new TDS type. Okay, you can pass alias name or item if you want to basically provide alias name.

[24:33] Otherwise it's not mandatory and then we need to filter our data based on some data structure. Okay, but first let's provide the type here. So our TDS type is vehicle as you remember and here we need to provide a TDS attribute and a value. Okay, so what item we want to create inside this particular type vehicle.

[25:04] Okay, so what I want to create is basically go into the application and once we go into the automobile page, these are the different items which are basically our test data for this particular application type because for every test case I'm going to use this test data like I want to test with different makes different performance different date of manufacturers like so I should have that test data in order to test my test cases with different sets of test data.

[25:39] Okay, so let's create some test data for this test data type in our test data services. So I want to first have item called make right. So let's create that and we are going to call it make. And then I'm going to give it a value called BMW. Okay, and then I can create another item and then I can give it a value.

[26:13] So our next item is engine performance, right? So let's call it engine and I give it a value something. Okay, and then maybe date of manufacture or let's call it DOM and it should be in this format. So I will call it 0101 and 2014. Okay, and then let's create number of seats.

[26:47] So seats and that would be four and then a fuel type. So, okay, and then I can name it patrol after this list price, right and here I can give it something like 1500 and annual mileage.

[27:24] Okay, so mileage and let me give it thousand. So this will basically create the test data for all the different items present on this particular page. We can also generate random data instead of giving these values here, right or we can also import this data if we have stored it somewhere on our Excel file, right?

[27:55] So we can use the import module. But right now I'm just trying to show you what are the modules which are present and this is the first module which is to create and provide new item. So it will basically create a new item and it will also provide that item for the remaining part of your test case. Okay, so everything goes in a particular flow or you can say in stepwise. So the first step it will create an item and it provided to the next step.

[28:26] The next step will take that item and it will do some update shown so which will see. Okay, but first let's create this so now that I have this I can go ahead and run it in scratch book. And hopefully the item will be added to our type. Okay, so this test execution field and I did this on purpose so that we can have a look at this mandatory information or you can call it a prerequisite step before you can run any tedious modules.

[29:03] Okay, so we need to have two configuration parameters added before we can run any test data services test cases. Okay, so we can either create it under configuration here. Okay, or we can create it also in our test configuration parameter where we are creating the test cases. Okay, so here like we create any other test configuration parameter we have to add a test configuration parameter here and we have to name it test data and point.

[29:41] Okay, and we need to give it a value you can see the value is already populated but it will be your server address and slash test data service for me it is local host. So I will give this okay value and then I may need to change it because my port is little bit different right? It's not the default port. So let me give it the port as well. Otherwise it may lead to some error. So this will be the complete value and then we need to add another test configuration parameter and that is the test data repository.

[30:20] So these two configuration parameters are very important. Okay without this it won't work. So test data repository here we can mention what is our test data repository name. It was sample app. Okay, so these are the two test configuration parameters which you need to add and after this you can again try and execute and this time hopefully it should be executed and the test data should be created in that particular type.

[30:52] Okay, so you will not see anything in the logs specifically because it is creating the test data but the best way to verify is to go back to your server page and just do a refresher. Okay, but we did a mistake. I mentioned a vehicle as the type so it created a new type called vehicle and it inserted the data inside this so you can see a single row right now and we had another type which we added right here automobile, but that's fine, right?

[31:34] So this test case can do both. It can create a type a new type or it can write create this items into an existing type as well. Okay, so if I go ahead right and I come here and then I change this type. Okay, I can change it to automobile. You can see it will be appearing in the drop-down as well. Now now that we have run this once it is able to grab those types.

[32:05] Okay, so you can easily change this type and you can again run this. Okay, so I can this time I can call it Audi and then if I run this again you will see it will be now creating it inside the automobile type. Okay, so if I go ahead and refresh this you will see that it is now created another record the make is different but all the remaining details are same so it is creating a record inside automobile and we have also a vehicle type which has got this particular information, right?

[32:51] So this is how you can use this particular module create and provide new item to basically create a new type or create items into an existing type. Okay, we'll see later how you can randomize this data and also how you can run this in loop so that it can generate any number of data for you. Okay. So after this let's go into our next module.

[33:24] Okay, and that is let's go to add desktop and here let's type this data and let me expand this so that we can see this and the next step basically is in the flow is to find and provide item, right? So once you create and provide the new item you we need to find it right so that it can be tracked right and then we can either do an update or we can insert something so that once we use this test data it can be I mean it is a use test data right?

[34:05] So we need to update that okay, this particular test data has already been used right? So for this we need to again put a TDS type here. Okay, so let me call this this time maybe vehicle. Okay, so this is our TDS type alias name is not mandatory position. We can give a first position or random position.

[34:36] It will pick up based on that. Okay, and then we can also look at a TD QL query. Okay, it is a query which can be easily done, but let's stick to the data search filter. Okay, and you can also sort your data based on some values. Okay, so these are the different properties for this particular module here again. We are trying to search particular data or filter basically our data based on some particular value, right?

[35:13] So what we could have done also on this particular data or on this data structure apart from what we added from the application. We should also add a custom item here. Okay, so let me add another item here and I'm going to call this status. Now the reason for using this status, okay is we are trying to verify what is the status of the test data because in test data management when the test data is flowing from one application or one process to another process we need to identify what is the state of the test data if it is already a used test data then you need to use a different test data, right?

[36:09] So this is a way of tracking and updating your test data. So you should always have this field called status so that you can track your test data the status of your test data whether it has been already used or not used by the application. Okay, so now what I can do here is I can search based on this particular custom field. Okay, so I can say here status and once you give this value right the status field the action mode will automatically change to constraint because we are trying to filter out values based on some particular some particular data, right?

[36:57] So it is a constraint type. It is easier to filter out using the constraint action mode and that is why by default it will change to constraint and here I'm going to call it status is new. Okay, so whatever data I have in this particular table if that particular status is new then only it will be filtered and then it will be provided to the next process in this complete flow.

[37:29] Okay, now it won't be doing much here right because what we are doing is we are just filtering out the data. So we would not be able to visualize what is happening here. But what we can do is we can basically use something called Tosca buffer. Okay, so I'll be using set buffer. Okay, okay.

[38:01] So this is the T box set buffer. I'll give it a name here called status. Okay, and then I'm going to pick up the value which has been searched here and it will be providing us that item, right? So what we can do we can grab that item from a TDS variable. Okay, so here we have to use this Calibris and then we have to type TDS so that will basically grab the value which has been stored in the memory after it has executed this particular step.

[38:43] Okay, so we are going to call this vehicle. Okay, dot status. So you will see if you have written the syntax correctly, it will show it like this. If not, then there is some problem with your syntax. Okay, so it is not doing much. It is just setting the buffer so that we can see the value what is the output of this particular step which is find and provide item.

[39:16] Okay, so let's go ahead and run this once again. Maybe we don't want to run the create and provide new item because it is going to again create a new item, right? So let's run these two steps for now. Okay, this test failed but I know the reason you can see in the log info that no available test data was found and that is because I forgot that we had added status recently.

[39:52] So this data was not created, right? So if I go into my test data management under vehicle, if I refresh there is no item called status. Okay, so that status column has not yet been created in our test data and that is why it is not able to filter. Okay, so let's do one thing. Let's go ahead and create this particular row here or this particular item in this particular type.

[40:25] Okay. So what I'm going to do is I am going to change this to vehicle. Okay. And I'm going to now run all the three steps together. Let's see what happens. Okay. Okay, so all that steps past and now you can see in my set buffer step.

[40:56] I can see the buffer value. Okay, and you can see that it has been set to value new so it was successfully able to create the item. It was successfully able to find the item and then it was able to also provide that item into the next step where I am trying to grab that value so that I can see that value in a real time application what you will do you will use the same method, but you will not use maybe the set buffer what you will do when you are taking the application or starting the application in all these fields.

[41:32] You can grab that value and you can enter in these particular fields. Okay in the similar way like I have shown you you can use the tedious and then the expression where the type dot whatever item you are trying to access. Okay. So it's it's just like grabbing some value based on your database table, right? So based on your records you take that particular item and the table name so table name dot engine that vehicle dot engine will give this value vehicle dot DOM will give this value, right so I can grab all these values and I can then use it in my test cases.

[42:18] So that's what it is doing. Okay, so that's our two modules now. Let's look at our third module. Okay, and let's search for test data again and this time I am going to use the update item. Okay, so in this update item we have to give alias name and this alias name is like the type so you can provide your vehicle.

[42:51] Okay, and then in the data structure we have or we can provide item which we want to update right? So what is happening here is I am now trying to update the status of metastata that it has already been used. Okay, so this will basically change the record. Okay, so this will basically change the status of this particular record from new to used.

[43:32] Okay, because I have already used this in this particular step. So while flowing this data through the process I'm going to change the status. Okay, so here I was able to track the status and here I am able to update the status of that particular item. Okay, so this will be now status used and what we can do is this time around we are going to just run these three steps and let's see if it executes.

[44:08] Okay, right. So it executed and now if we can see whether the item was updated or not again refresh this and come here and you will see now the status has changed to used. Okay, so this is how you can track and update the status of your test data. So individual items you can also do an update for all these items. Okay, if you want to inside your test cases using this module test data update item.

[44:44] Okay, and now let's go ahead and look at some more modules, but these are the important ones. Okay, but let's have a look what other modules are present here. So we can update a type. Okay, we can import and export items as I said and we can also move item to a different type. Okay, so let's let's look at this particular thing.

[45:17] Okay. So when you have multiple processes or multiple applications through which your test case is executing right. So if you want to move a particular item, once it's processed to another application or another process, right. So for example, if we have filled all the test or all the vehicle data here and then while selecting the price option which may be happening at the back end, right.

[45:50] It will require all this information which has been processed or the test data right and you want to send this test data to your next process which is a back end process. So in this case you need to have different types, right. So you'll have a different type for your back end process and different type for your front end process and then you can basically shift or you can move your item from your front end process to your back end process. Okay, so that way you can move your test data from one process to another using this particular module.

[46:28] Okay, so we have to provide existing or new tedious type. Okay, and I'm going to call it vehicle actually we should have basically used the vehicle here because we are trying to move the item from vehicle into a new tedious type or maybe an existing tedious type which you have already created but let's say we have not created and I want to create it. So I'm going to call it price option because that's where the calculation happens.

[47:00] Right. So I want to move this item into this particular tedious type. Right. So you need to provide two tedious types basically both could be existing or one could be new and one could be existing. Okay, and what we need to do here is we need to use the find and provide item and move item because until you don't provide the item this step cannot execute. If you try to execute this step isolated right it will fail because it doesn't have any item in the memory.

[47:38] Okay, so you need to run this find and provide item and then you can move this item to here. So let's go ahead and run this. Okay. So this time also it failed now the reason I'm taking you through all these failures is because you are going to face this issues if you're not careful about how you use these different modules because each module is basically passing data from one step to another right. So it's basically a continuous flow if you don't maintain that flow then you are going to face errors and that's what I'm basically showing you again.

[48:17] You can see here. It is saying no available test data was found. Now if you can guess the reason I have used find and provide item right and in this I'm trying to search for a status new okay, but if you remember in the previous step we already updated this item to used so basically if I go back to my item there is no such status new for any particular record or item right.

[48:48] So that's very logical that the test has failed. Okay. Now if I want to use this particular move item to type either I should change this new to used right or I can run all the steps all together. Okay, so let's go ahead and run this all together and let's see if it passes this time or not right. So this time it passed and now if you look at this particular type or for our repository you will see an additional type has been created which is the price option and that item has now been moved to this particular type.

[49:40] Okay, so this is the or the and it has got the status which is used which is fine and here we already have these different types or items right. So this is how you can use the move item to type and let's look at a final test step. Okay, and that is to how you can delete a particular item. Okay, so test data.

[50:16] Okay, and here is the delete item. So we can delete any particular item and it could be existing alias theme which is your type right. So here it will be the current item not all the items. So don't worry you will not be deleting all the items. Okay, but if I give vehicle right. So what we can do is we can change the find and provide item from new to used so that I can find a particular item which is already used.

[50:55] Okay, and then I can use this to test steps in conjunction so that I find that item and I delete it. Okay, so let's do this and let's go ahead and check this now. Okay, now you see that one item has been removed which was the used item. Okay, so this is a way of cleaning up your data if you don't want to use the test data which has already been used by some process.

[51:33] So going forward you can just remove it from your items so that you can again go through the whole process of creating new test data for your new test execution, right? So this is basically the complete flow. There are some other modules called import items and export items. They are pretty much similar to what we have seen but there is one other module which could be useful as the expert module.

[52:08] Okay, so this has got basically a combination of all your other modules. Okay, so if I look for the expert module. Okay, so this expert module has got a test test data task and in this test data task we have got all the different types or all the different modules which we have used earlier like we can start with create right we can then do a find we can do update we can delete the item we can also do some additional things like we can do or we can assign that item as read-only.

[52:53] Okay, and we can delete type we can delete all which I would not recommend you to use it will delete everything. And we can log the item and log the item we can log the type and unlock the type. Okay, so these few things or tasks are only available with expert module. Okay, so you you can either use these individual modules in your test cases or you can just use the expert module every time if you want to perform all these tasks using this particular module.

[53:31] Okay, it's again the same thing you need to provide a TDS type position is by default one you can put you can also provide a different position. You can provide a data structure to filter your particular item and you can also sort the particular value right, but let's look at an example for an expert module. Okay. So what I'm going to do is I'm going to use the find item here.

[54:02] Okay, or find task basically and then I'm going to use the vehicle again here. Okay, this time around I'm going to use the query. So let me show you the query expression. So this query expression is very simple. Okay, it's like any language or English language right or even if you are familiar with SQL it you can relate to your SQL expressions. Okay, so if you look at this particular type right, we need to first provide a type and then we need to basically give this item name and then the value dot value right.

[54:46] So using this it can find this particular item. Okay. So it's like a filtering the values using a data structure instead of that we can use a query. Okay. So for this we have to start with vehicle and then square bracket. Okay, and then I want to use this make equals equals and BMW. Okay, so this is a simple expression. You can see vehicle and make is BMW.

[55:18] So using this it can filter out this particular item. Okay, and let's go ahead and run this although will not get any output but the test case will pass. Okay, which means it was able to find this particular item. So this is how you can use all the different modules to prepare your or manage your test data inside your test case. Okay, as I said, you can either use all the individual modules or you can use just the expert module to perform all the different steps and also you can perform some additional steps in the expert module right now that we are familiar with all the tedious modules.

[56:02] Now, let's see how we can apply it back to our test cases, right? So if you remember we have our project where we have used the test design sheet. We have used a template to basically prepare different template instances based on the test design sheet, right? So that's the way of designing your test cases and then the test cases were basically referring to the excel sheet which we had or the design sheet from there it was getting all the values based on different conditions and different test cases, right?

[56:39] So that works pretty well, right? We have seen that already now if you want to use this test data in your test cases, right and you can easily integrate this into your project. All right, but what I'm going to do I'm not going to disturb this project because this is already developed right. But what I will do is I'm going to show you how you can basically create or use this test data inside your test case.

[57:10] Okay. So let's go ahead and copy and paste our template. Okay, and this will create another template but what I want to do is I'm going to convert it into a test case. Okay. So this is basically a simple test case. Now it's nowhere linked to any test data sheet. Okay, and what I'm going to tell here is verify mobile automation insurance and then I'm going to append this with TDS.

[57:50] Okay, so this implies that this is using TDS. Okay, and in real time how it will look is you have everything inside your process your test case whatever it is doing right but inside pre-processing what you can do is before even opening the application you can prepare your test data or even after opening the application before you go into the respective fields where you want that this data you can basically prepare your test data.

[58:22] Okay, so here inside pre-processing. Let's create another folder and let's call it prepare test data. Okay, and now inside this prepare test data. I am going to use some of these things which are these modules which we have already developed. Okay, so let's come here and here. And the first one I'm going to copy and paste is the test data create and provide new item.

[58:59] Okay, and then I'm going to do a find and provide item. So let's go here and let's paste it here. Okay, so this will create and provide new item and this will find and provide the item actually we right now. We only require these two. Okay, because after this we are going to use the values whatever this item finds out we are going to use those values.

[59:31] Okay, now inside this right. Okay, so we have got this and so we have got vehicle. I'm just checking if everything is still the same. Okay, we are going to use the status new right now because we have that here. So this too will work fine. Now we need to replace the test data which we have been using from the Excel sheet and we have to replace it with the tedious values.

[1:00:07] Okay, and let me show you how you can do this. Okay. So if you want to enter the vehicle data, this is the data which will be creating in the tedious and that's what we want to use right now instead of this Excel value. Okay, so again start with tedious and then vehicle. Okay. And here we are going to use make similarly here tedious.

[1:00:41] Okay, and vehicle dot engine and here so we are going to let's disable the step or escape the value. Okay, and here again tedious. Vehicle. Dot D O M. So let me fill out all these values quickly.

[1:01:33] Okay tedious and vehicle dot fill and this is the last one which is tedious.

[1:02:17] Vehicle dot mileage. Okay. So these are all the values and let me just cross-check so we have got the list price. Okay, all looks good. So as you can see now we are using all the tedious values which has been provided to us from the previous step, right?

[1:02:48] So now let's go ahead and execute this and we'll see whether this works or not. We are not going to execute the whole test case because we haven't replaced everything right now, right? So you can do that easily you have to just follow the same process. Okay, so let me run the pre-processing and these three steps. Okay, but before running this if remember we need to set the configuration parameter and it is always better you do it at a root level or at a component level.

[1:03:28] Okay, so let's look here where we had this test configuration parameter and let's see if I can copy this two parameters or not maybe and here I am going to paste it. Okay, so the test data point is here and the test repository. Let's come here and paste it here. Okay, so I have the configuration parameters now.

[1:03:59] Let's go back to our test case and let's try to run this again. Okay, so we want to run pre-processing click mobile automobile and enter vehicle data. Okay, so our test passed and you can see now it has entered values from the TDS not from the data sheet which we had prepared or any static values right now where this data comes from is completely dependent on your application like it may be coming from a database.

[1:04:46] It may be prepared by the business analyst or it may be prepared by the manual testing team. Right, so there are different sources from where you can generate test data, but you can do the test data management in TDS using tosca. Okay, now as a final step, let me show you how you can generate a bulk test data with this particular modules. Okay, now until now we have been generating just one single test data item right, whatever values we are providing here, but as I had mentioned earlier, we can randomize all these values.

[1:05:28] Okay, until and unless it is not coming from a drop-down like this make we cannot randomize this because it has to match that particular value from the drop-down but things like this engine right or the seats or the list price the mileage these things can be randomized. Okay, and the way to do is very simple. So use the random method. Okay, which we has used earlier as well.

[1:06:00] So I'm going to give it a random of three. So it always generates three-digit number here similarly for this seats, right? Okay, so I can again randomize this as well. I can put a range but for now it's fine. Okay, I can put a random of one this list price. I can put rnd of maybe four. Okay. And mileage I can again put rnd of maybe three.

[1:06:43] Okay, so you can see that I have put some random values here and this will generate some random data right but not only this what I can do I can also prepare bulk data out of this right not only single data but bulk data and how I can do this. So let's go ahead and disable the step for now. Okay, and this is a folder prepared as data and go to the properties for this particular folder.

[1:07:14] Okay, and if you remember we have got this repetition feature. Okay. So if I give a repetition of 10 okay, so this is going to generate 10 items with different data because I have some random values obviously some values will be fixed but all the other values can be randomized. Okay, and I can prepare 10 items right with this particular module by putting this under a folder and putting repetition.

[1:07:48] Okay, so let's go ahead and run this. Okay, so this is done and you can see the 10 repetitions. Okay, and if I go back now to my TDS. Okay. Now you can see there are 10 different values right or 10 different items in my data type vehicle.

[1:08:25] So this is one way of creating bulk data from the TDS modules. You can put some random value generators and you can generate different test data for your data type right and then you can use it inside your test cases. Okay, so it's a very useful way of doing it. But as I said the data generation can vary and it depends completely on you how you want to generate your test data.

[1:08:56] Okay. But this was all about test data services. It's a very important feature of Tosca because test data management is an important part of any test automation tool or framework.
