---
title: First TestCase
description: Build and run a complete login TestCase from scratch - folder structure, scanning the page into a Module, dragging the Module into the TestCase, values and ActionModes, the Browser Test Configuration Parameter, opening and closing the browser, and running in the ScratchBook.
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
---

The first TestCase is a login: open a demo web shop (the Sauce Labs "Swag Labs" demo site with a login page and a product list), enter username and password, click **Login**, and close the browser. Small as it is, it exercises the complete Tosca workflow: scan the page into a Module, assemble the TestCase from the Module, add the Standard modules that open and close the browser, set the browser as a Test Configuration Parameter, and run in the ScratchBook. Prerequisites: a workspace created from the standard template ([Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)), Chrome with the Tosca extension ([Installation](/ToscaBase/getting-started/installation/#browser-extension-for-xscan)), and the demo page open in Chrome.

## 1. Folder structure in TestCases

In the **TestCases** section create a folder for the scenario (`Ctrl+N` or the ribbon), for example `Sauce Demo Test`. Inside it create:

- a folder `Prerequisites`, which will open the application;
- a TestCase `Login Test`;
- later, a folder `Post condition`, which will close the application.

How you nest folders and TestCases is up to you; the point is that a folder can be executed as a unit, so prerequisites, test and cleanup run together in order.

## 2. Scan the login page into a Module

TestCases hold no technical information; that lives in **Modules**, Tosca's equivalent of page objects.

1. In the **Modules** section create a folder (for example `Sauce Demo`).
2. Right-click it and open **Scan**. The dropdown lists scan types: application, API, mobile, PDF, remote terminal, WebDriver, Salesforce, file scan, legacy scan. Choose **Application**.
3. The XScan agent lists the windows currently open. Select the Chrome window with the demo page and click **Scan**.
4. XScan asks you to click controls in the application to add them. Click the **username** field, the **password** field and the **Login** button. They appear in the XScan window with tick marks.
5. Click **Save** and close XScan. The **Advanced** section, where identification properties are changed when a control is not unique, is not needed here; see [Control identification](/ToscaBase/modules/control-identification/).
6. Rename the new Module to something anyone can read, for example `Login Page`.

Expanding the Module shows the three ModuleAttributes with their **ActionMode**, **value range** and, in the Properties pane, the identification properties Tosca will use. As long as every control is unique on the page there is nothing to change. Full detail in [XScan](/ToscaBase/modules/xscan/).

## 3. Drag the Module into the TestCase

Dock **Modules** next to **TestCases** (drag the section tab to the right docking target; see [Commander overview](/ToscaBase/getting-started/commander-overview/#arranging-sections)). Drag `Login Page` onto `Login Test`. Tosca creates a TestStep with one TestStepValue per ModuleAttribute. Now fill it in:

| TestStepValue | Data type | ActionMode | Value |
|---|---|---|---|
| Username | String | `Input` | the demo site's standard user name (shown on the login page) |
| Password | Password | `Input` | the matching password; it is masked once typed |
| Login | String | `Input` | `{CLICK}` (choose **Click** from the value dropdown) |

A text box takes an `Input` with a value; a button is not a text box, so its value is the click action picked from the dropdown while the ActionMode stays `Input`. Every ActionMode is explained in [ActionModes](/ToscaBase/test-cases/action-modes/).

## 4. Browser as a Test Configuration Parameter

Tosca must know which browser to use. Right-click the parent folder `Sauce Demo Test` and choose **Create Test Configuration Parameter**. Type or pick `Browser` (a predefined parameter type with browser values), set the value to `Chrome`, and leave the data type as string. Because it sits on the parent folder it applies to everything inside. More in [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## 5. Open the application (Prerequisites)

The browser is chosen, but nothing opens it yet. In `Prerequisites` add a TestStep from the Standard modules that came with the template: open the Modules section (from the **Home** tab if you closed it) and find **TBox XEngines > HTML > Open Url**, or press `Ctrl+T` in the folder and search. Drag it in, rename the step `Open Application`, and paste the demo site's URL into the **Url** value. The optional `ActiveTab` and browser-arguments values can stay empty.

## 6. Run in the ScratchBook

Right-click the **parent folder** (not just the TestCase, because the prerequisites must run first) and choose **Run in ScratchBook**. Chrome starts, the URL opens, the credentials are entered and Login is clicked. The ScratchBook lists `Open Url` and `Login Page` with their TestStepValues and a pass/fail per step.

:::caution
A passing ScratchBook run does not prove the login worked. In the source, the first run passed every step although the page showed "username and password do not match", because the TestCase only entered values and clicked; nothing verified the result. Add a verification (for example the product page title with ActionMode `Verify`) before trusting it; see [TestCase structure](/ToscaBase/best-practices/test-case-structure/).
:::

## 7. Close the browser (Post condition)

Create the `Post condition` folder and drag in **TBox Automation Tools > Basic window operations > TBox Window Operation**, renamed `Close Application`:

| TestStepValue | ActionMode | Value |
|---|---|---|
| Caption | `Select` | `Swag*`: the window title starts with "Swag Labs"; the wildcard covers the rest |
| Operation | `Input` | `Close` (the dropdown also offers Maximize, Minimize, Normal and others) |

Run the parent folder again: three steps now appear (Open Url, Login Page, TBox Window Operation) and the browser closes at the end. The Module is documented in [Window operations](/ToscaBase/standard-modules/window-operations/).

## 8. Set the Workstate

Every TestCase has a **Workstate**: `Planned`, `In Work`, `Completed`. Set `In Work` while you build and `Completed` when done; the icon changes with the state, and in a shared workspace it tells colleagues what is finished. Working alone you can ignore it. See [TestCase structure](/ToscaBase/best-practices/test-case-structure/#set-the-workstate).

## What you have learned

Scan a page into a Module, build a TestCase from Modules, supply values and ActionModes, parameterise the browser, wrap the test with prerequisites and cleanup, and run it. Every later topic (verification, Buffers, control flow, ExecutionLists) extends this skeleton. Continue with [TestCase basics](/ToscaBase/test-cases/test-case-basics/).
