---
title: Business Parameters and TestStepLibraries
description: Group TestSteps into TestStepBlocks, move them into a TestStepLibrary as reusable TestStepBlocks referenced from many TestCases, and pass different data into each reference with Business Parameters.
level: 2
sidebar:
  order: 30
sources:
  - id: 5kWTxvxcfXQ
    title: "Tricentis Tosca Tutorial Part-8: Tosca Business Parameters,Tosca Library,Reusable TestStepBlocks"
    url: https://www.youtube.com/watch?v=5kWTxvxcfXQ
    at: "00:45"
  - id: nL1Vv11tBpA
    title: "Tosca Tutorial | Lesson 51 - Create TestStep Libraries | Reusable TestStep Blocks | Parameters |"
    url: https://www.youtube.com/watch?v=nL1Vv11tBpA
    at: "03:10"
  - id: QZBqWTOxYz4
    title: "TRICENTIS Tosca 16.0 - Lesson 14 | TestStep Library | Reusable TestStep Blocks | Create TC Library"
    url: https://www.youtube.com/watch?v=QZBqWTOxYz4
    at: "11:12"
  - id: s4dxVDt9tvA
    title: "TRICENTIS Tosca 16.0 - Lesson 16 | Create Business Parameters |  Use Business Parameters"
    url: https://www.youtube.com/watch?v=s4dxVDt9tvA
    at: "07:13"
---

Most suites repeat the same few actions in every TestCase: open the application, log in, create a record, log out. Tosca lets you keep such a sequence once, in a **TestStepLibrary**, and reference it from any TestCase as a **reusable TestStepBlock**. **Business Parameters** are the inputs of that block, so each reference can run it with its own data. A change to the block is made in one place and every reference follows, which shortens development and, above all, maintenance. Copying a whole TestCase and editing the copy is the alternative Tosca 16 lesson 14 warns against: after a property change both copies have to be fixed.

## The building blocks

| Term | Meaning |
|---|---|
| **TestStepBlock** | A folder inside a TestCase that groups TestSteps performing one task (login, logout, create record). It improves readability and reduces maintenance even without a library. |
| **TestStepLibrary** | A container for reusable TestStepBlocks. It can be created in any folder of the **TestCases** section, but a folder can hold **only one** library. Its icon is a TestCase folder marked with an **L**. |
| **Reusable TestStepBlock** | A TestStepBlock that lives inside a library. TestCases do not copy it; they hold a **reference** to it. |
| **Business Parameter** | A named input of a reusable TestStepBlock. The block uses the parameter instead of a literal, and each reference supplies the value. |

## Creating a library and a reusable block

1. In a multi-user workspace, check out the parent folder first ([Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/)).
2. Right-click the folder and choose **Create TestStepLibrary** (the entry with the L icon; shortcut **Ctrl+L**).
3. Put a block into the library in one of two ways:
   - **Create it new**: right-click the library, create a reusable TestStepBlock, give it a functional name (`Google Search`, `Login User`) and drag the TestSteps in from an existing TestCase.
   - **Convert an existing block**: drag a TestStepBlock, or the steps themselves, from a TestCase into the library. The steps move into the library and what remains in the TestCase turns into a reference, shown with an arrow icon.
4. Use the block elsewhere by dragging it from the library into a TestCase. The result is again a reference, not a copy: delete the duplicated steps from the other TestCase and drop the reference in their place.

In the second video, two TestCases, *login with valid user* and *login with invalid user*, share the steps `Open URL` and `Login User`. After conversion both cases reference the same two blocks and run exactly as before.

Blocks inside a library are listed **alphabetically**, not in execution order, so name them accordingly or accept that the order in the library says nothing about the flow.

### Worked example: a second checkout scenario

The Tosca 16 lesson builds a webshop TestCase that pays by credit card, then needs the same flow paying by check or money order, where only the payment step and the price check differ (a payment-method fee is added to the total). Every TestStepBlock of the first case is dragged into the library: `Precondition` (open URL, log in), `Order Product`, `Start Checkout`, `Checkout`, `Verification of Prices`, `Confirmation`, `Verification of Success`, `Postcondition` (log out). The new TestCase is assembled by dragging six of the eight blocks from the library; `Checkout` and `Verification of Prices` are dragged in too, but then edited, see the next section. The new payment screen needed a new Module and one more TestStep; the run in ScratchBook then verified the total of 40 (subtotal 25, shipping 10, fee 5).

## Editing a referenced block: Resolve Reference

A reference is not a copy. Editing the steps inside a referenced block edits the block **in the library**, and every TestCase that references it changes with it. That is the point when a control property changes (fix the login block once, all TestCases follow), and a trap when one TestCase needs a variation.

For a variation, right-click the referenced block in the TestCase > **Resolve Reference**. The block becomes an independent set of TestSteps in this TestCase (the reference suffix and arrow disappear), the library block and the other TestCases stay untouched, and you can change the payment method or the total formula freely. Always resolve first, then edit.

## Business Parameters

A reference to a block still carries the block's own values: both login cases would now log in with the same user. Business Parameters make the data an input.

1. Select the reusable TestStepBlock in the library and right-click > **Create Business Parameter Container** (in Tosca 16 the entry is offered on the block folder itself).
2. Inside the container create one parameter per value that should vary: `Username`, `Password`, `URL`, or `SearchText` in the Google example. Parameters need no value, ActionMode or data type; they are only names.
3. In the block's TestSteps **delete the hard-coded values first**, then **drag each parameter onto the TestStepValue** that should use it. The value now shows the parameter reference, written as `{PL[Username]}` (the syntax is spelled out in lesson 16: curly braces, `PL`, the name in square brackets). A password field keeps masking the value.
4. Go back to the TestCases. Every reference to the block now lists the Business Parameters with empty values; fill them per TestCase (`standard_user` in one, `locked_out_user` in the other, the same URL in both).

To run the same flow with another data set, copy the TestCase and change only the Business Parameter values in the copy; the library is not touched. This is what distinguishes Business Parameters from [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/): both are set per TestCase, but a Business Parameter feeds one reference to one block, so two references in the same TestCase can carry different data.

Values passed to a reference can themselves be parameters. The first video creates a Test Configuration Parameter `SearchText` = `Tricentis Tosca` on the TestCase and enters `{CP[SearchText]}` as the Business Parameter value, so that the search text is configured in the **Test Configuration** tab rather than in the step. The same works for a URL kept at folder level. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## When to use a library

- Identify the steps that are common to many TestCases and move only those into the library; the rest stays in the TestCase.
- Parameterise every value that differs between callers (user, URL, search text); leave constants inside the block.
- Combine libraries with TestCase-Design: a template can reference a reusable block and feed its Business Parameters from the TestSheet, see [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/).

## Related

- [Buffers](/ToscaBase/data-and-parameters/buffers/): values captured at run time, the third parameter type
- [TestCase structure](/ToscaBase/best-practices/test-case-structure/): grouping steps into folders
