---
title: Message structure, SOAP and attachments
description: The Validate, Pretty Print, Word Wrap and Search in payload tools of API Scan, scanning and verifying a SOAP service, and sending a file as an attachment.
level: 3
sidebar:
  order: 40
sources:
  - id: udsDLQpUDrY
    title: "Tosca Tutorial | Lesson 85 - Search, Validate and Structure API message in API Scan | API Testing |"
    url: https://www.youtube.com/watch?v=udsDLQpUDrY
    at: "00:08"
  - id: tkUDG21IiMA
    title: "Tosca Tutorial | Lesson 86 - Scan & Verify SOAP API Messages | API Testing |"
    url: https://www.youtube.com/watch?v=tkUDG21IiMA
    at: "00:07"
  - id: 2ynHXKyfLFc
    title: "Tosca Tutorial | Lesson 87 - Send Attachments in API Messages using Tosca API Scan | API Testing |"
    url: https://www.youtube.com/watch?v=2ynHXKyfLFc
    at: "00:07"
---

Beyond sending and scanning, API Scan has a **Message** section with tools for checking and tidying a payload, it handles SOAP services with XML payloads the same way it handles REST, and it can attach files to a request. This doc covers those three features. Scanning itself is in [API Scan basics](/ToscaBase/api-testing/api-scan-basics/); building TestCases from the messages is in [API TestCases](/ToscaBase/api-testing/api-test-cases/).

## Payload tools in the Message section

Four options act on the payload of the selected message. They matter most when you look at freshly developed APIs or hand-written messages, before you test anything.

### Validate

Checks that the message and its payload are structurally correct, for example that a JSON body is well-formed. With a correct message the status line reports **No error found**. Remove a closing brace and **Validate** lists the validation errors, such as a JSON token not being valid for closing an object, with the **line and position**. Fix the payload and validate again. A message that fails validation will not get a response from the server, so this is the first thing to check when a request misbehaves.

### Pretty Print

Restores line breaks and indentation of the payload according to its format (JSON or XML). Useful after pasting or editing a body by hand.

### Word Wrap

Wraps very long lines so the whole payload fits in the pane. The source pastes an entire Petstore JSON definition, which arrives as one or two enormous lines; **Word Wrap** breaks it into readable lines, and **Pretty Print** afterwards restores the JSON structure. Together they make a large source file searchable.

### Search in payload

Opens a find dialog for the payload: **Find next** highlights the next match. Options include **match case**, **match whole word**, **regular expression**, **wildcards** and **search up** to search backwards. The **Replace** and **Replace all** buttons change text in place; the dialog reports when no more occurrences are found. The example renames a pet from `range` to `range1`.

## SOAP services

SOAP APIs use XML instead of JSON for both request and response, and the requests are `POST`. Scanning is identical to REST: choose **URI** (or **File**), give the WSDL address, click **OK**. The demo scans the Tricentis sample `calculator.svc` service; the result is a `Calculator` folder with one message per operation, `Add`, `Divide`, `Multiply`, `Subtract`. Open `Add`, put `10` in each operand node of the XML payload, run, and the response is status `200` with an XML payload whose result is `20`.

The only difference from REST is the payload format, so the checks you add are shaped by XML nodes rather than JSON fields. Everything else (export, Modules, TestCases, verifications) is the same.

### Verifying a SOAP calculation with Test Configuration Parameters

The source exports the `Add` message from the standalone API Scan as a subset, imports it into a `SOAP API testing` component folder (the mechanism is described in [API TestCases](/ToscaBase/api-testing/api-test-cases/)), then:

1. In the request Module, add both operand nodes as ModuleAttributes; in the response Module add the **status code** and the **result** node.
2. In the TestCase, verify the status code as `200`.
3. Create two Test Configuration Parameters, `num1` and `num2`, with values (see [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)), and set the request operands to `{CP[num1]}` and `{CP[num2]}` instead of static numbers.
4. Verify the result with a math expression over the same parameters: `{MATH[{CP[num1]}+{CP[num2]}]}` (see [Random values](/ToscaBase/expressions/random-values/) for the `MATH` expression). Count the braces; a missing one is the mistake the source makes on the first attempt.
5. Run in ScratchBook. The log shows both verifications, with expected and actual values equal.

This way the inputs can be changed in one place and the expected output is computed rather than hard-coded.

## Sending attachments

Some requests carry a file: an image, a document, a JSON source. To attach one:

1. Create a message (`test attachment` in the source), set the method to `POST` and the endpoint to a service that accepts uploads. The demo uses the Postman Echo service, which returns the content it received.
2. Under the payload, open the **Attachments** tab. Each attachment has a **Name**, a **File** and a **Content type**.
3. Click the **File** field; a **Load** button with an ellipsis appears. Click it and pick the file.
4. The content type is **detected automatically** and the name is filled from the file name; both can be edited.
5. Run. The response is status `200`, and Postman Echo returns the file content in the payload, encoded, so it is not human-readable.

Additional options on the tab are **Content transfer encoding**, **Content type**, **Omit file name** and **Enable MTOM**.

:::note
The speaker does not know what **Enable MTOM** does and does not explain the other three options. MTOM is a SOAP mechanism for transmitting binary attachments efficiently; the source gives no Tosca-specific detail, so leave the options at their defaults unless the API documentation asks for them.
:::
