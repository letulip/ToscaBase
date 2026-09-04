---
title: Multi-user workspaces
description: Create a multi-user workspace on a shared repository (SQLite for practice, Oracle, MS SQL Server or DB2 for projects), work with Update All, Checkout, Checkout Tree and Check In All, inspect or revoke another user's check-out, and understand the Synchronization policy behind greyed-out folders.
level: 4
sidebar:
  order: 10
sources:
  - id: duNDCSb2Tz0
    title: "Tosca Tutorial | Lesson 90 - Create Multi-User Workspace | SQLite DB | CheckIn/Checkout | Repository"
    url: https://www.youtube.com/watch?v=duNDCSb2Tz0
    at: "00:07"
  - id: kkhG9MAM41A
    title: "Tosca Tutorial | Lesson 95 - View Latest Change Details | Checkout Details | Revoke Checkout |"
    url: https://www.youtube.com/watch?v=kkhG9MAM41A
    at: "00:08"
  - id: PDP4hgWD9zY
    title: "Tosca Tutorial | Lesson 91 - Create and Manage User Groups with Users | Multi-User Workspace |"
    url: https://www.youtube.com/watch?v=PDP4hgWD9zY
    at: "02:17"
  - id: o1b8cACf4Hs
    title: "Tosca Tutorial | Lesson 138 - Common RealTime Tosca Problems & Fixes | Synchronization Policy |"
    url: https://www.youtube.com/watch?v=o1b8cACf4Hs
    at: "00:12"
---

A single-user workspace (see [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)) serves one person at a time. When a team shares the same Modules, TestCases and ExecutionLists, each member needs their own workspace connected to a **common repository**, a database that holds the master copy of every object. That is a multi-user workspace. It brings a check-out cycle, a login screen, user management, branches, versioning and Test mandates. This doc covers creation, the daily check-out cycle and the Synchronization policy; the rest have their own docs in this section.

## Repository types

When you create a workspace, the **Type of repository** field decides what you get:

| Repository | Result | Connection details |
|---|---|---|
| `None` | Single-user workspace | none |
| `SQLite` | Multi-user workspace on a local database | none: no connection string, no schema |
| `Oracle`, `MS SQL Server`, `DB2` | Multi-user workspace on a dedicated database server | database fields appear: a **connection string** (user, password and database address), which is required, and a **schema**, which Lesson 90 calls optional; **Test connection** before creating |

:::caution
SQLite is for practising and for trying out the multi-user features. It is not a solution for a real project; a real project needs a dedicated Oracle, MS SQL Server or DB2 instance.
:::

## Creating a multi-user workspace

1. In Tosca Commander choose **Create new** workspace.
2. Set **Type of repository** to `SQLite` (or a database type and its connection string; test the connection).
3. Pick the folder and give the workspace a name (the source uses `MultiDemo`).
4. Leave **Slim workspace** unchecked unless the repository is large: a slim workspace takes less disk space and speeds up a big repository.
5. Leave **Use existing repository** unchecked when this is the first workspace on this repository, so that Tosca creates the repository. Check it for every later workspace on the same repository (a second team member, or a [branch](/ToscaBase/administration/branches/)).
6. Click **OK**. Creation takes a moment, then the workspace opens.

:::note
The speaker's wording about **Use existing repository** in Lesson 90 is contradictory; the behaviour above is what the demonstration and Lesson 92 show.
:::

## The login screen and the default user

A multi-user workspace always asks for a user name and password. On a freshly created workspace Tosca has already created one user, `Admin`, with an empty password: enter `Admin`, leave the password blank and click **Login**. Create the real users afterwards as described in [Users and groups](/ToscaBase/administration/users-and-groups/).

## Check-out and check-in

Every object in the repository is either free, checked out by you, or checked out by somebody else:

- A **green mark** in front of an object means it is checked out by you. Only checked-out objects can be edited; on a free folder the context menu shows no **Create** entries at all.
- A **red stripe** in front of an object means another user has it checked out. You cannot change it until that user checks in.

While you hold an object nobody else can change it: unlike Git, Tosca does not merge concurrent edits of one object, it prevents them, so there are no conflicts to resolve. Edits by different users to different objects are merged at check-in.

The four operations, available on the toolbar of the multi-user section and in the context menu of each object:

| Operation | Effect |
|---|---|
| **Update All** | Fetches every change other users have checked in into your workspace. Do this before you start; TCShell can automate it ([Command-line tools](/ToscaBase/administration/command-line-tools/)). |
| **Checkout** | Checks out one object only, for example the `Execution` folder but nothing inside it. |
| **Checkout Tree** | Checks out the object and everything it contains. Use it on a folder you are about to rework so nobody changes its contents meanwhile. |
| **Check In All** | Checks in every object you hold and makes your changes available to the others. Do this when you finish. |

The recommended rhythm is: **Update All**, check out what you need (tree for a folder you will rework), work, **Check In All**. Closing a workspace with checked-out objects prompts you to check in; **No** leaves them checked out in the repository.

## Who changed it, who holds it

Right-click any object (this works whether you are an admin or a normal user):

- **Show latest change details** lists the object name, the time of the last change and the user who made it.
- **Show checkout details** shows when the object was checked out, by which user, and the object name. If you need an object that shows a red stripe, this tells you whom to ask.

## Revoking a check-out

Only an admin user can take a checked-out object away from another user; every new workspace has the groups `Admins` and `All users`, and the default `Admin` user belongs to `Admins`. Right-click the object and choose **Revoke checkout**. Tosca warns that all changes in the object will be discarded: what the other user did while holding it is lost, even if they check in later. After **OK** the object is free again; check it out yourself to work on it.

## Synchronization policy

*Synchronization* is the process that keeps the objects in your workspace in step with the changes in the common repository; **Update All** triggers it. In large repositories not every folder is synchronized: to shorten the time it takes to open and update a workspace, folders that most testers do not need are **excluded from synchronization** on purpose, and each tester includes only the folders they work on.

An excluded folder looks locked, but is not:

- the folder and the objects inside it stay greyed out after **Update All**;
- **Checkout** is disabled in the context menu, and **Checkout Tree** reports that there are no objects to check out;
- you cannot create, edit or check out anything inside it.

To make it accessible, right-click it and choose **Include for synchronization** (the object itself) or **Include all necessary items for tree** (the object with its children). Tosca synchronizes them with the repository and the folder becomes usable. The reverse commands, **Exclude from synchronization** and **Exclude tree from synchronization**, grey the object (or the whole subtree) out, and from the next check-in it is no longer synchronized with the repository.

What may be excluded is governed by the **Synchronization policy** property, shown in the Properties pane of a checked-out object:

| Value | Meaning |
|---|---|
| `Customizable, default is on` | Default. Synchronized, but any user may exclude the object |
| `off` | Not synchronized |
| `Cannot be excluded` | Always synchronized; nobody can exclude the object |
| `Cannot be excluded for whole tree` | The object and all its children cannot be excluded |

Objects created under a parent inherit the parent's value. Exporting or importing an object resets the property to `Customizable, default is on`.

## Related

- [Users and groups](/ToscaBase/administration/users-and-groups/): creating users, passwords, owning and viewing groups.
- [Command-line tools](/ToscaBase/administration/command-line-tools/): cloning a workspace for each team member with TCWorkspaceUtil; a copied workspace does not work.
- [Branches](/ToscaBase/administration/branches/), [Backup and restore](/ToscaBase/administration/backup-and-restore/), [Versioning and recovery](/ToscaBase/administration/versioning-and-recovery/), [Test mandates](/ToscaBase/administration/test-mandates/).
