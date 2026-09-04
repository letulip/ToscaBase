---
title: Buffer operations
description: The four TBox buffer Modules (Set Buffer, Partial Buffer, Name to Buffer, Delete Buffer) and how to use them to extract a value such as an order number.
level: 2
sidebar:
  order: 20
sources:
  - id: yj_4PepSreg
    title: "Tosca Tutorial | Lesson 13 - Use Buffer Operations | TBox Automation Modules |"
    url: https://www.youtube.com/watch?v=yj_4PepSreg
    at: "02:10"
---

A Buffer is a named value that a TestStep writes during execution. It does not disappear when the run ends: it stays in the local workspace until it is overwritten or deleted, which is why it can be inspected afterwards in the Buffer Viewer (lifetime, scope and the viewer are covered in [Buffers](/ToscaBase/data-and-parameters/buffers/)). Besides the `Buffer` ActionMode on any control, the TBox Automation Modules give you four dedicated buffer operations. Searching **Add TestStep** for `TBox buffer` lists all of them: **TBox Set Buffer**, **TBox Partial Buffer**, **TBox Name to Buffer** and **TBox Delete Buffer**.

## TBox Set Buffer

Creates a buffer, or overwrites an existing one, with a given value.

| ModuleAttribute | Meaning |
|---|---|
| Buffer name | Name of the buffer to create, for example `OrderNum` |
| Value | The value; can be a literal, another buffer `{B[...]}` or an expression |

Switch the ActionMode of the value to `Verify` and the same Module **verifies** the current value of an existing buffer instead of setting it. The value can be an expression, so a Set Buffer step is the usual place to clean a value, for example trimming whitespace from a buffered text before working with it.

## TBox Partial Buffer

Extracts part of a text and stores it in a buffer.

| ModuleAttribute | Meaning |
|---|---|
| Buffer name | New buffer that receives the extracted part |
| Value | Source text, usually a buffer such as `{B[OrderNum]}` |
| Start | Index of the first character to take |
| End | Index of the last character to take |
| Last | Number of characters to take counting from the end of the text |

- `Start` + `End` take a range: `Start` = 1 and `End` = 5 return the first five characters.
- `Last` = 7 returns the last seven characters.
- Do **not** combine `Start`/`End` with `Last`; they contradict each other. Pick the parameter that fits your use case.

With the ActionMode set to `Verify`, Partial Buffer verifies the extracted part against an expected value instead of storing it. That only makes sense when the expected value is known (for example from requirements), not for values the application generates dynamically.

## TBox Name to Buffer

Stores the **name of the TestCase** that contains the step into a buffer. The only ModuleAttribute is the buffer name (for example `TC_Name`). It is a niche operation but handy when a step needs to know which TestCase it runs in.

:::caution
Name to Buffer works only when the TestCase is run from an **ExecutionList**. The ScratchBook does not support it.
:::

## TBox Delete Buffer

Deletes one or more buffers by name. Use it as a final clean-up step listing every buffer the TestCase created; the log confirms each buffer was deleted. It is optional: a new execution simply overwrites buffers with the same names.

## Worked example: extract an order number

The task is to read a confirmation text such as `Your order number is: 1234567` (with surrounding whitespace) and end up with just the number. A previous approach used a long expression of string operations (trim, replace with ignore-case); see [String operations](/ToscaBase/expressions/string-operations/). The buffer Modules give a shorter alternative:

1. **Buffer the text.** On the control that shows the text, set the ActionMode to `Buffer` and buffer its inner text into `B_order`.
2. **TBox Set Buffer.** Buffer name `OrderNum`, value = the trim function applied to `{B[B_order]}`. Trimming is required first; otherwise the whitespace is still there when you extract a part.
3. **TBox Partial Buffer.** Buffer name `OrderNumber`, value `{B[OrderNum]}`, `Last` = 7. Counting from the end is the right choice because the text before the number varies in length, so `Start`/`End` would need counting dozens of characters.
4. **TBox Partial Buffer (Verify).** Same buffer, ActionMode `Verify`, expected = the number; only for demonstration, because a real order number is not known in advance.
5. **TBox Name to Buffer.** Buffer name `TC_Name`.
6. **TBox Delete Buffer.** `OrderNum`, `OrderNumber`, `TC_Name`.

Run it from an ExecutionList (step 5 needs it). The log shows `B_order` set to the raw text with whitespace, the trimmed value, the seven extracted characters, the verification passing, the TestCase name stored in `TC_Name`, and the three buffers deleted.

## Related

- [Action modes](/ToscaBase/test-cases/action-modes/) for the `Buffer` and `Verify` ActionModes
- [Buffers](/ToscaBase/data-and-parameters/buffers/) for the Buffer Viewer and XBuffer
