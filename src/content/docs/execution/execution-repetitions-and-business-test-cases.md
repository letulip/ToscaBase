---
title: Repetitions and business TestCases
description: Running an execution entry several times with the Repetitions property, and assembling business TestCases and business ExecutionLists into an end-to-end view for stakeholders.
level: 2
sidebar:
  order: 40
sources:
  - id: jQ-UZfAcU9o
    title: "Tosca Tutorial | Lesson 67 - Execute Test Case Multiple Times from Execution Lists | Repetitions |"
    url: https://www.youtube.com/watch?v=jQ-UZfAcU9o
    at: "00:08"
  - id: D9N2HVczgPc
    title: "Tosca Tutorial | Lesson 68 - Use Business Test Cases | Execution Lists | End-to-End Scenarios |"
    url: https://www.youtube.com/watch?v=D9N2HVczgPc
    at: "00:08"
---

Two features of the Execution section that change *how* a list runs and *how its results are read*, without touching the TestCases themselves: the **Repetitions** property on an execution entry, and the pair **business TestCase** plus **business ExecutionList** that stitches several ExecutionLists into one end-to-end result.

## Repeating an execution entry

The `Repetitions` property is known from TestCase folders (see [Repetitions](/ToscaBase/test-cases/repetitions/)). The same property exists on an **execution entry**, so a TestCase that has no repetition configured inside it can still be run several times from the ExecutionList.

1. Drag the TestCase into an ExecutionList; it becomes an execution entry.
2. Open the entry's **Properties** and set `Repetitions` to the number of runs, for example `3`.
3. Run the entry or its folder. Expanding the entry afterwards shows three executions in the log.

The values used by each repetition can still be varied the usual way. Choose the entry-level property when the repetition is an execution decision (soak, retry, per-environment runs) rather than part of the test design.

## Business TestCases and business ExecutionLists

Individual TestCases cover one function each: register a user, log in, process an order. Management wants to know whether the **business process** built from them works end to end, possibly across several applications, releases or execution runs. Business TestCases and business ExecutionLists provide that view.

- A **business TestCase** is a structural TestCase in the TestCases section. It only references other TestCases and fixes their order. It cannot be executed.
- A **business ExecutionList** is a structural list in the Execution section. It links a business TestCase and the ExecutionLists whose results belong to it. It cannot be executed either; it **concatenates the results** of the linked ExecutionLists.

### Creating them

1. In the TestCases section, create a folder (for example `Business scenarios`), right-click it and choose the option with the **briefcase icon** to create a business TestCase. Name it, for example `End-to-end scenario`.
2. Drag the individual TestCases into it in the order the business process runs: register, login, order processing.
3. In the Execution section, in a matching folder, create a **business ExecutionList** with the same name.
4. Drag the business TestCase onto the business ExecutionList to link them.
5. Drag the individual **ExecutionLists** that executed those TestCases onto the business ExecutionList, in the same order.

The business ExecutionList now shows the combined result: in the example, register and login passed while order processing failed, which is exactly the sentence to give the business: the process is broken at order processing.

:::note
Because both objects are structural, there is no **Run** option on them. Execute the underlying ExecutionLists as usual; the business ExecutionList reflects their `ActualLog`.
:::

The linked lists do not have to come from the same application or the same release. Dragging ExecutionLists from different release runs gives a chronological picture of the same process across releases.

## Related

- [ExecutionLists](/ToscaBase/execution/execution-lists/) for creating the lists that feed a business ExecutionList.
- [Results and logs](/ToscaBase/execution/execution-results-and-logs/) for archiving per release, which keeps business views accurate.
- [Requirements and risk](/ToscaBase/requirements-and-reporting/requirements-and-risk/) for the requirement-side view of the same results.
