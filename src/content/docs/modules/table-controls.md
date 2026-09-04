---
title: Table controls
description: How a scanned table is structured in a Module, the row, column and cell selectors, the ActionModes and properties for tables, worked steering examples, embedded controls inside cells, and verifying row and column counts.
level: 1
sidebar:
  order: 70
sources:
  - id: J24QB9a78hY
    title: "Tosca Tutorial | Lesson 155 - Steering Table Controls | Table Structure | Table Properties | Example"
    url: https://www.youtube.com/watch?v=J24QB9a78hY
    at: "00:10"
  - id: ojiutjOB61w
    title: "Tosca Tutorial | Lesson 45 - Creating & Handling Embedded Controls Inside Table | Table Control |"
    url: https://www.youtube.com/watch?v=ojiutjOB61w
    at: "00:08"
  - id: O5DWq3HSn3c
    title: "Tosca Tutorial | Lesson 46 - Verify Row and Column Count of a Web Table | Table Controls |"
    url: https://www.youtube.com/watch?v=O5DWq3HSn3c
    at: "00:07"
---

A table scanned with XScan becomes a TBox table control: a ModuleAttribute with a fixed inner structure of rows, columns and cells. In the TestCase you do not address a cell by its HTML; you say which row, which column and which cell, using selectors, constraints and properties that Tosca provides for every table. This doc covers the structure, the selectors, the ActionModes and properties, and the standard steering patterns. Problem tables (shuffled rows, `div` tables, unknown row counts) are in [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/); comparing a table against a saved snapshot is in [Table baseline comparison](/ToscaBase/modules/table-baseline-comparison/).

## Structure

When you drag a Module with a table into a TestCase, the TestStep shows the table with two child nodes, **Row** and **Column**. A row has cells; a column has cells too. So there are three levels to steer: the row (or column), then a cell inside it, then the cell's value or property. XScan reports the control with tag type `table`.

In the Module, the table has a **header row** setting under its properties. It defaults to the first row; change it if the header is elsewhere.

## Selectors for rows, columns and cells

The same selectors work on rows, columns and cells:

| Selector | Meaning |
|---|---|
| `$1`, `$2`, `$3` ... | Row, column or cell at that fixed position |
| `$last` | The last row, column or cell |
| `$header` | A cell in the table header |
| *last content row* | The last row that has a value |
| *first empty row* | The first row without a value |
| `#2` | The second match when a constraint matches several rows (see example 4) |

:::note
The speaker reads the last two selectors aloud (*last content row*, *first empty row*) without showing the spelling. Look them up in the value drop-down of the row node before using them.
:::

## ActionModes on tables

The usual ActionModes apply, with table-specific meaning:

- **Input**: enter a value into a cell.
- **Verify**: verify a cell value or a table property.
- **Constraint**: restrict the search. A constraint on a cell selects the row (or column) where that cell has the given value; the rest of the TestStep then acts on that row.
- **Buffer**: store the value of a cell, row or column in a Buffer; see [Buffers](/ToscaBase/data-and-parameters/buffers/).

ActionModes in general are in [ActionModes](/ToscaBase/test-cases/action-modes/).

## Table properties

Set on the table node (or a row/column/cell node) by choosing the property instead of a value:

| Property | Returns |
|---|---|
| `ColumnCount` | Number of columns |
| `RowCount` | Number of rows |
| `ColumnNumber`, `RowNumber` | Index of the selected column or row, counted from 0, relative to the header column or row |
| `RawColumnNumber`, `RawRowNumber` | The same index counted from 1 |
| `ResultCount` | Number of cells containing the specified content |

## Steering examples

All examples use the obstacle-list table of the Tricentis Obstacle Course (columns include `ID`, `Name`, `Category`), scanned into a Module `Obstacle list`. Each example is one TestStep of the Module.

1. **Fixed row position.** Row `$3`, cell `Name`, ActionMode `Verify`, value `Not a table`. Use only when the row number never changes.
2. **Row by a cell value (constraint).** Row, cell `Name` = `Fun with tables` with ActionMode `Constraint`; cell `Category` = `hard` with `Verify`. Tosca searches every row for the constraint value and selects the matching row. Two constraints (for example `ID` and `Name`) narrow further when one value is not unique.
3. **Row by value, without constraint.** Put the value directly on the row node: row = `Wait a moment`, then cell `Category` = `easy` with `Verify`. Works only when the value is unique across all rows; it is faster than a constraint on a large table, because a constraint has to filter the rows.
4. **The n-th matching row.** Row `#2`, cell `Category` = `easy` with `Constraint`, cell `Name` = `Twins` with `Verify`. Several rows have category `easy`; `#2` takes the second of them.
5. **Row and column count.** On the table node choose property `RowCount`, ActionMode `Verify`, value `12`. The same with `ColumnCount`; the speaker's guess of `10` fails because the table has nine columns. The verification runs at table level, so the log shows less detail than a cell verification.
6. **Buffer a cell.** Column `Name`, cell `$5`, property `Text`, ActionMode `Buffer`, value `p_name`. The Buffer receives `Fun with tables`, visible afterwards in the Buffer Viewer.

The pattern is always the same: first find the row or column by a search criterion, then act on a cell in it.

## Verify row and column count with a Buffer

Example 5 verifies the count directly. The other source does it in two steps, which is useful when the expected number is computed elsewhere:

1. Table node → property `RowCount`, ActionMode `Buffer`, value `rowcount`.
2. TestStep `TBox Evaluation Tool` with the expression `{B[rowcount]}==5`.
3. Same for `ColumnCount` into `columncount`, evaluated against `4`.

On the sample table the header row is counted: four data rows give `RowCount = 5`. See [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/) for the expression syntax.

## Embedded controls inside a table

A button or link that appears in every row (a *Go for it* link in the obstacle list) is scanned by XScan as a control **next to** the table, not inside a row. All such links share the same properties, so a click fails with *more than one control found*. The fix is to make the control part of a cell, so that it is addressed through the row.

**Way 1, rearrange the scanned control.** Scan the table and one link (ignore *not unique*). In the Module, drag the link attribute into the cell of the row that contains it. The tree now reads table → row → cell → link. Re-add the Module to the TestCase: row `$1`, cell `Action` with ActionMode `Select`, link → click. The click lands on the first row's link.

**Way 2, create the embedded control by hand.** With only the table scanned:

1. In the Module, right-click the cell under the row, open the **...** menu and choose **Create embedded link control** (other control types are offered). Name it, for example `Go`.
2. Right-click the new control, open **...** again and **Create technical ID parameter**. Add the properties you know: `tag` = `a`, and optionally `InnerText` = `Go for it`. Without technical properties the control only works while there is a single link in the cell.
3. In the TestCase: row `$1`, cell `Action` → `Select`, `Go` → type the click method by hand; the drop-down does not offer it for a custom control.

Both ways work for any container, not only tables. The same technique solves obstacle 5 in [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).
