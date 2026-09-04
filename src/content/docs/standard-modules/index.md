---
title: Standard modules
description: The TBox Automation Modules that ship with Tosca for files, folders, buffers, processes, screenshots, windows and JavaScript.
level: 2
sidebar:
  order: 0
sources:
  - id: 0Hc_M7ksots
    title: "TRICENTIS Tosca 16.0 - Lesson 05 | Model-Based Test Automation | Standard Modules of Tosca |"
    url: https://www.youtube.com/watch?v=0Hc_M7ksots
    at: "03:02"
---

Tosca ships a library of ready-made Modules, the **Standard modules** (also called TBox Automation Modules). They cover general operations a TestCase needs around the application under test, and you add them with **Add TestStep** without scanning anything. This section explains each group: what the Module does, its ModuleAttributes, and the pitfalls.

| Doc | What it covers |
|---|---|
| [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/) | Create, copy, compare and delete files and folders; check a folder exists |
| [Buffer operations](/ToscaBase/standard-modules/buffer-operations/) | Set Buffer, Partial Buffer, Name to Buffer, Delete Buffer |
| [Start and close programs](/ToscaBase/standard-modules/start-and-close-programs/) | TBox Start Program with arguments, closing programs with taskkill, Start/Stop Timer |
| [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/) | TBox Evaluation Tool: compare dynamic expressions, use as an If condition, math per operator |
| [Screenshots on failure](/ToscaBase/standard-modules/screenshots-on-failure/) | TBox Take Screenshot and the automatic screenshot project setting |
| [Window operations](/ToscaBase/standard-modules/window-operations/) | TBox Window Operation, closing popups, TBox Scroll Window Operation |
| [Desktop dialogs](/ToscaBase/standard-modules/desktop-dialogs/) | TBox Save As for the Windows Save As dialog and its confirmation popup |
| [Execute JavaScript](/ToscaBase/standard-modules/execute-javascript/) | Execute JavaScript and Verify JavaScript Result under TBox XEngines > HTML |

Read them in order: file and buffer operations are used by almost every TestCase, the process and window Modules come into play for desktop applications, and the JavaScript Modules are a fallback for web cases the HTML engine cannot express directly.

## Where they come from

The Standard modules are shipped as the subset `Standard.tsu` in the Tosca installation folder. When you create a workspace, **Use workspace template** points at this file, and the new workspace then has a **Standard modules** folder in its Modules section (see [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)). What you find there, as shown in Lesson 5:

| Folder | Examples |
|---|---|
| TBox Automation Tools | Basic window operations (send keys, window operation, scroll window), file operations (file comparison) |
| TBox XEngines > HTML | `OpenUrl`, `Close Browser` |
| Excel | Open and close a workbook, create and delete a worksheet ([Excel engine](/ToscaBase/engines/excel-engine/)) |
| PDF | Compare PDF files ([PDF engine](/ToscaBase/engines/pdf-engine/)) |
| SAP | Modules for SAP applications |

Each of them is a reusable function you would otherwise have to script: opening a URL, closing the browser, comparing files, handling a popup. They can be dragged into any number of TestCases.
