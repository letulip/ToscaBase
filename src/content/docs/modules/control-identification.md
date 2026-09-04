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

At run time Tosca has to find each control on the screen from what the Module stores about it. XScan offers four identification methods, selectable from the **Identify by** menu in the Advanced view: **properties**, **anchor**, **image** and **index**. They form a hierarchy: try them in that order and stop at the first that makes the control unique. A fifth technique, the `ExplicitName` configuration parameter, is not an XScan method but a way to choose one of several identical controls from the TestCase. Worked problem cases are in [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/). The playlist 1 sources use the Google start page, where the *Google Search* button is not unique because a second, invisible button has the same `name`, `type` and `value`; the Tosca 16 lessons use the Tricentis demo web shop.

## Identify by properties

The default. Tosca matches the technical properties ticked in XScan (`id`, `name`, `tag`, `value`, `InnerText`, `alt`, ...). Always prefer it: it is the most stable and the fastest.

When XScan reports *selected item is not unique*, the first move is to tick more properties in the Advanced view. Often one extra property is enough (`alt` for the Google logo, `value` for a radio button in [Rescan Modules](/ToscaBase/modules/rescan-modules/), `visible` for a *Books* category link that shares `tag` and `InnerText` with a product tab). Any number of properties can be ticked, but each one costs time at run time, so tick only what is necessary and stable, and prefer properties that describe identity, not state. If every sensible property is ticked and the control is still not unique, as with the *Google Search* button, move on to anchor.

### Wildcards for dynamic values

A property value that changes between pages or runs (a *dynamic ID* in the source) is matched with `*` in place of the changing part. The demo web shop's title is `Demo Web Shop. Login` on one page and `Demo Web Shop. Register` on the next; setting the Module's `Title` technical ID to `Demo Web Shop.*` lets one Module match every page. Any technical ID can be edited this way, in XScan (click the value) or later in the **Properties** pane: an order container whose `OuterText` starts with `Order number: 1234` gets `Order number: *`. Tosca then matches only the constant part, so a wildcard can make several controls match on purpose; see the order example under `ExplicitName`.

## Identify by anchor

An anchor is another control near the target that *is* unique. Tosca finds the anchor first and then the target relative to it. Use it only when properties fail; if no stable, unique control is available nearby, this method is not an option. A container is a good anchor: the demo web shop's category links (*Books*, *Computers*, ...) all match by properties, but each is unique relative to the `ul` element that holds them.

1. Raise **Filtered items** if the anchor you want (a `div` or `ul` container) is not in the tree.
2. Select the target control and choose **Identify by > Anchor**. The **Identify by anchor** pane opens on the right.
3. Drag a unique control from the tree into the anchor slot (the *I'm Feeling Lucky* button, or the `ul` container), or click **Select on screen** and click the anchor in the application. The pane reports *target control was successfully identified*.
4. The anchor itself must be unique. If the pane says it is not, click **Make anchor unique** (Tosca ticks an extra property, `InnerHTML` in the source) or tick one yourself.
5. Add more anchors if one is not enough. Repeat for each target; one container anchors all of its children and need not become a control itself.

The **relative algorithm** setting decides how Tosca walks from anchor to target: **Shortest path** follows the control tree from the anchor; **Coordinate** uses screen positions, which break when the resolution changes; **Auto**, the default in both sources, tries the shortest path first and falls back to coordinates. Leave it on *Auto* or *Shortest path*.

The message on the target changes to *selected item is unique* and the orange bar disappears.

:::note
Lesson 6 (playlist 1) also names an option *Always* that Lesson 7 (Tosca 16) does not show; check the option names in your version.
:::

## Identify by image

Tosca stores a bitmap of the control and finds it on screen by image matching. It is the fallback after anchor, and the source is explicit that it should be the last resort before index, because it depends on many run-time conditions.

1. Select the control and choose **Identify by > Image**. The **Identify by image** pane opens with the control's image.
2. Click **add image** (a picture with a plus). The pointer becomes a cross; drag a rectangle around the area to use, or press **Return** to take the control's own area. **Escape** cancels; the save icon stores the selection.
3. Tosca warns that image identification may run for a long time without a visible XScan window; answer **Yes** (tick *Remember my decision* to stop the prompt).
4. Fill in the **image properties**: a name, and check the recorded **screen resolution**, **offset** (image position relative to the control), **method** (*full screen* in the source) and **accuracy** (95 % by default).

The control is then identified by properties **and** image. The recorded values are its weakness: a different resolution at execution time, a changed offset, another method, or a match below the accuracy threshold all make the step fail. Keep execution machines identical to the scanning machine if you use it.

## Identify by index (ConstraintIndex)

When several controls have the same properties, the index is the position of the target among them. It is the last option in the hierarchy.

1. Choose **Identify by > Index**. The **Identify by index** pane warns to use the index only if no identification criteria uniquely identify the control.
2. Tosca has already detected which index the selected control has; tick it. The message changes to *selected item is unique*.

Under the hood the Module gets the configuration parameter `ConstraintIndex` with that number; it can also be created by hand, see [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/). The index is fragile: the order of identical controls can change with the page, and a similar control may end up at the recorded index.

## ExplicitName: choosing from the TestCase

Sometimes you do not want to fix the identity in the Module at all. On a product list every *Add to cart* button has the same properties; which one to click depends on the TestCase. By default a TestStepValue name cannot be changed in the TestCase, and a click on the scanned button fails with *more than one control found*.

1. In the Module, select the attribute and, in the **Properties** pane, right-click and choose **Create configuration parameter**. Name it `ExplicitName`.
2. Set it to `True`. (A value range is also allowed; the TestCase may then use any name from the range.)
3. In the TestStep, rename the attribute to `#3`. Tosca clicks the third *Add to cart* button.

The `#n` syntax is an index by another name, but it is set per TestStep instead of being baked into the Module, so one Module serves every product. The source calls it more stable than *Identify by index*, because the index is chosen where the context is known. `ExplicitName` with a cardinality of `0-n` is also how one scanned list item steers many entries, see [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/).

**Example: the latest order.** The demo web shop's order history lists every order in its own `div`, newest on top. Scan one container with its order number and total, make it match by `Order number: *` (see wildcards above), give it `ExplicitName = True`, and name it `#1` in the TestStep: it steers the first container whatever the number. Its `InnerText` is verified against `Order number: {B[order number]}*`, the number having been buffered on the confirmation page ([Buffers](/ToscaBase/data-and-parameters/buffers/)).

The name can also be an expression: in a TestStep folder with a Repetition, `{REPETITION}` steers control 1, 2, 3 ... on successive passes (Lesson 24 uses it as a table row selector to tick the *Remove* checkbox of every row); see [Repetitions](/ToscaBase/test-cases/repetitions/).

## Summary

| Method | Use when | Risk |
|---|---|---|
| Properties | Always first | None if the properties are stable |
| Anchor | Properties do not make the control unique, a unique neighbour exists | Neighbour changes |
| Image | Nothing else works | Resolution, offset, accuracy |
| Index | Nothing else works and image is impractical | Order of identical controls changes |
| `ExplicitName` (`#n`) | The right control depends on the TestCase | Same as index, but chosen per step |

Whatever you pick, the whole execution depends on it, so choose deliberately and name the attribute sensibly.
