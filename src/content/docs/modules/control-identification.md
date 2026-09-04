---
title: Control identification
description: The four ways XScan identifies a control (properties, anchor, image, index), the order to try them in, and the ExplicitName parameter for steering one of many identical controls from the TestCase.
level: 1
sidebar:
  order: 30
sources:
  - id: deY38EHGvNs
    title: "Tricentis Tosca Tutorial Part-4 : Tosca Module Creation, Tosca Xscan, Tosca Modules Overview"
    url: https://www.youtube.com/watch?v=deY38EHGvNs
    at: "08:36"
  - id: Hy7xq4YP-Eo
    title: "Tosca Tutorial | Lesson 6 - Identify Controls By Anchor | Scan Modules |"
    url: https://www.youtube.com/watch?v=Hy7xq4YP-Eo
    at: "00:02"
  - id: GGH8_xFhLdk
    title: "Tosca Tutorial | Lesson 7 - Identify Controls By Image | Image Based Test Automation |"
    url: https://www.youtube.com/watch?v=GGH8_xFhLdk
    at: "00:09"
  - id: zgqUoo_1tpM
    title: "Tosca Tutorial | Lesson 8 - Identify Controls By Index | Duplicate Controls |"
    url: https://www.youtube.com/watch?v=zgqUoo_1tpM
    at: "00:09"
  - id: rCZQyJFonhY
    title: "Tosca Tutorial | Lesson 43 - Use Explicit Name to identify duplicate controls | Module Properties"
    url: https://www.youtube.com/watch?v=rCZQyJFonhY
    at: "00:08"
  - id: EMsHHgKDvEU
    title: "TRICENTIS Tosca 16.0 - Lesson 07 | Identify controls by Properties & Anchor | Create Control Groups"
    url: https://www.youtube.com/watch?v=EMsHHgKDvEU
    at: "03:18"
  - id: NEThwpAbK5U
    title: "TRICENTIS Tosca 16.0 - Lesson 23 | Dynamic ID | Explicit Name |"
    url: https://www.youtube.com/watch?v=NEThwpAbK5U
    at: "04:07"
  - id: 4ELkBwejJIU
    title: "TRICENTIS Tosca 16.0 - Lesson 24 | Set Repetition on Folder Level | Explicit Name | ResultCount"
    url: https://www.youtube.com/watch?v=4ELkBwejJIU
    at: "17:33"
---

At run time Tosca must find each control on the screen from what the Module stores about it. XScan offers four identification methods in the **Identify by** menu of the Advanced view: **properties**, **anchor**, **image** and **index**, a hierarchy to try in that order, stopping at the first that makes the control unique. A fifth technique, the `ExplicitName` configuration parameter, is not an XScan method but chooses one of several identical controls from the TestCase. Problem cases: [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/). Playlist 1 uses the Google start page, the Tosca 16 lessons the Tricentis demo web shop.

## Identify by properties

The default and always the first choice: Tosca matches the technical properties ticked in XScan (`id`, `name`, `tag`, `value`, `InnerText`, `alt`, ...), the most stable and fastest method.

When XScan reports *selected item is not unique*, tick more properties in the Advanced view; often one extra is enough (`alt` for the Google logo, `value` for a radio button in [Rescan Modules](/ToscaBase/modules/rescan-modules/), `visible` for a *Books* category link that shares `tag` and `InnerText` with a product tab). Each ticked property costs run time, so tick only what is necessary and stable, preferring properties that describe identity, not state. If the control is still not unique with every sensible property ticked, as with the *Google Search* button (an invisible second button shares its `name`, `type` and `value`), move on to anchor.

### Wildcards for dynamic values

A property value that changes between pages or runs (a *dynamic ID*) is matched with `*` in place of the changing part: the demo web shop's title is `Demo Web Shop. Login` on one page and `Demo Web Shop. Register` on the next, so a `Title` technical ID of `Demo Web Shop.*` matches every page. Edit any technical ID this way in XScan (click the value) or later in the **Properties** pane. Since only the constant part is matched, a wildcard can also match several controls on purpose (see the order example under `ExplicitName`).

## Identify by anchor

An anchor is a nearby control that *is* unique; Tosca finds it first and then the target relative to it. Use it only when properties fail and a stable, unique neighbour exists. A container is a good anchor: the demo web shop's category links (*Books*, *Computers*, ...) share properties, but each is unique relative to the `ul` that holds them.

1. Raise **Filtered items** if the anchor you want (a `div` or `ul` container) is not in the tree.
2. Select the target, choose **Identify by > Anchor**, and in the **Identify by anchor** pane drag a unique control from the tree into the anchor slot (*I'm Feeling Lucky*, or the `ul`), or click **Select on screen** and click the anchor in the application. The pane reports *target control was successfully identified*, and the target's orange *not unique* bar disappears.
3. If the anchor itself is not unique, click **Make anchor unique** (Tosca ticks an extra property, `InnerHTML`) or tick one yourself.
4. Add more anchors if needed; one container anchors all its children and need not become a control itself.

The **relative algorithm** decides how Tosca walks from anchor to target: **Shortest path** follows the control tree, **Coordinate** uses screen positions (which break when the resolution changes), and **Auto**, the default, tries the shortest path first, then coordinates. Leave it on *Auto* or *Shortest path*.

:::note
Lesson 6 (playlist 1) also names an option *Always* that Lesson 7 (Tosca 16) does not show; check the option names in your version.
:::

## Identify by image

Tosca stores a bitmap of the control and finds it on screen by image matching: the fallback after anchor and the last resort before index, because it depends on many run-time conditions.

1. Choose **Identify by > Image**; the **Identify by image** pane shows the control's image.
2. Click **add image**, then drag a rectangle around the area to use or press **Return** for the control's own area; **Escape** cancels, the save icon stores the selection.
3. Answer **Yes** to the warning that image identification may run long without a visible XScan window (tick *Remember my decision* to stop the prompt).
4. Fill in the **image properties**: a name, plus the recorded **screen resolution**, **offset** (image position relative to the control), **method** (*full screen* in the source) and **accuracy** (95 % by default).

The control is then identified by properties **and** image; a different resolution, offset or method at execution time, or a match below the accuracy threshold, fails the step, so keep execution machines identical to the scanning machine.

## Identify by index (ConstraintIndex)

When several controls share the same properties, the index is the target's position among them, the last option in the hierarchy.

1. Choose **Identify by > Index**; the pane warns to use the index only if no identification criteria uniquely identify the control.
2. Tick the index Tosca has already detected; the message changes to *selected item is unique*.

The Module then gets the configuration parameter `ConstraintIndex` with that number (or create it by hand, see [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/)). The index is fragile: the order of identical controls can change with the page, and a similar control may end up at the recorded index.

## ExplicitName: choosing from the TestCase

Sometimes the choice belongs in the TestCase: every *Add to cart* button on a product list has the same properties, and which one to click depends on the test. A TestStepValue name cannot normally be changed in the TestCase, and clicking the scanned button fails with *more than one control found*.

1. In the Module, select the attribute and in the **Properties** pane right-click → **Create configuration parameter**; name it `ExplicitName` and set it to `True` (or a value range the TestCase may pick any name from).
2. In the TestStep, rename the attribute to `#3`. Tosca clicks the third *Add to cart* button.

`#n` is an index set per TestStep instead of baked into the Module, so one Module serves every product; the source calls it more stable than *Identify by index* because the index is chosen where the context is known. The name can also be an expression such as `{REPETITION}`, which steers control 1, 2, 3 ... on successive passes of a repeated TestStep folder (how Lesson 24 empties the cart; see [Repetitions](/ToscaBase/test-cases/repetitions/)), and with a cardinality of `0-n` one scanned list item can steer many entries ([Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/)).

**Example: the latest order.** Orders in the demo web shop's history are separate `div`s, newest on top. Scan one container (order number and total), wildcard its `OuterText` to `Order number: *`, set `ExplicitName = True` and name it `#1` in the TestStep to steer the newest order whatever its number; verify its `InnerText` against `Order number: {B[order number]}*`, the number buffered earlier on the confirmation page ([Buffers](/ToscaBase/data-and-parameters/buffers/)).

## Summary

| Method | Use when | Risk |
|---|---|---|
| Properties | Always first | None if stable |
| Anchor | Properties fail, unique neighbour exists | Neighbour changes |
| Image | Nothing else works | Resolution, offset, accuracy |
| Index | Image impractical too | Order of identical controls changes |
| `ExplicitName` (`#n`) | Choice depends on the TestCase | As index, chosen per step |

The whole execution depends on this choice: make it deliberately and name the attribute sensibly.
