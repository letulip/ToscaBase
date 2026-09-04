---
title: Design classes
description: TestCase-Design classes hold attributes and instances shared by several TestSheets; class references keep them centrally managed, and resolving a reference detaches a copy.
level: 2
sidebar:
  order: 50
sources:
  - id: R3tCelZvf8w
    title: "Tosca Tutorial | Lesson 58 - Create and use TestCase Design Classes for common Attributes |"
    url: https://www.youtube.com/watch?v=R3tCelZvf8w
    at: "00:06"
  - id: VeG0TLkQM8g
    title: "Tricentis Tosca Tutorial Part-10 : Tosca Test Case Design, Tosca Class"
    url: https://www.youtube.com/watch?v=VeG0TLkQM8g
    at: "10:25"
  - id: R0zEbmFq0HE
    title: "Tosca Tutorial | Live Session | Test Case Designing | End-To-End | Real time Examples | Live Project"
    url: https://www.youtube.com/watch?v=R0zEbmFq0HE
    at: "49:36"
---

A **class** in the TestCase-Design section is a container for attributes and instances that several TestSheets need. Instead of creating the same `Enter vehicle data` attributes with the same instances in an `Automobile` sheet and again in a `Truck` sheet, you create them once in a class and put a **class reference** into each sheet. Changes are made in the class and appear in every reference. It is the TestCase-Design counterpart of a TestStepLibrary ([Business parameters and libraries](/ToscaBase/data-and-parameters/business-parameters-and-libraries/)) or of a function you call from many places. TestSheets and attributes themselves are described in [TestSheets and attributes](/ToscaBase/test-case-design/test-sheets-and-attributes/).

## When a class pays off

In the *Vehicle Insurance* sample, *Automobile*, *Truck*, *Motorcycle* and *Camper* all start with an *Enter vehicle data* section. The fields are mostly the same; *Truck* adds `Payload` and `Total weight`. Modelling each vehicle type as its own TestSheet duplicates the attributes and their instances, and every later change has to be made four times. A class removes the duplication and centralises the maintenance.

## Create a class

Three ways, all ending with a class object (its icon carries a `C`) in a TestCase-Design folder:

1. **Manually.** Right-click the folder **> Create Class**, rename it, and add attributes and instances exactly as in a TestSheet.
2. **From a Module.** Drag a Module (for example `Enter vehicle data`) into the folder. Tosca creates a class with the Module's name, one attribute per ModuleAttribute and instances taken from the control values. Review it: not every generated instance is correct, and attributes can be added or removed.
3. **From an existing attribute.** Drag an attribute from a TestSheet into the folder and choose **Create class from attribute** (the menu also offers **Create structure from attribute**). The class gets the attribute's sub-attributes and instances.

A class is otherwise no different from a sheet: it has its own attributes and instances. In the Part 10 tutorial the class also has **class instances** (`Set 1`, `Set 2`), each assigning values to the class attributes from the details pane, so that a sheet can pick a whole data set at once.

## Reference the class from a TestSheet

Drag the class onto a TestSheet. The sheet now shows a **class reference** with the class's attributes and instances. Do the same for every sheet that needs the data. Rules:

- The reference is read-only: attributes and instances cannot be changed inside it. Edit the class, and every reference reflects the change (deleting an instance in the class removes it from all references).
- Right-click the reference **> Jump to referenced class** opens the class.
- When the class has class instances, select the wanted set (`Set 1` or `Set 2`) in the reference; the sheet then uses that set's values.
- In a template, class-reference attributes are mapped to TestStepValues the same way as sheet attributes ([Templates and instantiation](/ToscaBase/test-case-design/templates-and-instantiation/)).

## Resolve a reference

When one sheet needs the common attributes plus its own additions (`Payload` and `Total weight` for trucks), right-click the class reference **> Resolve class reference**. The reference becomes ordinary attributes in the sheet, which you can extend. The link to the class is gone for that sheet: later changes in the class no longer reach it, and the attributes are maintained locally again.

:::caution
Resolve only when the sheet really has to diverge. If the additions are optional fields, consider keeping the reference and adding the extra attributes next to it, so that the shared part stays centrally managed.
:::

## Where classes fit

Classes belong to the same design pass as the sheet: identify attributes that repeat across sheets, move them into a class, reference it, then continue with instances and templates. The [worked example](/ToscaBase/test-case-design/worked-example-end-to-end/) shows the whole sequence on one application.
