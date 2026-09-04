---
title: Best practices
description: Tricentis' recommended conventions for naming, TestCase structure, Module hygiene, synchronisation and review, with the reasoning behind each.
level: 3
sidebar:
  order: 0
---

This section collects the practices that keep a Tosca project readable, fast and maintainable as it grows and as more people work in it. Each doc explains what Tricentis recommends, what goes wrong without it, and how it looks in Commander. The practices build on each other: a naming convention prevents duplicate Modules, a review process enforces the naming convention.

| Doc | What it covers |
|---|---|
| [Naming conventions](/ToscaBase/best-practices/naming-conventions/) | Consistent names for Modules, TestCases, folders and TestSteps; a before-and-after example |
| [TestCase structure](/ToscaBase/best-practices/test-case-structure/) | Verification points, folder grouping (pre-processing, processing, post-processing), Repetitions and Constraints instead of loops, Workstates and their effect on requirement coverage |
| [Module hygiene](/ToscaBase/best-practices/module-hygiene/) | Limited ModuleAttributes, Modules categorised by functionality, finding and merging duplicate Modules |
| [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/) | `WaitOn` instead of `TBox Wait`, `X` instead of mouse and keyboard methods, with the Calculate / Send progress-bar example |
| [Review process](/ToscaBase/best-practices/review-process/) | Three approval stages as folders, the four-eyes principle, what reviewers check |

Read them in order: the review process at the end is where the earlier four become a team checklist.
