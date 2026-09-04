---
title: Agentic test automation
description: Tosca Agentic Test Automation in Tricentis Tosca Cloud - what it is, how an agent turns plain-English steps into Modules, a TestCase and a run, what you need before it works, and the limits stated in the source.
level: 1
sidebar:
  order: 90
sources:
  - id: RH2F4nkOj64
    title: "Tosca Agentic Test Automation Explained | AI Agents Write Test Cases from Plain English"
    url: https://www.youtube.com/watch?v=RH2F4nkOj64
    at: "02:26"
---

**Tosca Agentic Test Automation** is a feature of **Tricentis Tosca Cloud**, the browser-based edition of Tosca reached at `https://<organisation>.my.tricentis.com`. An AI agent reads test steps written in plain English, drives the application, creates the **Modules** for every control it touches, assembles the **TestCase** with TestSteps, values and verifications, saves it and runs it. Everything else in this knowledge base is built in the desktop Tosca Commander; the objects are the same (Module, TestCase, TestStep, TestStepValue), only the way they are produced changes. This page follows the source lesson, which was recorded on a 14-day trial.

## Traditional versus agentic

| Without the agent (Commander or Tosca Cloud) | With Tosca Agentic Test Automation |
|---|---|
| 1. Scan the controls of the application into Modules and save them | Write the test as numbered plain-English steps |
| 2. Create the TestCase | The agent does steps 1 to 6 |
| 3. Add TestSteps that map to the Modules | |
| 4. Enter the TestStepValues for each step | |
| 5. Run the TestCase and debug it | |
| 6. Read the results | |

The lesson demonstrates the left column first in Tosca Cloud (**Build > All assets**, **Module scan** opening XScan through the launcher, **New test case**, adding the scanned Modules from **User assets**, typing the vehicle data by hand) to show how many manual actions the agent removes.

## Getting access

1. Request the **14-day free trial** of Tosca Agentic Test Automation on the Tricentis site: business email, first and last name, country, phone, job title, and consent to marketing communications, then **Request trial**.
2. A mail arrives; its link opens Tricentis Tosca Cloud and asks for an **organisation name**. That name becomes your URL, `https://<organisation>.my.tricentis.com`.
3. On the first click on the **Tosca Agentic Test Automation** icon, enter the organisation name, then the username and password created during registration.

The cloud workspace opens with a quick start guide.

## Prerequisites

The agent runs in the cloud, but the application under test runs on your machine, so local components are required:

- A **Windows** machine.
- The **launcher**, a small application downloaded from Tosca Cloud that installs everything needed to steer local applications; it also opens XScan for a manual scan.
- The **Tricentis automation extension for Chrome**, mandatory for any web application (see [Tosca Automation Extension](/ToscaBase/getting-started/tosca-automation-extension/) for the desktop equivalent).
- A **local agent** registered under **Agents** in Tosca Cloud (the lesson uses a personal agent on the presenter's laptop). Runs started in the cloud are executed through it.
- The application open in a browser window before you start; the lesson uses the Tricentis **vehicle insurance** sample application in Edge.

## Generating a TestCase from plain English

1. Prepare the steps. The lesson keeps them in a text file: the application URL; click **Get a quote**; select make `Audi`; enter engine performance, date of manufacture, number of seats, fuel type `Diesel`, payload, total weight, list price, license plate and annual mileage; click **Next**; check that the *First name* field is visible; check that the *Last name* field is visible. Fifteen lines in all.
2. On the Tosca Cloud home page click **Tosca Agentic Test Automation**, then **Generate a test case**.
3. Choose the Module technology: **TBox** or **Vision AI**. Until recently the agent produced only Vision AI Modules; it now creates TBox Modules too, which are the better choice for maintenance. The lesson picks TBox.
4. **Continue** and **Open launcher**. The launcher initialises the *TBox inspection agent* (or the Vision AI agent) and lists the open application windows; select the one with the application. The agent's prompt window appears on the left, the application on the right.
5. Enter the steps directly in the chat, or **attach** the prompt file. Choose the mode:
   - **Co-create**: the agent asks for approval and puts questions to you at each step.
   - **Autonomous**: the agent works through the steps on its own.
6. Type a one-line goal (the lesson uses *Get a quote for insurance*) and press Enter. The agent reads the file line by line, opens the URL, clicks, fills the fields, creates a Module for the controls of each page and performs the visibility checks. A notification asks you to return to the automation window when it has finished.
7. Click **Save test case**. If the workspace already has Modules you can reuse them; otherwise choose **Keep new modules**. The TestCase and its Modules are sent to Tosca Cloud and a link to the new TestCase is shown.

Under **Build > All assets** the workspace now holds the generated Modules (two, one per page) and the TestCase `Get insurance quote vehicle data` with its TestSteps. The Modules' properties are TBox properties, not Vision AI ones.

## Running it

Open the TestCase, set the `Browser` parameter (the lesson uses `Edge`; new parameters are added in the same place), and **Run**. The local agent replays the steps in the browser. **View last run** shows every TestStep with status *Passed*.

## Limits as stated in the source

- The trial lasts 14 days and needs a business email.
- The launcher, the Chrome extension and a local agent must be installed and registered; without the launcher the agent cannot open the application.
- The demonstrated scenario is a single 15-step flow with two visibility checks; the presenter defers more complex end-to-end cases to a later lesson.
- TBox support in the agent is recent; earlier only Vision AI Modules could be generated.

:::note
The lesson does not show how the generated TestCase can be edited afterwards, how the agent handles controls it cannot identify, or how the cloud workspace relates to a desktop Commander workspace. Treat these as open questions rather than gaps in the product.
:::
