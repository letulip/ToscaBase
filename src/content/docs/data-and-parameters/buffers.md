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
  - id: XYRtKA8lkBI
    title: "TRICENTIS Tosca 16.0 - Lesson 13 | Action Mode Buffer | Math Function | Dynamic Expressions |"
    url: https://www.youtube.com/watch?v=XYRtKA8lkBI
    at: "04:27"
  - id: GsSNWhKRiRQ
    title: "TRICENTIS Tosca 16.0 - Lesson 13 (Updated) | Action Mode Buffer |Math Function |Dynamic Expressions|"
    url: https://www.youtube.com/watch?v=GsSNWhKRiRQ
    at: "02:03"
  - id: glZeQF7BWNo
    title: "TRICENTIS Tosca 16.0 - Lesson 22 | Dynamic Comparison | XBuffer Syntax {XB}"
    url: https://www.youtube.com/watch?v=glZeQF7BWNo
    at: "01:03"
---

A **Buffer** is Tosca's variable: a named value that a TestStep writes during execution and later TestSteps read back. It is the simplest of Tosca's parameterisation approaches (the others: [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/), [Business Parameters](/ToscaBase/data-and-parameters/business-parameters-and-libraries/), TestCase-Design, [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/)) and the standard way to carry a value the application generates, such as an order number or a total, from the screen where it appears to the screen where it is needed.

## Lifetime and scope

- A buffer is created the first time something writes to it and keeps its value until it is overwritten or deleted. The value is still there **after the execution finishes**, so you can inspect it in the Buffer Viewer.
- Buffers belong to the **local workspace**. They are not checked in to the shared repository, so a buffer written on one machine is not visible on another.
- A new execution simply overwrites buffers with the same names; deleting them at the end of a TestCase is optional housekeeping.

:::note
Tosca 16 Lesson 13 (Updated) says a buffer should be created and consumed inside the **same TestCase**, with shared data kept in TestCase-Design or Test Data Services; Part-9 and Lesson 77 show buffers surviving the run and being read from another TestCase. Both hold: the buffer persists in the workspace, but reading it from another TestCase works only in that execution order. Treat the same-TestCase rule as the recommended practice.
:::

## Creating a buffer

There are three ways to write a buffer:

1. **ActionMode `Buffer` on any TestStepValue.** Set the ActionMode of a ModuleAttribute to `Buffer` and enter the buffer name as the value. At run time Tosca reads the control's current value (for a text element, its inner text) and stores it under that name. This is how you capture what the application shows. In Tosca 16 you can pick the property explicitly: expand the arrow next to the attribute, choose `InnerText` (for a displayed price, say), enter the buffer name and set the ActionMode; the `=` turns into an arrow to show that the value flows into the buffer. See [ActionModes](/ToscaBase/test-cases/action-modes/).
2. **`TBox Set Buffer`** and the other buffer Standard Modules, when the value is known in the TestCase (a literal, an expression, another buffer or a Test Configuration Parameter). The four Modules, `Set Buffer`, `Partial Buffer`, `Name to Buffer` and `Delete Buffer`, are documented in [Buffer operations](/ToscaBase/standard-modules/buffer-operations/).
3. **A dynamic XBuffer inside a `Verify` step**, described below, when only part of a text is interesting.

The ScratchBook log reports every buffer a step creates, with its value, so ScratchBook is a quick check that a buffer step works.

## Reading a buffer: `{B[name]}`

Wherever a TestStepValue accepts text, `{B[MyBuffer1]}` is replaced by the current value of the buffer `MyBuffer1`. Typical uses:

- as the **Input** value of a control, to type a captured value back into the application;
- as the **Value** of `TBox Set Buffer` or `TBox Partial Buffer`, to copy or cut a buffer;
- inside [expressions](/ToscaBase/expressions/) such as string operations, where the buffer is normally the first argument;
- as the value of a Module-level Configuration Parameter such as `ConstraintIndex`, driven from the TestCase (see [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/#identical-browser-tabs)).

Buffers and Test Configuration Parameters combine naturally: `TBox Set Buffer` with the value `{CP[MyTCP]}` copies a configuration value into a buffer, and the log shows the resolved value.

## Buffers inside expressions

A buffer can be an operand of any dynamic expression, and the result can be verified directly. The Tosca 16 webshop example checks the checkout page after ordering 25 pairs of jeans:

1. On the product page, `Buffer` the `InnerText` of the price element into `PriceBlueJeans`.
2. On the checkout page, `Verify` the subtotal with `{MATH[{B[PriceBlueJeans]}*25]}`.
3. `Buffer` the subtotal into `SubTotal`, then `Verify` the order total with `{MATH[{B[SubTotal]}+10]}`, 10 being the shipping cost verified in a separate step.

Two details make this work. Right-click the value > **Translate value** shows what the expression resolves to (25, 35) before the run, so a malformed formula is caught early. And the TestStepValue's **data type** must be `Numeric`: with the default string type the verification of 35 against 35 failed in the lesson until the type was changed. Expression syntax is in [Expressions](/ToscaBase/expressions/).

## Extracting dynamic text: the XBuffer `{XB[name]}`

When a text contains a changing part, buffering the whole element is not enough. The **dynamic XBuffer** verifies the fixed part of a text and buffers the variable part in one step.

Scenario from the video: a success message reads "Purchase completed" followed by a total amount, the amount changes every time, and the amount must be entered into a text box on the same page.

1. Scan the page. The message element is not shown by default; raise the number of filtered items in the scan until the text element appears, then select it together with the target text box and save the Module.
2. In the TestCase, on the message element use the `InnerText` property (its properties show that inner text holds the full message including the amount).
3. Set the ActionMode to **`Verify`** and, as the value, paste the message text with the amount replaced by `{XB[amount]}`.
4. On the text box, ActionMode `Input`, value `{B[amount]}`.

At run time the `Verify` step checks that the fixed text matches and stores whatever stands in the `{XB[amount]}` position in the buffer `amount`; the next step types it. The execution log shows both the verification and the input.

:::note
The speaker calls the value at the amount position a "regular expression" but dictates only `{XB[amount]}`; the plain placeholder is enough here. Regular expressions in verifications are covered in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).
:::

Lesson 22 applies the same pattern to an order confirmation: `Verify` on the `InnerText` of the confirmation element with the value `Order number: {XB[OrderNumber]}` checks the label and stores the number; the log shows the verification as passed and **Tools > Buffer Viewer** lists `OrderNumber` with the actual value, ready for later steps. If the step belongs to a reusable TestStepBlock, resolve the reference before editing it (see [Business Parameters and TestStepLibraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/)).

The same technique reads a changing cell of a web table, see [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).

## Buffer Viewer

**Tools > Buffer Viewer** opens a window listing every buffer in the workspace, however it was created, and lets you edit them; every change takes effect immediately:

| Action | How |
|---|---|
| Search | Type in the search box; every buffer whose name or value contains the text is listed (searching `X` lists all buffers containing that character) |
| Rename | Click the name cell and type a new name |
| Change a value | Click the value cell and type |
| Add a buffer | Go to the empty last row, edit it, enter name and value |
| Delete | Select one row, or several with **Ctrl**, and press **Delete** |

Use it after a ScratchBook run to confirm what a step captured, to prepare a buffer by hand before a step that reads it, and to clean up accumulated buffers.

## Related

- [Buffer operations](/ToscaBase/standard-modules/buffer-operations/): `TBox Set Buffer`, `Partial Buffer`, `Name to Buffer`, `Delete Buffer` with a worked example
- [ActionModes](/ToscaBase/test-cases/action-modes/): the `Buffer` and `Verify` ActionModes
- [String operations](/ToscaBase/expressions/string-operations/): trimming and cutting buffered text
