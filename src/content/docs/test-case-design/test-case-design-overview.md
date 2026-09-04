---
title: TestCase-Design overview
description: What TestCase-Design (TCD) is, which objects it consists of, why test data is kept apart from TestCases, and the workflow from TestSheet to generated TestCases.
level: 2
sidebar:
  order: 10
sources:
  - id: VeG0TLkQM8g
    title: "Tricentis Tosca Tutorial Part-10 : Tosca Test Case Design, Tosca Class"
    url: https://www.youtube.com/watch?v=VeG0TLkQM8g
    at: "00:15"
  - id: R0zEbmFq0HE
    title: "Tosca Tutorial | Live Session | Test Case Designing | End-To-End | Real time Examples | Live Project"
    url: https://www.youtube.com/watch?v=R0zEbmFq0HE
    at: "00:02"
---

**TestCase-Design** (TCD) is the Tosca approach that keeps test data apart from the technical part of a TestCase. The data lives in TestSheets in the TestCase-Design section; the TestCase becomes a template that reads from the sheet; Tosca generates one concrete TestCase per data set. Changing the data no longer means editing TestCases, and the same template produces as many TestCases as the sheet has rows. Teams that skip this section and build TestCases directly in the TestCases section lose the core framework Tosca is built around.

## Why design before you build

TestCase-Design brings two classic functional-testing techniques into the tool: **equivalence partitioning** and **boundary value analysis**. The point of both is the same: the minimum number of TestCases that still covers the application and its highest risks, because nobody has time to test every value of every field in a sprint.

Take a field that accepts numbers from 1 to 2,000 (the *Engine performance* field of the *Vehicle Insurance* sample rejects 12,000 with a warning that the number must be between 1 and 2,000). Testing 2,000 values is impossible, so:

- **Equivalence partitioning** splits the values into partitions: below 1, from 1 to 2,000, above 2,000. One or two values per partition are enough (0, 200, 2,500): if 200 works, 500 and 1,000 are expected to work too.
- **Boundary value analysis** adds the values on the edges of each partition, such as 1, 2, 2,000 and 2,001, because coding errors cluster around boundaries.

In Tosca these techniques become properties of instances (valid / invalid / straight-through character, inner / boundary position) and the combinatorial methods that generate TestCase instances from them. See [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/).

## Objects in the TestCase-Design section

| Object | Role |
|---|---|
| **Folder** | Groups TestSheets and classes logically, typically one folder per application or component. |
| **TestSheet** | The list of data for all combinations of a scenario. Looks like an Excel sheet; it is the highest-level object in the section. |
| **Attribute** | A data parameter, usually one per application field or business object (user type, product, payment method). Attributes can nest to any depth. Attributes that are not business-relevant carry comments or descriptions; a *result* attribute carries expected results. |
| **Instances** collection | Holds the instances of an attribute, that is, all values the attribute can take. |
| **Instance** | One value of an attribute, created at TestSheet, attribute or class level. |
| **TestSheet instance** | An instance of the sheet itself. Each one is a TestCase: it picks one value per attribute and its name becomes the generated TestCase name. |
| **Class** | Like a TestSheet, but built for reuse: common attributes and data that several TestSheets share. |
| **Class reference** | The link from a TestSheet to a class, created by drag and drop. |

The hierarchy: a TestSheet contains attributes, instances and class references; a class contains attributes and instances; an attribute can contain further attributes and instances.

:::note
The Part 10 tutorial also lists "steps" (a TestSheet "may have TestSteps", "a step can keep more steps and attributes") among TestCase-Design objects. They are not demonstrated in any of the source videos, so this doc does not describe them.
:::

## The workflow

1. **Create a TestSheet** in a folder of the TestCase-Design section and add attributes for the data parameters of the scenario ([TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/)).
2. **Create instances** for every attribute, then create instances of the TestSheet itself: one per TestCase. For each TestSheet instance choose a value per attribute, or let Tosca generate the combinations ([Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/)).
3. **Move shared data into a class** and reference it from the TestSheets that need it ([Design classes](/ToscaBase/test-case-design/design-classes/)).
4. **Convert the TestCase into a template**, drag the TestSheet onto it and replace hard-coded values by references to sheet attributes.
5. **Instantiate** the template. Tosca creates one TestCase per TestSheet instance, filled with that instance's data. **Reinstantiate** whenever the sheet or the template changes ([Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/)).
6. **Execute** the generated TestCases from an ExecutionList ([Execution lists](/ToscaBase/execution/execution-lists/)).

A complete pass over the *Vehicle Insurance* sample is in [Worked example: end to end](/ToscaBase/test-case-design/worked-example-end-to-end/).

:::tip
The TestCase-Design section can be opened as a floating window on top of the TestCases section. That makes dragging a TestSheet onto a template, or an attribute into a TestStepValue, a single movement instead of a switch between sections.
:::

## Advantages and costs

Advantages:

- Dynamic test data and objects are easy to handle, and data is reused across TestCases.
- No scripting; data and technical components stay separate.
- When data changes, TestCases are regenerated, not edited.
- Coverage is planned from a design technique, which is also what interviewers expect to hear when they ask how you build TestCases: start in TestCase-Design, build a template, generate the TestCases.

Costs, as the Part 10 speaker puts it: the section is complicated and "a little expensive", and its UI takes time to learn. The live-session speaker agrees that it is the part newcomers find most confusing, which is why some teams skip it.
