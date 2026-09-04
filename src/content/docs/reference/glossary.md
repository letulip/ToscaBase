---
title: Glossary
description: Short definitions of every Tricentis Tosca term used in ToscaBase, each linked to the doc that explains it.
level: 1
sidebar:
  order: 10
---

Every Tosca term used in this knowledge base, in alphabetical order, with a one- or two-sentence definition and a link to the doc that explains it in depth. Tosca's own spelling is kept (`ExecutionList`, `TestStep`, `XScan`), because that is how the objects appear in Tosca Commander. If a term you meet in a doc is missing here, the doc that introduces it is the place to look, and the glossary should be extended.

## Symbols and numbers

**{DRAG} / {DROP}** — Built-in TestStepValues for drag and drop: `{DRAG}` on the source control and `{DROP}` on the target control in the same TestStep. See [Obstacles: input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/).

**{TDS[type.attribute]}** — Expression that reads an attribute of the Test Data Services item currently provided to the TestCase. TDQL (Test Data Query Language, e.g. `vehicle[make=="BMW"]`) filters which item is provided. See [Test Data Service Modules](/ToscaBase/data-and-parameters/test-data-service-modules/).

**1:1 Compare** — TBox standard Module of the PDF engine that compares a target PDF with a reference PDF at a given accuracy percentage, optionally excluding pages. See [PDF engine](/ToscaBase/engines/pdf-engine/).

## A

**ActionMode** — How a TestStepValue is applied to a control: `Input`, `Insert`, `Verify`, `Buffer`, `WaitOn`, `Select` or `Constraint`. See [ActionModes](/ToscaBase/test-cases/action-modes/).

**ActualLog** — The log object under an ExecutionList that holds the current execution results. It can be cleared, archived as a named snapshot (an archive can be dragged back to become current again) and charted as a trend chart of passed, failed and no-result counts over time. See [Results and logs](/ToscaBase/execution/execution-results-and-logs/).

**Anchor** — A uniquely identified neighbouring control used as a reference point to locate a control that is not unique on its own (Identify by anchor). See [Control identification](/ToscaBase/modules/control-identification/).

**AOS (Automation Object Service)** — Tosca Server service with its own workspace that mediates between Tosca Commander, the common repository and the DEX server during distributed execution. See [Distributed execution (DEX)](/ToscaBase/execution/distributed-execution-dex/).

**API Engine** — The Tosca engine that sends API requests and receives responses when API TestCases run. See [API testing](/ToscaBase/api-testing/).

**API message** — One request plus its response in API Scan; on export it becomes a request Module and a response Module. See [API Scan basics](/ToscaBase/api-testing/api-scan-basics/).

**API Module** — Module generated from an API message. It has an extra Technical view tab mirroring the API Scan message view, where payload elements and status codes are added as ModuleAttributes. See [API TestCases](/ToscaBase/api-testing/api-test-cases/).

**API Scan** — Tosca's separate tool, opened from Commander's API Testing tab or standalone (license-free), for composing, sending and scanning API messages. See [API Scan basics](/ToscaBase/api-testing/api-scan-basics/).

**ARIA support** — Tosca 16.0 feature that identifies ARIA-labelled controls natively; toggled under XScan settings > General settings. See [What's new in Tosca 16](/ToscaBase/getting-started/whats-new-in-tosca-16/).

**Attribute (TestCase-Design)** — A data parameter in a TestSheet or class, usually one per field or business object; attributes nest to any depth. See [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/).

## B

**Baseline (table)** — Saved snapshot of a table control that later executions are verified against, with dynamic rows and columns excluded. See [Table baseline comparison](/ToscaBase/modules/table-baseline-comparison/).

**Branch** — A separate line of development inside one multi-user repository; `Master` is the default. Branches are merged back and deleted in a Git-like workflow. See [Branches](/ToscaBase/administration/branches/).

**Buffer** — A named value written during execution (with the `Buffer` ActionMode or TBox Set Buffer) and read with `{B[name]}`. Buffers are local to the workspace and survive the run. See [Buffers](/ToscaBase/data-and-parameters/buffers/).

**Buffer Viewer** — Tools window that lists all buffers in the workspace and lets you search, rename, edit, add and delete them. See [Buffers](/ToscaBase/data-and-parameters/buffers/).

**Business Parameter** — Named input of a reusable TestStepBlock, referenced as `{PL[name]}` and valued separately for each reference. See [Business Parameters and TestStepLibraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/).

**Business Relevant** — TestSheet attribute property with the values `Yes`, `No` and `Result`, marking real test data, metadata or expected results. See [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/).

**Business TestCase** — Non-executable logical grouping of technical TestCases used to track coverage; a business ExecutionList links one business TestCase to several ExecutionLists and concatenates their results. See [TestCase basics](/ToscaBase/test-cases/test-case-basics/) and [Repetitions and business TestCases](/ToscaBase/execution/execution-repetitions-and-business-test-cases/).

## C

**Caption** — Window title by which TBox Window Operation, TBox Scroll Window Operation and similar Modules find a window; supports regular expressions. See [Window operations](/ToscaBase/standard-modules/window-operations/).

**Cardinality** — ModuleAttribute property (`0-1` by default, `0-n`) controlling how many times an attribute can be used in one TestStep. See [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/).

**Character and Position** — Instance properties in TestCase-Design: Character is `Valid`, `Invalid` or `Straight through`; Position is `Inner` or `Boundary`. See [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/).

**Check-out / Check-in** — The lock-based editing cycle of a multi-user workspace: Checkout or Checkout Tree locks objects, Check In All publishes changes, Update All fetches other users' check-ins. An administrator can revoke another user's checkout, discarding that user's changes. See [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).

**Class (TestCase-Design)** — Reusable set of attributes and instances shared by several TestSheets. A class reference is a read-only link from a sheet; resolving it detaches a local copy. See [Design classes](/ToscaBase/test-case-design/design-classes/).

**Cleanup Scenario** — TestSteps that run when the Recovery Scenario itself fails, restoring the application to a known state. See [Recovery and Cleanup Scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/).

**Combinatorial methods** — The Generate Instances options in TestCase-Design: all combinations, orthogonal, pairwise and linear expansion (recommended). Linear expansion needs one straight-through (happy-path) instance per attribute. See [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/).

**Common repository** — The database (SQLite, Oracle, MS SQL Server or DB2) that holds the master copy of all objects and that multi-user workspaces check out from. See [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).

**Condition** — An expression on an If, While or Do object that decides whether its TestSteps run; in TestCase-Design, a condition on a template TestStep or folder decides whether it is instantiated for a given sheet column. See [Control flow](/ToscaBase/test-cases/control-flow/) and [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/).

**Configuration (project-level)** — A reusable set of Test Configuration Parameters kept in the Configurations section and dragged onto TestCases, folders or ExecutionLists. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

**Configuration Parameter (Module-level)** — Per-ModuleAttribute steering setting such as `ExplicitName` or `ConstraintIndex`; distinct from a Test Configuration Parameter. See [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/).

**Constraint** — ActionMode that filters which row, node or control a TestStep addresses (for example a table row whose cell has a given value) instead of steering it. See [ActionModes](/ToscaBase/test-cases/action-modes/).

**ConstraintIndex** — Module-level Configuration Parameter that selects which of several identical browser tabs or windows a control is steered in. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

**Coverage Specified** — Share of a requirement covered by linked TestCases, weighted by their Workstate (Planned 20%, In Work 50%, Completed 100%). See [Requirements and risk weighting](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

## D

**DEX agent** — Machine running `DEXAgent.exe` that executes TestEvents distributed by the DEX server. See [Distributed execution (DEX)](/ToscaBase/execution/distributed-execution-dex/).

**DEX monitor** — Tosca Server web page listing the DEX agents and their test events. See [Tosca Server](/ToscaBase/administration/tosca-server/).

**Digest authentication** — Challenge-response HTTP authentication (401 with realm and nonce, then a hashed Authorization header); Tosca performs both round trips internally. See [API authentication](/ToscaBase/api-testing/api-authentication/).

**Distributed execution (DEX)** — Running ExecutionLists on remote DEX agents, in parallel, via Tosca Server. See [Distributed execution (DEX)](/ToscaBase/execution/distributed-execution-dex/).

**DokuSnapper** — Setting that generates a document per executed TestCase with the log and a screenshot per TestStep. See [DokuSnapper](/ToscaBase/execution/dokusnapper/).

**Dynamic expression** — A value in `{...}` inside a TestStepValue that Tosca evaluates at run time (buffer, date, random value, string operation, math) instead of a literal. See [Expressions](/ToscaBase/expressions/).

## E

**Embedded control** — A control such as a link or button placed inside a table cell in the Module so that it is addressed through the row. See [Table controls](/ToscaBase/modules/table-controls/).

**Endpoint and Resource (API)** — The endpoint is the common host part shared by an API's requests; the resource is the unique server location of one request. See [API Scan basics](/ToscaBase/api-testing/api-scan-basics/).

**Evaluation Tool (TBox)** — Standard Module that compares two dynamic expressions and returns true or false; used for verifications and as an If condition. See [Evaluation tool](/ToscaBase/standard-modules/evaluation-tool/).

**Excel 1:1 File Compare** — TBox Module that compares two workbooks sheet by sheet and writes mismatches to an output file. See [Excel engine](/ToscaBase/engines/excel-engine/).

**Execution entry** — A TestCase reference inside an ExecutionList; it carries its own Repetitions property and results. See [ExecutionLists](/ToscaBase/execution/execution-lists/).

**Execution Recorder** — TBox project setting that records executions as MP4; the `AvoidExecutionRecorder` Test Configuration Parameter opts a TestCase out. See [Recording executions](/ToscaBase/execution/recording-executions/).

**Execution State** — The passed, failed, not executed and not linked split of a requirement, derived from the ExecutionLists linked to it. See [Requirements and risk weighting](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

**ExecutionList** — A collection of TestCases grouped for a run. ExecutionLists hold the execution results and history and are the unit you schedule, distribute or report on. See [ExecutionLists](/ToscaBase/execution/execution-lists/).

**Exists** — Control property returning `True` or `False`; used with `Constraint` to search a table or with `WaitOn` to wait for a dialog. See [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/).

**ExplicitName** — Module-level Configuration Parameter; when `True`, renaming the attribute in a TestStep changes which control is steered, so one Module can address several identical controls. See [Control identification](/ToscaBase/modules/control-identification/).

**Exploratory testing** — Tosca's support for unscripted testing: a planned, time-boxed explorative session under Execution > Exploratory Testing, and the Explorative Scenario Manager that records an interaction into a screenshot-annotated scenario document. See [Exploratory testing](/ToscaBase/test-cases/exploratory-testing/).

## F

**File Scan** — Scan > More > File Scan; builds a Module whose attributes are the nodes of an XML file. See [XML engine](/ToscaBase/engines/xml-engine/).

## G

**Generic list item** — Item added through a ModuleAttribute's "..." menu to a combo box whose entries XScan did not scan. See [UIA engine and desktop controls](/ToscaBase/engines/uia-engine-and-desktop/).

## I

**Identification methods** — The four ways XScan identifies a control: by technical properties, by anchor, by image and by index, tried in that order. See [Control identification](/ToscaBase/modules/control-identification/).

**Identification, steering and transition parameters** — Three of the four parameter families on Modules and ModuleAttributes (the fourth is the Module-level Configuration Parameter): identification parameters find the control, steering parameters such as `ScrollingBehavior` change how it is operated, transition parameters describe what happens after. See [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/).

**Insert** — ActionMode for non-GUI interfaces that creates objects, for example XML nodes. See [ActionModes](/ToscaBase/test-cases/action-modes/).

**Instance** — One value of an attribute in TestCase-Design; an instance of a whole TestSheet is one generated TestCase (one column). See [Instances and combinatorics](/ToscaBase/test-case-design/instances-and-combinatorics/).

**Interval** — `{INTERVAL[base][limit]}` or `{INTERVAL[base][lower][upper]}`, a Verify-only check that a value lies in a numeric range. See [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).

## L

**License server** — Tricentis service (cloud-hosted or on-premise) that Tosca Commander authenticates against with support-portal credentials. Free trial and training licenses are requested through the support portal or tricentis.com. See [Licensing](/ToscaBase/getting-started/licensing/).

**LogViewer** — Standalone `LogViewer.exe` that shows Tosca's internal log stream filtered by level, for low-level diagnostics. See [Results and logs](/ToscaBase/execution/execution-results-and-logs/).

## M

**Maximum repetitions** — Property of While and Do objects that caps the number of iterations (default 30) to prevent infinite loops. See [Control flow](/ToscaBase/test-cases/control-flow/).

**Message Recorder** — API Scan feature that records HTTP traffic between an application and its backend and exports captured calls as API messages. See [Message Recorder](/ToscaBase/api-testing/api-message-recorder/).

**Module** — A reusable description of a screen, dialog, document or API endpoint that Tosca scanned or that you built by hand. A Module lists the controls (ModuleAttributes) that TestCases can act on. See [Modules overview](/ToscaBase/modules/modules-overview/).

**Module merge assistant** — Find duplicate Modules / Merge selected: merges a source Module into a target, re-links all usages and deletes the source. See [Duplicate and merge Modules](/ToscaBase/modules/duplicate-and-merge-modules/).

**ModuleAttribute** — A control or parameter declared in a Module that a TestStep sets a value and ActionMode for. See [Modules overview](/ToscaBase/modules/modules-overview/).

**MTOM** — SOAP binary-attachment option, enabled with Enable MTOM on the Attachments tab of API Scan. See [Message structure, SOAP and attachments](/ToscaBase/api-testing/api-message-structure-and-soap/).

**Multi-user workspace** — A workspace bound to a common repository; adds login, check-out and check-in, user management, branches, versioning and Test mandates. The Slim workspace option reduces its size for high-volume repositories. See [Multi-user workspaces](/ToscaBase/administration/multi-user-workspaces/).

## N

**Named group** — `(?<BufferName>subexpression)` inside `{REGEX[...]}`; stores the matched part in a buffer and requires ActionMode `Verify`. See [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).

## O

**Obstacle Course** — Tricentis' public web page of automation riddles used to practise control identification and steering. See [Troubleshooting](/ToscaBase/troubleshooting/).

**OffsetHorizontal / OffsetVertical** — Parameters (pixels or percent) that shift where `{CLICK}` and `{LONGCLICK}` hit a control; Click On Screen clicks at absolute X/Y coordinates in a window instead. See [Obstacles: input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/).

**Owning group / Viewing group** — Per-section or per-folder properties naming the user group that may change, or only view, the object. See [Users and groups](/ToscaBase/administration/users-and-groups/).

## P

**PDF Scan** — Scan mode of the PDF engine that turns drawn areas of a PDF (text, image, table) into a Module. See [PDF engine](/ToscaBase/engines/pdf-engine/).

**Pre-execution approval** — Tosca 16.0 automated TestCase approval workflow driven by Workstate; multi-user workspaces only. See [What's new in Tosca 16](/ToscaBase/getting-started/whats-new-in-tosca-16/).

## R

**Recorder** — Home-menu feature that generates Modules and a TestCase from recorded actions; its verification mode (Ctrl+Shift+V) turns clicks into Verify steps. See [Recorder](/ToscaBase/test-cases/recorder/).

**Recovery Scenario** — TestSteps that the recovery engine runs when a TestCase, TestStep or TestStepValue fails, then retries at the configured Retry level (TestCase, TestStep or TestStepValue). See [Recovery and Cleanup Scenarios](/ToscaBase/test-cases/recovery-and-cleanup-scenarios/).

**Relative Weight** — A requirement's Weight compared with the other weights in its requirement set. See [Requirements and risk weighting](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

**Repetition** — Folder property that runs the folder's TestSteps N times; the same name on an execution entry runs the TestCase N times. See [Repetitions](/ToscaBase/test-cases/repetitions/).

**Report definition** — A custom report: a data set definition (object selection by TQL), a designer definition (layout) and an output engine. Print View exports any view as a snapshot without a definition; Print Report runs a definition. See [Reports and report definitions](/ToscaBase/requirements-and-reporting/reports/).

**Repository type** — Field in the workspace-creation dialog (None, SQLite, Oracle, MS SQL Server, DB2) that decides whether the workspace is single- or multi-user. See [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/).

**Requirement set** — A group of requirements inside the Requirements section; TestCases link to individual requirements, never to the set. See [Requirements and risk weighting](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

**Rescan** — Reopening an existing Module in XScan against the live application to add properties or controls without breaking the TestCases that use it. See [Rescan Modules](/ToscaBase/modules/rescan-modules/).

**Resource (XML engine)** — Name given to an opened XML document; every XML TestStep refers to the file by it. See [XML engine](/ToscaBase/engines/xml-engine/).

**ResultCount** — Control property returning how many controls matched a ModuleAttribute, for example to count all links on a page. See [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/).

**Row selectors** — Table addressing in a TestStep: `$1` first row, `$n` n-th row, `$last` last row, `$lastContentRow` last data row, `$header` header row, `#n` n-th match. See [Table controls](/ToscaBase/modules/table-controls/).

**RowCount / ColumnCount** — Table-control properties returning the number of rows and columns, verifiable in a TestStep. See [Table controls](/ToscaBase/modules/table-controls/).

## S

**ScratchBook** — Ad-hoc dry run of a TestCase or TestStep; results are temporary and discarded when the ScratchBook is closed, and some features only work from an ExecutionList. See [ExecutionLists](/ToscaBase/execution/execution-lists/).

**ScrollingBehavior** — Steering parameter (`Top`, `Bottom`, `Center`, `None`) that positions a control in the viewport before it is steered. See [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/).

**Select** — ActionMode that picks a node in a hierarchy; assigned automatically on table and row paths. See [ActionModes](/ToscaBase/test-cases/action-modes/).

**SendKeys** — Keyboard emulation: `{SENDKEYS["..."]}` in a TestStepValue or the TBox Send Keys Module, using .NET SendKeys codes (`^` Ctrl, `+` Shift, `%` Alt). See [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/).

**Standard Modules (TBox Automation Modules)** — Ready-made Modules in the Standard subset for files, buffers, processes, windows, screenshots and more, added with Add TestStep without scanning. See [Standard modules](/ToscaBase/standard-modules/).

**Standard.tsu** — The standard workspace template that preloads Standard Modules, reusables, report templates and sample TestCases. See [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/).

**Static wait** — A TBox Wait step with a fixed duration; Tosca pauses for the full time regardless of application state, which is why WaitOn is preferred. See [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).

**Subset (.tsu) and .tdp** — `.tsu` is the subset export file produced by Export subset (and by standalone API Scan); `.tdp` is the repository backup dump created by an administrator. See [Backup and restore](/ToscaBase/administration/backup-and-restore/).

**Synchronization policy** — Object property in multi-user workspaces controlling whether an object can be excluded from repository synchronisation; Include and Exclude for synchronization are the context-menu actions, and excluded objects appear greyed out. See [Synchronisation, not waits](/ToscaBase/administration/multi-user-workspaces/).

## T

**Table control** — TBox representation of a table with Row, Column and cell nodes, selectors and properties (`RowCount`, `ColumnCount`, `RowNumber`, `ResultCount`). See [Table controls](/ToscaBase/modules/table-controls/).

**TargetDateFormat** — System Configuration Parameter on a date ModuleAttribute telling Tosca the control's date pattern. See [Date expressions](/ToscaBase/expressions/date-expressions/).

**TBox** — The engine framework behind XScan, XModules and the Standard Modules; "TBox" in a Module name means it is TBox-based. See [Modules overview](/ToscaBase/modules/modules-overview/).

**TBox buffer Modules** — TBox Set Buffer, Partial Buffer, Name to Buffer and Delete Buffer: the four Standard Modules for creating and extracting buffers. See [Buffer operations](/ToscaBase/standard-modules/buffer-operations/).

**TBox XEngines** — Engine-specific Standard Module group, for example TBox XEngines > HTML with Execute JavaScript and Verify JavaScript Result. See [Execute JavaScript](/ToscaBase/standard-modules/execute-javascript/).

**TCShell** — Command-line tool that opens a workspace and runs commands or `.tcs` scripts; the basis for scheduled and CI execution. See [Command-line tools](/ToscaBase/administration/command-line-tools/).

**TCWorkspaceUtil (TCWorkspaceCloneUtil)** — Command-line tool that clones a workspace with new IDs for every team member instead of copying it. See [Command-line tools](/ToscaBase/administration/command-line-tools/).

**TDS type and item** — A type is a table and an item is a row in a Test Data Services repository; the Expert Module is a single TDS Module whose Test Data Task folder covers all operations. See [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/).

**Technical TestCase** — Executable TestCase holding TestSteps, values and ActionModes, as opposed to a business TestCase. See [TestCase basics](/ToscaBase/test-cases/test-case-basics/).

**Template (TestCase template)** — TestCase converted with Convert to Template and linked through its schema path to a TestSheet; it is not executable itself. Check Template validates it against the sheet, Instantiate generates one TestCase per sheet instance, Reinstantiate regenerates them after changes. See [Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/).

**Test Configuration Parameter (TCP)** — Value defined in an object's Test Configuration tab, read with `{CP[name]}`, inherited down the folder tree and read-only during execution; `Browser` is the most common one. See [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/).

**Test Data Services (TDS)** — Tosca Server component for central test data management in repositories, types and items, shared between TestCases and applications. See [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/).

**Test mandate** — Execution-section object linked to an ExecutionList so that several users can run it concurrently without overwriting each other's results. See [Test mandates](/ToscaBase/administration/test-mandates/).

**TestCase** — An ordered set of TestSteps that drive the application through the controls declared in one or more Modules; the unit you execute, directly or from an ExecutionList. See [TestCase basics](/ToscaBase/test-cases/test-case-basics/).

**TestCase-Design (TCD)** — Commander section that keeps test data in TestSheets apart from TestCases and generates TestCases from templates. See [TestCase-Design overview](/ToscaBase/test-case-design/test-case-design-overview/).

**TestEvent** — Multi-user-workspace object that combines a Configuration and an ExecutionList and is executed on DEX agents. See [Distributed execution (DEX)](/ToscaBase/execution/distributed-execution-dex/).

**TestSheet** — Top-level TestCase-Design object: a grid of attributes and instances for one scenario, one column per generated TestCase. See [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/).

**TestStep** — One action inside a TestCase, created by dragging a Module in; it holds TestStepValues for the Module's attributes. See [TestCase basics](/ToscaBase/test-cases/test-case-basics/).

**TestStepLibrary** — Container (one per folder, Ctrl+L) holding reusable TestStepBlocks that TestCases reference instead of copying. See [Business Parameters and TestStepLibraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/).

**TestStepBlock** — Folder inside a TestCase that groups the TestSteps of one task; stored in a TestStepLibrary it becomes a reusable TestStepBlock. See [Business Parameters and TestStepLibraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/).

**TestStepValue** — The value plus ActionMode set on one ModuleAttribute within a TestStep. See [ActionModes](/ToscaBase/test-cases/action-modes/).

**Tosca Commander** — The desktop client where Modules, TestCases, ExecutionLists and requirements are created and managed. See [Architecture](/ToscaBase/getting-started/architecture/).

**Tosca Execution Client** — PowerShell/shell script (Tosca 15.2+) that triggers TestEvents from CI/CD and writes JUnit-style XML results. See [Tosca Execution Client](/ToscaBase/execution/tosca-execution-client/).

**Tosca Executor** — Component that runs TestCases and manages execution logs. See [Architecture](/ToscaBase/getting-started/architecture/).

**Tosca ID Mapper** — Tosca 16.0 XScan setting that defines application-level default identification properties for all controls of an application. See [What's new in Tosca 16](/ToscaBase/getting-started/whats-new-in-tosca-16/).

**Tosca Server** — Central server component hosting the REST API, file service, DEX server and monitor, AOS, license and user administration, and Test Data Services. See [Tosca Server](/ToscaBase/administration/tosca-server/).

**ToscaDateFormat** — System Test Configuration Parameter that sets which date format Tosca accepts as a valid date literal. See [Date expressions](/ToscaBase/expressions/date-expressions/).

**TQL (Tosca Query Language)** — Query grammar `scope->objecttype[constraint]` with operators such as `=?`, `==`, `>` and `<` for searching the workspace and feeding reports. See [TQL search and virtual folders](/ToscaBase/requirements-and-reporting/tql-and-virtual-folders/).

**Translate value** — Right-click command on a TestStepValue that shows the concrete value a dynamic expression will produce. See [Date expressions](/ToscaBase/expressions/date-expressions/).

## U

**Unattended execution** — Scheduled runs without a person present, through Windows Task Scheduler, Jenkins or the Tosca Execution Client. See [Scheduling executions](/ToscaBase/execution/scheduling-executions/).

## V

**Verification point** — A TestStep with ActionMode `Verify` that compares an expected value with the actual one; without one a TestCase can only produce a false positive. See [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

**Virtual folder** — Folder that owns no objects and shows the results of a stored TQL query; refreshed manually. See [TQL search and virtual folders](/ToscaBase/requirements-and-reporting/tql-and-virtual-folders/).

## W

**WaitOn** — ActionMode that waits until a control reaches the given value or state, up to the Synchronization timeout (Settings > TBox > Synchronization, default 20000 ms). See [ActionModes](/ToscaBase/test-cases/action-modes/).

**Weight** — A requirement's business-risk value (default 1, recommended scale 1-5), optionally derived as 2^Frequency Class * 2^Damage Class; it drives Contribution and Relative Weight. See [Requirements and risk weighting](/ToscaBase/requirements-and-reporting/requirements-and-risk/).

**Workspace** — The local project that Tosca Commander opens; it holds Modules, TestCases, ExecutionLists and requirements, either standalone or bound to a common repository. See [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/).

**Workstate** — TestCase status (`Planned`, `In Work`, `Completed`) that feeds requirement coverage and the review workflow. See [TestCase structure](/ToscaBase/best-practices/test-case-structure/).

## X

**XBuffer** — `{XB[name]}` inside a Verify value; verifies the fixed part of a text and buffers the variable part in one step. See [Buffers](/ToscaBase/data-and-parameters/buffers/).

**XModule / XModuleAttribute** — Module and attribute created by TBox-based XEngines through XScan, as opposed to classic Modules; an XDefinition describes how an XEngine structures a technology's controls for XScan. See [Modules overview](/ToscaBase/modules/modules-overview/).

**XScan** — Tosca's scanning tool that reads a running application and turns its controls into a Module. See [XScan](/ToscaBase/modules/xscan/).

**XScan engine (WinX, UIA, Vision AI)** — The technology XScan uses to read controls: WinX is the default for Windows windows, UIA (UI Automation) also handles browser-native popups such as JavaScript alerts, and Vision AI identifies controls from the screen image. See [UIA engine and desktop controls](/ToscaBase/engines/uia-engine-and-desktop/).
