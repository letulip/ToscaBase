---
title: Installation
description: Download the Tosca installer, walk through the setup wizard, install the browser extension for XScan, and optionally run Tosca on an AWS EC2 Windows Server instead of a local machine.
level: 1
sidebar:
  order: 40
sources:
  - id: gw1m7U_8xGg
    title: "Tricentis Tosca Tutorial Part 2:  Download Tosca, Install Tosca, Activate Tosca Trial license"
    url: https://www.youtube.com/watch?v=gw1m7U_8xGg
    at: "04:28"
  - id: 8OJHR-hCSNM
    title: "Tosca Tutorial - Setup Tricentis Tosca With Trial Cloud License (Latest Video)"
    url: https://www.youtube.com/watch?v=8OJHR-hCSNM
    at: "03:08"
  - id: qzYWlZJ8oac
    title: "Tosca Tutorial | Lesson 3 - Setup Tosca 16 | AWS EC2 | Virtual Windows Server | Cloud |"
    url: https://www.youtube.com/watch?v=qzYWlZJ8oac
    at: "00:04"
---

Tosca runs on Windows only. Installing it is a download of about 1.5 GB (the size varies with the installer version; the Tosca 15 LTS trial installer in [Licensing](/ToscaBase/getting-started/licensing/) is about 1.4 GB), a wizard where the defaults are fine, a license connection, and one browser extension so that XScan can see web pages. If your own machine is not a Windows box or is too small, the same steps work on a virtual Windows Server in AWS, which is also the only way to drive Tosca from a Mac. A support account and a license request are prerequisites; see [Licensing](/ToscaBase/getting-started/licensing/).

## Download

- **Support portal route**: log in, open the license request page (where your training license shows as Deployed) and follow the download link, or open the **Downloads** tab. The list contains many Tricentis products; pick the one whose product is Tosca and whose title is **Tricentis Tosca 16.0 LTS** (version 16.0). Do not confuse it with other 16.0-related products.
- **Free trial route**: the confirmation page of the trial request offers the installer directly (Tosca 15 LTS at the time of recording).

Download time depends on the connection; the file is a zip. Extract it: the folder contains the installer application and a `sha256` checksum file. Double-click the application to start the wizard.

## Setup wizard

1. **Welcome**: tick *I agree to license terms* and click **Continue**.
2. **Prerequisites**: missing prerequisite components are installed for you. Click **Next**.
3. **Setup type**: keep **Tosca Commander**. The other choices are to set the machine up as an *execution agent* (see [Distributed execution](/ToscaBase/execution/distributed-execution-dex/)) or a *custom* installation.
4. **Paths**: the default installation folders can be changed; keep them.
5. **Tosca Diagnostics**: usage statistics. Untick it if you do not want to send them.
6. **Update service**: enable or skip.
7. **Tosca Data Integrity**: not needed for UI automation; leave it out.
8. **Vision AI engine**: leave the default, which installs it.
9. **Review**: the list of features to install; individual features can still be removed here. Click **Install**.
10. Installation takes a couple of minutes. Each feature shows a green tick when done; logs are available if something fails. Click **Finish**.

If an older Tosca (for example 14.3) is already installed, the installer offers an **upgrade** to the downloaded version instead of a fresh install.

After installation the Windows Start menu has a **Tricentis** folder with all installed components; the one you need is **Tosca Commander**. On first launch it asks for a license: connect it as described in [Licensing](/ToscaBase/getting-started/licensing/), then it opens the start page where you create a workspace ([Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/)).

## Browser extension for XScan

Scanning a web application requires a Tosca extension in that browser. Without it, starting **Scan > Application** on a Chrome window shows the message *browser extension not installed or outdated*.

1. Answer **Yes** to the prompt. Tosca opens the extension page in the browser.
2. Click **Add to Chrome** and confirm.
3. Close the page and scan again; the XScan window now opens and controls can be added.

See [XScan](/ToscaBase/modules/xscan/) for the scan itself.

## Running Tosca on an AWS EC2 Windows Server

The QASCRIPT lesson sets up Tosca 16.0 on a free-tier AWS account. The steps are: create a Windows EC2 instance, connect to it over RDP, download and install Tosca on it, connect the license, install the browser extension.

### Launch the instance

1. In the AWS console open **EC2 > Instances > Launch instance** and give it a name (for example `Tosca web server`).
2. **AMI**: choose a Windows image. The default free-tier base image, **Windows Server 2022**, is sufficient.
3. **Instance type**: the free-tier `t2.micro` has 1 GB of memory, which is too little for anything but a demo. For real use choose **`t2.large` (8 GB)** or larger; 8 GB is the recommended minimum for Tosca.
4. **Key pair**: create one (for example `Tosca server`) in **`.pem`** format. It downloads automatically; you need it to decrypt the Windows password.
5. **Network settings**: create a security group that allows **RDP** (restrict the source to *My IP* if you prefer), plus **HTTP** and **HTTPS**. Without these the server is not reachable.
6. **Storage**: the default 30 GB is enough for Tosca Commander.
7. Leave the advanced details, keep one instance (a second instance is only needed if you want Tosca Server and Commander on separate machines), and click **Launch instance**. Wait until the state is **Running**.

### Connect over RDP

1. Select the instance, click **Connect** and choose the **RDP client** tab.
2. **Download remote desktop file**. The username is `Administrator`.
3. Click **Get password**, upload the `.pem` file and click **Decrypt password**. Copy the password.
4. Open the RDP file, paste the password and accept the connection dialogs. On the first login, answer **Yes** to the network discovery prompt.

### Install Tosca on the server

Open Edge (finish its first-run setup), log in to the Tricentis support portal with your account, open the license request page and download Tosca 16.0 LTS as above. Extract, run the installer with the defaults, launch **Tosca Commander** from the Start menu and connect to the cloud-hosted license server with your portal credentials. Create a single-user workspace with the standard template and Commander opens.

Chrome is not preinstalled on a fresh Windows Server; install it, then add the Tosca extension on the first scan as described above.

:::tip
A larger instance costs money, but it lets you run Tosca from a Mac or any other OS through RDP, keep it running for long executions, and avoid loading your own machine. Tosca itself cannot be installed on macOS.
:::
