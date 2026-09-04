---
title: Versioning and recovery
description: Manage the version history of a multi-user repository, read the change history of a project or a tree, and recover a deleted TestCase with Export subset for revision.
level: 4
sidebar:
  order: 50
sources:
  - id: L3gBI9u0VAc
    title: "Tosca Tutorial | Lesson 145 - Common Problems & Fixes | Recover Deleted Objects | Versioning |"
    url: https://www.youtube.com/watch?v=L3gBI9u0VAc
    at: "00:12"
---

Deleting an object in a multi-user workspace and checking in looks final: there is no undo for a check-in and no "restore deleted object" command. But when **versioning** is enabled for the repository, every check-in creates a revision, and any object can be brought back from a revision that still contained it. The same mechanism reverts an object to an earlier state. This doc covers the versioning settings, the change history views, and the recovery procedure step by step.

## Versioning settings

The **Versioning** tab on the menu bar of a multi-user workspace has three commands:

- **View change history for project**: every revision of the whole project. Selecting a revision shows what it did: in which folder an object was updated, deleted or added, with the object's unique ID for searching.
- **View recovered and lost objects**: a search for objects that were lost; empty in a healthy workspace.
- **Manage versioning**: shows whether versioning is enabled and lets you trim or disable it:
  - **Delete this day and older**: pick a date; versions from that date back are removed.
  - **Delete this revision and older**: enter a revision number; that revision and everything below it are removed.
  - **Disable versioning**: Tosca warns that this permanently deletes the entire version history and asks to confirm.

:::caution
Versioning stores a number of versions of every object, so an enabled repository grows. Keep it enabled anyway unless disk space is a hard constraint: it is the only way back after a mistaken delete, a corrupted workspace, or an object you cannot check in. Trim old revisions instead of disabling.
:::

## Change history of an object or a tree

Right-click any folder or object and open the **Versioning** submenu:

- **View change history**: revisions of this object alone.
- **View change history for tree**: revisions of the object and everything under it. This is the one to use for recovery, because it shows which revision deleted which child objects.
- **Export subset for revision**: writes the tree as it was in a chosen revision to a `.tsu` subset file.

## Recovering a deleted object

Scenario from the source: a folder holds `TC1`, `TC2`, `TC3`. `TC3` is deleted by mistake and **Check In All** is run. Later `TC4` is added and checked in as well.

1. Right-click the folder and choose **Versioning > View change history for tree**. Find the revision in which the object was deleted (revision 30 in the source: four objects deleted, `TC3` among them). Note the last revision **before** it that still contained the object (revision 26: one object added, listing `TC1`, `TC2`, `TC3`).
2. Close the history. Right-click the folder again and choose **Versioning > Export subset for revision**. Tosca asks for a revision number in the available range (1 to 30); enter the earlier one (26).
3. Save the subset (`TC3.tsu` in the source) and wait for the message that the export for the revision finished.
4. Check out the project root. **Import subset** is greyed out when only a folder is checked out because the import may touch objects in several sections (Modules, Execution); checking out the project enables it.
5. **Import subset** the file. Tosca reports mergeable objects (in the source a standard Module that already exists) and offers to import them as copies or merge them; choose merge.
6. The import creates a new folder (`TestCase import`) containing every object of the exported revision, not just the deleted one; it does not merge into the original folder. Move the recovered object (`TC3`) into its original folder and delete the imported duplicates.
7. **Check In All**. The workspace is back in the state before the deletion, with `TC4` kept.

:::tip
Any revision can be exported, not only the one before a delete. To revert an object to how it was two weeks ago, export the subset for that revision and import it the same way.
:::

## Related

- [Backup and restore](/ToscaBase/administration/backup-and-restore/): a whole-repository backup, which can include or exclude this version history.
- [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/): check-out and check-in.
