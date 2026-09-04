---
title: What is Tosca
description: Tricentis Tosca in one page - a scriptless, model-based test automation platform, its main features, the applications it supports, and how it compares with Selenium.
level: 1
sidebar:
  order: 10
sources:
  - id: qTmnXrP3Dqw
    title: "Tosca Testing Tutorial Part 1:  What is Tosca, Tosca, Architecture, Introduction"
    url: https://www.youtube.com/watch?v=qTmnXrP3Dqw
    at: "00:17"
  - id: 4At7coUGDJU
    title: "Tosca Tutorial | Lesson 1 - Introduction To Tosca | What is Tosca | Codeless Automation Tool |"
    url: https://www.youtube.com/watch?v=4At7coUGDJU
    at: "00:02"
---

Tricentis Tosca is a scriptless, model-based test automation platform for end-to-end testing. Instead of writing scripts, you scan the application under test into **Modules** and assemble **TestCases** from them by drag and drop, so functional, regression and API tests can be built with a small skill set and a short learning curve. It is a commercial product by Tricentis, positioned as a continuous testing platform that feeds fast results back into agile and DevOps pipelines.

## Why test automation, and why Tosca

Automation testing replaces manual test steps with steps performed by a tool. Its goals are product quality, saved human effort and a shorter development life cycle. Earlier generations of tools (QTP/UFT, RFT, Selenium) required scripting; Tosca's selling point is that the same work is done without code, so tests are written faster and by more people, and standard management reports come out of the box without customisation.

Tosca is used for functional and regression testing, and API testing is part of the same tool, which matters in agile projects where an application is tested layer by layer while it is still being built.

## Model-based testing

The feature that defines Tosca. For every unit-level functionality or screen of the application, the tester creates a **Module** that stores the technical information needed to steer it (the controls and their identifying properties). TestCases are then built by combining Modules. Because the technical detail lives in the Module and not in every test, a change in the application is fixed once, in the Module. See [Modules overview](/ToscaBase/modules/modules-overview/).

## Main features

| Feature | What it gives you |
|---|---|
| Scriptless automation | TestCases are built by dragging Modules; test data parameterisation and verification steps are configured, not coded |
| Risk-based testing | Requirements carry a risk weighting; Tosca picks the subset of the suite that minimises risk and measures risk coverage from execution results. See [Requirements and risk](/ToscaBase/requirements-and-reporting/requirements-and-risk/) |
| Distributed execution | Runs are spread over several machines and scheduled unattended. See [Distributed execution](/ToscaBase/execution/distributed-execution-dex/) |
| CI/CD integration | Jenkins, Azure DevOps, Jira and similar tools. See [CI integration](/ToscaBase/execution/ci-integration-jenkins/) |
| Dynamic test data | TCD (test case design), TDM (test data management) and TDS (test data service); test data can live in Tosca's own database or an external one |
| Recording | Test scenarios are recorded and turned into TestCases in one action. See [Recorder](/ToscaBase/test-cases/recorder/) |
| API testing | Components exposed through APIs are tested before the UI exists. See [API testing](/ToscaBase/api-testing/) |
| Service virtualisation | Dependent systems that are unavailable during execution are emulated so the run can proceed |
| Test management | Requirements, tracking, risk analysis, manual and exploratory testing, reporting and analytics in one workspace |
| Load testing | Named as supported in the QASCRIPT introduction; not covered further in this knowledge base |
| Third-party tools | Perfecto, Selenium and qTest integrate with minimal customisation |

Supported application types include web, desktop (.NET, PowerBuilder), SAP, Salesforce, mainframe, mobile and APIs. Element identification uses several technologies, marketed as AI-based, to find controls on any of these.

## Tosca versus Selenium

| | Tosca | Selenium |
|---|---|---|
| Cost | Licensed, paid | Open source, free |
| Approach | Codeless, model-based | Script-based, requires a programming language |
| Applications | Web, desktop, mobile, API | Web only |
| Support | Vendor support team | Community |
| Reporting and object repository | Built in | Not included in WebDriver |
| API and load testing | Included | Not out of the box |

Which one fits depends on budget, the types of applications to test and the team's skill set.

## Prerequisites for learning Tosca

Basic knowledge of software testing (test cases, test steps, verification) is assumed by both tutorial series; no programming background is needed.

## Where to go next

- [Architecture](/ToscaBase/getting-started/architecture/) explains the components (Commander, XScan, Executor, repository, license server).
- [Licensing](/ToscaBase/getting-started/licensing/) and [Installation](/ToscaBase/getting-started/installation/) get the tool on your machine.
- [First TestCase](/ToscaBase/getting-started/first-test-case/) builds a working login test end to end.
