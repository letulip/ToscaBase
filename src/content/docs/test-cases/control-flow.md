---
title: Control flow
description: If/Then/Else conditions and While and Do-While loops inside a TestCase - how to create them, what goes in the Condition, and how the Maximum repetitions property prevents infinite loops.
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
  - id: Wpi9H-KE9HQ
    title: "TRICENTIS Tosca 16.0 - Lesson 27 | Conditional Statements - Part 1 | IF-THEN, ELSE Statements"
    url: https://www.youtube.com/watch?v=Wpi9H-KE9HQ
    at: "00:13"
  - id: "-HtnOUykwaA"
    title: "TRICENTIS Tosca 16.0 - Lesson 19 | WHILE, IF and DO Statements | Conditional and Loop Statements |"
    url: https://www.youtube.com/watch?v=-HtnOUykwaA
    at: "09:14"
  - id: hvHsys7Cb9M
    title: "TRICENTIS Tosca 16.0 - Lesson 29 | Conditional Statements - Part 3 | WHILE Statements"
    url: https://www.youtube.com/watch?v=hvHsys7Cb9M
    at: "01:13"
  - id: VlOi6Ug2CE8
    title: "TRICENTIS Tosca 16.0 - Lesson 28 | Conditional Statements - Part 2 | DO Statements"
    url: https://www.youtube.com/watch?v=VlOi6Ug2CE8
    at: "01:14"
---

A TestCase normally runs its TestSteps top to bottom. Three control-flow objects change that: an **If** statement runs steps only when a condition holds, and **While** and **Do** statements repeat steps as long as a condition holds. All three are created from the TestCase's context menu; Tosca adds the child objects (a **Condition** that it evaluates plus the parts that hold ordinary TestSteps) automatically. A condition is usually a `Verify` on a control (`Exists`, `Visible`, `Enabled`) or a **TBox Evaluation Tool** expression on buffers, and a condition that evaluates to false is a branch decision, not a failed TestCase. Use these objects for genuinely dynamic situations; for plain counting, the folder [Repetition](/ToscaBase/test-cases/repetitions/) property is simpler, and Tricentis explains why loops should be the exception in [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

## If statement

### The problem it solves

A shop page shows an `Add to cart` button for each product; once the product is in the cart the button becomes `Remove`. A TestCase that clicks `Add to cart` fails when the product is already there, which is correct, but often you want the TestCase to handle the situation instead. The same applies to a login page that a previous run left logged in. Checking the state before acting is one of the most common needs in UI automation.

### Creating one

1. Right-click the TestCase (or a folder in it) and choose **Create If statement**. Tosca adds an `If` object with a **Condition** and a **Then** part; the order is always If, Condition, Then.
2. If you need the other branch, right-click the `If` object and choose **Create Else statement**. The **Then** part is shown with a left-pointing arrow icon, the **Else** part with a right-pointing one, and Else always comes last.
3. Drag the object to the right place in the flow.
4. Put the check into **Condition**: a TestStep with ActionMode `Verify`, for example `Enabled == True` on `Add to cart` or `Visible == True` on the `Login` link.
5. Put the actions into **Then**, and the alternative into **Else**.

:::caution
The condition step must use `Verify`. In Lesson 27 it was first left at `Input`, so the run tried to type into the link and had to be stopped; switching the ActionMode fixed it.
:::

### How it executes

- Condition met: the condition shows a tick, the **Then** steps run once, **Else** is skipped.
- Condition not met: the condition shows a cross, **Then** is skipped, the **Else** steps (if any) run once, and the TestCase **passes**.

Both outcomes are visible by expanding the `If` node in the ScratchBook or ExecutionList result. The login example from Lesson 27 shows both: **Condition** verifies that `Login` in the top menu is visible; **Then** clicks `Login` and enters the credentials; **Else** clicks `Logout`, then `Login`, then enters the credentials. Run against a fresh browser the Then branch executes; run again without logging out, the condition fails and the Else branch logs out and back in, and the TestCase still passes.

A condition does not have to be a control check. The **TBox Evaluation Tool** can evaluate an expression such as a buffer comparison, which turns an `If` into a branch on data; see [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/) for a multi-`If` example that emulates a `switch`.

## While statement

**Create While statement** adds a `While` object with a **Condition** and a **Loop** part, in that order. Tosca checks the condition first; if it is fulfilled the TestSteps in **Loop** run, then the condition is checked again, until it is no longer satisfied. If the condition is false from the start, the loop body never runs.

### Example: counting to five

Set a counter buffer to 0; while the counter is less than 5, add 1 to it.

1. Add **TBox Set Buffer** with buffer name `R` and value `0`; rename the step `Set repetition`. (Buffers are explained in [Buffers](/ToscaBase/data-and-parameters/buffers/).)
2. Create the `While`. In **Condition**, add **TBox Evaluation Tool** with the expression `{B[R]} < 5`.
3. In **Loop**, add another **TBox Set Buffer** for `R` with the value `{MATH[{B[R]}+1]}`, the math expression that adds 1 to the current buffer value (syntax in [String operations](/ToscaBase/expressions/string-operations/)).

In the ScratchBook the condition evaluates to true five times, the calculation runs on each pass, and on the sixth check `5 < 5` is false and execution leaves the loop.

:::caution
Buffer names are case-sensitive in expressions. In the source the buffer was accidentally renamed while renaming the TestStep, and `{B[R]}` stopped matching until the name was set back to `R`.
:::

### Example: empty the cart until the table is gone

The everyday `While` repeats an action until a control disappears. Lessons 19 and 29 build it as a reusable TestStepBlock in a TestStepLibrary, because every TestCase wants an empty cart to start with (see [Business parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/)): click the shopping cart (`X`), the `While`, click `Logout`, `WaitOn` `Visible == True` on the `Login` link, `Close Browser` with title `Demo*`.

- **Condition:** the cart Module's table node, `Exists == True`, ActionMode `Verify`. The cart table only exists while the cart has items.
- **Loop:** the same Module; row `$1`, column `Remove`, checkbox `Input` `True`; then `Update shopping cart` with `X`. Each pass removes the first remaining row.

With four items the loop runs four times; the fifth check finds no table, the condition is false and execution continues with the logout. The last condition entry in the log reads expected `True`, actual `False`: that is the exit, not an error. Table selectors are explained in [Table controls](/ToscaBase/modules/table-controls/).

### Maximum repetitions

Every `While` (and `Do`) object has a **Maximum repetitions** property that caps the number of iterations so that a condition that never becomes false cannot loop forever. The default is `30`, shown in the object's Value column and properties; change it when a loop legitimately needs more passes.

## Do statement (Do-While)

**Create Do statement** (or **Ctrl+N**, **Ctrl+D**) adds a `Do` object with a **Loop** part followed by a **Condition** part. It repeats **Loop** until the condition is no longer fulfilled, exactly like `While`, with one difference: the body runs **before** the condition is checked, so it executes at least once even if the condition is never true. **Maximum repetitions** applies with the same default of 30.

- The counter example becomes a `Do` by moving the `Calculate repetition` step into **Loop** and the evaluation into **Condition**: the run calculates first, then evaluates, and stops when `5 < 5` is false. Because the order is reversed the iteration count differs between `While` and `Do` for the same condition.
- Lesson 28 empties the cart with a `Do`: **Loop** ticks the `Remove` checkbox of row `$1` and clicks `Update shopping cart`, **Condition** verifies that the cart table still `Exists`. After the fourth removal the check fails and execution leaves the loop. Because the body runs first, this version assumes the cart is not already empty; if it might be, use the `While` version.

## Choosing between them

| Need | Use |
|---|---|
| Run steps only if a control is present or a value matches, with an alternative | `If` with `Then` and `Else` |
| Repeat while something is true, possibly zero times | `While` |
| Repeat at least once, then check | `Do` |
| Repeat a fixed or computed number of times | Folder [Repetition](/ToscaBase/test-cases/repetitions/) property, no loop |
| Find a table row by content | `Constraint` ActionMode, no loop; see [ActionModes](/ToscaBase/test-cases/action-modes/) |
| React to a failure rather than a condition | [Recovery and Cleanup Scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/) |
