---
title: UIA engine and desktop controls
description: What to do when Application scan misses controls - switch the XScan engine (WinX, UIA, Vision AI), add generic list items to a combo box, and click JavaScript alerts.
level: 3
sidebar:
  order: 40
sources:
  - id: UkEHEb_LNrI
    title: "Tosca Tutorial | Lesson 142 - Common Problems & Fixes | Desktop Application | Generic List Items"
    url: https://www.youtube.com/watch?v=UkEHEb_LNrI
    at: "00:12"
  - id: BUXOkE9GlI0
    title: "Tosca Tutorial | Lesson 143 - Common Problems & Fixes | UIA Engine | JavaScript Alert Window"
    url: https://www.youtube.com/watch?v=BUXOkE9GlI0
    at: "00:12"
---

Tosca scans web applications well, but desktop windows and browser-native dialogs are often only partly identified: a combo box appears without its items, a JavaScript alert does not appear at all. Writing a custom control in .NET is the last resort. Before that, XScan offers other engines for the same window, and Module properties let you add controls Tosca did not scan. This page shows both techniques on two common problems.

## Choosing another engine in XScan

**Scan > Application** shows every open window. Each window has an engine that XScan uses to identify its controls; right-click the window in the XScan tree to see and change it:

- **HTML** is preselected for browser windows.
- **WinX** is preselected for Windows-based windows such as Control Panel dialogs.
- **UIA** (UI Automation) can scan Windows-based controls and also browser-native popups.
- **Vision AI** identifies controls from the screen image; it requires a Vision AI account.

If the default engine does not list the control you need, first raise the number of filtered items in XScan to make sure it is not merely hidden, then rescan with UIA or Vision AI. Only if none of the engines finds it and no generic item can be added (see below) is a custom control justified.

## Desktop combo box without items

Example: **Device Manager > Monitors > Generic PnP Monitor > Properties > Details** has a `Property` combo box. The task is to verify that certain entries exist in that drop-down.

1. **Scan > Application** and pick the properties window; WinX is selected for it. The scan lists the label, the `Property` combo box, the `Value` list, the tab control and the buttons, but the items inside the combo box are missing, even with more filtered items.
2. Select the combo box (it is already unique), save the Module.
3. In the Module, right-click the combo box, open the **...** (ellipsis) menu and choose **Create generic list item**. A generic `Item` of type list item appears under the combo box. Its engine is WinX, and its **explicit name** property already lists every entry of the drop-down in the running application.
4. Because the item's cardinality is `0-n`, you can use it as many times as you like in a TestCase; each use adds another item row.

TestCase (`Verify driver properties` in a `Win controls` folder):

1. Add the Module. Set the combo box to ActionMode `Select`.
2. Add the generic item once per entry to check (`Device description`, `Capabilities`, `Status`), choose the entry from the explicit names, and verify `Exists` == `True` on each.
3. Run. Tosca maximises the window and the log info reports a successful verification for every item.

:::note
Generic items are available only for some control types. Where the **...** menu offers none and the other engines fail too, a custom control is needed.
:::

## JavaScript alert in Chrome

A JavaScript `alert()` opens a browser-native popup on top of the page and blocks all further steps. Scanning the browser with **Application** (engine HTML) lists the page's buttons and links but never the popup or its OK button, no matter how many filtered items you show.

1. Trigger the alert in the browser, then **Scan > Application** and select the browser window.
2. In the XScan window right-click the window and switch the engine from HTML to **UIA**, then click **Scan**. Among the scanned controls the alert and its `OK` button are now present.
3. Select `OK` (it is unique), save the Module as `JavaScript popup`.
4. Make the Module generic: the window title of a Chrome alert is `<site> says`, so replace the site part in the title identification with a wildcard, `*says`, and the Module matches any alert from any page.
5. Create a TestCase (`Click on popup`), add the Module, set the `OK` button to click and run it in the ScratchBook. The popup is dismissed and the TestCase continues.

:::caution
The title pattern is browser-specific. Firefox, Edge and others name the popup differently, so adjust the identification per browser.
:::

## Related

- [Control identification](/ToscaBase/modules/control-identification/) for identification by explicit name.
- [Obstacles: identification](/ToscaBase/troubleshooting/obstacles-identification/) for other cases of controls Tosca cannot see.
- [Desktop dialogs](/ToscaBase/standard-modules/desktop-dialogs/) for the standard Modules that handle native dialogs.
