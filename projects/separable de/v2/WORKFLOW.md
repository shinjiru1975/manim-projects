# Workflow (v2)

## Folder layout
```
separable_de/
  WORKFLOW.md
  common/                 <- everything shared (your "3b1b shared_constructs")
    __init__.py           <- `from common import *` gives scenes everything
    style.py              <- colours, RT, layout constants      (constants only)
    symbols.py            <- Symbols(), make_condition_parts()  (glyph factories)
    helpers.py            <- phantom, cancel_slash, answer_box  (pure functions)
    scene_base.py         <- DEScene: morph, derive, copy_down, reveal_answer ...
  example1/
    scene1.py             <- one FILE per scene, one CLASS per finished scene
    scene2.py
  example2/
    scene1.py
    scene2.py
  _scratch/               <- throwaway experiments (not part of the final video)
```
Every scene file starts with the same 3-line header (a `sys.path` shim that points at the project root, then `from manim import *`, `from common import *`, `from reactive_manim import *`, in that order). Copy it from example1/scene1.py into each new scene file. The shim means it works no matter which folder you run `manim` from.

## Daily loop
1. Run it however your editor does (the header shim finds `common`), e.g.:
   `manim -pql example2/scene1.py Example2Scene1`
   (`-ql` = fast low quality while drafting; `-qh` only for final renders.
)
2. Working on a late animation? Don't re-render from the start:
   - `-n 6`  starts from animation #6 (earlier ones are skipped; the scene still
     builds the objects, so variables exist).
   - Put the earlier result on screen with `self.add(prev_equation)`, like you
     already did in your Scene2 files.
   - `-s` saves just the last frame as a PNG: fastest way to check layout.
3. Only render in high quality when the whole scene is approved.

## Rules for code
- **Animation names stay**: `AnimA`, `AnimB`, ... (+ `A1`, `A2` for sub-steps);
  major equations stay `a`, `b`, `c`. In method style they become
  `anim_a()`, `anim_b()` and `self.a`, `self.b`.
- **Attempts**: don't keep `Attempt1..4` classes with 90% identical bodies.
  Use git (`git init`, then `git commit -am "e2s1: substitution works"`).
  Old attempt = a commit you can go back to, not a copy in the file.
  Rename the class to the final name once you accept it.
- **Rule of three**: first time, write it inline. Second time, copy it and
  notice. Third time, make it a function:
  - needs `self.play` -> method on `DEScene` (scene_base.py)
  - no `self.play`, just builds/returns a mobject -> function in helpers.py
  - a constant (colour, run_time, shift) -> style.py
- **A helper earns its place** only if it replaces a repeated block AND you can
  name it in 1-3 words. If you can't name it, it isn't a pattern yet.
- Don't edit helpers while a scene is half-finished; finish the scene,
  re-render the old scenes at `-ql` to confirm nothing changed, then commit.

## Style choice per scene
- Short (< ~60 lines): flat, everything in `construct()` (see example2/scene1.py)
- Longer: one method per AnimX, shared things on `self` (see example1/scene1.py)

## Python gotchas seen in the old files
- `eq.save_y` without `()` does nothing; it must be `eq.save_y()`.
- A function defined inside `construct()` is NOT `self.something`.
  Define it on the class (as `DEScene.substitute` now is) to call it as a method.
- In common/ modules, import `reactive_manim` LAST (after `.style`), or manim's MathTex can shadow it.
- Don't name variables `min` / `int`: they hide Python's own functions.
