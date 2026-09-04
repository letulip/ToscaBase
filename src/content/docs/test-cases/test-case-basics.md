---
title: TestCase basics
description: What a Tosca TestCase is, technical versus business TestCases, TestSteps from Modules, TestStep folders, entering values, configuring the browser and running, and a first end-to-end example.
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
  - id: SLWKhb4igB0
    title: "TRICENTIS Tosca 16.0 - Lesson 11 | Test Case Automation | Run your First Automated Tests | TCP |"
    url: https://www.youtube.com/watch?v=SLWKhb4igB0
    at: "05:55"
---

A TestCase is a set of instructions that walks through the application and verifies the result. Written from the requirements, an automated TestCase in Tosca is assembled from Modules (standard and user-defined) plus the test data they need. Modules hold the technical information (how to find each control), the TestCase holds the business information (the sequence of actions), so automating a manual test is four steps: lay out the TestCase structure, add TestSteps from Modules, enter the values, then configure the browser and run. This page covers the object itself; the click-by-click walkthrough is [First TestCase](/ToscaBase/getting-started/first-test-case/), the ActionModes are in [ActionModes](/ToscaBase/test-cases/action-modes/).

## Technical and business TestCases

| Kind | What it holds | Executable |
|---|---|---|
| Technical TestCase | All the technical information needed to steer controls: TestSteps, TestStepValues, ActionModes | Yes |
| Business TestCase | A group of technical TestCases representing one functionality, designed from the requirements | No; used to monitor coverage |

Below, technical TestCases only; business TestCases are in [Execution repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/).

## Creating a TestCase

1. In the **TestCases** section, right-click a folder and choose the create-TestCase icon, or press **Ctrl+N** followed by **Ctrl+T**.

:::note
**Ctrl+N** then **Ctrl+T** creates a TestCase; **Ctrl+T** on its own, inside a TestCase, opens the search for adding a TestStep from a Module.
:::
2. Give the TestCase a logical name. It is empty until TestSteps are added.
3. Add TestSteps from Modules: drag a Module from the **Modules** section onto the TestCase (or a TestStep folder in it), or right-click the TestCase or folder, choose **Search and add TestStep** (**Ctrl+T**) and pick the Module by name. Each Module becomes one TestStep whose TestStepValues are the Module's controls; the same Module can be added as often as needed.
4. For each control you need, enter a value in the **Value** column and choose an ActionMode. Controls you do not touch are ignored.
5. Rename each TestStep after the activity it performs (`Navigate to login page`, `Order blue jeans`) for a readable log. Reorder steps by dragging them; **Expand all** (context menu) opens every level at once.

:::tip
Plan the folders first. In a shared repository, check out the **TestCases** section (or the folder) before creating; see [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).
:::

## TestStep folders

TestSteps are grouped into folders (right-click the TestCase, **Create folder**); write the tree from the manual test before any Module is dragged in. The source builds every TestCase from `Precondition` (open the URL, go to the login page, log in), `Process` and `Post condition` (log out, close the browser), and splits `Process` into a subfolder per stage (`Order product`, `Start checkout`, `Checkout process`, `Verification of prices`, `Confirmation`, `Verification of success`). Such a skeleton already reads like the manual test; TestSteps are added folder by folder, and a folder can be run on its own. Why folders matter for maintenance is in [TestCase structure](/ToscaBase/best-practices/test-case-structure/#group-teststeps-into-folders); a folder is also the only place a [Repetition](/ToscaBase/test-cases/repetitions/) can be set.

## Entering values

- Type or pick a value in the **Value** column; as soon as a value is entered Tosca sets the ActionMode to `Input`, what most steps need. A text field takes the text, a drop-down offers the options XScan captured, a checkbox takes `True`, a button or link takes `X` (a click).
- Every TestStepValue also has a **data type**: `String` by default, with `Numeric`, `Date` and others in the drop-down. It matters for verifications, where two equal numbers compared as strings can fail; see [Verify](/ToscaBase/test-cases/action-modes/#verify).
- Modules that identify a window by its title, such as `Close Browser`, take a wildcard (`Demo Web Shop*`) with ActionMode `Select`.
- **F9** filters the TestCase to the TestStepValues that have a value; press it again to show every control.
- Values can stay empty while the steps are laid out; the source fills them in a second pass.

## Configure and run

Tosca drives Internet Explorer unless told otherwise, so a web TestCase needs the Test Configuration Parameter `Browser`: select the TestCase, open its **Test Configuration** tab, right-click the entry, **Create Test Configuration Parameter**, pick `Browser` and the browser name (`Chrome`). It can also sit on a folder or an ExecutionList; see [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/). Then right-click the TestCase and choose **Run in ScratchBook**: the browser opens and every step runs; green means passed. ScratchBook results are temporary, which makes it the place for trial runs; kept results need an [ExecutionList](/ToscaBase/execution/execution-lists/). To debug, select a few TestSteps with `Shift`, or one TestStep folder, and run only those; details in [First TestCase](/ToscaBase/getting-started/first-test-case/#6-run-in-the-scratchbook).

## Workstate

A TestCase has three states: `Planned`, `In Work` and `Completed`. The state is not cosmetic; it feeds requirement coverage figures. When to set which is in [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

:::note
The source calls the first state "planning"; the Workstate column in Commander shows `Planned`. Treat the two as the same value.
:::

## ActionModes at a glance

The ActionMode tells Tosca what to do with the value: `Input` enters data or clicks, `Verify` compares a property with the value, `Buffer` stores the control's value under a name, `WaitOn` pauses until a condition holds, `Select` and `Constraint` navigate and narrow down inside tables, `Insert` creates objects in non-UI structures such as XML. Details in [ActionModes](/ToscaBase/test-cases/action-modes/).

## Worked example: Google search

The scenario: open Google in Chrome, search for *Tricentis Tosca*, open the first result, verify that the Tricentis site appeared, close the browser. Three user-defined Modules (Google search screen, search results screen, Tricentis portal) hold only the controls needed; see [XScan](/ToscaBase/modules/xscan/).

| # | TestStep | Module | Values and ActionModes |
|---|---|---|---|
| 1 | Open Google | `OpenUrl` (standard Module, **TBox XEngines > HTML**) | URL `www.google.com`, `Input` |
| 2 | Search Tricentis Tosca | Google search screen | Google icon: `Exists` = `True`, `WaitOn`; search field: `Tricentis Tosca`, `Input`; search button: click, `Input` |
| 3 | Pause | `TBox Wait` (standard Module) | `5000` (milliseconds) |
| 4 | Open first result | Search results screen | first result link: click, `Input` |
| 5 | Verify Tosca official portal | Tricentis portal | logo: `Exists` = `True`, `Verify` |
| 6 | Close browser | `Close Browser` (standard Module) | title `Tricentis Tosca*` (wildcard) |

Notes:

- **Step 1.** The generic **TBox Automation Tools > Process Automation** Module starts any program; for a web application use `OpenUrl`.
- **Step 2.** The `WaitOn` on the Google icon handles synchronisation: the step waits until the page has rendered the icon.
- **Step 3.** The static 5 s wait is the source's workaround for slow results; best practice replaces it with `WaitOn`, see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).

Reusing TestSteps across TestCases: [Business parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/).
