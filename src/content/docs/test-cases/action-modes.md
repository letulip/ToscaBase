---
title: ActionModes
description: Complete reference for the Tosca ActionModes - Input, Insert, Verify, Buffer, WaitOn, Select and Constraint - with value syntax and settings, and links to the worked examples.
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
  - id: DFlqBXN_MDM
    title: "TRICENTIS Tosca 16.0 - Lesson 12 | Action Modes | Set Action Modes WaitOn | Verify | Select |"
    url: https://www.youtube.com/watch?v=DFlqBXN_MDM
    at: "03:51"
  - id: XYRtKA8lkBI
    title: "TRICENTIS Tosca 16.0 - Lesson 13 | Action Mode Buffer | Math Function | Dynamic Expressions |"
    url: https://www.youtube.com/watch?v=XYRtKA8lkBI
    at: "04:27"
  - id: GsSNWhKRiRQ
    title: "TRICENTIS Tosca 16.0 - Lesson 13 (Updated) | Action Mode Buffer |Math Function |Dynamic Expressions|"
    url: https://www.youtube.com/watch?v=GsSNWhKRiRQ
    at: "02:03"
  - id: 323__eiE-WM
    title: "TRICENTIS Tosca 16.0 - Lesson 25 | ActionMode Constraint | Actoin Modes |"
    url: https://www.youtube.com/watch?v=323__eiE-WM
    at: "02:03"
---

An ActionMode tells Tosca what to do with the **Value** of a TestStepValue: type it in, compare it, store it, wait for it, or use it to narrow a search. Each TestStepValue has one ActionMode, chosen in the **ActionMode** column; which ones are offered depends on whether the Module is GUI or non-GUI. This page is the reference for all seven; the surrounding concepts are in [TestCase basics](/ToscaBase/test-cases/test-case-basics/).

## Summary table

| ActionMode | What it does with the Value | Typical use | Notes |
|---|---|---|---|
| `Input` | Enters the value into the control, or clicks it | Text fields, drop-downs, checkboxes, buttons, links | Default; set automatically when a value is typed |
| `Insert` | Creates an object in a non-UI structure | XML and other non-GUI interfaces | Not offered for GUI Modules |
| `Verify` | Compares a property of the control with the value | Verification points | Logged with expected and actual values |
| `Buffer` | Stores a property of the control under the buffer name given in the Value | Reusing values later | See [Buffers](/ToscaBase/data-and-parameters/buffers/) |
| `WaitOn` | Pauses until the condition in the Value is true | Dynamic synchronisation | Bounded by a timeout setting; yellow background |
| `Select` | Navigates to a node in a hierarchy without steering it | Table, row and column nodes, drop-downs | Set automatically by Tosca on table paths |
| `Constraint` | Limits the search below a node to items matching the value | Picking a table row by cell content | Combine several to make a match unique |

## Input

`Input` is the default: Tosca pre-selects it for any input or clickable control and switches to it as soon as you type a value. What goes in the Value depends on the control:

- **Text field.** The text to type.
- **Drop-down.** One of the options XScan captured when the Module was scanned; pick from the list rather than typing.
- **Radio button, checkbox.** The state to set, for example `True`.
- **Button or link.** `X` performs the click internally, without moving the pointer. `{CLICK}` performs a physical mouse click with mouse movement. Prefer `X`; see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).

Values can be expressions: random values, dates, string operations and buffers `{B[name]}` are all valid inputs, and **Translate value** on the right-click menu shows what an expression resolves to before you run. See [Expressions](/ToscaBase/expressions/).

## Insert

`Insert` is offered for non-UI Modules only and creates objects inside a structure such as an XML document; see [XML engine](/ToscaBase/engines/xml-engine/).

## Verify

`Verify` compares a property of the control with the expected value. Click the arrow in the Value cell to pick the property (`Exists`, `Enabled`, `Visible`, `InnerText` and others) and complete the condition:

- `Exists == True`: the control is on the page.
- `Visible == True`: the order-confirmation message is shown.
- `Enabled == True`: a button is clickable.
- `InnerText == 10.00`: the displayed text of a cell or link.

When the condition holds, the TestStepValue passes; otherwise the TestStep and the TestCase fail. The ExecutionLog records a verification entry with expected and actual value, and only `Verify` steps produce one, which is one reason every TestCase should contain at least one (see [TestCase structure](/ToscaBase/best-practices/test-case-structure/)). To debug one verification, run only its TestStep folder in the ScratchBook.

:::caution
Set the **data type** of a numeric verification to `Numeric`. In Lesson 13 a total computed with `{MATH[...]}` failed with expected `35` and actual `35` until the data type was changed from `String`: as strings the two were not identical.
:::

Verification against intervals, regular expressions and multilingual alternatives is in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).

## Buffer

`Buffer` stores a property of the control under the buffer name given in the Value. Pick the property through the arrow in the Value cell (for a price label, `InnerText`), type the buffer name (`PriceBlueJeans`) and set the ActionMode; the `=` between property and name turns into an arrow, showing that the value flows into the buffer. At execution Tosca reads the control, writes the buffer and reports it in the log. Read it back with `{B[PriceBlueJeans]}`, for example in a later `Verify` of the cart subtotal against `{MATH[{B[PriceBlueJeans]}*25]}`. To verify a value and store part of it in one step, put `{XB[name]}` inside a `Verify` value.

:::note
Lesson 13 (Updated) says a buffer can only be used in the TestCase that created it, and that shared data belongs in test data. Lesson 29 of the earlier playlist reads a buffer in another TestCase, and the Buffer Viewer shows buffers surviving the run. Cross-TestCase use works but is fragile: the execution order decides whether the value is there.
:::

How buffers are otherwise created, read, scoped and inspected in the Buffer Viewer, including `{XB[...]}`, is in [Buffers](/ToscaBase/data-and-parameters/buffers/).

## WaitOn

`WaitOn` is Tosca's dynamic wait: it interrupts execution until the property named in the Value has the specified value, then continues immediately. Use it instead of a static `TBox Wait`, which always waits the full duration and slows every run.

- The Value is a condition such as `Enabled == True` or `Visible == True`.
- A `WaitOn` TestStepValue is shown with a yellow background; the log reports the wait as successful with expected and actual value.
- The maximum wait is **Settings > TBox > Synchronization > Synchronization timeout during WaitOn**, 20000 ms by default. If the condition is not met within the timeout the step fails.

Typical places: a `Send` button that is enabled only once a progress bar completes ([Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/)), or a `WaitOn` `Visible == True` on the `Login` link after `Logout`, so the browser is closed only once the logout has completed.

## Select

`Select` is a passive ActionMode: it navigates to a node in a hierarchy (table, row, column, drop-down) without sending anything to it, so that a child node can be steered. You rarely set it by hand: when a scanned table is steered, Tosca assigns `Select` to the table and row nodes on the way down to a cell. Rows are picked with `$1` for the first, `$last` for the last or `$n` for row *n*; columns by the header names XScan captured or by position (`#2` for the second column of a headerless price table: `#n` is the *n*-th match, and without a constraint every column matches). The cell itself then gets `Verify`, `Buffer` or `Input`. Full selector list: [Table controls](/ToscaBase/modules/table-controls/).

## Constraint

`Constraint` limits the search below a superordinate node (usually a table row) to the items whose value matches. You declare which cell values identify the row and Tosca finds it directly, which with hundreds of rows is far faster than a loop. Combine as many constraints as it takes to make the match unique: in Lesson 25 a cart holds two `Music 2` albums at different prices, so `Product` = `Music 2` alone fails; a second constraint on `Price` matching `10.00` identifies the row, an `Input` of `True` on its `Remove` checkbox marks it, `Update shopping cart` is clicked with `X`, and a `Verify` on the subtotal (data type `Numeric`) proves the right item went.

Within one TestStep the pattern is always the same: `Select` (automatic) on the table and the row, `Constraint` on the identifying cells, then `Verify`, `Buffer` or `Input` on the target cell: Constraint plus `Verify` checks, plus `Buffer` extracts, plus `Input` acts on the row. Mixing ActionModes in one TestStep is normal. More table examples, including `#n` for the *n*-th matching row, are in [Table controls](/ToscaBase/modules/table-controls/); shuffled rows and other problem tables in [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).
