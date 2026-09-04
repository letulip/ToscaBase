---
title: Multi-user workspaces
description: Create a multi-user workspace on a shared repository (SQLite for practice, Oracle, MS SQL Server or DB2 for projects), work with Update All, Checkout, Checkout Tree and Check In All, and inspect or revoke another user's checkout.
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
---

A single-user workspace (see [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)) can be used by one person at a time. When a team shares the same Modules, TestCases and ExecutionLists, each member needs their own workspace connected to a **common repository**, a database that holds the master copy of every object. That is a multi-user workspace. It brings a check-out and check-in cycle, a login screen, user management, branches, versioning and test mandates, none of which exist in a single-user workspace. This doc covers creating the workspace and the daily check-out cycle; the other features have their own docs in this section.

## Repository types

When you create a workspace, the **Type of repository** field decides what you get:

| Repository | Result | Connection details |
|---|---|---|
| `None` | Single-user workspace | none |
| `SQLite` | Multi-user workspace on a local database | none: no connection string, no schema |
| `Oracle`, `MS SQL Server`, `DB2` | Multi-user workspace on a dedicated database server | connection string (contains the user, password and database address); schema is optional; **Test connection** before creating |

:::caution
SQLite is for practising and for trying out the multi-user features. It is not a solution for a real project; a real project needs a dedicated Oracle, MS SQL Server or DB2 instance.
:::

## Creating a multi-user workspace

1. In Tosca Commander choose **Create new** workspace.
2. Set **Type of repository** to `SQLite` (or a database type and its connection string; test the connection).
3. Pick the folder and give the workspace a name (the source uses `MultiDemo`).
4. Leave **Slim workspace** unchecked unless the repository holds a high data volume. A slim workspace takes less disk space and speeds up a large repository; for a small one the speaker prefers a normal workspace.
5. Leave **Use existing repository** unchecked when this is the first workspace on this repository, so that Tosca creates the repository. Check it for every later workspace that should attach to the same repository (a second team member, or a workspace on a [branch](/ToscaBase/administration/branches/)).
6. Click **OK**. Creation takes a moment, then the workspace opens.

:::note
The speaker's wording about **Use existing repository** in Lesson 90 is contradictory; the behaviour above is what the demonstration and the follow-up in Lesson 92 show: the option is unavailable until a repository exists, and selected afterwards.
:::

## The login screen and the default user

A multi-user workspace always asks for a user name and password. On a freshly created workspace Tosca has already created one user, `Admin`, with an empty password: enter `Admin`, leave the password blank and click **Login**. Create the real users afterwards as described in [Users and groups](/ToscaBase/administration/users-and-groups/). Credentials are case-sensitive.

## Check-out and check-in

Every object in the repository is either free, checked out by you, or checked out by somebody else:

- A **green mark** in front of an object means it is checked out by you. Only checked-out objects can be edited; on a free folder the context menu shows no **Create** entries at all.
- A **red stripe** in front of an object means another user has it checked out. You cannot change it until that user checks in.

While you hold an object, nobody else can change it. This is the main difference from a code repository such as Git: Tosca does not merge concurrent edits of one object, it prevents them, so there are no conflicts to resolve. Changes from different users on different objects are merged when they check in.

The four operations, available on the toolbar of the multi-user section and in the context menu of each object:

| Operation | Effect |
|---|---|
| **Update All** | Fetches every change other users have checked in and merges it into your workspace. Do this before you start working. It can be automated with TCShell, see [Command-line tools](/ToscaBase/administration/command-line-tools/). |
| **Checkout** | Checks out one object only, for example the `Execution` folder but nothing inside it. |
| **Checkout Tree** | Checks out the object and everything it contains. Use it on a TestCase folder you are about to rework so that nobody changes its contents meanwhile. |
| **Check In All** | Checks in every object you hold and makes your changes available to the others. Do this when you finish. |

The recommended rhythm is: **Update All**, check out what you need (tree for a folder you will rework), work, **Check In All**. Closing a workspace with checked-out objects prompts you to check in; answering **No** leaves them checked out in the repository, which is what the next section is about.

:::tip
A folder that stays greyed out after **Update All**, with **Checkout** disabled and **Checkout Tree** reporting nothing to check out, is not locked by another user: it is excluded from synchronization. See the Synchronization policy section of [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).
:::

## Who changed it, who holds it

Right-click any object (this works whether you are an admin or a normal user):

- **Show latest change details** lists the object name, the time of the last change and the user who made it.
- **Show checkout details** shows when the object was checked out, by which user, and the object name. If you need an object that shows a red stripe, this tells you whom to ask.

## Revoking a checkout

Only a member of the `Admins` group can take a checked-out object away from another user. Right-click the object and choose **Revoke checkout**. Tosca warns that all changes in the object will be discarded: whatever the other user did while holding it is lost, and it will not be merged even if that user checks in later. After **OK** the object is free again; check it out yourself to work on it.

## Related

- [Users and groups](/ToscaBase/administration/users-and-groups/): creating users, passwords, owning and viewing groups.
- [Command-line tools](/ToscaBase/administration/command-line-tools/): cloning a workspace for each team member with TCWorkspaceUtil; a copied workspace does not work.
- [Branches](/ToscaBase/administration/branches/), [Backup and restore](/ToscaBase/administration/backup-and-restore/), [Versioning and recovery](/ToscaBase/administration/versioning-and-recovery/), [Test mandates](/ToscaBase/administration/test-mandates/).
