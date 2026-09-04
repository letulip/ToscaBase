---
title: Troubleshooting
description: Automation obstacles (duplicate IDs, dynamic tables, hidden elements, drag and drop) and common real-world problems, each with problem, cause and fix.
level: 3
sidebar:
  order: 0
---

This section is organised by symptom. The first three docs walk through the Tricentis *Obstacle Course*, a public page of automation riddles that reproduce what goes wrong in real applications; every obstacle is written up as **Problem / Cause / Solution**. The fourth doc covers questions that come up in projects but have no dedicated module. The last one is a full end-to-end walkthrough that ties the techniques together.

| Doc | What it fixes |
|---|---|
| [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/) | *Selected item is not unique*, twins, IDs that change between clicks, multi-select lists (cardinality, `ExplicitName`), autocomplete boxes (`SENDKEYS`, `ResultCount`), hidden elements, controls outside the viewport (`ScrollingBehavior`). |
| [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/) | Tables made of `div`s (anchor identification), rows that move (`Constraint`), `RowCount`, `$last` / `$lastContentRow`, searching cells with `Exists`, addressing cells by row and column header, drop-downs embedded in cells with `{XB[...]}`. |
| [Obstacles: input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/) | `{DRAG}` / `{DROP}`, clicking until a label changes (`While`), escaping values, `{CLICK}` with `OffsetHorizontal`, the *Click On Screen* module. |
| [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/) | Switching browser tabs with `TBox Send Keys`, counting all links on a page, downloading a file with `curl` and verifying it. |
| [Worked example: end-to-end live project](/ToscaBase/troubleshooting/worked-example-live-project/) | Finishing the vehicle-insurance sample: conditional template folders, data-driven choices, `WaitOn`, ExecutionList reporting. |

Read the obstacle docs after [Control identification](/ToscaBase/modules/control-identification/), [Table controls](/ToscaBase/modules/table-controls/) and [ActionModes](/ToscaBase/test-cases/action-modes/); they assume those basics and show them under pressure.
