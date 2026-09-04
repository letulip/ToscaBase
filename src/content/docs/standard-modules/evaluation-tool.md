---
title: Evaluation tool
description: TBox Evaluation Tool compares two dynamic expressions (buffers, Test Configuration Parameters, literals) with a true/false result; use it for verifications and as an If condition, quoting the operands.
level: 2
sidebar:
  order: 40
sources:
  - id: IkPL7G4QR7k
    title: "Tosca Tutorial | Lesson 16 - Using TBox Evalutation Tool | Compare Dynamic Expressions|"
    url: https://www.youtube.com/watch?v=IkPL7G4QR7k
    at: "00:10"
  - id: 2sbIUWs5wcI
    title: "Tosca Tutorial | Lesson 126 - Random Mathematical Operations | Evaluation Tool | Obstacle 20 |"
    url: https://www.youtube.com/watch?v=2sbIUWs5wcI
    at: "04:19"
---

**TBox Evaluation Tool** is a Standard Module in the *expression evaluation* group of the Standard subset. It evaluates a comparison and returns true or false: true passes the step, false fails it. It has a single ModuleAttribute, **Expression**, whose ActionMode is `Verify` by default because the step is a verification. The expression holds two values and a comparison operator (`==`, `!=`, `<`, `>` and so on), and each value can be any dynamic expression: a buffer against another buffer, a buffer against a Test Configuration Parameter, a buffer against a literal or a computed expression. That makes it the general-purpose comparison step in Tosca, and, placed inside an `If`, its multi-way branch.

## Comparing a buffer with a Test Configuration Parameter

Scenario: on the demo web shop, click Login, log in with an email and password stored as Test Configuration Parameters (TCPs), and verify that the username is displayed on the page.

### The usual way

A TestStep on the username control with ActionMode `Verify` and the value `=={CP[username]}` compares the control's inner text with the TCP. This works and the log shows expected and actual values.

### With the Evaluation Tool

1. Disable the old verification step: right-click the step and choose **Disable**. Tosca asks for a reason (optional) and records the timestamp and the user who disabled it.
2. Add a TestStep on the Module for the username control, ActionMode `Buffer`, buffer name `email`. Place it before the comparison.
3. Add **TBox Evaluation Tool**, rename it `Compare email`, and enter the expression `{B[email]}=={CP[username]}`.
4. Run. The step **fails** with a log message about a *missing end of file*. The values contain special characters that break the expression parser.
5. Put quotes around both operands: `'{B[email]}'=='{CP[username]}'`. Run again: the TestCase logs in, the Evaluation Tool evaluates to true, the buffer `email` is visible with its value, and the logout step confirms the scenario passed.

:::tip
Always wrap the operands of an Evaluation Tool expression in **single quotes**. It escapes special characters in the values and is the fix for the "missing end of file" error. The same rule applies when the expression is used as an `If` condition.
:::

The scenario is one of the most common in web automation, and both ways solve it; the Evaluation Tool version is more dynamic because either side of the comparison can be swapped for any expression without touching the Module.

## As an If condition: randomised arithmetic

An automation obstacle shows two random numbers and a random operator (`+`, `-`, `*` or modulo); a page refresh changes all three. The test must compute the result and type it into a result box. Any programming language would use a `switch`/`case`; Tosca has no switch, so the pattern is one `If` per operator with an Evaluation Tool as the condition.

### Module

Scan the page into a Module with four controls: first number, operator, second number, result field. Because the numbers and the operator change on every load, **rename the ModuleAttributes** to stable names (`Num1`, `Operand`, `Num2`, `Result`); otherwise the TestCase shows the values captured at scan time. See [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/).

### TestCase

1. **Buffer values.** One TestStep with ActionMode `Buffer` on `Num1`, `Operand` and `Num2`.
2. **If (addition).** Add an `If` statement. Its condition is a **TBox Evaluation Tool** step whose expression compares `'{B[Operand]}'` with `'+'`.
3. **Then.** A TestStep that enters into `Result` a math expression adding `{B[Num1]}` and `{B[Num2]}`.
4. Copy the `If` block three times, changing only the operator in the condition (`-`, `*`, the modulo sign) and inside the math expression.
5. Set the Workstate to Completed and run several times. Each run buffers different values, exactly one `If` matches, and the result box receives the right value.

:::note
The transcript says the condition checks whether the buffer "equals" the sign; `==` is the operator shown in Lesson 16, so that is the safe choice. The math expression is referred to only as "the math expression"; its syntax is covered in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).
:::

Four sequential `If` blocks are not elegant but are the only way to express a multi-way branch in Tosca. The result is effectively an automated calculator.

## Related

- [Control flow](/ToscaBase/test-cases/control-flow/) for `If`, `Do` and `While`
- [Buffer operations](/ToscaBase/standard-modules/buffer-operations/)
- [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)
- [Random values](/ToscaBase/expressions/random-values/)
