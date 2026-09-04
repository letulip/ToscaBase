---
title: Templates and instantiation
description: Convert a TestCase into a template, link it to a TestSheet through the schema path, check it, instantiate it into generated TestCases, make TestSteps conditional and reinstantiate after changes.
level: 2
sidebar:
  order: 40
sources:
  - id: ZPQqBvTdJew
    title: "Tosca Tutorial | Lesson 55 - How to create a Test Case Template | Dynamic Test Case Generation|"
    url: https://www.youtube.com/watch?v=ZPQqBvTdJew
    at: "00:01"
  - id: r0QVA5jM7m0
    title: "Tosca Tutorial | Lesson 56 - Dynamically Generate Test Cases with Template Instance | Instantiation"
    url: https://www.youtube.com/watch?v=r0QVA5jM7m0
    at: "00:01"
  - id: YOvThZyYOaM
    title: "Tosca Tutorial | Lesson 57 - Use condition in Test Case Instantiation | Test Case Templates |"
    url: https://www.youtube.com/watch?v=YOvThZyYOaM
    at: "00:02"
  - id: VeG0TLkQM8g
    title: "Tricentis Tosca Tutorial Part-10 : Tosca Test Case Design, Tosca Class"
    url: https://www.youtube.com/watch?v=VeG0TLkQM8g
    at: "07:15"
  - id: R0zEbmFq0HE
    title: "Tosca Tutorial | Live Session | Test Case Designing | End-To-End | Real time Examples | Live Project"
    url: https://www.youtube.com/watch?v=R0zEbmFq0HE
    at: "41:17"
---

A **TestCase template** is the bridge between a designed TestSheet and concrete TestCases. When several TestCases share the same sequence of TestSteps and differ only in data, you model the sequence once as a template, link it to a data source, and let Tosca **instantiate** it: one generated TestCase per TestSheet instance, with that instance's values. A TestSheet cannot be linked to a plain TestCase; the template is mandatory. Designing the sheet is covered in [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/) and [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/).

## Convert a TestCase into a template

1. Build the TestCase as usual. The Lesson 55 example, `Validate login`, has four steps: open the URL (taken from a Test Configuration Parameter), `Login user` (username, password, login button), `Validate error message` (the error field in ActionMode `Verify`), and a `TBox Window Operation` that closes the browser.
2. Check the TestCase out if the workspace is multi-user.
3. Right-click the TestCase **> Convert to Template**. A `T` symbol on the icon marks it as a template. A template cannot be executed; it exists for generating TestCases.

Right-click **> Convert to TestCase** turns a template back into a normal TestCase.

Two properties matter on a template:

- **Schema path**: the data source that defines the template's schema. It can be a TestSheet from the TestCase-Design section or an Excel sheet. Once linked, the property shows the sheet name.
- **Instance name**: the naming pattern for generated TestCases. By default they are named after the TestSheet instances; the live-session speaker entered a pattern beginning with `TC` and, after reinstantiation, every generated TestCase followed it.

## Link the TestSheet

Drag the TestSheet from the TestCase-Design section and drop it onto the template. That sets the schema path, and the sheet becomes the template's **schema definition**. To confirm the link, right-click the template **> Jump to Schema Definition**: Commander opens the linked sheet.

**Check Template** (ribbon or context menu) validates the template against the schema: it compares the names used in the template with the attribute names of the sheet, and also checks conditions, properties and Test Configuration Parameters. Run it every time you link a sheet or change the template. The result is either `No errors found in template` or a list of errors. **Edit schema path** opens a wizard to switch the template to another data source.

## Map TestStepValues to attributes

When the sheet is linked, Tosca fills every **empty** TestStepValue whose ModuleAttribute name matches a sheet attribute with a reference into the sheet, for example `Process.Username` and `Process.Password` under the `Login user` step. Values that already contain something are left alone. To map those, and any value whose name does not match:

- **Drag the attribute** from the TestSheet into the Value cell of the TestStepValue, or
- **Type the reference**: start typing the `XL` reference with a dot or opening bracket and Tosca offers the attributes of the linked sheet to pick from, for example `Verification.Message` for the error field that should be verified.

Replace every hard-coded value this way; a template with constants produces identical TestCases.

:::note
Neither video spells the typed syntax out: Lesson 55 only says "Excel dot ... square bracket" before the attribute list appears, and the live session calls it "this Excel link". What is certain is the shape: an `XL` reference, square brackets, `Attribute.SubAttribute` inside. Prefer the drag-and-drop method.
:::

Values that come from a class reference are mapped the same way as sheet attributes ([Design classes](/ToscaBase/test-case-design/design-classes/)).

## Instantiate

1. Run **Check Template** once more.
2. Right-click the template **> Create Template Instance**, or select it and click **Instantiate** in the TestCases ribbon (both do the same; there is a keyboard shortcut as well).
3. Confirm the *Start instantiation* dialog with **Yes**.

Tosca creates a folder under the template with one generated TestCase per TestSheet instance: two instances in the sheet give two TestCases, hundreds give hundreds. Each TestCase carries its column's data. In the login example the first TestCase logs in as `standard_user` and has no error to verify because the `Message` cell was left empty; the second uses `locked_out_user` and verifies the lock-out message. The generated names can be edited.

Drag the instance folder into an ExecutionList to run the TestCases ([Execution lists](/ToscaBase/execution/execution-lists/)).

## Reinstantiate after changes

Generated TestCases do not follow later edits by themselves. After you change the template (Lesson 56 switches the password value's data type from `String` to `Password` so that it is masked) or the TestSheet (new values, new columns), right-click the template instance folder **> Reinstantiate Instance** (also in the ribbon). The TestCases are regenerated and all of them pick up the change; no manual editing per TestCase. This is what makes maintenance cheap: one edit in the sheet or the template, one reinstantiation.

## Conditions: steps that exist only in some instances

Without conditions, every generated TestCase has every TestStep of the template. In the login example the valid `standard_user` TestCase still contains the `Validate error message` step; with an empty value it does nothing at execution, but it clutters the TestCase and confuses whoever reads it. When a template grows to many steps, the flow of each instance should follow business logic instead: a step is part of an instance only when a condition on the sheet data holds.

1. In the template, open the **Column Chooser** and add the **Condition** column (double-click it or drag it into the header).
2. Select the TestStep that should be conditional (`Validate error message`) and fill its Condition cell. The recommended way is drag and drop, not typing: open the TestSheet, expand the instances of the attribute the logic depends on (`Process.Username`), and drag the instance `locked_out_user` into the cell. Tosca writes the condition itself: `Process.Username == locked_out_user` (the speaker reads the generated text aloud as "process dot username equals equals locked out user"). Typing the same text is possible but error-prone.
3. The step's icon changes: a conditional TestStep shows the two arrows with two dots; an unconditional one shows plain arrows.
4. **Reinstantiate** the instances. The step is now present only in TestCases whose column satisfies the condition: the locked-out TestCase keeps `Validate error message`, the standard-user TestCase loses it.

The condition can be phrased either way round: *username equals locked_out_user* to include the step for the error case, or *username not equals standard_user*. Conditions work on folders too, so a template can hold alternative branches and each instance gets only the branch its data selects. That pattern, on the *Vehicle Insurance* sample, is in [Worked example: end-to-end live project](/ToscaBase/troubleshooting/worked-example-live-project/), step 2.
