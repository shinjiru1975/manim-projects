# Version 2
Version 2 is the improved version of `original` of this project. It is more organized and structured, based heavily on the code I already made in `original`.

This version heavily utilized animation helpers that Claude AI helped me create in the `common` folder at the root of the project. Helpers are groups of terms and/or animations that combine to form a single method. Instead of writing multiple `self.play` functions to convey an animation idea, you only write one function or fewer than what was originally needed. 

Among these helpers are:
- `self.morph`,
- `self.derive`,
- `self.copy_down`,
- `self.substitute`,
- etc.

## Examples
What used to be
```python
# from original/e2-s1.py
self.play(TransformInStages.from_copy(c2, d, **rt))
```
is now only
```python
# from v2/example2/scene2.py
self.derive(c2, d)
```

More prominently, what used to be
```python
# from original/e2-s2.py

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
# from v2/example2/scene2.py

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

`WORKFLOW.md` was the instructions file that came with the helpers Claude generated, but I don't really read or follow it that much.

It was also during this time that I finally created a GitHub repository to track all changes to this project.

