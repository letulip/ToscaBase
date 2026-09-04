---
title: Engines
description: The Tosca engines for documents and hard-to-scan controls - Excel, PDF, XML, the UIA and WinX engines for desktop windows and browser dialogs, and the Mobile engine with Tricentis Device Cloud for native apps on real devices.
level: 3
sidebar:
  order: 0
---

Beyond web pages, Tosca steers files, native windows and mobile apps through dedicated engines. Each engine brings its own scan (PDF Scan, File Scan) or its own set of standard Modules, and the same ActionModes you already use in TestCases apply to what they expose.

Read in this order:

1. [Excel engine](/ToscaBase/engines/excel-engine/): open, create and compare workbooks, define ranges, read and verify cells, and buffer row and column counts with the TBox Excel Modules.
2. [PDF engine](/ToscaBase/engines/pdf-engine/): compare two PDFs with `1:1 Compare`, scan text, images and tables with PDF Scan, and count pages of a document without page numbers.
3. [XML engine](/ToscaBase/engines/xml-engine/): open and verify XML by XPath, scan an XML file into a Module, and chain the browser, file and XML engines in one TestCase.
4. [UIA engine and desktop controls](/ToscaBase/engines/uia-engine-and-desktop/): switch the XScan engine (WinX, UIA, Vision AI) when Application scan misses controls, add generic list items to a combo box, and click JavaScript alerts.
5. [Mobile automation](/ToscaBase/engines/mobile-automation/): reach a device through Tricentis Mobile Agent, map the application and connection configurations to a TestCase, open a native Android app with `Open Mobile App`, and scan an app on SauceLabs real devices through a Cloud APM connection.
6. [Tricentis Device Cloud](/ToscaBase/engines/device-cloud/): the Tricentis device farm with remote control, performance sessions turned into issue cards by a mobile AI engine, and performance monitoring of user flows.

For the HTML engine and everyday web controls see [Modules](/ToscaBase/modules/), and for problem controls in general see [Troubleshooting](/ToscaBase/troubleshooting/).
