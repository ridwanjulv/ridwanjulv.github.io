---
title: Trying Claude Code for the First Time, Starting With Memory
date: 2026-04-02 00:00:00 +0700
categories: [ai, tools]       # only 2 level supported
tags: [ai, claudecode]    # TAG names should always be lowercase
---

# Trying Claude Code for the First Time, Starting With Memory

I have some project in my mind that I'd like to build, but I know doing it manually will takes time. That's why I look at AI and its promise. I know some people hates it, but other loves it. I know I need to do it myself before making up my mind about AI.

## Getting Setup

Everyone I follow who codes for a living has mentioned Claude Code at some point in the last few months. I kept noticing it, kept telling myself I'd look into it properly, and kept not doing it. 

Last week I finally installed it. I decided not to just throw a task at it immediately and see what happened. I wanted to understand the pieces first. A lot of people swear by CLAUDE.md, so that's where I started.

The question I was trying to answer was simple: What is this? How does the memory works? How should I use this for my POC  project?

## What CLAUDE.md Actually Is

As always, first let's see the official documentation say on [Memory](https://code.claude.com/docs/en/memory)

It is clear that *CLAUDE.md files are markdown files that give Claude persistent instructions for a project, your personal workflow, or your entire organization. You write these files in plain text; Claude reads them at the start of every session.*

That's it. You write instructions in it and Claude reads them before anything else happens. Emphasis on *loaded into the context window at the start of every session, consuming tokens alongside your conversation*. Oops. Okay, cool. So keep it short, specific, concise and well structured. Target less than 200 lines per file. 

Okay, now let's get it done.

## Writing the First File

My POC will use React Vite for the web, ReactNative for the mobile portion and nodeJS for the backend.

Knowing nothing, and in the spirit of maximizing AI usage, I turn to the AI again for preparing the first version. Here's what it give me, which looks good enough. For now. We'll see how it will looks like once the POC completed.

1. React Vite:

```
## Build & Development
- **Install:** `npm install`
- **Dev:** `npm run dev`
- **Build:** `npm run build`
- **Lint:** `npm run lint`

## Code Style & Patterns
- **Architecture:** Functional components with Hooks. Prefer `const Component = () => {}`.
- **Styling:** Tailwind CSS (utility-first). Avoid inline styles unless dynamic.
- **State:** Use `useState`/`useContext` for local/global state. Use TanStack Query for server state.
- **TypeScript:** Strict mode. Define interfaces for Props and API responses in `types/`.
- **Imports:** Use absolute paths `@/...` if configured. Group imports: React, third-party, local components, styles.

## Guidance
- Keep components small and focused (Single Responsibility).
- Use `lucide-react` for icons.
- Ensure all components are responsive and accessible (ARIA labels).
```

2. ReactNative:

```
## Build & Development
- **Install:** `npm install` (and `npx pod-install` for iOS)
- **Start:** `npx expo start` or `npm start`
- **Android:** `npm run android`
- **iOS:** `npm run ios`

## Code Style & Patterns
- **Layout:** Flexbox only. Use `SafeAreaView` for screen wrappers.
- **Navigation:** React Navigation (Native Stack). Keep navigation logic in `src/navigation/`.
- **Components:** Use `Pressable` over `TouchableOpacity`. Use `Image` from `expo-image` if applicable.
- **Performance:** Use `useMemo` and `useCallback` for heavy list items or expensive calculations.
- **Styling:** Use `StyleSheet.create`. No shorthand like `margin: 10 5` (not supported in RN).

## Guidance
- Always consider "keyboard avoidance" for input screens.
- Use `Platform.OS` only when behavior must diverge between iOS and Android.
- Test UI against both small screens and Notch/Dynamic Island devices.
```

3. NodeJS:

```
## Build & Development
- **Install:** `npm install`
- **Dev:** `npm run dev` (using nodemon/tsx)
- **Test:** `npm test`
- **Env:** Ensure `.env` is populated based on `.env.example`.

## Code Style & Patterns
- **Runtime:** Node.js LTS (ES Modules preferred over CommonJS).
- **Architecture:** Controller-Service-Repository pattern.
- **Error Handling:** Use `try/catch` in controllers with a global error-handling middleware. Never leak stack traces in production.
- **API:** RESTful conventions. Use `Zod` for request validation.
- **Database:** Prisma ORM. Keep migrations in `prisma/schema.prisma`.

## Guidance
- **Security:** Sanitize all inputs. Use `helmet` and `cors` middleware.
- **Logging:** Use `pino` or `winston` for structured JSON logging.
- **Async:** Always await Promises; avoid floating promises unless explicitly detached.
```


## What's next

There's /rules approach and auto-memory system. But next let's go with building the skeleton first.

See you in next article.