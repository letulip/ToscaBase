---
title: Date expressions
description: Generate, calculate and format dates and times with DATE, MONTHFIRST, LDAY and related expressions, and fix the Tosca date format problem.
level: 2
sidebar:
  order: 20
sources:
  - id: q60mMo6mp0A
    title: "Tosca Tutorial | Lesson 36 - Use Dynamic Date Expressions | Date Calculations |"
    url: https://www.youtube.com/watch?v=q60mMo6mp0A
    at: "03:12"
  - id: Zk3-J0TxUEc
    title: "Tosca Tutorial | Lesson 38 -  Generate, calculate and format date and time values | Date Expressions"
    url: https://www.youtube.com/watch?v=Zk3-J0TxUEc
    at: "02:08"
  - id: gLTi9Qyejp4
    title: "Tosca Tutorial | Lesson 120 - Calculate Calendar Date | Date Expressions | Obstacle 14 |"
    url: https://www.youtube.com/watch?v=gLTi9Qyejp4
    at: "02:19"
  - id: jZU_s3DspGY
    title: "Tosca Tutorial | Lesson 123 - Enter Tomorrow's Date | Dynamic Date Expression | Obstacle 17 |"
    url: https://www.youtube.com/watch?v=jZU_s3DspGY
    at: "02:26"
  - id: tOYDf55pDME
    title: "Tosca Tutorial | Lesson 135 - Future Date | LDay | Date Expressions | Offset | Obstacle 29 |"
    url: https://www.youtube.com/watch?v=tOYDf55pDME
    at: "02:15"
  - id: ucnJlmkhs04
    title: "Tosca Tutorial | Lesson 139 - Common RealTime Tosca Problems & Fixes | Tosca Date Format |"
    url: https://www.youtube.com/watch?v=ucnJlmkhs04
    at: "02:19"
---

Date fields rarely accept a fixed value: a start date must lie one month in the future, a form wants tomorrow's date, a report needs the first day of the next month. A static date stored in a TestSheet works on the day it was written and fails the next day. Tosca's date expressions compute the value at run time from the current date (or any base date), apply an offset and print it in the format the application expects, without any Java or .NET code.

## Simple date and time expressions

Typing `{` in a TestStepValue lists all expressions; the date-related ones are below. The example outputs come from a TestCase that writes each expression into a `TBox Set Buffer` and reads the results in the ScratchBook log, run on 14 August 2023.

| Expression | Returns | Output in the video |
|---|---|---|
| `{DATE}` | The full current date | `14.8.2023` (the run's current date) |
| `{DATETIME}` | Current date and time (timestamp) | date plus time |
| `{TIME}` | Current time only | |
| `{DAY}` | Current day, numeric | `14` |
| `{MONTH}` | Current month, numeric | `8` |
| `{YEAR}` | Current year, numeric | `2023` |
| `{MONTHFIRST}` | First day of the current month as a complete date | 1 August 2023 |
| `{MONTHLAST}` | Last day of the current month as a complete date | 31 August 2023 |
| `{SYSTEMDATE}` | The full date in the format defined by the operating system | system-formatted date |
| `{NDAY}`, `{NMONTH}`, `{NYEAR}` | Day, month, year as two digits, zero-padded (`8` becomes `08`) | `08` for August |
| `{ADAY}`, `{AMONTH}` | Three-letter abbreviation of the weekday or month | `Mon`, `Mar` |
| `{LDAY[date expression]}` | The weekday of a date, as a word, according to the system settings | `Friday` |

The speaker notes that more expressions exist than these; the list is what the videos demonstrate.

## Calculated dates: DATE with base, offset and format

```
{DATE[base date][offset][format]}
```

| Part | Meaning |
|---|---|
| base date | The date to calculate from. Leave empty for today. Can be a literal date or a buffer such as `{B[fulldate]}`. |
| offset | Deviation from the base date: `+`/`-` followed by a number and unit. Units shown: `D` days, `M` months, `Y` years. Several can be chained: `+1M+1D`, `+2M-1D`. The speaker also mentions weeks and "other variations" but does not show them. |
| format | Output pattern built from `dd` (day), `MM` (month, upper-case), `yyyy` (year), for example `MM/dd/yyyy`. Leave empty to keep the default (system) format. |

:::caution
All three bracket pairs are mandatory even when empty. `{DATE[][+1D][]}` is valid; dropping the empty brackets is not.
:::

Tosca's own description of the expression uses the example: base date 23 May 2016, offset `+3M-1D`, format `MM/dd/yyyy`.

| Expression | Result |
|---|---|
| `{DATE[][+1M+1D][MM/dd/yyyy]}` | One month and one day from today, US format: `11/17/2023` when run on 16 October 2023 |
| `{DATE[][+1D][]}` | Tomorrow in the default format |
| `{DATE[][+1D][dd<sep>MM<sep>yyyy]}` | Tomorrow as day-month-year (the obstacle in Lesson 123 requires this order) |
| `{DATE[{B[fulldate]}][+2M-1D][yyyy<sep>MM<sep>dd]}` | Two months ahead, one day back, from a buffered date: 14.8.2023 becomes 13 October 2023 |
| `{MONTHFIRST[{B[generatedDate]}][+2M][yyyy-MM-dd]}` | First day of the second following month, ISO format |
| `{LDAY[{DATE[25<sep>12<sep>2024][+2Y][]}]}` | Weekday of 25 December 2026: `Friday` |
| `{DATE[{B[todaydate]}][][dd<sep>MM<sep>yyyy]}` | Reformat a buffered date without an offset |

:::note
`<sep>` stands for the separator between day, month and year (`.`, `/` or `-`): in Lessons 38, 123, 135 and 139 the speaker types it but never says it, so it cannot be confirmed from the audio. Where it is spoken (`MM/dd/yyyy` in Lesson 36) it is given literally. `MONTHFIRST` accepts the same base/offset/format arguments as `DATE`.
:::

Right-click a value and choose **Translate value** to see the computed date before running; the videos use it on every expression.

## Worked examples

### A date one month in the future

The Tricentis vehicle demo application's *Enter product data* screen rejects a start date unless it is more than one month in the future, and expects `MM/dd/yyyy`. One month exactly is rejected, so the offset is one month plus one day: `{DATE[][+1M+1D][MM/dd/yyyy]}`. Every day the run produces a new valid date and the TestCase never goes stale.

### Tomorrow's date (obstacles 17 and "get tomorrow's date")

Scan the single text box, drag the Module in, and set `{DATE[][+1D][]}` if the default format already matches, or `{DATE[][+1D][dd<sep>MM<sep>yyyy]}` when the field dictates day-month-year. Translate value confirms tomorrow's date. If the page does not react to the entered text (the obstacle in Lesson 123 did not detect the input), type it with `{SENDKEYS[...]}` instead, as described in [Random values](/ToscaBase/expressions/random-values/#read-two-random-numbers-and-add-them-math-sendkeys).

### First day of the second following month (obstacle 14, "confusing dates")

A calendar button generates a date in US format; the answer must be the first of the second following month in ISO format, then **Done** is clicked.

1. Scan the calendar button, the generated-date box, the solution box and the Done button.
2. For both date ModuleAttributes, right-click in the properties section, choose **Configuration Parameter**, and add the system-defined parameter `TargetDateFormat` with the US month/day/year pattern as its value. The name must be spelled exactly as Tosca defines it.
3. TestSteps: click the button; **Buffer** the generated date into `generatedDate` and change its data type from String to **Date**; enter `{MONTHFIRST[{B[generatedDate]}][+2M][yyyy-MM-dd]}` into the solution box; click Done.

:::note
In the video the expression silently turned into `MONTH` while being typed and had to be corrected back to `MONTHFIRST`; check the highlighted name before running.
:::

### Weekday of a future date (obstacle 29, "future Christmas")

The field wants the weekday, as a word, on which 25 December falls two years from now. Nest a `DATE` with the literal base date and `+2Y` offset inside `LDAY`: `{LDAY[{DATE[25<sep>12<sep>2024][+2Y][]}]}`. Translate value returns `Friday`, which is entered into the text box.

## The Tosca date format problem

Tosca interprets every date literal according to one format: the format of the system it is installed on, or the one defined inside Tosca. A `DATE` expression can convert *out of* that format, but a literal in any other format is not recognised as a date at all, and the TestStep fails.

Example: the system format is day-month-year, a `TBox Set Buffer` named `todaydate` holds `2024<sep>03<sep>07` (year-month-day), and a second Set Buffer `newdate` uses `{DATE[{B[todaydate]}][][dd<sep>MM<sep>yyyy]}`. The expression is correct, yet the run fails because the buffered value cannot be interpreted as a date.

Fix: on the TestCase's test configuration, add the system-defined Test Configuration Parameter **ToscaDateFormat** and choose the format that matches the *source* value from its list of values. Tosca then treats that format as valid and the conversion succeeds. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).
