---
id: "J24QB9a78hY"
title: "Tosca Tutorial | Lesson 155 - Steering Table Controls | Table Structure | Table Properties | Example"
url: "https://www.youtube.com/watch?v=J24QB9a78hY"
channel: "QASCRIPT"
playlist: null
playlist_index: null
duration: 1351
upload_date: "20250606"
source: "whisper:medium"
language: "en"
transcribed_at: "2026-09-04T11:56:18Z"
status: "raw"
---

# Tosca Tutorial | Lesson 155 - Steering Table Controls | Table Structure | Table Properties | Example

[00:08] Hey there. In this particular session, we are going to talk about how to steer tables using Tosca. But first we'll understand what a table is and how it is structured in Tosca. So what are the different column and row attributes which you can use to steer different elements inside the table. And then we'll talk about the different action modes. And then we'll also look at some of the examples through which you can steer different elements inside a table in different ways using the methods which are available in the Tosca TBox module.

[00:47] So let's start with the basics, which is what is the table structure. So this particular image, it shows you a typical table when you create a module for a table and then you pull it into the Tosca TBox test case. Then this is the step where you will see that it has got a table. And then it has typically got rows and columns. So a table structure generally consists of two attributes, which is the column and the row.

[01:22] Then each row or column could have several cells and these cells then have different attributes. So there are basically three parts to a table. So one is the row, then a row will have several cells. Then there is a column which will also have several cells. So let's look at some of the attributes which can be used here. So whether it is a row or a column or a cell of a particular table.

[01:57] So using this $1, you can basically steer the first row or the first column or the first cell of a particular table. Similarly, you can steer any row, any column or any cell position using this $ sign with the particular number. So if I give $2, it will do the second row. If I give $3 for a column, it will steer the third column.

[02:29] And if I give the fourth cell, then it will steer the fourth cell. So it basically steers the specified row, column, cell position which you give in your test case. Then there's another attribute called $last. Now this basically steers the last row or column or the cell of the table. Then we have also got the $header. Now this will steer a cell in the table header.

[03:02] Then we have got the last content row which steers the last table row with value. And then the first empty row which will basically steer the first table row without a value. So as you can see, there are multiple options here. And these are provided by Tosca so that you can easily steer different elements on the table using different properties basically. So whether it is based on the position or whether it is based on the header or whether it is based on some content which is present or it's empty.

[03:42] So all the conditions are provided here and you can use this to steer different cell attributes. So now coming to different action modes which are present in the table. Now we have got four different action modes. Now these are pretty common to other objects as well. But for a table, we have got the input action mode using which we can enter a particular value. And then we have got the verify using which we can verify a value or a property.

[04:15] And then we have got the constraint. Now this will basically restrict your search within the table. So you can define a constraint on a particular column, on a particular row or on a particular cell. Then we have got the buffer. So this will basically buffer the value of a cell, row or column and then store it in a buffer variable. So all these action modes can be used when you are steering any particular table.

[04:47] Now let's talk about some of the general properties which are part of a table control. And then these properties can be used to perform different operations. And let's look at all of these. So we have got the column count. Now this will give you the number of columns in the table. We have got the row count which will give the number of rows in the table. We have got column number and row number. Now this is basically the index of the selected column or row. And this is obviously relative to the header column or row.

[05:20] Then we can also use the property row column number to get the index of the selected column. Similarly for the row we can use the row number which will provide the index of selected row. Now you will see a difference. Both seem pretty similar. Column number and row column number. But here the difference is the header column which starts at 0 for column number. But if you want to start at 1 then you can use the row column number.

[05:55] Then we have got the result count. Now this will return us the number of cells which contains the specified content. This will further help you to perform certain operations. Like if you want to get the total number of columns or total number of rows. Or you want to select a particular column or a row. Or you want to get the number of cells with specified content. So all of this can be done using this table properties. So now we have discussed the action modes, the properties and the table structure.

[06:28] Let's look at some examples of how we can steer a particular table using all of this. And then we can basically automate our scenarios in a particular table. So for this particular session we are going to use this particular table. It's part of the main obstacle page. And this is how a typical table looks like. So we have got the rows and we have got the columns and then we have got the cells. Inside those cells we have got some values.

[07:00] And then we need to steer this particular table to automate our scenarios. So let's go back to Tosca. And here I have already scanned this particular module here as you can see. So this is the obstacle list control. And it has got a table which has got different rows and columns. And then in the properties section if you go to the table you will see we have also got the header row.

[07:31] So we can also define our own header row. So we just need to change this value. If it is not the first row then we can define it anything here in the properties. So we can change that. So as you can see the tag type is table which means it is a table control. So let's go ahead and create a new folder here. And I'm going to call this steer tables.

[08:03] Inside this let's create a test case. And let's call this table steering. And then inside this we are going to pull our obstacle list module. So which will contain the table as you can see. So now let's look at our first example which is to select a particular row with a fixed position. Now what do I mean is if we know the position of a particular row and we want to select a particular row or a particular value in a particular row.

[08:43] So what I mean is if we already know the row number which is fixed and it is not going to change then we can use this method to select any particular value here. So for example I want to verify whether the name of this third row is not a table. So under the name this is the value. So what I will do is I'm going to copy this particular thing here. And then I'm going to come back here and here we are going to select this dollar with any particular number here.

[09:23] And we are going to select the row number three here. Okay. And then we are going to select the particular cell. So it is under the name. Right. And here we are going to give it a value. So let's go ahead and give it a value. And I've already copied that. So this is the value not a table. So we can go ahead and execute this now.

[09:56] Okay so now in the scratch book if we look the test step has passed. And here if I go further into the table you can see it selected the third row. And then it went into this particular cell under the column which is the name column. And then it verified the value. Right. So this is pretty simple and easy. If you already know the row number and it is not going to change then it's pretty straightforward.

[10:28] Right. Now let's look at our second scenario. And here we are going to select a row by using some values which are in specific cells. So here we don't know the row number but we know that there are some values in particular cells using that. We will select or verify some other value in that particular row. Okay. So let's go ahead and do that. So this I'm going to call this fixed position.

[11:02] Okay. And then let's go ahead and add another step here. So I'm going to drag this again. And here we are going to call this specific cell value. Okay. So now let's look at an example of what we can do here. So now based on these particular values here right.

[11:34] So we have got ID and we have got a name. So either we can use one or we can use both of them. And I want to verify the category. Okay. So let's take this fun with tables and then we want to verify the categories hard. Okay. So either we can put a constraint on this name or we can put a constraint on the ID or we can use both. So let's work out with just one constraint and then let's try to select a particular value.

[12:06] So here either you can use the ID or I can use the name. Since it is unique, I can go ahead and use the name here. So I'll come back here. I will go to a particular row. I will select the cell here and I'm going to use the name. I'll put the value here. Now instead of verify, I'm going to put a constraint here. Okay. So this is the way of basically filtering out your search based on some value. So Tosca will search for this value in all the rows and wherever it finds it, it will select that particular row.

[12:40] Right. So that's how this particular logic works. Now we want to see whether the category is basically what is the expected category here, which is hard. Right. So based on this constraint, it will select the row and then it will select a particular cell and then it will verify the value. That's what it is going to do here. So let's go ahead and run this. Okay. So in the scratch book, now you can see if you drill down the table, it has selected that particular row based on the constraint.

[13:17] And then it is verifying that particular cell value, which is hard. Okay. So that's our second scenario. So selecting a row based on a particular cell value. Now, the next one is pretty similar to this. Okay. But instead of constraint, if we know that a particular value is kind of unique in that particular table or in all the rows, then we can directly use the row value instead of selecting a constraint.

[13:50] Because the constraint, it will take some time. If you have got a large table, Tosca will take some time to filter out that results based on that particular constraint. But if you know that that particular value is unique across all the rows, then you don't need to use the constraint. Right. So I'm going to pull this table here. And then inside this row, we can directly put a value here. Right.

[14:20] So let's try with this one, or let's try with this one, since it's a different category. So we'll use this wait a moment value. Now, as you can see, it's unique across all the rows. If it's not, then it will not work. In that case, you have to use two constraints instead of one. Right. So here, the row value is wait a moment.

[14:50] Now, based on this, it will select a row. Okay. And then we can verify any particular value here. So if you want to verify the category, then we can just fill the value here. So its category is easy. We can also verify all the other values for this particular row. So the main challenge is to find the particular row or column where you want to do a verification for a particular cell value. So the first step always remains the same.

[15:22] You need to select the particular row and column based on some search criteria. Right. So now we can go ahead and execute this. Okay. And as expected, this also passed. If you drill down again, you will see the verification was successful. Okay. So this is another way of doing it. So this is based on a particular row value. So we can say specific row value.

[15:59] So let's move on to our next scenario. In this, we are going to select a particular cell by index. Okay. So let's go ahead and add another module here. So we'll drag this and we will name this select cell by index. And what we are going to do is we are going to select this particular row, which is the second row here, based on the category value, which is easy.

[16:29] Now this is common across both the rows. So we are telling Tosca to select the second row, which contains the value category as easy. Right. And we'll use a constraint to basically filter out these rows and then we'll select the second index, which is the second row, but the same value. Right. So here in the row, instead of dollar, we are going to use something called hash symbol. And then we are going to use the two, which is the index two.

[17:00] Inside this, we are going to use the dollar symbol and we are going to say the second cell, but this will be a constraint and the constraint would be the category, which is easy. Right. Actually, it is the third cell, not the second. And then here we will choose the second one and and we will verify the name, which is twins.

[17:34] Okay. And then let's go ahead and execute this. So as you can see, the test passed. And if you drill down again, you can go into the login for where you can see the expected and the actual value. So this is how you can select any particular cell by using the index. Right. So let's move forward and let's try to use some other properties, which could be useful in some scenarios, like getting the count of the number of rows or the columns or selecting any particular cell.

[18:07] So let's go ahead and add another module here and let's calculate or let's verify the row count of a particular table. And that we can do using the property which we already discussed, which is the row count. So here in the value of the table, we can put down the property name, which is row count, and then the value. For example, this is 12 and I'm still looking at the same table.

[18:40] And instead of select, we will change this to verify. Okay. So this verification will be done directly at the table control level. So let's go ahead and try to run this. Okay, as you can see in the scratchbook results that the value has been verified, and it was a success. Obviously will not get anything in the login for like other verifications, but it has done this verification.

[19:12] So, similarly, you can also do the column count here. Okay. And let's change the value to 10. I haven't counted the number of columns here, so it might fail. But we will see if it fails or passes. Okay. So expectedly it failed. The reason is this particular table has got around nine columns, right?

[19:45] So, but we can use these properties to verify the row and column count. So let me change this step name to row column count. Okay. And let's move on. Obviously I can correct this and I can rerun this always. Okay. And it should pass the second time around. So the next thing which we can do is saving the value of a particular cell to a buffer.

[20:21] So for that, again, we'll add the module here. Okay. So here what we will do is we will select a particular column. So let's choose maybe the name. Okay. And then we will choose a particular cell number. Right. So let's choose anything. Let's choose five. We don't know what kind of what cell value it has, but I want to buffer this and I want to save this. Right. So I'll choose the text property here.

[20:54] Okay. Then I will save it to some B underscore name. So this is the buffer name. So if it is able to select this and then it is able to get that text value, it will save it in this particular buffer. So let's go ahead and run this. Okay. So as you can see, the test has passed. And let's see what value it is stored in this particular buffer. So B underscore name has got the value fun with tables.

[21:28] Right. And if I look at my table, this is the fifth one, which is fun with tables. So I can buffer out any particular value from this particular table using this particular method. Okay. And if you want to see the buffer as well, so it will be available in the buffer viewer. Okay. So these are some of the different operations which you can do using different properties and different methods which are present in Tosca.

[22:00] This is part of the dbox table control. And once you add that control, then you will have access to all these properties. And using different action modes along with the properties and the attributes, you can basically steer any table and any cell or any column or row.
