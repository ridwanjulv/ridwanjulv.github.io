## Easy instructions for quick setup

[

![Alex Nedopaka](https://miro.medium.com/v2/resize:fill:88:88/1*zD3GxCgIHW1nkFBYsCKL-g.png)



](https://medium.com/@nedopaka?source=post_page-----62ecff357c7b--------------------------------)

Even with React frameworks like Next.js gaining popularity and React [documentation](https://react.dev/learn/start-a-new-react-project) advocating their use, still many developers tend to start with just using the React library without the additional tools available in the framework out of the box, as this extra layer introduces additional complexity that is unnecessary in many cases.

Since create-react-app is no longer supported, I’ve found that the best alternative for creating a new React app is to use Vite.

Below I pasted short description from the official [documentation](https://vitejs.dev/guide/).

Vite (French word for “quick”, pronounced `/vit/`, like “veet”) is a build tool that aims to provide a faster and leaner development experience for modern web projects. It consists of two major parts:

-   A dev server that provides [rich feature enhancements](https://vitejs.dev/guide/features) over [native ES modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), for example extremely fast [Hot Module Replacement (HMR)](https://vitejs.dev/guide/features#hot-module-replacement).
-   A build command that bundles your code with [Rollup](https://rollupjs.org/), pre-configured to output highly optimized static assets for production.

Vite is opinionated and comes with sensible defaults out of the box.

So, let’s create a new React project with Vite by executing the following command:

```
<span id="70e1" data-selectable-paragraph="">npm <span>create</span> vite<span>@latest</span></span>
```

First, you’ll be asked for project name:

```
<span id="1cc9" data-selectable-paragraph="">npm <span>create</span> vite<span>@latest</span><br>? Project name: › vite<span>-</span>project</span>
```

Then it asks for a framework to choose:

```
<span id="d7cd" data-selectable-paragraph="">npm <span>create</span> vite<span>@latest</span><br>✔ Project name: … vite<span>-</span>project<br>? <span>Select</span> a framework: › <span>-</span> Use arrow<span>-</span>keys. <span>Return</span> <span>to</span> submit.<br>❯   Vanilla<br>    Vue<br>    React<br>    Preact<br>    Lit<br>    Svelte<br>    Solid<br>    Qwik<br>    Others</span>
```

Select React and hit Enter.

Then you need to choose whether to use JavaScript/TypeSprit with Babel/SWC:

```
<span id="e76f" data-selectable-paragraph="">npm <span>create</span> vite<span>@latest</span><br>✔ Project name: … vite<span>-</span>project<br>✔ <span>Select</span> a framework: › React<br>? <span>Select</span> a variant: › <span>-</span> Use arrow<span>-</span>keys. <span>Return</span> <span>to</span> submit.<br>❯   TypeScript<br>    TypeScript <span>+</span> SWC<br>    JavaScript<br>    JavaScript <span>+</span> SWC</span>
```

Let’s choose **JavaScript + SWC** considering to work with a small project without type checking. SWC is a free and open-source JavaScript transcompiler like Babel, but unlike Babel it can significantly speed up build and development time due to SWC’s fast conversion capabilities, however it may not support all Babel plugins.

SWC plays an integral role in the Vite ecosystem. Vite uses SWC to run the Babel transformation pipeline much faster, which is especially useful for large React projects.

It is worth mentioning that Vite also uses Rollup for efficient production builds and supports most Rollup plugins. Thus, Vite offers lightning-fast development and reliable performance in production.

It’s a final step, and then you should see something like this:

```
<span id="dea2" data-selectable-paragraph="">npm create vite<span>@latest</span><br>✔ Project <span>name</span>: … vite-project<br>✔ Select a <span>framework</span>: › React<br>✔ Select a <span>variant</span>: › JavaScript + SWC<br><br>Scaffolding project in /Users/Alex_Nedopaka/vite-project...<br><br>Done. Now <span>run</span>:<br><br>  cd vite-project<br>  npm install<br>  npm run dev</span>
```

Now go to the project folder, install dependencies, start dev server to check that everything works fine.

![](https://miro.medium.com/v2/resize:fit:700/0*XpyCGYy-69S5XSHR.png)

Default page with App component

Let’s have a look what we’ve got in our `package.json` now:

```
<span id="590d" data-selectable-paragraph=""><span>{</span><br>  <span>"name"</span><span>:</span> <span>"vite-project"</span><span>,</span><br>  <span>"private"</span><span>:</span> <span><span>true</span></span><span>,</span><br>  <span>"version"</span><span>:</span> <span>"0.0.0"</span><span>,</span><br>  <span>"type"</span><span>:</span> <span>"module"</span><span>,</span><br>  <span>"scripts"</span><span>:</span> <span>{</span><br>    <span>"dev"</span><span>:</span> <span>"vite"</span><span>,</span><br>    <span>"build"</span><span>:</span> <span>"vite build"</span><span>,</span><br>    <span>"lint"</span><span>:</span> <span>"eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0"</span><span>,</span><br>    <span>"preview"</span><span>:</span> <span>"vite preview"</span><br>  <span>}</span><span>,</span><br>  <span>"dependencies"</span><span>:</span> <span>{</span><br>    <span>"react"</span><span>:</span> <span>"^18.2.0"</span><span>,</span><br>    <span>"react-dom"</span><span>:</span> <span>"^18.2.0"</span><br>  <span>}</span><span>,</span><br>  <span>"devDependencies"</span><span>:</span> <span>{</span><br>    <span>"@types/react"</span><span>:</span> <span>"^18.2.55"</span><span>,</span><br>    <span>"@types/react-dom"</span><span>:</span> <span>"^18.2.19"</span><span>,</span><br>    <span>"@vitejs/plugin-react-swc"</span><span>:</span> <span>"^3.5.0"</span><span>,</span><br>    <span>"eslint"</span><span>:</span> <span>"^8.56.0"</span><span>,</span><br>    <span>"eslint-plugin-react"</span><span>:</span> <span>"^7.33.2"</span><span>,</span><br>    <span>"eslint-plugin-react-hooks"</span><span>:</span> <span>"^4.6.0"</span><span>,</span><br>    <span>"eslint-plugin-react-refresh"</span><span>:</span> <span>"^0.4.5"</span><span>,</span><br>    <span>"vite"</span><span>:</span> <span>"^5.1.0"</span><br>  <span>}</span><br><span>}</span></span>
```

Vite kindly preinstalls ESLint for us. In `.eslintrc.cjs` we already have necessary rules for the code quality, and it provides us error highlights in our code.

![](https://miro.medium.com/v2/resize:fit:700/1*yQBoRlhD5nLuBSbB_hMCvg.png)

src/App.jsx

Keep in mind, that you should have installed ESLint plugin to make it work.

![](https://miro.medium.com/v2/resize:fit:700/0*sBuNsN1RezAGwguW.png)

ESLint extension for VS Code

Looking on `package.json` it has come to my attention that there are 2 packages with type declarations, although we do not use TypeScript in our project. Let’s get rid of them with `npm rm` command.

```
<span id="66dc" data-selectable-paragraph="">npm <span>rm</span> @types/react @types/react-dom</span>
```

Now let’s install Prettier to make our code look nice.

```
<span id="b2ff" data-selectable-paragraph="">npm <span>i</span> -D -E prettier</span>
```

And then create `.prettierrc` with the following content:

```
<span id="2c40" data-selectable-paragraph=""><span>{</span><br>  <span>"semi"</span><span>:</span> <span><span>true</span></span><span>,</span><br>  <span>"singleQuote"</span><span>:</span> <span><span>true</span></span><span>,</span><br>  <span>"trailingComma"</span><span>:</span> <span>"es5"</span><br><span>}</span></span>
```

To prevent conflicts in rules between ESLint and Prettier let’s add the following plugin:

```
<span id="6ca2" data-selectable-paragraph="">npm <span>i</span> -D eslint-config-prettier</span>
```

Then make changes in `.eslintrc.cjs` to match the following:

```
<span id="127a" data-selectable-paragraph=""><span>module</span>.<span>exports</span> = {<br>  <span>root</span>: <span>true</span>,<br>  <span>env</span>: { <span>browser</span>: <span>true</span>, <span>es2020</span>: <span>true</span> },<br>  <span>extends</span>: [<br>    <span>'eslint:recommended'</span>,<br>    <span>'plugin:react/recommended'</span>,<br>    <span>'plugin:react/jsx-runtime'</span>,<br>    <span>'plugin:react-hooks/recommended'</span>,<br>    <br>    <br>    <span>'prettier'</span>,<br>  ],<br>  <span>ignorePatterns</span>: [<span>'dist'</span>, <span>'.eslintrc.cjs'</span>],<br>  <span>parserOptions</span>: { <span>ecmaVersion</span>: <span>'latest'</span>, <span>sourceType</span>: <span>'module'</span> },<br>  <span>settings</span>: { <span>react</span>: { <span>version</span>: <span>'18.2'</span> } },<br>  <span>plugins</span>: [<span>'react-refresh'</span>],<br>  <span>rules</span>: {<br>    <span>'react/jsx-no-target-blank'</span>: <span>'off'</span>,<br>    <span>'react-refresh/only-export-components'</span>: [<br>      <span>'warn'</span>,<br>      { <span>allowConstantExport</span>: <span>true</span> },<br>    ],<br>  },<br>};</span>
```

And then add the following script to our `package.json`:

```
<span id="32c9" data-selectable-paragraph=""><span>"format"</span><span>:</span> <span>"prettier --write ./src"</span><span>,</span></span>
```

Now we can do `npm run format` to format All our source code, but it would be great if we could format our files automatically on paste and save actions.

For this, install Prettier plugin for VS Code.

![](https://miro.medium.com/v2/resize:fit:700/0*itLQPnoB36MTpW9C.png)

Prettier extension for VS Code

And then create `.vscode/settings.json` so we can use this project as a boilerplate for every our new React project.

```
<span id="0e15" data-selectable-paragraph=""><span>{</span><br>  <span>"editor.defaultFormatter"</span><span>:</span> <span>"esbenp.prettier-vscode"</span><span>,</span><br>  <span>"editor.formatOnPaste"</span><span>:</span> <span><span>true</span></span><span>,</span> <br>  <span>"editor.formatOnType"</span><span>:</span> <span><span>false</span></span><span>,</span> <br>  <span>"editor.formatOnSave"</span><span>:</span> <span><span>true</span></span><span>,</span> <br>  <span>"editor.formatOnSaveMode"</span><span>:</span> <span>"file"</span><span>,</span> <br>  <span>"files.autoSave"</span><span>:</span> <span>"onFocusChange"</span> <br><span>}</span></span>
```

Next, considering that we’re going to write unit tests for our code, let’s install the following dependencies:

```
<span id="76c6" data-selectable-paragraph="">npm <span>i</span> -D vitest jsdom <span>@testing-library</span>/jest-dom @testing-library/react</span>
```

Then create `src/__tests__/setup.js` and insert the following code:

```
<span id="4429" data-selectable-paragraph=""><br><br><br><br><span>import</span> <span>'@testing-library/jest-dom'</span>;</span>
```

Also, then modify `vite.config.js` to match:

```
<span id="982e" data-selectable-paragraph="">import { defineConfig } <span>from</span> <span>'vite'</span>;<br>import react <span>from</span> <span>'@vitejs/plugin-react-swc'</span>;<br><br><br>export <span>default</span> <span>defineConfig</span>({<br>  <span>plugins</span>: [<span>react</span>()],<br>  <span>test</span>: {<br>    <span>globals</span>: <span>true</span>,<br>    <span>environment</span>: <span>'jsdom'</span>,<br>    <span>setupFiles</span>: [<span>'src/__tests__/setup.js'</span>],<br>  },<br>});</span>
```

Now we’re ready to write our first test `App.test.jsx`:

```
<span id="55d3" data-selectable-paragraph=""><span>import</span> { describe, it, expect, test } <span>from</span> <span>'vitest'</span>;<br><span>import</span> { render } <span>from</span> <span>'@testing-library/react'</span>;<br><span>import</span> <span>App</span> <span>from</span> <span>'./App'</span>;<br><br><span>test</span>(<span>'demo'</span>, <span>() =&gt;</span> {<br>  <span>expect</span>(<span>true</span>).<span>toBe</span>(<span>true</span>);<br>});<br><br><span>describe</span>(<span>'render'</span>, <span>() =&gt;</span> {<br>  <span>it</span>(<span>'renders the main page'</span>, <span>() =&gt;</span> {<br>    <span>render</span>(&lt;App /&gt;);<br>    <span>expect</span>(<span>true</span>).<span>toBeTruthy</span>();<br>  });<br>});</span>
```

Finally, add the following script in `package.json`:

```
<span id="64f6" data-selectable-paragraph=""><span>"test"</span><span>:</span> <span>"vitest"</span></span>
```

Your `package.json` should look similar to:

```
<span id="0fa5" data-selectable-paragraph=""><span>{</span><br>  <span>"name"</span><span>:</span> <span>"vite-project"</span><span>,</span><br>  <span>"private"</span><span>:</span> <span><span>true</span></span><span>,</span><br>  <span>"version"</span><span>:</span> <span>"0.0.0"</span><span>,</span><br>  <span>"type"</span><span>:</span> <span>"module"</span><span>,</span><br>  <span>"scripts"</span><span>:</span> <span>{</span><br>    <span>"dev"</span><span>:</span> <span>"vite"</span><span>,</span><br>    <span>"build"</span><span>:</span> <span>"vite build"</span><span>,</span><br>    <span>"format"</span><span>:</span> <span>"prettier --write ./src"</span><span>,</span><br>    <span>"lint"</span><span>:</span> <span>"eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0"</span><span>,</span><br>    <span>"preview"</span><span>:</span> <span>"vite preview"</span><span>,</span><br>    <span>"test"</span><span>:</span> <span>"vitest"</span><br>  <span>}</span><span>,</span><br>  <span>"dependencies"</span><span>:</span> <span>{</span><br>    <span>"react"</span><span>:</span> <span>"^18.2.0"</span><span>,</span><br>    <span>"react-dom"</span><span>:</span> <span>"^18.2.0"</span><br>  <span>}</span><span>,</span><br>  <span>"devDependencies"</span><span>:</span> <span>{</span><br>    <span>"@testing-library/jest-dom"</span><span>:</span> <span>"^6.4.2"</span><span>,</span><br>    <span>"@testing-library/react"</span><span>:</span> <span>"^14.2.1"</span><span>,</span><br>    <span>"@vitejs/plugin-react-swc"</span><span>:</span> <span>"^3.5.0"</span><span>,</span><br>    <span>"eslint"</span><span>:</span> <span>"^8.56.0"</span><span>,</span><br>    <span>"eslint-config-prettier"</span><span>:</span> <span>"^9.1.0"</span><span>,</span><br>    <span>"eslint-plugin-react"</span><span>:</span> <span>"^7.33.2"</span><span>,</span><br>    <span>"eslint-plugin-react-hooks"</span><span>:</span> <span>"^4.6.0"</span><span>,</span><br>    <span>"eslint-plugin-react-refresh"</span><span>:</span> <span>"^0.4.5"</span><span>,</span><br>    <span>"jsdom"</span><span>:</span> <span>"^24.0.0"</span><span>,</span><br>    <span>"prettier"</span><span>:</span> <span>"3.2.5"</span><span>,</span><br>    <span>"vite"</span><span>:</span> <span>"^5.1.0"</span><span>,</span><br>    <span>"vitest"</span><span>:</span> <span>"^1.2.2"</span><br>  <span>}</span><br><span>}</span></span>
```

Run `npm test` to check if everything works as expected.

Now you can use this project as a boilerplate for your next React application.

That’s it, folks! Happy coding!