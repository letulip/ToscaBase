---
title: DokuSnapper
description: Enabling DokuSnapper so every ExecutionList or ScratchBook run produces a document with the log and a screenshot per TestStep.
level: 2
sidebar:
  order: 60
sources:
  - id: mFptsa3Wuts
    title: "Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper"
    url: https://www.youtube.com/watch?v=mFptsa3Wuts
    at: "04:24"
---

**DokuSnapper** is an optional feature that makes Tosca write a document for each executed TestCase, containing the execution log and a screenshot of every TestStep. It is proof of execution for audits or stakeholders who do not open Commander. Enabling it is a project setting; nothing changes in the TestCases.

## Enabling DokuSnapper

1. **Project > Settings** opens the settings wizard.
2. In the left tree, expand the engine node under **Settings**, select **DokuSnapper** and set **Enable Snapper** to `Yes`.
3. Adjust the other DokuSnapper options, including the document paths, if needed.
4. Close the wizard.

:::note
The tree path is only read out ("engine and DokuSnapper, under Settings"); the exact label of the engine node is not shown.
:::

## What is generated

From now on every execution, from an [ExecutionList](/ToscaBase/execution/execution-lists/) or the ScratchBook, produces a document named after the TestCase. Documents from ScratchBook runs are prefixed with `ScratchBook`. The document contains the execution log and one screenshot per TestStep.

The default location shown in the video is under the user's AppData folder: `AppData\...\Tricentis\Tosca TestSuite\7.0.0\DokuSnapper` (the version segment depends on the installation). Change it in the DokuSnapper settings if a shared location is required.

## Typical workflow

1. Enable DokuSnapper once, as above.
2. Check out the ExecutionList, right-click the entries or the whole list > **Run**.
3. Check in to store the results in the shared repository.
4. Open the DokuSnapper folder and find the document named after the TestCase: it contains the execution log and one screenshot per TestStep, which is the proof of execution you can attach to a release or an audit request.

The document is generated for both passed and failed runs, so it is also a quick way to see what the screen looked like at a failing step without re-running the TestCase.

## Related

- [Recording executions](/ToscaBase/execution/recording-executions/) for a video instead of a document.
- [Screenshots on failure](/ToscaBase/standard-modules/screenshots-on-failure/) for screenshots only where the run fails.
