---
title: "Obstacles: identifying controls"
description: Same IDs, twins, changing IDs, multi-select lists, autocomplete boxes, hidden and off-screen elements, and how to steer each of them.
level: 3
sidebar:
  order: 10
sources:
  - id: AX495tz4jIM
    title: "Tosca Tutorial | Lesson 107 - IDs are not everything | Elements with same IDs | Obstacle 1"
    url: https://www.youtube.com/watch?v=AX495tz4jIM
    at: "01:10"
  - id: jB6ay9xvRcE
    title: "Tosca Tutorial | Lesson 108 - Twins | Duplicate Elements with same ID and InnerText | Obstacle 2"
    url: https://www.youtube.com/watch?v=jB6ay9xvRcE
    at: "01:10"
  - id: sZ4uO5o26Kc
    title: "Tosca Tutorial | Lesson 110 - Two Times | Dynamically changing ID Property | Obstacle 4"
    url: https://www.youtube.com/watch?v=sZ4uO5o26Kc
    at: "01:13"
  - id: PKNn-hsjh_Q
    title: "Tosca Tutorial | Lesson 112 - Multiselect ListBox | Cardinality | Explicit Name | Obstacle 6"
    url: https://www.youtube.com/watch?v=PKNn-hsjh_Q
    at: "01:13"
  - id: daXKUviEo2g
    title: "Tosca Tutorial | Lesson 113 - Autocomplete TextBox | ResultCount | InnerText | Obstacle 7"
    url: https://www.youtube.com/watch?v=daXKUviEo2g
    at: "01:14"
  - id: jZvsxD41Iuw
    title: "Tosca Tutorial | Lesson 130 - Hidden Element | Click Element | Obstacle 24"
    url: https://www.youtube.com/watch?v=jZvsxD41Iuw
    at: "01:13"
  - id: RsbKnsNt8Rs
    title: "Tosca Tutorial | Lesson 131 - Scroll Into View | Steering Parameter | Scrolling | Obstacle 25"
    url: https://www.youtube.com/watch?v=RsbKnsNt8Rs
    at: "02:17"
---

The Tricentis *Obstacle Course* is a public web page of small automation riddles, each reproducing a problem you will meet in real applications. This doc collects the obstacles whose difficulty is in **identifying** the control: XScan reports *selected item is not unique*, the identifying property changes between runs, or the element is not visible at all. The lesson is the same every time: `id` is a good default, but when it fails, use other properties, the parent hierarchy, a different identification method or a steering parameter. The methods themselves are described in [Control identification](/ToscaBase/modules/control-identification/); here you see them applied. Table obstacles are in [Obstacles: tables](/ToscaBase/troubleshooting/obstacles-tables/), input and click obstacles in [Obstacles: input and clicks](/ToscaBase/troubleshooting/obstacles-input-and-clicks/).

:::tip
All obstacles are clicked with the value `X` (ActionMode `Input`) rather than `{CLICK}`. `{CLICK}` drives the real mouse, which is slower and not recommended by Tricentis; `X` does the same through the engine.
:::

## IDs are not everything (obstacle 1)

**Problem.** The page has two links, *Don't* and *Click me*. When you select *Click me* in XScan, Tosca reports that the item is not unique.

**Cause.** Both links share the same `id` and, being links, the same `tag`. Identification by these two properties alone cannot separate them.

**Solution.**

1. In XScan, compare the technical properties of the control with those of its twin.
2. Pick a property that differs. Here `InnerText` differs (*Click me* vs *Don't*); tick it and XScan reports the item as unique.
3. Save the Module, drag it into a TestCase, set `X` on the link and run.

Combine several technical properties when one is not enough; do not stick to `id` by habit.

## Twins (obstacle 2)

**Problem.** Two identical buttons labelled *I am the one*; the task is to click the second one (on the right). `id`, `InnerText` and `tag` are identical, so ticking more properties still leaves the item not unique.

**Cause.** The controls themselves carry no distinguishing property. The difference is only in *where* they sit in the page structure.

**Solution.** [Identify by index](/ToscaBase/modules/control-identification/#4-identify-by-index) works but breaks as soon as a similar link is added to the page. Identify through the parent container instead:

1. In XScan, raise the **filtered items** level so that parent elements become visible.
2. Find the container wrapping the target button; here the right-hand container has a unique `id`, the left-hand one's is empty.
3. Add the container to the Module, then the button inside it. In the TestCase Tosca sets the container's ActionMode to `Select`; put `X` on the nested link.

Parents and neighbours often carry the property the element lacks.

## Two times (obstacle 4)

**Problem.** A button must be clicked twice in a row. The label changes from *Click me twice* to *Click me once more* after the first click, and the TestStep that worked for the first click fails on the second.

**Cause.** The button's `id` is `rd_` followed by a number that changes after every click. A Module scanned before the click identifies the control by the old `id`.

**Solution.**

1. In the ModuleAttribute, replace the changing numeric part of the `id` with `*`, keeping the constant prefix (`rd_*`). The wildcard matches whatever digits appear.
2. Drag the Module into the TestCase twice (*Click once*, *Click twice*), each with the value `X`.

:::note
The speaker calls `*` a regular expression; in Tosca property values it is a wildcard. Full regular expressions are covered in [Intervals and verification expressions](/ToscaBase/expressions/intervals-and-verification-expressions/).
:::

## Multiselect list box (obstacle 6, "Testing methods")

**Problem.** A multi-select list box lists testing methods. Four of them (*Functional testing*, *GUI testing*, *End-to-End testing*, *Exploratory testing*) must be selected.

**Cause.** By default a ModuleAttribute can be used once per TestStep (cardinality `0-1`), and its name is fixed in the Module, so one scanned list item cannot address four different entries.

**Solution.** Scan only the list box and **one** list item; all items share the same properties, only their names differ. On the item attribute set **cardinality** to `0-n` and add the Configuration Parameter `ExplicitName = True`, so that the attribute can be used any number of times and the name given in the TestStep decides which item is steered (mechanism: [Control identification](/ToscaBase/modules/control-identification/#choosing-from-the-testcase-explicitname)).

In the TestCase, rename the item to `Functional testing`; a fresh empty item row appears, which you rename to the next method, and so on. ActionMode stays `Input`, which selects the entry. Use the full visible name (`End-to-End testing`, not `End-to-End`), otherwise the entry is not matched.

## Autocomplete text box (obstacle 7, "And counting")

**Problem.** A `span` shows a search text (for example `ddd`). Typing it into an autocomplete box opens a list of matching entries; the number of entries must be typed into a second text box.

**Cause.** The search text is dynamic; a normal `Input` into the autocomplete box does not open the suggestion list; the suggestions are a list of unknown length.

**Solution.** Module: the `span`, the autocomplete box, one list item with cardinality `0-n`, and the count text box. The page title may be dynamic; put a wildcard in the title property. TestSteps:

1. `span` → property `InnerText`, ActionMode `Buffer`, value `text`.
2. Autocomplete box → `{SENDKEYS "{B[text]}"}`. Sending keys one by one triggers the autocomplete; a plain `Input` does not.
3. List item → property `ResultCount`, ActionMode `Buffer`, value `count`. `ResultCount` returns how many controls matched the attribute.
4. Count text box → `{B[count]}` with ActionMode `Input`.

`ResultCount` is the same trick used to count links in [Common problems and fixes](/ToscaBase/troubleshooting/common-problems-and-fixes/).

## Hidden element (obstacle 24)

**Problem.** "Who turned off the lights?" The element to click is not visible on the page, so there is nothing to select on screen.

**Cause.** Visibility is not identification. Tosca steers whatever XScan can resolve from the DOM, whether or not the user can see it.

**Solution.**

1. Raise the **filtered items** level in XScan until the whole HTML tree is listed.
2. Orient yourself by visible neighbours (here the text *easy* sits in the same `div`) and find the target `span`. It has a unique `id`; no other property is needed.
3. Add it to the Module and click it with `X` in the TestCase; all the work is in the scan.

## Scroll into view (obstacle 25)

**Problem.** A text box inside an `iframe` is outside the visible area and something overlays the UI. Text entered while the box is out of view is discarded; it must be scrolled into view first, then filled and submitted.

**Cause.** The browser only accepts the input when the control is positioned in the viewport.

**Solution.** Use a **steering parameter** instead of a scroll step:

1. Scan the text field (XScan shows it nested `iframe` → HTML document → text field) and the *Submit* button.
2. Right-click the text field attribute, **Create Steering Parameter**, name it `ScrollingBehavior` and set it to `Top` (other values: `Bottom`, `Center`, `None`).
3. TestCase: *Enter text* (`Tosca`, ActionMode `Input`), then *Click submit* (`X`).

Tosca scrolls the field to the top of the viewport before typing; no static wait or scroll module is needed. Other steering parameters are listed in [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/); see also [Synchronisation, not waits](/ToscaBase/best-practices/synchronisation-not-waits/).
