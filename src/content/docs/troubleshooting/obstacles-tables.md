---
title: "Obstacles: tables"
description: Fake tables built from divs, rows that move, rows dragged into another table in order, counting rows, last-row values, cell search, row and column headers, and drop-downs embedded in cells.
level: 3
sidebar:
  order: 20
sources:
  - id: k6AQZELm3H4
    title: "Tosca Tutorial | Lesson 109 - Not a Table | Dynamically changing Table Element | Obstacle 3"
    url: https://www.youtube.com/watch?v=k6AQZELm3H4
    at: "02:16"
  - id: dWayq96UL1M
    title: "Tosca Tutorial | Lesson 111 - Complex Table Interactions | Dynamic Rows | Obstacle 5"
    url: https://www.youtube.com/watch?v=dWayq96UL1M
    at: "02:14"
  - id: vjxpW60gvXs
    title: "Tosca Tutorial | Lesson 115 - Drag and Drop Table Rows | Repetition | Obstacle 9 |"
    url: https://www.youtube.com/watch?v=vjxpW60gvXs
    at: "01:13"
  - id: GeBgfUdwM-E
    title: "Tosca Tutorial | Lesson 124 - Count Number of Rows | Dynamic Web Table | RowCount | Obstacle 18"
    url: https://www.youtube.com/watch?v=GeBgfUdwM-E
    at: "02:15"
  - id: 2cSYF98wQb8
    title: "Tosca Tutorial | Lesson 125 - Get Last Table Row Value | LastContentRow | Obstacle 19"
    url: https://www.youtube.com/watch?v=2cSYF98wQb8
    at: "02:18"
  - id: WMatBr3w8UI
    title: "Tosca Tutorial | Lesson 127 - Search Table Cell Value | Constraint Action Mode | Obstacle 21"
    url: https://www.youtube.com/watch?v=WMatBr3w8UI
    at: "02:16"
  - id: ULBjqXHmDjs
    title: "Tosca Tutorial | Lesson 128 - Meeting Scheduler Table | Buffer Action Mode | Obstacle 22"
    url: https://www.youtube.com/watch?v=ULBjqXHmDjs
    at: "03:20"
  - id: UQpoXy-e3no
    title: "Tosca Tutorial | Lesson 129 - Dropdown Table | Dynamic XBuffer | Embedded Controls | Obstacle 23"
    url: https://www.youtube.com/watch?v=UQpoXy-e3no
    at: "03:16"
---

Most real-world steering problems live in web tables: rows move between page loads, the row count is unknown, a "table" is a pile of `div` elements, or a control sits inside a cell but XScan placed it outside the row. The toolset is small: the `Constraint` ActionMode to pick a row, `Buffer` to read a cell, the properties `RowCount`, `ColumnCount` and `ResultCount`, row selectors such as `$last`, `{XB[...]}`, embedded controls, and the `Repetition` folder property. Concepts are in [Table controls](/ToscaBase/modules/table-controls/) and [ActionModes](/ToscaBase/test-cases/action-modes/).

Routine for every obstacle: scan a Module into an *Obstacles* folder, create a TestCase named after the obstacle, drag the Module in, set Workstate *Completed*, run in ScratchBook.

## Not a table (obstacle 3)

**Problem.** Clicking *Generate order ID* adds an order number to a table-like block, at a random row. Buffer the number and type it into a text box.

**Cause.** XScan shows no rows or cells: the "table" is nested `div` elements. The order-number `div` has a dynamic `InnerText` and nothing else distinguishing; without `InnerText` it is one `div` among many.

**Solution.**

1. Raise the **filtered items** level until the order-number `div` is listed.
2. Untick `InnerText` and switch from *Identify by properties* to *Identify by anchor*.
3. Drag the `div` with the static label *Order ID* into the anchor slot: wherever the row lands, the label is next to the number, so the item is unique.
4. Lower the filter level, add the *Generate order ID* link and the text box, rename the number attribute to `Order ID`.
5. TestCase: link → `X`; `Order ID` → property `InnerText`, ActionMode `Buffer`, value `orderId`; text box → `{B[orderId]}`.

Anchor identification is described in [Control identification](/ToscaBase/modules/control-identification/).

## Complex table interactions (obstacle 5)

**Problem.** Click the *Edit* button in the row of *John Doe*. Every refresh shuffles the rows, and two rows have the first name *John*.

**Cause.** The row index is meaningless, and XScan puts the scanned *Edit* button next to the table instead of inside a row.

**Solution.**

1. Scan the table and one *Edit* button (ignore *not unique*) and make the button an embedded control of the row, as described in [Embedded controls inside a table](/ToscaBase/modules/table-controls/#embedded-controls-inside-a-table).
2. TestCase: in the row, cell *First name* = `John` and cell *Last name* = `Doe`, both with ActionMode `Constraint` (one is not enough because *John* appears twice); *Edit* → `X`.

Two constraints filter to exactly one row regardless of its position; the click applies to that row's button.

## To-do list (obstacle 9)

**Problem.** Two tables, *To-do tasks* and *Completed tasks*. Drag every row of the first table into the second, in the order of the *ID* column (1 to 6).

**Cause.** A single drag and drop is solved with `{DRAG}` and `{DROP}` as in [Drag and drop image](/ToscaBase/troubleshooting/obstacles-input-and-clicks/#drag-and-drop-image-obstacle-8). The difficulty is doing it six times, on a different row each time, without six copies of the TestStep.

**Solution.**

1. Module: both tables.
2. TestCase: create a folder `Repetition`, move the table TestStep into it and set the folder's [Repetition](/ToscaBase/test-cases/repetitions/) property to `6`.
3. In the *To-do tasks* table choose the column *ID* and give the cell the value `{REPETITION}`. The expression returns the current pass number (1, then 2, and so on), so each pass addresses the row whose ID equals it.
4. That row → `{DRAG}`, ActionMode `Input`.
5. *Completed tasks* table → `{DROP}`, with no row or column: the row is dropped into the table as a whole.

Pass number and ID advance together, so the rows move in order. Any unique column numbered 1 to *n* can play the role of *ID*.

:::note
The subtitles garble the expression name; it is `{REPETITION}`. The speaker does not say which ActionMode the *ID* cell uses; `Constraint` (obstacle 5) is the natural fit.
:::

## Lots of rows (obstacle 18)

**Problem.** Count the rows of a table, type the count into *Row count*, click the button. The table changes size after each click, so a static number does not work.

**Cause.** The row count is only known at run time.

**Solution.** A table control exposes `RowCount` and `ColumnCount`.

1. Module: table, text box, button.
2. Table → property `RowCount`, ActionMode `Buffer`, value `rows`.
3. Text box → `{B[rows]}`; button → `X`.

## Last row (obstacle 19)

**Problem.** Verify that the last row shows an order value and copy that value into a text box. Neither the value nor the number of rows is constant.

**Cause.** The row index of "the last row" changes.

**Solution.** In the table's row attribute use a row selector from the drop-down instead of a number: `$last` selects the last row; `$lastContentRow` does the same here. In the cell of the *Value* column set ActionMode `Buffer` with value `b_val`, and enter `{B[b_val]}` into the text box.

The drop-down also offers `$1`, `$n`, the header row and the first empty row, so any row can be addressed without hard-coding its position.

## Table search (obstacle 21)

**Problem.** A dynamic table; find whether any cell contains the value `15` and type `true` or `false` into a text box.

**Cause.** The value may appear in any row and any column, or not at all.

**Solution.**

1. Module: the table and the text box.
2. TestCase: in the row, set a cell to `15` with ActionMode `Constraint`. Tosca filters the rows to the one containing that cell, in any column.
3. On the row, use the property `Exists` with ActionMode `Buffer` and value `b_exists`. The buffer receives `True` if the constrained row was found and `False` otherwise.
4. Text box → `{B[b_exists]}`.

Constraint plus `Exists` is the fastest whole-table search.

## Meeting scheduler (obstacle 22)

**Problem.** A timetable with times as row headers and weekdays as column headers. Read the status (*open* / *closed*) for Thursday, 11–13, and type it into a text box.

**Cause.** None; row and column are given, only addressing a cell by headers is new.

**Solution.**

1. Module: the timetable and the result text box.
2. TestCase: in the row attribute, type the row header text (`11 - 13`, as it appears on the page). Tosca selects the row by that text as long as it is unique.
3. Cell: choose the column `Thursday` from the column headers, ActionMode `Buffer`, value `b_status`.
4. Text box → `{SENDKEYS "{B[b_status]}"}`.

:::note
A dynamic time would have to be buffered or constrained first; the speaker mentions this but does not show it.
:::

## Drop-down table (obstacle 23)

**Problem.** Each row has a task like *Select the word that starts with letter M* and a drop-down; *Generate* changes the letters. For each row select the only matching word, then *Submit*.

**Cause.** The letter is unknown until run time, and XScan places the scanned `select` outside the row.

**Solution.**

1. Module: *Generate*, *Submit*, the table, and one drop-down (not unique; fine). Make the `select` an [embedded control](/ToscaBase/modules/table-controls/#embedded-controls-inside-a-table) of the cell, so that it exists in every row.
2. TestCase:
   - *Generate* → `X`.
   - Row `$2` (row 1 is the header). First cell → ActionMode `Verify`, value: the constant text followed by `{XB[letter]}`. The dynamic XBuffer verifies the fixed part and stores the changing letter in `letter` at the same time.
   - Second cell → ActionMode `Select` (Tosca defaults to `Verify`). Nested drop-down → `{B[letter]}*`: the word starting with that letter, whatever follows.
   - Copy the row block for rows `$3` to `$6`, changing only the row number. Each row overwrites the same buffer.
   - *Submit* → `X`.

`{XB[...]}` is covered in [Buffers](/ToscaBase/data-and-parameters/buffers/).
