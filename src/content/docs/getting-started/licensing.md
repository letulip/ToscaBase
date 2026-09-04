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
  - id: Cdmul1knpsI
    title: "TRICENTIS Tosca 16.0 - Lesson 01 | Download Tosca | Install Tosca 16.0 | Activate license|Automation"
    url: https://www.youtube.com/watch?v=Cdmul1knpsI
    at: "01:03"
---

Tosca is a licensed product: there is no public download and Commander refuses to open without a valid license. For learning you have two routes, both free and both ending at the same place, the **cloud-hosted license server** that Commander connects to with the credentials of your Tricentis support account. The older route requests a *training license* from the support portal; the newer route requests a *free trial* on tricentis.com. Whichever you use, the support account with a business email is the prerequisite.

## Step 1: register on the Tricentis support portal

1. Open the support portal (search for "Tosca download" and take the first result, or go to `https://support.tricentis.com/community`; the QASCRIPT lesson uses the newer Support Hub) and click **Register**.
2. Fill in the login data: email and password. Only a **business or professional email** is accepted; Gmail, Yahoo and similar addresses are rejected and there is no alternative.
3. Enter personal data (name, phone, time zone) and company data. Tricentis verifies the company data later, when the license request is processed. Fields other than email, password, name and time zone are optional. The Tosca 16 lesson shows the form with title, country, street, city, ZIP, language and business address as well; the business email is entered twice, and the phone number is marked optional.
4. Accept the privacy policy, pass the *I'm not a robot* check and submit. A verification mail arrives (it may take a while); click **Verify me now**. Until you verify, the portal shows an error on login.

Registration is a one-time activity per user.

## Step 2a: request a training license (support portal route)

1. Log in to the support portal and open the training license request page: `https://support.tricentis.com/community/training_license_request.do` (the address read out in the LambdaGeeks tutorial). The QASCRIPT lesson, recorded later, reaches the same page from the Support Hub with the query parameter `id=training_license_request`; the full Support Hub address is only shown on screen, so take it from the video or its description if the older URL no longer resolves.
2. Choose the **preferred license type**:
   - **Cloud**: Commander connects to Tricentis' cloud license server with your portal credentials. Recommended, because it works from any machine.
   - **On-premise**: a license installed on a standalone machine. While a cloud request is pending you cannot also request an on-premise one.
3. Submit (the button reads **Request cloud training license** in the Tosca 16 lesson). A success popup and a mail confirming that the request went to the support team follow. The request shows the state **Deploying**; a Tricentis manager approves it, a second mail announces the approval, and the state changes to **Deployed**. Refresh the page until you see it; then the license is ready.

Once the license is deployed, the portal's **Downloads** tab lists the products you may download; see [Installation](/ToscaBase/getting-started/installation/).

:::note
The training license is provided for learning only and must not be used for anything else. The LambdaGeeks tutorial states a 60-day term; the QASCRIPT lesson, recorded later, says only "a limited amount of time". Check the portal for the current term.
:::

## Step 2b: request a free trial on tricentis.com (newer route)

Tricentis later simplified the process: the download and the trial license come from the product website rather than the support portal.

1. On `tricentis.com` go to **Demos and trials**, find Tosca and click **Free trial**.
2. Check the system requirements shown on the page: about 1.4 GB of disk space, five to ten minutes of download on a stable connection, Windows 7 or later.
3. Fill in the form: email address, the required details, optionally your role and your goals for the trial (for example, learning Tosca). Submit.
4. The confirmation page explains what happens next, links videos for installing, activating the license and creating a first TestCase, and offers the installer download (about 1.4 GB for Tosca 15 LTS at the time of recording; other versions differ, [Installation](/ToscaBase/getting-started/installation/) quotes 1.5 GB).

The trial can be extended by 30 days; beyond that you must contact Tricentis. The trial covers Tosca only, not NeoLoad or qTest.

:::caution
Use the **same email** for the trial request and for the support portal account. Commander authenticates against the cloud license server with the portal credentials, and the trial is tied to the email it was requested with.
:::

## Step 3: connect Tosca Commander to the license server

The first time Commander starts without a license it opens the license page directly. Otherwise:

1. **Project > License**. If a license is already active the page says so.
2. Under **Activate**, click **Connect**. The options are a self-hosted license server, licenses from the local machine, and **Connect to cloud hosted license server**.
3. Choose **Connect to cloud hosted license server** and click **OK**.
4. Enter the username (your support portal email) and password and confirm. Commander reports that it is retrieving your cloud licenses; after a few seconds a message confirms that you are connected to the license server and can use Tosca Commander right away.

This is a one-time step: on later starts Commander validates and reconnects automatically. The same connection can be made from the separate **Tosca License Configuration** utility installed with Tosca, which offers the same **Connect** option.

## Related

- [Installation](/ToscaBase/getting-started/installation/) for downloading and running the installer, including on an AWS Windows server.
- [What's new in Tosca 16](/ToscaBase/getting-started/whats-new-in-tosca-16/) mentions the extended cloud license support for administrators.
