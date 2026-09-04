---
title: Workspace and project setup
description: What a Tosca workspace is, the difference between single-user and multi-user workspaces, the standard workspace template, and step-by-step creation of a single-user workspace.
level: 1
sidebar:
  order: 50
sources:
  - id: c-VgJF2i1mU
    title: "Tricentis Tosca Tutorial Part-3 : Tosca Initial Project Setup, Tosca Workspace Overview & Creation"
    url: https://www.youtube.com/watch?v=c-VgJF2i1mU
    at: "00:15"
  - id: 6Z-XkFoVoxw
    title: "Tosca Tutorial | Lesson 5 - Create First Test Case | Tosca Commander | New Workspace |"
    url: https://www.youtube.com/watch?v=6Z-XkFoVoxw
    at: "00:05"
  - id: qzYWlZJ8oac
    title: "Tosca Tutorial | Lesson 3 - Setup Tosca 16 | AWS EC2 | Virtual Windows Server | Cloud |"
    url: https://www.youtube.com/watch?v=qzYWlZJ8oac
    at: "18:39"
  - id: uw00il1mL40
    title: "TRICENTIS Tosca 16.0 - Lesson 03 | Create Workspace | Add Subset .tsu File | Automation Tool"
    url: https://www.youtube.com/watch?v=uw00il1mL40
    at: "02:02"
  - id: 0Hc_M7ksots
    title: "TRICENTIS Tosca 16.0 - Lesson 05 | Model-Based Test Automation | Standard Modules of Tosca |"
    url: https://www.youtube.com/watch?v=0Hc_M7ksots
    at: "05:07"
---

A **workspace** is the repository Tosca Commander works in. Everything you build (Modules, TestCases, test data, ExecutionLists, requirements) lives in a workspace, and you must connect to one before you can develop, maintain or execute anything. The workspace itself is defined on the local machine; its data can be kept locally or synchronised with a database that acts as a shared repository for a team. The first thing to do after installing and licensing Tosca is to create one.

## Single-user and multi-user workspaces

| | Single-user | Multi-user |
|---|---|---|
| Who can connect | One user | Several users |
| Central repository | Not needed | Required: a database (Oracle, SQLite, DB2, MS SQL Server) |
| Data management | Local | Shared; records must be **checked out** before editing and **checked in** afterwards |
| Login | None | Credentials; default user `Admin` with an empty password |

For learning Tosca, a single-user workspace is all you need, and it is what the rest of this section assumes. When a team shares Modules and TestCases, each member gets a workspace connected to a common repository instead. The **Type of repository** field in the creation dialog decides which kind you get: `None` creates a single-user workspace, any database type creates a multi-user one. The repository types, the multi-user creation procedure, the login screen and the check-out/check-in cycle are described in [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/); users, groups and branches in [Users and groups](/ToscaBase/administration/users-and-groups/) and [Branches](/ToscaBase/administration/branches/).

## The workspace template

The creation dialog offers **Use workspace template**. The standard template, `Standard.tsu`, preloads the workspace with default Modules (the [Standard modules](/ToscaBase/standard-modules/)), reusables, report templates and sample TestCases that every project needs. Always use it for a new project; you can also supply your own template.

If the template is not listed, browse to it: it sits under the Tosca projects folder, `C:\Tosca_Projects\`, which also holds the `Common Repositories` and `Workspaces` folders, in the `Tosca Commander` subfolder as `Standard.tsu` (folder names as read out in the QASCRIPT lesson, not verified on screen; the LambdaGeeks tutorial keeps the default path and does not name them). The Tosca 16 lessons confirm this: the path of `Standard.tsu` appears in the template field of the dialog, and the installer creates the folders.

### Training subset: Automation Specialist Level 1 Base.tsu

A `.tsu` file is a Tosca **subset**, a package of workspace objects. The Tosca 16 lessons build their workspace not from `Standard.tsu` but from `Automation Specialist Level 1 Base.tsu`, the subset of the Tricentis Automation Specialist Level 1 course. Besides the Standard modules it contains a `Workshop` folder of ready-made Modules with the controls and locators of the demo web shop that the lessons automate, so you can start on TestCases without scanning first. The lesson says both that the file is downloaded and that it comes with the Tosca 16 installation; look for it next to `Standard.tsu` and download it from the Tricentis training material if it is not there. Use it exactly like the standard template: tick **Use workspace template**, **Browse** to the `.tsu`, and create the workspace (the lesson names it `Project e-commerce`). After creation the **Modules** section shows both the `Standard modules` and the `Workshop` folder.

## Create a single-user workspace

1. Start Tosca Commander. On the start page click **Create new**.

   :::note
   Before Tosca 14.x the command was **Project > New**. In current versions it is on the start page.
   :::

2. **Type of repository**: `None`.
3. **Location**: keep the default path (a folder under `Workspaces`).
4. **Name**: the workspace name, for example `Training`.
5. Tick **Use workspace template** and keep `Standard.tsu`.
6. Click **OK**. Creation takes a few seconds; a success message appears and **Close** becomes enabled.
7. Close the dialog. Commander loads the new workspace with the default sections (TestCases, TestCase-Design, Execution and so on; see [Commander overview](/ToscaBase/getting-started/commander-overview/)).

To see the workspace hierarchy, click **Project** in the **Home** tab.

## Next

With the workspace open, continue with [Commander overview](/ToscaBase/getting-started/commander-overview/) to learn the sections, then [First TestCase](/ToscaBase/getting-started/first-test-case/).
