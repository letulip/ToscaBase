---
title: Manual execution
description: Running an execution entry as a manual TestCase through the checklist window, attaching screenshots and comments, switching back to automation, and setting a result by hand.
level: 2
sidebar:
  order: 30
sources:
  - id: FCtiAl8IbQg
    title: "Tosca Tutorial | Lesson 65 - Execute Test Cases Manually | Execution Lists | Manual Testing |"
    url: https://www.youtube.com/watch?v=FCtiAl8IbQg
    at: "00:08"
  - id: F33QydlpDI0
    title: "Tosca Tutorial | Lesson 66 - Set Execution Results Manually in Execution Lists | Manual Testing |"
    url: https://www.youtube.com/watch?v=F33QydlpDI0
    at: "00:08"
---

An ExecutionList can hold manual TestCases, and any automated TestCase can be run **as a manual test**: Tosca walks you through the TestSteps in a checklist, you verify each one on the application and record pass or fail, and the result lands in the `ActualLog` like an automated run. Separately, you can overwrite the result of an execution entry without executing anything. Both are ways to keep the ExecutionList truthful when automation cannot deliver in time.

## When to run automation manually

Typical case: an automated TestCase fails at some step, there is no time to fix the remaining steps, and the release decision needs results today. Run the same entry as a manual test, verify the application by hand along the TestSteps, and the stakeholders get a complete result with evidence.

## Run as manual TestCase

1. In the ExecutionList, right-click an execution entry, an execution entry folder, or the whole list > **Run as manual TestCase** (`Ctrl+Shift+M`).
2. The **checklist window** opens. It lists every TestStep with its values, ActionModes and previous results.
3. For each step, perform it in the application and click **Pass** or **Fail** in the result column. The folder counter updates (for example 1 of 64 steps passed). A result can be cleared again.
4. Optionally add a **comment**, an **attachment**, or a **screenshot** to the step. The screenshot tool has annotation options (arrows, lines, text boxes) and **Save and close**.
5. When done, **Finish** the execution.

A new execution log is added under the entry, showing which steps passed and failed, with the screenshots and comments you attached. Because the checklist carries values, screenshots and comments, the result doubles as a live test document.

### Checklist window controls

- **Collapse / Expand**: shrink the window so the application stays visible, and bring it back.
- **Mini size / Full size**: show only the step currently being executed, or the whole checklist.
- **Enable automation / Manual**: once the manual part is done, mark all remaining steps as automated and continue the run as automation; the reverse switch is also there.
- **Inject data value**: send the value of the selected TestStep to the system under test.
- **Set passed / Set failed** on the top bar, equivalent to the buttons in the result column.
- **Pause**: enabled while an automated run is in progress, pauses it.

## Setting a result manually

To change the recorded result of an execution entry without running it:

1. Right-click the execution entry > **Set result**.
2. Choose **Passed**, **Failed** or **No result**.
3. Enter a comment when prompted (for example `manually set to no result`) and confirm.

The most recent execution shows the new result, the log info records **who** set it and the comment, and the start time is logged. A manually set failure also marks the containing TestCase as failed in the statistics.

Use it to reset an entry to **No result** at the start of a release cycle, or to record a failure you found by hand in a feature the automation did not reach.

## Related

- [ExecutionLists](/ToscaBase/execution/execution-lists/) for creating and running lists.
- [Results and logs](/ToscaBase/execution/execution-results-and-logs/) for reading and archiving what these runs produce.
