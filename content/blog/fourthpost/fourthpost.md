---
title: "TIL: CSS :has() Is a Parent Selector and It Changes Everything"
description: The :has() pseudo-class finally gives CSS a parent selector. Here's what that unlocks.
date: 2024-09-05
tags:
  - til
---

Today I learned (well, internalized for the first time) what `:has()` actually makes possible in CSS.

## What it does

`:has()` selects an element if any of its descendants match the argument. The practical effect: it's a parent selector.

```css
/* Card that contains an image gets extra padding */
.card:has(img) {
  padding: 0;
}

/* Form that has an invalid input gets a red border */
form:has(:invalid) {
  border: 2px solid #c00;
}

/* Nav item whose link is the current page gets a dot */
.nav-item:has(a[aria-current="page"])::before {
  content: "→ ";
}
```

Before `:has()`, you needed JavaScript to do these things: listen for events, walk up the DOM, toggle classes on parent elements.

## Browser support

As of late 2023, `:has()` has full support in Chrome, Safari, Firefox, and Edge. Baseline 2023. The time to start using it is now.

## The thing that surprised me

You can combine it with sibling selectors to create conditional styling based on what follows an element:

```css
/* h2 followed by a paragraph — add less top margin */
h2:has(+ p) {
  margin-bottom: 0.5rem;
}

/* Figure that directly contains a figcaption — center the caption */
figure:has(> figcaption) {
  text-align: center;
}
```

This is expressive in a way that previously required either extra wrapper markup or JavaScript. It moves a whole category of layout logic back into CSS where it belongs.

## One gotcha

`:has()` cannot be nested inside most pseudo-elements and has some specificity quirks. The specificity of `:has(a.active)` is calculated as if you wrote `a.active` directly.
