---
title: Action modes
description: Complete reference for the Tosca ActionModes - Input, Insert, Verify, Buffer, WaitOn, Select and Constraint - with value syntax, settings, and worked examples on forms and tables.
level: 1
sidebar:
  order: 20
sources:
  - id: QIZ_97SiLNc
    title: "Tosca Tutorial | Lesson 31 - Use Select, Constraint & Verify Action Modes | Table Objects |"
    url: https://www.youtube.com/watch?v=QIZ_97SiLNc
    at: "00:09"
  - id: H4Khubsu95g
    title: "Tricentis Tosca Tutorial Part-11: Tosca Action Modes-Input,Verify,Constraint, Dynamic Buffer"
    url: https://www.youtube.com/watch?v=H4Khubsu95g
    at: "02:21"
  - id: "-rQU1krBgHU"
    title: "Tosca Tutorial | Lesson 29 - How to use Action Mode Buffer | Action Modes | Building Test Cases |"
    url: https://www.youtube.com/watch?v=-rQU1krBgHU
    at: "00:10"
  - id: V8gPjt1dqVQ
    title: "Tosca Tutorial | Lesson 30 - What is WaitOn Action Mode? | Action Modes | Building Test Cases |"
    url: https://www.youtube.com/watch?v=V8gPjt1dqVQ
    at: "00:10"
---

An ActionMode tells Tosca how to apply the **Value** of a TestStepValue to the control it steers: type it in, compare it, store it, wait for it, or use it to narrow a search. Every TestStepValue has exactly one ActionMode, chosen from a drop-down in the TestStep. Which ActionModes are offered depends on the interface type of the Module (GUI or non-GUI). This page is the reference for all seven; the surrounding concepts are in [TestCase basics](/ToscaBase/test-cases/test-case-basics/).

## Summary table

| ActionMode | What it does with the Value | Typical use | Notes |
|---|---|---|---|
| `Input` | Enters the value into the control, or clicks it | Text fields, drop-downs, radio buttons, buttons, links | Default for input and clickable controls |
| `Insert` | Creates an object in a non-UI structure | XML and other non-GUI interfaces | Not offered for GUI Modules |
| `Verify` | Compares a property of the control with the value | Verification points | Logged with expected and actual values |
| `Buffer` | Stores the control's value under the buffer name given in the Value | Reusing values later in the same or another TestCase | Value is the buffer name |
| `WaitOn` | Pauses until the condition in the Value is true | Dynamic synchronisation | Bounded by a timeout setting; shown with a yellow background |
| `Select` | Selects a node in a hierarchy | Table, row and column nodes | Set automatically by Tosca on table paths |
| `Constraint` | Limits the search below a superordinate node to items matching the value | Picking a table row by cell content | Combine several to make a match unique |

## Input

`Input` is the ActionMode Tosca pre-selects for any input or clickable control. What you put in the Value depends on the control:

- **Text field.** The text to type.
- **Drop-down.** One of the options listed in the ModuleAttribute's value list; XScan captures the options when the Module is scanned, so you pick from them rather than typing.
- **Radio button, checkbox.** The state to set.
- **Button or link.** `X` performs the click internally, without moving the pointer. `{CLICK}` performs a physical mouse click with mouse movement. Prefer `X`; see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/) for why.

Values can be expressions rather than literals: random values, dates, string operations and buffers `{B[name]}` are all valid inputs. See the [Expressions](/ToscaBase/expressions/) section.

## Insert

`Insert` exists for non-UI interfaces only; GUI Modules do not offer it. It creates objects inside a structure such as an XML document. The XML use case is covered in [XML engine](/ToscaBase/engines/xml-engine/).

## Verify

`Verify` compares a property of the control with the expected value. The Value drop-down lists the available properties (`Exists`, `Enabled`, `Visible`, `InnerText` and others) and you complete the condition, for example:

- `Exists == True` checks that the control is on the page.
- `Enabled == True` checks that a button is clickable.
- `InnerText == jane@example.com` checks the displayed text of a link or cell.

When the condition holds, the TestStepValue passes; otherwise the TestStep and TestCase fail. The ExecutionLog records a verification entry with the expected and the actual value, and only `Verify` steps produce such an entry, which is one reason every TestCase should contain at least one (see [TestCase structure](/ToscaBase/best-practices/test-case-structure/)). Verification against intervals, regular expressions and multilingual alternatives is in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).

## Buffer

A buffer is a named value stored temporarily in Tosca Commander so that it can be reused later, in a later TestStep or in another TestCase; the speaker compares it to a global variable. `Buffer` is one of several ways to create one (the standard Modules in [Buffer operations](/ToscaBase/standard-modules/buffer-operations/) are another).

1. Set the ActionMode of the control to `Buffer`. Tosca fills the Value with the control's name; change it to the buffer name you want, for example `email`.
2. At execution Tosca reads the control's current value and stores it under that name. The log reports that a buffer with that name was set to the value.
3. Read it back anywhere with the dynamic expression `{B[email]}`. Typing `{B` in a Value shows the description *returns the value stored in the specified buffer*.
4. Buffers are visible under **Settings > Engine > Buffer** as name/value pairs, and in the Buffer Viewer; see [Buffers](/ToscaBase/data-and-parameters/buffers/).

**Worked example (login verification).** Log in (`Input` on the link, the fields and the button), then on the header control that shows the logged-in user set `Buffer` with Value `email`. Add the same Module again with `Verify` on that control and Value `{B[email]}`, then click `Logout`. The log shows the verification with expected and actual value. The same pattern verifies table values from a database against the application, or vice versa.

**Dynamic buffer inside a Verify.** A `Verify` value can contain `{XB[name]}` in place of a changing part: the fixed part is verified and the changing part is stored in the buffer `name` at the same time. In the source a link shows a version number; verifying `InnerText` with the number replaced by `{XB[buffer_version]}` passes and leaves `buffer_version` in the Buffer Viewer. See [Buffers](/ToscaBase/data-and-parameters/buffers/) for `{XB[...]}`.

## WaitOn

`WaitOn` is Tosca's dynamic wait: it interrupts execution until the property named in the Value has the specified value, then continues immediately. Tricentis recommends it whenever you wait for a condition in the application or for a control that is not yet visible, instead of a static `TBox Wait`, which always waits the full duration and slows every run.

- The Value is a condition such as `Enabled == True` or `Exists == True`.
- A `WaitOn` TestStepValue is shown with a yellow background.
- The maximum wait is **Settings > TBox > Synchronization > Synchronization timeout during WaitOn**, 20000 ms by default; raise or lower it as needed. If the condition is not met within the timeout the step fails.

**Worked example (obstacle 33678).** Clicking `Calculate` starts a progress bar, and `Send` becomes enabled only when the bar completes. Three steps: `Calculate` → `X` (`Input`); `Send` → `Enabled == True` (`WaitOn`); `Send` → `X` (`Input`). The run waits exactly until the button is enabled and keeps working if the loading time changes later. The full argument against static waits is in [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).

## Select

`Select` picks a specific node in a hierarchy. You rarely set it by hand: when a scanned table is steered, Tosca automatically assigns `Select` to the table node and the row node on the way down to a cell. Row selection uses `$1` for the first row, `$last` for the last, or `$n` for row *n*; columns are addressed by the header names XScan captured. See [Table controls](/ToscaBase/modules/table-controls/) for the Module side.

## Constraint

`Constraint` limits the search below a superordinate node (usually a table row) to the items whose value matches. Instead of looping over rows and comparing cells, you declare which cell values identify the row and Tosca finds it directly; with hundreds of rows this is also much faster. Any number of constraints can be combined on the same row, and you need as many as it takes to make the match unique.

**Worked example (verify an email in a table).**

1. Scan the page and keep only the table in the Module.
2. In the TestStep expand the table and the row (`Select` is set automatically) and choose the `First name` cell. Set its ActionMode to `Constraint` with Value `InnerText == Jane`.
3. Choose the `Email` cell with ActionMode `Verify` and Value `InnerText == jane@example.com`.

The run finds the row whose first name is Jane and verifies its email; the log shows the selected row and the verification. If two rows share a first name (`John Doe` and another `John`), a single constraint fails because the row is not unique; add a second constraint on `Last name` = `Doe` and the row is identified.

**Reading a cell after a constraint.** In the LambdaGeeks example the first column is constrained to `Worldwide cover` and the cell under column `Gold` is set to `Buffer` with Value `buffer_gold`; the log confirms the buffer holds the cell's value. Constraint plus `Buffer` extracts, Constraint plus `Verify` checks. More table patterns are in [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).

:::note
The LambdaGeeks transcript describes selecting "cell label as $1" for the constrained cell; the QAScript lesson shows `$1` as the row selector. Row selectors apply to rows, not cells; the wording in the first source is unclear.
:::

## Choosing an ActionMode

- Act on the application: `Input` (GUI) or `Insert` (non-GUI).
- Prove something happened: `Verify`.
- Keep the value for later: `Buffer`; both at once: `Verify` with `{XB[...]}`.
- Wait for the application: `WaitOn`, never a static wait.
- Inside a table: `Select` (automatic) to reach the row, `Constraint` to pick it, then `Verify`, `Buffer` or `Input` on the target cell.

Mixing ActionModes in one TestStep is normal; the table example uses `Select`, `Constraint` and `Verify` together.
