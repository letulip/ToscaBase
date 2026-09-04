---
title: "Worked example: end-to-end live project"
description: Finishing the vehicle-insurance sample end to end with conditional template folders, data-driven price options, WaitOn for the confirmation, and ExecutionList reporting.
level: 3
sidebar:
  order: 50
sources:
  - id: Z_0TLCYKrBU
    title: "Tosca Tutorial | Live Project | Automate End-to-End Scenarios"
    url: https://www.youtube.com/watch?v=Z_0TLCYKrBU
    at: "00:04"
---

This walkthrough completes the *Vehicle Insurance* sample application end to end. It starts from a workspace that already follows the best practices from earlier sessions and finishes the last three pages: choosing a price option, sending the quote, and confirming the result. The point is not the pages themselves but how the pieces fit together: Modules, a TestCase template, a TestSheet with attributes and conditions, template instances, ScratchBook and an ExecutionList. Every technique used here has its own doc; follow the links for details.

## Starting point

Inside the *Vehicle Insurance* component folder there are already:

- Modules for every page (see [Modules overview](/ToscaBase/modules/modules-overview/)).
- A TestCase design (TestSheet) with the vehicle and product data ([TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/)).
- A template with pre-processing and post-processing steps ([Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/)).
- Four instances: one straight-through case, two valid cases with different data, one invalid case; one of them already has verification points.
- Requirements linked to the cases ([Requirements and risk](/ToscaBase/requirements-and-reporting/requirements-and-risk/)).

Executing the instances shows how far the coverage goes: data entry up to the price table, verification of the prices displayed, and selection of an option. Left to do: verify the generated PDF (deferred), click *Next*, fill the *Send Quote* page, click *Send*, and verify the success message.

## Step 1: scan the missing controls

1. Open the *Select price option* Module, which so far holds only the price table, and **rescan** it ([Rescan modules](/ToscaBase/modules/rescan-modules/)). Add only the *Download quote* link and the *Next* button.
2. Scan a new Module for the *Send Quote* page in basic view: the input fields and the *Send* button.
3. Fill the page manually, click *Send*, wait for the confirmation dialog, and scan its *OK* button into a separate Module. XScan gives it the same name as the previous one; rename it to *Confirmation message*.

:::tip
Add only the controls the automation actually uses. Scanning whole pages costs performance and workspace size, and is against the recommended practice ([Module hygiene](/ToscaBase/best-practices/module-hygiene/)).
:::

## Step 2: data-driven price option with conditional folders

The option to click (Silver, Gold, Platinum, Ultimate) must come from test data, not from a hard-coded step.

1. In the TestSheet, add an attribute `Price option` with the four instances. Fill the data points randomly / orthogonally so that no two TestCase instances share the same data ([Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/)).
2. In the template, create a folder *Select price option Silver* containing the price-option Module with a click on the Silver entry.
3. Put a **condition** on the folder: `Price option` equals `Silver` **and** the test data type is valid (the invalid case never reaches this page). Make sure the two conditions are combined with AND, not OR.
4. Copy the folder three times for Gold, Platinum and Ultimate; rename, change the condition, and replace the click.

:::caution
When you copy a folder and re-point the click, disable or delete the original click step. A copied step still has ActionMode `Input`, so an untouched copy will still expect a value for the old entry.
:::

5. In every price-option folder add a second TestStep *Click next* on the *Next* button, using the same Module. Keep it as a separate TestStep rather than merging it into the selection step.
6. **Check template** (no errors), then **reinstantiate** the instances. Each instance now contains exactly one price-option folder: the straight-through case has Silver, the valid cases Gold and Platinum, the invalid case none.

This is the core pattern: the template holds every branch, conditions on folders pick the branch per instance, and instantiation produces a unique TestCase per data row.

## Step 3: send the quote

1. In the TestSheet add an attribute `Send quote` with sub-attributes `Email`, `Phone`, `Username`, `Password`, `Confirm password`, `Comments`, and give them instances (a shared email is fine for a demo; real projects would use different users). `Phone` and `Comments` are optional on the page and left empty.
2. In the template create a folder *Send quote* with the *Send Quote* Module. Every field takes its value from the TestSheet attribute; no static values in the template ([Test case structure](/ToscaBase/best-practices/test-case-structure/)).
3. Condition the folder on valid test data, as before.
4. Click *Send*.

## Step 4: wait for the confirmation, do not sleep

1. Add the *Confirmation message* Module with the *OK* button set to property `Exists`, value `True`, ActionMode `WaitOn`. Tosca waits until the dialog is present, however long it takes.
2. Add the same Module again as *Click OK* with `X` on the button.

`WaitOn` replaces a static wait; see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/) and [ActionModes](/ToscaBase/test-cases/action-modes/).

## Step 5: check, reinstantiate, run

1. **Check template** again, **reinstantiate**. The instances gain the *Send quote* folder with their own values.
2. Run one instance in ScratchBook: the option is chosen, *Next* is clicked, the form is filled, the wait picks up the confirmation, *OK* is clicked.
3. Right-click the ExecutionList > **Synchronize** (a harmless precaution; strictly only folder changes need it) and run from there. The result is the same as in ScratchBook; the difference is that the ExecutionList stores it with date, time and duration ([Execution lists](/ToscaBase/execution/execution-lists/), [Results and logs](/ToscaBase/execution/execution-results-and-logs/)).
4. For management reporting use the ExecutionList **print view** and export to Excel or PDF. Add or remove columns in the ExecutionList and the export follows; a little formatting in Excel makes it presentable ([Reports](/ToscaBase/requirements-and-reporting/reports/)).

## What was left out, and where it goes

- **PDF verification** of the downloaded quote was shown separately and can be inserted after *Download quote*: [PDF engine](/ToscaBase/engines/pdf-engine/).
- **Email verification** is impossible on the demo (no email is sent). On a real system verify through the UI, or add API TestSteps if the email is sent through an API: [API TestCases](/ToscaBase/api-testing/api-test-cases/).
- **Test events** to run on several agents need a multi-user workspace: [Distributed execution](/ToscaBase/execution/distributed-execution-dex/).

## Practices the project relies on

- One **component folder** per project holding Modules, TestCases, TestCase design, requirements and ExecutionLists; several component folders for several projects ([Test case structure](/ToscaBase/best-practices/test-case-structure/)).
- **Naming conventions** for Modules, TestCases and TestSteps ([Naming conventions](/ToscaBase/best-practices/naming-conventions/)).
- **No constants** in TestCases: parameterise through the TestSheet or Test Configuration Parameters ([Test configuration parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)).
- **Conditions** on template folders so that each instance is a distinct scenario, not the same scenario with different labels.
