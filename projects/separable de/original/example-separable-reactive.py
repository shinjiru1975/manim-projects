from manim import *
from reactive_manim import  *

# Attempt 10: reactive manim
class Separable10(Scene):
    def construct(self):
        
        # Anim1
        x, y, yp, p = MathTex("x", "y", "y'", "+")

        tl = MathTex(x, y, yp)
        tr = MathTex("1", p, Term(y, "2"))

        tex = MathTex(tl, "=", tr).to_edge(UP)
        

        self.play(Write(tex), run_time=1.5)

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)

        x2 = x
        y2 = y
        dydx = Fraction(dy, dx)

        tex.LHS.terms = [ x2, y2, dydx ]

        self.play(TransformInStages.progress(tex))

        self.wait()

# Attempt 11: let's try from_copy na transform type
class Separable11(Scene):
    def construct(self):
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        dydx = Fraction(dy, dx)

        sp = MathTex(r"\ ")

        tex1 = MathTex(x, y1, yp, eq, [ wan, p, Term(y2, tu) ])
        tex2 = MathTex(x, y1, sp, [dydx], eq, [  wan, p, Term(y2, tu) ])
        tex3 = MathTex(Parentheses(dx), sp, x, y1, sp, [dydx], eq, [  wan, p, Term(y2, tu) ], sp, Parentheses(dx))

        VGroup(tex1, tex2, tex3).arrange(DOWN, buff=0.4).to_edge(UP)

        self.play(Write(tex1), run_time=1.5)
        self.play(TransformInStages.from_copy(tex1, tex2, run_time=1.5))
        self.play(TransformInStages.from_copy(tex2, tex3, run_time=1.5))
        self.wait()

        # NEXT NA GAGAWIN: bumalik sa Separable9 and i-try na i-define yung mga terms ng kagaya dito
        # x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")
        # gawing unique yung dx: 
        # dx1 = MathTex("dx") 
        # dx2 = MathTex("dx") 

# Attempt 13: i'm just gonna try implementing the animations from the non-reactive file to this reactive
class Separable13(Scene):
    def construct(self):
 
        self.next_section(skip_animations=False)

        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        dydx = Fraction(dy, dx)

        sp = MathTex(r"\ ")

        # ---------  Anim1  --------- 
        a = MathTex(x, y1, yp, eq, [ wan, p, Term(y2, tu) ]).to_edge(UP)

        self.play(Write(a), run_time=1.5)

        # ---------  Anim2  --------- 
        b = MathTex(x, y1, sp, dydx, eq, [  wan, p, Term(y2, tu) ]).next_to(a, DOWN, buff=0.5)
        a_copy = a.copy().move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            Indicate(a_copy[2], color=YELLOW, scale_factor=1.5, run_time=1.5)
        )

        # THIS IS FUCKING CINEMA
        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(a_copy, [b[0:2], b[4:5]], run_time=1.5), 
                Write(dydx), lag_ratio=0.6
            )
        )

        # ---------  Anim3  --------- 
        c = MathTex(Parentheses(dx), sp, x, y1, sp, dydx, eq, [  wan, p, Term(y2, tu) ], sp, Parentheses(dx)).next_to(b, DOWN, buff=0.5)
        b_copy = b.copy().move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            Write(c[0]),
            Write(c[9]),                                                                                                        
            run_time=1.5
        )

        left_cancel = Line(c[0].get_corner(DL), c[0].get_corner(UR), color=RED)
        right_cancel = Line(c[5].denominator.get_corner(DL), c[5].denominator.get_corner(UR), color=RED)

        self.play(
            Write(left_cancel), 
            Write(right_cancel), 
            run_time=1.5
        )
        
        # ---------  Anim4  --------- 
        d = MathTex(x, y1, sp, dy, eq, Parentheses([wan, p, Term(y2, tu)]), sp, dx).next_to(c, DOWN, buff=0.5)

        self.play(
            TransformInStages.from_copy(c, d, run_time=2), 
        )

        # ------------------  After Differentials  ------------------

        self.play(
            *[FadeOut(mob) for mob in self.mobjects], 
            d.animate.to_edge(UP).shift(DOWN * 0.4), 
            run_time=1.5
        )

        self.add(d)

        # ---------  Anim5  --------- 
        # nadiskubre na rin sa wakas kung paano i-keep yung parentheses, d.paren lang pala, or generally paren=[function].paren,
        # where [function] ay yung huling defined na function na pagkukunan ng parentheses ng current function
        # l_frac = Fraction([x, y1], x)
        # r_paren = Parentheses([wan, p, Term(y2, tu)], paren=d[5].paren)

        # e_1 = MathTex(l_frac, sp, dy, eq, r_paren, sp, dx).to_edge(UP).next_to(d, DOWN, buff=0.5)
        # d_copy = d.copy().move_to(e_1)

        # e_1[3].save_y()

        # self.play(
        #     TransformInStages.from_copy(d, d_copy, run_time=1.5)
        # )

        # e_2 = MathTex([l_frac], sp, dy, eq, Fraction(r_paren, l_frac.numerator[0]), sp, dx).move_to(e_1)
        # e_1[3].restore_y()

        # self.play(
        #     TransformInStages.replacement_transform(e_1, e_2, run_time=1.5)
        # )

        # let's try coloring the x to blue and y to yellow as well

        self.wait()

# Attempt 14: trying to simplify code with the official reactive manim syntax  fror TransformInStages.from_copy
class Separable14(Scene):
    def construct(self):
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        dydx = Fraction(dy, dx)

        sp = MathTex(r"\ ")

        tex1 = MathTex(x, y1, yp, eq, [ wan, p, Term(y2, tu) ]).to_edge(UP)
        tex2 = MathTex(x, y1, sp, [dydx], eq, [  wan, p, Term(y2, tu) ]).next_to(tex1, DOWN, buff=0.5)
        tex3 = MathTex(Parentheses(dx), sp, x, y1, sp, dydx, eq, [  wan, p, Term(y2, tu) ], sp, Parentheses(dx)).next_to(tex2, DOWN, buff=0.5)

        tex1_copy = tex1.copy().move_to(tex2)
        tex2_copy = tex2.copy().move_to(tex3)

        self.play(Write(tex1), run_time=1.5)
        self.play(TransformFromCopy(tex1, tex1_copy, run_time=1.5))
        # tangina mas cinema to gago
        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(tex1_copy, [tex2[0:2], tex2[4:5]], run_time=1.5),
                Write(tex2[3], run_time=1.5), lag_ratio=0.6
            )
        )
        self.play(TransformFromCopy(tex2, tex2_copy, run_time=1.5))
        self.play(
            Write(tex3[0]),
            Write(tex3[9]),                                                                                                        
            run_time=1.5
        )

        self.wait()

class Function1(Scene):
    def construct(self):

        func = Function("\text{sin}", "\theta")
        self.add(func)

        func.function.set_color(GREEN)
        func.input.set_color(LIGHT_BROWN)
        func.parentheses.set_color(WHITE)

class Quickstart(Scene):
    def construct(self):

        a = MathTex("a", color=RED)
        b = MathTex("b", color=BLUE)
        c = MathTex("c", color=GREEN)

        tex = MathTex([[ a, "x^2" ], "+", [ b, "x" ], "+", [ c ]], "=", 0)
        self.add(tex).wait(1)


        b.swap(lambda: Fraction(b, a.pop()))
        c.swap(lambda: Fraction(c, a))

        self.play(TransformInStages.progress(tex))