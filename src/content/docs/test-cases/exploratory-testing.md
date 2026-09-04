---
title: Exploratory testing
description: Tosca's exploratory testing support - explorative sessions, recording an interaction with the Explorative Scenario Manager, and exporting the resulting scenario document with screenshots to PDF or DOCX.
level: 1
sidebar:
  order: 70
sources:
  - id: VZDh9N5WjMQ
    title: "Tosca Tutorial | Lesson 76 - Record & Create Exploratory Testing Scenario Document |"
    url: https://www.youtube.com/watch?v=VZDh9N5WjMQ
    at: "01:08"
---

Exploratory testing is simultaneous learning, test design and execution: there are no predefined TestCases, the tester probes the system on the fly to find the bugs that scripted tests miss. It is ad hoc, but not random. Tosca supports it with **explorative sessions** that plan and time-box the work, and a recorder that turns a session into a step-by-step **scenario document** with screenshots, exportable to PDF. That document is useful well beyond exploratory testing: as a bug report for a developer, as a walkthrough for a new team member, or as the basis for questions to a business analyst.

## Explorative sessions

1. In the **Execution** section expand the **Exploratory Testing** folder.
2. Its context menu offers **Create explorative session**, **Create folder**, **Import results file** and **Import results from session ID**. Choose **Create explorative session**.

A session carries the planning data for one round of exploration:

| Field | Purpose |
|---|---|
| Exploratory testers | Who takes part |
| Issue proposals | Issues raised during the session |
| Scenario link and description | What the session is about |
| Session schedule | Time box from a start to an end time |
| Session owner | The administrator of the session |
| Status | `Planned` at creation; later passed or failed |
| Scenarios, duration, objects, email | Counters and contact details filled as the session runs |

## Recording a scenario

The core of a session is the scenario document, created with the **Explorative Scenario Manager**.

1. Open the Explorative Scenario Manager from the session and click **Explorative scenario** on its top bar.
2. Choose the application type to record; for a web application choose **Chrome**. Click **Start**.
3. Interact with the application: open a page, fill in fields, choose drop-down values. Every interaction is captured in the background.
4. Click **Stop**. Tosca builds the scenario document.

The document is a media document: on the left, the **scenario steps** as text (for example *click on Automobile*, *click the drop-down and select the value*); on the right, a screenshot of the whole screen for each step with the interaction annotated. Someone who has never seen the application can follow it step by step and mark each scenario as passed or failed.

Use **Save and close** to store the scenario in the session and move on to the next one.

## Exporting the document

The session document can be exported as **DOCX** or **PDF**; the speaker recommends PDF.

1. Choose the export and tick what to include: **steps and step values**, extra columns (**actual result**, **ActionMode**, **action property**), **media** (included by default) and the **page setup**.
2. Pick a target folder and click **OK**.

The exported PDF contains more than what was recorded:

- **Summary**: name, overall result, number of failed steps, number of steps.
- **Scenario description** with every step.
- **Media**: the screenshots in sequence, which read like a video of the interaction.
- **System information**: operating system, screen resolution and other details of the machine, useful when reproducing an issue.
- **Recorded applications** with their versions.

## Recorder or exploratory testing?

Both record what you do in the application, but for different outputs. The [Recorder](/ToscaBase/test-cases/recorder/) generates Modules and an executable TestCase; the Explorative Scenario Manager generates a human-readable document with screenshots and no automation objects. Use the first to automate, the second to document, report or hand over.

:::note
The source covers only explorative sessions, recording and export. The speaker mentions that the exploratory testing area has further options and leaves them for later; they are not documented here.
:::
