---
title: Synchronisation, not waits
description: Replace static TBox Wait steps with the WaitOn ActionMode and avoid mouse and keyboard methods in TestStep values, with the Calculate / Send progress-bar example worked both ways.
level: 3
sidebar:
  order: 40
sources:
  - id: CH-pNE6AhqQ
    title: "Tosca Tutorial | Lesson 100 - No Static Waits in Test Cases | Best Practices |"
    url: https://www.youtube.com/watch?v=CH-pNE6AhqQ
    at: "00:50"
  - id: NRzZcXaskvo
    title: "Tosca Tutorial | Lesson 101 - No Mouse or Keyboard Methods in Test Step Values | Best Practices |"
    url: https://www.youtube.com/watch?v=NRzZcXaskvo
    at: "00:35"
---

A TestCase should wait exactly as long as the application needs and interact with controls the way Tosca does internally, not the way a human does. Two Tricentis best practices follow from this: no static waits, and no mouse or keyboard methods in TestStep values. Both make execution faster and more stable.

## No static waits

A static wait is a TestStep with the standard Module `TBox Wait` and a fixed `Duration`. Tosca pauses for that long regardless of the application's state. If the control you need appeared after two seconds, the remaining time is wasted; add a few of these and the execution time of a TestCase grows by minutes. Worse, the value is a guess: page load time depends on network bandwidth and other factors you cannot control, so a wait that is long enough today is too short tomorrow, and the TestCase fails intermittently.

The dynamic alternative is the ActionMode `WaitOn` (see [Action modes](/ToscaBase/test-cases/action-modes/)). A `WaitOn` step polls the control until the specified condition is met, then proceeds immediately; it only gives up after the maximum wait time configured in the settings. Static waits always wait the full time; `WaitOn` waits only as long as needed.

The source demonstrates it on a Tricentis obstacle page: clicking **Calculate** starts a progress bar, and the **Send** button is enabled only when the bar reaches 100%.

- **Static version.** Click `Calculate`; `TBox Wait` with `Duration` 20 seconds; click `Send`. In the run, Tosca kept waiting after the bar had finished, and by the time it clicked the page had returned to its initial state, so the click never landed. The only remedy would be tuning the duration by trial and error.
- **Dynamic version.** Click `Calculate`; on the `Send` button, ActionMode `WaitOn` with value `Enabled == True`; then click `Send`. This is one step shorter, needs no timing calculation, and clicked the button as soon as it became enabled.

:::tip
Use a static wait only as a last resort, when no condition on the application can express what you are waiting for, and keep such steps to a minimum. `WaitOn` is the main mechanism; the speaker notes that Tosca offers other dynamic options too, without naming them.
:::

## No mouse or keyboard methods in TestStep values

To click a button or link, many testers type a click method into the TestStep value, or send key combinations through a SendKeys step. These methods simulate physical keystrokes and mouse clicks using the Microsoft-defined keys of the Windows operating system, which means Tosca has to go through several APIs to perform a simple click. That is slower and less stable than the alternative.

For a button or link, set the value to `X` with ActionMode `Input` instead. It performs the same click, but Tosca does it internally without moving the pointer; in the demonstration the mouse cursor visibly does not travel to the button. On a single step the difference is invisible; across a large regression suite the accumulated time saving is significant.

:::note
The transcript refers only to "the click method". In Tosca's value syntax the mouse-click method is `{CLICK}`; that name comes from Tosca documentation, not from the video.
:::

Where a keyboard or mouse method is genuinely needed (drag and drop, special key combinations) it remains available; the recommendation is to minimise it and always look for a faster, internal equivalent first.

:::note
"Synchronization" also names an unrelated multi-user repository feature, the Synchronization policy that decides which objects a workspace keeps in sync with the common repository; see [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).
:::
