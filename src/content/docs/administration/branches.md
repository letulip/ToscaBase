---
title: Branches
description: Create a branch of a multi-user repository, work on it in a separate workspace, merge it back into Master and delete it, following a Git-like workflow.
level: 4
sidebar:
  order: 30
sources:
  - id: M6J7EqEjjco
    title: "Tosca Tutorial | Lesson 92 - Create, Merge and Delete Branches | Multi-User Workspace |"
    url: https://www.youtube.com/watch?v=M6J7EqEjjco
    at: "00:07"
---

A branch is a separate line of development inside one multi-user repository. The repository you created with your first [multi-user workspace](/ToscaBase/administration/multi-user-workspaces/) is the `Master` branch. Testers working on a new feature or a coming release create their objects on their own branch, and an administrator merges the branch into `Master` once the work is tested. `Master` therefore only ever receives work that has been executed and verified, and people working on different releases do not overwrite each other. The workflow is the one you know from Git: a main branch, short-lived development branches, merge, delete.

## Roles

In the demonstration one person plays every role, which the speaker admits looks confusing. In a real project:

- the **administrator** owns the `Master` workspace, creates branches and merges them;
- each **tester** creates a workspace on the branch assigned to them, works there and notifies the admin when done.

## Creating a branch

In the `Master` workspace, logged in as an admin:

1. Right-click the root project and choose **Create Branch**.
2. Enter a name; the source uses `Multi-RC1` for "release candidate 1".
3. Tosca confirms the branch was created and lists what to do next: save all changes in the current workspace, close it, and create a new workspace on the new branch.

So: **Check In All**, close the workspace.

## Working on the branch: a workspace per branch

A branch is used through its own workspace:

1. **Create new** workspace, same repository type as `Master` (SQLite in the source).
2. Tick **Use existing repository** and select the common repository.
3. In the **Branch** field, which defaults to `Master`, pick the branch (`Multi-RC1`).
4. Name the workspace (the source uses `RC1`) and create it. Log in with any existing user.

The project inside looks identical to `Master`, and the workspace title even shows the same project name. Look at the title bar: the path is `RC1.tws` and the branch is `Multi-RC1`. Changes made here, checked in with **Check In All**, go to the branch, not to `Master`. In the source a new TestCase `TC3` is created and checked in on the branch.

:::tip
Because two workspaces can carry the same project name, always confirm the branch in the title bar before making changes.
:::

## Merging a branch into Master

When the branch is complete, tested and checked in:

1. Close the branch workspace and open the `Master` workspace (the title bar shows branch `Master`).
2. Right-click the root project and choose **Merge Branch**.
3. Select the branch to merge. With one branch it is preselected.
4. Tosca warns that the branch will be permanently deleted when you check in the changed objects. Confirm.
5. The merged objects appear in `Master` (`TC3` in the source). **Check In All**.

:::note
The speaker says that conflicts during a merge are "either merged or removed" without demonstrating a conflict. The transcript gives no detail on how Tosca presents or resolves a conflicting object; expect to test this on your own repository.
:::

## Deleting a branch

Right-click the root project and choose **Delete Branch**. A branch that was merged is already gone, and the command reports that no branches are available to delete. Use it for branches that were abandoned without a merge.

## Related

- [Users and groups](/ToscaBase/administration/users-and-groups/): who is an admin.
- [Command-line tools](/ToscaBase/administration/command-line-tools/): cloning a workspace for each tester.
