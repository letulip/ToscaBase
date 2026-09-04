---
title: Control flow
description: If/Then conditions and While and Do-While loops inside a TestCase - how to create them, what goes in the Condition, and how the Maximum repetitions property prevents infinite loops.
level: 1
sidebar:
  order: 30
sources:
  - id: ngQU7wKdoy8
    title: "Tosca Tutorial | Lesson 32 -  Use If Then Else Condition | Building Test Cases | Control Flows |"
    url: https://www.youtube.com/watch?v=ngQU7wKdoy8
    at: "03:06"
  - id: FphWNQxRrjM
    title: "Tosca Tutorial | Lesson 33 - Use Do & While Loops | Building Test Cases | Control Flows |"
    url: https://www.youtube.com/watch?v=FphWNQxRrjM
    at: "00:02"
---

A TestCase normally runs its TestSteps top to bottom. Three control-flow objects change that: an **If** statement runs steps only when a condition holds, and **While** and **Do** statements repeat steps as long as a condition holds. All three are created from the TestCase's context menu and contain a **Condition** part that Tosca evaluates plus a body of ordinary TestSteps. Use them for genuinely dynamic situations; for plain counting, the folder [Repetition](/ToscaBase/test-cases/repetitions/) property is simpler, and Tricentis explains why loops should be the exception in [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

## If statement

### The problem it solves

A shop page shows an `Add to cart` button for each product. Once the product is in the cart the button becomes `Remove`. A TestCase that clicks `Add to cart` fails when the product is already in the cart: the log says the button could not be found with the given properties, which is correct, but sometimes you want the TestCase to handle the situation rather than fail. Checking for a control before acting on it is one of the most common needs in UI automation.

### Creating one

1. Right-click the TestCase (or a folder in it) and choose **Create If statement**. Tosca adds an `If` object with a **Condition** part and a **Then** part.
2. Drag the object to the right place in the flow, for example after the login steps.
3. Put the check into **Condition**: a TestStep on the `Add to cart` button with ActionMode `Verify` and Value `Enabled == True` (instead of `Input` with a click).
4. Put the action into **Then**: a TestStep that clicks the same button with `X` and `Input`.

### How it executes

- Condition not met (button absent): the condition step shows a cross in the result, the **Then** part is skipped, and the TestCase **passes**. A failed condition is not a failed TestCase.
- Condition met (the app state was reset and the button is back): the condition shows a tick, and the **Then** part runs and clicks the button.

Both outcomes are visible by expanding the `If` node in the ScratchBook or ExecutionList result.

:::note
The speaker calls the object an "if else step", but the demonstration only shows the **Condition** and **Then** parts and never adds an **Else** branch. Check your Tosca version for how the Else part is added.
:::

A condition does not have to be a control check. The **TBox Evaluation Tool** can evaluate an expression such as a buffer comparison, which turns an `If` into a branch on data; see [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/) for a multi-`If` example that emulates a `switch`.

## While statement

A `While` checks its condition first; if it is fulfilled, the TestSteps in the **Loop** part run, then the condition is checked again, until it is no longer satisfied. If the condition is false from the start, the loop body never runs.

### Example: counting to five

The flow: set a counter buffer to 0; while the counter is less than 5, add 1 to it.

1. Add **TBox Set Buffer** with buffer name `R` and value `0`. Rename the step `Set repetition`. (Buffers are explained in [Buffers](/ToscaBase/data-and-parameters/buffers/).)
2. Right-click the TestCase and choose **Create While statement**. Tosca adds a `While` object with a **Condition** part and a **Loop** part.
3. In **Condition**, add **TBox Evaluation Tool** with the expression `{B[R]} < 5`. Rename it `Check repetition less than 5`.
4. In **Loop**, add another **TBox Set Buffer** for `R` with the value `{MATH[{B[R]}+1]}`, the math expression that adds 1 to the current buffer value (syntax in [String operations](/ToscaBase/expressions/string-operations/)). Rename it `Calculate repetition`.

Run it in the ScratchBook: the result shows the condition evaluated to true five times, the calculation ran on each pass, and on the sixth check `5 < 5` evaluated to false and execution left the loop.

:::caution
Buffer names are case-sensitive in expressions. In the source the buffer was accidentally renamed while renaming the TestStep, and the expression `{B[R]}` stopped matching until the buffer name was set back to `R`.
:::

### Maximum repetitions

Every `While` (and `Do`) object has a **Maximum repetitions** property, shown in its properties pane, that caps the number of iterations so that a wrong condition cannot loop forever. The default is `30`; change it when a loop legitimately needs more passes.

## Do statement (Do-While)

`Do` repeats its **Loop** part until the condition is no longer fulfilled, exactly like `While`, with one difference: the body runs **before** the condition is checked, so it executes at least once even if the condition is never true.

1. Right-click and choose **Create Do statement**, or press **Ctrl+N** followed by **Ctrl+D**. Tosca adds a `Do` object with a **Loop** part and a **Condition** part.
2. Copy the same `Set repetition`, `Calculate repetition` and `Check repetition` steps from the `While` example: the calculation goes into **Loop**, the evaluation into **Condition**.

The run calculates first, then evaluates; it repeats until the expression is false (`5 < 5` in the last pass) and then continues with the next TestStep. Because the order is reversed the number of iterations differs between `While` and `Do` for the same condition, so choose by whether the body must run at least once. **Maximum repetitions** applies to `Do` as well, with the same default of 30.

## Choosing between them

| Need | Use |
|---|---|
| Run steps only if a control is present or a value matches | `If` |
| Repeat while something is true, possibly zero times | `While` |
| Repeat at least once, then check | `Do` |
| Repeat a fixed number of times | Folder [Repetition](/ToscaBase/test-cases/repetitions/) property, no loop |
| Find a table row by content | `Constraint` ActionMode, no loop; see [ActionModes](/ToscaBase/test-cases/action-modes/) |
| React to a failure rather than a condition | [Recovery and Cleanup Scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/) |
