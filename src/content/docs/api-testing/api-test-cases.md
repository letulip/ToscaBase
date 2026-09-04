---
title: API TestCases
description: Export API Scan messages into Tosca Commander, add ModuleAttributes for status codes and payload fields, verify responses, buffer values to chain requests, and run API TestCases from an ExecutionList.
level: 3
sidebar:
  order: 20
sources:
  - id: NXR5dZ-DYHw
    title: "Tricentis Tosca Tutorial Part-13: Advance Tosca Api Testing And Tosca API Test Case"
    url: https://www.youtube.com/watch?v=NXR5dZ-DYHw
    at: "00:15"
  - id: rdxTMtZrVEs
    title: "Tosca Tutorial | Lesson 81 - Generate & Execute API Test Cases | API Testing |"
    url: https://www.youtube.com/watch?v=rdxTMtZrVEs
    at: "02:08"
  - id: 4Y9u474ohJM
    title: "Tosca Tutorial | Lesson 82 - Buffer API Response Values | Configure Request Parameters | API Testing"
    url: https://www.youtube.com/watch?v=4Y9u474ohJM
    at: "01:16"
  - id: tkUDG21IiMA
    title: "Tosca Tutorial | Lesson 86 - Scan & Verify SOAP API Messages | API Testing |"
    url: https://www.youtube.com/watch?v=tkUDG21IiMA
    at: "03:13"
---

Messages in [API Scan](/ToscaBase/api-testing/api-scan-basics/) can be sent, but not verified or parameterized. To test an API you export the messages into Tosca Commander, where each one becomes a pair of **API Modules** and a TestCase. You then add ModuleAttributes for the fields you care about, verify the response, buffer values from one response to use in the next request, and run everything from an ExecutionList.

## Exporting messages from API Scan

1. In Commander, create a **component folder** for the API (for example `API testing`) and **select it**. If nothing is selected, the export lands in the root folder. The workspace, or at least the target folder, must be **checked out**; in a multi-user workspace the export fails otherwise (see [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/)).
2. In API Scan, **select every message** you want to export. Only selected messages are exported; with one message selected you get exactly one.
3. Go to **API Test Case > Export** and close API Scan once the process finishes.

If API Scan was started standalone, the same menu instead saves a **subset** (`.tsu` file). In Commander, select the component folder, import the subset, and you get an import folder with the same Modules and TestCases. When API Scan was started from Commander, the objects appear directly (the LambdaGeeks part shows them under a folder named `API Scan_import`).

What the export creates:

- **Modules**: **two per message**, one for the request and one for the response, grouped in folders that mirror the message folders. Three messages therefore give six Modules. Rename them to fit your application if you like.
- **TestCases**: one per message, each with **two TestSteps**, request and response.

## The Technical view

API Modules have an extra tab, **Technical view**, that ordinary scanned Modules do not have. It is the same view as in API Scan: method, endpoint, resource, header parameters and payload for the request; status code, response time and payload for the response. Because everything the message needs is stored there, a generated TestCase runs as it is, without opening API Scan.

Run one and look at the log: it passes, but it only reports the server response time. Nothing has been verified yet.

## Adding ModuleAttributes

To verify or parameterize anything, turn message elements into ModuleAttributes. These are the API equivalent of Business Parameters: values you can set per TestCase.

1. Open the Module and its **Technical view**.
2. Select the element: the status code, a payload field, the response time, or a parameter. Multi-select works; selecting everything adds every payload item at once.
3. Click **Add** at the top of the **API Testing** tab.

The attribute immediately shows up in every TestCase that uses the Module. In the TestStep, either pick a value from the drop-down (it holds the values captured by the scan) or type one, and set the ActionMode (see [ActionModes](/ToscaBase/test-cases/action-modes/)).

:::note
The LambdaGeeks part describes the same operation as opening an "attribute assistant" through an option the subtitles render as "buffer module attributes with dynamic list items", where you select fields and click **Add**. The wording is unreliable; the QASCRIPT steps above are the confirmed path.
:::

## Verifying the response

The minimum verification for every request is the **status code**: add it from the response Module, set the value to `200` and the ActionMode to `Verify`. The log then shows the expected and actual value, and the TestCase fails if they differ. Add payload fields the same way; in the Petstore example the `name` sent in the `POST` request is verified in the response.

:::caution
The scan captures whatever values the last run produced. In the source, the request name had been changed after scanning, so the response Module still held the old name, and a `404` was recorded for a status code from a run that had failed. Never trust scanned values: configure the request values you send, and verify the response values you expect.
:::

To send a different value, add the field from the **request** Module too and set it in the request TestStep (`Max` for the pet name in the example).

## Buffering values to chain requests

A `GET` or `DELETE` by ID needs the ID the `POST` returned. Chain the requests through a buffer (see [Buffers](/ToscaBase/data-and-parameters/buffers/)):

1. In the response Module of the `POST`, add `id` as a ModuleAttribute.
2. In the `POST` TestCase, set its ActionMode to `Buffer` and enter the buffer name as the value, for example `B_pet_ID`.
3. In the `GET` and `DELETE` request Modules, add the path parameter `petId` (and, for `DELETE`, the `api_key` header) as ModuleAttributes.
4. In those TestCases set `petId` to `{B[B_pet_ID]}`. A constant such as the API key can stay literal or become a Test Configuration Parameter (see [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)).

Run the `POST` in ScratchBook: the log shows the returned ID stored in `B_pet_ID`, and the following requests use it. Add a status code verification to the `GET` and `DELETE` responses as well.

Because the order matters, rename the TestCases `01_post_request`, `02_get_request`, `03_delete_request` and drag them into that sequence. A useful negative TestCase is a `GET` by ID after the `DELETE`, which should return `404`.

## Worked example: token login, create, verify

The LambdaGeeks part builds one TestCase, `Add Coffee`, against the Tricentis sample Swagger service with three TestStep folders: `Authentication`, `Post Coffee`, `Verify New Coffee`. Drag the request and response Modules into the matching folders.

| TestStep | Values |
|---|---|
| Login request | `username`, `password` |
| Login response | Verify `status code`; buffer `token` as `auth_token` |
| Post coffee request | `name` = `test 1`, `description` = `test coffee`, `authorization` = the word `token`, a space, then `{B[auth_token]}` |
| Post coffee response | Verify `status code`; buffer `id` |
| Get coffee by id request | `id` = the buffered id, `authorization` as above |
| Get coffee by id response | Verify `status code` = `200`, verify `name` = `test 1` |

:::note
The subtitles give the login status code as "0 ok" and the final one as "200 ok". The first is most likely a mishearing of `200`; only the response of the service can confirm it.
:::

## Running API TestCases

Run from ScratchBook, or create an ExecutionList folder (for example `API Suite`), an ExecutionList (`Swagger App`), drag the TestCases in, keep them in order and **Run** (see [ExecutionLists](/ToscaBase/execution/execution-lists/)). No UI appears during execution. The execution log shows the status of each request and response, the value that was buffered and the value that was used later; the [Buffer Viewer](/ToscaBase/data-and-parameters/buffers/) lists the buffers. Save and check in the workspace afterwards.
