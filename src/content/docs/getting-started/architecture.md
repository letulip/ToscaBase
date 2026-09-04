---
title: Architecture
description: The components of the Tosca suite - Tosca Commander, XScan, Executor, the test repository and the license server - and the interfaces through which Tosca is used.
level: 1
sidebar:
  order: 20
sources:
  - id: qTmnXrP3Dqw
    title: "Tosca Testing Tutorial Part 1:  What is Tosca, Tosca, Architecture, Introduction"
    url: https://www.youtube.com/watch?v=qTmnXrP3Dqw
    at: "05:35"
  - id: 4At7coUGDJU
    title: "Tosca Tutorial | Lesson 1 - Introduction To Tosca | What is Tosca | Codeless Automation Tool |"
    url: https://www.youtube.com/watch?v=4At7coUGDJU
    at: "05:35"
---

Tosca is not one program but a suite. The part you work in every day is Tosca Commander; behind it sit the scanner that produces Modules, the executor that runs TestCases, a repository that stores everything, and a license server that decides who may use the tool. Knowing which component does what makes the rest of this knowledge base easier to place: Modules come from XScan, results come from the Executor, and a multi-user workspace is a repository.

## Components

| Component | Role |
|---|---|
| **Tosca Commander** | The main application. Creates, manages, executes and analyses test automation: TestCase development, execution, maintenance and reporting all happen here. See [Commander overview](/ToscaBase/getting-started/commander-overview/) |
| **Tosca XScan** (scan wizard) | Scans the application under test and saves the technical information of its controls into Modules, which are then used to identify and steer the screen items. See [XScan](/ToscaBase/modules/xscan/) |
| **Tosca Executor** | Runs TestCases against the test objects and manages executions and their logs. See [ExecutionLists](/ToscaBase/execution/execution-lists/) |
| **Test repository** | Stores TestCases, Modules, dynamic test data, user information and related artefacts in a shared database. Supported databases named in the source: Oracle, SQL Server, DB2 (SQLite is used for small multi-user setups; see [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)) |
| **License server** | Configures, connects and validates licenses so that users can access Tosca. See [Licensing](/ToscaBase/getting-started/licensing/) |

:::note
The LambdaGeeks tutorial describes Tosca as "five components" including the license server; the QASCRIPT introduction lists four (Commander, Executor, XScan, test repository) and describes the repository as holding "the test data needed for all test execution". Both are simplifications of the same suite; the table above merges them.
:::

## Interfaces

Tosca is accessed through several interfaces:

- **GUI**: Tosca Commander's graphical interface, the normal way to work.
- **API**: programmatic access for integrations.
- **CLI**: the command line, used for unattended execution and administration. See [Command-line tools](/ToscaBase/administration/command-line-tools/).
- **Integrated test management environment**: access from test management tools that embed Tosca.

## How the parts fit together

1. The tester opens **Tosca Commander** connected to a workspace (a local file, or a shared repository for a team).
2. **XScan** scans the application and produces **Modules** in that workspace.
3. TestCases are assembled from Modules and grouped into **ExecutionLists**.
4. The **Executor** runs the ExecutionLists, locally or on distributed agents, and writes results and logs back to the repository.
5. Every Commander instance and agent checks out a license from the **license server**, which may be Tricentis' cloud server or a self-hosted one.

Related: [What is Tosca](/ToscaBase/getting-started/what-is-tosca/), [Distributed execution](/ToscaBase/execution/distributed-execution-dex/), [Tosca Server](/ToscaBase/administration/tosca-server/).
