---
title: Buffers
description: What a Tosca buffer is, how to create one with the Buffer ActionMode or TBox Set Buffer, read it with {B[name]}, extract dynamic text with the XBuffer {XB[name]}, and inspect or edit buffers in the Buffer Viewer.
level: 2
sidebar:
  order: 10
sources:
  - id: cTqAz-nwRV8
    title: "Tricentis Tosca Tutorial Part-9 : Tosca Buffer"
    url: https://www.youtube.com/watch?v=cTqAz-nwRV8
    at: "00:45"
  - id: HOZ81KPcyMY
    title: "Tosca Tutorial | Lesson 77 - View and Manage buffers using Buffer Viewer | Tools |"
    url: https://www.youtube.com/watch?v=HOZ81KPcyMY
    at: "00:08"
  - id: HhOPIJ-fwyI
    title: "Tosca Tutorial | Lesson 116 - Extract Text | XBuffer | Dynamic Text | Obstacle 10 |"
    url: https://www.youtube.com/watch?v=HhOPIJ-fwyI
    at: "03:22"
---

A **Buffer** is Tosca's variable: a named value that a TestStep writes during execution and later TestSteps read back. Buffers are the simplest of the parameterisation approaches Tosca offers (the others are [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/), [Business Parameters](/ToscaBase/data-and-parameters/business-parameters-and-libraries/), TestCase-Design and [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/)). They are the standard way to carry a value the application generates, such as an order number or a total amount, from the screen where it appears to the screen where it is needed.

## Lifetime and scope

- A buffer is created the first time something writes to it and keeps its value until it is overwritten or deleted. The value is still there **after the execution finishes**, so you can inspect it in the Buffer Viewer.
- Buffers belong to the **local workspace**. They are not checked in to the shared repository, so a buffer written on one machine is not visible on another.
- A new execution simply overwrites buffers with the same names; deleting them at the end of a TestCase is optional housekeeping.

## Creating a buffer

There are three ways to write a buffer:

1. **ActionMode `Buffer` on any TestStepValue.** Set the ActionMode of a ModuleAttribute to `Buffer` and enter the buffer name as the value. At run time Tosca reads the control's current value (for a text element, its inner text) and stores it under that name. This is how you capture what the application shows. See [Action modes](/ToscaBase/test-cases/action-modes/).
2. **`TBox Set Buffer`** and the other buffer Standard Modules, when the value is known in the TestCase (a literal, an expression, another buffer or a Test Configuration Parameter). The four Modules, `Set Buffer`, `Partial Buffer`, `Name to Buffer` and `Delete Buffer`, are documented in [Buffer operations](/ToscaBase/standard-modules/buffer-operations/).
3. **A dynamic XBuffer inside a `Verify` step**, described below, when only part of a text is interesting.

The ScratchBook log reports every buffer that a step creates, with its value, which makes ScratchBook a quick way to check that a buffer step works.

## Reading a buffer: `{B[name]}`

Wherever a TestStepValue accepts text, `{B[MyBuffer1]}` is replaced by the current value of the buffer `MyBuffer1`. Typical uses:

- as the **Input** value of a control, to type a captured value back into the application;
- as the **Value** of `TBox Set Buffer` or `TBox Partial Buffer`, to copy or cut a buffer;
- inside [expressions](/ToscaBase/expressions/) such as string operations, where the buffer is normally the first argument;
- as the value of a Module-level Configuration Parameter, so that a Module setting such as `ConstraintIndex` is driven from the TestCase (see [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/#identical-browser-tabs)).

Buffers and Test Configuration Parameters combine naturally: `TBox Set Buffer` with the value `{CP[MyTCP]}` copies a configuration value into a buffer, and the log shows the resolved value.

## Extracting dynamic text: the XBuffer `{XB[name]}`

When a text contains a changing part, buffering the whole element is not enough. The **dynamic XBuffer** verifies the fixed part of a text and buffers the variable part in one step.

Scenario from the video: a success message reads "Purchase completed" followed by a total amount, the amount changes every time, and the amount must be entered into a text box on the same page.

1. Scan the page. The message element is not shown by default; raise the number of filtered items in the scan until the text element appears, then select it together with the target text box and save the Module.
2. In the TestCase, on the message element use the `InnerText` property (its properties show that inner text holds the full message including the amount).
3. Set the ActionMode to **`Verify`** and, as the value, paste the message text with the amount replaced by `{XB[amount]}`.
4. On the text box, ActionMode `Input`, value `{B[amount]}`.

At run time the `Verify` step checks that the fixed text matches and stores whatever stands in the `{XB[amount]}` position in the buffer `amount`; the next step types it. The execution log shows both the verification and the input.

:::note
The speaker also says he "put a regular expression" at the place of the amount, but the exact pattern is not visible in the transcript. The step works as described with the plain `{XB[amount]}` placeholder; combine it with a regular expression only if the fixed text itself varies. Regular expressions in verifications are covered in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).
:::

The same technique reads a changing cell of a web table, see [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).

## Buffer Viewer

**Tools > Buffer Viewer** opens a separate window listing every buffer in the workspace, whichever way it was created. Besides viewing, the window edits buffers, and every change takes effect immediately:

| Action | How |
|---|---|
| Search | Type in the search box; every buffer whose name or value contains the text is listed (searching `X` lists all buffers containing that character) |
| Rename | Click the name cell and type a new name |
| Change a value | Click the value cell and type |
| Add a buffer | Go to the empty last row, edit it, enter name and value |
| Delete | Select one row, or several with **Ctrl**, and press **Delete** |

Use the Buffer Viewer after a ScratchBook run to confirm what a step actually captured, to prepare a buffer by hand before running a step that reads it, and to clean up when a project has accumulated many buffers.

## Related

- [Buffer operations](/ToscaBase/standard-modules/buffer-operations/): `TBox Set Buffer`, `Partial Buffer`, `Name to Buffer`, `Delete Buffer` with a worked example
- [Action modes](/ToscaBase/test-cases/action-modes/): the `Buffer` and `Verify` ActionModes
- [String operations](/ToscaBase/expressions/string-operations/): trimming and cutting buffered text
