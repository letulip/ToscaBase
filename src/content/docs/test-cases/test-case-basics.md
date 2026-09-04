---
title: TestCase basics
description: What a Tosca TestCase is, technical versus business TestCases, how TestSteps are built from Modules, and a first end-to-end example with WaitOn, Input and Verify.
level: 1
sidebar:
  order: 10
sources:
  - id: TMfn5am9x-c
    title: "Tricentis Tosca Tutorial Part-5 : Tosca Test Case, Tosca Test Case Design and Best Practices"
    url: https://www.youtube.com/watch?v=TMfn5am9x-c
    at: "01:15"
---

A TestCase is a set of instructions that walks through the application and verifies the result. It is written from the software requirements and can be manual or automated; in Tosca an automated TestCase is assembled from Modules (standard and user-defined) plus the test data those Modules need. This page covers the object itself: the two kinds of TestCase, how TestSteps come from Modules, and a complete first example. Which ActionMode to use on each value is the subject of [Action modes](/ToscaBase/test-cases/action-modes/).

## Technical and business TestCases

| Kind | What it holds | Executable |
|---|---|---|
| Technical TestCase | All the technical information needed to steer controls: TestSteps, TestStepValues, ActionModes | Yes |
| Business TestCase | A logical group of technical TestCases representing one piece of functionality, designed from the requirements | No, it is used to monitor test coverage |

Everything below is about technical TestCases. Business TestCases are covered with ExecutionLists in [Execution repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/).

## Creating a TestCase

1. In the **TestCases** section, right-click a folder and choose the create-TestCase icon (the blue circular arrow), or press **Ctrl+N** followed by **Ctrl+T**.

:::note
The chord **Ctrl+N**, **Ctrl+T** (two keys in sequence) creates a TestCase; **Ctrl+T** on its own, inside a TestCase, opens the search for adding a TestStep from a Module.
:::
2. Give the TestCase a logical name. The new TestCase is empty: it has no TestSteps yet.
3. Drag a Module from the **Modules** section onto the TestCase. Each dragged Module becomes one TestStep whose TestStepValues are the Module's controls.
4. For each control you need, enter a value in the **Value** column and choose an ActionMode. Controls you do not touch are ignored.
5. Rename each TestStep after the activity it performs (for example `Open Google`, `Search Tricentis Tosca`). Renaming is not required but makes the log readable.

:::tip
Folders are optional but recommended: group TestCases logically before you create them. In a shared repository, check out the **TestCases** section (or the folder) before creating anything in it. See [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).
:::

## Workstate

A TestCase has three states: `Planned`, `In Work` and `Completed`. The state is not cosmetic; it feeds requirement coverage figures. When to set which value is explained in [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

:::note
The source calls the first state "planning"; the Workstate column in Commander shows `Planned`. Treat the two as the same value.
:::

## ActionModes at a glance

Every TestStepValue carries an ActionMode that tells Tosca what to do with the value:

- `Input` enters data or performs a click.
- `Insert` creates objects in non-UI structures (XML, for example).
- `Verify` compares a property of the control with the value; the value holds the condition.
- `Buffer` stores the control's value in a named buffer.
- `WaitOn` pauses execution until the condition in the value is satisfied (synchronisation).
- `Select` navigates hierarchy levels to reach child items, typically table rows and cells.
- `Constraint` restricts a search to items with a particular value, mostly in table columns.

The full reference, with syntax and examples for each, is [Action modes](/ToscaBase/test-cases/action-modes/).

## Worked example: Google search

The scenario: open Google in Chrome, search for *Tricentis Tosca*, open the first result, verify that the Tricentis site appeared, close the browser. Three user-defined Modules already exist (Google search screen, search results screen, Tricentis portal), each containing only the controls needed; see [XScan](/ToscaBase/modules/xscan/) for how they were scanned.

| # | TestStep | Module | Values and ActionModes |
|---|---|---|---|
| 1 | Open Google | `OpenUrl` (standard Module, **TBox XEngines > HTML**) | URL `www.google.com`, `Input` |
| 2 | Search Tricentis Tosca | Google search screen | Google icon: `Exists` = `True`, `WaitOn`; search field: `Tricentis Tosca`, `Input`; search button: click, `Input` |
| 3 | Pause | `TBox Wait` (standard Module) | `5000` (milliseconds) |
| 4 | Open first result | Search results screen | first result link: click, `Input` |
| 5 | Verify Tosca official portal | Tricentis portal | logo: `Exists` = `True`, `Verify` |
| 6 | Close browser | `Close Browser` (standard Module) | title `Tricentis Tosca*` |

Notes on individual steps:

- **Step 1.** The generic **TBox Automation Tools > Process Automation** Module can start any program, but for a web application the dedicated `OpenUrl` Module is the right choice; the source first drags the generic one, then replaces it.
- **Step 2.** The `WaitOn` on the Google icon handles synchronisation: the step does not continue until the page has rendered the icon.
- **Step 3.** The speaker adds a static 5 s wait because search results can be slow on a poor network. This is what the source does, but Tricentis' own best practice is to replace static waits with `WaitOn`; see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).
- **Step 6.** `Close Browser` identifies the window by title. The asterisk is a wildcard: `Tricentis Tosca*` matches any title starting with that text.
- **Browser.** Tosca drives Internet Explorer by default. To run in Chrome, add a Test Configuration Parameter `Browser` on the TestCase and set it to `Chrome`. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

The TestCase is now ready to run from an [ExecutionList](/ToscaBase/execution/execution-lists/) or the ScratchBook.

## Where to go next

- [Action modes](/ToscaBase/test-cases/action-modes/) for each ActionMode in depth.
- [TestCase structure](/ToscaBase/best-practices/test-case-structure/) for folders, verification points and Workstate.
- [Business parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/) for reusing TestSteps across TestCases.
