---
title: API Scan basics
description: What API testing in Tosca is for, how to launch Tosca API Scan, send a request by hand, and scan a Swagger, OpenAPI, WSDL or WADL definition into ready-made messages.
level: 3
sidebar:
  order: 10
sources:
  - id: hJ395Eb3dng
    title: "Tricentis Tosca Tutorial Part-12: Tosca Api Testing and TOSCA Scan | Tosca Api Automation"
    url: https://www.youtube.com/watch?v=hJ395Eb3dng
    at: "00:15"
  - id: omYYNn94Vpc
    title: "Tosca Tutorial | Lesson 79 - What is API Scan | How to Send or Receive API requests | API Testing |"
    url: https://www.youtube.com/watch?v=omYYNn94Vpc
    at: "01:09"
  - id: OId0okYmuM8
    title: "Tosca Tutorial | Lesson 80 - Scan API Definition File and URI using  | Tosca API Scan | API Testing|"
    url: https://www.youtube.com/watch?v=OId0okYmuM8
    at: "00:08"
---

Tosca tests web services through its **API Engine**, and the tool you work in is **Tosca API Scan**: a separate window where you compose API messages, send them, read the responses and, most importantly, scan an API definition so that every request of the service is created for you. This doc covers why API testing matters, how to open API Scan, how to send a request manually, and how to scan a definition file or URI. Turning the scanned messages into Modules and TestCases is covered in [API TestCases](/ToscaBase/api-testing/api-test-cases/).

## Why test APIs in Tosca

An API (application programming interface) lets two applications talk through a common message format such as XML or JSON. In a landscape where, say, SAP, a mobile app, a web portal and a billing system are integrated, each system sends API requests and receives responses, and the API routes the messages to the target system. API testing checks that this core functionality works **without going through the UI layer**.

Benefits the sources list for doing it in Tosca:

- Core functionality can be validated before the UI exists or while it is being modified, so testing starts much earlier than UI-based functional testing.
- Frequent application changes are retested quickly; API TestCases are fast to create and maintain.
- Execution is much faster than UI automation, and no UI appears during a run.
- A standalone API Scan wizard scans an API in the simplest possible way.

The overall flow is: identify the API details and functional flow from the API services or documentation, scan the API with API Scan to create Modules, generate TestCases and parameterize them, then execute and share the reports.

## Two ways to open API Scan

1. **From Tosca Commander**: open the **API Testing** tab and click **Start API Scan**. The wizard takes a few seconds to appear.
2. **Standalone**: search Windows for `API Scan` and run it. Tosca Commander does not need to be running.

The window and its features are identical either way. The differences:

| | From Commander | Standalone |
|---|---|---|
| License | Needs Commander (licensed) | **No license required** |
| Getting messages into Commander | Export creates the folders directly in the Commander project | Export writes a subset file that you import into Commander |

The standalone tool is meant to be shared with developers and API architects: they can send and check requests, and even scan their APIs, without a Tosca license. When you want verifications, parameterization and integration with UI TestCases, you need Commander.

## Sending a request by hand

The left pane holds a tree: a project (you can rename it), folders and **messages**. A message is one API request together with its response.

1. Create a message in a folder and give it a meaningful name, for example `Get list of users`.
2. Choose the **method**. All REST methods are offered; `GET`, `POST`, `PUT` and `DELETE` are the ones you will use most.
3. Enter the **endpoint** and the **resource**. The endpoint is the part common to every request of the API; the resource is the unique location on the server you read from or write to, for example `/api/users?page=2`.
4. Add a **payload** if the method needs one (a `GET` has none, a `POST` usually does).
5. Add parameters if needed. Three kinds are available: **query**, **path** and **header** parameters.
6. Set **authentication** if the API is protected (Basic, OAuth 2.0, Digest, NTLM, Kerberos; see [API authentication](/ToscaBase/api-testing/api-authentication/)), add **attachments** or a **security protocol** if applicable.
7. Click **Run** at the top.

After the run, the message switches from the **Request** tab to the **Response** tab; you can switch back at any time. The response shows the **status code** (for example `200`), the **response time**, and the response **payload** (the JSON with all user details in the example). For the request headers, payloads and the search, validate and formatting helpers, see [Message structure, SOAP and attachments](/ToscaBase/api-testing/api-message-structure-and-soap/).

## Scanning an API definition

Rather than typing every request, scan the definition. The two buttons at the top left of the wizard are:

- **File**: a local definition file, such as WSDL, WADL, Swagger or OpenAPI (for example a Swagger JSON export).
- **URI**: the URL of the definition, for example the Petstore `swagger.json`. The same formats are supported.

Select the folder that should receive the result first, then click **URI** (or **File**), enter the address (or pick the file) and click **OK**. The **Advanced** section of the dialog takes a **username and password** if the definition itself is protected, and a **proxy** address with its username and password.

What the scan produces, for the Petstore example:

- A folder named after the API (`Swagger Petstore`) with one subfolder per resource (`pet`, `store`, `user`), mirroring the Swagger documentation.
- Inside each, one message per request type (`POST` add pet, `PUT` update pet, `GET` find by status, and so on). Each message is wrapped in an extra node; you only work with the request itself.
- Endpoint, resource and method are filled in. `POST` and `PUT` payloads contain default values. `GET` messages have their query parameters listed, but the **values are empty**.

The scan does not know which values to send, and it cannot fill in your credentials. So after scanning, fill in the parameters and authentication and run one message to prove the scan works. In the example, `GET /pet/findByStatus` needs the query parameter `status`; the documentation allows three values, and `available` returns status `200` with every available pet.

:::tip
Scanning cuts out most of the preparation work. It is worth doing even when you only want to check an API manually, because the whole folder and message structure comes for free.
:::

## A protected sample API

The LambdaGeeks part scans the Tricentis sample Swagger service instead. Its `auth` folder holds the login request: the payload carries `user` and `password`, and running it returns a **token** and an `expires` timestamp. The token is then supplied with every other request, for example `GET` all coffees (empty payload; status `200` and the coffee list in JSON), `POST` coffee (`description`, `id` and `name` in the payload), delete coffee or search coffee by `id` (the `id` is mandatory). The full parameterized version of this scenario is in [API TestCases](/ToscaBase/api-testing/api-test-cases/).

:::note
The Whisper transcript has the token entered on the "Perms tab" of the `GET` request, most plausibly the **Params** tab; the exact tab name is not confirmed by the audio. In the QASCRIPT lessons the token is passed as a header parameter, which is the same idea.
:::

## Limits of API Scan on its own

Inside API Scan you can call any request with data and read the response, much like Postman. What you cannot do there is parameterize data, verify values or run the messages as part of a test. For that, export the messages to Tosca Commander, which creates API Modules and TestCases: see [API TestCases](/ToscaBase/api-testing/api-test-cases/). To capture the calls an application makes rather than scan a definition, use the [Message Recorder](/ToscaBase/api-testing/api-message-recorder/).
