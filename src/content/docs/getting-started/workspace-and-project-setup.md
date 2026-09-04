---
title: Workspace and project setup
description: What a Tosca workspace is, single-user versus multi-user workspaces, the repository types, the standard workspace template, and step-by-step creation of both kinds.
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

Locking a record so that nobody else can change it is called **check-out**; releasing it after the change is **check-in**. Multi-user workspaces, users, groups and branches are covered in [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/) and [Users and groups](/ToscaBase/administration/users-and-groups/).

## Repository type

The **Type of repository** field in the creation dialog decides which kind of workspace is created:

| Value | Result |
|---|---|
| `None` | Single-user workspace |
| `SQLite` | Multi-user workspace with a SQLite file as repository |
| `Oracle` | Multi-user; asks for schema name and connection details |
| `MS SQL Server` | Multi-user |
| `DB2` | Multi-user |

For any value other than `None`, database-specific fields (schema, connection type, connection string) appear after the selection.

## The workspace template

The creation dialog offers **Use workspace template**. The standard template, `Standard.tsu`, preloads the workspace with default Modules (the [Standard modules](/ToscaBase/standard-modules/)), reusables, report templates and sample TestCases that every project needs. Always use it for a new project; you can also supply your own template.

If the template is not listed, browse to it: it sits under the Tosca projects folder, `C:\Tosca_Projects\`, which also holds the `Common Repositories` and `Workspaces` folders, in the `TOSCA Commander` subfolder as `Standard.tsu` (folder names as spoken in the source).

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
7. Close the dialog. Commander loads the new workspace with the default sections (TestCases, TestCase Design, Execution and so on; see [Commander overview](/ToscaBase/getting-started/commander-overview/)).

To see the workspace hierarchy, click **Project** in the **Home** tab.

## Create a multi-user workspace with SQLite

1. **Create new** on the start page.
2. **Type of repository**: `SQLite` (for Oracle you would add the schema and connection string instead).
3. **Repository path**: keep the default.
4. **Use existing repository**: leave unticked when creating the repository for the first time; tick it later to connect another workspace to the same repository.
5. **Name**: for example `Multi user workspace`.
6. Keep the standard template and click **OK**. Wait for the success message and close the dialog.
7. Log in when prompted. The default user is `Admin` with an empty password.

Working in this workspace differs from single-user in one habit: **check out** an object before editing, **check in** to save it to the repository. The project can be viewed, and the Admin password reset, by right-clicking the root of the hierarchy.

:::caution
Everyone working in the same multi-user repository sees your check-outs. Check in promptly, and set the TestCase Workstate so colleagues know what is in progress; see [TestCase structure](/ToscaBase/best-practices/test-case-structure/#set-the-workstate).
:::

## Next

With the workspace open, continue with [Commander overview](/ToscaBase/getting-started/commander-overview/) to learn the sections, then [First TestCase](/ToscaBase/getting-started/first-test-case/).
