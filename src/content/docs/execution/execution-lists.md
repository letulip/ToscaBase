---
title: ExecutionLists
description: Why ExecutionLists replace the ScratchBook once a TestCase is ready, how to build one from folders and TestCases, run it, and keep it synchronised with the TestCases section.
level: 2
sidebar:
  order: 10
sources:
  - id: H16RSCy6e_g
    title: "Tosca Tutorial | Lesson 59 - Execute Test Cases | Execution Lists | Test Results | Execution Entry|"
    url: https://www.youtube.com/watch?v=H16RSCy6e_g
    at: "00:02"
  - id: mFptsa3Wuts
    title: "Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper"
    url: https://www.youtube.com/watch?v=mFptsa3Wuts
    at: "01:17"
  - id: c42YuuEksL0
    title: "Tosca Tutorial | Lesson 61 - Synchronize Execution List with Test Cases | Execution Lists |"
    url: https://www.youtube.com/watch?v=c42YuuEksL0
    at: "00:06"
---

An **ExecutionList** is a collection of TestCases that are ready to run, together with every result those runs ever produced. It lives in the **Execution** section of the workspace and is the recommended way to execute tests once development is finished: unlike the ScratchBook, its logs survive, so you can debug, report, and compare iterations later.

## ScratchBook versus ExecutionList

Tosca runs TestCases in two places.

| | ScratchBook | ExecutionList |
|---|---|---|
| Purpose | Dry run, check that a TestCase is ready | Real execution, results kept for reference |
| How to start | Right-click a TestCase (or a single TestStep) > **Run in ScratchBook** | Right-click an execution entry, folder or list > **Run** |
| Check-out needed | No | Yes, the ExecutionList must be checked out |
| Results | Temporary, gone when the ScratchBook is closed | Stored in the `ActualLog` until you clear or archive them |

Tricentis advises the ScratchBook for dry runs only. In both cases every TestStep in the log gets a green tick on success and a red cross on failure, including verification steps.

## Where the Execution section is

If the green **Execution** folder is not visible on the home page, open it from the sections list and dock it next to **TestCases** so you can drag between the two. A fresh project already contains default items: an ExecutionList with standard-module examples, virtual folders, Exploratory Testing, Interactive Testing, **Configurations** and **TestEvents** (the last two belong to [distributed execution](/ToscaBase/execution/distributed-execution-dex/)).

## Creating an ExecutionList

An ExecutionList cannot be created directly under the Execution root; it needs an **ExecutionList folder** first.

1. Check out the Execution folder (or your parent folder).
2. Right-click it > **Create ExecutionList folder** (also available as a toolbar icon) and rename it, for example to the name of the application or release.
3. Right-click the new folder > **Create ExecutionList** and name it.
4. Add TestCases by **drag and drop** from the TestCases section. Dropping a whole TestCase folder recreates the same folder structure inside the list; dropping single TestCases adds them one by one. You can also build your own folder structure inside the list by hand, for example per functionality.
5. **Check in** to save the list to the shared repository.

Each TestCase added to a list becomes an **execution entry**; folders become **execution entry folders**. The list also has a **Test Configuration** tab showing the Test Configuration Parameters defined during TestCase development; a change made there applies to this ExecutionList only (see [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)).

## Running an ExecutionList

1. Check out the ExecutionList.
2. Select one execution entry, several, a folder, or the whole list, right-click > **Run**. (The neighbouring **Run as manual TestCase** is covered in [Manual execution](/ToscaBase/execution/manual-execution/).)
3. Tosca runs the entries one after another, processes the results and returns you to the list.
4. Check in again so the results are stored permanently in the repository.

The **Details** pane shows the outcome per entry; expand an entry to see which TestSteps passed and which failed. Use the **column chooser** to add columns such as summary, start time, end time or duration. Results stay in the list until you delete or archive them; how to read, reshape and export them is in [Results and logs](/ToscaBase/execution/execution-results-and-logs/).

## Keeping the list in sync with TestCases

Execution entries are references to the TestCases, not copies. Some changes made in the TestCases section flow into the ExecutionList automatically, others require a manual **Synchronize**.

Synchronised automatically:

- editing TestSteps or values inside a TestCase,
- renaming a TestCase.

Not synchronised automatically, you must right-click the ExecutionList (or folder) > **Synchronize**:

- renaming a TestCase folder (the execution entry folder keeps the old name until you synchronise),
- moving a TestCase to another folder or removing it from the folder (the entry stays in place until you synchronise, then it disappears from the old location),
- adding a new TestCase to a folder that is already in the list (the new entry appears only after synchronising).

:::tip
Synchronising is only needed when you keep restructuring TestCases after the ExecutionList exists. If you create the list after development is finished and only edit TestSteps afterwards, you never need it.
:::

## Related

- [Results and logs](/ToscaBase/execution/execution-results-and-logs/) for reading the `ActualLog`, trend charts, archiving and Excel export.
- [Repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/) for running an entry several times and assembling end-to-end views.
- [DokuSnapper](/ToscaBase/execution/dokusnapper/) for a generated document with a screenshot per TestStep.
