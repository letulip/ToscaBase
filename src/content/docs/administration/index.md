---
title: Administration
description: Multi-user workspaces on a common repository, users and groups, branches, backup and versioning, Test mandates, command-line tools and Tosca Server.
level: 4
sidebar:
  order: 0
---

Everything in this section presupposes a team: several people working on the same Modules, TestCases and ExecutionLists through a shared repository, and someone administering it. It starts with the multi-user workspace, because every other feature here only exists inside one, and ends with Tosca Server, the component that connects Commander installations, DEX agents and CI.

| Doc | What it covers |
|---|---|
| [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/) | Repository types (SQLite, Oracle, MS SQL Server, DB2), creating the workspace, Update All / Checkout / Checkout Tree / Check In All, change and checkout details, revoking a checkout |
| [Users and groups](/ToscaBase/administration/users-and-groups/) | Creating users and groups, passwords, the Admins group, owning and viewing groups per section, disabling users, the personal data report |
| [Branches](/ToscaBase/administration/branches/) | Create a branch, work on it in its own workspace, merge into Master, delete |
| [Backup and restore](/ToscaBase/administration/backup-and-restore/) | Export subset for single-user projects; repository backup and restore for multi-user projects |
| [Versioning and recovery](/ToscaBase/administration/versioning-and-recovery/) | Versioning settings, change history, recovering a deleted object with Export subset for revision |
| [Test mandates](/ToscaBase/administration/test-mandates/) | Executing one ExecutionList from several users without overwriting results |
| [Command-line tools](/ToscaBase/administration/command-line-tools/) | TCShell in interactive and script mode; cloning workspaces with TCWorkspaceUtil |
| [Tosca Server](/ToscaBase/administration/tosca-server/) | Architecture, installation, services, dashboard and DEX monitor |

The repository **Synchronization policy**, the most common source of "I cannot check this folder out" questions, is explained in [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/#synchronization-policy).
