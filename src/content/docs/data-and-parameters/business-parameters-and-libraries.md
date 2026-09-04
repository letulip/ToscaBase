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
---

Most suites repeat the same few actions in every TestCase: open the application, log in, create a record, log out. Tosca lets you keep such a sequence once, in a **TestStepLibrary**, and reference it from any TestCase as a **reusable TestStepBlock**. **Business Parameters** are the inputs of that block, so each reference can run it with its own data. A change to the block is made in one place and every reference follows, which shortens development and, above all, maintenance.

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

## Business Parameters

A reference to a block still carries the block's own values: both login cases would now log in with the same user. Business Parameters make the data an input.

1. Select the reusable TestStepBlock and choose **Create Business Parameter Container**.
2. Inside the container create one parameter per value that should vary: `Username`, `Password`, `URL`, or `SearchText` in the Google example. Parameters need no value, ActionMode or data type; they are only names.
3. In the block's TestSteps delete the hard-coded values and **drag each parameter onto the TestStepValue** that should use it. The value now shows the parameter reference, written as `{PL[Username]}`.
4. Go back to the TestCases. Every reference to the block now lists the Business Parameters with empty values; fill them per TestCase (`standard_user` in one, `locked_out_user` in the other, the same URL in both).

:::note
The speaker describes the reference as "PL followed by the parameter name"; `{PL[name]}` is the written form used here, by analogy with `{B[...]}` and `{CP[...]}`. Check what Tosca inserts when you drop the parameter.
:::

Values passed to a reference can themselves be parameters. The first video creates a Test Configuration Parameter `SearchText` = `Tricentis Tosca` on the TestCase and enters `{CP[SearchText]}` as the Business Parameter value, so that the search text is configured in the **Test Configuration** tab rather than in the step. The same works for a URL kept at folder level. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## When to use a library

- Identify the steps that are common to many TestCases and move only those into the library; the rest stays in the TestCase.
- Parameterise every value that differs between callers (user, URL, search text); leave constants inside the block.
- Combine libraries with TestCase-Design: a template can reference a reusable block and feed its Business Parameters from the TestSheet, see [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/).

## Related

- [Buffers](/ToscaBase/data-and-parameters/buffers/): values captured at run time, the third parameter type
- [TestCase structure](/ToscaBase/best-practices/test-case-structure/): grouping steps into folders
