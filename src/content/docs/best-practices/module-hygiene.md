---
title: Module hygiene
description: Keep Modules small and categorised by functionality, and merge duplicate Modules regularly, to protect workspace size and execution performance.
level: 3
sidebar:
  order: 30
sources:
  - id: 8_WAZ6d1jQM
    title: "Tosca Tutorial | Lesson 99 - Use limited Module Attributes | Categorize | Best Practices |"
    url: https://www.youtube.com/watch?v=8_WAZ6d1jQM
    at: "00:40"
  - id: VT4f_mHizH4
    title: "Tosca Tutorial | Lesson 104 - Merge Duplicate Modules | Workspace Performance | Best Practices |"
    url: https://www.youtube.com/watch?v=VT4f_mHizH4
    at: "00:45"
---

Modules are the largest part of a Tosca workspace and the objects most often created carelessly. Two Tricentis best practices keep them under control: scan only the ModuleAttributes you need and split them into Modules by functionality, and find and merge duplicate Modules on a regular basis. Both target the same problems: workspace size, execution speed, and maintenance effort.

## Limit ModuleAttributes and categorise Modules

When you scan a page with XScan it is tempting to select every control, so that the Module can serve every future TestCase without rescanning. The source compares two ways of scanning the `Enter Vehicle Data` page of the sample insurance application, a form with mandatory and optional fields plus page headers and footers:

- **Categorised.** A `Headers` Module holding only the `Automobile` link, and an `Enter Vehicle Data` Module holding the form fields.
- **Monolithic.** One Module holding every control on the page.

The monolithic Module looks reusable but is not efficient:

- **Workspace size.** Every scanned control is stored whether or not a TestCase uses it, and the workspace grows accordingly.
- **Execution speed.** To click the `Automobile` link through the monolithic Module, Tosca has to work through all its ModuleAttributes to find the one being steered; through the one-attribute `Headers` Module it does not.
- **TestCase readability.** Categorised Modules carry their structure into the TestCase: each TestStep is one Module, and the sequence of steps reads as the flow. With one Module reused in every step you end up renaming every TestStep by hand.

The rule: scan only the controls the TestCase needs, and put them into Modules that follow the application's functionality (a page, a header bar, a form). When a later TestCase needs a control you did not scan, rescan that window and add the control to the existing Module rather than creating a new one; see [Rescan Modules](/ToscaBase/modules/rescan-modules/) and [XScan](/ToscaBase/modules/xscan/).

## Merge duplicate Modules

A duplicate Module is a second scan of a screen that already has one. Working alone you rarely create them, because you know what you have scanned. In a team they appear constantly: Modules are not named according to a [naming convention](/ToscaBase/best-practices/naming-conventions/), a colleague cannot find the right one among hundreds, or is not sure that the existing one does what its name suggests, and scanning again is quicker than searching. Each of these is a mistake, and together they produce a workspace with several copies of every screen.

The cost compounds over time:

- Workspace size grows until it becomes unmanageable; Tosca loads slowly and executions get slower.
- Every change to a screen has to be applied to every copy, so migration and maintenance effort multiplies.
- Different team members use different copies, so a fix in one does not reach the others.

Tosca ships a **Module merge assistant** for exactly this, and the recommendation is to run it on a schedule, not only when something breaks.

1. If you already know the two Modules are duplicates, select them and merge directly.
2. Otherwise select a Module and use **Find duplicate Modules**; Tosca lists Modules with the same ModuleAttributes (in the source, two scans of a `Swag Labs` login form, each with `Username`, `Password` and `Login`).
3. Select the ones to combine and choose **Merge selected**.

The merge takes the source Module and merges it into the target. The target Module is left unchanged, every usage of the source Module in TestCases is re-linked to the target, and the source Module is deleted. Nothing needs to be fixed by hand afterwards. The full procedure, with screenshots of the assistant, is in [Duplicate and merge Modules](/ToscaBase/modules/duplicate-and-merge-modules/).

:::caution
The merge assistant only finds Modules whose attributes match. Duplicates that were scanned with different control selections will not be flagged; catching those needs a naming convention and a [review process](/ToscaBase/best-practices/review-process/).
:::

## Why this is a performance topic

Both practices come back to workspace size. A workspace with bloated and duplicated Modules starts slowly, executes slowly and takes longer to synchronise in a multi-user setup. Keeping Modules lean and unique is the cheapest performance optimisation available, and it belongs in the checklist of every review.
