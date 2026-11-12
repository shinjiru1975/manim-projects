"""
Example 1, Scene 1:  x y' = 1 + y^2   ->   x dy = (1 + y^2) dx
(was e1-s1.py / class Separable13)

STYLE: "method per animation" (3b1b style).
    construct() reads like a table of contents.
    Each AnimX is its own method.
    Things later steps need are stored on `self` (self.a, self.b, ...).

Run from the project root:
    python -m manim -pql example1/scene1.py Example1Scene1
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))  # project root, so `common` is found
from manim import *
from common import *
from reactive_manim import *   # last, so its MathTex wins (and so VS Code can see these names)


class Example1Scene1(DEScene):
    def construct(self):
        self.s = Symbols()           # fresh glyphs for this scene

        self.anim_a()    # write the equation
        self.anim_b()    # y' -> dy/dx
        self.anim_c()    # multiply both sides by dx, cancel
        self.anim_d()    # x dy = (1 + y^2) dx
        self.to_top()    # clear and park d at the top

        self.wait()

    # ---------  AnimA  ---------
    def anim_a(self):
        s = self.s
        self.a = MathTex(
            s.x, s.y1, s.yp, s.eq, [s.wan, s.p, Term(s.y2, s.tu)]
        ).to_edge(UP)
        self.play(Write(self.a), run_time=1.5)

    # ---------  AnimB  ---------
    def anim_b(self):
        s, a = self.s, self.a
        dydx = Fraction(s.dy, s.dx)

        b = MathTex(
            s.x, s.y1, s.sp, dydx, s.eq, [s.wan, s.p, Term(s.y2, s.tu)]
        ).next_to(a, DOWN, buff=0.5)
        a_copy = a.copy().move_to(b)

        self.play(TransformFromCopy(a, a_copy), **RT)
        self.play(Indicate(a_copy[2], color=YELLOW, scale_factor=1.5, run_time=1.5))
        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(
                    a_copy, [b[0:2], b[4:5]], run_time=1.5
                ),
                Write(dydx),
                lag_ratio=0.6,
            )
        )
        self.b, self.dydx = b, dydx

    # ---------  AnimC  ---------
    def anim_c(self):
        s, b, dydx = self.s, self.b, self.dydx

        c = MathTex(
            Parentheses(s.dx), s.sp, s.x, s.y1, s.sp, dydx, s.eq,
            [s.wan, s.p, Term(s.y2, s.tu)], s.sp, Parentheses(s.dx)
        ).next_to(b, DOWN, buff=0.5)
        b_copy = b.copy().move_to(c)

        self.play(TransformFromCopy(b, b_copy), **RT)
        self.play(Write(c[0]), Write(c[9]), **RT)

        # the two red slashes (was 2 x Line(get_corner(DL), get_corner(UR)))
        self.play(
            Write(cancel_slash(c[0])),
            Write(cancel_slash(c[5].denominator)),
            **RT,
        )
        self.c = c

    # ---------  AnimD  ---------
    def anim_d(self):
        s, c = self.s, self.c
        self.d = MathTex(
            s.x, s.y1, s.sp, s.dy, s.eq,
            Parentheses([s.wan, s.p, Term(s.y2, s.tu)]), s.sp, s.dx
        ).next_to(c, DOWN, buff=0.5)
        self.derive(c, self.d, run_time=2)

    # ---------  after the differentials  ---------
    def to_top(self):
        d = self.d
        # Kept exactly as in your original: d is in self.mobjects, so it fades
        # while moving, then self.add(d) pops it back. If you wanted d to stay
        # visible, use:  self.clear_except(d)  then  self.play(d.animate.to_edge(UP)...)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            d.animate.to_edge(UP).shift(DOWN * 0.4),
            run_time=1.5,
        )
        self.add(d)
