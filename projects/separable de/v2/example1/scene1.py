from manim import *
from common import *
from symbols import *
from reactive_manim import *   

class Example1Scene1(DEScene):
    def construct(self):

        x, y1, y2, yp, wan, tu, z, p, mn, eq, dy, dx, sp, C, integ = make_symbols()

        # ---------  AnimA: write the equation  ---------
        a = MathTex(
            x, y1, yp, 
            eq, 
            [wan, p, Term(y2, tu)]
        ).to_edge(UP)
                    
        self.play(Write(a), run_time=1.5)

        # ---------  AnimB: y' -> dy/dx  ---------
        dydx = Fraction(dy, dx)

        b = MathTex(
            x, y1, sp, dydx, 
            eq, 
            [wan, p, Term(y2, tu)]
        ).next_to(a, DOWN, buff=0.5)

        a_copy = a.copy().move_to(b)

        self.play(TransformFromCopy(a, a_copy), **RT)
        self.play(Indicate(a_copy[2], color=YELLOW, scale_factor=1.5, run_time=1.5))
        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(
                    a_copy, [b[0:2], b[4:5]], 
                    run_time=1.5
                ),
                Write(dydx),
                lag_ratio=0.6,
            )
        )

        # ---------  AnimC: multiply both sides by dx, tas cancel  ---------
        c = MathTex(
            Parentheses(dx), 
            sp, x, y1, sp, dydx, 
            eq,
            [wan, p, Term(y2, tu)], sp, 
            Parentheses(dx)
        ).next_to(b, DOWN, buff=0.5)

        b_copy = b.copy().move_to(c)

        self.play(TransformFromCopy(b, b_copy), **RT)
        self.play(Write(c[0]), Write(c[9]), **RT)

        self.play(
            Write(cancel_slash(c[0])),
            Write(cancel_slash(c[5].denominator)),
            **RT,
        )

        # ---------  AnimD: x dy = (1 + y^2) dx  ---------
        d = MathTex(
            x, y1, sp, dy, 
            eq,
            Parentheses([wan, p, Term(y2, tu)]), sp, dx
        ).next_to(c, DOWN, buff=0.5)

        self.derive(c, d, run_time=2)

        # clear everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            d.animate.to_edge(UP).shift(DOWN * 0.4),
            run_time=1.5,
        )
        self.add(d)

        self.wait()