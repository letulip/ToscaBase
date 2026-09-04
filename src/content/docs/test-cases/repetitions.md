---
title: Repetitions
description: Run the TestSteps in a folder a fixed number of times with the Repetition property, set either through the column chooser or the folder's properties.
level: 1
sidebar:
  order: 40
sources:
  - id: jWpcEtvOo-w
    title: "Tosca Tutorial | Lesson 48 - Run Test Steps Repeatedly using Repetitions |"
    url: https://www.youtube.com/watch?v=jWpcEtvOo-w
    at: "02:06"
---

A **Repetition** is a number on a TestStep folder that makes Tosca execute every TestStep inside that folder that many times in a row. It is the simplest way to repeat steps: no condition, no counter buffer, no loop object. Typical uses are a scenario that genuinely repeats an action (add the same product to the cart five times) or a rough load check on a single element. Where a fixed count is enough, Tricentis prefers this over a `While` loop; see [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

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

- **Folder icon.** A folder with a Repetition shows a rounded arrow pointing backwards. Remove the Repetition and the icon returns to a normal folder. This is the quickest way to spot repeated steps in a large TestCase.
- **Results.** In the ScratchBook or ExecutionList result, the folder node lists the repetitions; expanding it shows the step executed once per repetition (five entries for `5`, four for `4`).

## Related

- [Control flow](/ToscaBase/test-cases/control-flow/) for `While` and `Do` loops when the count depends on a condition.
- [Execution repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/) for repeating a whole TestCase from an ExecutionList, which is a different property.
- [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/) for running the same steps with different data, which is what TestCase-Design is for rather than Repetitions.
