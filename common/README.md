# Common Folder
This folder contains the helpers I use for groups of animations I use in my projects. These helpers makes the code more concise by condensing multiple groups of animations or succeeding animations to just one or fewer than originally needed.

These helpers were created by Claude after I asked it to look for animations groups and sequences I use the most. Claude created these helpers with `def` to define function.

At the beginning of every project, add
```python
from manim import *
from common import *
```
and `common` should be imported regardless wherever the `.py` project file is. This is possible after modifying of `pyproject.toml` and `uv`, where the folder now has its own place in `.venv`.

As a beginner, I can kinda understand how the helpers work by reading the code, but I am not yet at the level where I can create such on my own.