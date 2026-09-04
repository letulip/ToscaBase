---
title: Command-line tools
description: Steer Tosca Commander from the command line with TCShell in interactive or script mode to execute ExecutionLists and check in, and clone a workspace for every team member with TCWorkspaceUtil instead of copying it.
level: 4
sidebar:
  order: 70
sources:
  - id: OoIOA5VMnI8
    title: "Tosca Tutorial | Lesson 78 - Steer Tosca Commander using Command Line | TCShell |"
    url: https://www.youtube.com/watch?v=OoIOA5VMnI8
    at: "00:02"
  - id: us-zGUBdgwU
    title: "Tosca Tutorial | Lesson 94 - Clone Workspaces using Command Line Tool | TCWorkspaceUtil |"
    url: https://www.youtube.com/watch?v=us-zGUBdgwU
    at: "00:08"
---

Two executables in the Tosca Commander installation folder do administrative work without the Commander UI. **TCShell** opens a workspace from a command prompt and runs commands against it: execute an ExecutionList, save results, check in. It is the basis of every CI integration (see [CI integration with Jenkins](/ToscaBase/execution/ci-integration-jenkins/)). **TCWorkspaceUtil** clones a workspace so that each team member gets a valid copy connected to the shared repository.

Both live in the Commander installation directory, `C:\Program Files\Tricentis\Tosca Commander` by default. The environment variable `%COMMANDER_HOME%` points there; typing it into File Explorer's address bar opens the folder.

## TCShell

TCShell is installed with Commander; nothing needs to be set up. It takes the workspace to open and, for a multi-user workspace, the login credentials:

| Parameter | Value |
|---|---|
| workspace | Full path to the workspace file, up to and including the `.tws` file |
| login | User name and password. Not needed for a single-user workspace; required in a multi-user workspace |
| script | Path to a `.tcs` script file (script mode only) |

:::note
The exact switch spelling is only shown on screen, never spoken. Run `help` inside TCShell (or read the Commander documentation) for the precise syntax before writing a batch file.
:::

### Interactive mode

Start TCShell with the workspace parameter. It checks the licence and logs in to the workspace; when the prompt appears you are connected. Type `help` to list the available commands. The ones the source highlights:

| Command | Purpose |
|---|---|
| compact workspace | Compacts the workspace for performance |
| change node, jump to node | Navigate to an object by its path in the project tree |
| call script | Run a `.tcs` script |
| get option, set option, save options | Read and change options |
| set property | Change a property of the current object |
| health check | Background check of the workspace |
| task | Run a task on the current object, such as executing an ExecutionList; also check in all |

Interactive mode asks questions where needed: how to exit, whether to proceed when the workspace is locked. Exit with the exit command when done.

:::caution
A single-user workspace cannot be open in Commander and in TCShell at the same time. TCShell reports it is blocked by another process and asks whether to continue; close the workspace in Commander first. A multi-user workspace with separate workspaces per client does not have this limit.
:::

### Script mode

Prepare the commands once in a `.tcs` file and pass its path as the script parameter; TCShell runs it without prompting. The script in the source has four lines:

1. Jump to node with the path of the ExecutionList, starting at the project root: `Project / Execution / ExecutionLists / PDF compare`.
2. Task: clear the execution log.
3. Task: run the ExecutionList.
4. Task: save the results.

When the run finishes TCShell prints each step and "run finished"; the results are posted back to the workspace, so the ExecutionList in Commander shows the new start timestamp and result (failed in the source, as expected for a PDF comparison that differs). Execution from the command line is faster than from the UI and is the only way to trigger Tosca from a CI/CD tool such as Jenkins or from a scheduler. If a batch file also needs to close Commander afterwards, see the `taskkill` note in [Start and close programs](/ToscaBase/standard-modules/start-and-close-programs/).

## TCWorkspaceUtil: cloning workspaces

### Why copying a workspace fails

Every workspace has a unique ID created with it. A workspace folder copied to another machine keeps that ID, so two Commander processes end up accessing "the same" workspace and it locks. Team members therefore need clones, not copies.

### Cloning

The tool is `TCWorkspaceCloneUtil.exe` in `%COMMANDER_HOME%`. It cannot be started by double-click; run it from a command prompt or a batch file with three parameters:

| Parameter | Value |
|---|---|
| `-workspace` | Full path of the workspace to clone |
| `-out` | Output folder that will receive the clones |
| `-count` | Number of clones to create (5 in the source; any number) |

The batch file in the source has two lines: change directory to `%COMMANDER_HOME%`, then call the executable with the three parameters. Running it creates one subfolder per clone in the output folder; each is a complete workspace with its own ID. Copy one to each tester's machine. All clones stay connected to the same repository, so everybody checks in and out against the same data.

:::note
The video title calls the tool TCWorkspaceUtil; the speaker and the file name he searches for say TCWorkspaceCloneUtil. Search the installation folder for "WorkspaceCloneUtil".
:::

## Related

- [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/): the repository the clones share.
- [Scheduling executions](/ToscaBase/execution/scheduling-executions/) and [Distributed execution](/ToscaBase/execution/distributed-execution-dex/): other ways to run without the UI.
