---
title: Message Recorder
description: Capture the HTTP traffic between an application and its backend with the API Scan Message Recorder, inspect the calls, and export them as API messages to build TestCases from.
level: 3
sidebar:
  order: 50
sources:
  - id: GWWPLBMYatE
    title: "Tosca Tutorial | Lesson 88 - Record API Messages using Message Recorder | API Testing |"
    url: https://www.youtube.com/watch?v=GWWPLBMYatE
    at: "00:07"
---

Scanning a definition (see [API Scan basics](/ToscaBase/api-testing/api-scan-basics/)) only works when someone gives you a Swagger, WSDL or similar file. When the API calls an application makes are undocumented, the **Message Recorder** in API Scan records the traffic between the system under test and its backend, shows every call as an API message, and exports the ones you pick so you can build TestCases from them.

## Opening the recorder

Click **Record** in the top bar of API Scan. The Message Recorder window has:

| Control | Purpose |
|---|---|
| **Start** / **Stop** | Begin and end a recording session (message tracing). Once started, the button turns into Stop |
| **Clear all** | Remove every message captured so far |
| **Configure** | Proxy address, username and password; option to **decrypt HTTPS traffic** |
| **Export** | Send the selected messages into API Scan as messages |

## Recording a session

1. Click **Start**. The list stays empty until traffic occurs.
2. Generate traffic. Either run a TestCase from Tosca Commander (the source runs a Vehicle Insurance web TestCase in ScratchBook) or use the application yourself in the browser; the recorder does not care which, it captures whatever the system under test sends.
3. Watch the list fill up. Each entry shows the **result** (status code), the **host URL**, the **content type** and the **process**. Click an entry to see the full details of the request and response in the panes.
4. Click **Stop** when done.

In the demo, the whole UI TestCase produces a single HTTP request, because the sample application is almost entirely front-end. Manually triggering a backend action, generating a document from the page, adds a second message with content type `application/pdf` and result `200`. That is the point of the recorder: it shows which interactions actually hit a backend and what they send.

## Exporting the captured messages

1. **Select every message** you want. Only the selected messages are exported; the source first exports with one selected and gets one.
2. Click **Export**.

API Scan creates a folder `Trace_import` with one folder per message, each containing the message with its endpoint, resource and payload exactly as recorded. From here the workflow is the usual one: adjust the messages, run them, and export them to Commander as described in [API TestCases](/ToscaBase/api-testing/api-test-cases/).

Clearing the list and pressing **Start** again begins a fresh session.

## When to use it

- The developers have not provided API documentation, but you know the application talks to an API.
- You want to see which backend calls a UI flow triggers before deciding what to test at API level.
- A new API is under development and you want to capture real calls to start verification early.

:::tip
Run the recorder while an existing UI TestCase executes: you get the exact requests behind the flow you already automate, ready to be turned into faster API-level checks.
:::
