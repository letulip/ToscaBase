---
title: Rescan Modules
description: Use Rescan to reopen an existing Module in XScan, add technical properties to a control that is not unique, add missing controls, and update the TestCases that use it.
level: 1
sidebar:
  order: 40
sources:
  - id: 7LTRawRLoE8
    title: "Tosca Tutorial | Lesson 9 - Rescan Modules in Tosca | Handle Non Unique Controls |"
    url: https://www.youtube.com/watch?v=7LTRawRLoE8
    at: "01:07"
  - id: TuRpQ3aLCdw
    title: "TRICENTIS Tosca 16.0 - Lesson 15 | Apply Value Range | Rescan | Module Merge"
    url: https://www.youtube.com/watch?v=TuRpQ3aLCdw
    at: "03:06"
---

The first scan of a page rarely gets every control right. Tosca identifies some controls uniquely and leaves others ambiguous, and you only find out when a TestStep fails with *more than one control found*. Rescan reopens an existing Module in XScan against the live application, so you can add technical properties, change the identification method or add controls you skipped, without creating a second Module for the same page. It is also the tool to use when the application changed and a control no longer matches.

## When to rescan

- A TestStep fails because more than one control matched. In the source this is a radio button: the page has two radio buttons with identical technical properties, and Tosca cannot decide which one to click.
- A control on the page changed and the Module no longer finds it.
- A new TestCase needs a control that was not scanned. Rescan and add it to the existing Module rather than scanning again; see [Module hygiene](/ToscaBase/best-practices/module-hygiene/). In Lesson 15 a shopping-cart Module scanned with only the checkout controls gets the *Update shopping cart* button, the coupon and gift-card boxes with their buttons, and, after a second rescan, the *coupon applied* message.

## Procedure

1. Open the application under test at the page the Module describes. If it is not open, Rescan reports *no window found*.
2. In the **Modules** section, right-click the Module and choose **Rescan**.
3. XScan opens and attaches to the open page by itself, without the **Select application** dialog, with the controls that are already in the Module selected, plus every other control on the page. Refresh if the page is not shown yet.
4. Select the problem control. An orange bar and the message *selected item is not unique* at the bottom confirm the problem. The technical properties currently ticked are shown; in the source only `name` and `tag` were selected.
5. Tick an additional technical property. Choose one that makes sense for identification (`id`, `name`, `value`), not any property that happens to differ (`checked`, `disabled`, `readonly` are listed but are state, not identity). Ticking `value` makes the radio button unique and the orange bar disappears. If no property does it, switch the identification method; see [Control identification](/ToscaBase/modules/control-identification/).
6. To add controls, use **Select on screen** as in a first scan and rename them. **Save** and close XScan; Commander returns to the Module, which now lists the added controls. Rescan can be repeated as often as the page needs it.

## What Rescan does to the Module

In the source, Rescan did not edit the existing attribute: it **added a new attribute** with the extra property (`value`) next to the old one. Afterwards:

1. Rename the new attribute so you can tell which one carries the fix.
2. Delete the old attribute. Tosca warns that it is used in a TestStep; confirm.
3. Open the TestCase. The TestStepValue that referenced the deleted attribute is now broken; delete it and add the new attribute to the TestStep with the action you need.
4. Run in ScratchBook. The mouse pointer goes to the right radio button and the TestCase passes.

:::note
Whether Rescan updates an attribute in place or adds a new one is not explained in the source; only the "new attribute" behaviour is shown. Check the Module after every rescan for duplicate attributes before deleting anything.
:::

## Rescan versus a new scan

A new scan creates a second Module for the same page, and every TestCase that already uses the first one keeps pointing at it. Rescan keeps one Module and one set of usages. If someone has already scanned a second copy, combine them with [Duplicate and merge Modules](/ToscaBase/modules/duplicate-and-merge-modules/).
