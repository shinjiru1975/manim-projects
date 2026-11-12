from manim import *
from reactive_manim import *

class Parenthesis(Scene):
    def construct(self):

        x, y1, eq, wan, p, y2, tu = MathTex("x", "y", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)

        sp = MathTex(r"\ ")

        paren_1 = Parentheses([ x, p, wan ])
        paren_2 = Parentheses([y1, p, wan], paren=paren_1.paren)
  
        e = MathTex(x, paren_1)
        f = MathTex(x, paren_2)

        self.play(Write(e), run_time=1.5)
        self.play(
            TransformInStages.replacement_transform(e, f, run_time=2), 
        )

class Testing(Scene):
    def construct(self):

        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)

        sp = MathTex(r"\ ")


        d = MathTex(x, y1, sp, dy, eq, Parentheses([wan, p, Term(y2, tu)]), sp, dx).to_edge(UP).shift(DOWN * 0.4); eq.save_y() # cinema din to, hindi na magagalaw yung y

        # ---------  Anim5  --------- 
        # nadiskubre na rin sa wakas kung paano i-keep yung parentheses, d.paren lang pala, or generally paren=[function].paren,
        # where [function] ay yung huling defined na function na pagkukunan ng parentheses ng current function

        self.add(d)

        l_frac = Fraction([x, y1], "x")
        l_frac_num = l_frac.numerator, l_frac.vinculum

        r_paren = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)

        e_1 = MathTex(l_frac, sp, dy, eq, r_paren, sp, dx).move_to(d); eq.restore_y()

        # tangina palo
        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(d, l_frac_num, run_time=1.5),
                Write(l_frac.denominator, run_time=1.5), 
                lag_ratio=0.5
            ) 
        )

        x2 = MathTex("x")

        r_frac1 = Fraction(r_paren, x2)
        r_frac1_num = r_frac1.numerator, r_frac1.vinculum

        e_2 = MathTex(l_frac, sp, dy, eq, r_frac1, sp, dx).move_to(e_1); eq.restore_y()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(e_1, r_frac1_num, run_time=1.5),
                Write(r_frac1.denominator, run_time=1.5), 
                lag_ratio=0.5
            )
        )   
    


        den_paren = Parentheses([wan, p, Term(y2, tu)])   # no paren=..., no reused objects
        r_paren2 = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)
        r_frac2 = Fraction(r_paren, [x2, r_paren])
        r_frac2_num = r_frac2.numerator, r_frac2.vinculum

        e_3 = MathTex(l_frac, sp, dy, eq, r_frac2, sp, dx).move_to(e_2); eq.restore_y()

        self.play(
            TransformInStages.replacement_transform(e_2, [r_frac2_num, e_3[4].denominator[0]], run_time=1.5),
            TransformInStages.replacement_transform(e_2, e_3[4].denominator[1], config={"intro": Write}, run_time=1.5)
        )
        

        self.wait()

        # medyo okay: e_2 = MathTex(Fraction([x, y1], x), sp, dy, eq, Fraction(Parentheses([wan, p, Term(y2, tu)], paren=e_1[4].paren), [x]), sp, dx).move_to(e_1)
        # 10-18-26 04:01 pm: the code above ^ was an attempt to make the denominators use the Write function, which took me so long to debug yet I'm so close to success
        # however, I decided to just stick with the normal transform where the numerators duplicate and slide to the denominators, which makes much more sense anyway
        # since they're just literal copies of themselves and are not new elements. Write should only be used for new elements

class Testing2(Scene):
    def construct(self):

        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        sp = MathTex(r"\ ")

        d = MathTex(x, y1, sp, dy, eq, Parentheses([wan, p, Term(y2, tu)]), sp, dx).to_edge(UP).shift(DOWN * 0.4); eq.save_y(),  # cinema din to, hindi na magagalaw yung y

        # ---------  Anim5.1  --------- 
        # nadiskubre na rin sa wakas kung paano i-keep yung parentheses, d.paren lang pala, or generally paren=[function].paren,
        # where [function] ay yung huling defined na function na pagkukunan ng parentheses ng current function

        self.add(d)

        l_frac1 = Fraction([x, y1], x)
        r_paren = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)
        e_1 = MathTex(l_frac1, sp, dy, eq, r_paren, sp, dx).move_to(d); eq.restore_y(), 

        # tangina palo
        self.play(TransformInStages.replacement_transform(d, e_1)) 

        # ---------  Anim5.2  --------- 
        r_frac1 = Fraction(r_paren, x)
        e_2 = MathTex([l_frac1], sp, dy, eq, r_frac1, sp, dx).move_to(e_1); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_1, e_2, run_time=1.5))
        
        # ---------  Anim5.3  --------- 
        r_frac2 = Fraction(r_paren, [x, r_paren], vinculum=r_frac1.vinculum)
        e_3 = MathTex(l_frac1, sp, dy, eq, r_frac2, sp, dx).move_to(e_2); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_2, e_3, run_time=1.5))

        # ---------  Anim5.4  --------- 
        l_frac2 = Fraction(l_frac1.numerator, [l_frac1.denominator, r_paren], vinculum=l_frac1.vinculum)
        e_4 = MathTex(l_frac2, sp, dy, eq, [r_frac2], sp, dx); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_3, e_4, run_time=1.5))
        # tangina cinema talaga

        # ---------  Anim6  --------- 
        f = MathTex(l_frac2, sp, dy, eq, r_frac2, sp, dx).next_to(e_4, DOWN, buff=0.6)
        e_4_copy = e_4.copy().move_to(f)

        self.play(
            TransformFromCopy(e_4, e_4_copy), run_time=1.5)

        l_cancel2_num = Line(
            f[0].numerator[0].get_corner(DL), 
            f[0].numerator[0].get_corner(UR), 
            color=RED
        )
        l_cancel2_den = Line(
            f[0].denominator[0].get_corner(DL), 
            f[0].denominator[0].get_corner(UR), 
            color=RED
        )
        r_cancel2_num = Line(
            f[4].numerator.get_corner(DL), 
            f[4].numerator.get_corner(UR), 
            color=RED
        )
        r_cancel2_den = Line(
            f[4].denominator[1].get_corner(DL), 
            f[4].denominator[1].get_corner(UR), 
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

        # ---------  Anim7  --------- 
        l_frac3 = Fraction([l_frac2.numerator[1], sp, dy], l_frac2.denominator[1], vinculum=l_frac2.vinculum)
        r_frac3 = Fraction(dx, r_frac2.denominator[0], vinculum=r_frac2.vinculum)
        
        g = MathTex(l_frac3, eq, r_frac3).next_to(f, DOWN, buff=0.6)

        self.play(TransformInStages.from_copy(e_4_copy, g, run_time=1.5))

        self.wait()

# this is after realizing na di na dapat pa isama yung integration na scene
class Testing3(Scene):
    def construct(self):

        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)

        sp = MathTex(r"\ ")

        d = MathTex(x, y1, sp, dy, eq, Parentheses([wan, p, Term(y2, tu)]), sp, dx).to_edge(UP).shift(DOWN * 0.4); eq.save_y(),  # cinema din to, hindi na magagalaw yung y

        # ---------  Anim5  --------- 
        # nadiskubre na rin sa wakas kung paano i-keep yung parentheses, d.paren lang pala, or generally paren=[function].paren,
        # where [function] ay yung huling defined na function na pagkukunan ng parentheses ng current function

        self.add(d)

        # chakalimination = Text("CHAKALIMINATION™").set_color(LIGHT_PINK).next_to(d, DOWN, buff=0.8)
        # box = SurroundingRectangle(chakalimination, color=YELLOW, buff=0.3)

        # self.play(Write(chakalimination[0:15], run_time=1.5))
        # self.play(Write(chakalimination[15], run_time=0.7))
        # self.play(Write(box), run_time=1.5)

        # chaka = Text("chaka", font="LMRoman10", slant=ITALIC).shift(LEFT * 3).scale(0.7)
        # self.play(TransformFromCopy(chakalimination[0:5], chaka), run_time=1.7)
        
        # chaka_par = Paragraph(
        #     "any term/variable",
        #     "that does not belong",
        #     "to its group",
        #     alignment="center",
        #     font="LMRoman10",
        #     line_spacing=0.6
        # ).next_to(chaka, DOWN * 0.01).scale(0.6)
        # self.play(DrawBorderThenFill(chaka_par), run_time=2)

        # elimination = Text("elimination", font="LMRoman10", slant=ITALIC).shift(RIGHT * 3).scale(0.7)
        # self.play(TransformFromCopy(chakalimination[6:15], elimination), run_time=1.7)

        # elimination_par = Paragraph(
        #     "to eliminate",
        #     "that term/variable",
        #     "via division",
        #     alignment="center",
        #     font="LMRoman10",
        #     line_spacing=0.6
        # ).next_to(elimination, DOWN * 0.01).scale(0.6)
        # self.play(DrawBorderThenFill(elimination_par), run_time=2)

        # self.play(
        #     AnimationGroup(
        #         FadeOut(VGroup(chaka, chaka_par, elimination, elimination_par)),
        #         VGroup(chakalimination, box).animate.to_edge(DOWN).shift(UP * 0.2).scale(0.7),
        #         run_time=1.5
        #     )
        # )

        self.play(
            AnimationGroup(
                VGroup(y1, y2).animate.set_color(YELLOW),
                x.animate.set_color(BLUE),
                run_time=1.5
            )
        )
        
        # ---------  Anim6.1  --------- 
        l_frac1 = Fraction([x, y1], x)
        r_paren = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)
        e_1 = MathTex(l_frac1, sp, dy, eq, r_paren, sp, dx).move_to(d); eq.restore_y(), 

        # tangina palo
        self.play(TransformInStages.replacement_transform(d, e_1)) 

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
        e_4 = MathTex(l_frac2, sp, dy, eq, [r_frac2], sp, dx); eq.restore_y(), 

        self.play(TransformInStages.replacement_transform(e_3, e_4, run_time=1.5))
        # tangina cinema talaga

        # ---------  Anim6  --------- 
        f = MathTex(l_frac2, sp, dy, eq, r_frac2, sp, dx).next_to(e_4, DOWN, buff=0.6)
        e_4_copy = e_4.copy().move_to(f)

        self.play(TransformFromCopy(e_4, e_4_copy, run_time=1.5))

        l_cancel2_num = Line(
            f[0].numerator[0].get_corner(DL), 
            f[0].numerator[0].get_corner(UR), 
            color=RED
        )
        l_cancel2_den = Line(
            f[0].denominator[0].get_corner(DL), 
            f[0].denominator[0].get_corner(UR), 
            color=RED
        )
        r_cancel2_num = Line(
            f[4].numerator.get_corner(DL), 
            f[4].numerator.get_corner(UR), 
            color=RED
        )
        r_cancel2_den = Line(
            f[4].denominator[1].get_corner(DL), 
            f[4].denominator[1].get_corner(UR), 
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

        # ---------  Anim7  --------- 
        l_frac3 = Fraction([l_frac2.numerator[1], sp, dy], l_frac2.denominator[1], vinculum=l_frac2.vinculum)
        r_frac3 = Fraction(dx, r_frac2.denominator[0], vinculum=r_frac2.vinculum)
        
        g = MathTex(l_frac3, eq, r_frac3).next_to(f, DOWN, buff=0.7)

        self.play(TransformInStages.from_copy(e_4_copy, g, run_time=1.8))

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

        # self.play(TransformInStages.replacement_transform(h, i, run_time=1.5))
        # self.play(Write(ans), run_time=1.5)

        self.wait()

        # ---------  Anim10 (reyal)  --------- 
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


class ParenthesesTest(Scene):
    def construct(self):
        wan, p, y2, tu = MathTex("1", "+", "y", "2")
        term = Term(y2, tu)

        paren = Parentheses([wan, p, term])

        print("Parentheses type:", type(paren).__name__)
        print("Direct children:", len(paren.submobjects))

        for i, child in enumerate(paren.submobjects):
            print(
                i,
                type(child).__name__,
                "children:", len(child.submobjects),
            )

        self.play(Write(paren), run_time=2)
        self.wait()