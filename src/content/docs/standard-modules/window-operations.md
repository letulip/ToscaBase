---
title: Window operations
description: TBox Window Operation (bring to front, maximise, minimise, close, wait on open) and TBox Scroll Window Operation, including how to close a popup window without scanning it.
level: 2
sidebar:
  order: 60
sources:
  - id: _WKauyXPI8g
    title: "Tosca Tutorial | Lesson 18 - Window Operations | TBox Automation Module |"
    url: https://www.youtube.com/watch?v=_WKauyXPI8g
    at: "00:10"
  - id: SZj-04A7aQA
    title: "Tosca Tutorial | Lesson 25 - Scroll Window | TBox Window Scroll Operation | Standard Module |"
    url: https://www.youtube.com/watch?v=SZj-04A7aQA
    at: "00:07"
  - id: doHtSzuBCFY
    title: "Tosca Tutorial | Lesson 122 - Close Window Popup | Window Operations |Obstacle 16 |"
    url: https://www.youtube.com/watch?v=doHtSzuBCFY
    at: "02:14"
  - id: zr-SyuOhTeQ
    title: "TRICENTIS Tosca 16.0 - Lesson 58 | OBSTACLE #16 | Window Operations | Window Popup | Standard Module"
    url: https://www.youtube.com/watch?v=zr-SyuOhTeQ
    at: "06:24"
---

**TBox Window Operation** sends a command to a window identified by its caption: bring it to the front, resize it, close it, or wait for it to appear. **TBox Scroll Window Operation** scrolls a window's content by a number of pixels or lines. Both live under **Modules > Standard modules > TBox Automation Tools > Basic window operations** and are aimed mainly at Windows-based applications, but they also work on browser windows, for example for popups.

## TBox Window Operation

| ModuleAttribute | Meaning |
|---|---|
| Caption | Title of the window. Supports regular expressions |
| Window index | Which window to use when several share the caption; the first one if left empty |
| Operation | Dropdown with the command to send |

Available operations: **Bring to front**, **Close**, **Maximize**, **Minimize**, **Move to center**, **Normal** (restore the original size), **Resize**, **Verify window exists**, **Wait on close**, **Wait on open**.

### Captions and regular expressions

A Notepad window is titled `Untitled - Notepad`, and the first part changes with the file name. Write the caption as a regular expression that matches the stable part (`Notepad`) and lets the rest vary, so the step keeps working when the title changes. The same trick handles popups whose title is only partly predictable (below).

### Example: driving Notepad

1. **TBox Start Program** with the Notepad path; see [Start and close programs](/ToscaBase/standard-modules/start-and-close-programs/). This is a process operation, not a window operation, but the window has to exist first.
2. **TBox Window Operation**, caption `Notepad` as a regex, operation `Maximize`.
3. Copy the step and change only the operation: `Minimize`.
4. `Bring to front` after the minimise step, so the minimised window comes back.
5. `Normal` to restore the original size.
6. `Close`.

Run the steps one at a time in the ScratchBook to watch each effect; a full run is too fast to see. You can try the remaining operations on the same window.

## Closing a popup window

An automation obstacle opens a new window when a button is clicked and asks you to close it. You do **not** need to scan the popup: TBox Window Operation finds it by caption.

1. Scan only the button into a Module and add a TestStep that clicks it.
2. Add **TBox Window Operation** (drag it from **Standard modules > TBox Automation Tools > Basic window operations**). For the caption take the part of the popup title that is unique (in the example an account handle such as `@tricentis`; the word `Tricentis` alone also appears in the main window's title, so `*tricentis*` would close the main page) and surround it with regex wildcards.
3. Operation `Wait on open`. The popup takes a moment to load; without the wait the step runs before the window is there and fails.
4. Operation `Close` on the same caption. Lesson 122 puts it in a second TBox Window Operation step; in Lesson 58 (Tosca 16) choosing an operation adds another empty *Operation* row to the same TestStep, so `Wait on open` and `Close` are stacked in one step. Both forms pass.
5. Set the Workstate to Completed and execute: the button is clicked, the popup appears, is waited for and closed.

:::tip
`Wait on open` is the window-level equivalent of the `WaitOn` ActionMode. Use it in front of any operation on a window that takes time to appear rather than adding a static wait. See [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).
:::

## TBox Scroll Window Operation

Search **Add TestStep** for `TBox Scroll`.

| ModuleAttribute | Meaning |
|---|---|
| Caption | Title of the page or application window to scroll (regex allowed) |
| Window index | Which window, by opening order, if captions repeat |
| Vertical | How far to scroll vertically, in pixels or lines |
| Horizontal | How far to scroll horizontally, in pixels or lines |
| Mouse policy | `None` (pointer not moved) or `Center` (pointer positioned during the scroll) |
| Direction policy | `No direction policy`, `Vertical first` or `Horizontal first`: which axis is scrolled first when both are set |
| Delay | Milliseconds to wait between the vertical and the horizontal scroll when both are defined |

Only some attributes are mandatory: the caption, and at least one of Vertical or Horizontal. Index, mouse policy (`Center` is fine), direction policy and delay are optional.

Example on a page with infinite scroll whose title is `The Internet`: caption `The Internet` with a regex so a later title change still matches, no index, Vertical `500` (pixels), mouse policy `Center`, direction policy `Vertical first`, no delay. The ScratchBook run scrolls the page 500 pixels down; increase the value to scroll further. The Module works on any window that has scrollbars, web or desktop.

:::note
The Module was introduced in Tosca 16 and is not available in older versions. The video title calls it "TBox Window Scroll Operation" while the speaker says "scroll window operation"; search for `TBox Scroll` to find it.
:::

## Related

- [Desktop dialogs](/ToscaBase/standard-modules/desktop-dialogs/)
- [Obstacles: identification](/ToscaBase/troubleshooting/obstacles-identification/)
