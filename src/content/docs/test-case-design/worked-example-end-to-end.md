---
title: "Worked example: end to end"
description: One pass through TestCase-Design on the Vehicle Insurance sample, from a TestSheet with attributes and instances to generated TestCases in an ExecutionList, with links to each concept.
level: 2
sidebar:
  order: 60
sources:
  - id: R0zEbmFq0HE
    title: "Tosca Tutorial | Live Session | Test Case Designing | End-To-End | Real time Examples | Live Project"
    url: https://www.youtube.com/watch?v=R0zEbmFq0HE
    at: "12:23"
---

This walkthrough follows a live session that designs the *Enter vehicle data* page of the *Vehicle Insurance* sample application from scratch: TestSheet, attributes, instances, combinatorial generation, template, instantiation, ExecutionList, and finally a class. It is the practical companion of the [TestCase-Design overview](/ToscaBase/test-case-design/test-case-design-overview/); every step links to the doc that explains it. A second walkthrough that continues the same application into conditional template folders is [Worked example: end-to-end live project](/ToscaBase/troubleshooting/worked-example-live-project/).

## Starting point

A component folder holds the sections for the session. The *Enter vehicle data* page has already been scanned into a Module with one ModuleAttribute per field (`Make`, `Engine performance`, `Date of manufacture`, `Number of seats`, `Fuel type`, `License plate number`, ...). A TestCase containing that Module exists in the TestCases section, with empty values. Nothing is designed yet.

## Step 1: sheet and attributes

1. In the TestCase-Design section create a folder, then a TestSheet named `Vehicle data` inside it (one sheet per requirement is the guideline). [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/)
2. Create a top-level attribute `Enter vehicle data` and sub-attributes for the fields that will be tested: `Make`, `Engine performance`, `License plate number`. One attribute per screen with a child per field keeps the sheet aligned with the application.
3. Set **Business relevant**: `Make` and `Engine performance` are mandatory fields, so `Yes`; `License plate number` is optional, so `No`; anything that verifies a result would be `Result`. The speaker toggles the value with **Toggle Business Relevance** and watches the icon colour change.

## Step 2: instances with character and position

1. Give `Make` the instances `Audi`, `BMW`, `Ford`. [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/)
2. Give `Engine performance` the boundary values `1` and `2000` (the field accepts 1 to 2,000) and an out-of-range `12000`. The invalid value exists on purpose: negative scenarios come from invalid instances.
3. Set **Character** and **Position**: `1` and `2000` are `Valid`, `12000` is `Invalid` (position `Inner`, since it is not a boundary of the valid range). One value per attribute becomes `Straight through`: `Audi` for the make, `2000` for engine performance. `1` is marked `Boundary`; `2000` would be a boundary too, but as soon as its character is `Straight through` Tosca sets the position to `Inner` and makes it read-only.

:::note
The subtitle transcript mentions `2001` as "at the boundary" once, although that instance was never created on screen. The rule the speaker states is clear: one straight-through instance per attribute, boundary values marked as such.
:::

## Step 3: TestCase instances, by hand and generated

1. Right-click the sheet **> Create Instance** three times. Three columns appear; in each, pick a value per attribute from the dropdown: a column with all straight-through values, a column with other valid values, a column with the invalid `12000`.
2. Delete the three columns to try the generators. **Generate Instances > All combinations** produces two columns while the sheet has only two-value attributes.
3. Drag the `Enter vehicle data` Module onto the sheet. Tosca creates attributes and instances for every field from the Module. Fix the generated values where they are wrong (free-text fields) and set character, position and business relevance again.
4. **All combinations** now fails: 77,760 instances exceed the limit of 1,000. **Orthogonal** produces the minimum set, with at least one value of every attribute per column. **Pairwise** produces more.
5. **Linear expansion** fails with a message that a straight-through instance is missing. Mark one per attribute (manually; there is no automatic way) and run it again: the result is the optimum set Tricentis recommends.

## Step 4: template

1. In the TestCases section right-click the TestCase **> Convert to Template**. It can no longer be executed. [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/)
2. Drag the `Vehicle data` sheet onto the template. The template's **Schema path** property now shows the sheet name; **Jump to Schema Definition** opens the sheet.
3. Click **Check Template**: `No errors found in template`.
4. Look at the TestStepValues: the empty ones were filled with references into the sheet (attribute and sub-attribute). Values that were already filled were not touched; for those, drag the attribute from the sheet into the value, or type the reference.

## Step 5: instantiate, execute, maintain

1. Right-click the template **> Create Template Instance** (or **Instantiate** in the ribbon), confirm **Start instantiation**. A folder with as many TestCases as the sheet has columns appears; open two of them and the values differ according to the combination.
2. In the Execution section create a folder and an ExecutionList, and drag the instance folder into it: one execution entry per TestCase. [Execution lists](/ToscaBase/execution/execution-lists/)
3. Change a value in the sheet, then right-click the instance folder **> Reinstantiate Instance**. The change is in every affected TestCase.
4. On the template set **Instance name** to a pattern starting with `TC` and reinstantiate; the TestCases are renamed to the pattern.

## Step 6: a class for the shared attributes

The same `Enter vehicle data` attributes would be needed in sheets for trucks, motorcycles and campers. Drag the attribute into the folder and choose **Create class from attribute**; a class `Enter vehicle data` with all sub-attributes and instances is created. In each sheet delete the local attributes and drag the class in: the sheet now holds a read-only class reference, and changes are made once in the class. [Design classes](/ToscaBase/test-case-design/design-classes/)

## What the session leaves you with

- A sheet that documents the scenario: attributes per screen, values with valid/invalid/straight-through characters, boundaries marked.
- A generated, optimum set of TestCases instead of hand-written ones, regenerated with one click when data changes.
- An answer for the interview question "how do you build TestCases in Tosca": start in TestCase-Design with a design technique, build a template, instantiate. Building directly in the TestCases section works, but uses Tosca as an editor rather than as a framework.
