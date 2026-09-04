---
title: Recovery and Cleanup Scenarios
description: How the Tosca recovery engine retries a failed TestCase - enabling recovery globally or per folder, creating a Recovery Scenario Collection, setting the Retry level, and adding a Cleanup Scenario for when the TestCase cannot be recovered.
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
  - id: DWTkzYY0G7A
    title: "TRICENTIS Tosca 16.0 - Lesson 20 | Recovery Scenarios | Recovery Scenarios TestCase &TestStep Level"
    url: https://www.youtube.com/watch?v=DWTkzYY0G7A
    at: "01:03"
  - id: fx3rD0s5DxM
    title: "TRICENTIS Tosca 16.0 - Lesson 21 | Cleanup Scenarios | Recovery Scenarios  | Execution List"
    url: https://www.youtube.com/watch?v=fx3rD0s5DxM
    at: "01:01"
---

Every automation tool has to deal with unexpected failures; in code you would write a try/catch block. Tosca ships a **recovery engine** instead: you define a collection of TestSteps called a **Recovery Scenario**, and when a TestCase fails Tosca runs those steps and then retries the failed part. If the recovery does not help, a **Cleanup Scenario** brings the application back to a known state so that the next TestCase can still run. Together they keep a long execution from stopping at the first surprise; you look at the failures afterwards instead of losing the whole run.

## Configuring recovery in three steps

1. **Enable recovery**, either for the whole workspace in the settings or for a folder through Test Configuration Parameters.
2. **Create the Recovery Scenario** in a Recovery Scenario Collection, which can sit anywhere in the TestCases section: on a folder or on a single TestCase.
3. **Set the Retry level** property of the scenario so that Tosca knows at which failure it should kick in.

All three are required.

### Step 1a: enable globally

**Project > Settings > TBox > Recovery** lists three failure types, each with the same four possible values:

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

Choose **Recover** for each failure type you want Recovery Scenarios to handle. Three more settings in the same dialog cap the number of attempts: **TestCase retries**, **TestStep retries** and **TestStepValue retries**, the maximum number of recovery attempts per TestCase, TestStep and TestStepValue respectively. Any values are allowed; they can differ. Close the dialog and recovery is enabled for every object in the workspace.

### Step 1b: enable per folder

If different folders need different behaviour, set the same options as Test Configuration Parameters on a TestCase folder; they override the global settings for that folder.

1. Select the folder and open its **Test Configuration** tab.
2. **Create Test Configuration Parameter**, choose `On dialog failure`, set it to `Recover`. Repeat for `On exception failure` and `On verification failure`.
3. Add `TestCase retries`, `TestStep retries` and `TestStepValue retries` with the counts you want (the source uses 1, 2 and 2).

See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/) for the mechanism.

### Step 2: create the Recovery Scenario

1. Right-click the TestCase folder (or TestCase) and choose **Create Recovery Scenario Collection** (**Ctrl+N**, **Ctrl+R**). Tosca adds a folder `Recovery Scenarios` (white plus icon).
2. Right-click that folder and choose **Create Recovery Scenario** (red plus icon). A collection can hold several scenarios: if the first one fails, Tosca moves on to the next scenario in the collection.
3. Add the TestSteps that should run when recovery is triggered, exactly as in a normal TestCase.

### Step 3: set the Retry level

Open the Recovery Scenario's properties and set **Retry level** to `TestCase`, `TestStep` or `TestStepValue`. This decides what Tosca re-runs after a successful recovery: the whole TestCase, the failed TestStep, or the failed TestStepValue. Both sources keep `TestCase`.

## Worked examples

**A button that is not ready.** A `Submit` button is disabled for about 13 seconds after load. The TestCase is: `OpenUrl`; on `Submit`, `Verify` `Enabled == True` then click `X`; close the page. It fails at the verification. The Recovery Scenario contains a single TestStep on the same button with ActionMode `WaitOn` and value `Enabled == True`; Retry level `TestCase`, TestCase retries 1. Running the folder from an ExecutionList gives this log:

1. `Submit enabled` verification fails.
2. The recovery engine starts the Recovery Scenario; the `WaitOn` waits until the button is enabled.
3. The TestCase is executed again: the verification now passes, the click happens, the TestCase passes.

With retries set to 1 there is one attempt. If a scenario needs more, raise `TestCase retries`; Tosca stops retrying as soon as the TestCase passes and keeps going until the count is exhausted otherwise.

**A leftover session.** Lesson 20's login-and-logout TestCase fails when the browser is already logged in from a previous run: the `Login` link cannot be found. The Recovery Scenario, on the same top-menu Module, clicks `Logout` (`X`), waits with `WaitOn` `Visible == True` for `Login` to reappear, and closes the browser (`Close Browser`, title `Demo*`). From the ExecutionList the log shows the failure, the recovery logging out and closing the window, and the retried TestCase opening a fresh browser and passing.

:::caution
Recovery and Cleanup Scenarios only run when the TestCase is executed from an **ExecutionList**. In the ScratchBook they are ignored and the TestCase simply fails.
:::

:::tip
Edits inside a TestCase reach its ExecutionList entry automatically; **Synchronize** (right-click the ExecutionList) is only needed after structural changes such as moved folders or new TestCases. See [ExecutionLists](/ToscaBase/execution/execution-lists/).
:::

Both examples use a `WaitOn` inside the recovery, which patches a missing synchronisation or precondition step; in a real project you would also fix the TestCase. Recovery is for the failures you did not foresee. See [ActionModes](/ToscaBase/test-cases/action-modes/) for `WaitOn`.

## Cleanup Scenarios

A Recovery Scenario changes the application state so that the retry can succeed. When the TestCase cannot be recovered, because the recovery failed or because the collection holds no Recovery Scenario at all, the application is left in a state from which the next TestCase would fail too. A **Cleanup Scenario**, also part of the recovery engine and stored in the same collection, then runs the TestSteps that reset the application: relaunch it, empty what the failed run left behind, log out, so that the environment is ready for the next TestCase.

### Creating one

A Cleanup Scenario requires an existing Recovery Scenario Collection; it does not require a Recovery Scenario in it.

1. Right-click the `Recovery Scenarios` folder and choose **Create Cleanup Scenario** (**Ctrl+N**, **Ctrl+C**).
2. Add the cleanup TestSteps. They can be copies of the TestCase's own steps (`Close URL` and `Open URL` in Lesson 50), or an existing TestCase dragged into the scenario, as Lesson 21 does with its empty-the-cart TestCase.

### Worked examples

**Recovery failed.** The `Submit` TestCase gains a step that clicks an `Open new page` link. If `Submit` is still not enabled and the recovery fails, the link cannot be clicked either; the Cleanup Scenario reopens the page. In the ExecutionList log: the verification fails, the Recovery Scenario runs and fails, the Cleanup Scenario runs `Close URL` and `Open URL`, and execution continues with the remaining TestSteps.

**No recovery, just cleanup.** Lesson 21's checkout TestCase is made to fail by not accepting the terms of service, so the shop shows an error and the TestCase stops with ten pairs of jeans in the cart and the session logged in; the next TestCase would start in that state. The collection on the TestCase holds only a Cleanup Scenario, built from the cart-emptying `While` loop in [Control flow](/ToscaBase/test-cases/control-flow/) plus `Logout` and `Close Browser`. In the ExecutionList log the TestCase fails, the Cleanup Scenario empties the cart, logs out and closes the browser, and the environment is ready for the next run.

## Related

- [Control flow](/ToscaBase/test-cases/control-flow/) when the situation is a known condition rather than a failure: an `If` is cheaper than a recovery.
- [Execution lists](/ToscaBase/execution/execution-lists/) and [Execution results and logs](/ToscaBase/execution/execution-results-and-logs/) for reading the recovery entries in the log.
