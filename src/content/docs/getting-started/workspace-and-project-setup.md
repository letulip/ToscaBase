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

If the template is not listed, browse to it: it sits under the Tosca projects folder, `C:\Tosca_Projects\`, which also holds the `Common Repositories` and `Workspaces` folders, in the `Tosca Commander` subfolder as `Standard.tsu` (folder names as spoken in the source).

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
