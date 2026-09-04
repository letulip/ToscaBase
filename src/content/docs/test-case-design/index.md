---
title: Test case design
description: Model test data in TestSheets with attributes, instances and classes, then generate TestCases from templates.
level: 2
sidebar:
  order: 0
---

The **TestCase-Design** section is where Tosca separates test data from TestCases. You describe a scenario as a TestSheet of attributes and their values, mark which values are valid, invalid, straight-through or on a boundary, and let Tosca combine them into TestCase instances. A TestCase converted into a template reads from the sheet, and instantiation produces one concrete TestCase per instance. This section covers that whole path.

| Doc | What it covers |
|---|---|
| [TestCase-Design overview](/ToscaBase/test-case-design/test-case-design-overview/) | Why data is kept apart from TestCases, equivalence partitioning and boundary values, the objects of the section, the workflow |
| [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/) | Folders and TestSheets, attributes and sub-attributes, the four recommended attributes, the Business Relevant property |
| [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/) | Instances as values and as TestCases, Character and Position, all combinations / orthogonal / pairwise / linear expansion |
| [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/) | Convert to Template, schema path, Check Template, mapping values, Instantiate, conditional TestSteps, Reinstantiate |
| [Design classes](/ToscaBase/test-case-design/design-classes/) | Classes for shared attributes, class references, resolving a reference |
| [Worked example: end to end](/ToscaBase/test-case-design/worked-example-end-to-end/) | The full sequence on the Vehicle Insurance sample, from empty sheet to ExecutionList |

Read them in order. The overview gives the vocabulary, the next two docs build the sheet, the template doc turns it into TestCases, classes reduce duplication across sheets, and the worked example ties everything together. Related: [Test case structure](/ToscaBase/best-practices/test-case-structure/) for the no-constants rule that templates depend on, and [Requirements and risk](/ToscaBase/requirements-and-reporting/requirements-and-risk/) for linking generated TestCases to requirements.
