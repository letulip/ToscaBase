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
---

At run time Tosca has to find each control on the screen from what the Module stores about it. XScan offers four identification methods, selectable from the **Identify by** menu in the Advanced view: **properties**, **anchor**, **image** and **index**. They form a hierarchy: try them in that order and stop at the first that makes the control unique. A fifth technique, the `ExplicitName` configuration parameter, is not an XScan method but a way to choose one of several identical controls from the TestCase. This doc explains the methods; worked problem cases are in [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/).

All four sources use the same example: the Google start page, where the *Google Search* button is not unique because a second, invisible button has exactly the same properties (`name`, `type`, `value`). The text box next to it is unique.

## Identify by properties

The default. Tosca matches the technical properties ticked in XScan (`id`, `name`, `tag`, `value`, `InnerText`, `alt`, ...). Always prefer it: it is the most stable and the fastest.

When XScan reports *selected item is not unique*, the first move is to tick more properties in the Advanced view. Often one extra property is enough (`alt` for the Google logo, `value` for a radio button in [Rescan Modules](/ToscaBase/modules/rescan-modules/)). Pick properties that describe identity, not state. If every sensible property is already ticked and the control is still not unique, as with the *Google Search* button, move on to anchor.

## Identify by anchor

An anchor is another control, in the neighbourhood of the target, that *is* unique. Tosca finds the anchor first and then the target relative to it. Use it only when properties fail; if no stable, uniquely identified control is available nearby, this method is not an option.

1. Select the target control and choose **Identify by > Anchor**. The **Identify by anchor** pane opens on the right.
2. Tosca can try to pick an anchor automatically. The pane offers a mode setting; the source mentions the values *Auto*, *Always*, *Shortest path* and *Coordinate* and uses *Auto*, which did not find an anchor for the button.
3. Add an anchor yourself: drag a unique control from the tree into the anchor slot (the source drags the *I'm Feeling Lucky* button; the text box would also do), or click **Select on screen** and click the anchor in the application. The pane reports *target control was successfully identified*.
4. Several anchors can be added if one is not enough.

The message on the target changes to *selected item is unique* and the orange bar disappears.

:::note
The anchor-mode names are read from speech; the source does not explain how the algorithms differ. Do not rely on the exact option names without checking the pane.
:::

## Identify by image

Tosca stores a bitmap of the control and finds it on screen by image matching. It is the fallback after anchor, and the source is explicit that it should be the last resort before index, because it depends on many run-time conditions.

1. Select the control and choose **Identify by > Image**. The **Identify by image** pane opens and already shows the control's image.
2. Click the **add image** button (a picture with a plus). The pointer becomes a cross; drag a rectangle around the area to use, or press **Return** to take the control's own area. **Escape** cancels; the cross icon cancels and the save icon stores the selection.
3. Tosca warns that image identification may result in a long duration without a visible XScan window. Answer **Yes** (tick *Remember my decision* to stop the prompt).
4. Fill in the **image properties**: a name for the image, and check the values Tosca recorded: **screen resolution**, **offset** (position of the image relative to the control), **method** (*full screen* in the source) and **accuracy** (95 % by default).

The control is then identified by properties **and** image; XScan shows both. Its weaknesses are the recorded values: a different screen resolution at execution time, a changed offset, a method other than full screen, or a match below the accuracy threshold all make the step fail. Keep execution machines identical to the scanning machine if you use it.

## Identify by index (ConstraintIndex)

When several controls have the same properties, the index is the position of the target among them. It is the last option in the hierarchy.

1. Choose **Identify by > Index**. The **Identify by index** pane shows a warning: use the index only if you cannot choose identification criteria that uniquely identify the control.
2. Tosca has already detected which index the selected control has; tick it. The message changes to *selected item is unique*.

Under the hood the Module gets the configuration parameter `ConstraintIndex` with that number; XScan reports that the control uses a constraint index for identification. The index is fragile because the order of identical controls can change with the page; a similar control may end up at the index you recorded. The same parameter can be created by hand, see [Module properties and parameters](/ToscaBase/modules/module-properties-and-parameters/).

## ExplicitName: choosing from the TestCase

Sometimes you do not want to fix the identity in the Module at all. On a product list every *Add to cart* button has the same properties; which one to click depends on the TestCase. With the default settings a TestStepValue name cannot be changed in the TestCase, and a click on the scanned button fails after the timeout with *more than one control found*.

1. In the Module, select the attribute and, in the **Properties** pane, right-click and choose **Create configuration parameter**. Name it `ExplicitName`.
2. Set it to `True`. (A value range is also allowed; the TestCase may then use any name from the range.)
3. In the TestStep, rename the attribute to `#3`. Tosca clicks the third *Add to cart* button.

The `#n` syntax is an index by another name, but it is set per TestStep instead of being baked into the Module, so one Module serves every product. The source calls it more stable than *Identify by index*; the reasoning is that the index is chosen where the context is known. `ExplicitName` with a cardinality of `0-n` is also how one scanned list item steers many entries, see [Obstacles: identifying controls](/ToscaBase/troubleshooting/obstacles-identification/).

## Summary

| Method | Use when | Risk |
|---|---|---|
| Properties | Always first | None if the properties are stable |
| Anchor | Properties do not make the control unique, a unique neighbour exists | Neighbour changes |
| Image | Nothing else works | Resolution, offset, accuracy |
| Index | Nothing else works and image is impractical | Order of identical controls changes |
| `ExplicitName` (`#n`) | The right control depends on the TestCase | Same as index, but chosen per step |

Whatever you pick, the whole execution depends on it, so choose deliberately and record the choice by naming the attribute sensibly.
