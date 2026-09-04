---
title: Expressions
description: Dynamic values in TestStepValues - random data, calculated dates, string operations, arithmetic and regular expressions.
sidebar:
  order: 0
---

A TestStepValue can be more than a literal: anything written in curly braces is a dynamic expression that Tosca evaluates at run time. Typing `{` in a value cell opens the autocomplete list of every expression; **Translate value** on the right-click menu shows what an expression will produce before you run the TestCase. This section is the reference for those expressions, grouped by what they do.

- [Random values](/ToscaBase/expressions/random-values/) - `RND`, `RNDDECIMAL` and `RANDOMTEXT` for generated data, plus `MATH` and `SENDKEYS` for calculating with values the application generates and typing them back.
- [Date expressions](/ToscaBase/expressions/date-expressions/) - `DATE`, `DATETIME`, `MONTHFIRST`, `LDAY` and related expressions with base date, offset and format, and the `ToscaDateFormat` fix when a date literal is not recognised.
- [String operations](/ToscaBase/expressions/string-operations/) - `STRINGLENGTH`, `STRINGTOUPPER`/`STRINGTOLOWER`, `NUMBEROFOCCURRENCES`, `TRIM`, `STRINGREPLACE` with escaped characters, `BASE64` encode/decode and `CALC`.
- [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/) - `INTERVAL` for verifying a value within a range, `REGEX` in ModuleAttributes and Verify steps, multilingual identification with alternatives, and named groups that split a value into buffers.

Expressions are usually combined with buffers (`{B[name]}`) and configuration parameters (`{CP[name]}`); those are covered in [Buffers](/ToscaBase/data-and-parameters/buffers/). How the Verify, Buffer and Input ActionModes interact with expressions is explained in [ActionModes](/ToscaBase/test-cases/action-modes/).
