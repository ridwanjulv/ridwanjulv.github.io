[

![David Jöch](https://miro.medium.com/v2/resize:fill:88:88/1*whVzSv-tY6v-8fBlwDYvug.jpeg)



](https://djoech.medium.com/?source=post_page-----231e3fbd7108--------------------------------)

In this article I want to show you the differences between functional and class components in React and when you should choose which one.

But first let me give you a brief introduction to React components from the [documentation](https://reactjs.org/docs/components-and-props.html):

The simplest way to define a component in React is to write a JavaScript function:

```
<span id="dc3f" data-selectable-paragraph="">function Welcome(props) {<br>  return &lt;h1&gt;Hello, {props.name}&lt;/h1&gt;;<br>}</span>
```

It’s just a function which accepts props and returns a React element.  
But you can also use the ES6 class syntax to write components.

```
<span id="466c" data-selectable-paragraph="">class Welcome extends React.Component {<br>  render() {<br>    return &lt;h1&gt;Hello, {this.props.name}&lt;/h1&gt;;<br>  }<br>}</span>
```

Both versions are equivalent and will give you the exact same output.  
Now you might ask yourself: _“When should I use a function and when a class?”_

## Differences between functional and class-Components

## Syntax

The most obvious one difference is the syntax. A functional component is just a plain JavaScript function which accepts props as an argument and returns a React element.

A class component requires you to extend from React.Component and create a render function which returns a React element. This requires more code but will also give you some benefits which you will see later on.

If you take a look at the transpiled code by Babel you will also see some major differences:

![](https://miro.medium.com/v2/resize:fit:700/1*pKQRqwhe_XLY9aLpbzioLg.png)

As functional component transpiled by Babel

![](https://miro.medium.com/v2/resize:fit:700/1*HCUtuON8qsHAyWusOsR64A.png)

The exact same component written as class component transpiled with Babel

## State

> Edit (29.03.2019): This changed with the **React 16.8 Hooks** update!  
> You can now use the [useState](https://reactjs.org/docs/hooks-state.html) hook to use state in your functional components.

Because a functional component is just a plain JavaScript function, you cannot use setState() in your component. That’s the reason why they also get called functional stateless components. So everytime you see a functional component you can be sure that this particular component doesn’t have its own state.

If you need a state in your component you will either need to create a class component or you lift the state up to the parent component and pass it down the functional component via props.

## Lifecycle Hooks

> Edit (29.03.2019): This changed with the **React 16.8 Hooks** update!  
> You can now use the [useEffect](https://reactjs.org/docs/hooks-effect.html) hook to use lifecycle events in your functional components.

Another feature which you cannot use in functional components are lifecycle hooks. The reason is the same like for state, all lifecycle hooks are coming from the React.Component which you extend from in class components.

So if you need lifecycle hooks you should probably use a class component.

## So why should I use functional components at all?

You might ask yourself why you should use functional components at all, if they remove so many nice features. But there are some benefits you get by using functional components in React:

1.  Functional component are much **easier to read and test** because they are plain JavaScript functions without state or lifecycle-hooks
2.  You end up with **less code**
3.  They help you to use **best practices**. It will get easier to separate container and presentational components because you need to think more about your component’s state if you don’t have access to setState() in your component
4.  The React team [mentioned](https://reactjs.org/blog/2015/10/07/react-v0.14.html#stateless-functional-components) that there may be a **performance** boost for functional component in future React versions

## Conclusion

And so to answer our question before, you should use functional components if you are writing a presentational component which doesn’t have its own state or needs to access a lifecycle hook. Otherwise you can stick to class components or take a look into the library [recompose](https://github.com/acdlite/recompose) which allows you to write functional components and enhance them with a state or lifecycle hooks with [HOCs](https://reactjs.org/docs/higher-order-components.html)!