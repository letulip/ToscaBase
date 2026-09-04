---
title: Self-healing mode
description: What Tosca's self-healing mode does when a control changes in a new build, how self-healing properties are captured in XScan, how to enable the mode with the SelfHealing Test Configuration Parameter, and how healed steps appear in the log and get applied to the Module.
level: 2
sidebar:
  order: 120
sources:
  - id: c_zKy9iBeME
    title: "TRICENTIS Tosca 16.0 - Lesson 26 | Enable Self-healing Mode | Self-healing Test Cases | AI Powered"
    url: https://www.youtube.com/watch?v=c_zKy9iBeME
    at: "01:05"
---

**Self-healing mode** lets a TestCase keep running when a control in the system under test has changed. The classic case is a new build: a button's identifying property changes, the Module no longer matches, and every TestCase using it fails until someone rescans. With self-healing enabled, Tosca falls back to a set of **self-healing properties** stored with the ModuleAttribute, finds the control anyway, marks the step as healed in the log, and lets you write the new identification back into the Module with one click. The gain is more stable runs, an explicit list of changed controls, and far less Module maintenance after each build.

Tricentis describes the workflow in four steps: create the TestCase with Modules whose attributes carry self-healing properties, enable self-healing mode for the TestCase, put the TestCase in an [ExecutionList](/ToscaBase/execution/execution-lists/), and run it. The lesson was recorded on Tosca 2023 but states that the feature exists in 15, 16 and 2023 alike.

## Self-healing properties in the Module

Self-healing only works for ModuleAttributes that have self-healing properties. XScan adds them automatically when you scan or rescan a control; you decide which ones to keep.

1. Scan the control as usual ([XScan](/ToscaBase/modules/xscan/)). The identification properties, for example `Tag` = `input` and `Value` = `Sign in` for a button, are chosen as before ([Control identification](/ToscaBase/modules/control-identification/)).
2. In the scan window switch the property view to **Self-healing properties**. XScan lists candidates such as `Label`, `ClassName`, `Id`, `Name`, `Tag`, `Title`, `Value`, `Type`, `XPath` and the action point. Tick the ones that are stable and non-empty (in the lesson `XPath`, `Tag`, `Type`, `ClassName`, `Value` and the action point; `Id` and `Name` were blank and left out). Untick the property already used for identification if you expect it to change.
3. Save the Module. In Tosca Commander the ModuleAttribute now has a **Self-healing properties** tab next to **Details**, listing each property with a weight: in the lesson `Tag` 0.25, `Type` 0.5, `ClassName`, `XPath`, `Value` and the action point 1.0. The weights are assigned by Tosca and feed the weighted algorithm below.

:::tip
Capture self-healing properties during the **first** scan. If a Module was scanned without them, the control cannot be healed; you have to [rescan](/ToscaBase/modules/rescan-modules/) it while the application still matches the Module.
:::

## Enabling the mode

Self-healing is switched on through a [Test Configuration Parameter](/ToscaBase/data-and-parameters/test-configuration-parameters/), so it can be set on a TestCase, a folder or an ExecutionList:

1. Open the **Test Configuration** tab of the TestCase and create a parameter; pick `SelfHealing` from the drop-down.
2. Choose a value:

| Value | Behaviour |
|---|---|
| `Weighted` | Uses the weights of the self-healing properties to find the most unique control |
| `Combination` | Builds all possible combinations of the stored self-healing properties until one identifies a suitable control |
| `False` | Self-healing disabled (default) |

In the lesson `Browser` = Edge and `SelfHealing` = `Combination` were set on the TestCase and the run was started directly from the TestCase; the documented workflow runs it from an ExecutionList.

## How a healed step is reported

The lesson simulated a new build by renaming the login button from `Sign in` to `Login` in the browser (the Module identified it by `Value` = `Sign in`).

- **Without self-healing** the step fails with the usual message that the control could not be found.
- **With self-healing** the step passes, and the execution log marks it with a **self-healing icon** (a heart symbol). Expanding the step shows the method (`Combination`), a certainty value, how many combinations were tried (seven) and which property finally identified a unique control (`ClassName`).

The TestCase therefore completes, and the log doubles as a list of every control whose identification no longer holds.

## Applying the healed identification

A healed step is a workaround, not a fix: the next run heals again. To make it permanent, right-click the healed step in the log > **Apply self-healing properties**. Tosca replaces the old identification property in the ModuleAttribute with the one it found (`ClassName` instead of `Value` in the lesson); save the Module and the TestCase runs normally.

## Limits

- Only controls scanned with self-healing properties can be healed; nothing is guessed for attributes without them.
- Healing needs at least one stable property in the stored set. If every stored property changes, or if the healed property matches several controls, the step still fails.
- The feature is enabled per TestCase, folder or ExecutionList through the parameter, not globally; a TestCase without `SelfHealing` behaves as before.
- Self-healing hides breakage until you look at the log. Review healed steps after every run and apply or rescan, otherwise the Modules drift from the application.

## Related

- [Control identification](/ToscaBase/modules/control-identification/): the identification properties self-healing falls back from
- [Rescan Modules](/ToscaBase/modules/rescan-modules/): the manual alternative when a control changes
- [Results and logs](/ToscaBase/execution/execution-results-and-logs/): reading the execution log
