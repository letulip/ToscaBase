---
title: Glossary
description: Short definitions of the Tricentis Tosca terms used throughout ToscaBase.
sidebar:
  order: 1
---

Short definitions of the Tosca terms used throughout this knowledge base.
Each entry links to the page where the concept is covered in depth once
that page exists.

## Terms

Module
: A reusable description of a screen, dialog, or API endpoint that Tosca
  scanned or that you built by hand. A Module lists the controls (ModuleAttributes)
  that TestCases can act on. Modules live in the *Modules* section of the workspace.

TestCase
: An ordered set of steps (TestSteps) that drive the application through the
  controls declared in one or more Modules. A TestCase is what you execute,
  either directly or from an ExecutionList.

ExecutionList
: A collection of TestCases grouped for a run. ExecutionLists hold the actual
  execution results and history, and are the unit you schedule, distribute, or
  report on.
