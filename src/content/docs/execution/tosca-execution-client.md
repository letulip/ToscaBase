---
title: Tosca Execution Client
description: Triggering DEX TestEvents from the command line or a CI/CD pipeline with the Tosca Execution Client PowerShell/shell script, and calling it from Jenkins.
level: 2
sidebar:
  order: 110
sources:
  - id: e5hbUh6SM08
    title: "Tosca Tutorial | Lesson 153 - Tosca Execution Client | Script Based CI/CD Integration | Powershell |"
    url: https://www.youtube.com/watch?v=e5hbUh6SM08
    at: "00:03"
---

The **Tosca Execution Client** is a command-line tool, introduced with Tosca 15.2, that triggers **TestEvents** on Tosca Server from any CI/CD system (Jenkins, GitLab, anything that can run a script). It requires [distributed execution with AOS](/ToscaBase/execution/distributed-execution-dex/); the events, configurations and agents are set up there, the client only starts them and collects results. Compared with the [TCShell and Jenkins](/ToscaBase/execution/ci-integration-jenkins/) route it needs no Commander on the build machine and runs on Windows or Linux.

## Download and prerequisites

- Source: the GitHub repository `tricentis/tosca-execution-client` (search "Tosca execution client"). Download the `main` branch as ZIP and extract it to a folder such as `C:\execution\tosca-execution-client`. It contains a README and the client: a **PowerShell** script for Windows and a **shell** script for Linux.
- Supported from Tosca **15.2** upwards.
- On Windows, PowerShell's execution policy blocks scripts by default (`Undefined`). In PowerShell run `Set-ExecutionPolicy Bypass -Scope LocalMachine` and confirm the security prompt. Linux has its own configuration, described in the README.

## Parameters

Mandatory:

| Parameter | Value |
|---|---|
| Tosca server URL | For example `http://localhost:80`, or the server IP with port |
| Project name | The **project root name** of the project containing the TestEvent |
| Events | JSON array of TestEvent names to run, or |
| Events config file path | Path to a JSON file with the event configuration |

Optional: CA certificate, client ID and client secret (HTTPS only), client timeout, execution environment, execution ID, polling interval, request timeout, retries and retry delay, results file name and folder (default: next to the script), deactivating logging, log folder path.

## Running from PowerShell

1. `cd` to the client folder; running the script from elsewhere fails as not executable.
2. Run the command from the README with your values: the PowerShell script name, the server URL, the events (`sample` in the demo, a TestEvent with a DEX configuration and a login ExecutionList) and the project name (`multi-user`).

The output shows the event being **enqueued**, started, and completed; the test runs on the agent (the demo's login on the same machine), and the TestEvent shows up as executed in Commander and the DEX monitor. Two outputs land in the client folder: a `logs` folder for debugging, and a **results XML** with suite name, test counts, failures and timings. It is JUnit-style, so any CI reporting plugin can render it.

## Running from Jenkins

1. Install the **PowerShell** plugin if the build step is missing: **Manage Jenkins > Plugins > Available plugins**, search `PowerShell`, install.
2. **New Item > Freestyle project**, name it (`execution client`), **OK**.
3. **Build > Add build step > PowerShell**, enter two lines: `cd` to the client folder, then the same execution command as above. **Save**.
4. **Build Now**. The **Console Output** shows the same enqueue/start/complete log, the test runs on the agent, and the build finishes **SUCCESS** with the results written to the XML file.

Add an XML or other reporting plugin for a readable report inside the build. Hooking the job to the team's pipeline means every code change can trigger the TestEvents automatically.
