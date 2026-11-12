"""
DEScene = your scene class with the animation patterns you repeat as methods.
Your scenes inherit it:   class MyScene(DEScene):
Every method here is a thing you previously typed out by hand 4-30 times.

All methods accept run_time=... etc.; the default is RT (1.5s) from style.py.
"""
from manim import *
from .style import *
from reactive_manim import *   # keep LAST: its MathTex must win
from .helpers import *


class DEScene(Scene):

    # ---- the three transforms you use constantly -------------------------
    def morph(self, old, new, **kw):
        """Rewrite `old` into `new` in place (replacement_transform).
        Build `new` with .move_to(old) first.  Returns `new`."""
        self.play(TransformInStages.replacement_transform(old, new, **{**RT, **kw}))
        return new

    def derive(self, src, new, **kw):
        """Keep `src` on screen, grow `new` out of a copy of it (from_copy).
        Build `new` with .next_to(src, DOWN, ...) first.  Returns `new`."""
        self.play(TransformInStages.from_copy(src, new, **{**RT, **kw}))
        return new

    def copy_down(self, old, new, shift=ORIGIN, **kw):
        """The 'copy the line down, then rewrite the copy' pattern:
             TransformFromCopy(old -> copy at new's spot), then
             replacement_transform(copy -> new).
        Build `new` with .next_to(old, DOWN, ...) first.  Returns `new`.
        `shift` nudges the copy (your old `.shift(RIGHT * 1.75)`)."""
        kw = {**RT, **kw}
        old_copy = old.copy().move_to(new).shift(shift)
        self.play(TransformFromCopy(old, old_copy, **kw))
        self.play(TransformInStages.replacement_transform(old_copy, new, **kw))
        return new

    # ---- the 'arrow -> boxed answer' ending ------------------------------
    def reveal_answer(self, old, kept, ans, sp, **kw):
        """
        old  : equation on screen          (e.g. the integrated line `e`)
        kept : the SAME pieces as a list   (e.g. [l_int, eq, r_int])
        ans  : the answer MathTex (not placed yet)
        sp   : your spacer glyph
        Slides `old` left, writes  ->  ans  and a pink box.
        Returns (new_equation, ans, box).
        """
        kw = {**RT, **kw}
        arrow = MathTex(sp, r"\rightarrow", sp)
        ans_ph, arrow_ph = phantom(ans), phantom(arrow)

        new = MathTex(kept, arrow_ph, ans_ph).move_to(old)
        ans.move_to(ans_ph)
        arrow.move_to(arrow_ph)
        box = answer_box(ans)

        self.play(LaggedStart(
            TransformInStages.replacement_transform(old, new, **kw),
            Write(arrow, **kw),
            Write(ans, **kw),
            Write(box, **kw),
            lag_ratio=0.5,
        ))
        return new, ans, box

    def caption(self, text, under, scale=0.7, buff=0.4, **kw):
        """Write a word label (e.g. 'general solution') under a mobject."""
        label = word_label(text, under, buff=buff, scale=scale)
        self.play(DrawBorderThenFill(label), **{**RT, **kw})
        return label

    # ---- housekeeping ------------------------------------------------------
    def clear_except(self, *keep, **kw):
        """Fade out everything on screen except the mobjects in `keep`."""
        fade = [m for m in self.mobjects if m not in keep]
        self.play(*[FadeOut(m) for m in fade], **{**RT, **kw})

    def dump(m, name="", depth=0, max_depth=3):
        pad = "  " * depth
        keys = sorted(vars(m).keys())
        track = {k: getattr(m, k) for k in keys
                if any(s in k.lower() for s in ("track", "id", "key", "tag"))}
        print(f"{pad}{name} <{type(m).__name__}> obj_id={id(m)} "
            f"center={m.get_center().round(3)} track={track}")
        if depth < max_depth:
            for i, sm in enumerate(m.submobjects):
                dump(sm, f"[{i}]", depth + 1, max_depth)

    # ---- your own `substitute` idea, promoted to a real method ------------
    def substitute(self, old, build, sources, color=None, **kw):
        """
        Fly copies of `sources` into slots of a new equation.
        old     : solid equation currently on screen
        build   : fn(slot_contents) -> equation; MUST build fresh pieces each call
        sources : mobjects whose values fly in (repeat one for several slots)
        Returns the new solid equation -- always continue from the return value.

        (In your Scene2Attempt3 this was defined INSIDE construct() but called as
        self.substitute(...), which would raise AttributeError. As a method on
        the base class it now works the way you called it.)
        """
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

        print("OLD first-term parts:", [getattr(a, "original_id", None) for a in old[0].submobjects])
        print("NEW first-term parts:", [id(b) for b in new_ph[0].submobjects])
        
        self.play(
            TransformInStages.replacement_transform(old, new_ph, **kw),
            *moves,
            **kw
        )

        self.remove(new_ph, *fliers)

        parts = build(fliers)                       # the real pieces, kept for the next stage
        solid = MathTex(*parts).move_to(center)
        self.add(solid)
        return solid, parts