---
title: Reports and report definitions
description: Export any section with Print View, print the built-in report definitions for ExecutionLists, TestCases and requirements, and create your own report definition with a data set, a TQL query and a designer.
level: 3
sidebar:
  order: 30
sources:
  - id: epE3kZJjoP0
    title: "Tosca Tutorial | Lesson 72 - Generate Reports and Create Report Definitions | Reporting |"
    url: https://www.youtube.com/watch?v=epE3kZJjoP0
    at: "00:08"
---

Tosca offers three levels of reporting. **Print View** dumps whatever is on screen into a document in seconds. The **Reporting** section ships default report definitions that turn an ExecutionList, a set of TestCases or a requirement set into a formatted report with a summary, a pie chart, logs and screenshots. And a custom **report definition** lets you choose exactly which objects (through a TQL query) and which layout (default designer, XML or Excel) go into the document.

## Print View: the quick snapshot

1. Select the object or folder and expand what you want to see (for example an ExecutionList with all entries open).
2. Click **Print View**, choose a format: PDF, Word, Excel or HTML.
3. Click **Start**. Tosca generates the file and opens it (HTML opens in the browser).

The result is an exact snapshot of the Commander view, not attractive but immediate. It works in every section, including the [requirements dashboard](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

## The Reporting section and default definitions

If the **Reporting** section is not visible, open it from the **Sections** menu **> Reporting**. It lists the default report definitions and data definitions provided by Tosca:

- ExecutionList reports: **Execution entries with actual log** and **Execution entries with detailed logs**.
- A requirements report.
- A TestCase report.

Each is a report definition (layout) plus a data set definition (which objects to fetch).

### Print a default report

1. Right-click an ExecutionList, an ExecutionList folder, a TestCase folder or a requirement set **> Print Report**. Only the definitions matching that object type are offered.
2. Pick a definition, e.g. **Execution entries with detailed logs**. The print dialog opens again, but the output now follows the definition rather than the screen.
3. Click **Start**, save the file, and answer the prompts: whether to show only failed items (answer No to include everything) and whether to include screenshots (Yes).

The report contains a header with the Tricentis logo (replaceable in the Reporting section), the creation date, a summary with a pie chart (for example 19 TestCases: 3 passed, 14 no result, 2 failed), then one block per ExecutionList and entry with every TestStep, start and end time, who executed it, the log, and a screenshot wherever a step failed. It works equally for a single [business TestCase](/ToscaBase/execution/execution-repetitions-and-business-test-cases/) and for a whole [ExecutionList](/ToscaBase/execution/execution-lists/) folder.

:::note
The subtitle for the first prompt reads "only field stations"; it is most likely "only failed TestSteps". The speaker answers No.
:::

## Create your own report definition

1. Right-click the **Reporting** folder **> Create Report Definition**. The new definition carries an exclamation mark: it is not configured yet.
2. **Assign a data set definition and object type.** Drag an object of the type you want to report on (an ExecutionList, a TestCase, a requirement, a Module) onto the report definition. The link sets the definition's object type, e.g. `ExecutionList`. The exclamation mark stays because a designer is still missing.
3. **Create a designer definition.** Right-click the definition **> Create Designer Definition** and choose one of three:
   - **Default**: opens the report in the Report Designer, a bundled third-party tool where you edit texts, headers, footers and the logo.
   - **XML report**: an XML document with all generated information.
   - **Excel report**: a Microsoft Excel worksheet per data definition.

   With a designer assigned the exclamation mark disappears. The result now resembles the built-in "Execution entries with actual log" definition.
4. **Tell the data set which objects to fetch.** The object type alone is not enough. Create a further data set definition and give it a [TQL query](/ToscaBase/requirements-and-reporting/tql-and-virtual-folders/) that finds the objects in the workspace. Either type the query into the **TQL query** column (add it through the **Column Chooser** if hidden), or build it from the fields **Link**, **Object type** and **Constraint**. For example: link `SubParts`, object type `ExecutionList`, constraint `Name=="End to end scenario"`. Tosca assembles the TQL query as you fill in the fields.
5. Right-click the target object **> Print Report** and pick your definition.

:::tip
For an ExecutionList, a TestCase folder or a requirement set the default definitions are usually good enough. Build a custom definition only when you need a specific selection of objects (via TQL or a [virtual folder](/ToscaBase/requirements-and-reporting/tql-and-virtual-folders/)) or a branded layout.
:::
