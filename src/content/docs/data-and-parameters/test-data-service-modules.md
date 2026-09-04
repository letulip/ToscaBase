---
title: Test Data Service Modules
description: The Standard Modules that drive Test Data Services from a TestCase (Create and Provide New Item, Find and Provide Item, Update Item, Move Item to Type, Delete Item, Expert Module), the create-find-update flow, reading items with {TDS[type.attribute]}, and generating bulk data with random values and Repetitions.
level: 2
sidebar:
  order: 50
sources:
  - id: Eli2iucdQ_s
    title: "Tosca Tutorial | Lesson 154 - Test Data Management with Tosca | Test Data Services | TDS Modules |"
    url: https://www.youtube.com/watch?v=Eli2iucdQ_s
    at: "22:27"
---

Test Data Services are meant to be driven from TestCases, so that data exists before the TestCases that need it run. Searching **Add TestStep** for `test data` lists the TDS Standard Modules from the Standard subset. This page walks through them in the order a real flow uses them. The concept, the web interface and the two required Test Configuration Parameters (`TestDataEndpoint`, `TestDataRepository`) are in [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/); without those parameters every Module below fails.

## The Modules

| Module | Purpose |
|---|---|
| **Create and Provide New Item** | Creates an item in a type (creating the type if it does not exist) and *provides* it to the following steps |
| **Find and Provide Item** | Selects an existing item by filter or query and provides it |
| **Update Item** | Changes attributes of the provided item |
| **Update Type** | Changes a type |
| **Move Item to Type** | Moves the provided item from one type to another |
| **Delete Item** | Deletes the provided item (only that one) |
| **Import Items**, **Export Items** | File import and export, as in the web interface |
| **Expert Module** | One Module with a *Test Data Task* folder that covers all of the above plus tasks only available here |

Common ModuleAttributes: **existing or new TDS type** (after the first successful run, a drop-down lists known types), an optional **alias name**, a **data structure** where you add one attribute-value pair per column, and for the find operations a **position** (first, random; default 1), a **TDQL query** and a **sort**.

:::caution
The Modules form a **flow**: each step passes the provided item in memory to the next. `Update Item`, `Move Item to Type` and `Delete Item` fail with *no available test data was found* when nothing has been provided before them, or when the find filter matches nothing. Run the steps together, not in isolation.
:::

## Step 1: create an item

Add **Create and Provide New Item**, set the type (`Vehicle`), then add attributes and values in the data structure: `Make` = `BMW`, `Engine`, `DOM` = `01/01/2014`, `Seats` = `4`, `FuelType`, `Price`, `Mileage` = `1000`, matching the fields of the vehicle form. Add a custom attribute **`Status`** = `new` as well: it is the field that tracks whether an item has already been consumed.

Run in ScratchBook. The log shows nothing special; verify by refreshing the type on the server page, where a new row appears. Changing the type to `Automo` and the make to `Audi` and running again adds a row to that type instead, so one Module both creates types and fills existing ones.

## Step 2: find an item

**Find and Provide Item** with type `Vehicle`. In the data structure enter `Status` = `new`; as soon as a value is entered the ActionMode switches to `Constraint` automatically, because the attribute is a filter, not an input. Only items whose status is `new` are provided.

To see what was found, follow it with `TBox Set Buffer`, buffer `status`, value `{TDS[vehicle.status]}`; the log then shows the buffer set to `new`. The `{TDS[type.attribute]}` expression is the way TestSteps consume the item: `{TDS[vehicle.engine]}`, `{TDS[vehicle.dom]}` and so on go straight into the `Input` values of the form. See [Buffers](/ToscaBase/data-and-parameters/buffers/).

Alternatively filter with a **TDQL query**, which reads like SQL: `vehicle[make=="BMW"]` selects the BMW item. The TestCase passes without visible output, which shows the query matched.

:::note
The transcript states the query as "vehicle, square bracket, make equals equals BMW"; whether the value needs quotes is not audible. Try both forms.
:::

## Step 3: update the state

**Update Item** with alias `Vehicle` and `Status` = `used` in the data structure changes the provided item. After running create, find and update together, the server page shows the item with status `used`. This is the tracking loop: find `new` data, consume it in the application, mark it `used` so the next run does not pick it again.

## Step 4: move an item to the next process

When the data must continue into another application (the price calculation in the back end, say), keep one type per process and move the item: **Move Item to Type** takes the source type (`Vehicle`) and a target type (`PriceOption`, existing or new). It needs a provided item, so run **Find and Provide Item** first; if that step still filters on `new` after the item was set to `used`, nothing is found and the move fails. Running the whole flow from create onwards passes, and the server page then shows a new type `PriceOption` holding the moved item.

## Step 5: delete used data

**Delete Item** with alias `Vehicle` deletes the currently provided item, not the whole type. Change the preceding find filter to `Status` = `used` and the pair find-then-delete cleans up consumed data.

## The Expert Module

**Expert Module** contains a *Test Data Task* folder with create, find, update, delete and additionally **assign read-only**, **delete type**, **delete all** (not recommended: it deletes everything), **lock item / unlock item**, **lock type / unlock type**. It takes the same inputs (type, position, data structure or query, sort). Use it when you prefer one Module for all tasks or need the extra ones.

## Using TDS data in a real TestCase

The video copies a TestCase-Design template into a plain TestCase (`Verify mobile automation insurance - TDS`) and, inside the pre-processing folder, adds a `Prepare test data` folder containing **Create and Provide New Item** and **Find and Provide Item** (`Status` = `new`). The TestStepValues that previously came from the TestSheet are replaced by `{TDS[vehicle.engine]}`, `{TDS[vehicle.mileage]}` and so on. With the two TCPs copied to the folder, running pre-processing, the navigation and the *enter vehicle data* block fills the form from TDS. Where the data ultimately comes from (a database, business analysts, the manual test team) does not matter; TDS manages it.

## Bulk data with random values and Repetitions

1. In **Create and Provide New Item**, replace fixed values with random expressions ([Random values](/ToscaBase/expressions/random-values/)): a three-digit random number for the engine, one digit for seats, four digits for the price, three for the mileage. Values that must match a drop-down (`Make`) stay fixed.
2. Open the **Properties** of the `Prepare test data` folder and set **Repetition** to `10` ([Repetitions](/ToscaBase/test-cases/repetitions/)).

One run creates ten items with different data in the type. How you generate data is your choice; TDS is where it is managed.

## Related

- [Test Data Services](/ToscaBase/data-and-parameters/test-data-services/): concept, web interface, prerequisites
- [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/)
- [Buffer operations](/ToscaBase/standard-modules/buffer-operations/)
