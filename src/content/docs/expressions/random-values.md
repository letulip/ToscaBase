---
title: Random values
description: Generate random numbers, decimals and strings in TestStepValues with RND, RNDDECIMAL and RANDOMTEXT, and handle random values the application produces.
level: 2
sidebar:
  order: 10
sources:
  - id: d7s1tQfLlMk
    title: "Tosca Tutorial | Lesson 34 - Generate Random Values | Test Steps | Random Expressions |"
    url: https://www.youtube.com/watch?v=d7s1tQfLlMk
    at: "01:03"
  - id: BVuIulDDDpA
    title: "Tosca Tutorial | Lesson 117 - Add Random Numbers | Math Expression | SendKeys | Obstacle 11 |"
    url: https://www.youtube.com/watch?v=BVuIulDDDpA
    at: "03:20"
  - id: 9-nRnS3-lPM
    title: "Tosca Tutorial | Lesson 119 - Extract Random Numbers | Regex | Named Group | Obstacle 13 |"
    url: https://www.youtube.com/watch?v=9-nRnS3-lPM
    at: "03:23"
  - id: KyyPVKyA60A
    title: "Tosca Tutorial | Lesson 137 - Select Random Combo Box Item | Random Text | Buffer | Obstacle 31 |"
    url: https://www.youtube.com/watch?v=KyyPVKyA60A
    at: "02:16"
---

A TestStepValue does not have to be a fixed string. Tosca ships a set of dynamic expressions, written in curly braces, that generate a new random integer, decimal or string on every run. This makes a TestCase reusable for registration forms, unique IDs and any field that rejects duplicate data. The second half of this page covers the reverse problem: the *application* produces a random value and the TestCase has to read it back, calculate with it or select it.

## Generator expressions

Every expression is typed into the **Value** column of a TestStep. As soon as you type `{`, Tosca opens an autocomplete list of the available expressions; pick one or type its name, then add the arguments in square brackets and close the brace. After pressing Enter a valid expression is shown highlighted in the value cell.

| Expression | What it generates | Example |
|---|---|---|
| `{RND[length]}` | An integer of the given number of digits, without limits. Any length works (the video names 9, 10, 50, 100). | `{RND[10]}` for a 10-digit telephone number |
| `{RND[lower][upper]}` | An integer between a lower and an upper limit. | `{RND[1000][10000]}` |
| `{RNDDECIMAL[length][decimal places]}` | A number of the given length with the given number of decimal places (2, 3, 4...). | `{RNDDECIMAL[5][2]}` |
| `{RNDDECIMAL[decimal places][lower][upper]}` | A decimal number with the given number of decimal places, inside a range. | `{RNDDECIMAL[2][1000][10000]}` |
| `{RANDOMTEXT[length]}` | A random string of the given length, mixing letters and digits. | `{RANDOMTEXT[5]}` |

The speaker also mentions that a string with a timestamp can be generated, but does not show it; see [Date expressions](/ToscaBase/expressions/date-expressions/) for `DATETIME`.

:::note
If a value is not highlighted after you press Enter, the expression is malformed. Use **Translate value** (below) to confirm what Tosca will actually produce.
:::

## Checking what an expression produces

Right-click the TestStepValue and choose **Translate value**. Tosca shows the concrete value it would generate for that expression: a five-character mix of letters and digits for `{RANDOMTEXT[5]}`, a ten-digit number for `{RND[10]}`. This is the fastest way to validate an expression before running the TestCase.

## Worked example: registering an account

The example TestCase fills a registration form (first name, last name, e-mail, telephone, password, confirm password, a newsletter radio button, a privacy-policy checkbox and a **Continue** button).

1. Create a TestCase folder for the application and two TestCases: `Open application` (an `OpenUrl` standard Module with the URL, ActionMode **Input**, plus a Test Configuration Parameter `Browser` = `Chrome`) and `Register account`.
2. Scan the registration page into a new Module and drag the Module onto `Register account`. Press **Ctrl+T** on a TestCase to search all Modules in the workspace instead of browsing the Modules section.
3. Set the values:
   - First name: `{RANDOMTEXT[5]}`
   - Last name: `{RANDOMTEXT[5]}`
   - E-mail and password: static values (the video enters a fixed e-mail and password)
   - Telephone: `{RND[10]}`
   - Radio button: click; checkbox: `true`/`false`; Continue button: click
4. Run in ScratchBook. The log shows a different generated name and telephone on each run.

The run in the video then fails on the radio button with *more than one control found*: two controls share the same identification properties. That is a Module problem, not an expression problem; fix it by rescanning the Module and picking a unique property (see [Rescan Modules](/ToscaBase/modules/rescan-modules/) and [Control identification](/ToscaBase/modules/control-identification/)).

:::tip
A random *password* has to be typed twice (password and confirm password) with the same value, so a plain `{RANDOMTEXT[8]}` in each field would not match. The video defers this case; the pattern is to generate the value once, store it in a [Buffer](/ToscaBase/data-and-parameters/buffers/) and reuse the buffer in both fields.
:::

## Random values produced by the application

Three obstacle-course scenarios show how to consume random data instead of generating it. All of them rely on the **Buffer** ActionMode (see [ActionModes](/ToscaBase/test-cases/action-modes/)).

### Read two random numbers and add them (MATH, SENDKEYS)

The page shows two randomly generated numbers and expects their sum in a text box.

1. Scan the two number elements and the result field; rename the ModuleAttributes to `num1`, `num2` and `result`.
2. For `num1` and `num2` set ActionMode **Buffer**, buffer the `InnerText` property and give each buffer a name.
3. In `result` do not write `{B[num1]}+{B[num2]}`: a bare `+` between two buffers returns no result. Arithmetic has to go through the math expression: `{MATH[{B[num1]}+{B[num2]}]}` (operands are the buffers, the operator is `+`; subtraction, multiplication and division work the same way).
4. The sum is entered correctly, but the obstacle is still not marked complete, because the page expects key-by-key typing. Wrap the same expression in **SendKeys** so Tosca emulates a user typing: `{SENDKEYS["{MATH[{B[num1]}+{B[num2]}]}"]}`. With SendKeys the obstacle completes.

Set the TestCase Workstate to **Completed** before running from ScratchBook, as the video does each time.

### Buffer random text and select it in a combo box

A button generates a random string that is also one of the entries of a select box; the TestCase has to pick the matching entry and submit.

| TestStep | ModuleAttribute | ActionMode / value |
|---|---|---|
| Click random button | Generate random text button | click (`X`) |
| Buffer random text | Text box | **Buffer**, value `RND` (the buffer name) |
| Select random text | Select box | **Select**, value `{B[RND]}` |
| Click submit | Submit button | click (`X`) |

The Module is dragged in four times, one TestStep per action, and every TestStep is renamed. The speaker's recommendation: keep a single action or value per TestStep.

### Extract several random numbers from a random string (named groups)

Clicking the first edit box reveals a random sentence containing three large numbers, which must be entered into three other boxes. Buffering the whole text is not enough; the numbers are extracted with a regular expression and **named groups**, each group storing its match in a buffer:

```
{REGEX[^.*(?<number1>[0-9]+).*(?<number2>[0-9]+).*(?<number3>[0-9]+).*$]}
```

Each `(?<name>...)` group stores its match in the buffer of that name; the named-group syntax is explained in [Extracting parts of a value with named groups](/ToscaBase/expressions/intervals-and-verification-expressions/#extracting-parts-of-a-value-with-named-groups). Here the groups are separated by `.*` to swallow the surrounding text and the pattern is anchored with `^` and `$`. As there, the TestStep must use ActionMode **Verify** ("input is not supported for regex values").

The three boxes are then filled with `{B[number1]}`, `{B[number2]}` and `{B[number3]}`.
