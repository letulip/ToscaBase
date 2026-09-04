---
title: "Distributed execution (DEX)"
description: "Setting up Tosca distributed execution with AOS: the AOS workspace, the DEX agent, Commander settings, Configurations, TestEvents, and matching agents to configurations."
level: 2
sidebar:
  order: 100
sources:
  - id: -hceXOD_WB4
    title: "Tosca Tutorial | Lesson 152 - Tosca Distributed Execution Setup with AOS | DEX Agents| Test Events |"
    url: https://www.youtube.com/watch?v=-hceXOD_WB4
    at: "00:03"
---

**Distributed execution (DEX)** runs ExecutionLists on other machines, called **DEX agents**, and in parallel. You trigger a **TestEvent** from Commander, Tosca Server distributes it to an agent, and the results come back into the repository. The setup has several parts; this doc walks through them in the order they have to be done. It assumes Tosca Server is installed with the **Automation Object Service (AOS)** and the **Distribution Service** running (see [Tosca Server](/ToscaBase/administration/tosca-server/)).

## Architecture

- **Commander** (your workspace) creates and triggers TestEvents.
- **Tosca Server** hosts the **AOS** and the **DEX server**. The AOS has its own workspace and is the middleman: it fetches the automation objects and test data the event needs from the common repository and hands them to the DEX server, which distributes the work to agents. When agents finish, results go back through the AOS into the repository.
- **DEX agents** are machines running the agent process (with or without a full Commander) that execute the tests.

:::caution
DEX works only with **multi-user workspaces**. The AOS workspace and your working workspace must be on the **same repository**. The demo uses SQLite on one machine; production needs Oracle, SQL Server or DB2 and separate machines (see [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/)).
:::

## Step 1: the AOS workspace

On the machine running Tosca Server, create a dedicated workspace for the AOS:

1. **Create new** workspace, choose the **existing repository** your multi-user workspace uses (do not create a new one), branch `master`, and a distinct name such as `multi-aos`.
2. Do **not** create a slim workspace; the AOS does not work with one.
3. Creation can take long on a big repository because all objects are updated.
4. Log in once to verify the project root name and that the objects are the same as in your working workspace, then close it.

Never use this workspace for daily work; open it and DEX stops working.

## Step 2: register the workspace on the server

In the Tosca Server UI, **Settings > Automation Object Service > Add new**, enter the **project root name** (as shown in the workspace, `multi-demo` in the demo, not the workspace name), the **workspace name** (`multi-aos`), username and password. Up to **10** AOS workspaces can run in parallel, one per project. **Save** restarts the related services.

Then restart the DEX server: in Windows **Services**, find the Tricentis **Distributed Execution** service and restart it, plus the monitor service. The server dashboard should show everything running again.

## Step 3: the DEX agent

The agent executable ships with Commander at `...\Tricentis\Tosca Testsuite\Distributed Execution\DEXAgent.exe`. The installer also offers installing **only the DEX agent** instead of full Commander, which is lighter and the better choice for a dedicated execution machine. Run it as administrator.

A tray icon shows the state: **white** not running, **green** configured and connected, **yellow** executing, **red** misconfigured. Right-click it to **configure** or **stop** the agent. Configuration fields:

- Machine details (operating system, memory, OS type, IP address, host name), detected automatically and editable.
- No workspace is needed on the agent.
- **Connect to server**: the DEX server endpoint, `localhost:5007` in the demo. Verify it in the server UI under **Settings > Automation Object Service > Distribution server address**.
- **Authentication** if required.
- **RDP**: enable and enter username, password and desktop size when the agent runs on a remote machine, so mouse and keyboard actions work even when the session is locked. Without it, tests fail once the machine locks.
- **Logging**: set to `Debug`; the log file sits next to the executable.

Once green, the agent appears in the server's **DEX monitor > Agent view** in the idle state (other states: running, paused, stopped, error). From the monitor you can restart an agent and change its machine, RDP and logging configuration; the endpoint URL can only be changed on the agent itself.

## Step 4: connect Commander to the server

In your working workspace, **Project > Settings**:

- **Commander > Distributed Execution**: **Monitor URL** (`http://localhost:8080/monitor` in the demo, copy it from the server) and **Server** (the DistributionServerService/ManagerService endpoint; change only host and port).
- **Tricentis Services**: the server endpoint, host plus port (`localhost:8080`).

Close the dialog to save.

## Step 5: Configurations

In the Execution section, the **Configurations** folder holds three defaults: `Any` (every agent), `RDP` (`UseRDP` = true) and `SupportsClassic` (classic Modules). Right-click **Configurations > Refresh agents**: each agent is listed under every configuration whose properties it matches, so the new agent shows under `Any`. The number of agents per configuration is what a TestEvent will use.

## Step 6: TestEvents

**TestEvents** exist only in multi-user workspaces, under the Execution folder. A TestEvent needs a **configuration** and an **ExecutionList**:

1. Check out the TestEvents folder and create a TestEvent (`dex event`).
2. Drag a configuration onto it (`Any` lets the server pick a free agent; a specific configuration pins the agent type).
3. Drag the ExecutionList to run onto it. Test mandates or other execution objects can be added the same way.
4. **Check in everything**: the TestEvent, the ExecutionList and its TestCases.
5. Right-click the TestEvent > **Execute now**.

The TestEvent appears in the monitor's **Event view** with status, start time and creator; open it for details. The agent view shows the agent executing, then idle again.

:::caution
A checked-out TestEvent or ExecutionList makes the event fail with **cancelled** and "failed to retrieve the needed automation objects". Check in first.
:::

## Custom configurations

The properties a configuration can have come from `ConfigurationParameters.xml` under the Tosca Server installation (`...\Tosca Server\DEX Server\` in the demo): operating systems, memory sizes, OS types, `UseRDP`, `SupportsClassic`, IP address. Edit it as administrator, for example adding `Windows 11` to the operating systems or a `Browser` parameter with values, and save. Then in Commander:

1. Check out the project root, right-click **Configurations > Update configurations from server** (fails without the checked-out root).
2. Create a new configuration (`local`) and set its properties: OS `Windows 11`, memory `16 GB`, type `64bit`.
3. On the agent, set the **same** values in its configuration.
4. Check in all and **Refresh agents**; the agent now appears under `local`.
5. Replace `Any` in the TestEvent with `local` to run only on matching agents.

Configuration, agent properties and the XML must agree; that is the whole matching rule.

## Triggering from outside Commander

TestEvents can be started from a CI pipeline with the [Tosca Execution Client](/ToscaBase/execution/tosca-execution-client/).
