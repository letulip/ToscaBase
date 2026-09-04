---
title: Results and logs
description: Reading the ActualLog of an ExecutionList, changing its view, trend charts, clearing and archiving logs, copying results to Excel, and the LogViewer for low-level diagnostics.
level: 2
sidebar:
  order: 20
sources:
  - id: 26Uj-nXXcAw
    title: "Tosca Tutorial | Lesson 60 - Change View of Execution Results | Execution Lists | Actual Logs |"
    url: https://www.youtube.com/watch?v=26Uj-nXXcAw
    at: "00:08"
  - id: IJyo8YlR2Dg
    title: "Tosca Tutorial | Lesson 62 - Create Trend Charts from Execution Results | Execution Lists | Logs |"
    url: https://www.youtube.com/watch?v=IJyo8YlR2Dg
    at: "00:04"
  - id: el-UnoqLoCA
    title: "Tosca Tutorial Lession 63 - Clear and Archive actual execution logs | Execution Lists | Logs |"
    url: https://www.youtube.com/watch?v=el-UnoqLoCA
    at: "00:08"
  - id: R-am5RdZYUw
    title: "Tosca Tutorial | Lesson 64 - Transfer Execution Results from Execution Lists to Microsoft Excel |"
    url: https://www.youtube.com/watch?v=R-am5RdZYUw
    at: "00:08"
  - id: w-g6OTmrr7M
    title: "Tosca Tutorial | Lesson 69 - Monitor TestCase Execution Logs using Log Viewer | Monitoring | Debug |"
    url: https://www.youtube.com/watch?v=w-g6OTmrr7M
    at: "00:08"
---

Every run of an [ExecutionList](/ToscaBase/execution/execution-lists/) writes into its `ActualLog`. This doc covers everything you do with those logs after the run: shaping the view, charting results over time, keeping the log clean between releases, handing results to people who live in Excel, and, when the execution log itself is not enough, watching Tosca's internal log stream in the **LogViewer**.

## Changing the view of an ExecutionList

The **Details** pane of an ExecutionList folder shows a default set of columns. Two levels of customisation exist:

- **Column chooser**: add or remove columns (summary, start and end time, duration and so on).
- **View > ExecutionList** drop-down: toggles that change what the whole view displays. The defaults are pre-ticked; the others are:

| Option | Effect |
|---|---|
| Show only last ActualLog | Hides older logs, keeps only the log of the most recent run per entry |
| Multi-line logs | The log info column shows the full multi-line message instead of a one-liner; useful when debugging failures |
| Show statistics | The pass/fail bars and counts per folder; switching it off removes all bars |
| Show statistics only on visible ExecutionLists | Restricts statistics to the lists currently in view |
| Show statistics logarithmically | Shrinks the bars from full-column width to a logarithmic scale |
| Show failed logs only | Filters the log to failed TestCases |
| Duration in seconds | Shows durations as plain seconds instead of h:m:s, handy for timing individual steps |

## Trend charts

Trend charts must be enabled once per project: **Project > Options > View > Enable trend charts**. Afterwards every ExecutionList folder and ExecutionList gets a **Trend chart** tab next to **Details** and **Test Configuration**.

- The y-axis is the number of executed TestCases; the x-axis is time, grouped by the chosen interval (**Months** by default; also **Years**, **Weeks**, **Days**, **Hours**).
- Hovering a bar shows the interval and how many TestCases passed, failed or had no result.
- The chart type defaults to **Stacked bar**; **Bar**, **Line** and several 3D variants are available.
- You can zoom in to a single day or out to the whole range, and reset to the default view.
- The **print view** exports the chart as PDF, HTML, DOCX or XLS. An HTML export opens in the browser and can be shared as-is.

## Clearing and archiving the ActualLog

Every execution adds another entry to the `ActualLog`. When ExecutionLists are linked to requirements, the requirement dashboard reflects whatever is in the log, so a log from last quarter will still be counted as the current result. Two ways to start fresh:

- **Clear**: right-click the `ActualLog` > **Clear log**. The old results are deleted; you cannot see them again.
- **Archive**: right-click the ExecutionList > **Archive actual execution log**, enter an archive name (for example `RC01`), and answer the question whether to **discard the ActualLog**. **Yes** empties the `ActualLog` and keeps only the archive under the list; **No** keeps both.

An archive is not read-only history. Drag it back onto the `ActualLog` and it becomes the current log again (the `ActualLog` turns green). Archives also make debugging easier: when a step fails in the new run, you can open the archive and see that the same step passed in the previous release, which narrows the change in the application.

:::tip
Archive per release (`RC01`, `RC02`...) rather than clearing, so the requirement dashboard shows the current picture and the previous results stay available for comparison.
:::

## Copying results to Excel

Teams that report in Excel can transfer an ExecutionList table without any export wizard:

1. In the ExecutionList, select the folders, lists and execution entries you want (the hierarchy is preserved).
2. Right-click > **Copy table to clipboard** (`Ctrl+Shift+C`).
3. Open an Excel sheet, select a cell and press `Ctrl+V`.

Exactly the columns visible in the list are pasted, so add or remove columns with the column chooser before copying. Rename headers and format the sheet in Excel afterwards.

## LogViewer

The execution log tells you which TestStep failed; the **LogViewer** shows what Tosca itself was doing at the time. It is a separate application, `LogViewer.exe`, present in both the Commander home directory and the TBox home directory. Start it by double-clicking the executable (or from the command line) and keep it open next to Commander.

Options along the top:

- **Log level**: `Off` (default, shows nothing), errors only, warnings, information, or all levels. `All` floods the console as soon as Commander starts, so most of the time errors or warnings are enough.
- **Display mode**: **Console** shows events live; **File** only points to the log file being written. The **Files** list opens the generated log files, including `diagnostic log.txt`.
- **Clear** empties the console; **Save** writes the captured events to a file of your choice.
- **Chrome trace** saves the events as JSON for Google Chrome's tracing and profiling tool.
- **Previous/Next error** jump between errors; **Find** searches, with regex support.

Run a TestCase in the ScratchBook with the level set to `All` and you will see debug and info events from every Commander component. You do not need to understand them all: the viewer is for cases where the normal log gives no usable reason, and its output is what to send to your technical team or Tricentis support. It is also useful for configuration problems, for example server transactions failing in the background unrelated to the TestCase.

## Related

- [Manual execution](/ToscaBase/execution/manual-execution/) for setting a result by hand.
- [Recording executions](/ToscaBase/execution/recording-executions/) and [Screenshots on failure](/ToscaBase/standard-modules/screenshots-on-failure/) for visual evidence of a failure.
- [Reports](/ToscaBase/requirements-and-reporting/reports/) for formal report definitions.
