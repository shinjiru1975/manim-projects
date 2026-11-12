from manim import *
from reactive_manim import *

# from `parentheses-test (scene2).py`
class Testing4(Scene):
    def construct(self):

        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)

        sp = MathTex(r"\ ")

        r_paren = Parentheses([wan, p, Term(y2, tu)])

        d = MathTex(x, y1, sp, dy, eq, r_paren, sp, dx).to_edge(UP).shift(DOWN * 0.4)  # cinema din to, hindi na magagalaw yung y

        # ---------  Anim5  --------- 
        # nadiskubre na rin sa wakas kung paano i-keep yung parentheses, d.paren lang pala, or generally paren=[function].paren,
        # where [function] ay yung huling defined na function na pagkukunan ng parentheses ng current function

        self.add(d)

        chakalimination = Text("CHAKALIMINATION™").set_color(LIGHT_PINK).next_to(d, DOWN, buff=0.8)
        box = SurroundingRectangle(chakalimination, color=YELLOW, buff=0.3)

        self.play(Write(chakalimination[0:15], run_time=1.5))
        self.play(Write(chakalimination[15], run_time=0.7))
        self.play(Write(box), run_time=1.5)

        chaka = Text("chaka", font="LMRoman10", slant=ITALIC).shift(LEFT * 3).scale(0.7)
        self.play(TransformFromCopy(chakalimination[0:5], chaka), run_time=1.7)
        
        chaka_par = Paragraph(
            "any term/variable",
            "that does not belong",
            "to its group",
            alignment="center",
            font="LMRoman10",
            line_spacing=0.6
        ).next_to(chaka, DOWN * 0.01).scale(0.6)
        self.play(DrawBorderThenFill(chaka_par), run_time=2)

        elimination = Text("elimination", font="LMRoman10", slant=ITALIC).shift(RIGHT * 3).scale(0.7)
        self.play(TransformFromCopy(chakalimination[6:15], elimination), run_time=1.7)

        elimination_par = Paragraph(
            "to eliminate",
            "that term/variable",
            "via division",
            alignment="center",
            font="LMRoman10",
            line_spacing=0.6
        ).next_to(elimination, DOWN * 0.01).scale(0.6)
        self.play(DrawBorderThenFill(elimination_par), run_time=2)

        self.play(
            AnimationGroup(
                FadeOut(VGroup(chaka, chaka_par, elimination, elimination_par)),
                VGroup(chakalimination, box).animate.to_edge(DOWN).shift(UP * 0.2).scale(0.7),
                run_time=1.5
            )
        )

        self.play(
            
                y1.animate.set_color(YELLOW),
                y2.animate.set_color(YELLOW),
                x.animate.set_color(BLUE),
                run_time=1.5
            
        )

        # ---------  Anim6.1  --------- 
        l_frac1 = Fraction([x, y1], x)
        r_paren = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)
        
        e_1 = MathTex(l_frac1, sp, dy, eq, r_paren, sp, dx).next_to(d, DOWN, buff=0.9); eq.save_y(), 
        d_copy = d.copy().move_to(e_1)

        # self.add(d)
        
        self.play(
            TransformFromCopy(d, d_copy, run_time=1.5)
        )

        # tangina palo
        self.play(TransformInStages.replacement_transform(d_copy, e_1, run_time=1.5)) 

        # ---------  Anim6.2  --------- 
        r_frac1 = Fraction(r_paren, x)
        e_2 = MathTex([l_frac1], sp, dy, eq, r_frac1, sp, dx).move_to(e_1); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_1, e_2, run_time=1.5))
        
        # ---------  Anim6.3  --------- 
        r_frac2 = Fraction(r_paren, [x, r_paren], vinculum=r_frac1.vinculum)
        e_3 = MathTex(l_frac1, sp, dy, eq, r_frac2, sp, dx).move_to(e_2); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_2, e_3, run_time=1.5))

        # ---------  Anim6.4  --------- 
        l_frac2 = Fraction(l_frac1.numerator, [l_frac1.denominator, r_paren], vinculum=l_frac1.vinculum)
        e_4 = MathTex(l_frac2, sp, dy, eq, [r_frac2], sp, dx).move_to(e_3); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_3, e_4, run_time=1.5))
        # tangina cinema talaga

        # ---------  Anim7  --------- 
        l_cancel2_num = Line(
            e_4[0].numerator[0].get_corner(DL), 
            e_4[0].numerator[0].get_corner(UR), 
            color=RED
        )
        l_cancel2_den = Line(
            e_4[0].denominator[0].get_corner(DL), 
            e_4[0].denominator[0].get_corner(UR), 
            color=RED
        )
        r_cancel2_num = Line(
            e_4[4][0].numerator.get_corner(DL), 
            e_4[4][0].numerator.get_corner(UR), 
            color=RED
        )
        r_cancel2_den = Line(
            e_4[4][0].denominator[1].get_corner(DL), 
            e_4[4][0].denominator[1].get_corner(UR), 
            color=RED
        )

        self.play(
            Create(l_cancel2_num),
            Create(l_cancel2_den),
            run_time=1.5
        )
 
        self.play(
            Create(r_cancel2_num),
            Create(r_cancel2_den),
            run_time=1.5
        )

        # ---------  Anim8  --------- 
        l_frac3 = Fraction([l_frac2.numerator[1], sp, dy], l_frac2.denominator[1], vinculum=l_frac2.vinculum)
        r_frac3 = Fraction(dx, r_frac2.denominator[0], vinculum=r_frac2.vinculum)
        
        g = MathTex(l_frac3, eq, r_frac3).next_to(e_4, DOWN, buff=0.7)
        e_4_copy = e_4.copy().move_to(g)

        self.play(
            TransformInStages.from_copy(e_4, g, run_time=1.8),
            FadeOut(chakalimination),
            FadeOut(box),
            run_time=1.8
        )

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        l_int1 = MathTex(integ, l_frac3)
        r_int1 = MathTex(integ, r_frac3)
        
        h = MathTex(l_int1, eq, r_int1).move_to(g)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g, [h[0][1], h[2][1]], run_time=1.5),
                AnimationGroup(
                    Write(l_int1[0]),
                    Write(r_int1[0]),
                    run_time=1.5,
                ),
                lag_ratio=0.5
            )
        )

        # group = VGroup(h[0][1], h[2][1], l_int1[0], r_int1[0]).move_to(g)

        self.add(h)

        # ---------  Anim10  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)

        ans = MathTex(Term(y1, tu), eq, "C", Term(x, tu), "-", wan)
        arrow = MathTex(sp, r"\rightarrow", sp)
        ans_phantom = create_phantom(ans)
        arrow_phantom = create_phantom(arrow)

        i = MathTex([l_int1, eq, r_int1], arrow_phantom, ans_phantom).move_to(h)

        # self.play(Write(i))

        ans.move_to(ans_phantom)
        arrow.move_to(arrow_phantom)
        box = SurroundingRectangle(ans, color=LIGHT_PINK, buff=0.2).move_to(ans_phantom)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(h, i, run_time=1.5),
                Write(arrow, run_time=1.5),
                Write(ans, run_time=1.5),
                Write(box, run_time=1.5),
                lag_ratio=0.5
            )
        )

        gensol = Text("general solution", font="LMRoman10").next_to(ans, DOWN, buff=0.4).scale(0.7)
        self.play(DrawBorderThenFill(gensol), run_time=1.5)

        # self.play(TransformInStages.replacement_transform(h, i, run_time=1.5))
        # self.play(Write(ans), run_time=1.5)

        self.wait()

        # # ---------  Anim10 (reyal)  --------- 
        # ans = MathTex(Term(y1, tu), eq, "C", Term(x, tu), "-", wan).next_to(h, DOWN, buff=0.8)
        # box = SurroundingRectangle(ans, color=LIGHT_PINK, buff=0.3)

        # self.play(
        #     LaggedStart(
        #         Write(ans, run_time=1.5),
        #         Write(box, run_time=1.5),
        #         lag_ratio=0.5
        #     )
        # )
        
        # self.wait()