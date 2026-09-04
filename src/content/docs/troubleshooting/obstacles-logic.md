---
title: "Obstacles: loops and conditions"
description: Sorting numbers with a Do loop and an If statement, and playing a keyboard game with Do, If/Else and TBox Send Keys, for the rare cases where a TestCase genuinely needs logic.
level: 3
sidebar:
  order: 35
sources:
  - id: 7_689-oZGi0
    title: "TRICENTIS Tosca 16.0 - Lesson 74 | OBSTACLE #32 | Sort Numbers | Do & While Loop|If & Else Statement"
    url: https://www.youtube.com/watch?v=7_689-oZGi0
    at: "01:12"
  - id: 1Ox9h67g3PY
    title: "TRICENTIS Tosca 16.0 - Lesson 75 | OBSTACLE #33 | Loops and conditions | Send Keys | Play Game"
    url: https://www.youtube.com/watch?v=1Ox9h67g3PY
    at: "01:15"
---

The last two obstacles of the Tricentis *Obstacle Course* cannot be written as a straight list of TestSteps or as a folder [Repetition](/ToscaBase/test-cases/repetitions/): the number of passes is unknown, and each pass has to look at the page and decide what to do. Both are solved with a `Do` statement (body first, then the condition) that holds an `If` statement; obstacle 33 adds an `Else` branch and keyboard input through **TBox Send Keys**. How the three control-flow objects work is described in [Control flow](/ToscaBase/test-cases/control-flow/); the simplest loop obstacle, *Again and again* (obstacle 15, a `While`), is in [Obstacles: input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/#again-and-again-obstacle-15). Tricentis still advises against logic in TestCases; these two are the cases that need it.

## Bubble sort (obstacle 32)

**Problem.** Ten numbers in a row and a "bubble" highlighting two neighbours. If the left number is greater than the right one, click *Swap* and then *Next*; otherwise click *Next* only. Keep going until the numbers are in ascending order, when the *Keep sorting* label changes to a success message.

**Cause.** Neither the number of passes nor the action in a pass is known before the run, and the numbers' `InnerText` changes every time the bubble moves.

**Solution.** Module:

1. Scan the buttons *Swap*, *Next* and *Keep sorting*; each is unique by `id`.
2. Raise the **filtered items** level twice until the bubble `div` is listed. Untick its `InnerText` (the two current digits), identify it by `class`, rename it `bubble`.
3. Inside the bubble, the two number `div`s share `class` `num` and `tag`. Untick `InnerText` on both and switch to *Identify by index*: index `1` becomes `first`, index `2` becomes `second`. Index is safe here because the bubble always holds exactly two numbers.

TestCase:

1. Right-click → **Create Do Statement**. Tosca adds a *Loop* part and a *Condition* part.
2. Loop, first step: **TBox Wait** with `500` ms, so that the page has redrawn before the pass reads it.
3. Loop, second step: `first` → property `InnerText`, ActionMode `Buffer`, value `num1`.
4. Loop, third step: right-click → **Create If Statement**.
   - Condition: `second` → property `InnerText`, ActionMode `Verify`, value `<{B[num1]}`. Set the attribute's data type to *Numeric* in the properties pane first; as strings, `9` is greater than `10`.
   - Then: *Swap* → `X`.
5. Loop, fourth step, after the `If` and outside it: *Next* → `X`. It runs in every pass, because a swap has to be followed by *Next* as well.
6. Condition of the `Do`: *Keep sorting* → property `InnerText`, ActionMode `Verify`, value `Keep sorting`. The loop repeats while the verification passes and exits as soon as the label changes.

:::note
A `Do` statement stops after its **Maximum repetitions**, 30 by default. Ten numbers may need more passes than that; raise the value in the statement's properties, as obstacle 33 shows.
:::

## Tosca Olympics (obstacle 33)

**Problem.** After *Start* a skier runs down a slope. Before each tree an instruction (*Go left* or *Go right*) says which arrow key to press; the text ends with a success message, or a crash message when a key was missed.

**Cause.** The number of turns and the direction of each are known only at run time, and there is nothing to click: the input is a keyboard key sent to the browser window.

**Solution.** Module: the *Start* button and the instruction `div` (filter level raised twice; keep `id` and `tag`, untick the changing `InnerText`; rename it `instruction`).

TestCase:

1. *Start* → `X`.
2. Right-click → **Create Do Statement**; in its *Loop*, **Create If Statement**:
   - Condition: `instruction` → property `InnerText`, ActionMode `Verify`, value `Go left`.
   - Then: standard module **TBox Send Keys** with `Caption` = the window title with a wildcard (`Tricentis Obst*`) and `Keys` = `"{LEFT}"`.
   - Right-click the `If` → **Create Else Statement**; Else: another **TBox Send Keys** with `"{RIGHT}"`. No second verification is needed: whatever is not *Go left* is *Go right*.
3. Condition of the `Do`: `instruction` → `InnerText`, ActionMode `Verify`, *not equal to* `{REGEX["crash|you did it"]}`. The loop continues while neither end message is displayed.
4. Open the `Do` statement's properties and raise **Maximum repetitions** from `30` to `100`. The first run crashed after exactly 30 turns; the game needed 44.

`TBox Send Keys` is the same module that switches browser tabs in [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/#switching-between-browser-tabs); anything a user can do with the keyboard, it can do.

:::note
The speaker reads the loop condition aloud as *not equal to* without showing the operator; Tosca's negation is `!=` in front of the value, so the cell should read `!={REGEX["crash|you did it"]}`. The exact wording of the end messages is not shown either; copy it from the page.
:::
