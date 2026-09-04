---
title: Mobile automation
description: Set up the Mobile engine with Tricentis Mobile Agent, map the application and connection configurations to a TestCase, automate a first Android TestCase with Open Mobile App on a real device and an emulator, and scan a native app on SauceLabs real devices through a Cloud APM connection.
level: 3
sidebar:
  order: 50
sources:
  - id: wpkwzSAGpgs
    title: "Tosca Mobile Automation - Lesson 05 | Automate First Mobile Test Case for Android | Test Automation"
    url: https://www.youtube.com/watch?v=wpkwzSAGpgs
    at: "02:16"
  - id: ohfGxtWWRno
    title: "Tosca Mobile Automation - Lesson 06 | Scan Native App using SauceLabs | SauceLabs Integration"
    url: https://www.youtube.com/watch?v=ohfGxtWWRno
    at: "05:32"
---

The Mobile engine steers native Android and iOS apps the way the HTML engine steers a web page: scan the app into a Module, assemble TestSteps with the usual ActionModes, run. What differs is the plumbing. Tosca reaches the device through **Tricentis Mobile Agent** (TMA), a separate service with its own console, and the device is either attached to the machine running the agent (USB, Wi-Fi, an Android Studio emulator) or rented from a cloud farm such as SauceLabs, BrowserStack or [Tricentis Device Cloud](/ToscaBase/engines/device-cloud/). This page covers the configurations a mobile scan creates, the first Android TestCase, and scanning a native app on SauceLabs devices.

:::note
Lessons 1 to 4 of the mobile series (installing Tricentis Mobile Agent, Android Studio and virtual devices, connecting an Android phone over USB or Wi-Fi, scanning a native app with **Scan > Mobile**) are not in the ingested playlist. This page starts where they end: a device is listed in the agent console and the app (a *Tip calculator* APK) is scanned into a Module.
:::

## What a mobile scan leaves behind

**Scan > Mobile** asks for a connection, a device and an application before it opens the scanner, and it saves those choices under the project node in **Configurations > Mobile**:

- **Applications**: one entry per scanned app, with `ApplicationID` (the full path of the APK), the platform and the application type.
- **Connections**: `Local` and `Remote`. A remote connection carries the address of the TMA server and the type `TMA`.

These entries are [Test Configuration Parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/), and every mobile TestCase needs them mapped before its first step runs.

## First Android TestCase

The scenario: open the tip calculator, enter a base price, verify the total that the app computes with its default tip.

1. Create a folder `Mobile automation` and a TestCase `Tip calculator basic test`.
2. Open the TestCase's **Test configurations** tab. Drag the project tab to the right so that the TestCase and the project sit side by side, expand **Configurations > Mobile** and drag the application entry (`Tip calculator`) and the connection you use (`Remote` in the source: the phone hangs on another machine that runs the agent) onto the TestCase's configurations.
3. Add a third parameter: right-click, **Create test configuration parameter**, and pick `DeviceName` from the names Tosca proposes. Its value is the device's **UDID**. Right-click the TMA tray icon, choose **Open console > Configure devices** and copy the UDID of the device; every device has its own.
4. First TestStep: the standard Module **TBox Engine > Mobile > Open Mobile App** (right-click the TestCase, **Search and add TestStep**, type its name). In `Application` enter `{CP[ApplicationID]}`: typing `{CP[` lists the parameters mapped to the TestCase, and `ApplicationID` resolves to the APK path. Every mobile TestCase starts with this step.
5. Drag the scanned app Module below it and name the step `Validate the total price`: the base text box gets `2000` with ActionMode `Input`, the total gets `2300` with ActionMode `Verify`.
6. Save and **Run in ScratchBook**. Tosca installs the APK on the device first (it does so on every run), opens the app, enters the value and verifies; a mirror window shows the phone screen while it runs.

:::caution
The first run fails: expected `2300`, actual `2300.0`. The app shows the total with a decimal place, so the verified value must be written the way the app renders it.
:::

### The same TestCase on an emulator

Start an Android Virtual Device from Android Studio's Device Manager. It appears in the TMA console next to the real phone, with its own UDID (`emulator-54xx`). Change nothing but the `DeviceName` parameter and run again: the APK is installed on the emulator and the same steps pass.

## Scanning a native app on SauceLabs

To scan or run on a SauceLabs device you need an account, the app uploaded there, and a connection of a different type in Tosca.

Prepare SauceLabs first:

- **App Management**: upload the APK (Android) and the IPA (iOS) of the app; the source uses the *Swag Labs* sample app that SauceLabs provides.
- **Live > Mobile App** lists the real devices you can use (Google Pixel, Samsung Galaxy, iPhone XR, iPhone 12). Each device page shows its unique id, for example `iPhone_XR_free`.
- **Account > User settings** shows the **OnDemand URL**, the address Tosca connects to.

Then in Tosca, right-click **Modules** and choose **Scan > Mobile**:

1. **Add connection**: a name (`SauceLabs connect`), type **Cloud APM** instead of `TMA`, and the OnDemand URL as APM server address (see the caution below).
2. **Add device**: a name, the **Device ID** copied from the device page, the operating system (iOS or Android) and *real device*. The source adds an iPhone XR and a Samsung Galaxy.
3. **Add app**: application type **Native**, a name (`SauceLabs_Android`), and as **Full path** `storage:filename=<file name>`, where the file name comes from **App Management > the app > Settings > App version** in SauceLabs; then the app type (APK or iOS).
4. Pick the connection, the device and the app, click **Connect** and wait for *connection established, device is connected*, then **Scan**. A live view of the cloud device opens next to the scanner. Select the controls (username and password with **Make unique** when the scanner reports the control is not unique; the login button via **Select on screen**), save the Module (`Mobile app Android`) and close the scan, which also closes the live view.
5. Repeat with the iPhone XR and an app entry for the IPA (`storage:filename=<ipa file name>`, type iOS) to get `Mobile app iOS`.

:::caution
In the Tosca 2023 version used in Lesson 6 the **Add connection** dialog rejects the full OnDemand URL as invalid, and with the URL cut down to the part starting at `ondemand` **Connect** fails with *failed serving request POST*. Workaround: add the connection with the shortened URL, then open **Configurations > Mobile > Connections > SauceLabs connect** in the project, paste the full OnDemand URL into the APM server field and save. The scan dialog then shows the full address and Connect works. The full URL embeds your SauceLabs user name and key, so treat that configuration as a secret.
:::

BrowserStack and Tricentis Device Cloud follow the same path: a Cloud APM connection, devices, apps, then scan.

## Related

- [Test configuration parameters](/ToscaBase/data-and-parameters/test-configuration-parameters/): the `Mobile` group of parameters and the `{CP[...]}` syntax.
- [Tricentis Device Cloud](/ToscaBase/engines/device-cloud/): what the Tricentis device farm adds beyond running TestCases.
- [XScan](/ToscaBase/modules/xscan/): scanning in general.
