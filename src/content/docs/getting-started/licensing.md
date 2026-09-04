---
title: Licensing
description: How to get a Tosca trial or training license - support portal registration, the training license request page, the tricentis.com free trial, and connecting Tosca Commander to the cloud-hosted license server.
level: 1
sidebar:
  order: 30
sources:
  - id: gw1m7U_8xGg
    title: "Tricentis Tosca Tutorial Part 2:  Download Tosca, Install Tosca, Activate Tosca Trial license"
    url: https://www.youtube.com/watch?v=gw1m7U_8xGg
    at: "00:16"
  - id: EoTAKgbeB8Y
    title: "Tosca Tutorial | Lesson 2 - How to get a free cloud training license? | Free License |"
    url: https://www.youtube.com/watch?v=EoTAKgbeB8Y
    at: "00:11"
  - id: 8OJHR-hCSNM
    title: "Tosca Tutorial - Setup Tricentis Tosca With Trial Cloud License (Latest Video)"
    url: https://www.youtube.com/watch?v=8OJHR-hCSNM
    at: "00:01"
---

Tosca is a licensed product: there is no public download and Commander refuses to open without a valid license. For learning you have two routes, both free and both ending at the same place, the **cloud-hosted license server** that Commander connects to with the credentials of your Tricentis support account. The older route requests a *training license* from the support portal; the newer route requests a *free trial* on tricentis.com. Whichever you use, the support account with a business email is the prerequisite.

## Step 1: register on the Tricentis support portal

1. Open the support portal (search for "Tosca download", or go to `support.tricentis.com` / the Support Hub) and click **Register**.
2. Fill in the login data: email and password. Only a **business or professional email** is accepted; Gmail, Yahoo and similar addresses are rejected and there is no alternative.
3. Enter personal data (name, phone, time zone) and company data. Tricentis verifies the company data later, when the license request is processed. Fields other than email, password, name and time zone are optional.
4. Accept the privacy policy and submit. A verification mail arrives (it may take a while); click **Verify me now**. Until you verify, the portal shows an error on login.

Registration is a one-time activity per user.

## Step 2a: request a training license (support portal route)

1. Log in to the support portal and open the training license request page. The QASCRIPT lesson gives it as the Support Hub URL with the query `id=training_license_request`; the LambdaGeeks tutorial reads it as `support.tricentis.com/community/training_license_request`. Both were read from subtitles, so check the video description if the address does not resolve.
2. Choose the **preferred license type**:
   - **Cloud**: Commander connects to Tricentis' cloud license server with your portal credentials. Recommended, because it works from any machine.
   - **On-premise**: a license installed on a standalone machine. While a cloud request is pending you cannot also request an on-premise one.
3. Submit. A success popup and a confirmation mail follow. The request shows the state **Deploying**; refresh until it changes to **Deployed**, then the license is ready.

Once the license is deployed, the portal's **Downloads** tab lists the products you may download; see [Installation](/ToscaBase/getting-started/installation/).

:::note
The training license is provided for learning only and must not be used for anything else. The LambdaGeeks tutorial calls it a 60-day trial; the QASCRIPT lessons say only "a limited amount of time". Expect a time limit and check the portal for the exact term.
:::

## Step 2b: request a free trial on tricentis.com (newer route)

Tricentis later simplified the process: the download and the trial license come from the product website rather than the support portal.

1. On `tricentis.com` go to **Demos and trials**, find Tosca and click **Free trial**.
2. Check the system requirements shown on the page: about 1.4 GB of disk space, five to ten minutes of download on a stable connection, Windows 7 or later.
3. Fill in the form: email address, the required details, optionally your role and your goals for the trial (for example, learning Tosca). Submit.
4. The confirmation page explains what happens next, links videos for installing, activating the license and creating a first TestCase, and offers the installer download (about 1.4 GB, Tosca 15 LTS at the time of recording).

The trial can be extended by 30 days; beyond that you must contact Tricentis. The trial covers Tosca only, not NeoLoad or qTest.

:::caution
Use the **same email** for the trial request and for the support portal account. Commander authenticates against the cloud license server with the portal credentials, and the trial is tied to the email it was requested with.
:::

## Step 3: connect Tosca Commander to the license server

The first time Commander starts without a license it opens the license page directly. Otherwise:

1. **Project > License**. If a license is already active the page says so.
2. Click **Connect** (under **Activate**; the transcripts also mention a **Manage** view next to it). The options are a self-hosted license server, licenses from the local machine, and **Connect to cloud hosted license server**.
3. Choose **Connect to cloud hosted license server** and click **OK**.
4. Enter the username (your support portal email) and password and confirm. Validation takes a few seconds; a message confirms that you are connected to the license server.

This is a one-time step: on later starts Commander validates and reconnects automatically. The same connection can be made from the separate **Tosca License Configuration** utility installed with Tosca, which offers the same **Connect** option.

## Related

- [Installation](/ToscaBase/getting-started/installation/) for downloading and running the installer, including on an AWS Windows server.
- [What's new in Tosca 16](/ToscaBase/getting-started/whats-new-in-tosca-16/) mentions the extended cloud license support for administrators.
