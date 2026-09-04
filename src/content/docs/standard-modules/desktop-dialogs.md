---
title: Desktop dialogs
description: Automate the Windows Save As dialog with the TBox Save As Module, including the confirmation popup that may follow the Save click.
level: 2
sidebar:
  order: 70
sources:
  - id: cW_JhVahFpE
    title: "Tosca Tutorial | Lesson 24 - Desktop Automation | Save As Dialog Box | TBox Automation Module |"
    url: https://www.youtube.com/watch?v=cW_JhVahFpE
    at: "01:10"
---

The Windows **Save As** dialog is a desktop dialog box, not part of the web page, so the HTML XEngine cannot scan or steer it. Tosca's Standard subset ships a dedicated Module, **TBox Save As**, that fills the file name, picks the button and even handles a confirmation popup that appears after saving. It works for any application that shows the standard dialog, for example a Microsoft Office document you edited and want to save under a new name.

## TBox Save As

Add it via **Add TestStep** and search for `TBox Save As`.

| ModuleAttribute | Meaning | Value in the example |
|---|---|---|
| Caption | Title of the dialog window | `Save As` |
| File name label | Label of the file-name edit box. When it is the standard `File name`, Tosca steers it automatically and the attribute can stay empty; fill it in only for a custom label | `File name` |
| File path | Full path including the file name to enter in the file-name box | `C:\Training\test.docx` |
| Button | Which dialog button to click: `Save` or `Cancel` | `Save` |
| Confirmation popup caption | Title of a popup that may appear after the button click | `Microsoft Word` |
| Confirmation popup button | Button to click in that popup | `OK` |

## Example: save a Word document

1. Open the document, make a change, and open the Save As dialog.
2. Add **TBox Save As** with caption `Save As`, file path `C:\Training\test.docx`, button `Save`.
3. Run. Tosca enters the path and clicks Save, but Word then shows a popup saying the document will be upgraded to a new file format and asks for confirmation. The file is **not** saved until that popup is answered.
4. Fill in **Confirmation popup caption** = `Microsoft Word` and **Confirmation popup button** = `OK`.
5. Reset the application (cancel the popup so the dialog is back) and run the step again. The file is saved under the given name in the given folder.

:::tip
You will not always know in advance whether a popup follows the Save click. Run the step once without the two confirmation attributes, see what appears, then read its title and button name into them. The same two attributes handle the popup that asks whether to overwrite an existing file.
:::

:::note
The transcript says the file name as "test dot doc" and later "test dot talk"; the exact extension is not audible. Any Word extension works; the point is that the path and file name go into a single attribute.
:::

## Related

- [Window operations](/ToscaBase/standard-modules/window-operations/) for generic window commands such as Wait on open and Close
- [UIA engine and desktop](/ToscaBase/engines/uia-engine-and-desktop/) for scanning desktop applications
- [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/) to verify or clean up the saved file
