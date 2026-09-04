---
title: Screenshots on failure
description: Take a screenshot at any TestStep with TBox Take Screenshot, and let Tosca capture one automatically on every failed verification through the project settings.
level: 2
sidebar:
  order: 50
sources:
  - id: w3k8DuVFNBU
    title: "Tosca Tutorial | Lesson 17 - Automatically take Screenshot on Failures | TBox Automation Module |"
    url: https://www.youtube.com/watch?v=w3k8DuVFNBU
    at: "00:10"
---

There are two ways to get screenshots out of a Tosca run. The **TBox Take Screenshot** Module captures the screen at whatever point in the TestCase you place it. A **project setting** captures a screenshot automatically whenever a TestStep fails, without touching any TestCase. Use them together: the Module for screenshots a requirement asks for, the setting for debugging failures.

The example TestCase logs in to a demo web shop with deliberately invalid credentials, so it fails at the login verification.

## TBox Take Screenshot

Search **Add TestStep** for `TBox Take Screenshot`.

| ModuleAttribute | Value |
|---|---|
| Environment | `Desktop` or `Mobile` |
| Directory | Folder where the image is saved |
| File name | Name of the image file |

After the run, the step's **Details** in the ScratchBook show where the file was written, and the log info states that the screenshot was created.

### Unique file names

A fixed name such as `Screenshot1` is overwritten on every execution. To keep one image per run, append a dynamic **date/time expression** to the file name (see [Date expressions](/ToscaBase/expressions/date-expressions/)). The name then carries the date and time down to seconds and is unique every time.

### Where to put the step

A screenshot step placed **after** the step that fails is never executed, because the TestCase stops at the failure. Place it before the risky step (in the example: after clicking Login but before the login verification). You can add as many screenshot steps as you like at different points.

## Automatic screenshots on failed TestSteps

Set it once per project in **Project settings > TBox > Logging > Screenshots**:

| Setting | Recommended value |
|---|---|
| Make screenshot on failed TestSteps | On (off by default) |
| On which failure | `Verification failure`. The other choice is detection failure; verification failures are where tests usually fail and where you need to see the state |
| Screenshot directory | Any folder, for example the same one used by the Module |
| Image format | `PNG` (several formats are offered) |

The setting applies to every TestCase in the project.

### Viewing the screenshot

:::caution
The ScratchBook cannot display the automatic screenshot. Its Details pane only shows a `System.Drawing.Bitmap` entry. Run the TestCase from an **ExecutionList** to see the image.
:::

1. Drag the TestCase into an ExecutionList and execute it.
2. Open the failed TestStep in the results. Its **Details** section shows both the screenshot taken by the Module and the one captured automatically at the failed verification.
3. In the example the image shows the web shop's "login unsuccessful" message, which is exactly what is needed to diagnose the failure.

:::tip
Do not switch windows or close the browser while the execution is still running; the screenshot is taken at the moment of failure and will show whatever is on screen. Look at the results only after the execution has finished.
:::

## Related

- [Execution results and logs](/ToscaBase/execution/execution-results-and-logs/)
- [DokuSnapper](/ToscaBase/execution/dokusnapper/) for step-by-step documentation of a run
