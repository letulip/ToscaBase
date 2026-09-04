---
title: Backup and restore
description: Back up a single-user project with Export subset, back up a multi-user common repository as an administrator, and restore it into a new repository.
level: 4
sidebar:
  order: 40
sources:
  - id: RwG5mX78aDA
    title: "Tosca Tutorial | Lesson 93 - Backup & Restore Repositories | Multi-User Repositories |"
    url: https://www.youtube.com/watch?v=RwG5mX78aDA
    at: "00:08"
---

Tosca Commander can back up and restore two kinds of item: an entire project, single-user or multi-user, and a component folder (a smaller project inside a big one). The mechanism differs by workspace type: a single-user project is backed up with a subset export, a multi-user project through a repository backup that only an administrator can run. Regular backups are what let you rebuild a repository after a database or infrastructure failure.

## Single-user project: Export subset

1. Right-click the project (or the component folder) and choose **Export subset**.
2. Give the file a name; it is saved as `<name>.tsu`.

To restore, **Import subset** the `.tsu` file. Do this into a different project than the one it came from: importing into the same project makes Tosca ask to merge every object with the copies that already exist.

## Multi-user project: backing up the common repository

The backup contains all workspace objects, the project settings and properties, and, unless you exclude it, the object versioning history (see [Versioning and recovery](/ToscaBase/administration/versioning-and-recovery/)).

Prerequisites:

- Enough disk space: the backup file can be about 20 percent of the size of the repository.
- The database user needs create and drop rights for a later restore.
- You must be logged in as an administrator; a normal user cannot back up.

Steps:

1. Open the multi-user workspace and log in as an admin.
2. Go to **Project > Info** and choose **Backup the currently used common repository**.
3. Answer whether to **exclude object versioning history** from the backup (yes or no).
4. Select the destination folder (the source creates a `Backup` folder next to the workspaces) and click **OK**.

Depending on the repository size this takes minutes or hours; a small demo repository finishes instantly. The result is a single dump file with the extension `.tdp`.

:::note
The speaker says `.tdp` when the backup is written but reads the file's extension differently when selecting it for the restore; the extension is only legible on screen. Check the file Tosca writes.
:::

## Restoring a repository

Tricentis recommends restoring into a **newly created repository**. Restoring into an existing repository overwrites all data in it; Tosca warns that existing data in the affected repository will be discarded and that the transaction cannot be undone or rolled back.

1. Close the workspace; no project needs to be open.
2. Go to **Project > Info** and choose the **Restore** option (it is offered once a backup exists).
3. Read the warning about discarded data and confirm.
4. Select the backup file (`MultiDemo dump.tdp` in the source).
5. Choose the repository type for the target: `Oracle`, `MS SQL Server`, `DB2` or `SQLite`.
6. For a database server enter the connection string (schema optional) and click **Test connection**.
7. Click **OK**. The speaker stops here rather than overwrite his demo repository.

## Related

- [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/): repository types and connection strings.
- [Versioning and recovery](/ToscaBase/administration/versioning-and-recovery/): recovering a single deleted object without a restore.
