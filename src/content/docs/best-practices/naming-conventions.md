---
title: Naming conventions
description: Why consistent names for Modules, TestCases, folders and TestSteps decide whether a Tosca project stays maintainable, with a before-and-after example.
level: 3
sidebar:
  order: 10
sources:
  - id: 09bxXvoB5zo
    title: "Tosca Tutorial | Lesson 97 - Use Proper Naming Conventions | Best Practices |"
    url: https://www.youtube.com/watch?v=09bxXvoB5zo
    at: "01:08"
---

A naming convention is a rule the whole team follows for how Modules, TestCases, TestStep folders and TestSteps are named. Tricentis lists it as the first of its recommended best practices, and it is the one that costs nothing to adopt and the most to skip: without it a project fills with duplicate Modules, becomes unreadable for anyone who did not build it, and loses the reusability that is the whole point of model-based testing.

## What goes wrong without a convention

When you scan an application with XScan and drag Modules into a TestCase, Tosca assigns default names. It derives them from the screen or the functionality it scanned, so a checkout flow produces a Module called `Demo Webshop Checkout` for every page of the checkout, and the recorded TestCase inherits the same names for its TestSteps. `Open URL` is still understandable; three TestSteps all called `Demo Webshop Checkout` are not.

The consequences appear once the project grows or a second person joins:

- **Nobody can tell what a Module does.** Is `Demo Webshop Checkout` the billing address page, the shipping method page or the payment page? A newcomer cannot know without opening every one.
- **Duplicate Modules and TestCases.** People who cannot find the right object scan it again, so the workspace accumulates copies of the same screen (see [Module hygiene](/ToscaBase/best-practices/module-hygiene/)).
- **Higher maintenance, lower reuse.** Each duplicate has to be maintained separately, and a Module nobody recognises is a Module nobody reuses.
- **The TestCase flow is invisible.** Looking at the list of TestSteps does not tell you what the test does.

The same reasoning applies to any automation tool and to development in general; it is not a Tosca-specific rule.

## What a well-named TestCase looks like

The convention itself is up to the team, but the example in the source shows the shape that works:

1. **Top-level folders describe phases.** `Pre-processing` (open the URL), `Processing` (the actual scenario) and `Post-processing` (log out, cleanup). See [TestCase structure](/ToscaBase/best-practices/test-case-structure/) for why folders matter.
2. **Sub-folders describe functionality or pages.** `Register user`, `Login user`, `Add products to cart`, `Shopping cart`, `Checkout`, `Confirm order`, `Verify PDF order information`.
3. **TestSteps describe the action, not the screen.** The name says what the step does: *click* `Register`, *buffer* the email, first name and last name, *verify* the logout link. Because a TestStep is a Module plus an ActionMode, the verb (click, verify, buffer) belongs in the step name, not in the Module name.
4. **Steps on the same Module get a separator plus a qualifier.** Checkout spans several pages, so the steps become `Checkout - Billing address`, `Checkout - Shipping address`, `Checkout - Shipping method`, and so on. The separator makes clear that they share a flow while still telling them apart.
5. **Module names match the step names.** The Module used for the billing address is called `Checkout Billing Address`, so a reader who jumps from TestStep to Module lands on something recognisable.

Read from top to bottom, such a TestCase is documentation of its own flow: open the URL, register a user, log out, log in, add products, go to the cart, check out page by page, confirm, verify the invoice.

## Rules of thumb

- Decide the convention before scanning the first Module, and write it down so new team members follow it.
- Rename Modules right after XScan; the default names are only a starting point.
- Rename TestSteps as soon as you set the ActionMode, while you still remember what the step is for.
- Apply the convention to every object type: Modules, ModuleAttributes, TestCases, folders, TestSteps. Consistency across the team matters more than the specific format.

:::tip
Naming conventions are a common Tosca interview question. Being able to explain both the convention and the reasons behind it (readability, no duplicates, reusability, lower maintenance) is what interviewers look for.
:::

Related: [TestCase structure](/ToscaBase/best-practices/test-case-structure/), [Module hygiene](/ToscaBase/best-practices/module-hygiene/), [Review process](/ToscaBase/best-practices/review-process/).
