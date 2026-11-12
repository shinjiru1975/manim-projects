"""
Small PURE helpers: they take mobjects, return a mobject, never touch the scene.
(Anything that needs `self.play` lives in scene_base.py instead.)
"""
from manim import *
from .style import *
from reactive_manim import *   # keep LAST: its MathTex must win


def phantom(term):
    """Invisible stand-in for `term`. Reserves its space inside an equation so
    you can build the NEXT equation's layout, then fly the real thing in."""
    return term.clone().clear_tracking().set_opacity(0)

# def cancel_slash(mob, color=CANCEL_COLOR):
#     """Red diagonal slash through `mob`  (replaces the 4-line Line(...) block)."""
#     return Line(mob.get_corner(DL), mob.get_corner(UR), color=color)

def _flatten(items):
    for it in items:
        if isinstance(it, (list, tuple)):
            yield from _flatten(it)
        else:
            yield it

def cancel_slash(*mobs, color=CANCEL_COLOR, buff=0.05, **line_kwargs):
    """Slash through one mobject, several, or a list/slice of them (treated as one block)."""
    target = Group(*_flatten(mobs))
    ll = target.get_corner(DL) + buff * DL
    ur = target.get_corner(UR) + buff * UR
    return Line(ll, ur, color=color, **line_kwargs)

def cancel_slash_multiple(terms_group, color=RED, stroke_width=2):
    """Returns a VGroup of diagonal lines crossing out a group of terms."""
    lines = VGroup()
    for term in terms_group:
        slash1 = Line(term.get_corner(DL), term.get_corner(UR), color=color, stroke_width=stroke_width)
        slash2 = Line(term.get_corner(UL), term.get_corner(DR), color=color, stroke_width=stroke_width)
        lines.add(VGroup(slash1, slash2))
    return lines



def answer_box(ans, color=ANSWER_COLOR, buff=0.2):
    """Pink box around a final answer."""
    return SurroundingRectangle(ans, color=color, buff=buff).move_to(ans)


def pin_top(mob, shift=TOP_SHIFT):
    """Put an equation at the top of the frame, slightly below the edge."""
    return mob.to_edge(UP).shift(shift)


def word_label(text, under, buff=0.4, scale=0.7):
    """Small italic-ish caption such as 'general solution' under `under`."""
    return Text(text, font=LABEL_FONT).next_to(under, DOWN, buff=buff).scale(scale)
