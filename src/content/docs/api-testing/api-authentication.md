---
title: API authentication
description: Authorizing API requests in Tosca API Scan with Basic and Digest authentication, how Digest differs under the hood, and where token and scan-time credentials go.
level: 3
sidebar:
  order: 30
sources:
  - id: ZDUQj2z3m7o
    title: "Tosca Tutorial | Lesson 83 - Authorize API requests using Basic Authentication | API Testing |"
    url: https://www.youtube.com/watch?v=ZDUQj2z3m7o
    at: "00:14"
  - id: f5vrILeqbmQ
    title: "Tosca Tutorial | Lesson 84 -  Authorize API requests using Digest Authentication | API Testing |"
    url: https://www.youtube.com/watch?v=f5vrILeqbmQ
    at: "00:07"
---

Most real APIs reject a request that carries no credentials. In Tosca API Scan every message has an **Authentication** setting where you choose the mechanism the API expects and enter the credentials; Tosca then takes care of the protocol. The sources demonstrate Basic and Digest authentication; the other mechanisms are listed for completeness.

## Available mechanisms

The authentication drop-down of a message offers, among others:

| Mechanism | What you enter | Notes |
|---|---|---|
| Basic | Username, password | The most common one |
| Digest | Username, password | Same input as Basic; a hashed multi-step exchange underneath |
| OAuth 2.0 | Token-based | Listed in the source, not demonstrated |
| NTLM | Windows credentials | Listed in the source, not demonstrated |
| Kerberos | Windows credentials | Listed in the source, not demonstrated |

Pick the one your API is documented to use; sending Basic credentials to a Digest-protected endpoint will not authorize the request even though the input looks identical.

## Basic authentication

1. Create a message (the source names it `Basic auth` in an `Authentication` folder) and set the endpoint to a protected resource. The demo uses the Postman Echo service, `postman-echo.com/basic-auth`, but any username and password protected API works.
2. Run it **without** authentication first. The response is status `401 Unauthorized` with the payload `Unauthorized`: the server wants credentials in the request before it answers.
3. Go back to the **Request** tab, set authentication to **Basic**, enter the **username** and **password**.
4. Run again. The status is now `200` and the payload reports `authenticated: true`.

## Digest authentication

From the client side Digest looks exactly like Basic: you select **Digest**, enter username and password, and run. The difference is what happens on the wire:

1. The client (Tosca) sends the request.
2. The server answers `401 Unauthorized`, but its `WWW-Authenticate` header carries a **realm** and a **nonce**.
3. The client sends the request again with an `Authorization` header in which the credentials are **hashed** using those values, so the password never travels in clear text.
4. The server verifies the hash and answers `200` with the payload.

So two requests and two responses are exchanged instead of one pair. Tosca performs the whole exchange internally; in API Scan you only see the final `200`.

The demo uses a Tricentis sample service protected by Digest (the "secured employee" API, version 2, on the Tricentis web service host). Without authentication it returns `401`; with **Digest** and the sample credentials it returns `200` and the employee data.

:::note
The exact URL of the sample service is not intelligible in the transcript. Take it from the Tricentis API services page rather than from this doc.
:::

## Other places credentials appear

- **Token from a login call.** Some APIs issue a token from a login request, which you then send as a header parameter with every other request. In a TestCase you buffer the token from the login response and reference the buffer in the header of the following requests; the worked example is in [API TestCases](/ToscaBase/api-testing/api-test-cases/).
- **Scanning a protected definition.** The **Advanced** section of the scan dialog takes a username and password (and proxy settings) for the definition file itself; see [API Scan basics](/ToscaBase/api-testing/api-scan-basics/). This is separate from the per-message authentication above.
- **Message Recorder.** Its **Configure** option takes proxy credentials and can decrypt HTTPS traffic; see [Message Recorder](/ToscaBase/api-testing/api-message-recorder/).

:::tip
Whatever mechanism you use, keep the `401` run as a negative TestCase: it proves the endpoint is actually protected.
:::
