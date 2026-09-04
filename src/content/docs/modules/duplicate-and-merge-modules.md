---
title: Duplicate and merge Modules
description: Find duplicate Modules in the workspace and merge them with the Module merge assistant, including resolving attribute conflicts and what happens to TestCases that use the merged Module.
level: 1
sidebar:
  order: 50
sources:
  - id: UVOH_DevQAc
    title: "Tosca Tutorial | Lesson 10 - Find Duplicate Modules | Merge Modules | Merge Module Assistant |"
    url: https://www.youtube.com/watch?v=UVOH_DevQAc
    at: "02:04"
  - id: VT4f_mHizH4
    title: "Tosca Tutorial | Lesson 104 - Merge Duplicate Modules | Workspace Performance | Best Practices |"
    url: https://www.youtube.com/watch?v=VT4f_mHizH4
    at: "03:13"
---

In a team, the same screen gets scanned more than once: the existing Module is badly named, hard to find among hundreds, or nobody is sure it does what its name says, so someone scans again. Each copy adds objects to the workspace, and every change to the screen must then be made in every copy. Tosca's **Module merge assistant** finds such duplicates and merges them into one Module, re-linking every TestCase that used the removed copy. Why this matters for workspace size and performance is in [Module hygiene](/ToscaBase/best-practices/module-hygiene/); this doc is the procedure.

Both sources demonstrate on a login form (username, password, login button) scanned twice, or copied to simulate a duplicate.

## Where the commands are

Select a Module in the **Modules** section and open the **Modules** tab of the ribbon. Two commands matter:

- **Find duplicate Modules**: searches the workspace for Modules whose ModuleAttributes match the selected one.
- **Merge Modules**: enabled when two Modules are selected; opens the merge dialog directly.

## Way 1: find duplicates, then merge

1. Select the Module you want to keep looking for duplicates of, and click **Find duplicate Modules**. Tosca searches the whole workspace and lists every Module with the same attributes.
2. The Module you selected is the **source**. Choose one of the listed Modules as the **target** (a target can be set on any of them). **Merge selected** becomes enabled.
3. Click **Merge selected**. Tosca runs its checks and reports them: the target Module was not changed, no usages were still linked to the source, the source Module is deleted.

If the attributes match exactly there are no conflicts and nothing else to do.

:::note
The two sources disagree on naming. Lesson 10 says the target is renamed with the source's name after the merge; Lesson 104 says the target is left unchanged. Both agree that the target's attributes are kept and the source is deleted. Check the resulting name after merging.
:::

## Way 2: select two Modules and merge

Use this when you already know the two Modules are the same, or when their attributes differ and you want to decide what survives.

1. Select both Modules (`Login page` and `Login page_2` in the source) and click **Merge Modules**.
2. The dialog shows the **target** and the **source** with their attributes side by side, and three commands: **Merge**, **Switch Modules** and **Show**.
3. **Switch Modules** swaps which one is the target. The target is the final Module, so the Module with the better name and complete attributes should be the target.
4. Attributes that exist in the source but not in the target are shown as differences. For each you can **link** it into the target (keep it) or **unlink** it (drop it). Linking and unlinking can be undone before merging. In the source, `Login page_2` lacks the login button; with `Login page_2` as target the button would be removed, so the speaker switches them.
5. Click **Merge**. Tosca reports what it did: change rights checked, *n* ModuleAttributes updated in the target, usages re-linked, source deleted.

## What happens to TestCases

Every TestStep that used the source Module is re-linked to the target Module. Nothing in the TestCases has to be edited by hand. If an attribute was unlinked during the merge, TestSteps that used it lose that TestStepValue, so review the differences list before you click **Merge**.

## Make it routine

The merge assistant only finds Modules whose attributes match, so it catches identical scans, not two half-scans of one page. Run **Find duplicate Modules** regularly, not only when something breaks, and pair it with a [naming convention](/ToscaBase/best-practices/naming-conventions/) so that the next tester finds the existing Module instead of scanning a new one. If a page needs one more control, use [Rescan](/ToscaBase/modules/rescan-modules/) on the existing Module.
