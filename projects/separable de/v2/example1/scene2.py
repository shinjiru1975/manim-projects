from manim import *
from common import *
from symbols import *
from reactive_manim import *   

class Example1Scene2(DEScene):
    def construct(self):

        S = Symbols()
        x, y1, yp, eq, wan, p, y2, tu, dy, dx, sp, integ = S.unpack(
            "x y1 yp eq wan p y2 tu dy dx sp integ"
        )

        r_paren = Parentheses([wan, p, Term(y2, tu)])

        d = pin_top(
            MathTex(
                x, y1, sp, dy, 
                eq, 
                r_paren, sp, dx
            )
        )   

        self.add(d)

        # ---------  AnimE0: CHAKALIMINATION  ---------
        chakalimination = Text("CHAKALIMINATION™").set_color(LIGHT_PINK).next_to(d, DOWN, buff=0.8)
        box = SurroundingRectangle(chakalimination, color=YELLOW, buff=0.3)

        self.play(Write(chakalimination[0:15], run_time=1.5))
        self.play(Write(chakalimination[15], run_time=0.7))
        self.play(Write(box), run_time=1.5)

        chaka = Text("chaka", font=LABEL_FONT, slant=ITALIC).shift(LEFT * 3).scale(0.7)
        self.play(TransformFromCopy(chakalimination[0:5], chaka), run_time=1.7)

        chaka_par = Paragraph(
            "any term/variable", 
            "that does not belong", 
            "to its group",
            alignment="center", font=LABEL_FONT, line_spacing=0.6
        ).next_to(chaka, DOWN * 0.01).scale(0.6)

        self.play(DrawBorderThenFill(chaka_par), run_time=2)

        elimination = Text("elimination", font=LABEL_FONT, slant=ITALIC).shift(RIGHT * 3).scale(0.7)
        self.play(TransformFromCopy(chakalimination[6:15], elimination), run_time=1.7)

        elimination_par = Paragraph(
            "to eliminate", 
            "that term/variable", 
            "via division",
            alignment="center", font=LABEL_FONT, line_spacing=0.6
        ).next_to(elimination, DOWN * 0.01).scale(0.6)

        self.play(DrawBorderThenFill(elimination_par), run_time=2)

        self.play(
            AnimationGroup(
                FadeOut(VGroup(chaka, chaka_par, elimination, elimination_par)),
                VGroup(chakalimination, box).animate.to_edge(DOWN).shift(UP * 0.2).scale(0.7),
                run_time=1.5,
            )
        )

        self.play(
            y1.animate.set_color(Y_COLOR),
            y2.animate.set_color(Y_COLOR),
            x.animate.set_color(X_COLOR),
            **RT,
        )

        # ---------  AnimE1: copy down, divide left by x  ---------
        l_frac1 = Fraction([x, y1], x)
        r_paren = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)

        e_1 = MathTex(
            l_frac1, sp, dy, 
            eq, 
            r_paren, sp, dx
        ).next_to(d, DOWN, buff=0.9); eq.save_y()

        self.copy_down(d, e_1)

        # ---------  AnimE2: divide right by x  ---------
        r_frac1 = Fraction(r_paren, x)

        e_2 = MathTex(
            [l_frac1], sp, dy, 
            eq, 
            r_frac1, sp, dx
        ).move_to(e_1); eq.restore_y()

        self.morph(e_1, e_2)

        # ---------  AnimE3: divide right by (1 + y^2)  ---------
        r_frac2 = Fraction(r_paren, [x, r_paren], vinculum=r_frac1.vinculum)

        e_3 = MathTex(
            l_frac1, sp, dy, 
            eq, 
            r_frac2, sp, dx
        ).move_to(e_2); eq.restore_y()

        self.morph(e_2, e_3)

        # ---------  AnimE4: divide left by (1 + y^2)  ---------
        l_frac2 = Fraction(l_frac1.numerator, [l_frac1.denominator, r_paren], vinculum=l_frac1.vinculum)

        e_4 = MathTex(
            l_frac2, sp, dy, 
            eq, 
            [r_frac2], sp, dx).move_to(e_3); eq.restore_y()
        
        self.morph(e_3, e_4)

        # ---------  AnimE5: cancellation  ---------
        self.play(
            Create(cancel_slash(e_4[0].numerator[0])),
            Create(cancel_slash(e_4[0].denominator[0])),
            **RT,
        )
        self.play(
            Create(cancel_slash(e_4[4][0].numerator)),
            Create(cancel_slash(e_4[4][0].denominator[1])),
            **RT,
        )

        # ---------  AnimG: copy down what was left  ---------
        l_frac3 = Fraction([l_frac2.numerator[1], sp, dy], l_frac2.denominator[1], vinculum=l_frac2.vinculum)
        r_frac3 = Fraction(dx, r_frac2.denominator[0], vinculum=r_frac2.vinculum)

        g = MathTex(
            l_frac3, 
            eq, 
            r_frac3
        ).next_to(e_4, DOWN, buff=0.7)

        self.play(
            TransformInStages.from_copy(e_4, g, run_time=1.8),
            FadeOut(chakalimination),
            FadeOut(box),
            run_time=1.8,
        )

        # ---------  AnimH1: integrate both sides  ---------
        l_int1 = MathTex(integ, l_frac3)
        r_int1 = MathTex(integ, r_frac3)
        
        h = MathTex(
            l_int1, 
            eq, 
            r_int1
        ).move_to(g)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g, [h[0][1], h[2][1]], run_time=1.5),
                AnimationGroup(Write(l_int1[0]), Write(r_int1[0]), run_time=1.5),
                lag_ratio=0.5,
            )
        )

        self.add(h)

        # ---------  AnimH2: -> general solution (boxed)  ---------
        ans = MathTex(
            Term(y1, tu), 
            eq, 
            "C", Term(x, tu), "-", wan
        )

        i, ans, box = self.reveal_answer(h, [l_int1, eq, r_int1], ans, sp)

        self.caption("general solution", ans, scale=0.7)

        self.clear_all()

        self.wait()