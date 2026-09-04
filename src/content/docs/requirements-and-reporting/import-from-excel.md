---
title: Import a folder structure from Excel
description: Build a TestCase or component folder tree in Excel and paste it into Tosca Commander with Create Folder Structure, following the column-per-level rules.
level: 3
sidebar:
  order: 40
sources:
  - id: ob-ktPgLPIA
    title: "Tosca Tutorial | Lesson 74 - Import Folder Structures from Microsoft Excel Sheet |"
    url: https://www.youtube.com/watch?v=ob-ktPgLPIA
    at: "00:09"
---

If a test structure already exists in Microsoft Excel (a test plan, a legacy TestCase inventory, the folder layout of a new project), you do not have to recreate its folders one by one in Tosca Commander. Copy the cells and let Commander create the whole tree in one action. This is a structure import only: it creates folders, not TestCases or TestSteps.

## Example structure

The lesson uses the vehicle-insurance sample application and the recommended pre-processing / process / post-processing layout (see [TestCase structure](/ToscaBase/best-practices/test-case-structure/)):

```
Vehicle Insurance Offer
    Pre-processing
        Open Application
    Process
        Select Vehicle Data
        Enter Vehicle Data
        Enter Personal Data
        Enter Insurance Data
        Choose Product
        Premium Calculation
        Check Premiums
    Post-processing
        Close Application
```

In the worksheet the root name sits in column A, `Pre-processing`, `Process` and `Post-processing` in column B, their children in column C, and any deeper level in column D.

## Rules for the worksheet

- Objects are laid out **hierarchically in columns from left to right**: the parent in the leftmost column, each child level one column further right.
- **Objects of the same level share the same column.**
- **One value per row.** A row never carries two names.
- **Fewer than 15 levels.**

If any rule is broken the structure will not import as intended.

## Import steps

1. In Excel select every row of the structure and press **Ctrl+C**.
2. In Tosca Commander create or choose the target folder. Any folder works (a TestCases folder, for instance), but the recommended target is a **component folder**, for example `Import from Excel`.
3. Right-click the folder **> Create Folder Structure**. Commander builds the tree from the copied cells.
4. Right-click **> Expand All** to check the result: every folder from the worksheet exists, nested exactly by column.

:::note
The speaker mentions keyboard shortcuts for the create action and names them as Ctrl+N and Ctrl+S; the subtitles are unclear here, so use the context menu entry if in doubt.
:::

:::caution
Sibling folders may come out in a different order than in the worksheet (`Process` before `Pre-processing`, for example). Reorder them by hand afterwards.
:::

## When it helps

- Migrating a test inventory that was maintained in Excel before Tosca.
- Bootstrapping the folder skeleton of a new project from a test plan.
- Importing a requirements-style structure agreed with the business, which you then fill with TestCases and link to [requirements](/ToscaBase/requirements-and-reporting/requirements-and-risk/).
