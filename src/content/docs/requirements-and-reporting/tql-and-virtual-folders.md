---
title: TQL search and virtual folders
description: Query the workspace with Tosca Query Language, filter ExecutionLists and TestCases by their properties, and save the query as a self-refreshing virtual folder.
level: 3
sidebar:
  order: 20
sources:
  - id: bhuotHSk12Q
    title: "Tosca Tutorial | Lesson 73 - Using Tosca Query Language(TQL) Search with Virtual Folders | Reporting"
    url: https://www.youtube.com/watch?v=bhuotHSk12Q
    at: "00:03"
---

Tosca Query Language (TQL) is Tosca's own query grammar for searching the workspace by object type and property, not just by text. A TQL query returns every object that matches (TestCases, Modules, requirements, ExecutionLists, TestStepValues and so on). A **virtual folder** stores such a query and shows its results as folder content, so a frequently needed view, such as "ExecutionLists with no failures" or "TestCases created by a given user", is one click away and can feed a [report](/ToscaBase/requirements-and-reporting/reports/).

## The search window

Open **Search** from the top menu. One window holds both search modes and a button to save the current TQL query into a virtual folder on the right-hand side.

- **Simple search**: type text and Tosca returns every object that contains it. Nothing more to configure.
- **TQL search**: the simple search is converted into a TQL expression that you can edit. This is where properties and operators come in.

## How a TQL query is built

A query is a chain of sub-expressions:

1. **Scope**: where to look. `SubParts` from the current folder returns everything underneath it; run from the root project it searches the whole workspace.
2. **Object type**: which class of object to return, e.g. `ExecutionList`, `TestCase`, `Requirement`, `Module`.
3. **Constraint** in square brackets: a logical comparison of a property against a value.

Operators the lesson uses:

| Operator | Meaning | Example |
|---|---|---|
| `=?` | contains the text (what simple search generates) | `Name=?"Google"` |
| `==` | exact match, far fewer results | `Name=="Google"`, `CreatedBy=="Admin"` |
| `>` | greater than | `NumberOfTestCasesPassed>1` |
| `<` | less than | `NumberOfTestCasesFailed<1` |

The operators are as spoken in the lesson; the property names are spoken only as words ("number of test cases passed", "created by"), so their exact spelling is what you see in the search window's column list. In the report definition editor the same query is built from **Link**, **Object type** and **Constraint** fields, which also shows you the exact spelling Tosca expects.

### Example: ExecutionList health

1. Start with `SubParts` and object type `ExecutionList`: the result lists every ExecutionList in the workspace.
2. The result grid offers the ExecutionList's properties as filter fields, including number of TestCases passed and failed.
3. Add a constraint `NumberOfTestCasesPassed>1` to keep only lists where more than one TestCase passed.
4. Change it to `NumberOfTestCasesFailed==0` (or `<1`) to list ExecutionLists in which nothing failed.

The same pattern works on any object: requirements, Modules, TestStepValues, TestCases. The only learning curve is the structure of sub-expressions and the property names, which are the column names you see in Commander.

## Virtual folders

A virtual folder owns no objects. It holds only a TQL query, and its content is whatever the query returns. That makes it a saved search: open the folder instead of retyping the query.

### Create one

1. Go to a real folder, for example `TestCases`. A virtual folder can be created inside any folder of any section (TestCases, Modules, Requirements, Execution), but **not** directly at the root project. This is also why the search window refuses to save into a virtual folder while you are at the root.
2. Right-click the folder **> Create Virtual Folder**. Rename it; with several virtual folders an explicit name matters.
3. Open the folder's **Properties** and enter the TQL query. Example from the `TestCases` folder: `SubParts`, object type `TestCase`, constraint `CreatedBy=="Admin"`. Click **OK** and the folder fills with every TestCase created by that user.

Extend the constraint to filter by creation date, by Workstate (completed or not), by whether the TestCase is a template, and so on. Which user created how many TestCases is a ready-made report for management.

### Use one

- Results are **not** live. After changes in the workspace right-click the folder **> Refresh Virtual Folder** to re-run the query.
- Edit the query from the folder's properties at any time.
- A virtual folder can be the source of a report; the option appears in its context menu (see [Reports](/ToscaBase/requirements-and-reporting/reports/)).

:::tip
Create several virtual folders for the views you need repeatedly (failed ExecutionLists, TestCases still `In Work`, requirements without linked TestCases) and build the analysis on them rather than on ad-hoc searches.
:::
