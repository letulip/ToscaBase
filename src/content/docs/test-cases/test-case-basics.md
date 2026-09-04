---
title: TestCase basics
description: What a Tosca TestCase is, technical versus business TestCases, how TestSteps are built from Modules, TestStep folders that mirror the business flow, entering values, and a first end-to-end example with WaitOn, Input and Verify.
level: 1
sidebar:
  order: 10
sources:
  - id: TMfn5am9x-c
    title: "Tricentis Tosca Tutorial Part-5 : Tosca Test Case, Tosca Test Case Design and Best Practices"
    url: https://www.youtube.com/watch?v=TMfn5am9x-c
    at: "01:15"
  - id: R5IzSJwGgSc
    title: "TRICENTIS Tosca 16.0 - Lesson 08 | Test Case Automation | Create TestCase Structure |"
    url: https://www.youtube.com/watch?v=R5IzSJwGgSc
    at: "02:04"
  - id: nEcKRePDKa0
    title: "TRICENTIS Tosca 16.0 - Lesson 09 | Test Case Automation | Create Test Steps using Modules |"
    url: https://www.youtube.com/watch?v=nEcKRePDKa0
    at: "01:01"
  - id: ZZ6lWHHHnCg
    title: "TRICENTIS Tosca 16.0 - Lesson 10 | Test Case Automation | Populate TestStep Values for Test Cases |"
    url: https://www.youtube.com/watch?v=ZZ6lWHHHnCg
    at: "04:05"
---

A TestCase is a set of instructions that walks through the application and verifies the result. It is written from the requirements and can be manual or automated; in Tosca an automated TestCase is assembled from Modules (standard and user-defined) plus the test data they need. Modules hold the technical information (how to find each control), the TestCase holds the business information (the sequence of actions), so automating a manual test is four steps: lay out the TestCase structure, add TestSteps from Modules, enter the values, then configure the browser and run. This page covers the object itself; the click-by-click walkthrough of one such test is [First TestCase](/ToscaBase/getting-started/first-test-case/), and which ActionMode to use on each value is the subject of [ActionModes](/ToscaBase/test-cases/action-modes/).

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
3. Add TestSteps from Modules in one of two ways: drag a Module from the **Modules** section onto the TestCase (or onto a TestStep folder in it), or right-click the TestCase or folder, choose **Search and add TestStep** (**Ctrl+T**) and pick the Module by name from the search list. Either way each Module becomes one TestStep whose TestStepValues are the Module's controls, and the same Module can be added as often as needed (one top-menu Module gives the steps that open the login page, open the cart and log out).
4. For each control you need, enter a value in the **Value** column and choose an ActionMode. Controls you do not touch are ignored.
5. Rename each TestStep after the activity it performs (`Navigate to login page`, `Order blue jeans`); not required, but it makes the log readable. Reorder steps by dragging them; **Expand all** on the context menu of a TestCase, folder or TestStep opens every level at once.

:::tip
Group TestCases into folders before you create them. In a shared repository, check out the **TestCases** section (or the folder) first; see [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).
:::

## TestStep folders

TestSteps can be grouped into folders inside the TestCase (right-click the TestCase, **Create folder**), and the folder tree is best written before any Module is dragged in, straight from the manual test. The source builds every TestCase from `Precondition` (open the URL, go to the login page, log in), `Process` and `Post condition` (log out, close the browser), and splits `Process` into one subfolder per stage: `Order product`, `Start checkout`, `Checkout process`, `Verification of prices`, `Confirmation`, `Verification of success`. An empty TestCase structured this way already reads like the manual test; TestSteps are then added folder by folder, and a single folder can be run on its own in the ScratchBook. The left pane shows the tree, the right pane (double-click) is where TestSteps and values are edited. Why folders matter for maintenance is in [TestCase structure](/ToscaBase/best-practices/test-case-structure/#group-teststeps-into-folders); a folder is also the only place a [Repetition](/ToscaBase/test-cases/repetitions/) can be set.

## Entering values

- Type or pick a value in the **Value** column; as soon as a value is entered Tosca sets the ActionMode to `Input`, which is what most steps need. A text field takes the text, a drop-down offers the options XScan captured, a checkbox takes `True`, a button or link takes `X` (a click). An empty value on a clickable control still clicks it under `Input`, but the source recommends `X` so the intent is visible in the step.
- Every TestStepValue also has a **data type**: `String` by default, with `Numeric`, `Date` and others in the drop-down. It matters for verifications, where two equal numbers compared as strings can fail; see [Verify](/ToscaBase/test-cases/action-modes/#verify).
- Modules that identify a window by its title, such as `Close Browser`, take a wildcard (`Demo Web Shop*`) with ActionMode `Select`, because nothing is entered.
- **F9** filters the TestCase to the TestStepValues that have a value; press it again to show every control. Useful in Modules with many attributes of which only a few are used.
- Values can stay empty while the steps are laid out; the source adds all TestSteps first and fills the values in a second pass.

## Workstate

A TestCase has three states: `Planned`, `In Work` and `Completed`. The state is not cosmetic; it feeds requirement coverage figures. When to set which value is explained in [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

:::note
The source calls the first state "planning"; the Workstate column in Commander shows `Planned`. Treat the two as the same value.
:::

## ActionModes at a glance

Every TestStepValue carries an ActionMode that tells Tosca what to do with the value: `Input` enters data or clicks, `Verify` compares a property with the value, `Buffer` stores the control's value under a name, `WaitOn` pauses until a condition holds, `Select` and `Constraint` navigate and narrow down inside tables, `Insert` creates objects in non-UI structures such as XML. Syntax and examples for each are in [ActionModes](/ToscaBase/test-cases/action-modes/).

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

- **Step 1.** The generic **TBox Automation Tools > Process Automation** Module can start any program; for a web application the dedicated `OpenUrl` is the right choice.
- **Step 2.** The `WaitOn` on the Google icon handles synchronisation: the step does not continue until the page has rendered the icon.
- **Step 3.** The static 5 s wait is what the source does for slow search results; Tricentis' best practice is to replace static waits with `WaitOn`, see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).
- **Step 6.** `Close Browser` identifies the window by title; the asterisk in `Tricentis Tosca*` is a wildcard.
- **Browser.** Tosca drives Internet Explorer by default. To run in Chrome, add a Test Configuration Parameter `Browser` on the TestCase and set it to `Chrome`. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

The TestCase is now ready to run from an [ExecutionList](/ToscaBase/execution/execution-lists/) or the ScratchBook.

For reusing TestSteps across TestCases see [Business parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/).
