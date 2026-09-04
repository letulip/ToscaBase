---
title: TestCase structure
description: Four structural rules for a maintainable TestCase - always verify something, group TestSteps into folders, prefer Repetitions and Constraints over loops, and keep the Workstate current.
level: 3
sidebar:
  order: 20
sources:
  - id: rRLn2RFyN14
    title: "Tosca Tutorial | Lesson 98 - Use Verification Points in Test Cases | Best Practices |"
    url: https://www.youtube.com/watch?v=rRLn2RFyN14
    at: "00:40"
  - id: oa8weD5auAY
    title: "Tosca Tutorial | Lesson 103 - Test Steps should be grouped into different folders | Best Practices |"
    url: https://www.youtube.com/watch?v=oa8weD5auAY
    at: "00:50"
  - id: a_npDSmS95s
    title: "Tosca Tutorial | Lesson 102 - Loops should be avoided in Test Cases | Best Practices |"
    url: https://www.youtube.com/watch?v=a_npDSmS95s
    at: "00:45"
  - id: IAXhQvwRuuk
    title: "Tosca Tutorial | Lesson 105 - Set Proper Workstates for Test Cases | Best Practices |"
    url: https://www.youtube.com/watch?v=IAXhQvwRuuk
    at: "00:35"
---

A TestCase that merely clicks through an application is not a test. Tricentis' best practices add four structural rules on top of [naming conventions](/ToscaBase/best-practices/naming-conventions/): every TestCase needs at least one verification point, TestSteps belong in folders, loops should give way to Repetitions and Constraints, and the Workstate must reflect where the TestCase really is. Each rule targets a concrete failure mode: false positives, slow debugging, fragile execution, and wrong requirement coverage.

## Always include a verification point

Without a verification the expected result is never compared with the actual result, so the TestCase can only produce a false positive. Tosca checks that each control can be found and steered; once the last step succeeds, the TestCase passes regardless of what the application did. A login TestCase that enters credentials and clicks **Login** passes even when the login fails and an error page appears.

The fix is a TestStep with ActionMode `Verify` on something that proves the outcome. For a login, verify that the `Logout` link is visible (`Visible` with value `True`, ActionMode `Verify`). In the ExecutionLog this produces an explicit verification entry with expected and actual values; when the link is missing the TestCase fails, which is exactly what you want, because a failure is what gets a defect logged.

Verification points are also what tie a TestCase to its requirements: whatever the manual test validates becomes a `Verify` step in the automated one. A TestCase may have several; it must have at least one. ActionModes are explained in [ActionModes](/ToscaBase/test-cases/action-modes/).

## Group TestSteps into folders

TestSteps placed flat under a TestCase hide the flow. Nobody can see where the login is, where the shopping cart starts, or which of three checkouts failed, and debugging means reading every step. Folders make the TestCase readable and make navigation from a failed ExecutionList entry back to the responsible steps immediate: the folder name tells you which functionality broke.

The recommended shape:

1. **Three top-level folders.** `Pre-processing` for prerequisites (open the URL, log in), `Processing` for the actual scenario, `Post-processing` for cleanup and logout.
2. **Sub-folders inside `Processing`** for one page or one functionality each: `Register user`, `Login user`, `Add products to cart`, `Shopping cart`, `Checkout` (with billing address, shipping address, shipping method), `Confirm order`, `Verify PDF order information`.
3. **Nest freely.** A Repetition folder or a condition folder can sit inside a functional folder; if a folder grows too long, split it again.

To create one, right-click the TestCase or a folder and add a folder, then drag the steps in. The structure follows naturally if Modules are also categorised by page (see [Module hygiene](/ToscaBase/best-practices/module-hygiene/)).

## Prefer Repetitions and Constraints over loops

Tosca offers `Do`, `While` and `If` (see [Control flow](/ToscaBase/test-cases/control-flow/)), but Tricentis recommends minimising their use. Tosca is not a programming language: loops are slow, add complexity that the tool handles poorly, and raise the chance of failure. Two built-in mechanisms cover the usual cases:

- **Repetition instead of a counting loop.** The source shows a `While` loop that sets Buffer `X` to `1`, verifies `X < 5` and increments `X` on each pass; the execution shows five iterations before the condition evaluates to false. The same result comes from putting the calculation step in a folder and setting the folder's **Repetition** property to `5`. One property replaces the verification step and the loop. See [Repetitions](/ToscaBase/test-cases/repetitions/).
- **Constraints instead of iterating a table.** To find a cell in a web table, do not loop over rows and columns comparing values. Set ActionMode `Constraint` on the identifying columns (first name and last name in the example) and `Verify` on the target cell; Tosca locates the row that satisfies both constraints directly. See [Table controls](/ToscaBase/modules/table-controls/).

Keep loops for the cases these two cannot express. The goal is a TestCase that is simpler, faster and easier to maintain.

## Set the Workstate

Every TestCase has a **Workstate** column (enable it through the column chooser if it is hidden) with three values:

| Workstate | Meaning |
|---|---|
| `Planned` | Scenario is being analysed; the TestCase is not built yet |
| `In Work` | The TestCase is being built or changed |
| `Completed` | The TestCase is finished and ready for use |

Setting it correctly matters for two reasons. In a team, colleagues working in the same folder can see what is done and plan around it, and management gets an overview of progress. More importantly, Workstate feeds the Requirements section, which is the dashboard test management and stakeholders look at. In the source, a requirement showed **Coverage specified** 100% and **Execution state** 97%; switching its linked TestCase from `Completed` to `In Work` dropped those to 69% and 65%, because that TestCase had a contribution of 54.77% to the requirement. Setting it back to `Completed` restored the figures. A forgotten Workstate therefore misreports coverage for the whole project. See [Requirements and risk](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

:::tip
Combine Workstate with the folder-based [review process](/ToscaBase/best-practices/review-process/): a TestCase moves to `Completed` only after review.
:::
