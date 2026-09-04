---
title: Repetitions
description: Run the TestSteps in a folder a fixed number of times with the Repetition property, set through the column chooser or the folder's properties, or a number of times computed at run time from a buffer.
level: 1
sidebar:
  order: 40
sources:
  - id: jWpcEtvOo-w
    title: "Tosca Tutorial | Lesson 48 - Run Test Steps Repeatedly using Repetitions |"
    url: https://www.youtube.com/watch?v=jWpcEtvOo-w
    at: "02:06"
  - id: 4ELkBwejJIU
    title: "TRICENTIS Tosca 16.0 - Lesson 24 | Set Repetition on Folder Level | Explicit Name | ResultCount"
    url: https://www.youtube.com/watch?v=4ELkBwejJIU
    at: "06:09"
---

A **Repetition** is a number on a TestStep folder that makes Tosca execute every TestStep inside that folder that many times in a row. It is the simplest way to repeat steps: no condition, no counter buffer, no loop object. Typical uses are a scenario that genuinely repeats an action (add the same product to the cart five times), a rough load check on a single element, or, with a buffer as the count, one pass per row of a table. Where a count is enough, Tricentis prefers this over a `While` loop; see [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

## Where a Repetition can be set

Only on a **folder** inside a TestCase. The property is not available on an individual TestStep or on the TestCase itself. To repeat one step, put it in a folder of its own.

The example TestCase has three parts: login steps, a folder `Add products` containing one TestStep that clicks `Add to cart`, and a step that closes the application. The Repetition goes on `Add products`.

## Way 1: the Repetition column

1. In the TestCases section, right-click the column header row and choose **Column Chooser**.
2. Find the **Repetition** column and drag it into the header row, or double-click it. The column now appears for all TestCases.
3. In the folder's row, enter the number of repetitions, for example `5`.

To remove a column again, drag its header out of the header row until a cross sign appears and release it.

## Way 2: the folder's properties

1. Select the folder and open its **Properties** pane.
2. Set the **Repetition** property, for example to `4`.

Both ways set the same property; changing it in the properties pane updates the column and vice versa.

## What you see

- **Folder icon.** As soon as a Repetition is set the folder shows a rounded arrow pointing backwards. Remove the Repetition and the icon returns to a normal folder. This is the quickest way to spot repeated steps in a large TestCase.
- **Results.** In the ScratchBook or ExecutionList result, the folder node lists the repetitions; expanding it shows the step executed once per repetition (five entries for `5`, four for `4`).

## A count that comes from the application

The Repetition value can be a buffer instead of a literal, and inside the folder the expression `{REPETITION}` returns the number of the current pass (1, 2, 3, ...). Together they let a folder do something once per row of a table without a loop object. Lesson 24 empties a shopping cart this way; the `While` and `Do` versions of the same scenario are in [Control flow](/ToscaBase/test-cases/control-flow/).

1. `Verify table exists`: the cart Module, table node, `Exists == True`, ActionMode `Verify`.
2. `Count items in cart`: the same Module, the table's rows node, property `ResultCount`, ActionMode `Buffer`, value `CartItems`. The count includes the header row, so it is one more than the number of products.
3. `Calculate items without header`: **TBox Set Buffer**, buffer `ActualCartNumber`, value `{MATH[{B[CartItems]}-1]}`.
4. Create the folder `Select remove` and set its Repetition to `{B[ActualCartNumber]}`. The folder icon changes as soon as the value is entered.
5. Inside the folder, one TestStep on the cart Module: row `${REPETITION}`, column `Remove`, checkbox `Input` `True`. On the first pass the row selector resolves to `$1`, on the second to `$2`, and so on, so each pass ticks the next row.
6. After the folder, one step clicks `Update shopping cart` (`X`).

With two products in the cart the folder ran twice, both boxes were ticked, and the single update click emptied the cart. Table properties such as `ResultCount` and the row selectors are listed in [Table controls](/ToscaBase/modules/table-controls/#table-properties); another use of `{REPETITION}`, addressing a row by ID on each pass, is in [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).

## Related

- [Control flow](/ToscaBase/test-cases/control-flow/) for `While` and `Do` loops when the count depends on a condition rather than a number.
- [Execution repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/) for repeating a whole TestCase from an ExecutionList, which is a different property.
- [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/) for running the same steps with different data, which is what TestCase-Design is for rather than Repetitions.
