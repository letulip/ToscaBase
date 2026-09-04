---
title: Recovery and cleanup scenarios
description: How the Tosca recovery engine retries a failed TestCase - enabling recovery globally or per folder, creating a Recovery Scenario Collection, setting the Retry level, and adding a Cleanup Scenario for when recovery itself fails.
level: 1
sidebar:
  order: 50
sources:
  - id: d_9ugVdRpZY
    title: "Tosca Tutorial | Lesson 49 - Create Recovery Scenarios | Handle Unexpected Errors | Recovery Engine"
    url: https://www.youtube.com/watch?v=d_9ugVdRpZY
    at: "00:02"
  - id: 2xPO0SHEHLo
    title: "Tosca Tutorial | Lesson 50 - Add Cleanup Scenarios to Test Cases | Recovery Engine |"
    url: https://www.youtube.com/watch?v=2xPO0SHEHLo
    at: "00:55"
---

Every automation tool has to deal with unexpected failures; in code you would write a try/catch block. Tosca ships a **recovery engine** instead: you define a collection of TestSteps called a **Recovery Scenario**, and when a TestCase fails Tosca runs those steps and then retries the failed part. If the recovery steps fail as well, a **Cleanup Scenario** brings the application back to a known state so that the remaining TestSteps can still run. Together they keep a long execution from stopping at the first surprise; you look at the failures afterwards instead of losing the whole run.

## Configuring recovery in three steps

1. **Enable recovery**, either for the whole workspace in the settings or for a folder through Test Configuration Parameters.
2. **Create the Recovery Scenario** on a TestCase folder or a single TestCase.
3. **Set the Retry level** property of the scenario so that Tosca knows at which failure it should kick in.

All three are required.

### Step 1a: enable globally

**Settings > TBox > Recovery** lists three failure types, each with the same four possible values:

| Setting | Triggers on |
|---|---|
| **On dialog failure** | Tosca can no longer interact with the application (dialog-level failure) |
| **On exception failure** | An exception during execution |
| **On verification failure** | A `Verify` step fails |

| Value | Meaning |
|---|---|
| Halt execution | Stop completely |
| Execute next test case | Skip to the next TestCase |
| Continue execution | Carry on with the next step |
| Recover | Run the Recovery Scenario |

Choose **Recover** for each failure type you want recovery scenarios to handle. Three more settings in the same dialog cap the number of attempts: **TestCase retries**, **TestStep retries** and **TestStepValue retries**, the maximum number of recovery attempts per TestCase, TestStep and TestStepValue respectively. Any values are allowed; they can differ. Close the dialog and recovery is enabled for every object in the workspace.

### Step 1b: enable per folder

If different folders need different behaviour, set the same options as Test Configuration Parameters on a TestCase folder; they override the global settings for that folder.

1. Select the folder and open its **Test Configuration** tab.
2. **Create Test Configuration Parameter**, choose `On dialog failure`, set it to `Recover`. Repeat for `On exception failure` and `On verification failure`.
3. Add `TestCase retries`, `TestStep retries` and `TestStepValue retries` with the counts you want (the source uses 1, 2 and 2).

See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/) for the mechanism.

### Step 2: create the Recovery Scenario

1. Right-click the TestCase folder and choose **Create Recovery Scenario Collection** (**Ctrl+N**, **Ctrl+R**). Tosca adds a folder `Recovery Scenarios` (white plus icon).
2. Right-click that folder and choose **Create Recovery Scenario** (red plus icon). A collection can hold several scenarios.
3. Add the TestSteps that should run when recovery is triggered, exactly as in a normal TestCase.

### Step 3: set the Retry level

Open the Recovery Scenario's properties and set **Retry level** to `TestCase`, `TestStep` or `TestStepValue`. This decides which failure starts the recovery: the failure of the whole TestCase, of a TestStep, or of a single TestStepValue. The source keeps `TestCase`.

## Worked example

A page has a `Submit` button that, after a recent change, is disabled for about 13 seconds after load. The TestCase is: `OpenUrl`; on `Submit`, `Verify` `Enabled == True` then click `X`; close the page. It fails at the verification because the button is not yet enabled.

The Recovery Scenario contains a single TestStep on the same button with ActionMode `WaitOn` and value `Enabled == True`, renamed `Check submit`. Retry level is `TestCase`, TestCase retries is 1. Running the folder from an ExecutionList gives this log:

1. `Submit enabled` verification fails.
2. The recovery engine starts the Recovery Scenario; `Check submit` waits until the button is enabled.
3. The TestCase is executed again: the verification now passes, the click happens, the TestCase passes.

With retries set to 1 there is one attempt. If a scenario needs more, raise `TestCase retries`; Tosca stops retrying as soon as the TestCase passes and keeps going until the count is exhausted otherwise.

:::caution
Recovery Scenarios only run when the TestCase is executed from an **ExecutionList**. In the ScratchBook the scenario is ignored and the TestCase simply fails.
:::

:::tip
Changed a TestCase after adding it to an ExecutionList? Right-click the ExecutionList and choose **Synchronize** so the entry reflects the changes before you run it.
:::

The example uses a `WaitOn` inside the recovery, which is a workaround for a missing synchronisation step; in a real project you would also fix the TestCase. Recovery is for the failures you did not foresee. See [Action modes](/ToscaBase/test-cases/action-modes/) for `WaitOn`.

## Cleanup Scenarios

A Recovery Scenario changes the application state so that the retry can succeed. If the recovery itself fails, the application is stuck in a state from which every following TestStep would fail too. A **Cleanup Scenario**, also part of the recovery engine, runs when the recovery scenario has failed and holds the TestSteps that return the application to its original state, for example relaunch the application, log in and navigate back to the page where the next steps expect to be.

### Creating one

A Cleanup Scenario requires an existing Recovery Scenario Collection.

1. Right-click the `Recovery Scenarios` folder and choose **Create Cleanup Scenario** (**Ctrl+N**, **Ctrl+C**).
2. Add the cleanup TestSteps. In the example they are copies of the TestCase's own `Close URL` and `Open URL` steps.

### Worked example continued

The TestCase gains a further step: click an `Open new page` link that opens the same page in another tab. If `Submit` is still not enabled and the recovery fails, the link cannot be clicked either; reopening the page makes it clickable without going through the button. In the ExecutionList log:

1. `Submit enabled` fails.
2. The Recovery Scenario runs and fails as well.
3. The Cleanup Scenario runs: `Close URL`, `Open URL`.
4. Execution continues with the remaining TestSteps, which would have been blocked without cleanup.

## Related

- [Control flow](/ToscaBase/test-cases/control-flow/) when the situation is a known condition rather than a failure: an `If` is cheaper than a recovery.
- [Execution lists](/ToscaBase/execution/execution-lists/) and [Execution results and logs](/ToscaBase/execution/execution-results-and-logs/) for reading the recovery entries in the log.
