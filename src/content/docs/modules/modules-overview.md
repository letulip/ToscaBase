---
title: Modules overview
description: What a Tosca Module is, how ModuleAttributes map to controls, classic Modules versus XModules, the engines behind them, and standard versus user-defined Modules.
level: 1
sidebar:
  order: 10
sources:
  - id: deY38EHGvNs
    title: "Tricentis Tosca Tutorial Part-4 : Tosca Module Creation, Tosca Xscan, Tosca Modules Overview"
    url: https://www.youtube.com/watch?v=deY38EHGvNs
    at: "00:40"
---

A Module is Tosca's description of one screen, page or dialog of the application under test. It stores the technical properties of every control a TestCase needs, so that TestSteps can refer to a control by name instead of by its HTML or window internals. Creating Modules is the first step of TestCase development: no Module, no TestStep. This doc explains the vocabulary; scanning is in [XScan](/ToscaBase/modules/xscan/) and the ways Tosca tells controls apart are in [Control identification](/ToscaBase/modules/control-identification/).

## Module and ModuleAttribute

- A **Module** maps one page or screen of the application to Tosca. One Module per logical functional block (a login form, a header bar, a table page) is the recommended granularity; see [Module hygiene](/ToscaBase/best-practices/module-hygiene/).
- A **ModuleAttribute** is one control inside the Module: a text box, a button, a link, a table. Each attribute carries the technical properties (for HTML: `id`, `name`, `tag`, `value`, `InnerText` and so on) that Tosca uses to find the control at run time. Attributes can be renamed to a logical name; the technical properties stay underneath.
- The **Properties** pane on the right of Commander shows the attribute's properties and parameters. What they mean is in [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/).

When a Module is dragged into a TestCase it becomes a TestStep, and each ModuleAttribute becomes a TestStepValue that takes a value and an ActionMode. Modules are stored in the **Modules** section of the workspace; in a multi-user workspace, new Modules must be checked in (**Check in all**) before colleagues see them.

## Classic Modules and XModules

Tosca has two generations of Modules, distinguished by the engine architecture that created them:

| Kind | Created by | Attributes |
|---|---|---|
| Classic Module | Classic engines, the original Tosca engines, each written for one technology | Classic ModuleAttributes |
| XModule | TBox-based XEngines, scanned with XScan | XModuleAttributes |

The icons differ slightly in the Modules tree. Everything in this knowledge base uses XModules, because that is what XScan produces and what current Tosca versions expect.

### Engines

- **Classic engines** were developed in the early phase of Tosca. Each processes the TestCase information and steers the test object for one technology.
- **TBox** is the framework whose algorithm is the basis for the XEngines. It steers GUI and non-GUI objects alike.
- **XEngines** are defined in Tosca through **XDefinitions**. An XDefinition structures the controls of a technology hierarchically, so the tree of test objects maps onto the tree of ModuleAttributes you see in XScan.

The source lists the 3.0 generation of TBox-compatible engines: XScan 3.0, AnyUI Engine 3.0, API Engine 3.0, Database Engine 3.0, .NET Engine 3.0, Mobile Engine 3.0 and SAP Engine 3.0. Engine-specific details are in the [Engines](/ToscaBase/engines/) section.

:::note
The engine names come from an automatic subtitle track and one of them is garbled ("ap engine"); it is read here as the API Engine. Treat the list as illustrative rather than complete.
:::

## Standard and user-defined Modules

By usage, Modules fall into two groups.

**Standard Modules** are shipped by Tricentis and imported when the workspace is created (they can also be loaded later). They perform common operations that do not depend on your application: open a file, start a program, string and buffer operations, verifications. The source groups them into three folders that appear in the Modules section by default:

- **TBox Automation Tools**: basic operations on windows, buffers, files and folders, strings, date and time, processes and resources.
- **TBox XEngines**: technology-specific base Modules for database, HTML, .NET, SAP, mobile and so on.
- **Test data related Modules**: Test Data Management and Test Data Services.

Tosca ships many more, but these three folders are the ones used in almost every project. They are documented in [Standard Modules](/ToscaBase/standard-modules/).

**User-defined Modules** are created by the tester by scanning the application under test. Each represents one logical functional block. Creating them is the subject of [XScan](/ToscaBase/modules/xscan/).

## Where to go next

1. [XScan](/ToscaBase/modules/xscan/): scan a page and pick the controls.
2. [Control identification](/ToscaBase/modules/control-identification/): make every control unique.
3. [Rescan Modules](/ToscaBase/modules/rescan-modules/): fix a Module after the page or your needs change.
4. [Duplicate and merge Modules](/ToscaBase/modules/duplicate-and-merge-modules/): keep the workspace free of copies.
5. [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/): tune how a control is found and steered.
6. [Table controls](/ToscaBase/modules/table-controls/): rows, columns, cells and embedded controls.
