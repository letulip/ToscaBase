---
title: Intervals and verification expressions
description: Verify a value within a numeric range with INTERVAL, use regular expressions in ModuleAttributes and Verify steps for multilingual identification, and split a value into buffers with named groups.
level: 2
sidebar:
  order: 40
sources:
  - id: Ul3ZN1FKw2E
    title: "Tosca Tutorial | Lesson 37 - Use Intervals to verify values within a specific range | Verify Action"
    url: https://www.youtube.com/watch?v=Ul3ZN1FKw2E
    at: "01:10"
  - id: hBRAnB_3iBc
    title: "Tosca Tutorial | Lesson 35 - Multilingual Testing | Multiple Languages | Regular Expressions |"
    url: https://www.youtube.com/watch?v=hBRAnB_3iBc
    at: "04:12"
  - id: LeSc28YnTTk
    title: "Tosca Tutorial | Lesson 140 - Common RealTime Tosca Problems & Fixes | Regular Expression | Buffers|"
    url: https://www.youtube.com/watch?v=LeSc28YnTTk
    at: "02:18"
  - id: 9-nRnS3-lPM
    title: "Tosca Tutorial | Lesson 119 - Extract Random Numbers | Regex | Named Group | Obstacle 13 |"
    url: https://www.youtube.com/watch?v=9-nRnS3-lPM
    at: "03:23"
  - id: HzsNAXGMSlY
    title: "TRICENTIS Tosca 16.0 - Lesson 33 | Multi Language Testing | Regular Expressions"
    url: https://www.youtube.com/watch?v=HzsNAXGMSlY
    at: "08:32"
  - id: gWrv7f6Sqtc
    title: "TRICENTIS Tosca 16.0 - Lesson 34 | INTERVALS Syntax in Verify Action Mode | INTERVALS"
    url: https://www.youtube.com/watch?v=gWrv7f6Sqtc
    at: "02:15"
---

An exact string is not always the right way to identify a control or to verify a value: a discount only has to fall in a range, a page title changes with the UI language, a transaction ID is only partly predictable. Tosca accepts two families of expressions wherever a value is compared: **intervals**, which verify that a number lies within a range, and **regular expressions**, which match patterns in identification properties of a ModuleAttribute and in TestStepValues with the **Verify** ActionMode. With *named groups* a regular expression also cuts the matched text into pieces and stores each piece in a Buffer.

## Intervals: verifying a value within a range

Intervals only work with the **Verify** ActionMode, on numeric or string data types, and with the operators `==` and `!=`. Instead of a fixed expected value, the TestStepValue defines a base and how far the actual value may deviate from it. Typing `{INTERVAL` in the value cell shows Tosca's description, the syntax and an example.

| Type | Syntax | Valid range | Example |
|---|---|---|---|
| Simple interval (equal boundaries) | `{INTERVAL[base][limit]}` | base − limit to base + limit | `{INTERVAL[10][5]}` passes for any value from 5 to 15 |
| Custom interval (different boundaries) | `{INTERVAL[base][lower boundary][upper boundary]}` | base − lower boundary to base + upper boundary | `{INTERVAL[10][6][5]}` passes for 4 to 15 |

Tosca's own description uses base 100: a limit of 25 gives 75 to 125; a lower boundary of 10 and an upper boundary of 50 give 90 to 150.

Worked example, from the Tricentis vehicle insurance sample application: after vehicle, insurance and product data are entered, the *Select price option* screen shows a table of plans (silver, gold, platinum, ultimate) with a *claims discount* row. The discount changes with the data the user enters but always stays between 0 and 10, so verifying a static `5` would break the TestCase.

1. Drag the scanned `Select price option` table Module into the TestCase.
2. In the column choose `Platinum`; identify the row cell by typing the complete text of the row label instead of the cell index, so the TestStep addresses the claims-discount cell.
3. First run with ActionMode **Buffer** into `B_discount` to confirm the cell is read correctly; the log shows the buffer holding `5`.
4. Copy the TestStep, set ActionMode **Verify** and the value `{INTERVAL[10][5]}` (simple interval), then another copy with `{INTERVAL[10][6][5]}` (custom interval, 4 to 15; Lesson 37 uses `{INTERVAL[10][5][5]}`). Both verifications pass. As soon as you click away from a valid expression the cell shows it highlighted; if it stays plain text a bracket is missing.

:::note
An interval verification does not write a line to the log info; a passed TestCase is the confirmation that the value was inside the range. Both lessons state that intervals also apply to strings but demonstrate only numbers.
:::

## The REGEX expression

```
{REGEX["pattern"]}
```

Type `{`, choose `REGEX` from the autocomplete list, open a square bracket, put the pattern in double quotes, and close the bracket and the brace. Lesson 33 omits the quotes (`{REGEX[pattern]}`) and the run passes as well. Tosca's own description of the expression adds the form for extracting text:

```
{REGEX[expression(?<BufferName>subexpression)expression]}
```

The expression as a whole verifies that the text matches the pattern; each `(?<BufferName>subexpression)` is a named group whose match is saved to the buffer of that name. The buffer name is free; the sub-expression describes the dynamic part.

| Regex element | Meaning (as used in the videos) |
|---|---|
| `^` ... `$` | Start and end of the text |
| `.*`, `.*?` | Any characters, any number of them (greedy, or lazy: as few as possible) |
| `\|` | Alternative: either the left or the right pattern |
| `[0-9]+` | One or more digits |
| `[A-Z]*` | Any number of upper-case letters |
| `\d{3}` | Exactly three digits |
| `\d*` | Any number of digits (the rest of a number) |
| `(?<name>...)` | Named group; the match is stored in buffer `name` |

## Multilingual identification with alternatives

A site offered in English and French keeps the same layout, but the page title and the link texts change with the language. A control with a language-independent property such as an ID keeps working; the *Cameras* link in the example is identified by `InnerText` and tag only, so switching the site to French breaks both the Module's page title and the link.

Instead of one Module per language, put both texts into one regular expression with `|` and use it in the identification property:

| ModuleAttribute property | Value |
|---|---|
| Page title (Module) | `{REGEX["Cameras from Nikon.*\|Appareils photo.*"]}` |
| `InnerText` of the Cameras link | `{REGEX["Cameras\|Appareils photo.*"]}` |

Each alternative keeps only the constant part of the text and ends with `.*`, so trailing text may change. The same pattern extends to any number of languages: add one alternative per language for every control whose text is translated. The TestCase (`Click cameras`, one Module, click the link) then passes with the site in French and again in English.

The same technique works for a whole text block (Lesson 33, moodle.org in English and Dutch): a description paragraph is identified by its full `InnerText` and verified with `Exists == true` before a link is clicked. Switching the site to Dutch fails the verification until the `InnerText` becomes `{REGEX[English paragraph|Dutch paragraph]}`, with the Dutch text copied from the browser's inspect pane; the TestCase then passes in both languages.

:::note
The French link text is only shown on screen in Lesson 35; `Appareils photo` is the standard French wording for *Cameras*. Check the exact strings (in Chrome: inspect, search for `title` or the element's inner text) on the page you automate.
:::

## Extracting parts of a value with named groups

A transaction ID such as `IN` + a bank abbreviation + a three-digit number + more digits has to be split into four buffers for later verification steps.

1. `TBox Set Buffer`: buffer `trans` = the transaction ID.
2. Second `TBox Set Buffer` on the *same* buffer name `trans`, with the regular expression as the value and ActionMode **Verify**:

   ```
   {REGEX[(?<part1>IN)(?<part2>[A-Z]*)(?<part3>\d{3})(?<part4>\d*)]}
   ```

| Group | Sub-expression | Buffer holds |
|---|---|---|
| `part1` | `IN` | The static prefix |
| `part2` | `[A-Z]*` | The letters before the first digit, however many |
| `part3` | `\d{3}` | Exactly the next three digits |
| `part4` | `\d*` | All remaining digits |

3. Set the Workstate to Completed and run. With ActionMode **Input** the run fails (*input is not supported for regex values*); extracting text with `REGEX` requires **Verify**.
4. Check the results in **Tools > Buffer Viewer**; searching for `part` lists the four buffers.

The same technique reads three random numbers out of a random sentence in [Random values](/ToscaBase/expressions/random-values/#extract-several-random-numbers-from-a-random-string-named-groups), where the groups are separated by lazy `.*?` and the pattern is anchored with `^` and `$`.

## When to use which

| Situation | Approach |
|---|---|
| A number may vary but must stay within a range | `{INTERVAL[base][limit]}` or `{INTERVAL[base][lower][upper]}`, ActionMode Verify |
| A control's text differs per language or has a variable suffix | `{REGEX["..."]}` with `\|` and `.*` in the identification property |
| Verify that a value matches a pattern | `{REGEX["..."]}` as the TestStepValue, ActionMode Verify |
| Verify and split a value into buffers | Named groups inside `REGEX`, ActionMode Verify |
| Remove a prefix or a special character from a buffered value; match any suffix with a bare `*` wildcard | [String operations](/ToscaBase/expressions/string-operations/) |

For the ActionModes themselves see [ActionModes](/ToscaBase/test-cases/action-modes/); for buffers see [Buffers](/ToscaBase/data-and-parameters/buffers/); for addressing table cells by column and row see [Table controls](/ToscaBase/modules/table-controls/).
