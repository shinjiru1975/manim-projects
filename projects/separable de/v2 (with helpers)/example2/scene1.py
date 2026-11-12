"""
Example 2, Scene 1:  initial-value problem  2x(y+1) dx - y dy = 0,  x=1, y=0
(was e2-s1.py / class Scene1Attempt2)

STYLE: "flat" -- everything inside construct(), like before, but the repeated
blocks are now one-liners from common/.  Both styles are fine; use flat for
short scenes, methods when a scene passes ~60 lines.

Run from the project root:
    python -m manim -pql example2/scene1.py Example2Scene1
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))  # project root, so `common` is found
from manim import *
from common import *
from reactive_manim import *   # last, so its MathTex wins (and so VS Code can see these names)


class Example2Scene1(DEScene):
    def construct(self):
        S = Symbols()
        x, y1, y2, wan, tu, z, p, mn, eq, dy, dx, sp, integ = S.unpack(
            "x y1 y2 wan tu z p mn eq dy dx sp integ"
        )

        # ---------  AnimA1  ---------
        paren = Parentheses([y1, p, wan])
        a = pin_top(MathTex(tu, x, paren, sp, dx, mn, y2, sp, dy, eq, z))
        self.play(Write(a), **RT)

        # ---------  AnimA2  (add the initial condition)  ---------
        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = make_condition_parts()

        conditions = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)
        conditions_ph = phantom(conditions)

        a1 = MathTex(tu, x, paren, sp, dx, mn, y2, sp, dy, eq, z, conditions_ph).move_to(a)
        conditions.move_to(conditions_ph)

        self.play(LaggedStart(
            TransformInStages.replacement_transform(a, a1, **RT),
            Write(conditions, **RT),
            lag_ratio=0.6,
        ))
        self.play(
            x.animate.set_color(X_COLOR),
            y1.animate.set_color(Y_COLOR),
            y2.animate.set_color(Y_COLOR),
            **RT,
        )

        # ---------  AnimB  (copy down, rewrite)  ---------
        paren = Parentheses([y1, p, wan], paren=a1[2].paren)
        b = MathTex(tu, x, paren, sp, dx, eq, y2, sp, dy).next_to(a1, DOWN, buff=0.9)
        self.copy_down(a1, b, shift=RIGHT * 1.75)

        # ---------  AnimC1 / C2  (turn into fractions)  ---------
        l_frac = Fraction([tu, x, paren], paren)
        c1 = MathTex(l_frac, sp, dx, eq, y2, sp, dy).move_to(b)
        self.morph(b, c1)

        r_frac = Fraction(y2, paren)
        c2 = MathTex([l_frac], sp, dx, eq, r_frac, sp, dy).move_to(c1)
        self.morph(c1, c2)

        # ---------  AnimC3  (cancel)  ---------
        self.play(
            Create(cancel_slash(c2[0][0].numerator[2])),
            Create(cancel_slash(c2[0][0].denominator)),
            **RT,
        )

        # ---------  AnimD  ---------
        d = MathTex(tu, x, sp, dx, eq, r_frac, sp, dy).next_to(c2, DOWN, buff=0.75)
        eq.save_y()
        self.derive(c2, d)

        # ---------  AnimE  (integrate both sides)  ---------
        l_int = MathTex(integ, tu, x, sp, dx)
        r_int = MathTex(integ, r_frac, sp, dy)
        e = MathTex(l_int, eq, r_int).move_to(d)
        eq.restore_y()
        self.morph(d, e)

        # ---------  AnimF  (-> boxed general solution)  ---------
        ans = MathTex(Term(x, tu), eq, y2, mn, Function(r"\ln", [y2, p, wan]), p, "C")
        f, ans, box = self.reveal_answer(e, [l_int, eq, r_int], ans, sp)
        self.caption("general solution", ans, scale=0.8)

        # ---------  AnimG  (keep only answer + condition, send to top)  ---------
        g_ans_ph = phantom(ans)
        g_cond_ph = phantom(conditions)
        MathTex(g_ans_ph, g_cond_ph).move_to(a1)      # lays the two slots out

        keep = [ans, conditions, box]
        fade = [m for m in self.mobjects if m not in keep]
        self.play(
            ans.animate.move_to(g_ans_ph),
            box.animate.move_to(g_ans_ph).set_opacity(0),
            conditions.animate.move_to(g_cond_ph),
            *[FadeOut(m) for m in fade],
            **RT,
        )
        self.remove(box)
        self.wait()
