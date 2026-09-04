---
title: File and folder operations
description: TBox Standard Modules for creating, copying, comparing and deleting files and folders, and for checking that a folder exists.
level: 2
sidebar:
  order: 10
sources:
  - id: OoKV56JM8BE
    title: "Tosca Tutorial | Lesson 11 - Performing File Operations | TBox Automation Modules |"
    url: https://www.youtube.com/watch?v=OoKV56JM8BE
    at: "00:11"
  - id: U5iILzXT56A
    title: "Tosca Tutorial | Lesson 12 - Performing Folder Operations | TBox Automation Modules |"
    url: https://www.youtube.com/watch?v=U5iILzXT56A
    at: "00:10"
---

Tosca ships a set of ready-made **TBox Automation Modules** in the Standard subset. They are a library of general-purpose operations you can drop into any TestCase without scanning anything: file and folder handling, buffer handling, process control, timers and more. This page covers the file and folder Modules. Every one of them is added the same way: in the TestCase choose **Add TestStep**, search for `TBox` plus the operation name, and fill in the ModuleAttributes.

## File operations

### TBox Image Compare

Compares two image files.

| ModuleAttribute | Value |
|---|---|
| First image file path | Path of the first image (browse or paste) |
| Second image file path | Path of the second image |

The step is a verification: if the images differ, the verification fails and the TestCase fails. That is the expected outcome when you deliberately compare two different pictures.

### TBox Read/Create File

One Module both reads and creates text files. To create a file:

| ModuleAttribute | Value used in the example |
|---|---|
| Directory | Target folder |
| File name | `test1.txt` |
| Text | Content to write into the file |
| Encoding | `UTF-8` or `UTF-16` |
| Override | `True` to replace an existing file with the same name |
| Add byte order mark | `True` |

After the run the ScratchBook reports Passed and the file appears in the folder with the text you supplied.

### TBox Copy File

| ModuleAttribute | Value |
|---|---|
| Source | Path of the file to copy |
| Target directory | Destination folder |
| Target file name | Name for the copy, for example `test2.txt` |
| Override | `True` to overwrite an existing target |

Works for any file type (the video mentions `.txt` and `.xml`), not only text files.

### TBox File Compare

Compares the content of two files, a common check in TestCases.

| ModuleAttribute | Value |
|---|---|
| First file path | Path of file 1 |
| Second file path | Path of file 2 |

- Identical files: the log info states that the contents are identical and **no report is generated**.
- Different files: the verification fails, the TestCase fails, and Tosca generates an **HTML report**. The report highlights in red what is additional in one file or missing in the other.

### TBox Delete File

Takes a single path (for example `...\test1.txt`) and removes the file.

### Other file Modules

The Standard subset also has Modules to read a file, move it, rename it and append text to it. They are not demonstrated in the source video; use the same search-and-add approach.

## Folder operations

### TBox Create Folder

| ModuleAttribute | Value |
|---|---|
| Path | Full path of the folder to create |
| Override | `True` |

:::caution
Give the path of the **new subfolder** (for example `C:\Training\Folder1`), not the path of an existing folder. With Override set to `True` and the existing folder's path, Tosca overwrites that folder instead of creating a new one.
:::

### TBox Copy Folder

Searching for `TBox copy` shows two Modules, Copy File and Copy Folder; pick the folder one.

| ModuleAttribute | Value |
|---|---|
| Source path | Folder to copy |
| Target path | Destination, where it becomes a subfolder |
| Override | `True` |

The folder and everything inside it (subfolders and files) are copied.

### TBox Delete Folder

| ModuleAttribute | Value |
|---|---|
| Path | Folder to delete |
| Recursive | `True` deletes the folder together with its contents; otherwise nothing inside it is deleted |

### TBox Folder Existence

Verifies that a folder is present. Enter the path by hand: this ModuleAttribute has no browse button. The result shows an expected and an actual value (the folder should exist / does exist), and the verification passes or fails accordingly.

:::tip
A typical use is checking that a reports or test-data folder exists **before** the TestCases that need it run. Put the existence check first, then create, copy and delete. You can also combine all folder steps into one TestCase and wrap them in an `If` condition; see [Control flow](/ToscaBase/test-cases/control-flow/).
:::

## Related

- [Buffer operations](/ToscaBase/standard-modules/buffer-operations/)
- [Start and close programs](/ToscaBase/standard-modules/start-and-close-programs/)
- [Excel engine](/ToscaBase/engines/excel-engine/) and [PDF engine](/ToscaBase/engines/pdf-engine/) for content-level work with those file types
