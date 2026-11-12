# Common Folder
This folder contains the helpers I use for groups of animations I use in my projects. These helpers makes the code more concise by condensing multiple groups of animations or succeeding animations to just one or fewer than originally needed.

## Example Helpers
What used to be
```python
self.play(TransformInStages.from_copy(c2, d, **rt))
```
is now only
```python
self.derive(c2, d)
```

More prominently, what used to be
```python
wan_con_ph = phantom(wan_con)
x_sub = Term(wan_con_ph, tu, paren=True)

h = MathTex(x_sub, g[0][1:7]).move_to(ans_copy)

wan_con_target = x_sub.term.get_center().copy()   
wan_con_copy = wan_con.copy()

self.play(
    TransformInStages.replacement_transform(ans_copy, h, **rt),
    wan_con_copy.animate.move_to(wan_con_target).set_color(BLUE),
    **rt
)

self.remove(h)
self.remove(wan_con_copy)
x_sub = Term(wan_con_copy, tu, paren=True)
h1 = MathTex(x_sub, g[0][1:7]).move_to(h)
self.add(h1)
```
is now only
```python
i, i_parts = self.substitute(
    h,
    lambda f: [
        h_parts[0], eq, Parentheses(f[0]), mn,
        Function(ln1.function, [Parentheses(f[1]), p, wan], paren=ln1.paren),
        g[0][5:7]
    ],
    [z_con, z_con], color=Y_COLOR
)
```

These helpers were created by Claude after I asked it to look for animations groups and sequences I use the most. Claude created these helpers with `def` to define function.

At the beginning of every project, add
```python
from manim import *
from common import *
```
and `common` should be imported regardless wherever the `.py` project file is. This is possible after modifying of `pyproject.toml` and `uv`, where the folder now has its own place in `.venv`.

More specific usage instructions are written in the individual files.

As a beginner, I can kinda understand how the helpers work by reading the code, but I am not yet at the level where I can create such on my own.