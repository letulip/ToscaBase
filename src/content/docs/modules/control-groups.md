---
title: Control groups
description: Group related ModuleAttributes into a control group in XScan, name the group, and split it back into separate attributes when it no longer helps.
level: 1
sidebar:
  order: 90
sources:
  - id: EMsHHgKDvEU
    title: "TRICENTIS Tosca 16.0 - Lesson 07 | Identify controls by Properties & Anchor | Create Control Groups"
    url: https://www.youtube.com/watch?v=EMsHHgKDvEU
    at: "20:55"
---

A control group is a folder inside a Module: a named node that holds several ModuleAttributes. It changes nothing about how the controls are identified; it only organises them, so that a Module with dozens of attributes reads as a few groups (*Product category links*, *Filter buttons*, *Address fields*) instead of a flat list. Groups are created and dissolved in XScan, the same tool that scans the controls; see [XScan](/ToscaBase/modules/xscan/).

## When to use one

- A page has many controls of the same kind: every link of a category menu, every button of a toolbar, every text box of a form. Grouping by type is what the source does.
- Controls belong together functionally and are always steered together, for example the fields of one address block.
- A Module is long enough that finding an attribute in the list takes time. Groups can be collapsed in the Module tree.

Do not group as a substitute for splitting: a page that needs three groups of unrelated controls is usually better scanned as three Modules by functionality, see [Module hygiene](/ToscaBase/best-practices/module-hygiene/).

## Create a control group

1. Scan the controls into the Module as usual and make each one unique first; in the source the category links are made unique by anchor, see [Control identification](/ToscaBase/modules/control-identification/).
2. In XScan (Advanced view), select all the controls that belong together.
3. Right-click the selection and choose **Convert to control group**. XScan replaces the selected controls with one group node and nests them under it.
4. Rename the group node (`Product category links`). Expand it to check that every control is inside.
5. **Save** or **Finish screen** as with any scan.

The Module now shows the group as a node with the attributes as children.

## Dissolve a control group

Right-click the group node in XScan and choose **Convert to separate XModuleAttributes**. The attributes return to the Module level as ordinary controls; nothing about their identification changes.

## What the source does not show

The lesson creates and dissolves the group in XScan only. It does not show the group in a TestCase or explain whether the group node can be steered as a unit; treat it as a naming and ordering aid until you have checked in your own workspace. Grouping is also unrelated to [Rescan](/ToscaBase/modules/rescan-modules/): a rescanned Module keeps its groups, and new controls are added at the level where you put them.
