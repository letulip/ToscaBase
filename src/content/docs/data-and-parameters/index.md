---
title: Data and parameters
description: Where values live outside TestSteps - buffers, Test Configuration Parameters, Business Parameters with TestStepLibraries, and Test Data Services.
level: 2
sidebar:
  order: 0
---

A TestStep with a hard-coded value has to be edited every time the data changes. Tosca offers several ways to keep values outside the steps, each for a different kind of data: a **buffer** for values the application produces at run time, a **Test Configuration Parameter** for environment settings, a **Business Parameter** for the inputs of a reusable TestStepBlock, and **Test Data Services** for data that must be unique, tracked and shared between applications. Static data-driven design with TestSheets is in [TestCase-Design](/ToscaBase/test-case-design/).

| Doc | What it covers |
|---|---|
| [Buffers](/ToscaBase/data-and-parameters/buffers/) | The `Buffer` ActionMode, `{B[name]}`, the dynamic XBuffer `{XB[name]}`, buffer lifetime, the Buffer Viewer |
| [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/) | `{CP[name]}`, inheritance from folders, system-defined parameters, project-level Configurations, the Module-level `ConstraintIndex` for identical browser tabs |
| [Business Parameters and TestStepLibraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/) | TestStepBlocks, TestStepLibraries, reusable TestStepBlocks, Business Parameter containers |
| [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/) | Test data management on Tosca Server: repositories, types, items, required parameters, `{TDS[type.attribute]}` |
| [Test Data Service Modules](/ToscaBase/data-and-parameters/test-data-service-modules/) | Create, find, update, move and delete items from a TestCase; Expert Module; bulk data with Repetitions |

Read them in order: buffers appear in almost every TestCase, Test Configuration Parameters in every suite, libraries once a suite has repeated steps, and Test Data Services when several processes share data. The buffer Standard Modules themselves are in [Buffer operations](/ToscaBase/standard-modules/buffer-operations/).
