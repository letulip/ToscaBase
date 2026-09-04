---
title: Scheduling executions
description: Unattended runs without a CI server, by triggering a TCShell script through a batch file from Windows Task Scheduler.
level: 2
sidebar:
  order: 80
sources:
  - id: EWJxuLJyJWU
    title: "Tosca Tutorial| Lesson 141 - Common RealTime Tosca Problems & Fixes | Schedule Automated Executions|"
    url: https://www.youtube.com/watch?v=EWJxuLJyJWU
    at: "00:12"
---

Automated tests that someone has to start by hand every day waste the automation. Every project should have **unattended execution**: a schedule that runs the ExecutionLists without a person at the desk. The usual answer is a CI/CD tool ([Jenkins](/ToscaBase/execution/ci-integration-jenkins/)), but when no CI tool is available, **Windows Task Scheduler** can start a TCShell script on any schedule.

The building blocks are the same as for the Jenkins integration: a `.tcs` script that tells Commander what to do, and a `.bat` file that calls TCShell with that script. Task Scheduler only replaces the trigger.

## The TCShell script

TCShell is Tosca's command-line tool for driving Commander without opening it; its commands are covered in [Command-line tools](/ToscaBase/administration/command-line-tools/). The script in the demo (`script.tcs`) does four things:

1. `jumptonode` to the ExecutionList to run, by its path in the Execution section (Execution folder > ExecutionList folder > `Swag Labs` > `Run login`).
2. A task that **clears the log**.
3. A task that **runs** the ExecutionList.
4. A task that **saves** the results.

## The batch file

The batch file (`execute.bat` in the demo) contains two commands:

1. `cd` into the Commander home directory.
2. The TCShell command with the workspace file path, the login credentials (empty for a local workspace) and the script path as parameter, for example `C:\training\tcshell_script.tcs`.

Create it in Notepad and save with the `.bat` extension.

## Creating the scheduled task

1. Open **Task Scheduler**, go to **Task Scheduler Library**, and click **Create Task** in the **Actions** pane.
2. **General**: enter a name (`Tosca executions`) and description; tick **Run with highest privileges**.
3. **Triggers > New**: keep **On a schedule**; choose **One time** for a first test (the demo sets a time two minutes ahead), or **Daily**/**Weekly** for real use. Advanced settings allow a random delay, repeating the task every hour for a duration, and an expiry.
4. **Actions > New**: action **Start a program**, browse to the `.bat` file.
5. Confirm. The task appears in the library with status **Ready**, its last trigger time and the **next run time**. Right-click > **Run** starts it immediately without waiting.

At the scheduled time a command prompt opens on its own, runs the batch commands, executes the ExecutionList and finishes the task.

:::caution
The workspace must be **closed** in Commander when the task fires. TCShell logs in to the workspace, and a workspace that is open locally cannot be logged in to a second time; the run simply waits. The demo hits exactly this: the first trigger stalls until the workspace is closed, and the trigger has to be re-edited to fire again.
:::

## Related

- [Jenkins integration](/ToscaBase/execution/ci-integration-jenkins/) uses the same script and batch file behind a CI build.
- [Distributed execution](/ToscaBase/execution/distributed-execution-dex/) for running TestEvents on remote agents instead of the local machine.
