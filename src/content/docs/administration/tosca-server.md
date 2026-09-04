---
title: Tosca Server
description: What Tosca Server is in the Tosca architecture, how to download and install it with matching Commander version, which services it runs, how to restart them, and what the dashboard and DEX monitor show.
level: 4
sidebar:
  order: 80
sources:
  - id: btvqHGsOLMo
    title: "Tosca Tutorial | Lesson 151 - Tosca Server Setup, Features & Architecture"
    url: https://www.youtube.com/watch?v=btvqHGsOLMo
    at: "00:04"
---

Tosca Server is the central component that Tosca Commander installations, DEX agents and the CI client talk to. It bundles a set of Windows services (REST API, file service, DEX server and monitor, Automation Object Service, license administration, authentication and others) behind one web dashboard. You need it as soon as you want [distributed execution](/ToscaBase/execution/distributed-execution-dex/), [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/) or central licence and user administration. This doc covers the architecture, installation and service maintenance; DEX configuration is in the execution section.

## Architecture

The architecture diagram in the source places Tosca Server in the middle, connected to:

- the **database tier** (the common repository);
- **Tosca Commander** installations;
- **DEX agents**, which receive test events from the DEX server;
- the **Tosca CI client**, used to build CI/CD pipelines;
- the **licence tier**.

Services running inside Tosca Server, as named in the source: REST API service, file service, DEX monitor, DEX server, Automation Object Service (AOS), license administration, authentication service, gateway, and Test Data Services (TDS).

## Sizing and placement

Tosca Server runs many services and uses noticeably more resources than Commander. A real setup has three kinds of machine: a **dedicated Windows server** (physical or cloud) for Tosca Server, separate machines for Commander users, and separate machines for DEX agents. Installing Server and Commander on the same PC is fine for practice if the machine can carry both, and is what the source does; it is not a production setup.

## Download

1. Open the Tricentis support portal and go to product support.
2. Choose the Tosca version and open its download section.
3. Download the **Tosca Server** installer for that version.

:::caution
The Server version must match the installed Commander version. The speaker had Commander 14.3, found no 14.3 server on the portal, and upgraded Commander to 16.0 before installing Server 16.0. Either upgrade Commander to the version you can download, or download the server that matches Commander.
:::

## Installation

The installer works like the Commander one:

1. Run the `.exe` and click **Continue**; missing prerequisites are installed first.
2. The list of services to install is shown (gateway, license administration, AOS, distributed execution, file service, REST API and others). Keep the default location or change it.
3. Choose **HTTP** or **HTTPS**. HTTPS requires a certificate whose thumbprint you enter and which must match; the speaker uses HTTP for a demo.
4. Choose the port. The default is 80; if it is in use (as on the speaker's PC) enter another, for example `8080`. The server is then reachable at `http://localhost:8080`.
5. Confirm the install location for the file service and start the installation. It takes several minutes.

When it finishes, Tosca Server opens in the browser together with its **settings** page.

## Dashboard and settings

The dashboard is the landing page for administrators and for users with access to the server. The tiles named in the source:

- **Test Data Services (TDS)**
- **License administration**
- **User administration**
- **Administration console**
- **Distributed execution**, which opens the DEX monitor

The **Settings** page lists every service with its port, endpoint URL and configuration. Change a value and click **Save**: the affected service restarts. Every service you use must be in the running state, and each port must be free on the machine, otherwise that service is unavailable. Services you do not use can stay stopped.

## Restarting services

Three ways, all equivalent:

1. **Settings page**: click **Save**; the service restarts.
2. **Task Manager > Services**: the Tricentis services are listed; start, stop or restart one (restart goes through stopped to running).
3. **Windows Services** (`services.msc`): same list with status, for monitoring and restarting.

Configuration files live under `C:\Program Files\Tricentis\Tosca Server\`, one folder per service (including `DEX monitor` and `DEX server`). Some setups, distributed execution among them, require editing those files.

## DEX monitor

The **Distributed execution** tile opens the DEX monitor, a web page with two views:

- **Agents**: every DEX agent connected to the server, with its state (running or in error). Agents can be restarted from here. With no agents set up the count is zero.
- **Events**: every test event triggered from Commander, with its state (running, passed, failed). Events can be stopped from here.

The monitor URL becomes available as soon as Tosca Server is installed. Setting up agents and triggering test events is covered in [Distributed execution](/ToscaBase/execution/distributed-execution-dex/).

## Related

- [Licensing](/ToscaBase/getting-started/licensing/) and [Installation](/ToscaBase/getting-started/installation/) of Commander.
- [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/): the repository in the database tier.
