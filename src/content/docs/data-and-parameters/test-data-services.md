---
title: Test Data Services
description: Tosca's Test Data Services (TDS) register test data centrally on Tosca Server, track its state across processes and share it between applications; how repositories, types and items work in the web interface and which Test Configuration Parameters a TestCase needs to use them.
level: 2
sidebar:
  order: 40
sources:
  - id: Eli2iucdQ_s
    title: "Tosca Tutorial | Lesson 154 - Test Data Management with Tosca | Test Data Services | TDS Modules |"
    url: https://www.youtube.com/watch?v=Eli2iucdQ_s
    at: "00:03"
---

**Test Data Services** (TDS) is the Tosca Server component for test data management: a central store where TestCases register the data they create, look up data that is ready to use, mark it as used and hand it on to the next process. This page covers the concept and the web interface; the TBox Modules that drive TDS from a TestCase are in [Test Data Service Modules](/ToscaBase/data-and-parameters/test-data-service-modules/).

## Why test data management

Creating and storing test data is easy (Excel, a database, XML, JSON, random generators). Managing it is not:

- Each execution needs **unique** data. Registering with the same e-mail address a second time fails because the application already knows it.
- A business process spans **several applications**; the data created by the web front end must flow to the back end and back without manual copying.
- Manual tracking of which record was used in which cycle is slow and error-prone.

TDS answers this with one place to register data after it is created, pick the right data for a run, track and update the **state** of every item through its life cycle, and share items between processes: process 1 creates an item and stores it, process 2 finds it, modifies it and stores it again, process 3 continues.

## Where TDS runs

TDS is installed **with Tosca Server**; nothing extra is needed. Open the Tosca Server landing page (`http://localhost:8080` in the video) and go to **Test Data Management**. The backend is a database: SQLite by default, stored as a `.db` file in a local folder under the Tosca Server program data, or a Microsoft SQL Server or Oracle database for a shared setup. See [Tosca Server](/ToscaBase/administration/tosca-server/).

Everything below can be done in the web interface **or** from Tosca Commander with Standard Modules. The interface is for exploring and maintenance; in a real project the data is prepared by the TestCases themselves before they run.

## Repositories, types and items

TDS has its own **repositories**, unrelated to workspace repositories. A default one, `Data Repository`, exists on first opening. Think in database terms: a repository is a database, a **type** is a table, an **item** is a row, and the columns are the item's attributes.

### Create a repository

1. **Create repository**, enter a **name** without spaces or special characters, for example `TestRepository` or `SampleApp`.
2. Choose the database. **SQLite** creates the file locally; for **MSSQL** or **Oracle** enter server URL, database, user, password and schema, or paste a connection string.
3. **Test connection**; a connected indicator confirms it.
4. Add a description and **Save**. Authorization can be enabled, but that is configured on the Tricentis service configuration side, not here.

:::tip
If **Save** stays disabled, a database file with that name may already exist, or the service needs a refresh: reload the page and test the connection again.
:::

Repositories can be edited (name, description) and deleted; deleting can also remove the linked database.

### Types

Open a repository and **add a type**. How you cut types is up to you: by functionality, by process, by application, by team. A `Users` type with first name, last name, e-mail and so on is a typical example; the video uses `Vehicle` and `Automo` for a vehicle-insurance demo. A type must exist, or be created by a Module, before items can be stored in it.

### Items

Inside a type you can:

- **Import** items from a file (browse or paste), or load Tricentis sample data: pick a category and a sample such as `Names International 500` or `Airlines` and **Add**; the `Users` type then holds about 500 records with name, surname, gender, region. JSON is shown; other formats are not demonstrated.
- **Add item**: a new row appears, fill the attributes and click elsewhere to commit.
- **Lock / unlock** a row so no other process can take it while it is in use.
- **Delete** a row.
- **Export** the type to CSV, Excel or JSON, choosing encoding, line break and separator, and import the file into another type.

## Prerequisites in Tosca Commander

Before any TDS Module executes, the TestCase must see two Test Configuration Parameters, otherwise the step fails:

| Parameter | Value |
|---|---|
| `TestDataEndpoint` | The server address followed by `/testdataservice`, with the port if it is not the default (the value is pre-filled, adjust the host and port) |
| `TestDataRepository` | Name of the TDS repository, for example `SampleApp` |

Create them under the project's **Configurations** (a `Test Data Service` configuration is among the defaults) or in the **Test Configuration** tab of the folder that holds the TestCases; a root or component level is best so every TestCase inherits them. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

:::note
The path is only read out as "slash test data service" and the port is never stated (only that it is not the default); `/testdataservice` follows the pre-filled value the speaker keeps. Check the pre-filled value in your installation.
:::

## Reading TDS values in TestSteps

Once a Module has *provided* an item (see the Modules page), any TestStepValue can read its attributes with `{TDS[type.attribute]}`, for example `{TDS[vehicle.engine]}` or `{TDS[vehicle.status]}`. Tosca highlights a correctly written expression; if it is not highlighted the syntax is wrong. Use it directly as the `Input` value of the fields the data belongs to, or copy it into a buffer with `TBox Set Buffer` to see it in the log.

## Related

- [Test Data Service Modules](/ToscaBase/data-and-parameters/test-data-service-modules/): create, find, update, move and delete items from a TestCase
- [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)
- [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/): the TestCase-Design alternative for static data
