---
title: "JavaScript Closures: What They Are and When They Bite You"
description: A practical look at closures in JavaScript — how they work, why they matter, and three patterns where they cause subtle bugs.
date: 2024-03-15
tags:
  - javascript
---

Closures are one of those JavaScript concepts that developers use every day without necessarily thinking about them. They also cause some of the sneakiest bugs in the language. This post covers what closures actually are, a mental model for reasoning about them, and three real-world patterns where they trip people up.

## What a closure is

A closure is a function that retains access to variables from the scope in which it was defined, even after that outer function has returned.

```js
function makeCounter() {
  let count = 0;
  return function increment() {
    count++;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

`increment` closes over `count`. Even though `makeCounter` has returned, the returned function still has a live reference to that variable.

The key insight: closures capture **variables**, not values. When the variable changes, the closure sees the change.

## The loop bug

This is probably the most common closure pitfall in older JavaScript:

```js
// Broken
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // prints 3, 3, 3
  }, 100);
}
```

All three callbacks share the same `i` variable (because `var` is function-scoped). By the time the timeouts fire, the loop has finished and `i` is `3`.

The `let` fix works because `let` is block-scoped — each loop iteration creates a fresh binding:

```js
// Fixed
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i); // prints 0, 1, 2
  }, 100);
}
```

## Event listeners and stale state

When you attach event listeners inside a function, each listener closes over the variables in scope at that time. This can lead to listeners holding stale references:

```js
function attachListeners(items) {
  items.forEach(function(item) {
    item.element.addEventListener('click', function() {
      // Closes over `item` — each listener has its own binding
      console.log(item.name);
    });
  });
}
```

This is actually the *correct* behavior here. The problem arises when you mutate the object:

```js
let config = { debug: false };

button.addEventListener('click', function() {
  console.log(config.debug); // always reads the current value
});

config.debug = true; // listener will now log `true`
```

Because closures capture variables (references to objects), not the objects themselves, mutations are visible. If you intended to snapshot the value, you need to copy it explicitly.

## Closures in React hooks

In React, stale closures are a frequent source of bugs with `useEffect` and `useCallback`:

```js
function SearchInput({ onSearch }) {
  const [query, setQuery] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      onSearch(query); // Might capture a stale `query`
    }, 300);
    return () => clearTimeout(timer);
  }, [query, onSearch]); // Declaring deps ensures fresh closure
}
```

The dependency array is essentially telling React "this effect closes over these variables — re-run it if they change." Omitting a dependency creates a stale closure.

The eslint-plugin-react-hooks exhaustive-deps rule exists specifically to catch this category of bug.

## Summary

- Closures capture variables, not values at the time of creation
- `let` and `const` in loops create new bindings per iteration; `var` does not
- Mutations to closed-over objects are visible to all functions sharing that reference
- In React, the dependency array prevents stale closure bugs in hooks
