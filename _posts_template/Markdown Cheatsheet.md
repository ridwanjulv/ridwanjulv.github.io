
# Extension used
- https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
- https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid
- https://marketplace.visualstudio.com/items?itemName=bierner.markdown-emoji

> Note: use ctrl-K + V to Toggle preview to side


# Standard Formatting

```
# Header1
## Header2
### Header3
```

**Bold**
*Italic*
~~Strikethrough~~

linebreak:
<hr />

List
- item
- item

Ordered List
1. item
2. item

Highlight
> test
>> Sub highlight  
>> test double-space at the end for  
>> newline
>>> Sub Sub highlight


# Link
![imagelink](Images/avatar.jpg)<br />
[ReferenceLink](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
> note: highlight then past the link to quickly create reference link

[ReferenceToFooter][link-id]

[link-id]: https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one

Tasks
- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
- [ ] (Optional) Open a followup issue

```
this is a code block
```

this is a `code snippet` syntax

# Table of Contents

Run command "Create Table of Contents" (in the VS Code Command Palette) to insert a new table of contents.
```
# Section 1

# Section 1.1 <!-- Omit in toc -->

```

# Table
Auto format table using Alt-Shift-F
```
|left|center|right
:---|:---:|---:
1|2|3
45|67|89
```

| left | center | right |
| :--- | :----: | ----: |
| 1    |   2    |     3 |
| 45   |   67   |    89 |

# Math Syntax
$$
f(x) = \int_{-\infty}^{\infty}
        \hat f(\xi)\,e^{2 \pi i \xi x}
        \,d\xi
$$


