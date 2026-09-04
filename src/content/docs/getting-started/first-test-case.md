---
title: First TestCase
description: Build and run a login TestCase from scratch - folder structure, scanning a Module, values and ActionModes, the Browser parameter, opening and closing the browser, running whole or in part in the ScratchBook.
level: 1
sidebar:
  order: 70
sources:
  - id: 6Z-XkFoVoxw
    title: "Tosca Tutorial | Lesson 5 - Create First Test Case | Tosca Commander | New Workspace |"
    url: https://www.youtube.com/watch?v=6Z-XkFoVoxw
    at: "02:11"
  - id: U9X3juv6tz4
    title: "Tosca Tutorial | Lesson 4 - Tosca Commander Overview | Execute First Test Case | Test Results |"
    url: https://www.youtube.com/watch?v=U9X3juv6tz4
    at: "08:14"
  - id: nEcKRePDKa0
    title: "TRICENTIS Tosca 16.0 - Lesson 09 | Test Case Automation | Create Test Steps using Modules |"
    url: https://www.youtube.com/watch?v=nEcKRePDKa0
    at: "09:17"
  - id: ZZ6lWHHHnCg
    title: "TRICENTIS Tosca 16.0 - Lesson 10 | Test Case Automation | Populate TestStep Values for Test Cases |"
    url: https://www.youtube.com/watch?v=ZZ6lWHHHnCg
    at: "04:05"
  - id: SLWKhb4igB0
    title: "TRICENTIS Tosca 16.0 - Lesson 11 | Test Case Automation | Run your First Automated Tests | TCP |"
    url: https://www.youtube.com/watch?v=SLWKhb4igB0
    at: "04:47"
---

The first TestCase is a login: open a demo web shop (the Sauce Labs "Swag Labs" demo site with a login page and a product list), enter username and password, click **Login**, and close the browser. Prerequisites: a workspace created from the standard template ([Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)), Chrome with the Tosca extension ([Installation](/ToscaBase/getting-started/installation/#browser-extension-for-xscan)), and the demo page open in Chrome.

## 1. Folder structure in TestCases

In the **TestCases** section create a folder for the scenario (`Ctrl+N` or the ribbon), for example `Sauce Demo Test`. Inside it create:

- a folder `Prerequisites`, which will open the application;
- a TestCase `Login Test`;
- later, a folder `Post condition`, which will close the application.

A folder can be executed as a unit, so prerequisites, test and cleanup run together in order.

## 2. Scan the login page into a Module

TestCases hold no technical information; that lives in **Modules**, Tosca's equivalent of page objects.

1. In the **Modules** section create a folder (for example `Sauce Demo`).
2. Right-click it and choose **Scan > Application**.
3. The XScan agent lists the windows currently open. Select the Chrome window with the demo page and click **Scan**.
4. Click the **username** field, the **password** field and the **Login** button in the application; they appear in XScan with tick marks.
5. Click **Save** and close XScan. The **Advanced** section (identification properties for non-unique controls) is not needed here; see [Control identification](/ToscaBase/modules/control-identification/).
6. Rename the new Module to something anyone can read, for example `Login Page`.

Expanding the Module shows the three ModuleAttributes with their **ActionMode**, **value range** and identification properties; as long as every control is unique on the page there is nothing to change. Full detail in [XScan](/ToscaBase/modules/xscan/).

## 3. Drag the Module into the TestCase

Dock **Modules** next to **TestCases** ([Commander overview](/ToscaBase/getting-started/commander-overview/#arranging-sections)) and drag `Login Page` onto `Login Test`, or right-click the TestCase and use *search and add step* (`Ctrl+T`), as the Tosca 16 lessons do. Either way Tosca creates a TestStep with one TestStepValue per ModuleAttribute; rename it after the business action it performs. Fill it in:

| TestStepValue | Data type | ActionMode | Value |
|---|---|---|---|
| Username | String | `Input` | the demo site's standard user name (shown on the login page) |
| Password | Password | `Input` | the matching password; it is masked once typed |
| Login | String | `Input` | `X` |

Typing or pasting a value switches the ActionMode to `Input` automatically; the data type defaults to String. A button or link takes `X`: an internal click without moving the pointer and the recommended way to click (an empty `Input` value also clicks, but `X` makes the intent visible). A checkbox takes `True`. The older video picks **Click** from the value dropdown (`{CLICK}`, a slower physical mouse click; see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/)). Every ActionMode is explained in [ActionModes](/ToscaBase/test-cases/action-modes/).

:::tip
Once a TestCase has many steps, `F9` toggles the TestCases section between showing only the TestStepValues that carry a value and showing all of them.
:::

## 4. Browser as a Test Configuration Parameter

Tosca must know which browser to use. Right-click the parent folder `Sauce Demo Test` and choose **Create Test Configuration Parameter**. Type or pick `Browser` (a predefined parameter type with browser values), set the value to `Chrome`, and leave the data type as string. Because it sits on the parent folder it applies to everything inside. Lesson 11 sets it on the TestCase itself instead (its **Test Configuration** tab, right-click the entry, **Create Test Configuration Parameter**, `Browser` = `Chrome`); an ExecutionList can carry it too, and its value overrides the TestCase's. More in [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## 5. Open the application (Prerequisites)

The browser is chosen, but nothing opens it yet. In `Prerequisites` add a TestStep from the Standard modules: **TBox XEngines > HTML > Open Url** in the Modules section, or `Ctrl+T` in the folder and search. Rename the step `Open Application` and paste the demo site's URL into the **Url** value. The optional `ActiveTab` and browser-arguments values can stay empty.

## 6. Run in the ScratchBook

Right-click the **parent folder** (not just the TestCase, because the prerequisites must run first) and choose **Run in ScratchBook**. Chrome starts, the URL opens, the credentials are entered and Login is clicked. The ScratchBook lists `Open Url` and `Login Page` with their TestStepValues and a pass/fail per step: all green means every step passed. ScratchBook runs are trial runs: results are temporary, not saved like an [ExecutionList](/ToscaBase/execution/execution-lists/)'s. The same command runs the Tosca 16 lessons' end-to-end web shop TestCase, from login to checkout and logout ([TestCase basics](/ToscaBase/test-cases/test-case-basics/)).

:::caution
A passing ScratchBook run does not prove the login worked: in the source the first run passed although the page showed "username and password do not match", because nothing verified the result. Add a verification (the product page title with ActionMode `Verify`, say); see [TestCase structure](/ToscaBase/best-practices/test-case-structure/).
:::

### Running part of a TestCase

To debug, run only a piece:

- Select a few TestSteps (`Shift`+click), right-click, **Run in ScratchBook**: only those steps run, for example just the login.
- Right-click a TestStep folder such as `Checkout process` and run it alone.
- Open **ScratchBook** from the ribbon, dock it to the right, drag TestSteps into it and right-click **Run**. The ScratchBook keeps its entries, so clear them before the next run.

A partial run assumes the application is already in the right state; in the source one run failed only because two tabs of the shop were open, so close extra tabs first.

## 7. Close the browser (Post condition)

Create the `Post condition` folder and drag in **TBox Automation Tools > Basic window operations > TBox Window Operation**, renamed `Close Application`:

| TestStepValue | ActionMode | Value |
|---|---|---|
| Caption | `Select` | `Swag*` (the title starts with "Swag Labs"; wildcard for the rest) |
| Operation | `Input` | `Close` (the dropdown also offers Maximize, Minimize, Normal and others) |

Run the parent folder again: three steps appear and the browser closes at the end. The Module is documented in [Window operations](/ToscaBase/standard-modules/window-operations/).

## 8. Set the Workstate

Every TestCase has a **Workstate**: `Planned`, `In Work`, `Completed`. Set `In Work` while you build and `Completed` when done; in a shared workspace it tells colleagues what is finished. See [TestCase structure](/ToscaBase/best-practices/test-case-structure/#set-the-workstate).

## What you have learned

Scan a page into a Module, build a TestCase from Modules, supply values and ActionModes, parameterise the browser, wrap the test with prerequisites and cleanup, run it whole or in parts. Every later topic extends this skeleton; continue with [TestCase basics](/ToscaBase/test-cases/test-case-basics/).
