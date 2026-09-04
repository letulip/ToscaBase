---
title: API testing
description: Testing REST and SOAP services with Tosca API Scan and the API Engine, from the first manual request to chained, verified API TestCases.
level: 3
sidebar:
  order: 0
---

Tosca tests web services through its API Engine and the **Tosca API Scan** tool. You scan an API definition or record live traffic to get messages, send and inspect them in API Scan, then export them to Tosca Commander where they become API Modules and TestCases with verifications, buffers and Configuration Parameters, exactly like UI tests.

| Doc | What it covers |
|---|---|
| [API Scan basics](/ToscaBase/api-testing/api-scan-basics/) | Why test APIs, launching API Scan from Commander or standalone, sending a request by hand, scanning a Swagger, OpenAPI, WSDL or WADL file or URI |
| [API TestCases](/ToscaBase/api-testing/api-test-cases/) | Exporting messages, request and response Modules, the Technical view, ModuleAttributes, verifying status codes and payload fields, buffering values to chain requests, ExecutionLists |
| [API authentication](/ToscaBase/api-testing/api-authentication/) | Basic and Digest authentication, how Digest works underneath, tokens and scan-time credentials |
| [Message structure, SOAP and attachments](/ToscaBase/api-testing/api-message-structure-and-soap/) | Validate, Pretty Print, Word Wrap and Search in payload; scanning and verifying a SOAP calculator with Configuration Parameters and MATH; sending file attachments |
| [Message Recorder](/ToscaBase/api-testing/api-message-recorder/) | Recording the traffic of a running application and exporting the captured calls as messages |

Read them in order. The first two docs are the core workflow; the remaining three add authentication, message tooling, SOAP and attachments, and traffic recording on top of it.
