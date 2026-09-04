---
title: Modules
description: How Tosca describes screens as reusable Modules, from scanning with XScan and making controls unique to properties, parameters, tables and workspace hygiene.
level: 1
sidebar:
  order: 0
---

A Module is Tosca's model of one screen or page: the controls a TestCase needs, with the technical properties Tosca uses to find them at run time. Everything else in Tosca builds on Modules, so this section comes right after [Getting started](/ToscaBase/getting-started/). Read the docs in order; each assumes the previous one.

| Doc | What it covers |
|---|---|
| [Modules overview](/ToscaBase/modules/modules-overview/) | Module and ModuleAttribute, classic Modules versus XModules, engines and TBox, standard versus user-defined Modules |
| [XScan](/ToscaBase/modules/xscan/) | Starting a scan, selecting controls on screen, the unique / not unique feedback, saving and checking in |
| [Control identification](/ToscaBase/modules/control-identification/) | Identify by properties, anchor, image and index, in that order, and `ExplicitName` for choosing a control from the TestCase |
| [Rescan Modules](/ToscaBase/modules/rescan-modules/) | Reopening a Module in XScan to add properties or controls, and fixing the TestCases that use it |
| [Duplicate and merge Modules](/ToscaBase/modules/duplicate-and-merge-modules/) | Find duplicate Modules and the Module merge assistant |
| [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/) | Cardinality, business type, synchronization policy, and configuration, identification, steering and transition parameters |
| [Table controls](/ToscaBase/modules/table-controls/) | Rows, columns and cells, selectors, table properties, steering examples, embedded controls, row and column count |
| [Table baseline comparison](/ToscaBase/modules/table-baseline-comparison/) | Snapshot a table and verify later executions against it |

Related: the real-world cases where identification goes wrong are in [Troubleshooting](/ToscaBase/troubleshooting/), and the reasons to keep Modules small and unique are in [Module hygiene](/ToscaBase/best-practices/module-hygiene/). Modules shipped with Tosca are in [Standard Modules](/ToscaBase/standard-modules/).
