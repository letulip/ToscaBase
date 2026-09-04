---
title: Learning path
description: Recommended reading order through ToscaBase, from first concepts to enterprise setup.
level: 1
sidebar:
  order: 5
---

A curated route through the knowledge base, ordered so that every doc builds on the ones before it.
Follow it top to bottom if you are new to Tosca; jump to a level if you already know the basics.
Every doc carries its level as a badge, and the [Glossary](/ToscaBase/reference/glossary/) explains any term you meet on the way.

The four levels match the sidebar groups: Foundations (what Tosca is and how Modules and TestCases work),
Building tests (data, expressions, reusable pieces and execution), Specialised (engines, API testing,
reporting, best practices and troubleshooting) and Enterprise (multi-user administration).

## Level 1 · Foundations

After this level you can install Tosca, create a workspace, scan an application into Modules with XScan, make every control uniquely identifiable, and build and run a TestCase with the right ActionModes, conditions, loops and recovery scenarios in the ScratchBook.

### [Getting started](/ToscaBase/getting-started/)

1. [What is Tosca](/ToscaBase/getting-started/what-is-tosca/) — Tricentis Tosca in one page - a scriptless, model-based test automation platform, its main features, the applications it supports, and how it compares with Selenium.
2. [Architecture](/ToscaBase/getting-started/architecture/) — The components of the Tosca suite - Tosca Commander, XScan, Executor, the test repository and the license server - and the interfaces through which Tosca is used.
3. [Licensing](/ToscaBase/getting-started/licensing/) — How to get a Tosca trial or training license - support portal registration, the training license request page, the tricentis.com free trial, and connecting Tosca Commander to the cloud-hosted license server.
4. [Installation](/ToscaBase/getting-started/installation/) — Download the Tosca installer, walk through the setup wizard, install the browser extension for XScan, and optionally run Tosca on an AWS EC2 Windows Server instead of a local machine.
5. [Tosca Automation Extension](/ToscaBase/getting-started/tosca-automation-extension/) — Why XScan needs the Tosca Automation Extension in the browser, how to install it in Chrome and Edge by hand, and a tour of the Tricentis demo web shop that the Tosca 16 lessons automate.
6. [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/) — What a Tosca workspace is, the difference between single-user and multi-user workspaces, the standard workspace template, and step-by-step creation of a single-user workspace.
7. [Commander overview](/ToscaBase/getting-started/commander-overview/) — A tour of Tosca Commander - the start page and the First Steps sample project, the workspace sections, what a TestCase looks like inside, Test Configuration Parameters, and running a TestCase in the ScratchBook.
8. [First TestCase](/ToscaBase/getting-started/first-test-case/) — Build and run a complete login TestCase from scratch - folder structure, scanning the page into a Module, dragging the Module into the TestCase, values and ActionModes, the Browser Test Configuration Parameter, opening and closing the browser, and running in the ScratchBook.
9. [What's new in Tosca 16](/ToscaBase/getting-started/whats-new-in-tosca-16/) — The Tosca 16.0 release - Tosca ID Mapper and ARIA support for Oracle and other ERP applications, the new themes, TestCase pre-execution approval, and the list of smaller enhancements.
10. [Agentic test automation](/ToscaBase/getting-started/agentic-test-automation/) — Tosca Agentic Test Automation in Tricentis Tosca Cloud - what it is, how an agent turns plain-English steps into Modules, a TestCase and a run, what you need before it works, and the limits stated in the source.

### [Modules](/ToscaBase/modules/)

11. [Modules overview](/ToscaBase/modules/modules-overview/) — What a Tosca Module is, how ModuleAttributes map to controls, classic Modules versus XModules, the engines behind them, and standard versus user-defined Modules.
12. [XScan](/ToscaBase/modules/xscan/) — Scan a running application with XScan to create a TBox Module, pick controls on screen, read the unique / not unique feedback, and save the Module.
13. [Control identification](/ToscaBase/modules/control-identification/) — The four ways XScan identifies a control (properties, anchor, image, index), the order to try them in, and the ExplicitName parameter for steering one of many identical controls from the TestCase.
14. [Rescan Modules](/ToscaBase/modules/rescan-modules/) — Use Rescan to reopen an existing Module in XScan, add technical properties to a control that is not unique, add missing controls, and update the TestCases that use it.
15. [Duplicate and merge Modules](/ToscaBase/modules/duplicate-and-merge-modules/) — Find duplicate Modules in the workspace and merge them with the Module merge assistant, including resolving attribute conflicts and what happens to TestCases that use the merged Module.
16. [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/) — The properties Tosca stores on Modules and ModuleAttributes (cardinality, business type, synchronization policy, IDs) and the four parameter types, configuration, identification, steering and transition, with the ones you will actually use.
17. [Table controls](/ToscaBase/modules/table-controls/) — How a scanned table is structured in a Module, the row, column and cell selectors, the ActionModes and properties for tables, worked steering examples, embedded controls inside cells, and verifying row and column counts.
18. [Table baseline comparison](/ToscaBase/modules/table-baseline-comparison/) — Save a snapshot of a web table as a baseline, compare later executions against it, exclude dynamic rows and columns, and update or auto-generate baselines.
19. [Control groups](/ToscaBase/modules/control-groups/) — Group related ModuleAttributes into a control group in XScan, name the group, and split it back into separate attributes when it no longer helps.

### [Test cases](/ToscaBase/test-cases/)

20. [TestCase basics](/ToscaBase/test-cases/test-case-basics/) — What a Tosca TestCase is, technical versus business TestCases, how TestSteps are built from Modules, TestStep folders that mirror the business flow, entering values, and a first end-to-end example with WaitOn, Input and Verify.
21. [ActionModes](/ToscaBase/test-cases/action-modes/) — Complete reference for the Tosca ActionModes - Input, Insert, Verify, Buffer, WaitOn, Select and Constraint - with value syntax and settings, and links to the worked examples.
22. [Control flow](/ToscaBase/test-cases/control-flow/) — If/Then/Else conditions and While and Do-While loops inside a TestCase - how to create them, what goes in the Condition, and how the Maximum repetitions property prevents infinite loops.
23. [Repetitions](/ToscaBase/test-cases/repetitions/) — Run the TestSteps in a folder a fixed number of times with the Repetition property, set through the column chooser or the folder's properties, or a number of times computed at run time from a buffer.
24. [Recovery and Cleanup Scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/) — How the Tosca recovery engine retries a failed TestCase - enabling recovery globally or per folder, creating a Recovery Scenario Collection, setting the Retry level, and adding a Cleanup Scenario for when the TestCase cannot be recovered.
25. [Recorder](/ToscaBase/test-cases/recorder/) — Record your actions on an application and let Tosca generate the Modules and a TestCase automatically - the recorder toolbar, verification mode, settings, what gets generated and what you still have to fix.
26. [Exploratory testing](/ToscaBase/test-cases/exploratory-testing/) — Tosca's exploratory testing support - explorative sessions, recording an interaction with the Explorative Scenario Manager, and exporting the resulting scenario document with screenshots to PDF or DOCX.

## Level 2 · Building tests

After this level you can keep test data apart from TestCases with TestCase-Design, use the TBox Standard Modules and dynamic expressions in TestStepValues, share values through Buffers, Test Configuration Parameters and reusable TestStepBlocks, and run everything from ExecutionLists, read the results, and automate runs through a scheduler, Jenkins or distributed execution.

### [Test case design](/ToscaBase/test-case-design/)

1. [TestCase-Design overview](/ToscaBase/test-case-design/test-case-design-overview/) — What TestCase-Design (TCD) is, which objects it consists of, why test data is kept apart from TestCases, and the workflow from TestSheet to generated TestCases.
2. [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/) — Create a TestSheet in the TestCase-Design section, structure it with the four recommended attributes, and set the Business Relevant property to yes, no or result.
3. [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/) — Instances as attribute values and as TestCases, the Character and Position properties, and the four combinatorial methods (all combinations, orthogonal, pairwise, linear expansion).
4. [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/) — Convert a TestCase into a template, link it to a TestSheet through the schema path, check it, instantiate it into generated TestCases, make TestSteps conditional and reinstantiate after changes.
5. [Design classes](/ToscaBase/test-case-design/design-classes/) — TestCase-Design classes hold attributes and instances shared by several TestSheets; class references keep them centrally managed, and resolving a reference detaches a copy.
6. [Worked example: end to end](/ToscaBase/test-case-design/worked-example-end-to-end/) — One pass through TestCase-Design on the Vehicle Insurance sample, from a TestSheet with attributes and instances to generated TestCases in an ExecutionList, with links to each concept.

### [Standard modules](/ToscaBase/standard-modules/)

7. [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/) — TBox Standard Modules for creating, copying, comparing and deleting files and folders, and for checking that a folder exists.
8. [Buffer operations](/ToscaBase/standard-modules/buffer-operations/) — The four TBox buffer Modules (Set Buffer, Partial Buffer, Name to Buffer, Delete Buffer) and how to use them to extract a value such as an order number.
9. [Start and close programs](/ToscaBase/standard-modules/start-and-close-programs/) — Use TBox Start Program to launch applications with arguments, close them with taskkill, clear the Chrome cache with cmd, and measure step duration with TBox Start/Stop Timer.
10. [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/) — TBox Evaluation Tool compares two dynamic expressions (buffers, Test Configuration Parameters, literals) with a true/false result; use it for verifications and as an If condition, quoting the operands.
11. [Screenshots on failure](/ToscaBase/standard-modules/screenshots-on-failure/) — Take a screenshot at any TestStep with TBox Take Screenshot, and let Tosca capture one automatically on every failed verification through the project settings.
12. [Window operations](/ToscaBase/standard-modules/window-operations/) — TBox Window Operation (bring to front, maximise, minimise, close, wait on open) and TBox Scroll Window Operation, including how to close a popup window without scanning it.
13. [Desktop dialogs](/ToscaBase/standard-modules/desktop-dialogs/) — Automate the Windows Save As dialog with the TBox Save As Module, including the confirmation popup that may follow the Save click.
14. [Execute JavaScript](/ToscaBase/standard-modules/execute-javascript/) — Run JavaScript in the browser with the Execute JavaScript Module and check a script's return value with Verify JavaScript Result; both need a Browser Test Configuration Parameter.

### [Expressions](/ToscaBase/expressions/)

15. [Random values](/ToscaBase/expressions/random-values/) — Generate random numbers, decimals and strings in TestStepValues with RND, RNDDECIMAL and RANDOMTEXT, and handle random values the application produces.
16. [Date expressions](/ToscaBase/expressions/date-expressions/) — Generate, calculate and format dates and times with DATE, MONTHFIRST, LDAY and related expressions, and fix the Tosca date format problem.
17. [String operations](/ToscaBase/expressions/string-operations/) — Length, case conversion, occurrence counting, trim, replace with escaped characters, Base64 encode/decode, and arithmetic on cleaned strings.
18. [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/) — Verify a value within a numeric range with INTERVAL, use regular expressions in ModuleAttributes and Verify steps for multilingual identification, and split a value into buffers with named groups.

### [Data and parameters](/ToscaBase/data-and-parameters/)

19. [Buffers](/ToscaBase/data-and-parameters/buffers/) — What a Tosca buffer is, how to create one with the Buffer ActionMode or TBox Set Buffer, read it with {B[name]}, extract dynamic text with the XBuffer {XB[name]}, and inspect or edit buffers in the Buffer Viewer.
20. [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/) — Test Configuration Parameters (TCPs) hold environment and settings data outside the TestSteps; where to define them, the {CP[name]} syntax, system-defined parameters, and project-level Configurations.
21. [Business Parameters and TestStepLibraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/) — Group TestSteps into TestStepBlocks, move them into a TestStepLibrary as reusable TestStepBlocks referenced from many TestCases, and pass different data into each reference with Business Parameters.
22. [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/) — Tosca's Test Data Services (TDS) register test data centrally on Tosca Server, track its state across processes and share it between applications; how repositories, types and items work in the web interface and which Test Configuration Parameters a TestCase needs to use them.
23. [Test Data Service Modules](/ToscaBase/data-and-parameters/test-data-service-modules/) — The Standard Modules that drive Test Data Services from a TestCase (Create and Provide New Item, Find and Provide Item, Update Item, Move Item to Type, Delete Item, Expert Module), the create-find-update flow, reading items with {TDS[type.attribute]}, and generating bulk data with random values and Repetitions.

### [Execution](/ToscaBase/execution/)

24. [ExecutionLists](/ToscaBase/execution/execution-lists/) — Why ExecutionLists replace the ScratchBook once a TestCase is ready, how to build one from folders and TestCases, run it, and keep it synchronised with the TestCases section.
25. [Results and logs](/ToscaBase/execution/execution-results-and-logs/) — Reading the ActualLog of an ExecutionList, changing its view, trend charts, clearing and archiving logs, copying results to Excel, and the LogViewer for low-level diagnostics.
26. [Manual execution](/ToscaBase/execution/manual-execution/) — Running an execution entry as a manual TestCase through the checklist window, attaching screenshots and comments, switching back to automation, and setting a result by hand.
27. [Repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/) — Running an execution entry several times with the Repetitions property, and assembling business TestCases and business ExecutionLists into an end-to-end view for stakeholders.
28. [Recording executions](/ToscaBase/execution/recording-executions/) — Recording ScratchBook and ExecutionList runs as MP4 with the Execution Recorder setting, limiting it to failures, and excluding TestCases with the AvoidExecutionRecorder Test Configuration Parameter.
29. [DokuSnapper](/ToscaBase/execution/dokusnapper/) — Enabling DokuSnapper so every ExecutionList or ScratchBook run produces a document with the log and a screenshot per TestStep.
30. [Cross-browser execution](/ToscaBase/execution/cross-browser-execution/) — Running the same TestCase in several browsers by feeding the Browser Test Configuration Parameter from a Buffer, and fixing the "No feasible executor found" error caused by a TestStep without a Module.
31. [Scheduling executions](/ToscaBase/execution/scheduling-executions/) — Unattended runs without a CI server, by triggering a TCShell script through a batch file from Windows Task Scheduler.
32. [Jenkins integration](/ToscaBase/execution/ci-integration-jenkins/) — Running Tosca Commander tasks from a Jenkins freestyle job by executing a Windows batch file that calls TCShell with a .tcs script.
33. [Distributed execution (DEX)](/ToscaBase/execution/distributed-execution-dex/) — Setting up Tosca distributed execution with AOS: the AOS workspace, the DEX agent, Commander settings, Configurations, TestEvents, and matching agents to configurations.
34. [Tosca Execution Client](/ToscaBase/execution/tosca-execution-client/) — Triggering DEX TestEvents from the command line or a CI/CD pipeline with the Tosca Execution Client PowerShell/shell script, and calling it from Jenkins.
35. [Self-healing mode](/ToscaBase/execution/self-healing/) — What Tosca's self-healing mode does when a control changes in a new build, how self-healing properties are captured in XScan, how to enable the mode with the SelfHealing Test Configuration Parameter, and how healed steps appear in the log and get applied to the Module.

## Level 3 · Specialised

After this level you can automate Excel, PDF and XML documents and hard-to-scan desktop controls, test REST and SOAP services with API Scan, link tests to requirements and produce reports and TQL queries, follow Tricentis' best practices, and recognise and fix the classic automation obstacles.

### [Engines](/ToscaBase/engines/)

1. [Excel engine](/ToscaBase/engines/excel-engine/) — Compare two workbooks with Excel 1:1 File Compare, and create, fill, verify and read Excel sheets with the TBox Excel standard modules - open, worksheet, range, manipulation, close, row and column counts.
2. [PDF engine](/ToscaBase/engines/pdf-engine/) — Compare two PDFs with the 1:1 Compare standard module, scan text, images and tables with PDF Scan, and count pages of a PDF without page numbers.
3. [XML engine](/ToscaBase/engines/xml-engine/) — Open, create and verify XML files with the XML engine Modules, build XPath expressions, scan an XML file into a Module, and extract values from XML into buffers and web forms.
4. [UIA engine and desktop controls](/ToscaBase/engines/uia-engine-and-desktop/) — What to do when Application scan misses controls - switch the XScan engine (WinX, UIA, Vision AI), add generic list items to a combo box, and click JavaScript alerts.
5. [Mobile automation](/ToscaBase/engines/mobile-automation/) — Set up the Mobile engine with Tricentis Mobile Agent, map the application and connection configurations to a TestCase, automate a first Android TestCase with Open Mobile App on a real device and an emulator, and scan a native app on SauceLabs real devices through a Cloud APM connection.
6. [Tricentis Device Cloud](/ToscaBase/engines/device-cloud/) — What Tricentis Device Cloud offers a Tosca or Testim team - a farm of real smartphones and tablets with remote control, performance sessions analysed by a mobile AI engine into issue cards, and performance monitoring of user flows over time.

### [API testing](/ToscaBase/api-testing/)

7. [API Scan basics](/ToscaBase/api-testing/api-scan-basics/) — What API testing in Tosca is for, how to launch Tosca API Scan, send a request by hand, and scan a Swagger, OpenAPI, WSDL or WADL definition into ready-made messages.
8. [API TestCases](/ToscaBase/api-testing/api-test-cases/) — Export API Scan messages into Tosca Commander, add ModuleAttributes for status codes and payload fields, verify responses, buffer values to chain requests, and run API TestCases from an ExecutionList.
9. [API authentication](/ToscaBase/api-testing/api-authentication/) — Authorizing API requests in Tosca API Scan with Basic and Digest authentication, how Digest differs under the hood, and where token and scan-time credentials go.
10. [Message structure, SOAP and attachments](/ToscaBase/api-testing/api-message-structure-and-soap/) — The Validate, Pretty Print, Word Wrap and Search in payload tools of API Scan, scanning and verifying a SOAP service, and sending a file as an attachment.
11. [Message Recorder](/ToscaBase/api-testing/api-message-recorder/) — Capture the HTTP traffic between an application and its backend with the API Scan Message Recorder, inspect the calls, and export them as API messages to build TestCases from.

### [Requirements and reporting](/ToscaBase/requirements-and-reporting/)

12. [Requirements and risk weighting](/ToscaBase/requirements-and-reporting/requirements-and-risk/) — Structure requirements in Tosca, weight them by business risk, link TestCases and ExecutionLists to them, and read the coverage and execution-state dashboard.
13. [TQL search and virtual folders](/ToscaBase/requirements-and-reporting/tql-and-virtual-folders/) — Query the workspace with Tosca Query Language, filter ExecutionLists and TestCases by their properties, and save the query as a self-refreshing virtual folder.
14. [Reports and report definitions](/ToscaBase/requirements-and-reporting/reports/) — Export any section with Print View, print the built-in report definitions for ExecutionLists, TestCases and requirements, and create your own report definition with a data set, a TQL query and a designer.
15. [Import a folder structure from Excel](/ToscaBase/requirements-and-reporting/import-from-excel/) — Build a TestCase or component folder tree in Excel and paste it into Tosca Commander with Create Folder Structure, following the column-per-level rules.

### [Best practices](/ToscaBase/best-practices/)

16. [Naming conventions](/ToscaBase/best-practices/naming-conventions/) — Why consistent names for Modules, TestCases, folders and TestSteps decide whether a Tosca project stays maintainable, with a before-and-after example.
17. [TestCase structure](/ToscaBase/best-practices/test-case-structure/) — Four structural rules for a maintainable TestCase - always verify something, group TestSteps into folders, prefer Repetitions and Constraints over loops, and keep the Workstate current.
18. [Module hygiene](/ToscaBase/best-practices/module-hygiene/) — Keep Modules small and categorised by functionality, and merge duplicate Modules regularly, to protect workspace size and execution performance.
19. [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/) — Replace static TBox Wait steps with the WaitOn ActionMode and avoid mouse and keyboard methods in TestStepValues, with the Calculate / Send progress-bar example worked both ways.
20. [Review process](/ToscaBase/best-practices/review-process/) — A folder-based review workflow with three approval stages and the four-eyes principle for Modules, TestCases and other Tosca artifacts.

### [Troubleshooting](/ToscaBase/troubleshooting/)

21. [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/) — Same IDs, twins, changing IDs, multi-select lists, autocomplete boxes, hidden and off-screen elements, and how to steer each of them.
22. [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/) — Fake tables built from divs, rows that move, rows dragged into another table in order, counting rows, last-row values, cell search, row and column headers, and drop-downs embedded in cells.
23. [Obstacles: input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/) — Drag and drop, clicking until a label changes, entering text that Tosca mistakes for a command, clicking at an offset, and clicking at screen coordinates.
24. [Obstacles: loops and conditions](/ToscaBase/troubleshooting/obstacles-logic/) — Sorting numbers with a Do loop and an If statement, and playing a keyboard game with Do, If/Else and TBox Send Keys, for the rare cases where a TestCase genuinely needs logic.
25. [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/) — Switching browser tabs with SendKeys, steering one of two identical tabs with ConstraintIndex, counting all links or similar controls with ResultCount, and downloading and verifying a file with curl from Tosca.
26. [Worked example: end-to-end live project](/ToscaBase/troubleshooting/worked-example-live-project/) — Finishing the vehicle-insurance sample end to end with conditional template folders, data-driven price options, WaitOn for the confirmation, and ExecutionList reporting.

## Level 4 · Enterprise

After this level you can set up a multi-user workspace on a common repository, manage users, groups, branches, backups and versioning, let several testers share an ExecutionList through Test mandates, drive Commander from the command line, and operate Tosca Server.

### [Administration](/ToscaBase/administration/)

1. [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/) — Create a multi-user workspace on a shared repository (SQLite for practice, Oracle, MS SQL Server or DB2 for projects), work with Update All, Checkout, Checkout Tree and Check In All, inspect or revoke another user's check-out, and understand the Synchronization policy behind greyed-out folders.
2. [Users and groups](/ToscaBase/administration/users-and-groups/) — Create users and user groups in a multi-user workspace, set and change passwords, grant the Admins role, restrict sections with owning and viewing groups, disable users, and read the personal data report.
3. [Branches](/ToscaBase/administration/branches/) — Create a branch of a multi-user repository, work on it in a separate workspace, merge it back into Master and delete it, following a Git-like workflow.
4. [Backup and restore](/ToscaBase/administration/backup-and-restore/) — Back up a single-user project with Export subset, back up a multi-user common repository as an administrator, and restore it into a new repository.
5. [Versioning and recovery](/ToscaBase/administration/versioning-and-recovery/) — Manage the version history of a multi-user repository, read the change history of a project or a tree, and recover a deleted TestCase with Export subset for revision.
6. [Test mandates](/ToscaBase/administration/test-mandates/) — Let several users execute the same ExecutionList at the same time without overwriting each other's results by linking it to a Test mandate, and clear the auto-merge link when it is no longer needed.
7. [Command-line tools](/ToscaBase/administration/command-line-tools/) — Steer Tosca Commander from the command line with TCShell in interactive or script mode to execute ExecutionLists and check in, and clone a workspace for every team member with TCWorkspaceUtil instead of copying it.
8. [Tosca Server](/ToscaBase/administration/tosca-server/) — What Tosca Server is in the Tosca architecture, how to download and install it with matching Commander version, which services it runs, how to restart them, and what the dashboard and DEX monitor show.
