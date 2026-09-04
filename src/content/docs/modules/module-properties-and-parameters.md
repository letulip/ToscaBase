---
title: Module properties and parameters
description: The properties Tosca stores on Modules and ModuleAttributes (cardinality, business type, synchronization policy, IDs) and the four parameter types, configuration, identification, steering and transition, with the ones you will actually use.
level: 1
sidebar:
  order: 60
sources:
  - id: IYGr51H7CIg
    title: "Tosca Tutorial | Lesson 157 - Module Properties | Configuration, Identification & Steering Params |"
    url: https://www.youtube.com/watch?v=IYGr51H7CIg
    at: "00:10"
---

Every Module and every ModuleAttribute carries a set of **properties** that XScan fills in when it scans, plus optional **parameters** that you or Tosca add to change how a control is found and steered. Both live in the **Properties** pane on the right of Commander (expand it with the arrow if collapsed). Some are read-only, some editable. Knowing them lets you fix a control that scans fine but does not steer, without rescanning.

## Properties

Properties with a blue icon are created by Tosca. The important ones:

| Property | On | Meaning |
|---|---|---|
| **Automation framework** | Module | `TBox`, the default engine shipped with Tosca, or the generic automation framework, used when you deploy your own DLLs and generic controls |
| **Business type** | Module and attribute | The technology-specific type. On a Module it is the root element, `HTML document` or `XML document`; on an attribute it is the control type, for example `TextBox` |
| **Cardinality** | Attribute | How often the attribute may be used as a TestStepValue in one TestStep. Default `0-1` (once). Set `0-n` to use it any number of times, for example a list item or a checkbox you need repeatedly |
| **Node path** | Both | Unique path of the object in the workspace, from the root through `Modules` down to the attribute |
| **Synchronization policy** | Module | Whether the object is included in repository synchronization: `Default is on`, `Default is off`, `Cannot be excluded`, `Cannot be excluded for whole tree`. Explained in [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/) |
| **Technical ID** | Module | A technology-specific property, mostly set by Tosca; not every Module has one |
| **Unique ID** | Both | The object's unique number in the workspace; use it to search for the object |
| **Owning group name**, **Viewing group name** | Module | The user groups that own the object and may see it; see [Users and groups](/ToscaBase/administration/users-and-groups/) |
| **Data type**, **Action mode**, **Default value** | Attribute | Type of the value, the default ActionMode, and a default value for the TestStepValue |
| **Interface type** | Attribute | `GUI`, `Non-GUI` or `Implicit` |

:::note
The Synchronization policy values are read twice in the source; the second reading, at 07:09, is the one used above. The first mentions *customizable, default is on*, which is also the wording used in the best-practices doc. Check the drop-down in your version.
:::

## Parameters

Right-click a Module or attribute in the Properties pane to see what can be created: a ModuleAttribute, a **configuration parameter**, a **transition parameter**, a **steering parameter**, and three kinds of identification parameter: **business ID**, **technical ID** and **reflected ID**. That gives the four parameter families:

| Family | Decides |
|---|---|
| Identification | Which properties are used to search for the control (business ID, technical ID, reflected ID) |
| Configuration | Which components are used to steer the control |
| Steering | How the control behaves while it is steered |
| Transition | Switching technology or context within one TestStep |

A freshly scanned HTML Module already has some: the configuration parameter `Engine = HTML`, the steering parameters `ControlFramework = None`, `EnableSlotContentHandling = False` and `IgnoreAreaControls = False`, and a technical ID parameter `Title`. A scanned text box carries technical IDs `id` and `tag` with their values and, in the source, the steering parameter `FireEvent = Change`. You add your own when the generic behaviour is not enough.

### Identification parameters

- **Technical ID**: the common one. Technology-specific properties such as `value` for HTML input controls, `InnerText` for HTML elements, `encoding` for an XML declaration. XScan creates these from the properties you tick; you can add more with **Create technical ID parameter** if you know the name and value. Several IDs are combined with AND.
- **Business ID**: properties that are the same across technologies for a control type, for example every button has `label`, every text box has `text`.
- **Reflected ID**: properties that Tosca does not expose by default, read from the technology through reflection. The technology must support reflected object access, and reflected IDs are slower than the default ones. The source's only example is the `language` attribute in Internet Explorer.

### Configuration parameters

Create with **Create configuration parameter**, then type the exact name. The ones relevant to web controls:

| Parameter | Value | Use |
|---|---|---|
| `ConstraintIndex` | integer | Pick the *n*-th of several controls with identical properties. What *Identify by index* sets; see [Control identification](/ToscaBase/modules/control-identification/) |
| `ExplicitName` | `True`, `False` or a value range | Allows the attribute's name to be edited in the TestStep; with a range, only names from the range. Steering by `#n` and multi-use list items depend on it |
| `CanExecuteInParallel` | `True` / `False` | For distributed execution on DEX agents when two TestCases use the same Module at once; see [Distributed execution](/ToscaBase/execution/distributed-execution-dex/) |
| `ExternalEngine` | | Mobile engine Modules, mostly image-based automation |
| `AlgorithmicAssociation`, `TechnicalAssociation` | | Search-algorithm parameters for finding a target object within a selected context; engine-specific, rarely needed |
| `SpecialExecutionTask` | | Performs a specific task while steering the control |

Example from the source: on the `Username` attribute create `ExplicitName = True` and `ConstraintIndex = 1`. In a new TestCase the `Password` and `Login` names cannot be edited, but `Username` can be renamed to `User` or `Email`.

### Steering parameters

Create with **Create steering parameter**. Many are specific to Vision AI, SAP or mobile Modules; the general ones:

| Parameter | Value | Effect |
|---|---|---|
| `BringToFront` | `True` (default) / `False` | Bring the window to the foreground before steering; `False` lets it run in the background |
| `IgnoreInvisibleHtmlElements` | `True` / `False` | Skip invisible HTML elements that slow execution down |
| `ScrollingBehavior` | `Top`, `Bottom`, `Center`, `None` | Where a control is positioned on screen when Tosca scrolls to it |
| `SendKeysDelay` | milliseconds, e.g. `100` | Delay between the individual characters of a keyboard command |
| `SynchronizationTimeout` | milliseconds | How long Tosca waits for the control before it throws an error. Can also be set in settings or per TestCase via a configuration parameter; `WaitOn` has its own steering parameter |
| `UserSimulation` | `True` / `False` (default) | Trigger clicks and keyboard events through ActionMode `Input` the way a user would: select or deselect checkboxes and radio buttons, click links, type into text boxes. Use it when the regular engine action does not take effect |
| `WaitBefore`, `WaitAfter` | milliseconds | Wait before or after the control is steered, for a control that is still loading |

The source adds `WaitBefore = 10` to the `Login` button and describes it as 10 milliseconds. A wait this short is a demonstration, not a recommendation; prefer synchronization, see [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).

### Transition parameters

Rarely used. A transition parameter changes technology or context inside one TestStep so that different engines can share it; the value is the name of the transition, for example `StringPropertyToXml` or `XPathToXmlElement`. The source's example switches from the browser context to the mobile engine while reusing one XPath. Related engines: [XML engine](/ToscaBase/engines/xml-engine/).

## Rules of thumb

- Fix identification in XScan first ([Control identification](/ToscaBase/modules/control-identification/)); reach for parameters when the control is found but does not behave.
- Type parameter names exactly as Tosca spells them; they are case sensitive.
