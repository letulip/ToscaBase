---
title: Users and groups
description: Create users and user groups in a multi-user workspace, set and change passwords, grant the Admins role, restrict sections with owning and viewing groups, disable users, and read the personal data report.
level: 4
sidebar:
  order: 20
sources:
  - id: qeYPDWYYEX4
    title: "Tricentis Tosca Tutorial Part-14: Tosca User Management, Tosca User Group, Tosca Password Reset"
    url: https://www.youtube.com/watch?v=qeYPDWYYEX4
    at: "01:21"
  - id: PDP4hgWD9zY
    title: "Tosca Tutorial | Lesson 91 - Create and Manage User Groups with Users | Multi-User Workspace |"
    url: https://www.youtube.com/watch?v=PDP4hgWD9zY
    at: "00:14"
  - id: K8oTSYoowWo
    title: "TRICENTIS Tosca 16.0 - Lesson 41 | Multi-user Workspace| Manage Users & User Groups | User Access"
    url: https://www.youtube.com/watch?v=K8oTSYoowWo
    at: "02:18"
---

User management exists only in a [multi-user workspace](/ToscaBase/administration/multi-user-workspaces/). It answers two questions: *authentication* (who may log in, with which password) and *authorization* (which group may change or view which part of the workspace). Both are configured by an administrator inside Tosca Commander; there is no separate admin tool.

## Where user management is

It is not on the top menu. Select the root project node and open its **User management** tab (in Tosca 16 it sits next to **Details**, **Test configurations**, **Properties** and **Definition**); the right-hand part of the window lists groups and users. Every change here requires the root project to be checked out first, and every change must be checked in (**Check In All**) before other users see it, including a new password.

Two groups exist by default:

- `Admins`: administrators. The default `Admin` user is in it and cannot be disabled.
- `All users`: every user you create appears here.

## Creating a group

Right-click the root project (or the top of the user management area) and choose **Create user group**, then rename the new group. Groups can reflect roles (the sources create `Tosca specialists` and `Tosca design specialists`) or projects that need separate access (`Project XYZ`). Right-click > **Delete** removes a group but keeps its users: they stay in `All users`, where you delete or disable them.

## Creating a user

Right-click a group and choose **Create user** (the `All users` group has the same command). The user is created with a placeholder name such as `User 6`; rename it. Properties on the user:

| Property | Meaning |
|---|---|
| **Enabled** | Checked by default. Uncheck to lock the user out (see below). |
| **Description** | Free text, e.g. what the user or group is for. |
| **Domain** | Optional domain for the user. |
| **Set result allowed** | When unchecked, the user cannot set an execution result manually to passed or failed; only the result Tosca produces is shown. Lesson 41 unchecks it for design specialists, who only build TestCases, and keeps it for testers. |
| **Level** | `Basic`, `Advanced` or `Expert`. |
| **Owning group** | `Admins` or `All users`: only members of the owning group can change this user or group entry. A `Super users` group with owning group `Admins` can be managed by administrators only (Lesson 41). |

:::note
The sources disagree on **Level**: Part 14 calls it the user's proficiency, Lessons 91 and 41 say it gives different access to different sections. None shows a concrete effect. Treat it as a classification until you verify it in your version.
:::

A user can belong to several groups. Drag the user into another group to add it there; the entries are instances of the same user, and a change made in one place (a password, the Enabled flag) is reflected in all of them. To make a user an administrator, drag it into `Admins`.

## Passwords

A new user has an empty password, so set one immediately: right-click the user, choose **Set password**, enter and confirm it. Only an administrator sees this command; an admin can set, change or remove any user's password with it at any time and hands the password to the team member.

A logged-in user changes their own password by right-clicking the root project (checked out) and choosing **Change my password**: enter the old password, then the new one twice. Check in; the new password applies from the next login.

To try a new login, check in, close the workspace and reopen it (an existing workspace on the same repository needs an **Update All** first, or create a fresh workspace on the shared repository). The login prompt takes a moment to appear; names and passwords are case-sensitive.

## Owning group and viewing group: access rights

Access is granted per section or folder through two properties, visible after checking the object out and opening its properties:

- **Owning group name**: the group allowed to change the object (create, delete, update). Default is `All users`, inherited from the parent.
- **Viewing group name**: empty by default. When set, members of that group can open the object but not change it.

Example from the source: on the `Modules` section set the owning group to `Tosca design specialists` and the viewing group to `Tosca specialists` (or leave it at `All users`); design specialists maintain the Modules, everybody else can only read them. Lesson 41 does the same on the `TestCases` section (viewing `All users`, owning `Tosca specialists`) and on **Configurations**, where DEX agents and the database are set up: viewing `All users`, owning `Super users`, so only that group can add or manage agents. Use **Checkout Tree** on the section before editing the properties. The same works at any level: the whole project, a component folder, or a single TestCase, so a project team can be given exactly its own folder.

## Disabling a user

Select the user and uncheck **Enabled**; the change is replicated to all instances of the user. After **Check In All** the user can no longer log in. Disabled users can be hidden or shown with the **Show disabled users** toggle in the **View** options of user management.

## Personal data report

Right-click a user and choose **Create personal data report**: Tosca writes an Excel file into a folder of the workspace, to trace what the user did: machine ID, workspace ID, user ID and user name, revisions with their creation date, the object IDs that were changed, and comments. A user who has never logged in has an empty report.

## Related

- [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/): check-out, and the admin-only **Revoke checkout**.
- [Review process](/ToscaBase/best-practices/review-process/): a folder-based workflow that owning and viewing groups can enforce.
