---
title: TestSheets and attributes
description: Create a TestSheet in the TestCase-Design section, structure it with the four recommended attributes, and set the Business Relevant property to yes, no or result.
level: 2
sidebar:
  order: 20
sources:
  - id: 29ZncNqBgrc
    title: "Tosca Tutorial | Lesson 52 - Create Test Sheet and Attributes | Test Case Design | Business Relevant"
    url: https://www.youtube.com/watch?v=29ZncNqBgrc
    at: "00:01"
  - id: R0zEbmFq0HE
    title: "Tosca Tutorial | Live Session | Test Case Designing | End-To-End | Real time Examples | Live Project"
    url: https://www.youtube.com/watch?v=R0zEbmFq0HE
    at: "12:23"
---

A **TestSheet** is the top-level object of the TestCase-Design section: a grid, similar to an Excel sheet, that holds the test data and the logical structure of the TestCases for one scenario. If you have driven Selenium tests from an Excel workbook you know the idea; Tosca provides it inside the tool without code. A TestSheet is built from **attributes** (the characteristics of the application you test: account types, customer types, payment methods, single fields) and their **instances** (the values). This doc covers the sheet and its attributes; instances are in [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/).

## Create a folder and a TestSheet

1. Open the **TestCase-Design** section of Tosca Commander. Its folders are red, so you can tell the section apart from TestCases (blue) and others.
2. Do not create sheets directly under the root TestCase-Design folder. Right-click it and create a folder per application or component, for example `Swag Labs` or `Vehicle Insurance`.
3. Right-click the folder **> Create TestSheet** (the icon looks like a spreadsheet) and name it, for example `Regression test sheet` or `Vehicle data`.

How many sheets: one TestSheet per requirement is the recommended practice. One sheet per scenario or business area, or a single sheet for everything, also works; it depends on the project.

## Add attributes

Right-click the TestSheet **> Create Attribute**. Attributes can have sub-attributes, and those can have sub-attributes again, to any depth: a tree with a parent and any number of children. There is no limit on their number. Choose attributes by asking what you need to test on each page: the business objects, features or plain fields. In a purchase flow that gives `Products` with the children `Name`, `Price`, `Quantity`, and `Checkout` with `Shipping information`, `Payment information`, `Item total price`. For the *Vehicle Insurance* sample it gives one attribute per screen (`Enter vehicle data`, `Enter insurance data`, `Enter product data`, `Price option`) with a child per field (`Make`, `Engine performance`, ...).

### The four recommended attributes

Tosca recommends that every TestSheet has at least these top-level attributes:

| Attribute | Contents | Business relevant |
|---|---|---|
| `Administration` | No test data. Metadata about the sheet: `Designer`, `Business contact` (who to ask about the requirements), `Test cycle` (smoke, regression), `Comments` (what the sheet includes and excludes). | No |
| `Precondition` | Prerequisite data that sets the TestCases up: login data, users and their type (new, registered, business, technical), address or personal details, data that must exist in the application first. | Yes |
| `Process` | The main test data the TestCases enter: products, quantities, checkout and payment data. | Yes |
| `Verification` | Data used to compare expected with actual results, for example the confirmation message after an order. | Result |

You can have more or fewer attributes; this is the recommended minimum, not a rule.

## Business Relevant

Every attribute has a **Business relevant** property with three values: `Yes`, `No` and `Result`. The default is `Yes`.

- `Yes`: the attribute carries real test data and matters to the business. Mandatory fields such as `Make` and `Engine performance` belong here. These are the attributes that count when TestCases are designed and executed.
- `No`: descriptive information, or optional fields you still want to fill (`License plate number`) but whose failure should not stop a release. Not-business-relevant attributes can be ignored when TestCases are generated.
- `Result`: the attribute is used to verify something.

Two ways to set it:

1. Select the attribute and change **Business relevant** in the properties pane on the right (it is the second-to-last property in the list).
2. Select the attribute and click **Toggle Business Relevance** in the TestCase-Design ribbon. Each click cycles the value: `Yes` to `Result` to `No` and back to `Yes`.

The attribute icon changes colour with the value: dark red for `Yes`, a pale colour for `No`, green for `Result`. Set the property on sub-attributes as well, not only on the four top-level ones.

## Faster ways to fill a sheet

Creating every attribute by hand is fine for a small sheet. For a whole page there are shortcuts:

- **Drag a Module into the TestSheet.** Tosca creates one attribute per ModuleAttribute and fills instances from the values it knows for those controls (the entries of a dropdown, for example). Review the result: for free-text fields such as `Engine performance` the generated instances are not the values you want, and character, position and business relevance still have to be set by hand. See [Modules overview](/ToscaBase/modules/modules-overview/).
- **Create from the clipboard.** If the field structure is maintained in Excel, copy it and use the **Create element from clipboard** option on the sheet (or the equivalent option for instances). The copied cells must follow the structure Tosca expects.

:::note
The live-session speaker mentions both clipboard options only in passing and does not show the required cell layout. A related but different feature, importing a *folder* structure from Excel, is described in [Import from Excel](/ToscaBase/requirements-and-reporting/import-from-excel/).
:::

Attributes that repeat across several TestSheets should not be copied: put them into a class and reference it, see [Design classes](/ToscaBase/test-case-design/design-classes/).
