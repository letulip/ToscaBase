---
title: PDF engine
description: Compare two PDFs with the 1:1 Compare standard module, scan text, images and tables with PDF Scan, and count pages of a PDF without page numbers.
level: 3
sidebar:
  order: 20
sources:
  - id: XOSmgNewTp0
    title: "Tosca Tutorial | Lesson 22 - Compare PDF files | TBox Automation Module | 1:1 Compare"
    url: https://www.youtube.com/watch?v=XOSmgNewTp0
    at: "00:02"
  - id: O9FYIm7L9YU
    title: "Tosca Tutorial | Lesson 23 - Scan and Verify different elements on a PDF document | PDF Engine"
    url: https://www.youtube.com/watch?v=O9FYIm7L9YU
    at: "00:04"
  - id: 1t4hgmo42lM
    title: "Tosca Tutorial | Lesson 146 - Common Problems & Fixes | Get Total PageCount of PDF | PDF Scan"
    url: https://www.youtube.com/watch?v=1t4hgmo42lM
    at: "00:12"
---

Tosca offers two ways to test a PDF. The standard module `1:1 Compare` from the TBox subset compares a whole document against a reference with a tolerance, without any Module of your own. The **PDF Scan** of the PDF engine builds a Module from selected areas of a document (text, image, table) so you can verify individual values in a TestCase. A typical end-to-end scenario drives the web application, waits for the generated PDF and then verifies it with one of these two approaches.

## Quick comparison: `1:1 Compare`

The TBox standard module `1:1 Compare` sits next to the other comparison Modules (file compare, image compare, Excel compare). Add it to a TestCase and fill its attributes:

| Attribute | Meaning |
|---|---|
| Reference PDF | Full path of the baseline document, including the `.pdf` extension |
| Reference password | Password of the baseline, if it is protected; Tosca enters it automatically |
| Target PDF | Full path of the document to compare against the reference |
| Target password | Password of the target, if any |
| Accuracy | Required match in percent. `100` means both documents must be identical; a lower value tolerates small differences |
| Excluded pages | Pages left out of the comparison. Several entries are separated by semicolons; a page range is also accepted |

How the result is evaluated:

- With accuracy `80`, two slightly different one-page documents still **pass**. The log info says the success condition was met: every page of the target and the baseline matched at least 80 percent, and no pages were excluded.
- With accuracy `100` the same TestCase **fails**. The log info lists the areas where at least one difference was detected (top left, top right, mid left, mid right, bottom right and so on).

:::note
The comparison reports only *where* on the page something differs, not *what*. It is meant as a quick overall check. To verify specific values you need PDF Scan (below).
:::

:::note
The speaker's example for excluded pages excludes page 1, a range of pages 3 to 4 and page 5, separated by semicolons. The exact character used inside the range was not spoken out loud in the video; check the attribute's tooltip in your Tosca version.
:::

## Scanning a PDF with PDF Scan

1. In the **Modules** section, right-click a folder and choose **Scan > PDF** (not **Application**, which is for desktop and web applications).
2. Select the PDF document. The **PDF Scan** window opens with a preview of every page.

The toolbar offers:

- **Zoom fit**, zoom in and zoom out.
- **Select document language**.
- **Show content preview**: a pane (hidden by default) showing the value of the element you just scanned.
- **Scan new document** to switch to another PDF, **Save** to store the scanned controls, and **Close**.
- Three scan tools, one per element type found in PDFs: **Text**, **Image** and **Table**.

### Text and image controls

1. Click **Text** (or **Image**); the cursor turns into a plus sign.
2. Draw a rectangle around the area. Tosca recognises the content of the area and shows it in the content preview. Draw the rectangle larger than the value if longer values are possible.
3. On the right the control appears with its type and a generic name. Double-click to rename it (for example `Make`, `FuelType`, `Logo`).
4. Use **Jump to** to highlight the scanned area on the page, **Redraw** to change the area, or **Remove** to drop the control.

### Table controls

A table control only works well when the PDF contains a real table with aligned rows and columns; otherwise Tosca cannot tell rows from columns. Options for a scanned table:

- **Use header row** / **Use header column**, and which row is the header (the first row by default).
- Adjust the cell borders if the automatic grid is off; the coordinates are shown while hovering.
- **Consider invisible cells**.

### Save the Module

Click **Save** and close PDF Scan. The new Module is named after the file path; rename it (for example `InsuranceQuotePDF`). It contains the scanned controls plus two ModuleAttributes: `Target PDF` (path of the document to test) and `PDF password`.

## Verifying PDF elements in a TestCase

1. Create a TestCase and add the scanned Module as a TestStep.
2. Set `Target PDF` to the path of the document, with the `.pdf` extension. Leave `PDF password` empty unless needed.
3. **Text control**: enter the expected value. ActionMode is set to `Verify` automatically, because verification is what you normally do with a PDF.
4. **Image control**: verify the property `Exists` with the value `True`.
5. **Table control**: the Module exposes rows and cells. Choose the column by number, then the cell by number, and enter the expected value. Wildcards help when a cell contains more than the value you care about: `*Bonus 1*` passes even if other text precedes or follows.

After execution the log info shows each verification: text expected and actual values match, the image exists, and the table cell matches the pattern. Use `*` wherever part of a text is constant and the rest changes.

## Counting the pages of a PDF

Some PDFs have no page number in the header or footer, so there is no element to read the total from. The workaround uses the fact that a PDF Module walks through all pages when a control is allowed on any page.

1. **Scan > PDF**, open the document and create one **Text** control anywhere on a page; where does not matter. Save and rename the Module (for example `SamplePDF`).
2. Below the text-area control the Module holds a document-level element. If it is not shown, select the Module and press **F12**.
3. Open the properties of that element. Its `Page` property is `1`; change it to `*` (any page). Close the properties.
4. Create a TestCase, add the Module and set `Target PDF`.
5. On the document-level element choose ActionMode `Buffer` with a buffer name such as `PageCount`.
6. On the text control (`PDF Area 1`) verify the value `*`, which matches any text on any page.
7. Set the Workstate to completed and run in the ScratchBook. Execution takes longer for long documents because Tosca visits every page.

The log shows the buffer being set to 1, 2, 3 ... and finally to the last page number (57 in the video); the verification succeeds because `*` is always true. Check the final value under **Tools > Buffer Viewer** or verify it in a later TestStep.

:::note
In the auto-generated subtitles the speaker calls the document-level element a "div element". The exact name in the Module tree could not be confirmed from the audio; look for the element that carries the `Page` property.
:::

If the PDF does have page numbers in a header or footer, scan that area as a text control, mark it as a repetitive area in PDF Scan and buffer its value while iterating; the last buffered value is the page count.

## Related

- [Buffers](/ToscaBase/data-and-parameters/buffers/) for the values you buffer from a PDF.
- [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/) for the file-compare Modules mentioned alongside `1:1 Compare`.
- [Excel engine](/ToscaBase/engines/excel-engine/) and [XML engine](/ToscaBase/engines/xml-engine/) for the other document engines.
