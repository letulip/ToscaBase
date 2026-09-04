---
title: Jenkins integration
description: Running Tosca Commander tasks from a Jenkins freestyle job by executing a Windows batch file that calls TCShell with a .tcs script.
level: 2
sidebar:
  order: 90
sources:
  - id: GFVCsjV-8_w
    title: "Tosca Tutorial | Lesson 89 - Run Tosca Commander Tasks from Jenkins | CI/CD | DevOps |"
    url: https://www.youtube.com/watch?v=GFVCsjV-8_w
    at: "00:03"
---

TCShell lets you execute an ExecutionList from a command prompt without opening Commander (see [Command-line tools](/ToscaBase/administration/command-line-tools/)). Typing that command is still a manual step. Wrapping it in a **Jenkins** job turns it into a button, a schedule, or a trigger on a code change, which is what a CI/CD pipeline needs. This doc covers the TCShell route; the newer alternative for [distributed execution](/ToscaBase/execution/distributed-execution-dex/) is the [Tosca Execution Client](/ToscaBase/execution/tosca-execution-client/).

## Prerequisite: a batch file

Jenkins cannot execute a `.tcs` script directly, so it needs a Windows batch file that calls TCShell. The demo's `execute.bat` contains the same two commands used from the command prompt:

1. `cd` to the Commander home folder.
2. The TCShell command that calls `script.tcs`.

The `.tcs` script holds the Commander tasks (jump to an ExecutionList, run it, save), so the batch file never changes: to do something else, change the script. Create the batch file in Notepad and save it as `.bat`.

## Creating the Jenkins job

The demo uses a local Jenkins instance; on a server instance the steps are the same, possibly with more configuration.

1. **New Item**, choose **Freestyle project** (a Pipeline works too), name it, for example `Tosca_Execute_CI`, and click **OK**.
2. Skip the optional sections (description, discard old builds, source code management, build triggers) unless you need them. Build triggers are where a periodic schedule or SCM polling would go.
3. Under **Build**, click **Add build step > Execute Windows batch command**.
4. Enter two lines: `cd` to the directory containing the batch file, then `execute.bat`.
5. **Save**.

Click **Build Now**. The **Console Output** shows the same output as the command prompt: TCShell logs in to the workspace, runs the tasks in the script, and the build ends **SUCCESS**.

:::caution
Close the workspace in Commander before building. Commander itself may stay open, but if the workspace is logged in, TCShell cannot log in and the build misbehaves.
:::

## Where this fits

Whatever the script can do in Commander, the job can do: run tests, or any other TCShell task. Scheduling the job from Jenkins is the CI equivalent of [scheduling with Windows Task Scheduler](/ToscaBase/execution/scheduling-executions/).
