---
title: Instances and combinatorics
description: Instances as attribute values and as TestCases, the Character and Position properties, and the four combinatorial methods (all combinations, orthogonal, pairwise, linear expansion).
level: 2
sidebar:
  order: 30
sources:
  - id: oCuNTr5nvPw
    title: "Tosca Tutorial | Lesson 53 - Create different Instances for Attributes | Test Case Design | Position"
    url: https://www.youtube.com/watch?v=oCuNTr5nvPw
    at: "00:01"
  - id: IPjsBUMM00k
    title: "Tosca Tutorial | Lesson 54 - Use Different Combinatorial methods to generate instances | Test Design"
    url: https://www.youtube.com/watch?v=IPjsBUMM00k
    at: "00:02"
  - id: R0zEbmFq0HE
    title: "Tosca Tutorial | Live Session | Test Case Designing | End-To-End | Real time Examples | Live Project"
    url: https://www.youtube.com/watch?v=R0zEbmFq0HE
    at: "24:51"
---

An **instance** is a value. Instances of an attribute are the variations that attribute has in the application: the attribute `Type of user` has the instances `Registered`, `New`, `Business`, `Technical`. Instances of the TestSheet itself are the TestCases: each one picks a value per attribute and appears as a column of the sheet. Tosca can create these TestCase instances for you with a **combinatorial method**, which is where the design techniques from the [overview](/ToscaBase/test-case-design/test-case-design-overview/) pay off. Attributes themselves are covered in [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/).

## Instances of an attribute

Right-click an attribute **> Create Instance** and name it with the value: `Smoke` and `Regression` for `Test cycle`, `1`, `2`, `3` for `Quantity`, `Credit card`, `Internet banking`, `UPI` for `Payment information`, `Success` and `Failure` for the verification `Message`. Instances cannot have sub-instances; only attributes nest. Include invalid values on purpose (an `Engine performance` of `12000` when the field accepts 1 to 2,000): negative scenarios come from invalid instances.

Adding instances to attributes does not change the number of TestCases in the sheet. That happens when you create instances of the sheet.

## Character and Position

Every instance has two properties that encode the design technique. The defaults are `Valid` and `Inner`.

**Character** has three values:

- `Valid`: no error is expected when this value is used.
- `Invalid`: an error is expected, and the error is the point of the TestCase. An invalid instance is not a TestCase that "should fail"; it verifies that the application rejects the input correctly.
- `Straight through`: the happy path. The value most customers use, with the fewest dependencies, easy to implement, and carrying the highest business risk. In the *Vehicle Insurance* sample that is the default make, four seats, petrol. Straight-through instances should always pass; when time is short, execute only them and the high-risk functionality is covered. Every attribute should have one straight-through instance, and the linear-expansion method below requires it.

**Position** has two values:

- `Boundary`: the value sits on the edge of a valid range. For a quantity of 1 to 10, `1` and `10` are boundaries.
- `Inner`: any value inside the range that is not immediately at a boundary, such as `2` to `9`.

Values outside the range (`0`, negatives, `11`, `12`) are invalid inputs; the Lesson 53 speaker refers to them as lower and upper boundary values, but their character is `Invalid`.

Set the properties in the properties pane, or select the instance and click **Toggle Character** / **Toggle Position** in the TestCase-Design ribbon. Toggle Character cycles through `Valid`, `Invalid` and `Straight through`; the instance icon changes with each value. When the character is `Straight through`, Tosca sets the position to `Inner` and makes it read-only.

## Instances of the TestSheet: the TestCases

1. Right-click the TestSheet **> Create Instance**. Each sheet instance becomes a column. Name them `Test case 1`, `Test case 2`, ..., or better with the requirement id, Jira id or TestCase id; a sheet can hold hundreds of them.
2. In each column choose a value for every attribute. The cell (or the details pane) offers a dropdown with the instances of that attribute: `Smoke` or `Regression` for the cycle, `Registered` or `New` for the user, a quantity, a payment method, `Success` or `Failure` for the expected message.
3. Give each column a different business flow: one straight-through case with the happy-path values, valid cases with other data, an invalid case with an out-of-range value.

The chosen values are what drive the generated TestCase: whatever `Make` a column selects is the value the TestCase enters in the application. Make sure every attribute has a value in every column.

## Generate instances with a combinatorial method

Instead of filling columns by hand, right-click the TestSheet **> Generate Instances** and pick a method. The generated columns take their names from the instance values; rename them if you like. Existing instances can be selected and deleted first.

| Method | What it does | Example counts |
|---|---|---|
| **All combinations** | Every possible combination of all instances of all attributes. The highest number of TestCases; complete but usually impossible to execute. | 3 hand-made cases became 972. On the *Vehicle Insurance* sheet with Module-generated instances the run stopped: 77,760 instances exceed the limit of 1,000. |
| **Orthogonal** | The fewest combinations: each instance value is used just once, with at least one value of every attribute in every TestCase. | 3 existing cases plus 3 generated, 6 in total. |
| **Pairwise** | Every pair of values of any two attributes appears in at least one TestCase. More than orthogonal, far fewer than all combinations. | 16 TestCases. |
| **Linear expansion** | Starts from the straight-through combination and expands it. Contains the highest-risk cases and yields the optimum number, "not too high, not too low". Recommended by Tricentis. | 16 TestCases, similar to pairwise on the same sheet. |

Linear expansion fails with an error if any attribute has no straight-through instance. Set one per attribute (there is no automatic way, whether the attributes were created by hand or from a Module), then run it again.

:::note
The 1,000-instance limit in the live session was reported by Tosca itself; the speaker said it is a project property but did not show where. The same speaker mentioned a fifth entry in the Generate Instances menu, an extension "using the relation concept", without explaining it. Treat both as unverified.
:::

:::tip
Use all combinations only when you really have the time to execute everything. For a regression sheet, start with linear expansion; the straight-through instances it requires are worth defining anyway, because they are the cases you run first when a release is due.
:::

The sheet is now designed. The next step is to link it to a TestCase template and let Tosca generate the TestCases: [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/).
