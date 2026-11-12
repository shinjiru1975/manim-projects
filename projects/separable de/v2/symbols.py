"""
Factory for the glyphs you re-type at the top of every scene.

WHY A FUNCTION/CLASS AND NOT MODULE-LEVEL VARIABLES?
Reactive Manim glyphs are objects that get moved/tracked while a scene runs.
If they were created once at import time, scene 2 would inherit scene 1's
leftovers. So: call Symbols() INSIDE construct(), once per scene.
"""
from manim import *
from common import *
from reactive_manim import *   # keep LAST: its MathTex must win


class Symbols:
    def __init__(self, colored=False):
        """
        colored=False : x, y stay white (you reveal the colour later with
                        x.animate.set_color(...)).  dx / dy are always coloured.
        colored=True  : x, y, dx, dy are coloured from the start.
        """
        # one MathTex call, then unpack -- exactly like your old first line
        (self.x, self.y1, self.y2, self.yp, self.wan, self.tu, self.z,
         self.p, self.mn, self.eq, self.dy, self.dx, self.sp,
         self.C, self.integ) = MathTex(
            "x", "y", "y", "y'", "1", "2", "0",
            "+", "-", "=", "dy", "dx", r"\ ",
            "C", r"\int",
        )
        self.dy.set_color(Y_COLOR)
        self.dx.set_color(X_COLOR)
        if colored:
            self.x.set_color(X_COLOR)
            self.y1.set_color(Y_COLOR)
            self.y2.set_color(Y_COLOR)
            self.yp.set_color(Y_COLOR)

    def unpack(self, names):
        """
        Pull out only the glyphs you want, in the order you want, by name:

            x, y1, eq, sp = S.unpack("x y1 eq sp")

        (Order can't go wrong the way a 12-name tuple can.)
        Available: x y1 y2 yp wan tu z p mn eq dy dx sp C integ
        NOTE: `mn` = minus.  Avoid naming a variable `min` or `int`:
        that shadows Python's built-ins.
        """
        return tuple(getattr(self, n) for n in names.split())


def make_condition_parts():
    """
    The initial condition  x = 1, y = 0 ;  as 8 separate glyphs:
        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi
    Pieces are separate because you animate them individually later
    (e.g. wan_con flies into the answer).
    """
    x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex(
        "x", "=", "1", ",", "y", "=", "0", ";"
    )
    x_con.set_color(X_COLOR)
    y_con.set_color(Y_COLOR)
    return x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi
