---
title: "TypeScript Discriminated Unions: Stop Using Optional Properties"
description: Optional properties spread uncertainty through your types. Discriminated unions give you precise types for every state your data can be in.
date: 2024-11-18
tags:
  - javascript
---

Optional properties feel ergonomic when you're modeling state that changes over time. In practice, they create types that permit impossible states and force narrowing everywhere the data is used.

Discriminated unions are the better pattern. Here's the before and after.

## The optional property trap

A common way to model an async operation:

```ts
type AsyncData<T> = {
  loading: boolean;
  data?: T;
  error?: Error;
};
```

This type allows combinations that should never exist: `loading: true` with `data` set, or both `data` and `error` set simultaneously. Every consumer has to defensively check `data !== undefined` even when they know the operation succeeded.

## Discriminated unions

Model each state explicitly:

```ts
type AsyncData<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };
```

Now TypeScript understands which fields are available in each state:

```ts
function render<T>(state: AsyncData<T>) {
  switch (state.status) {
    case 'idle':
      return null;
    case 'loading':
      return <Spinner />;
    case 'success':
      return <View data={state.data} />; // data is T, not T | undefined
    case 'error':
      return <ErrorBanner message={state.error.message} />;
  }
}
```

No optional chaining, no non-null assertions, no "should never happen" comments.

## Exhaustiveness checking

Add a default branch that narrows to `never`:

```ts
function assertNever(x: never): never {
  throw new Error(`Unhandled case: ${JSON.stringify(x)}`);
}

function render<T>(state: AsyncData<T>) {
  switch (state.status) {
    case 'idle': return null;
    case 'loading': return <Spinner />;
    case 'success': return <View data={state.data} />;
    case 'error': return <ErrorBanner message={state.error.message} />;
    default: return assertNever(state);
  }
}
```

If you add a new variant to `AsyncData` and forget to handle it in `render`, TypeScript will produce a compile error at the `assertNever` call. Exhaustiveness checking turns adding states into a safe, compiler-guided refactor.

## When optional properties are still fine

Not every optional property is a design smell. Optional properties make sense for configuration objects, partial updates, and optional UI features. The pattern to avoid is optional properties that represent **mutually exclusive states** — where some combination of fields is invalid.

If you find yourself writing `if (data && !error)` in more than one place, that's a sign a discriminated union would serve the shape better.
