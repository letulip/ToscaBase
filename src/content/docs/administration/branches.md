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
  - id: CGNk4vGRkco
    title: "TRICENTIS Tosca 16.0 - Lesson 42 | Multi-user Workspace | Create & Manage Branch | Delete Branch"
    url: https://www.youtube.com/watch?v=CGNk4vGRkco
    at: "06:22"
---

A branch is a separate line of development inside one multi-user repository. The repository you created with your first [multi-user workspace](/ToscaBase/administration/multi-user-workspaces/) is the `Master` branch. Testers working on a new feature, a coming release, an application or a team create their objects on their own branch (Lesson 42 runs `Team A branch` and `Team B branch` side by side), and an administrator merges each branch into `Master` once the work is tested. `Master` therefore only ever receives work that has been executed and verified, and people working on different releases do not overwrite each other. The workflow is the one you know from Git: a main branch, short-lived development branches, merge, delete.

## Roles

In the demonstration one person plays every role, which the speaker admits looks confusing. In a real project:

- the **administrator** owns the `Master` workspace, creates branches and merges them;
- each **tester** creates a workspace on the branch assigned to them, works there and notifies the admin when done;
- the **team lead** reviews the branch and executes its TestCases before asking for the merge.

Nobody works directly on `Master`; Lesson 42 creates `TC01` and `TC02` there only so that the branches have something to inherit.

## Creating a branch

In the `Master` workspace, logged in as an admin (on the admin credentials in Tosca 16 see the note in [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/)):

1. Check out the root project (not required, but Lesson 42 recommends it), right-click it and choose **Create Branch**.
2. Enter a name; the sources use `Multi-RC1` ("release candidate 1") and `Team A branch`. Repeat for every branch you need.
3. Tosca confirms the branch was created and lists what to do next: save all changes in the current workspace, close it, and create a new workspace on the new branch.

So: **Check In All** (this also checks in the branch creation), close the workspace.

## Working on the branch: a workspace per branch

A branch is used through its own workspace:

1. **Create new** workspace, same repository type as `Master` (SQLite in the source).
2. Tick **Use existing repository** and select the common repository.
3. In the **Branch** field, which defaults to `Master`, pick the branch (`Multi-RC1`).
4. Name the workspace (the sources use `RC1`, `Team A`) and create it. Log in with any existing user; in a real project every team member uses their own.

The project inside looks identical to `Master`, and the workspace title even shows the same project name. Look at the title bar: the path is `RC1.tws` and the branch is `Multi-RC1`. Changes made here, checked in with **Check In All**, go to the branch, not to `Master`. In the source a new TestCase `TC3` is created and checked in on the branch.

What each side sees: objects that were in `Master` when the branch was created (`TC01`, `TC02`) appear in every branch workspace; objects checked in on a branch stay invisible in `Master` and in other branches until the merge.

:::tip
Because two workspaces can carry the same project name, always confirm the branch in the title bar before making changes.
:::

## Merging a branch into Master

When the branch is complete, tested and checked in:

1. Close the branch workspace and open the `Master` workspace (the title bar shows branch `Master`).
2. Check out the root project, right-click it and choose **Merge Branch**.
3. Select the branch to merge. With one branch it is preselected; with several, pick one.
4. Tosca warns that the branch will be permanently deleted when you check in the changed objects. Confirm.
5. The merged objects appear in `Master` (`TC3`; in Lesson 42 `Module A` and `Module B` from Team A). **Check In All**, then repeat for the next branch (`Team B branch` brings `Module C` and `Module D`).

:::note
The speaker says that conflicts during a merge are "either merged or removed" without demonstrating a conflict. The transcript gives no detail on how Tosca presents or resolves a conflicting object; expect to test this on your own repository.
:::

## Deleting a branch

Right-click the root project and choose **Delete Branch**; the dialog lists the remaining branches, pick one and confirm. A branch that was merged is already gone, and with none left the command reports that no branches are available to delete. Use it for branches that were abandoned without a merge.

## Related

- [Users and groups](/ToscaBase/administration/users-and-groups/): who is an admin.
- [Command-line tools](/ToscaBase/administration/command-line-tools/): cloning a workspace for each tester.
