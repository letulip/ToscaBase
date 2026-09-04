---
title: What's new in Tosca 16
description: The Tosca 16.0 release - Tosca ID Mapper and ARIA support for Oracle and other ERP applications, the new themes, TestCase pre-execution approval, and the list of smaller enhancements.
level: 1
sidebar:
  order: 80
sources:
  - id: 9FwDDivrNT4
    title: "Tosca Tutorial - New features released in latest version of Tosca 16.0"
    url: https://www.youtube.com/watch?v=9FwDDivrNT4
    at: "00:02"
---

Tosca 16.0 is a long-term-support release whose headline is enterprise application automation: a new **Tosca ID Mapper** and native **ARIA** support make dynamic controls in Oracle and similar ERP systems identifiable without customising every control. It also brings a refreshed Commander UI with dark and high-contrast themes, an automated **pre-execution approval** workflow for TestCases, and a list of engine and platform updates. This page covers the features the source lesson demonstrates; the full list is in Tricentis' "Introducing new features in Tosca 16" blog post.

Upgrading is the usual installer run: download 16.0 from the support portal and go through the wizard ([Installation](/ToscaBase/getting-started/installation/)). **About Tosca** in Commander confirms the version.

## Enhanced automation for Oracle: Tosca ID Mapper

Oracle applications, like most ERP systems, are heavily customised, integrated with many other systems and full of dynamic controls whose IDs change on every load, so identification by ID is unreliable. The ID Mapper lets you define, once per application, a **default ID** strategy that every control in that application then uses.

The demonstration scans a "create contact" page of an Oracle ERP with text boxes, dropdowns and buttons whose IDs are all dynamic.

1. In **Modules** create a folder, scan the application and switch XScan to the **Advanced** tab.
2. Click the new **settings icon** in the XScan window and open **Unique application identifiers**.
3. Define an application: a name (for example `Oracle`), the **application identifier** (`Title` by default; `URL` is the other option) and its value, which is filled in from the current page. Save.
4. Select a control, for example the *First name* text box. It was identified by `id` and a tag, but the id is dynamic. Untick the id, tick stable properties instead: the default **name** (`first name`) and **visible** (`true`).
5. In the control's settings choose **Define default ID at application level**, which opens **Select application**; pick the application defined in step 3 and save. The control reloads with the default ID.

From now on every other control in that application (the *Last name* field, for instance) is identified by the same default properties automatically instead of by id and tag. Customisation time drops and stability rises, and the saved identifier library can be reused by others. See [Control identification](/ToscaBase/modules/control-identification/) for the general rules of unique identification.

## ARIA framework support

**ARIA** (Accessible Rich Internet Applications) is the framework that makes web content usable with screen readers, magnifiers and text-to-speech. It is used by Oracle, Workday, Microsoft Dynamics 365, SAP and others, and its adoption is being driven by EU accessibility regulation that the source expects to become mandatory for most applications by 2025. Tosca 16.0 can identify controls by their ARIA labels natively; a steering parameter decides whether native ARIA support is considered.

The demonstration scans an "add absence" page whose three buttons **Save and close**, **Submit** and **Cancel** sit inside a table.

- In the XScan **settings icon > General settings** there is a checkbox to **ignore ARIA controls**. It is unticked by default, so ARIA controls are taken into account; tick it to identify everything by ordinary properties instead.
- Without ARIA support those three buttons appear as `div` elements, which are hard to identify because they have no unique properties. With it, they appear as **buttons**, and the control's adapter property reads `Tricentis.Automation.Engines.Adapter.Aria.AriaButtonAdapter` (as spoken in the source).
- Select the buttons, save the Module, and steer them like any other button.

Leave ARIA support enabled whenever the application uses ARIA controls.

## New UI and themes

Tosca 16 changed folder icons and colours across Commander. A theme selector at the top of the window offers **Light** (default), **High contrast light**, **High contrast dark** and **Dark**. The dark theme suits people used to dark IDEs; the setting can be changed back at any time.

## TestCase pre-execution approval

An automated process to request and grant approval for TestCases before they are executed, so that only validated TestCases run and no unauthorised change slips in after validation. It covers **TestCases only**: not TestCase templates, business TestCases, Modules or ExecutionLists.

It reuses the TestCase **Workstate**, which Tosca now sets automatically:

| Event | Workstate |
|---|---|
| New TestCase in progress | `Planned` |
| User requests approval | `In Work` |
| Approved | `Completed` |
| Rejected | back to `Planned` |

The feature only works in a **multi-user workspace**, because a designated user group reviews and approves. Enable it by right-clicking the root project and choosing the option from the menu; user groups for the approval are created at the same level. The source could not demonstrate it in a single-user workspace.

Compare with the folder-based manual [review process](/ToscaBase/best-practices/review-process/), which pre-execution approval automates, and [Users and groups](/ToscaBase/administration/users-and-groups/).

## Other enhancements in 16.0

Listed in the source without demonstration:

- Tricentis Mobile Agent for Android and iOS connectivity
- Cloud license support, mainly relevant to Tosca administrators (see [Licensing](/ToscaBase/getting-started/licensing/))
- File service improvements
- SAP innovations
- qTest integration
- DEX (distributed execution) enhancements; see [Distributed execution](/ToscaBase/execution/distributed-execution-dex/)
- PDF automation and PDF comparison improvements; see [PDF engine](/ToscaBase/engines/pdf-engine/)
- Mainframe improvements
- Support for Java 17 applications
- Support for Windows 11

The source recommends upgrading, especially for teams automating ERP applications.
