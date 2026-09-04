---
title: "Obstacles: input and clicks"
description: Drag and drop, clicking until a label changes, entering text that Tosca mistakes for a command, clicking at an offset, and clicking at screen coordinates.
level: 3
sidebar:
  order: 30
sources:
  - id: Fq68hFb2K_0
    title: "Tosca Tutorial | Lesson 114 - Drag and Drop Image | Repositioning | Obstacle 8"
    url: https://www.youtube.com/watch?v=Fq68hFb2K_0
    at: "01:13"
  - id: G-1TF7oLe8g
    title: "Tosca Tutorial | Lesson 121 - Multiple Interactions | While Loop | Obstacle 15"
    url: https://www.youtube.com/watch?v=G-1TF7oLe8g
    at: "02:21"
  - id: B2A_h9TMzFM
    title: "Tosca Tutorial | Lesson 132 - Escape Values | Click Method | Obstacle 26"
    url: https://www.youtube.com/watch?v=B2A_h9TMzFM
    at: "02:16"
  - id: 3QNlHZLmelw
    title: "Tosca Tutorial | Lesson 133 - Click Position | OffsetHorizontal | OffsetVertical | Obstacle 27"
    url: https://www.youtube.com/watch?v=3QNlHZLmelw
    at: "01:14"
  - id: aAjkpWkv9lE
    title: "Tosca Tutorial | Lesson 136 - Click On Screen | XModules | Screen Width | Obstacle 30"
    url: https://www.youtube.com/watch?v=aAjkpWkv9lE
    at: "03:19"
  - id: SI_UkkF_LHU
    title: "TRICENTIS Tosca 16.0 - Lesson 50 | OBSTACLE #8 | Drag & Drop Image | Repositioning |"
    url: https://www.youtube.com/watch?v=SI_UkkF_LHU
    at: "01:16"
  - id: NnuHH_OkwpA
    title: "TRICENTIS Tosca 16.0 - Lesson 57 | OBSTACLE #15 | While Loop | Multiple Interactions"
    url: https://www.youtube.com/watch?v=NnuHH_OkwpA
    at: "01:15"
  - id: 9tVFPH7ex_Q
    title: "TRICENTIS Tosca 16.0 - Lesson 66 | OBSTACLE #24| Escape Values | Click Method"
    url: https://www.youtube.com/watch?v=9tVFPH7ex_Q
    at: "01:13"
  - id: pkUfVwKe5sU
    title: "TRICENTIS Tosca 16.0 - Lesson 65 | OBSTACLE #23 | Click Position | OffsetHorizontal | OffsetVertical"
    url: https://www.youtube.com/watch?v=pkUfVwKe5sU
    at: "02:15"
  - id: l5SNsxfX9no
    title: "TRICENTIS Tosca 16.0 - Lesson 72 | OBSTACLE #30 | Click On Screen | Screen Width | XModules"
    url: https://www.youtube.com/watch?v=l5SNsxfX9no
    at: "01:13"
---

These obstacles are not about finding the control; the Module is trivial. The difficulty is in the **action**: a mouse gesture Tosca has to emulate, an unknown number of clicks, a value that collides with Tosca's own syntax, or a click that must land at a precise position. Each is solved with a built-in expression (`{DRAG}`, `{DROP}`, `{CLICK}` with offsets, escaping), a control-flow object, or a standard module. See [ActionModes](/ToscaBase/test-cases/action-modes/) for the value syntax used throughout and [Control flow](/ToscaBase/test-cases/control-flow/) for loops; the two obstacles that need a `Do` loop with `If`/`Else` are in [Obstacles: loops and conditions](/ToscaBase/troubleshooting/obstacles-logic/). The Tosca 16 series (Lessons 50–72) solves each obstacle the same way and counts *Halfway* as obstacle 23 and *Escape* as 24; where it shows a syntax the first series only described, the doc follows the Tosca 16 lesson.

## Drag and drop image (obstacle 8)

**Problem.** Drag an image from the left box into the right box.

**Cause.** There is no ActionMode for a mouse drag; it has to be expressed as two steps.

**Solution.** Module: the image and the target `div`. TestStep:

1. Image → value `{DRAG}`, ActionMode `Input`. The expression selects the object for repositioning.
2. Target `div` → value `{DROP}`, ActionMode `Input`. It drops the object previously selected with `{DRAG}`.

Both expressions are predefined in Tosca and appear in the value auto-complete inside `{ }`. The element must support drag and drop in the application; `{DRAG}` on an element that is not draggable does nothing.

## Again and again (obstacle 15)

**Problem.** Click *Click me* repeatedly. After an unknown number of clicks the label changes to *Enough*; that button must then be clicked once more to finish.

**Cause.** The number of clicks is not fixed, so a linear TestCase cannot express it.

**Solution.** Use a `While` loop with a verification as its condition.

1. Module: just the button.
2. In the TestCase, right-click → **Create While Statement**. Drag the Module inside the loop.
3. Condition TestStep (*Check button*): button → property `InnerText`, ActionMode `Verify`, value `Click me`. While the label is still *Click me* the condition holds and the body runs.
4. Loop body: button → `X` (*Click button*).
5. After the loop, one more TestStep with the button → `X` (*Click button* final). When the label becomes *Enough*, the verification fails, the loop exits, and the final click completes the obstacle.

:::caution
`While`, `Do` and `If` exist in Tosca, but Tricentis does not recommend building logic into TestCases; Tosca is not a programming language. Use a loop only when the scenario genuinely requires it, as here.
:::

## Escape (obstacle 26)

**Problem.** Type the literal text `{CLICK}` into a text box.

**Cause.** `{CLICK}` is a Tosca expression. Entered as is, the TestStep clicks the text box instead of typing into it; a plain word such as `username` is typed normally.

**Solution.** Escape the value so that Tosca reads it as plain text. Either:

- right-click the value cell and choose **Escape value**, which wraps the value in double quotes for you, or
- type the quotes yourself: `"{CLICK}"`.

Both mark every character inside as literal. The same escaping applies whenever a value contains characters Tosca would otherwise parse (`{`, `}`, `[`, `]`, `"`), see [String operations](/ToscaBase/expressions/string-operations/).

:::note
Lesson 132 describes the value as the bare word `click` and never shows the value cell; Lesson 66 shows both the obstacle text and the TestStep, and the value is `{CLICK}` with braces. It is the braces that make Tosca parse it as a command.
:::

## Halfway (obstacle 27)

**Problem.** A long button that only reacts when clicked in its **right** half. A plain click lands in the centre and nothing happens.

**Cause.** `{CLICK}` and `X` click the centre of the control.

**Solution.** Give the click method an offset. `{CLICK}` and `{LONGCLICK}` take two optional parameters in square brackets after the expression, `OffsetHorizontal` first and `OffsetVertical` second, each in pixels or as a percentage of the control's size; the value cell's tooltip confirms the reading (*80% horizontal offset*). Without offsets the click lands at 50 % / 50 %.

```text
{CLICK}[80%]          right half, vertical centre
{CLICK}[95%][10%]     far right, near the top edge
```

`80%`, `90%` and `95%` all pass the obstacle; `30%` clicks the left half and fails. `{LONGCLICK}` holds the left mouse button for at least two seconds and takes the same offsets; use it for controls that need a long press or that fail to react to a quick click.

:::note
Lesson 133 confirms the value `90%` inside the `{CLICK}` expression but never shows how it is written; the bracket form above is from Lesson 65.
:::

## Red stripe (obstacle 30)

**Problem.** Clicking *Generate* shows a number (for example `62`) and a red stripe. The number is how far from the left edge, as a percentage of the screen width, the stripe appears. Click the stripe.

**Cause.** The stripe has no control to scan; the click target is a screen position derived from a value on the page. The number itself is in a hidden `div`.

**Solution.**

1. Scan *Generate*. To find the number, raise the **filtered items** level two steps until the hidden `div` appears; identify it by its unique `id` and `tag`, unticking `InnerText`: that, like `InnerHTML` and `OuterText`, holds the changing number.
2. TestCase, step 1: *Generate* → `X`; number `div` → property `InnerText`, ActionMode `Buffer`, value `num`.
3. Step 2: right-click → **Search and add TestStep**, type *Click On Screen* and pick the *TBox XEngines HTML* variant, not the Mobile one. It has three attributes:
   - `Caption`: the window title of the application; a partial title with a wildcard (`Tricentis Obst*`) is enough.
   - `X coordinate`: `{B[num]}`.
   - `Y coordinate`: any value, since the stripe runs from top to bottom; both lessons use `{B[num]}` again so the click lands on a definite point.

:::note
The page describes the number as a percentage of the screen width, and both lessons pass it straight into the X coordinate with success. Lesson 72 calls the coordinates "horizontal and vertical percentage", Lesson 136 does not say; neither shows what the module does with a value above 100. Test it against your own screen resolution.
:::

Click On Screen is one more way to click when no control can be steered; it sits alongside `{CLICK}`, `X` and the offset form above. Related window-level modules are in [Window operations](/ToscaBase/standard-modules/window-operations/).
