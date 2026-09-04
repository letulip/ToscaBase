---
title: Test Configuration Parameters
description: Test Configuration Parameters (TCPs) hold environment and settings data outside the TestSteps; where to define them, the {CP[name]} syntax, system-defined parameters, and project-level Configurations.
level: 2
sidebar:
  order: 20
sources:
  - id: k_paxCad6Kw
    title: "Tricentis Tosca Tutorial Part-7: Tosca Parameters,Tosca Configuration Parameter"
    url: https://www.youtube.com/watch?v=k_paxCad6Kw
    at: "01:50"
  - id: H5M6Y_Su4OQ
    title: "Tosca Tutorial | Lesson 156 - Test Configuration Parameters | Project Configurations |"
    url: https://www.youtube.com/watch?v=H5M6Y_Su4OQ
    at: "00:09"
---

A **Test Configuration Parameter** (TCP) is a named value defined on a Tosca object rather than inside a TestStep. TestSteps refer to it with `{CP[name]}`, so changing the value in one place changes every step that uses it. TCPs are the right home for data that is the same across a suite but differs between environments or runs: application URL, credentials, browser, timeouts, report paths. Hard-coding such values in TestSteps means editing the TestCase every time the data changes; with a thousand steps using the same URL, that is a thousand edits.

## Where TCPs live

Every object that can carry TCPs has a **Test Configuration** tab in its details: the project root, component folders, TestCase folders, TestCases, ExecutionLists, the TestCase-Design folder, and the **Configurations** section. Rules:

- A TCP defined on a folder is **inherited** by every sub-folder and TestCase below it. Define shared values as high as makes sense (root or component level) and override lower down only when needed.
- TCPs are **read-only during execution**; set them before the run.
- Some parameters are **system-defined** by Tosca (they appear in a drop-down when you create one), the rest are **custom** parameters you name yourself.

## Creating and using a TCP

1. Select the TestCase (or folder, ExecutionList), open the **Test Configuration** tab.
2. Right-click the object at the top of the tab and choose **Create Test Configuration Parameter**.
3. In the parameter drop-down pick a system-defined parameter (for example `Browser`, which then offers a drop-down of browser values: Chrome, Firefox, Edge, Internet Explorer and more) or type a custom name such as `Username`, `Password`, `URL`, `MyTCP`.
4. Enter the value. The **data type** can be changed; choose `Password` for credentials so the value is hidden.
5. In the TestStep, replace the literal with `{CP[name]}`. Typing `{CP[` pops up the list of parameters visible to this TestCase.

A value cannot be deleted from the list; use **Reset to default value** on the parameter, which removes it.

Beyond maintainability, the video points out two side effects: TestSteps become **abstract** (a reader sees `{CP[Password]}`, not the secret) and the suite is easier to run against another environment. The demo replaced the username, password and URL of a login TestCase with TCPs so that the same case could be run for seven different demo users without creating seven TestCases.

TCPs combine with other parameter types:

- `TBox Set Buffer` with value `{CP[MyTCP]}` copies a configuration value into a [buffer](/ToscaBase/data-and-parameters/buffers/); the ScratchBook log shows the resolved value.
- A [Business Parameter](/ToscaBase/data-and-parameters/business-parameters-and-libraries/) of a reusable TestStepBlock can be fed with `{CP[SearchText]}` instead of a literal.
- Some Standard Modules and Test Data Services require specific TCPs before they run at all: `Browser` for [Execute JavaScript](/ToscaBase/standard-modules/execute-javascript/), `TestDataEndpoint` and `TestDataRepository` for [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/).

## System-defined parameters worth knowing

The complete list is in the Tricentis documentation; these are the ones the video singles out, grouped by engine.

| Engine | Parameter (as named in the video) | What it controls |
|---|---|---|
| XBrowser | `Browser` | Which browser the web TestCase runs in; the most important parameter for web tests |
| XBrowser | Browser version | Version of that browser |
| XBrowser | Accessibility analysis, accessibility fast mode | Whether an accessibility analysis runs, and whether in fast mode |
| TBox | Avoid execution recorder | Enables or disables recording for the TestCase |
| TBox (recovery engine) | On dialog failure, on exception failure, on verification failure | What Tosca does after each kind of failure |
| TBox | Page sync | Synchronisation with pending Ajax requests |
| TBox | Scrolling behaviour | Vertical or horizontal scrolling |
| TBox | `SynchronizationTimeout` | How long Tosca waits for a control; has a default you can override |
| TBox | `TargetDateFormat`, target time format | Date and time format used by the TestCase, see [Date expressions](/ToscaBase/expressions/date-expressions/) |
| TBox (recovery engine) | TestStep retries, TestCase retries | How many times a step or a TestCase is retried |
| Mobile | APM server, browser, device model, device name, live view, simulator | Mobile engine settings, covered in the mobile lessons |

:::note
The transcript names most parameters in speech ("page sync", "avoid execution recorder"); only the ones shown in code above appear spelled out elsewhere in this knowledge base. Check the drop-down or the Tricentis documentation for the exact identifiers.
:::

## Project-level Configurations

The **Configurations** section of the project holds reusable sets of TCPs. It ships with defaults (API, mobile, Test Data Service) and lets you create your own Configuration, a configuration folder, a structure, or a virtual folder. Example: `Project A` with `Browser` = Chrome and `SynchronizationTimeout` = 3000, `Project B` with `Browser` = Firefox and `SynchronizationTimeout` = 6000, the same parameters with different values for two teams.

- **Use** a Configuration by dragging it onto a TestCase, folder or ExecutionList. The object then inherits the whole set.
- **Lock** a Configuration by opening its **Properties** and setting **Predefined** to `true`. A predefined Configuration cannot be modified or deleted, only inherited. A TestCase that inherits it can still override a value locally (Chrome to Edge, say), and that override applies only to that TestCase; the original stays unchanged. This keeps project-wide settings under the control of an administrator.

## Module-level Configuration Parameters are a different thing

Modules also carry **Configuration Parameters** (`ExplicitName`, `ConstraintIndex` and others), set per ModuleAttribute: they tune how Tosca steers a control and are never read with `{CP[...]}`; see [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/) and, for `ExplicitName`, [Control identification](/ToscaBase/modules/control-identification/). The one case where such a parameter is driven from the TestCase through a buffer (`ConstraintIndex` for two identical browser tabs) is a troubleshooting recipe in [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/#identical-browser-tabs).

## Related

- [Buffers](/ToscaBase/data-and-parameters/buffers/): the run-time counterpart of TCPs
- [Business Parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/)
- [Cross-browser execution](/ToscaBase/execution/cross-browser-execution/): the `Browser` TCP on ExecutionLists
