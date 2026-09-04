---
title: Requirements and risk weighting
description: Structure requirements in Tosca, weight them by business risk, link TestCases and ExecutionLists to them, and read the coverage and execution-state dashboard.
level: 3
sidebar:
  order: 10
sources:
  - id: z7Vck380lDs
    title: "Tosca Tutorial | Lesson 71 - Create, Structure & Risk Weight Requirements | Risk Analysis |"
    url: https://www.youtube.com/watch?v=z7Vck380lDs
    at: "01:04"
  - id: Vgo6EM86-7k
    title: "Tosca Tutorial | Live Webinar Session | Requirements Management | Risk Based Testing | Live Project |"
    url: https://www.youtube.com/watch?v=Vgo6EM86-7k
    at: "04:05"
  - id: eaXtMXX84-o
    title: "TRICENTIS Tosca 16.0 - Lesson 18 | Link Automated Test Cases to Requirements | Link Execution Lists|"
    url: https://www.youtube.com/watch?v=eaXtMXX84-o
    at: "03:38"
---

The **Requirements** section of Tosca Commander holds the business requirements of the application under test, lets you assign a risk weight to each of them, and links them to TestCases, ExecutionLists and TestCase-Design sheets. Once linked, the section works as a project dashboard: it shows how much of each requirement is covered by specified TestCases and how much of it has passed or failed in execution. This is the foundation of risk-based testing, one of the two pillars Tosca is built on (the other being its modular, model-based approach): cover the highest-risk requirements with the fewest TestCases.

## Where the section lives

`Requirements` is a default section of every project. If it is not visible, open it from the **Sections** menu (choose **Requirements**). The **Requirements** entry on the top menu offers the same create actions as the right-click menu. You can also create a Requirements folder inside your own component folder.

Before you start, make sure the columns you need are visible. Right-click any column header, choose **Column Chooser**, and click a column to add it. The important ones are `Frequency Class`, `Damage Class` and `Weight`; useful extras are `Contribution`, `Relative Weight`, `Coverage Specified`, `Coverage Executed`, `Execution State`, `Required TestCases`, `Aggregated Weight`, `Result Aggregation` (requirement-set level), `Requirement Type` and a TestCase-Design column.

## Structure: folder, requirement set, requirement

The hierarchy is always:

1. **Folder** (right-click **Requirements > Create Folder**). Recommended even though it is optional. Structure folders by application, by functional area, by release or sprint, or by testing view (regression, smoke), whatever matches the project. Example: `Release` > `Sprint 1`.
2. **Requirement set** (right-click the folder > **Create Requirement Set**). A group of related requirements, e.g. `User Actions` or `Product Actions`. A new set shows 100% coverage because it contains nothing yet.
3. **Requirement** (right-click the set > **Create Requirement**), e.g. `Login User`, `Register User`, `Filter Products`, `Add Products`, `Search Products`. A requirement can hold **sub-requirements** (right-click the requirement > **Create Requirement**): the Tosca 16 webshop example has `Customer Tasks` with `Register`, `Login`, `Modify Customer Data` and `Check Order` underneath, next to `Handle Product`, `Shopping Cart` and `Order Process`.

Give each requirement a description ("User should be able to log in to the application"); an existing requirements document can be transferred as is.

## Weighting requirements

Every new requirement gets `Weight` = 1. Weight expresses the business risk: what happens to the business if this functionality fails. There are two ways to set it.

### Basic weighting

Type a value into `Weight` directly. Tosca accepts 1 to 10, but the recommended scale is **1 (least critical) to 5 (most critical)**. For example `Login User` = 5 because nothing else works without login, `Register User` = 3. The `Contribution` and `Relative Weight` columns recalculate automatically: a requirement's relative weight is its weight compared with all other weights in the same requirement set.

### Complex weighting (frequency and damage class)

Instead of guessing a weight, let Tosca calculate it from two factors:

- **`Frequency Class`**: how often end users use this functionality.
- **`Damage Class`**: the potential loss (financial, or for the client and end user) if this functionality fails.

Use the same 1 to 5 scale for both, and Tosca sets `Weight` with the formula:

```
Weight = 2 ^ FrequencyClass * 2 ^ DamageClass
```

So classes 3 and 3 give 8 * 8 = 64, and 5 and 5 give 32 * 32 = 1024. Contribution and relative weight follow from the calculated weight.

:::caution
Be consistent. If one requirement is rated on a 1 to 5 scale and another on 1 to 10, contribution and coverage figures become meaningless. Agree the values with the product owner or business analyst; they can also fill in this section themselves.
:::

## Requirement types

By default every requirement has the type `Requirement`. To classify requirements (for example `Functional Requirement` and `Non-functional Requirement`):

1. Open the project's **Properties Definition** node (under the project root) and right-click **> Create Requirement Type Definition**. Name it.
2. Drag the **requirement** onto the requirement type definition (not the other way round).
3. The requirement's properties now show the new type; add the `Requirement Type` column to see it in the list.

## Linking TestCases: coverage specified

Drag a TestCase, or a whole TestCase folder (for example a folder of template instances), onto a **requirement**; docking the Requirements section next to TestCases (split-screen view) makes this easier. TestCases can only be linked to requirements, never to a requirement set. An alternative is right-click the requirement **> Create TestCase Link**, rename the link and drag the TestCases onto it; drag-and-drop directly onto the requirement is the quicker option.

`Coverage Specified` shows how complete the linked TestCases are. It is driven by the TestCase **Workstate**, which maps to a fixed percentage:

| Workstate | Counts as |
|---|---|
| `Planned` | 20% |
| `In Work` | 50% |
| `Completed` | 100% |

Coverage specified = relative weight * Workstate percentage, aggregated over the linked TestCases. With every TestCase `Completed` the requirement shows 100%; set one to `In Work` and one to `Planned` and the figure drops (87% in the webinar example). Always mark finished TestCases `Completed`, otherwise the dashboard under-reports coverage. See [TestCase structure and Workstates](/ToscaBase/best-practices/test-case-structure/).

## Linking ExecutionLists: execution state

Drag an [ExecutionList](/ToscaBase/execution/execution-lists/), or individual execution entries, onto a requirement set or requirement. Linking TestCases alone is not enough: the results of a run reach the requirements only through a linked ExecutionList, so link the list that runs those TestCases to their parent **requirement set** (the webshop example links the `Webshop` ExecutionList to the `Webshop Frontend` set). `Execution State` then splits into passed, failed, not executed and not linked (for example 37% passed, 30% failed, 20% not executed, 13% not linked). Before anything is linked, `Coverage Specified` and `Execution State` are grey and show 100% by default.

Figures aggregate upwards by weight: with one sub-requirement at 100% coverage and another at 20%, the parent showed 49%, and a requirement whose only linked TestCase failed showed 100% failed. Together the two columns form the traceability matrix of the project.

The properties of a requirement show the same figures under **Status** (passed, failed, not linked) and **Calculation results**.

## Linking TestCase-Design

A [TestSheet](/ToscaBase/test-case-design/test-sheets-and-attributes/) can also be dragged onto a requirement; Tosca creates a TestCase substitute link.

:::note
In the webinar the drag-and-drop of a TestSheet was refused; the speaker suspected the sheet contained only a design class without attributes or instances. Treat the TestSheet link as possible but unverified; TestCases and ExecutionLists are the links that matter for the dashboard.
:::

## Keeping the values current

In a [multi-user workspace](/ToscaBase/administration/multi-user-workspaces/) other users add TestCases and run executions, so the percentages can go stale. Right-click the requirement set **> Update Values**. Tosca warns that recalculation can take time on large projects; it then recomputes every linked figure.

## Importing requirements from Word

Right-click a requirements folder **> Import Requirements from Word Captions**. The document must follow the structure in the Tosca documentation (a sample document is provided): a heading per requirement, sub-headings for sub-requirements, and text underneath.

## Sharing the dashboard

Stakeholders without Tosca access can get the dashboard through **Print View** in the Requirements section, exported as HTML, PDF or Excel (Excel is easiest to tidy into a management report). See [Reports](/ToscaBase/requirements-and-reporting/reports/) for report definitions with charts and logs.
