---
title: String operations
description: Length, case conversion, occurrence counting, trim, replace with escaped characters, Base64 encode/decode, and arithmetic on cleaned strings.
level: 2
sidebar:
  order: 30
sources:
  - id: GziZqKLQh58
    title: "Tosca Tutorial | Lesson 39 - Use String Operations | Find length | Convert To Uppercase | Occurences"
    url: https://www.youtube.com/watch?v=GziZqKLQh58
    at: "02:10"
  - id: 1_-3R24tqaI
    title: "Tosca Tutorial | Lesson 40 - Use Base64 String Operations | Encode and Decode text |"
    url: https://www.youtube.com/watch?v=1_-3R24tqaI
    at: "01:09"
  - id: GVUvUvMGlYY
    title: "Tosca Tutorial | Lesson 41 - Trim whitespace and Replace text | String Operations | Challenge |"
    url: https://www.youtube.com/watch?v=GVUvUvMGlYY
    at: "06:14"
  - id: ajyFN1dqNHE
    title: "Tosca Tutorial | Lesson 148 - Common Issues | Remove Special Characters | String Replace | Escape |"
    url: https://www.youtube.com/watch?v=ajyFN1dqNHE
    at: "05:31"
---

Values read from an application seldom arrive in the shape a verification needs: an order number is embedded in a label, a price carries a currency sign, a text has stray whitespace. Tosca's string operations are dynamic expressions that transform a string in place, usually inside a `TBox Set Buffer` TestStep, so the cleaned value can be buffered and reused. They replace what would be `String` methods in Java or .NET.

## Reference

All operations take the input string as the first argument; that string is normally a buffer (`{B[name]}`) or a Test Configuration Parameter (`{CP[name]}`). Expressions nest freely.

| Expression | Result | Example from the videos |
|---|---|---|
| `{STRINGLENGTH[string]}` | Number of characters | `{STRINGLENGTH[{B[str]}]}` returned `15` for a website address |
| `{STRINGTOUPPER[string]}` | Lower-case letters converted to upper case | `{STRINGTOUPPER[{B[str]}]}` |
| `{STRINGTOLOWER[string]}` | Upper-case letters converted to lower case | `{STRINGTOLOWER[{B[str]}]}` |
| `{NUMBEROFOCCURRENCES[string][pattern]}` | How often the pattern (one or more characters) occurs, case-sensitive | `{NUMBEROFOCCURRENCES[{B[str]}][t]}` returned `1` |
| `{NUMBEROFOCCURRENCES[string][pattern][IGNORECASE]}` | Same, ignoring case | `{NUMBEROFOCCURRENCES[{B[str]}][t][IGNORECASE]}` returned `3` |
| `{TRIM[string]}` | Removes whitespace from the start and end | `{TRIM[{B[B_order]}]}` |
| `{STRINGREPLACE[string][pattern][replacement]}` | Replaces every occurrence of the pattern | `{STRINGREPLACE[{B[price1]}]["\$"][]}` |
| `{STRINGREPLACE[string][pattern][replacement][IGNORECASE]}` | Same, ignoring case | `{STRINGREPLACE[{B[B_order]}][Order number:][][IGNORECASE]}` |
| `{BASE64[text][ENCODE]}` | Base64-encodes the text | `{BASE64[{CP[username]}][ENCODE]}` |
| `{BASE64[encoded text][DECODE]}` | Decodes a Base64 string | `{BASE64[{B[encode_username]}][DECODE]}` |
| `{MATH[expression]}` | Evaluates an arithmetic expression | `{MATH[{B[price1]}+{B[price2]}]}` |

:::note
The Lesson 148 video calls the arithmetic expression `CALC`; this knowledge base uses `MATH` throughout (see [Random values](/ToscaBase/expressions/random-values/)). A correctly formed expression is highlighted in the value cell; if it stays plain text, a brace or bracket is wrong.
:::

## Escaping special characters in patterns

`{STRINGREPLACE[{B[price1]}][$][]}` does nothing: **Translate value** shows the dollar sign still in place. Characters with a special meaning must be escaped with a backslash, and the pattern is placed in double quotes: `{STRINGREPLACE[{B[price1]}]["\$"][]}`. After that the translation shows the bare number.

## Worked examples

### Extract an order number from a confirmation label

A web-shop checkout ends with a line such as *Order number: 1431918*, and the number changes on every order. Goal: store just the number in a buffer for later verification.

1. In the Module, identify the label by `InnerText` with a wildcard, `Order number*`, so the ModuleAttribute matches any order number.
2. TestStep 1: ActionMode **Buffer**, buffer the `InnerText` into `B_order`. The log shows the buffer holds the whole label, with the words *Order number:* and a lot of whitespace before and after.
3. TestStep 2 (`TBox Set Buffer`, buffer `B_order_number`): replace the prefix with nothing, then trim what is left:

   ```
   {TRIM[{STRINGREPLACE[{B[B_order]}][Order number:][][IGNORECASE]}]}
   ```

   `IGNORECASE` is optional; it protects against the label being upper- or lower-case in the application.
4. The log reports *buffer with name B_order_number has been set to value 1431918*.

The speaker pastes rather than types this expression: nested braces and brackets are easy to get wrong, and a single missing bracket makes the whole value invalid.

### Sum prices that contain a currency sign

Two items in a cart show `$` prices; the TestCase must verify their total.

1. Scan the two price elements (raise the filtered-items count in the scan dialog until they appear), rename them `item1`, `item2`, save the Module as `cart`.
2. **Buffer** the `InnerText` of each into `price1` and `price2`.
3. `{MATH[{B[price1]}+{B[price2]}]}` in a Set Buffer named `sum` fails: the `$` makes it *not a valid expression*.
4. Replace the buffers with cleaned versions using `{STRINGREPLACE[{B[price1]}]["\$"][]}` (and the same for `price2`), then run the `MATH` expression again. The run passes and the log shows the total; it can be checked against the page with a **Verify** step.

### Encode and decode credentials with Base64

Usernames, passwords or database details stored in Test Configuration Parameters can be masked with Base64 so the clear text does not travel through the suite.

| Set Buffer name | Value |
|---|---|
| `encode_username` | `{BASE64[{CP[username]}][ENCODE]}` |
| `encode_password` | `{BASE64[{CP[password]}][ENCODE]}` |
| `decode_username` | `{BASE64[{B[encode_username]}][DECODE]}` |
| `decode_password` | `{BASE64[{B[encode_password]}][DECODE]}` |

The log shows the encoded strings after the first two steps and the original values after the last two. Passing plain text instead of an encoded buffer to `DECODE` fails, as the video demonstrates by mistake.

:::tip
Encoding and decoding the same value in one TestCase is only a demonstration. In practice you receive an already-encoded value (a buffer or a parameter) and `DECODE` it where the test needs the clear text, or you `ENCODE` something the application returned (an order ID, customer data) before storing it.
:::

## Where string operations fit

Use them whenever a buffered value has to be compared with an expected result, fed into a calculation, or entered into another field in a different shape. Buffering itself is covered in [Buffers](/ToscaBase/data-and-parameters/buffers/) and the `TBox Set Buffer` Module in [Buffer operations](/ToscaBase/standard-modules/buffer-operations/); splitting a string into several buffers with regular expressions is in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).
