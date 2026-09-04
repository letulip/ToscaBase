---
title: Review process
description: A folder-based review workflow with three approval stages and the four-eyes principle for Modules, TestCases and other Tosca artifacts.
level: 3
sidebar:
  order: 50
sources:
  - id: 1wda85oh_ok
    title: "Tosca Tutorial Lesson 106 - Review Process | Approval stages | 4 eyes principal | Best Practices |"
    url: https://www.youtube.com/watch?v=1wda85oh_ok
    at: "00:45"
---

A review process is the best practice that enforces all the others. Every Module and TestCase passes through defined approval stages and is checked by two people before it counts as complete, so naming, structure, verification points, lean Modules and correct waits are verified by someone other than the author. Tricentis rates this as the most important of its recommendations because it turns the other practices from advice into a team guideline.

## Why review

In development, every code change goes through peer review or static analysis; the same applies to test automation. The author of a TestCase does not see every possible improvement, and mistakes that are easy to make in Tosca, such as duplicate Modules, wrong folder structure, or Modules with far too many ModuleAttributes, are easy for a second person to catch before they reach the shared workspace. Reviewed artifacts are more efficient, cause fewer performance and workspace-size problems, and need less maintenance.

The review applies to every artifact type, with different priorities:

| Artifact | Review priority |
|---|---|
| Modules | Highest; most structural mistakes happen here |
| TestCases | Highest; the other best practices are checked here |
| Requirements | Optional; usually agreed with business or product owners already, or imported from a document, so fewer mistakes |
| ExecutionLists | Optional; execution rarely needs approval |

## Approval stages

Tricentis recommends three stages. Teams may add more, but three are enough for most projects. They are implemented as folders in the Modules section and in the TestCases section; an artifact moves from folder to folder as it progresses.

| Stage (Modules) | Stage (TestCases) | Who works here |
|---|---|---|
| `Inbox` | `In Work` | Authors create and edit; everything here is unfinished |
| `Ready for approval` | `Ready for approval` | Reviewers inspect; nothing is edited by the author |
| `Completed` | `Completed` | Final versions used by the project |

Workflow:

1. Create the Module or TestCase in the first stage folder and work on it there.
2. When you consider it finished, move it to `Ready for approval`.
3. The reviewers go through it, checking the best practices: naming, folder structure, verification points, no duplicate Modules, limited ModuleAttributes, no static waits.
4. If it meets expectations, move it to `Completed`. Only artifacts in `Completed` are used by the project.
5. Remove anything that was moved from the earlier stage folders, so that no copy lingers and no duplicate Modules arise.

Match the TestCase's [Workstate](/ToscaBase/best-practices/test-case-structure/#set-the-workstate) to the stage: `In Work` while it is being built, `Completed` once approved, so that requirement coverage stays accurate.

## Four-eyes principle

Every change is reviewed by two people, hence four eyes. In the folder workflow this means assigning two reviewers to the `Ready for approval` stage; an artifact moves to `Completed` only when both have approved it. This is what makes the review a check rather than a formality: one reviewer can miss what another sees.

## Making it stick

- Write the stage folders and the review checklist down as team guidelines. New members then follow the same process from their first day.
- Run the [duplicate Module check](/ToscaBase/best-practices/module-hygiene/) as part of the review rather than as a separate cleanup.
- Keep the checklist short: the five best-practice docs in this section are the list.

:::note
The source mentions that Tricentis publishes further best practices beyond the ten covered in this series but does not enumerate them.
:::

Related: [Naming conventions](/ToscaBase/best-practices/naming-conventions/), [TestCase structure](/ToscaBase/best-practices/test-case-structure/), [Module hygiene](/ToscaBase/best-practices/module-hygiene/), [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).
