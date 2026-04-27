---
title: "Taming Flaky Tests: A Systematic Approach"
description: Flaky tests erode trust in your CI pipeline. Here's a repeatable process for diagnosing and fixing them instead of just re-running.
date: 2024-05-22
updated: 2024-08-14
tags:
  - devops
---

A flaky test is one that passes and fails on the same code with no changes. Every team above a certain size eventually accumulates them. The standard response — "just re-run" — is a tax that compounds. This post outlines how to systematically find and eliminate flakiness rather than live with it.

## Why flakiness is a CI problem, not just a test problem

When a test is known to be unreliable, people stop trusting the signal. A red build becomes "probably just a flaky test" instead of "something broke." At that point, your CI pipeline is providing less information than no pipeline at all.

The goal is zero tolerance: every failure should be investigated, not retried.

## Categories of flakiness

Most flaky tests fall into a small number of categories:

**Timing dependencies** — test assumes an operation completes in a fixed time window. Common with animations, network calls, or setTimeout usage in integration tests.

**Shared state** — tests pollute global state (database rows, environment variables, module singletons) that a later test depends on being clean.

**Test order dependence** — test B passes only if test A ran first. Randomizing test order surfaces these.

**External service calls** — tests that make real HTTP requests will flake whenever the service is slow or unavailable.

**Race conditions** — concurrent code whose outcome depends on timing.

## A diagnostic process

```bash
# Run the suspect test 50 times and log failures
for i in $(seq 1 50); do
  npm test -- --testPathPattern="flaky.test.ts" 2>&1 | grep -E "PASS|FAIL" >> flaky-log.txt
done
grep "FAIL" flaky-log.txt | wc -l
```

If it fails, check the failure message. Is it always the same assertion? Does it correlate with other parallel tests?

Next, isolate:

```bash
# Run only the suspect test, no parallelism
npx jest --runInBand --testPathPattern="flaky.test.ts" --verbose
```

If it passes in isolation but fails in the full suite, the culprit is shared state or test order.

## Fixing the common cases

**Timing**: Replace `setTimeout`/`sleep` with explicit waits or polling.

```ts
// Fragile
await new Promise(r => setTimeout(r, 500));
expect(element).toBeVisible();

// Robust
await waitFor(() => expect(element).toBeVisible(), { timeout: 3000 });
```

**Shared state**: Ensure each test owns its setup and teardown.

```ts
beforeEach(async () => {
  await db.clear();
  await db.seed(fixtures.default);
});

afterEach(async () => {
  await db.clear();
});
```

**External calls**: Use deterministic fakes or recorded responses.

```ts
// Record once, replay deterministically
nock('https://api.example.com')
  .get('/users/1')
  .reply(200, { id: 1, name: 'Alice' });
```

## Tracking flakiness over time

A useful pattern: fail the build if a test has flaked more than N times in the last 30 days. Most CI systems support flakiness metrics natively now (GitHub Actions, BuildKite, CircleCI all have some form of this). Using them gives you data to prioritize fixes rather than playing whack-a-mole.

The payoff from a stable test suite is large. A green build that you trust is one of the highest-leverage artifacts in a software team.
