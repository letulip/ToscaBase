---
title: XScan
description: Scan a running application with XScan to create a TBox Module, pick controls on screen, read the unique / not unique feedback, and save the Module.
level: 1
sidebar:
  order: 20
sources:
  - id: deY38EHGvNs
    title: "Tricentis Tosca Tutorial Part-4 : Tosca Module Creation, Tosca Xscan, Tosca Modules Overview"
    url: https://www.youtube.com/watch?v=deY38EHGvNs
    at: "05:31"
  - id: Hy7xq4YP-Eo
    title: "Tosca Tutorial | Lesson 6 - Identify Controls By Anchor | Scan Modules |"
    url: https://www.youtube.com/watch?v=Hy7xq4YP-Eo
    at: "03:11"
  - id: xI8nEYSbqLQ
    title: "TRICENTIS Tosca 16.0 - Lesson 06 | Introduction to XScan | Scan your SUT with XScan |"
    url: https://www.youtube.com/watch?v=xI8nEYSbqLQ
    at: "03:10"
---

XScan is the scanner that creates TBox Modules (XModules). You point it at a running application, select the controls a TestCase will need, check that each control is uniquely identified, and save. The result is a Module whose ModuleAttributes hold the technical properties of those controls. Tosca provides engines to scan many technologies; the walk-through here uses a web page in Chrome, which is what the sources demonstrate. Vocabulary is in [Modules overview](/ToscaBase/modules/modules-overview/).

:::note
Tosca has two scanners. The classic *Tosca Scan* (also available as a standalone wizard) creates classic Modules; *XScan* creates TBox Modules. This doc, and everything else in the knowledge base, is about XScan.
:::

## Before you scan

1. Open the application under test and bring the page you want to scan to the screen. XScan lists the applications that are open on the desktop; a closed application cannot be scanned.
2. In Commander, open the **Modules** section. The standard Module folders (TBox Automation Tools, TBox XEngines, Test data related Modules) are already there.
3. Create a folder for your own Modules and give it a meaningful name. Scanning into a folder keeps user-defined Modules apart from the standard ones.

## Start the scan

Either right-click the folder and choose **Scan**, or select the folder and use the **Scan** icon on the **Modules** tab of the Commander ribbon. Both open the same list of scan types; for a web or desktop application choose **Application**.

Tosca then opens the **Select application** dialog. It takes a few seconds to appear because Tosca is enumerating every active application on the desktop. Select the browser window with your page and click **Scan**.

## The XScan window

XScan opens in **Basic view**: a screenshot-like representation of the page in which a single click on a control adds it to the Module. Switch to **Advanced view** to see the control tree with the technical properties of each control as tick boxes (a link comes with `InnerText` and `tag` ticked; tick `class` or another property to add it); the identification methods other than properties are only reachable there. The **Filtered items** setting controls how much of the tree is shown; raise it when a control or its container (`div`, `ul`) is hidden by the default filter.

To pick controls:

- In Basic view, click the control.
- In Advanced view, tick controls in the tree, or switch on **Select on screen** and click them in the application. The button is a toggle, off by default; click it again to leave that mode. The sources pick a search text box, a logo image and a button this way.
- **Condensed view** docks the XScan pane to the right edge of the screen so that the whole application stays visible; selection works the same.

Controls added in one view stay when you switch to another. **Highlight selection** (Advanced view) frames the selected control in the application, useful on a page with many controls; click it again to remove the frame. Each selected control is added to the Module with a proposed name and a set of ticked technical properties.

### Unique or not unique

XScan checks after every selection whether the ticked properties identify exactly one control on the page:

- **Selected item is unique**: nothing to do.
- **Selected item is not unique**, shown with an orange bar on the control: the same properties match more than one element. In the source, a text box is unique but a search button and a logo are not.

The message appears at the bottom of the XScan window, so you can see at a glance which controls still need attention. A Module can be saved with non-unique controls, but a TestStep on such a control fails at run time with *more than one control found*.

Fixing a non-unique control is a topic of its own: tick more technical properties (the logo becomes unique by its `alt` property), or switch to identification by anchor, image or index. The methods and the order in which to try them are in [Control identification](/ToscaBase/modules/control-identification/).

## Rename, save, check in

1. Rename each control to a logical name (`Search box`, `Search button`) instead of the technical default. Names carry over into TestSteps and make TestCases readable; see [Naming conventions](/ToscaBase/best-practices/naming-conventions/).
2. Check the Module name at the top of XScan: the proposal is derived from the page title (`Demo Web Shop. Login`) and can be edited there. Click **Save** and close XScan. The new Module appears in the folder you scanned into.
3. Select the Module: its controls are listed in the middle pane, and the **Properties** pane on the right shows each control's technical properties as parameters (see [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/)).
4. In a multi-user workspace, click **Check In All** so the Module reaches the central repository.

The Module is now ready to be dragged into a TestCase, where each control becomes a TestStepValue; see [TestCase basics](/ToscaBase/test-cases/test-case-basics/).

### Save or Finish screen

**Save** writes the Module and leaves XScan open with the selected controls in place. Add a forgotten control and click **Save** again: the same Module is updated, no second one is created. **Finish screen** also saves, but clears the selection so that the next page can be scanned into a new Module without closing XScan. Closing XScan with unsaved controls prompts to save; answer **No** to discard the scan.

## Scan only what you need

Select the controls the TestCase needs, not the whole page, and split a page into Modules by functionality. A page scanned in full is slower to steer and bloats the workspace. If a later TestCase needs a control you skipped, add it to the existing Module with [Rescan](/ToscaBase/modules/rescan-modules/) rather than scanning a second copy. The reasoning is in [Module hygiene](/ToscaBase/best-practices/module-hygiene/).
