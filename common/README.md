# Common Folder
This folder contains the helpers I use for groups of animations I use in my projects. These helpers makes the code more concise by condensing multiple groups of animations or succeeding animations to just one or fewer than originally needed.

## Example Helpers
What used to be
```python
# from projects/separable de/original/e2-s1.py

self.play(TransformInStages.from_copy(c2, d, **rt))
```
is now only
```python
# from projects/separable de/v2/example2/scene1.py

self.derive(c2, d)
```
because of
```python
# from common/scene_base.py

def derive(self, src, new, **kw):
    self.play(TransformInStages.from_copy(src, new, **{**RT, **kw}))
    return new
```

More prominently, what used to be
```python
# from projects/separable de/original/e2-s2.py

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
# from projects/separable de/v2/example2/scene2.py

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
because of
```python
# from common/scene_base.py

def substitute(self, old, build, sources, color=None, **kw):
    kw = {**RT, **kw}
    center  = old.get_center().copy()
    ghosts  = [phantom(s) for s in sources]
    new_ph  = MathTex(*build(ghosts)).move_to(center)
    targets = [g.get_center().copy() for g in ghosts]
    fliers  = [s.copy() for s in sources]

    moves = [
        f.animate.move_to(t).set_color(color) if color is not None
        else f.animate.move_to(t)
        for f, t in zip(fliers, targets)
    ]
    
    self.play(
        TransformInStages.replacement_transform(old, new_ph, **kw),
        *moves,
        **kw
    )

    self.remove(new_ph, *fliers)

    parts = build(fliers)                      
    solid = MathTex(*parts).move_to(center)
    self.add(solid)
    return solid, parts
```
doing all the heavy code-work.

These helpers were created by Claude after I asked it to look for animations groups and sequences I use the most. Claude created these helpers with `def` to define function.

At the beginning of every project, add
```python
from manim import *
from common import *
```
and `common` should be imported regardless wherever the `.py` project file is. This is possible after modifying of `pyproject.toml` and `uv`, where the folder now has its own place in `.venv`.

More specific usage instructions are written in the individual files.

As a beginner, I can kinda understand how the helpers work by reading the code, but I am not yet at the level where I can create such helpers on my own.