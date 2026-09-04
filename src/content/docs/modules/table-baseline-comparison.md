---
title: Table baseline comparison
description: Save a snapshot of a web table as a baseline, compare later executions against it, exclude dynamic rows and columns, and update or auto-generate baselines.
level: 1
sidebar:
  order: 80
sources:
  - id: u33y-Vu12fQ
    title: "Tosca Tutorial | Lesson 47 - Use Baseline Comparison for Table Control | Compare Web Tables |"
    url: https://www.youtube.com/watch?v=u33y-Vu12fQ
    at: "02:11"
  - id: ykanlKKy8tY
    title: "TRICENTIS Tosca 16.0 - Lesson 76 | OBSTACLE #34 | Table Baseline Comparison | Store Baseline Table"
    url: https://www.youtube.com/watch?v=ykanlKKy8tY
    at: "04:07"
---

Web tables are dynamic: cell values change between runs, and sometimes the structure changes too. Verifying every cell by hand does not scale. Tosca's **table compare** lets you take a snapshot of a table control, the **baseline**, when its content is correct according to the requirements, and then verify at each execution that the current table still matches it. A difference fails the TestStep and the log shows what changed. It is meant for content that should *not* change; rows and columns that legitimately vary are excluded from the comparison. The table control itself is explained in [Table controls](/ToscaBase/modules/table-controls/).

Lesson 47 uses the sample insurance application: a Module `Select price option` containing the price table, in a TestCase `Compare table baseline`. Lesson 76 solves obstacle 34 of the Tricentis Obstacle Course, *Find the changed cell*, with the same feature.

## Create a baseline manually

1. Drag the Module into the TestCase so that the table with its rows and columns is in the TestStep. Open the application at the page with the table.
2. Select the table node in the TestStep and click **Create baseline**: the last command on the **TestCases** tab of the ribbon, or the same entry in the node's right-click menu (Lesson 76, Tosca 16).
3. Tosca reads the table that is currently open in the application, stores all its values (a progress percentage runs for a few seconds on a large table) and confirms that the baseline was created.

Afterwards the table node holds a **table compare expression** as its value with ActionMode `Verify`, and a baseline object with its creation time appears under the table in the TestCase.

## Exclude rows and columns

Anything that is allowed to change must be excluded, otherwise every run fails.

- **By row name.** Under the table, add a row and type its name, for example `Select option` (the row of radio buttons in the price table). Because the node is under a baseline comparison, the ActionMode is set to `Exclude` automatically.
- **By cell value or column.** Exclusion also works at column level and by condition on a cell value: the source mentions excluding where a cell contains `limited` or the column is `Platinum`. Set the condition on the row or column node in the same way.

The baseline now acts as the expected result for every later comparison.

## Run the comparison

Add the TestCase to an ExecutionList and execute it (see [Execution lists](/ToscaBase/execution/execution-lists/)). With the application unchanged the TestStep passes and the result shows that the verification against the baseline succeeded.

To see a failure, Lesson 47 changes the insurance sum on the *Enter product data* page, which changes the yearly prices in the table. The next execution fails, and the result lists the details: *verification failed*, the column that was modified, expected versus actual values, the affected row, and a screenshot. Both **values** and **structure** are compared, so a changed table layout is reported as well, which is a defect to raise with the development team.

The failure log also works as a diff tool. In obstacle 34 the page changes one random cell of a large table; the eye cannot find it, Tosca can. Scan only the table, create the baseline while the original table is shown, switch the page to the changed table and run the TestCase in ScratchBook. It fails with the message that column *X* in row *23* was modified, with expected (original) and actual (changed) values; those four items are what the obstacle asks for. A run in ScratchBook compares against the baseline just like an ExecutionList run.

## Update the baseline

When a change is intended, replace the snapshot instead of editing values:

1. In the ExecutionList, select the TestCase.
2. On the **ExecutionList** tab of the ribbon click **Update baseline**. Tosca confirms that the baseline of the table was updated to the snapshot from this execution.

The next execution is compared with the new baseline.

## Automatic baselines

**File > Settings > TBox > Engines > Table compare > Enable autogenerate baseline** set to `True` makes Tosca create a baseline automatically on execution. The source leaves it at `False` and recommends the manual route: create a baseline deliberately when the table is known to be right, and update it when a change is approved. An automatic baseline would happily snapshot a wrong table.

## When to use it

- Large tables with many rows and values, where a cell-by-cell verification is impractical.
- Streaming or feed-driven tables that must be compared repeatedly against a known-good state.
- Regression protection for table structure.

Not for tables whose content is expected to change every run; exclude those rows or columns, or verify them with constraints and cell verifications as in [Table controls](/ToscaBase/modules/table-controls/).
