from manim import *
from reactive_manim import *

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

        r_frac1 = Fraction(r_paren, "x")
        r_frac1_num = r_frac1.numerator, r_frac1.vinculum

        e_2 = MathTex([l_frac], sp, dy, eq, [r_frac1], sp, dx).move_to(e_1); eq.restore_y()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(e_1, r_frac1_num, run_time=1.5),
                Write(r_frac1.denominator, run_time=1.5), 
                lag_ratio=0.5
            )
        )   
    
        r_frac2 = Fraction(r_paren, ["x", r_paren])
        r_frac2_num = r_frac2.numerator, r_frac2.vinculum

        e_3 = MathTex([l_frac], sp, dy, eq, [r_frac2], sp, dx).move_to(e_2); eq.restore_y()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(e_2, r_frac2_num, run_time=1.5),
                Write(r_frac2.denominator[1], run_time=1.5), 
                lag_ratio=0.5
            )
        )

        self.wait()