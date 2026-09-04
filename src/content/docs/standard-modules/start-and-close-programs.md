---
title: Start and close programs
description: Use TBox Start Program to launch applications with arguments, close them with taskkill, clear the Chrome cache with cmd, and measure step duration with TBox Start/Stop Timer.
level: 2
sidebar:
  order: 30
sources:
  - id: OATubSuVee8
    title: "Tosca Tutorial | Lesson 14 - Use TBox Start Program | Open Application | Executable File |"
    url: https://www.youtube.com/watch?v=OATubSuVee8
    at: "00:03"
  - id: sbKJIaEoRd4
    title: "Tosca Tutorial | Lesson 15 - Close Programs | Taskkill | TBox Start Program Module |"
    url: https://www.youtube.com/watch?v=sbKJIaEoRd4
    at: "00:07"
  - id: OnymDRufrak
    title: "Tosca Tutorial | Lesson 27  - Automatically Clear Cache in Chrome Browser | TBox Start Program"
    url: https://www.youtube.com/watch?v=OnymDRufrak
    at: "02:10"
---

The process operations in the TBox Automation Modules let a TestCase start any executable, desktop application or browser, and, through the Windows `taskkill` command, close programs that are running. Two companion Modules, TBox Start Timer and TBox Stop Timer, measure how long the steps between them take, which turns a functional step into a simple performance check.

## TBox Start Program

Add the Module with **Add TestStep** and search for `TBox Start Program`.

| ModuleAttribute | Meaning |
|---|---|
| Path | Full path of the executable, for example `C:\Windows\notepad.exe` |
| Arguments | Command-line arguments passed to the program |
| Wait for exit | Whether the step waits for the program to finish |
| Run as | Username and password when the application must run under a specific account |

For Notepad only the path is needed. Running the step in the ScratchBook reports Passed and Notepad opens in the background.

### Starting a browser with arguments

Chrome's executable lives at `C:\Program Files\Google\Chrome\Application\chrome.exe` on 64-bit installations, or under `Program Files (x86)` otherwise. Put that in **Path** and add two arguments: the incognito switch and the URL to open. Executing the step launches Chrome in incognito mode already on the requested page.

:::note
The exact spelling of the incognito argument is not read out in the video; Chrome's documented switch is `--incognito`.
:::

## Closing programs with taskkill

TBox Start Program does not only start programs. Point it at Windows' own `taskkill` command and it ends processes: browsers, editors, even Tosca Commander itself. Typical use: a desktop test that must start from a clean desktop closes everything else first, so no other program interferes.

1. Add **TBox Start Program**.
2. **Path**: `taskkill` (no executable path needed).
3. **Arguments**: `/F /IM <image name>`.
   - `/IM` selects the process by its image name. `/PID` (process id) is the alternative.
   - `/F` forces termination of every process with that image name. Without it a program such as an editor may show a "do you want to save?" prompt instead of closing, so always include it.
4. Run the step. The log shows taskkill started with the arguments, and the program disappears.

To find the image name open **Task Manager > Processes**, select the app, choose **Go to details**, and read the **Name** column; that is also where the PID is shown. Examples from the video:

| Program | Image name |
|---|---|
| Google Chrome (all tabs and windows) | `chrome.exe` |
| Notepad++ | `notepad++.exe` |
| Tosca Commander | `ToscaCommander.exe` |

:::caution
Killing `ToscaCommander.exe` closes the Commander you are working in; save everything first. It is rarely needed interactively, but it is useful when a batch file opens Commander and runs tests through TCShell and you want to close Commander afterwards. See [Command-line tools](/ToscaBase/administration/command-line-tools/).
:::

## Measuring duration: TBox Start Timer and TBox Stop Timer

1. TestCase **Start timer**: add **TBox Start Timer** with an **ID**, for example `Timer1`.
2. The TestCase(s) you want to measure, for example one that starts Chrome.
3. TestCase **Stop timer**: add **TBox Stop Timer** with the same **ID**.

Run the folder. In the results the Start Timer log entry shows the timer starting, and the Stop Timer entry contains a **Measured value**: the time the steps between the two timers took (28 ms for opening the browser in the example).

### Turning the timer into a performance check

TBox Stop Timer also has a **Maximum duration**. Fill it in and set the ActionMode to `Verify`: if the measured time exceeds the maximum, the Stop Timer step fails with an expected/actual message, which marks the TestCase as not meeting its performance expectation.

:::note
The speaker calls the measured value "28 milliseconds" and the maximum "10 milliseconds", then reads the failure message as "less than 10 seconds, actually took 43 seconds". The unit is visible on screen only; check what Tosca shows for Measured value in your version before choosing a limit.
:::

## Clearing the Chrome cache

Leftover browser data can affect an execution, so clearing the cache is a common prerequisite step before running web tests. Manually it is done in Chrome under **Settings > More tools > Clear browsing data** (tick cached images and files, optionally browsing history, more under Advanced, then Clear data). To automate it, TBox Start Program runs the Windows command prompt with a delete command.

1. Add **TBox Start Program** to a TestCase (for example `Chrome cache`).
2. **Path**: `cmd`.
3. **Arguments**, in this order: `/C`, then `del`, then `/Q /S /F`, then the cache folder path in double quotes.

| Argument | Meaning |
|---|---|
| `/C` | Tells cmd to run the command that follows |
| `del` | The Windows delete command |
| `/F` | Force deletion of read-only files, without a confirmation prompt (prompting is `/P`, which automation must avoid) |
| `/S` | Delete the specified files from the given directory and display the names of the files being deleted |
| `/Q` | Quiet mode, runs in the background |
| `"<path>"` | Chrome's cache folder; the quotes stop the backslashes and spaces in the path from being misread |

With Chrome installed in its default location the cache is at `C:\Users\<user>\AppData\Local\Google\Chrome\User Data\Default\Cache`; a non-default installation stores it elsewhere. Search for *Windows cmd del* to see the full syntax of the delete command.

Run the step in the ScratchBook: a black console window flashes up, lists the files being deleted and closes; the step passes and the cache folder is empty afterwards. The same TestStep clears the cache of Internet Explorer or Firefox once the path argument points at their cache folder.

## Related

- [Window operations](/ToscaBase/standard-modules/window-operations/) to maximise, minimise or close a window you started
- [File and folder operations](/ToscaBase/standard-modules/file-and-folder-operations/)
