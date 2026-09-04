---
title: Tosca Automation Extension
description: Why XScan needs the Tosca Automation Extension in the browser, how to install it in Chrome and Edge by hand, and a tour of the Tricentis demo web shop that the Tosca 16 lessons automate.
level: 1
sidebar:
  order: 45
sources:
  - id: 31ARJsbViJk
    title: "TRICENTIS Tosca 16.0 - Lesson 04 | Install Tosca Automation Extension | Introduction to SUT"
    url: https://www.youtube.com/watch?v=31ARJsbViJk
    at: "02:06"
---

Tosca steers web pages through its **XBrowser engine**, and XScan turns a page into **XBrowser Modules**, the object repository of the application's controls and locators. The engine can only reach a browser that has the **Tosca Automation Extension** installed, so the extension is a prerequisite for scanning or running anything on the web. This page covers installing it by hand in Chrome and Edge (Tosca can also prompt you into it on the first scan, see [Installation](/ToscaBase/getting-started/installation/#browser-extension-for-xscan)) and introduces the **system under test** that the Tosca 16 lessons automate from [First TestCase](/ToscaBase/getting-started/first-test-case/) onwards.

## Which browsers

Tricentis publishes the extension for **Chrome**, **Firefox** and **Edge**. The extension page on the Tricentis site links the store entry for each browser; the lesson uses the entry labelled for Tosca 13.2 and upwards, which is the right one for Tosca 16.

## Install in Chrome

1. Open the Tricentis extension page, pick **Google Chrome** and follow the link for Tosca 13.2 and upwards; it opens the Chrome Web Store. Alternatively search the Web Store for *Tosca automation extension*.
2. Click **Add to Chrome**, then **Add extension** in the confirmation dialog.
3. The extension icon appears in Chrome's extension list. Nothing else is configured.

If the extension is already installed and you want to reinstall it, remove it from Chrome first; the store page then shows **Add to Chrome** again.

## Install in Edge

1. Open **Edge Add-ons** in Edge and search for *Tosca automation extension*.
2. In the result **Tosca Automation Extension for Microsoft Edge** click **Get**, then **Add extension**.
3. The extension appears in Edge's extension list.

:::note
Without the extension in the browser you are scanning, XScan cannot create XBrowser Modules, and an existing TestCase cannot steer the page. Install it in every browser you intend to use as a value of the `Browser` Test Configuration Parameter.
:::

## The system under test: Tricentis demo web shop

The **system under test** is the application you test or automate. The lessons use the Tricentis **demo web shop**, a public e-commerce site built for training. Anyone can register, and you should do so before continuing so that the login steps of later lessons work with your own account.

- **Register**: gender, first name, last name, email, password and confirmation.
- **Log in / Log out** from the top menu.
- **Product categories** (books, computers, electronics, apparel and shoes and others): open a category, pick a product such as *Blue Jeans*, set a quantity and click **Add to cart**; a message confirms that the product is in the shopping cart.
- **Shopping cart**: apply a discount coupon or a gift card code, tick *agree to the terms of service*, and click **Checkout**.
- **Checkout** runs through billing address (a new one or an existing one), shipping address (same as billing, or in-store pickup), shipping method (ground, next day, second day, each with a different price), payment method (cash on delivery, check or money order, credit card, purchase order) and payment information, then a confirmation page that repeats billing and shipping addresses, shipping and payment methods, prices, quantity, tax and total. **Confirm** places the order and returns an order number.

This flow is what the lessons automate step by step: log in, navigate to a category, order a product, go through checkout, verify the prices and the success page, log out. Every page in it becomes a Module (login page, top menu, product choice tab, shopping cart, billing address, shipping method, payment method and so on), and the TestCase strings the Modules together.

## Next

- [Workspace and project setup](/ToscaBase/getting-started/workspace-and-project-setup/) explains the `Automation Specialist Level 1 Base.tsu` subset, which already contains Modules for the demo web shop.
- [XScan](/ToscaBase/modules/xscan/) shows how the extension is used to scan a page.
