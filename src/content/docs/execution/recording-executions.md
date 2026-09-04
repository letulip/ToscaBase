---
title: Recording executions
description: Recording ScratchBook and ExecutionList runs as MP4 with the Execution Recorder setting, limiting it to failures, and excluding TestCases with the AvoidExecutionRecorder Test Configuration Parameter.
level: 2
sidebar:
  order: 50
sources:
  - id: piCdpKk86Zc
    title: "Tosca Tutorial | Lesson 70 - Record Test Executions and save it in MP4 format | Debug Errors |"
    url: https://www.youtube.com/watch?v=piCdpKk86Zc
    at: "00:08"
---

Tosca can record the whole screen while a TestCase runs and save the result as an MP4 file. This is aimed at runs nobody watches: remote or [distributed](/ToscaBase/execution/distributed-execution-dex/) executions and long TestCases where the log says *what* failed but not *why*. The recording shows the state of the application at the moment of failure without re-running the test.

:::note
The **Execution Recorder** exists in newer versions only; the speaker places it at Tosca 15.1 or later and demonstrates on Tosca 16. If the setting is missing, upgrade Commander.
:::

## Enabling the recorder

**Project > Settings > TBox > Execution Recorder**:

| Setting | Meaning |
|---|---|
| Enable Execution Recorder | Off by default. Choose between recording **all executions** or **only failed** executions |
| Output file name template | Default combines the TestCase name and the execution start time, `.mp4` |
| Output path | Default is the `Recordings` folder under the Tosca projects directory (`C:\Tosca_Projects\Tosca_Commander\Recordings` in the demo) |

Close the settings and every run, from the ScratchBook or from an ExecutionList, produces a file in that folder. Recording from an ExecutionList names the file after the list and TestCase, so ScratchBook and ExecutionList recordings of the same TestCase sit side by side.

Recording only on failure is the sensible default: it is the failing run you want to watch, and video takes real disk space.

:::caution
Pausing an execution does not pause the recording; it keeps recording until the run completes.
:::

## Excluding individual TestCases

With the recorder set to *all*, you can still opt specific TestCases out, for example stable ones or very long ones, without changing the project setting each time:

1. On the TestCase, its folder, or the project root, create a **Test Configuration Parameter**.
2. Name it `AvoidExecutionRecorder` and set the value to `True`.

Set it to `False` (or remove it) to record again. Because it is a Test Configuration Parameter it inherits down the folder tree, so a whole folder can be excluded with one parameter (see [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)).

## Managing the files

Recordings are plain MP4 files; there is no retention inside Tosca. Decide who deletes old recordings and when, or keep the recorder on *failures only*. For a still image instead of a video, use [Screenshots on failure](/ToscaBase/standard-modules/screenshots-on-failure/).
