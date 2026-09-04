---
title: Cross-browser execution
description: Running the same TestCase in several browsers by feeding the Browser Test Configuration Parameter from a Buffer, and fixing the "No feasible executor found" error caused by a TestStep without a Module.
level: 2
sidebar:
  order: 70
sources:
  - id: 8tXcwf0qLx8
    title: "Tosca Tutorial | Lesson 144 - Common Problems & Fixes | Cross Browser Testing | Multiple Browsers |"
    url: https://www.youtube.com/watch?v=8tXcwf0qLx8
    at: "00:12"
  - id: h8u3f4AU4_I
    title: "Tosca Tutorial | Lesson 143 - Common Problems & Fixes | No Feasible Executor Found | Execution |"
    url: https://www.youtube.com/watch?v=h8u3f4AU4_I
    at: "00:12"
---

Which browser a web TestCase runs in is decided by the `Browser` Test Configuration Parameter, one value per run. That answers "run on Chrome today, Firefox tomorrow", but not "run this TestCase on Chrome *and* Edge in the same execution", which is both a common project requirement and a popular interview question. The trick is to make the parameter dynamic. The second half of this doc covers an execution error that looks like a browser or agent problem but is not.

## One browser per run

On the TestCase or ExecutionList, open **Test Configuration** and add the Test Configuration Parameter `Browser`; pick the browser from its list (Chrome, Firefox, Edge...). Change the value before each run to switch browser. Details of the parameter mechanism are in [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## Several browsers in one TestCase

Instead of a constant, give `Browser` a **Buffer reference**, then set that Buffer from inside the TestCase before each part that must run in a different browser.

1. Structure the TestCase into one folder per browser run. In the demo the `Login process` folder (Open URL, Close Browser) is copied so there are two: `Login process 1` and `Login process 2`; Close Browser is removed from the first one.
2. In **Test Configuration** of the TestCase, set `Browser` to a Buffer reference; the demo uses `{B[B_browser]}` for a Buffer named `B_browser`.
3. As the **first TestStep** of each folder add **TBox Set Buffer** (see [Buffer operations](/ToscaBase/standard-modules/buffer-operations/)): Buffer name `B_browser`, value `Chrome` in the first folder, `Edge` in the second.
4. Run. The log shows the Buffer being set to `Chrome`, the URL opening in Chrome, then the Buffer set to `Edge` and the URL opening in Edge; the Close Browser step closes the browser that the current folder opened.

Because the browser is read from the Buffer at the time each Open URL runs, one TestCase covers as many browsers as you have Set Buffer steps. No duplicate TestCases per browser and no distributed execution are needed for this.

The Buffer name is your choice; it only has to match between the Set Buffer step and the `{B[...]}` reference.

If the first folder does not close its browser, that browser stays open after the run, which is what the demo shows for Chrome.

## "Unable to run the selected items. No feasible executor was found"

This error appears when starting a TestCase, an ExecutionList, or a TestEvent. It is easy to misread as a problem with the execution environment, particularly for a TestEvent, where it suggests the DEX agent is broken. The usual cause is much simpler: **a TestStep no longer references a Module**.

Sometimes the message includes the reason ("this TestStep is not referencing a Module"); sometimes only the first line is shown.

### How it happens

Open the TestCase and look at the failing TestStep: the values are still there, but no ModuleAttribute is associated and **Jump to Module** is not offered. The Module that the step was built from was deleted, replaced or renamed in the workspace. In a multi-user workspace this is typically someone cleaning up Modules; Tosca warns on deletion that the Module is used by a TestStep, but the deletion can still go ahead. Standard modules such as Open URL and Close Browser cannot be deleted, so the culprit is an application Module.

One orphaned step is enough to prevent the whole TestCase from running, even though every other step is fine.

### Fix

1. Delete the orphaned TestStep. The TestCase (and the ExecutionList or TestEvent containing it) runs again immediately.
2. To restore the coverage, rescan the application, recreate the Module, and add the TestStep back.

See [Module hygiene](/ToscaBase/best-practices/module-hygiene/) for how to clean up Modules without breaking TestCases, and [Rescan Modules](/ToscaBase/modules/rescan-modules/) for the rescan.
