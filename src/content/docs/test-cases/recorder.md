---
title: Recorder
description: Record your actions on an application and let Tosca generate the Modules and a TestCase automatically - the recorder toolbar, verification mode, settings, what gets generated and what you still have to fix.
level: 1
sidebar:
  order: 60
sources:
  - id: _DlTBXAcxSw
    title: "Tosca Tutorial | Lesson 75 - Create TestCases Automatically using the Recorder |"
    url: https://www.youtube.com/watch?v=_DlTBXAcxSw
    at: "01:11"
---

The normal way to build a TestCase is to scan Modules with [XScan](/ToscaBase/modules/xscan/) and assemble TestSteps from them. The **Recorder** offers a shortcut: you perform the flow on the application, and Tosca creates the Modules and a TestCase for every action, verification included. It is the quickest route to a running TestCase, but not the cleanest, so it fits two situations: a feasibility check of whether Tosca can drive a given application, and small applications that need a quick automation. For a real regression suite, scanning your own Modules and structuring them yourself remains the preferred approach.

## Starting a recording

The Recorder is the last option on the **Home** menu bar. It has two entries:

- **Automated TestCase** records a plain TestCase.
- **Automated data-driven TestCase** records the same, plus a TestSheet so the TestCase can be driven by data (see [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/)).

Clicking the Recorder icon itself, or one of the two entries, loads the recorder: a small toolbar appears and red marks in the four corners of the screen show that the whole screen is being recorded.

## The recorder toolbar

| Control | What it does |
|---|---|
| Settings | Shows all recorder settings (see below) |
| Image-based TestStep | Switches to image-based control identification for the next step; press **Esc** to return to normal mode. Same mechanism as image identification in [Control identification](/ToscaBase/modules/control-identification/) |
| Verification mode (tick icon, **Ctrl+Shift+V**) | While on, clicking a control adds a `Verify` step for it instead of an action |
| Pause | Pauses recording, for example while you navigate somewhere you do not want recorded |
| Stop and save | Ends the recording and generates the objects |

Hints shown during recording list further shortcuts: **Ctrl+Shift+H** records a mouse-over event, **F5** refreshes the recorder.

### Settings

- **Auto record mouse over** (off by default).
- **Hints** on or off.
- **Reuse existing Modules** so the recording does not create duplicates of Modules you already have.
- **Block processes** from recording.
- Shortcuts for changing the recording mode, recording mouse-over and refreshing the recorder.

## Worked example: web shop checkout

With **Automated TestCase** selected: click `Login`, enter email and password, click `Login`; open a product and add it to the cart; open the cart and go through checkout (billing address, shipping address, shipping method, payment), clicking **Continue** to the confirmation page and **Confirm**. On the confirmation page press **Ctrl+Shift+V**, click the order number to record a verification, switch verification mode off, continue, and click `Logout`. Then **Stop and save**.

Tosca creates a new folder in the project containing:

- **One Module per page**, with ModuleAttributes for every control that was used, named with Tosca's default names.
- **One TestCase** with a TestStep per recorded action. A click is recorded as Value `X` with ActionMode `Input`, typed text as the text with `Input`, and the verification as `Verify` on `InnerText` of the clicked control.

## What to fix afterwards

A recorded TestCase runs, but it is not finished:

- **Rename** Modules, ModuleAttributes and TestSteps according to your [naming conventions](/ToscaBase/best-practices/naming-conventions/); the generated names describe nothing.
- **Remove duplicates.** Clicking a control several times during recording produces several steps; in the source the order number was verified three times and two of the steps had to go.
- **Replace static values.** The recorded verification compares against the literal order number seen during recording, which changes on every order. Buffer it or verify a pattern instead; see [Action modes](/ToscaBase/test-cases/action-modes/) and [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).
- **Restructure** into folders and reusable steps as described in [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

The trade-off is time: recording an end-to-end flow takes a few minutes, scanning every Module separately takes longer; the price is generated names and structure you would not have chosen. For documenting a manual session with screenshots rather than generating a TestCase, use the [exploratory testing](/ToscaBase/test-cases/exploratory-testing/) recorder instead.
