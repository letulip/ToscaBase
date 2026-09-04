---
title: Test cases
description: Building TestCases from Modules - TestSteps and ActionModes, conditions and loops, repetitions, Recovery and Cleanup Scenarios, the recorder and exploratory testing.
level: 1
sidebar:
  order: 0
---

A TestCase is where Modules turn into an executable test: each TestStep steers the controls of one Module, and the ActionMode on every value decides whether Tosca enters, verifies, buffers or waits for it. This section starts with the TestCase object and the ActionMode reference, then covers what changes the straight top-to-bottom flow (conditions, loops, repetitions, recovery), and ends with two ways of recording instead of building.

| Doc | Covers |
|---|---|
| [TestCase basics](/ToscaBase/test-cases/test-case-basics/) | Technical and business TestCases, creating a TestCase, TestSteps from Modules, Workstate, a first end-to-end example |
| [ActionModes](/ToscaBase/test-cases/action-modes/) | Reference for `Input`, `Insert`, `Verify`, `Buffer`, `WaitOn`, `Select` and `Constraint`, with a summary table and worked examples on forms and tables |
| [Control flow](/ToscaBase/test-cases/control-flow/) | `If` statements, `While` and `Do` loops, the Maximum repetitions property |
| [Repetitions](/ToscaBase/test-cases/repetitions/) | Repeating a folder's TestSteps a fixed number of times through the Repetition column or property |
| [Recovery and Cleanup Scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/) | Enabling the recovery engine, Recovery Scenario Collections, Retry level, Cleanup Scenarios |
| [Recorder](/ToscaBase/test-cases/recorder/) | Generating Modules and a TestCase by recording actions, verification mode, what to clean up afterwards |
| [Exploratory testing](/ToscaBase/test-cases/exploratory-testing/) | Explorative sessions, recording a scenario document with screenshots, exporting to PDF |

Read in order: the first two are prerequisites for everything else in the site. Reusing TestSteps across TestCases (libraries, Business Parameters) is in [Data and parameters](/ToscaBase/data-and-parameters/), and the rules for a maintainable TestCase are in [Best practices](/ToscaBase/best-practices/).
