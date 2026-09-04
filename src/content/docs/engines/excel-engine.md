---
title: Excel engine
description: Compare two workbooks with Excel 1:1 File Compare, and create, fill, verify and read Excel sheets with the TBox Excel standard modules - open, worksheet, range, manipulation, close, row and column counts.
level: 3
sidebar:
  order: 10
sources:
  - id: idPsLArM3zc
    title: "Tosca Tutorial | Lesson 19 - Compare Two Excel Files | TBox Automation Module | Excel Engine"
    url: https://www.youtube.com/watch?v=idPsLArM3zc
    at: "02:11"
  - id: hi0GA1Dg1Nc
    title: "Tosca Tutorial | Lesson 20 - Create, Open, Modify & Delete Excel Workbook | Excel Engine"
    url: https://www.youtube.com/watch?v=hi0GA1Dg1Nc
    at: "01:09"
  - id: 4V0ygehvBAk
    title: "Tosca Tutorial | Lesson 21 - Verify RowCount & ColumnCount of Excel WorkBook | Excel Engine"
    url: https://www.youtube.com/watch?v=4V0ygehvBAk
    at: "01:09"
---

The Excel engine ships as a family of TBox standard modules, so there is nothing to scan and no library to install: search the Modules for `TBox Excel` and you get modules to compare two files, open or create a workbook, add worksheets, define a cell range, read, write, buffer and verify cells, run macros and close or save the workbook. Every workbook TestCase follows the same pattern: open, define a range, manipulate the range, close.

## The Excel standard modules

| Module | Role |
|---|---|
| **TBox Excel 1:1 File Compare** | Compares two workbooks sheet by sheet and reports mismatching cells |
| **TBox Open Excel Workbook** | Opens an existing workbook or creates a new one |
| **TBox Create Excel Worksheet** | Adds a worksheet to the opened workbook |
| **TBox Define Excel Range** | Names a block of cells; mandatory before any manipulation |
| **TBox Excel Range Manipulation** | Inputs, buffers and verifies cells and range properties of a defined range |
| **TBox Close Excel Workbook** | Closes the workbook, optionally saving it under a new name or type |
| **TBox Run Excel Macro** | Runs a macro contained in the workbook |
| **TBox Clear Excel Range** | Clears the values previously entered into a range |
| **TBox Delete Excel Worksheet**, **TBox Update Excel Worksheet** | Remove or rename sheets in multi-sheet workbooks |

:::caution
The workbook must not be open in Excel while the TestCase runs, otherwise the Open step fails. Close Excel first, saving if needed.
:::

## Compare two workbooks

`TBox Excel 1:1 File Compare` sits next to the file, image and [PDF](/ToscaBase/engines/pdf-engine/) comparison modules. Its attributes:

| Attribute | Meaning |
|---|---|
| Reference file | Full path of the baseline workbook, including `.xlsx` |
| Target file | Full path of the workbook compared against it |
| Reference password, Target password | Only for protected files |
| Include cells data, Include formats, Include objects | Booleans that add cell values, formatting and objects to the comparison; optional |
| Include sheets | Names of the sheets to compare, separated by semicolons. A sheet not listed here is **not** compared |
| Output path | A text file (for example `results.txt`) where mismatches are written. Nothing is written when the files match |

Example: `users.xlsx` and `users1.xlsx` both have a sheet `Email` with a list of addresses; one address is missing from the target. Run in the ScratchBook and the step fails with a log that names both files, then the mismatch: sheet `Email`, cell `A49`, reference value `test@gmail.com`, target has no value in `A49`. The output file contains the same lines for reporting. Comparison time depends on the amount of data.

## Create and fill a workbook

The TestCase `Create Excel` builds `emp.xlsx` with a sheet containing a header, two employees with salaries and a total.

1. **TBox Delete File** removes a previous copy of the file, so the run is repeatable.
2. **TBox Open Excel Workbook**: `Workbook name` is a name used by every following step (`EmployeeData`), `Path` is the file (`C:\training\emp.xlsx`), `Create new` is `True` to create the file or `False` to open an existing one. `Password` and `Read only` (`True`/`False`) are optional.
3. **TBox Create Excel Worksheet**: the same `Workbook name`, a `Worksheet name` (`EMP`) and `Worksheet order`, which places the sheet `first`, `last` or at a given position.
4. **TBox Define Excel Range**: `Range name` (`EmployeeData`), workbook and worksheet names, a start cell (`A1`) and an end cell (`B4`). The range is what later steps steer, like selecting cells in Excel. If more records may come, define a larger end cell, for example row 50 for up to 49 records.
5. **TBox Excel Range Manipulation** with `Range name` `EmployeeData`. Its data table mirrors the range: the first row is marked as the header and gets `Full name` and `Salary`; the next rows carry values. Each cell has its own ActionMode, so within one step the salaries are entered and buffered (`Amount1`, `Amount2`), and the `Total salary` cell is verified against a math expression that sums the two buffers.
6. **TBox Close Excel Workbook**: `Workbook name`, `Save` (`True`/`False`), the `Path` (a different path saves a copy elsewhere) and `Save as type`. The type list covers every format Excel can write, including workbook, PDF, TXT and CSV, so a TestCase can export a sheet as PDF directly. The same module also opens those other types.

After the run the log shows the values entered, the buffered amounts and the successful verification of the total; the file `emp.xlsx` exists with sheet `EMP` and the same data.

:::tip
The speaker verifies the total in the same manipulation step that fills the sheet, and notes that a separate verification TestCase is the recommended layout.
:::

:::note
The video shows the total computed with a math function over `{B[Amount1]}` and `{B[Amount2]}`; the exact expression syntax is not read out. See [Expressions](/ToscaBase/expressions/) for Tosca's math expressions.
:::

## Buffer the row and column count

For a sheet with four rows and two columns (`EmployeeData` from the example above):

1. Create a TestCase `Get row count and column count` and reuse the **Open Excel Workbook** (`Create new` = `False`), **Define Excel Range** (same workbook, worksheet and range name) and **Close Excel Workbook** steps.
2. Add **TBox Excel Range Manipulation**, drag it above the Close step and rename it `Get row count`. Copy it, paste below and rename the copy `Get column count`. Enter the range name `EmployeeData` in both; the speaker forgot it in the second step and the run failed until it was filled in.
3. In `Get row count` open the data table, click the arrow in the **Value** cell and choose the property `RowCount`. Enter the buffer name `RC` as value and set ActionMode `Buffer`. `RowCount` is a special property that returns the number of rows of a table; you can also type it instead of picking it.
4. In `Get column count` do the same with `ColumnCount`, buffer `CC`, ActionMode `Buffer`.

The log reports that range `EmployeeData` was updated successfully, `RC` set to `4` and `CC` set to `2`. Verify the buffers in a later TestStep to turn the read-out into a check; it works for existing workbooks and for ones created earlier in the same TestCase.

## Related

- [Buffers](/ToscaBase/data-and-parameters/buffers/) and [Buffer operations](/ToscaBase/standard-modules/buffer-operations/).
- [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/) for TBox Delete File and the other file comparison modules.
- [Table controls](/ToscaBase/modules/table-controls/) for `RowCount` and `ColumnCount` on application tables.
