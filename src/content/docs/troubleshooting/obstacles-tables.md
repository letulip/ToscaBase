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
  - id: 4gM7fyyRJpE
    title: "TRICENTIS Tosca 16.0 - Lesson 45 | OBSTACLE#3 | Dynamically changing Table Elements – Not a Table |"
    url: https://www.youtube.com/watch?v=4gM7fyyRJpE
    at: "01:14"
  - id: vPB8nzD54Hs
    title: "TRICENTIS Tosca 16.0 - Lesson 47 | OBSTACLE#5 | Complex Table Interactions | Dynamic Rows |"
    url: https://www.youtube.com/watch?v=vPB8nzD54Hs
    at: "01:15"
  - id: 6sOxIsT81YI
    title: "TRICENTIS Tosca 16.0 - Lesson 37 | Drag & Drop Operations | Web Table | Repetition |"
    url: https://www.youtube.com/watch?v=6sOxIsT81YI
    at: "01:19"
  - id: IasTOBRqL2Y
    title: "TRICENTIS Tosca 16.0 - Lesson 51 | OBSTACLE #9 | Drag & Drop Dynamic WebTable Rows | Repetition |"
    url: https://www.youtube.com/watch?v=IasTOBRqL2Y
    at: "01:15"
  - id: 3m45f0Yu9G8
    title: "TRICENTIS Tosca 16.0 - Lesson 60 | OBSTACLE #18 | Dynamic Web Table | Count Number of Rows| RowCount"
    url: https://www.youtube.com/watch?v=3m45f0Yu9G8
    at: "01:15"
  - id: fWUEjwHsCls
    title: "TRICENTIS Tosca 16.0 - Lesson 61 | OBSTACLE #19 | Get Last Table Row Value | LastContentRow"
    url: https://www.youtube.com/watch?v=fWUEjwHsCls
    at: "01:14"
  - id: iYsG4hbu7sw
    title: "TRICENTIS Tosca 16.0 - Lesson 63 | OBSTACLE #21 | Search Table Cell Value | Constraint Action Mode"
    url: https://www.youtube.com/watch?v=iYsG4hbu7sw
    at: "01:13"
  - id: iOh_KgFyhWU
    title: "TRICENTIS Tosca 16.0 - Lesson 64 | OBSTACLE #22 | Table Search | Dynamic Table | Buffer Action Mode"
    url: https://www.youtube.com/watch?v=iOh_KgFyhWU
    at: "01:12"
  - id: NKe6fY6ffWE
    title: "TRICENTIS Tosca 16.0 - Lesson 68 | OBSTACLE #26 | Dropdown Table |Dynamic XBuffer |Embedded Controls"
    url: https://www.youtube.com/watch?v=NKe6fY6ffWE
    at: "01:13"
---

Most real-world steering problems live in web tables: rows move between page loads, the row count is unknown, a "table" is a pile of `div` elements, or a control sits in a cell but XScan placed it outside the row. The toolset is small: ActionMode `Constraint` to pick a row, `Buffer` to read a cell, the properties `RowCount`, `ColumnCount` and `ResultCount`, row selectors such as `$last`, `{XB[...]}`, embedded controls and the `Repetition` folder property. Concepts: [Table controls](/ToscaBase/modules/table-controls/), [ActionModes](/ToscaBase/test-cases/action-modes/). Comparing a whole table with a saved snapshot (obstacle 34 of the Tosca 16 series) is covered in [Table baseline comparison](/ToscaBase/modules/table-baseline-comparison/).

Routine for every obstacle: scan a Module into an *Obstacles* folder, create a TestCase named after the obstacle, drag the Module in, set Workstate *Completed*, run in ScratchBook. The Tosca 16 series (Lessons 45–68; *Drop-down table* is obstacle 26 there) solves each identically; extra details are noted in place.

## Not a table (obstacle 3)

**Problem.** Clicking *Generate order ID* adds an order number to a table-like block, at a random row. Buffer the number and type it into a text box.

**Cause.** XScan shows no rows or cells: the "table" is nested `div` elements, and the order-number `div` has nothing distinguishing except a dynamic `InnerText`.

**Solution.**

1. Raise the **filtered items** level until the order-number `div` is listed.
2. Untick `InnerText`, switch to *Identify by anchor* and drag the `div` with the static label *Order ID* into the anchor slot: the label stays next to the number wherever the row lands ([Control identification](/ToscaBase/modules/control-identification/)).
3. Lower the filter level, add the *Generate order ID* link and the text box, rename the number attribute to `Order ID`.
4. TestCase: link → `X`; `Order ID` → property `InnerText`, ActionMode `Buffer`, value `orderId`; text box → `{B[orderId]}`.

## Complex table interactions (obstacle 5)

**Problem.** Click the *Edit* button in the row of *John Doe*. Every refresh shuffles the rows, and two rows have the first name *John*.

**Cause.** The row index is meaningless, and XScan places the scanned *Edit* button outside the row.

**Solution.**

1. Scan the table and one *Edit* button (ignore *not unique*) and make it an [embedded control](/ToscaBase/modules/table-controls/#embedded-controls-inside-a-table) of the row.
2. TestCase: in the row, cell *First name* = `John` and cell *Last name* = `Doe`, both ActionMode `Constraint` (one is not enough, *John* appears twice); *Edit* → `X`. Two constraints filter to exactly one row regardless of position; the click hits that row's button.

## To-do list (obstacle 9)

**Problem.** Two tables, *To-do tasks* and *Completed tasks*. Drag every row of the first table into the second, in the order of the *ID* column (1 to 6).

**Cause.** A single drag and drop is `{DRAG}` plus `{DROP}` as in [Drag and drop image](/ToscaBase/troubleshooting/obstacles-input-and-clicks/#drag-and-drop-image-obstacle-8); the difficulty is doing it six times, on a different row each time, without six copies of the TestStep.

**Solution.**

1. Module: both tables.
2. TestCase: in *To-do tasks* choose column *ID*, cell value `1`; row → `{DRAG}` (ActionMode `Input`); *Completed tasks* table → `{DROP}` (also `Input`), without row or column, so the row lands in the table as a whole. Run once to confirm one row moves.
3. Move the TestStep into a folder `Repetition` and set the folder's [Repetition](/ToscaBase/test-cases/repetitions/) property to `6`.
4. Replace the `1` with `{REPETITION}`, the current pass number (1, 2, ...): each pass addresses the row whose ID equals it, so the rows move in order; the log lists each pass separately. Any unique column numbered 1 to *n* can serve as *ID*.

:::note
The subtitles garble the name; it is `{REPETITION}`. No lesson says which ActionMode the *ID* cell uses; `Constraint` (obstacle 5) is the natural fit. `{DROP}` left on the default `Verify` fails with *could not find table* (Lesson 37).
:::

## Lots of rows (obstacle 18)

**Problem.** Count the rows of a table, type the count into *Row count*, click the button. The table changes size after each click.

**Cause.** The row count is only known at run time; a static number does not work.

**Solution.** A table control exposes `RowCount` (and `ColumnCount`). Module: table, text box, button. Table → property `RowCount`, ActionMode `Buffer`, value `rows`; text box → `{B[rows]}`; button → `X`.

## Last row (obstacle 19)

**Problem.** Verify that the last row shows an order value and copy it into a text box; neither the value nor the row count is constant.

**Cause.** The row index of "the last row" changes.

**Solution.** In the row attribute pick a row selector from the drop-down instead of a number: `$last` selects the last row (`$lastContentRow` does the same here and needs ActionMode `Select` on the row). *Value* cell → ActionMode `Buffer`, value `b_val`; text box → `{B[b_val]}`. The drop-down also offers `$1`, `$n`, the header row and the first empty row, so no position is hard-coded.

## Table search (obstacle 21)

**Problem.** A dynamic table; find whether any cell contains the value `15` and type `true` or `false` into a text box.

**Cause.** The value may appear in any row and any column, or not at all.

**Solution.**

1. Module: the table and the text box.
2. TestCase: in the row, set a cell to `15` with ActionMode `Constraint`; Tosca filters to the row containing that cell, in any column.
3. Row → property `Exists`, ActionMode `Buffer`, value `b_exists`: `True` if the constrained row was found, `False` otherwise.
4. Text box → `{B[b_exists]}`.

Constraint plus `Exists` is the fastest whole-table search.

## Meeting scheduler (obstacle 22)

**Problem.** A timetable with times as row headers and weekdays as column headers. Read the status (*open* / *closed*) for Thursday, 11–13, and type it into a text box.

**Cause.** None; row and column are given, only addressing a cell by headers is new.

**Solution.**

1. Module: the timetable and the result text box.
2. Row attribute: type the row header text (`11 - 13`, as on the page), ActionMode `Select`; Tosca selects the row by that text as long as it is unique.
3. Cell: choose column `Thursday` from the headers, ActionMode `Buffer`, value `b_status`.
4. Text box → `{B[b_status]}` with `Input` (Lesson 128 uses `{SENDKEYS "{B[b_status]}"}`; both work).

:::note
A dynamic time would have to be buffered or constrained first; the speaker mentions this but does not show it.
:::

## Drop-down table (obstacle 23)

**Problem.** Each row has a task like *Select the word that starts with letter M* and a drop-down; *Generate* changes the letters. For each row select the only matching word, then *Submit*.

**Cause.** The letter is unknown until run time, and XScan places the scanned `select` outside the row.

**Solution.**

1. Click *Generate* before scanning so that the drop-downs exist. Module: *Generate*, *Submit*, the table and one drop-down (not unique; fine); drag the `select` into the cell so it becomes an [embedded control](/ToscaBase/modules/table-controls/#embedded-controls-inside-a-table) present in every row.
2. TestCase:
   - *Generate* → `X`.
   - Row `$2` (row 1 is the header). First cell → ActionMode `Verify`, value: the constant text followed by `{XB[letter]}`, which verifies the fixed part and stores the changing letter in `letter` at once ([Buffers](/ToscaBase/data-and-parameters/buffers/)).
   - Second cell → ActionMode `Select` (default is `Verify`). Nested drop-down → `{B[letter]}*`: the word starting with that letter.
   - Copy the row block for rows `$3` to `$6`, changing only the row number; each row overwrites the same buffer.
   - *Submit* → `X`.
