---
title: Execute JavaScript
description: Run JavaScript in the browser with the Execute JavaScript Module and check a script's return value with Verify JavaScript Result; both need a Browser Test Configuration Parameter.
level: 2
sidebar:
  order: 80
sources:
  - id: zZfamr0wZlc
    title: "Tosca Tutorial | Lesson 26 - Execute JavaScript | Verify JavaScript call | TBox HTML Modules |"
    url: https://www.youtube.com/watch?v=zZfamr0wZlc
    at: "00:07"
---

Two Standard Modules under **Modules > Standard modules > TBox XEngines > HTML** let a TestCase run JavaScript in the browser: **Execute JavaScript** runs a script, and **Verify JavaScript Result** runs a script and verifies what it returns. Anything JavaScript can do in the page (navigate, act on elements, read `document` state) is available through them.

## Prerequisite: the Browser Test Configuration Parameter

Both Modules throw an `InvalidOperationException` and the log asks you to define a Test Configuration Parameter for the browser if none is set. Fix:

1. Select the TestCase (better: its folder, so every TestCase inherits it) and open the **Test Configuration** tab.
2. Add a parameter named `Browser` and set its value to the browser to use, for example `Chrome`.

See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

## Execute JavaScript

| ModuleAttribute | Meaning |
|---|---|
| Title | Title of the browser window; a regular expression matching any title works |
| JavaScript | The script to run |

Example: navigate to a site by assigning `window.location.href` the URL of the demo shop (saucedemo). Running the step redirects the open Chrome window to that page and the TestCase passes.

## Verify JavaScript Result

| ModuleAttribute | Meaning |
|---|---|
| Title | Window title, regex allowed |
| JavaScript | Script that **returns** a value |
| Result | Expected value; ActionMode `Verify` |

Example: verify a session cookie after login.

1. In the browser's developer tools check the site's cookies: none before login; after logging in as the standard user a cookie named `session-username` with the value `standard_user` appears.
2. Title `*` as a regex, JavaScript `return document.cookie;`.
3. Result: the cookie in `name=value` form, `session-username=standard_user`, with ActionMode `Verify`.
4. Execute. The log shows the verification succeeded, with expected and actual values.

:::note
Subtitles drop punctuation, so the exact cookie string is reconstructed from the demo site. Check the name and value in your browser's developer tools before typing them into the Result attribute.
:::

## Related

- [Window operations](/ToscaBase/standard-modules/window-operations/)
- [UIA engine and desktop](/ToscaBase/engines/uia-engine-and-desktop/) for handling JavaScript alerts
