---
title: Test mandates
description: Let several users execute the same ExecutionList at the same time without overwriting each other's results by linking it to a test mandate, and clear the auto-merge link when it is no longer needed.
level: 4
sidebar:
  order: 60
sources:
  - id: zFHcStTuHbI
    title: "Tosca Tutorial | Lesson 96 - Use Test Mandates to execute same tests simultaneously | Multiple Users"
    url: https://www.youtube.com/watch?v=zFHcStTuHbI
    at: "00:09"
---

In a multi-user workspace an [ExecutionList](/ToscaBase/execution/execution-lists/) has one result log, and it has to be checked out to be executed. If several users run the same ExecutionList at the same time, each run overwrites the others' results. A **test mandate** solves this: it is an object in the Execution section that is linked to an ExecutionList, an execution entry or an execution folder. Users execute the mandate instead of the ExecutionList, no checkout of the ExecutionList is needed, and when everyone has checked in their results are collated into the ExecutionList rather than overwritten. Test mandates exist only in multi-user workspaces.

## Creating a test mandate and linking it

1. Check out the tree of the ExecutionList folder.
2. Right-click the ExecutionList folder and choose **Create Test Mandate**; name it (the source uses `Login mandate` for an ExecutionList `Login test`).
3. Drag the ExecutionList (or an execution entry, or an execution folder) onto the mandate. Tosca creates a copy of it as a folder inside the mandate, including the TestCase entries.
4. In the log of the original ExecutionList a **blue arrow** now marks it as linked to a test mandate.
5. **Check In All** so that other users see the mandate.

## Executing through the mandate

Each user checks out the mandate (not the ExecutionList) and runs it like an ExecutionList; the run shows passed or failed as usual. After **Check In All**, open the original ExecutionList: its latest execution is marked as linked to the mandate and carries the mandate's results. When several users execute the mandate, their results are collated in the ExecutionList and shown in the mandate, never overwriting each other.

From the ExecutionList log there is a command to jump to the corresponding test mandate entry.

## Removing the link

To stop the ExecutionList from collecting mandate results:

1. Check out the ExecutionList.
2. Right-click its log and choose **Clear auto merge list**.

The latest execution log is no longer linked to the mandate and the mandate's results stop appearing in the ExecutionList.

## Related

- [Execution results and logs](/ToscaBase/execution/execution-results-and-logs/): reading the log the mandate feeds.
- [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/): the check-out rules that make mandates necessary.
