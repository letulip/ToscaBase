---
title: Commander overview
description: A tour of Tosca Commander - the start page and the First Steps sample project, the workspace sections, what a TestCase looks like inside, Test Configuration Parameters, and running a TestCase in the ScratchBook.
level: 1
sidebar:
  order: 60
sources:
  - id: U9X3juv6tz4
    title: "Tosca Tutorial | Lesson 4 - Tosca Commander Overview | Execute First Test Case | Test Results |"
    url: https://www.youtube.com/watch?v=U9X3juv6tz4
    at: "00:02"
  - id: c-VgJF2i1mU
    title: "Tricentis Tosca Tutorial Part-3 : Tosca Initial Project Setup, Tosca Workspace Overview & Creation"
    url: https://www.youtube.com/watch?v=c-VgJF2i1mU
    at: "05:30"
  - id: 6Z-XkFoVoxw
    title: "Tosca Tutorial | Lesson 5 - Create First Test Case | Tosca Commander | New Workspace |"
    url: https://www.youtube.com/watch?v=6Z-XkFoVoxw
    at: "09:21"
---

Tosca Commander is the application where the whole testing life cycle happens: Modules, TestCases, requirements, test design, execution and results are all sections of one window. The quickest way to get oriented is the **First Steps** sample project that ships with Tosca. It contains ready-made TestCases you can open, inspect and run before you build anything yourself.

## Start page and the First Steps project

After the license is connected, Commander shows its start page with the recently used workspaces and, by default, the **First Steps** project. Click it to open. Its **TestCases** section holds sample folders for manual tests, automated tests, data-driven tests and helpers, plus a TestCase named `Run me` intended for a first run.

## Sections of a workspace

Each block in the Commander window is a section of the workspace. The main ones:

| Section | What it holds |
|---|---|
| **TestCases** | Folders, TestCases and their TestSteps; the place where automation is assembled |
| **Modules** | The technical information about the application's controls, produced by XScan. See [Modules overview](/ToscaBase/modules/modules-overview/) |
| **Requirements** | Requirements with risk weighting, linked to TestCases. See [Requirements and risk](/ToscaBase/requirements-and-reporting/requirements-and-risk/) |
| **TestCase Design** | TestSheets, attributes and instances for data-driven test design. See [TestCase design](/ToscaBase/test-case-design/) |
| **Execution** | ExecutionLists and their permanent results. See [ExecutionLists](/ToscaBase/execution/execution-lists/) |
| **Issues** | Defects linked to executions |
| **Tutorial** | Built-in tutorial material; not needed for this knowledge base |

To see the hierarchy of the whole project, click **Project** in the **Home** tab.

### Arranging sections

Sections can be shown side by side. Drag a section's tab and drop it on one of the docking targets (centre, top, bottom, left, right) to split the window; with **Modules** on the right and **TestCases** on the left, you can drag Modules straight into TestCases. A section you have closed is reopened from the **Home** tab, where every section is listed.

## Inside the TestCases section

The section is a tree: parent folders, child folders, and TestCases inside them (the TestCase icon is a circle). Right-click a folder to see what can be created there:

- **Create Folder** (`Ctrl+N`) and **Create Virtual Folder** (a query-based folder; see [TQL and virtual folders](/ToscaBase/requirements-and-reporting/tql-and-virtual-folders/))
- **Create TestCase**
- **Create Business TestCase** (see [Execution repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/))
- **Create TestStep Library** (see [Business parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/))
- **Create Recovery Scenario Collection** (see [Recovery and cleanup scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/))
- **Create Test Configuration Parameter**

Keyboard shortcuts are shown next to each menu entry; `Ctrl+T` opens a search to add a TestStep from a Module.

### What a TestCase contains

Open the sample automated TestCase. Its TestSteps read like the manual flow: open the sample application, maximise the browser, main menu, vehicle data, insurance data, product data, price option, send quote. **Expand all** / **Collapse all** show or hide the TestStepValues under each step.

Each TestStepValue is one control of the application (a text field, a link, a button). The right-hand **Properties** pane shows the identification properties that XScan captured, and the **Value** column holds the data to enter or the action to perform. This is how a TestCase is built: the Module supplies the controls, the TestCase supplies values and ActionModes. See [TestCase basics](/ToscaBase/test-cases/test-case-basics/) and [ActionModes](/ToscaBase/test-cases/action-modes/).

The TestCase's details also show a **control flow diagram**, a graphical representation of the steps in order.

### Test Configuration Parameters

The sample TestCase carries a **Test Configuration** with a parameter `Browser` whose value is `Internet Explorer`, the browser it was designed for. Change the value to `Chrome`, `Edge` or `Firefox` to run it elsewhere, and reset to the default afterwards. New parameters are added by right-clicking the TestCase (or a folder) and choosing **Create Test Configuration Parameter**. Full treatment in [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## Running a TestCase in the ScratchBook

1. Select the TestCase (or its folder) and right-click **Run in ScratchBook**, or use the green play button in the **TestCases** ribbon.
2. Tosca drives the application through every step.
3. The **ScratchBook** shows each step with its result (passed or failed), start time, duration, and anything written to the log info.

:::caution
ScratchBook results are temporary and are stored nowhere. They are for dry runs while you build a TestCase. For results you can keep, report on or compare, put the TestCase into an **ExecutionList** in the **Execution** section and run it from there; see [ExecutionLists](/ToscaBase/execution/execution-lists/).
:::

## Next

[First TestCase](/ToscaBase/getting-started/first-test-case/) builds a TestCase of your own: scan a login page, drag the Module in, set values, and run it.
