---
title: Execution
description: Running TestCases through ExecutionLists, reading and archiving results, manual and recorded runs, scheduling, CI integration and distributed execution on DEX agents.
level: 2
sidebar:
  order: 0
---

The **Execution** section of the workspace is where finished TestCases are run and where their results live. This section starts with the basic unit, the ExecutionList, then covers what to do with results, the variants of a run (manual, repeated, recorded, documented, multi-browser), and finally how to take the run out of Commander: on a schedule, from a CI server, or across DEX agents.

| Doc | What it covers |
|---|---|
| [ExecutionLists](/ToscaBase/execution/execution-lists/) | ScratchBook versus ExecutionList, creating and running lists, synchronising with TestCases |
| [Results and logs](/ToscaBase/execution/execution-results-and-logs/) | ActualLog view options, trend charts, clear and archive, copy to Excel, LogViewer |
| [Manual execution](/ToscaBase/execution/manual-execution/) | Run as manual TestCase with the checklist window, set a result by hand |
| [Repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/) | Repetitions on an execution entry, business TestCases and business ExecutionLists |
| [Recording executions](/ToscaBase/execution/recording-executions/) | Execution Recorder MP4 setting, AvoidExecutionRecorder parameter |
| [DokuSnapper](/ToscaBase/execution/dokusnapper/) | A generated document with log and screenshot per TestStep |
| [Cross-browser execution](/ToscaBase/execution/cross-browser-execution/) | Browser parameter from a Buffer, "No feasible executor found" |
| [Scheduling executions](/ToscaBase/execution/scheduling-executions/) | TCShell script, batch file, Windows Task Scheduler |
| [Jenkins integration](/ToscaBase/execution/ci-integration-jenkins/) | Freestyle job that runs the TCShell batch file |
| [Distributed execution (DEX)](/ToscaBase/execution/distributed-execution-dex/) | AOS workspace, DEX agent, Configurations, TestEvents |
| [Tosca Execution Client](/ToscaBase/execution/tosca-execution-client/) | Triggering TestEvents from PowerShell, shell or Jenkins |

Read the first two before anything else; every later doc assumes you can create a list and read its log. Recovery and Cleanup Scenarios that react to failures during a run are in [Test cases](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/).
