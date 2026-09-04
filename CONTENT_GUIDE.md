# Content guide

## What a doc is

A doc is a reworked article, not a transcript. Written for someone learning Tosca who wants
to find an answer fast. Precise Tosca terminology (Module, TestCase, TestStep, ExecutionList,
TBox, XScan, Buffer, Business Parameter, Configuration Parameter, ActionMode, Steering).
No "in this video", no "hello friends", no filler. Facts from the source only; if the
transcript is unclear or wrong, say so in an admonition rather than inventing.

## Topic taxonomy (directories under `src/content/docs/`)

| Directory                 | Covers                                                                                   |
|---------------------------|------------------------------------------------------------------------------------------|
| `getting-started/`        | what Tosca is, architecture, licensing (trial, cloud), install, cloud/VM setup, workspace and project setup, Commander overview, first TestCase, release notes |
| `modules/`                | Modules, XScan, identification (anchor, image, index, explicit name), rescan, duplicate/merge modules, module properties, configuration/identification/steering parameters, table and embedded controls |
| `test-cases/`             | TestSteps, ActionModes (Input, Verify, Buffer, WaitOn, Select, Constraint), control flow (If, Do, While), repetitions, recovery and cleanup scenarios, verification points, recorder, exploratory testing |
| `test-case-design/`       | TestSheets, attributes, instances, combinatorial methods, templates, instantiation, TestCase design classes |
| `standard-modules/`       | TBox automation modules: file and folder operations, buffer operations, start/close program, evaluation tool, screenshots, window operations, scroll, JavaScript, desktop dialogs |
| `engines/`                | Excel engine, PDF engine, XML engine, UIA engine, HTML modules, desktop automation |
| `expressions/`            | random values, date expressions, string operations, Base64, intervals, regex, math, multilingual/regex verification |
| `execution/`              | ExecutionLists, results and logs, trend charts, manual execution, business TestCases, log viewer, execution recording, scheduling, distributed execution (AOS, DEX agents), execution client, Jenkins/CI |
| `data-and-parameters/`    | Buffers and Buffer Viewer, Configuration Parameters, Test Configuration Parameters, Business Parameters, TestStep libraries and reusable TestStepBlocks, Test Data Services |
| `api-testing/`            | API Scan, API TestCases, request parameters, authentication, SOAP, attachments, message recorder |
| `requirements-and-reporting/` | requirements, risk weighting, reports and report definitions, TQL, virtual folders, Excel import |
| `administration/`         | users, groups, password reset, multi-user workspaces and repositories, check-in/check-out, branches, backup/restore, TCShell, TCWorkspaceUtil, test mandates, Tosca Server |
| `best-practices/`         | naming conventions, verification points, no static waits, folder grouping, workstates, review process |
| `troubleshooting/`        | "obstacles" (duplicate IDs, twins, dynamic tables, hidden elements, drag and drop...) and common real-time problems and fixes |
| `reference/`              | glossary, cheat sheets                                                                   |

One doc = one topic. If a video covers three topics, write three docs (or update three).
If a topic already has a doc, update it: merge new facts, keep structure, do not duplicate.

## File and frontmatter

File name: kebab-case, `<directory>/<topic>.md`. Same path under `ru/` for the translation.

```yaml
---
title: Execution Lists
description: One sentence, shown in search results and page meta.
sidebar:
  order: 20            # 10, 20, 30... leaves room for inserts
sources:
  - id: mFptsa3Wuts    # YouTube video id
    title: "Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper"
    url: https://www.youtube.com/watch?v=mFptsa3Wuts
    at: "02:15"        # timestamp where this topic starts, optional
---
```

`sources` is a custom field; keep it accurate, it is rendered at the bottom of the page.

## Structure inside a doc

1. One-paragraph summary: what it is and why it matters.
2. Sections with `##` headings by sub-topic. Steps as numbered lists. UI paths as
   **Bold > Menu > Item**. Names of Tosca objects in `code` when they are literal names.
3. `:::note`, `:::tip`, `:::caution` admonitions (Starlight syntax) for gotchas.
4. Cross-links to related docs using relative paths, e.g. `[Buffers](/ToscaBase/data-and-parameters/buffers/)`.
   Use the site base `/ToscaBase/` prefix; for RU pages `/ToscaBase/ru/...`.

Length: 300 to 1200 words. Split if longer.

## Russian translation

- Same file path under `src/content/docs/ru/`. Same frontmatter, translated `title` and `description`.
- Tosca terms stay in English, with a Russian gloss on first use: `ExecutionList (список выполнения)`.
- Natural technical Russian, not word-by-word. Keep code, paths, UI names as in EN.
- Cross-links point to `/ToscaBase/ru/...`.

## Glossary

`reference/glossary.md` holds every Tosca term used anywhere. When you introduce a term in a
doc, make sure the glossary has it. RU glossary gives the English term, the Russian gloss,
and a one-line explanation.
