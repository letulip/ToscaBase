---
title: Common problems and fixes
description: Switching browser tabs with SendKeys, steering one of two identical tabs with ConstraintIndex, counting all links or similar controls with ResultCount, and downloading and verifying a file with curl from Tosca.
level: 3
sidebar:
  order: 40
sources:
  - id: pfEIPPUBbo0
    title: "Tosca Tutorial | Lesson 147 - Common Problems & Fixes | Switch Browser Tabs | SendKeys"
    url: https://www.youtube.com/watch?v=pfEIPPUBbo0
    at: "00:02"
  - id: 1khI-I1gonk
    title: "Tosca Tutorial | Lesson 106 - Handle multiple browser tabs | Configuration Parameter | Obstacles |"
    url: https://www.youtube.com/watch?v=1khI-I1gonk
    at: "02:11"
  - id: oA61Emt_HUs
    title: "Tosca Tutorial | Lesson 149 - Common Issues | Count All Links | ResultCount | Cardinality | Regex"
    url: https://www.youtube.com/watch?v=oA61Emt_HUs
    at: "02:19"
  - id: WBx--Dvc1eM
    title: "Tosca Tutorial | Lesson 150 - Common Issues | Download & Verify File | Curl | PowerShell"
    url: https://www.youtube.com/watch?v=WBx--Dvc1eM
    at: "01:14"
---

Four questions that come up repeatedly in real projects and have no obvious module: moving between browser tabs, steering one of two identical tabs, counting every link (or button, or checkbox) on a page, and downloading a file so that it can be verified. The common thread is the fallback rule: when Tosca has no direct method, emulate what a user would do at the keyboard, generalise one Module attribute so it matches many controls, or start an external command-line tool. The Obstacle Course docs ([identification](/ToscaBase/troubleshooting/obstacles-identification/), [tables](/ToscaBase/troubleshooting/obstacles-tables/), [input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/)) cover the page-level puzzles; this doc covers environment-level ones.

## Switching between browser tabs

**Problem.** The application opens several tabs and the TestCase must move to the third tab, then the fifth, then back.

**Cause.** Tosca has no module that switches browser tabs.

**Solution.** Send the keyboard shortcuts a user would press with the standard module `TBox Send Keys`:

1. Add `TBox Send Keys` as a TestStep. Its `Caption` is the browser window title; use a distinctive part of the title followed by a wildcard so it still matches after the page title changes.
2. In `Keys`, write the shortcut using the SendKeys codes:

| Goal | Shortcut | Keys value |
|---|---|---|
| Go to tab number 3 | Ctrl+3 | `^3` |
| Next tab | Ctrl+Tab | `^{TAB}` |
| Previous tab | Ctrl+Shift+Tab | `^+{TAB}` |

The codes are the ones of the Microsoft .NET `SendKeys` class: `^` is Ctrl, `+` is Shift, `%` is Alt, and named keys go in braces (`{TAB}`). Search for the `SendKeys` class documentation to get the full list; every code there works in Tosca.

Use the numbered form when you know which tab you need; use `^{TAB}` / `^+{TAB}` when the number of tabs is unknown.

:::tip
The same idea applies to any missing method: if a user can do it with the keyboard, `TBox Send Keys` can do it too.
:::

## Identical browser tabs

**Problem.** Two browser tabs show the **same page** (same title, same controls). A TestCase that clicks a link works for a while, then fails after Tosca has switched between the tabs; the log says more than one matching tab was found.

**Cause.** The Module identifies the browser window by properties both tabs share, so the match is ambiguous. Rescanning does not help: the tabs really are identical.

**Solution.** Tell the Module which of the matching tabs to use with the Module-level Configuration Parameter `ConstraintIndex`, and drive its value from the TestCase:

1. Open the Module, right-click the control and choose **Create Configuration Parameter**.
2. Name it `ConstraintIndex` and set the value to the index of the tab to use (`2` selects the second tab). The click now lands in that tab.
3. A static index in the Module is fragile, so make it dynamic: add a `TBox Set Buffer` step before the click that sets a buffer `index` to `1` or `2`, and in the Module replace the value with `{B[index]}`. The TestCase, a TestCase-Design sheet or a Test Configuration Parameter now decides which tab is steered, and the Module never changes again.

:::note
The speaker says the parameter name is "constraint index"; `ConstraintIndex` is the spelling used here. Module-level Configuration Parameters are described in [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/); they are a different mechanism from [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).
:::

## Counting all links (or any set of similar controls)

**Problem.** Verify that a product page shows six products. The product titles are links; a page could show a hundred of them, so scanning each one is not an option.

**Cause.** By default a Module attribute matches exactly one control and can be used once.

**Solution.** Make one attribute match all of them and count the matches. Example from the SauceDemo products page:

1. Scan one product link. Its `tag` is `a`; its `id` is `item_4_title_link`. Another product has `item_0_title_link`: the prefix changes, the suffix `title_link` is constant.
2. In the Module, rename the attribute to something generic (`Product`). In the `id` property replace the changing part with a wildcard, keeping `*title_link`. The attribute now matches every product link.
3. Set **cardinality** to `0-n` and add the Configuration Parameter `ExplicitName = True`, so the attribute can be used repeatedly and renamed per TestStep if you also need to click individual links.
4. TestCase *Get product count*: `Product` → property `ResultCount`, ActionMode `Buffer`, value `b_products`. `ResultCount` returns the number of controls that matched.
5. Add `TBox Evaluation Tool` with the expression `{B[b_products]}==6`. It passes when the expression is true; the ScratchBook log shows `b_products` set to `6` and `6==6` evaluated to `True`.

Remove the `id` property entirely and the attribute matches **every** link on the page (all `a` tags). The same recipe counts buttons, or ticks all checkboxes on a page, by generalising the property they share. See [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/) and [Buffers](/ToscaBase/data-and-parameters/buffers/).

## Downloading and verifying a file

**Problem.** Download a file (PDF, image, media) from the application and then verify it, for example with the [PDF engine](/ToscaBase/engines/pdf-engine/).

**Cause.** Clicking the download link saves the file to the browser's *Downloads* folder; you then have to move it or point later steps at that folder. It works, but it is a long and sometimes fragile chain.

**Solution.** Download directly with `curl` from a TestStep.

`curl` (client for URL) is a free, open-source command-line tool for transferring data over network protocols. Install it on Windows and check with `curl --help` in a command prompt; if the option list appears, it is available. The basic download form is:

```text
curl <file url> -o <target path\file name>
```

In Tosca:

1. Add the standard module `TBox Start Program`. Set the program to `powershell.exe`.
2. Pass the arguments in order: `curl`, the file URL, `-o`, and the full target path (for example `C:\Temp\media.png`).
3. Set `Wait for exit` to `True` so the TestCase waits until the download finishes.
4. Add `TBox File Existence` with the target directory and file name, ActionMode `Verify`. The log reports one match when the file is there.

From here the file can be passed to any engine or file module; see [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/) and [Start and close programs](/ToscaBase/standard-modules/start-and-close-programs/).
