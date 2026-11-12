from manim import *
from reactive_manim import *

class Scene3Attempt1(Scene):
    def construct(self):

        rt = {"run_time":1.5}
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        y1.set_color(YELLOW)
        y2.set_color(YELLOW)
        x.set_color(BLUE)

        sp = MathTex(r"\ ")

        # ---------  Anim8  --------- 
        paren_new = Parentheses([wan, p, Term(y1, tu)])
        l_frac3_new = Fraction([y1, sp, dy], paren_new)
        r_frac3_new = Fraction(dx, x)

        g_new = MathTex(l_frac3_new, eq, r_frac3_new).to_edge(UP)

        self.add(g_new)

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        int1 = MathTex(integ, l_frac3_new)
        int2 = MathTex(integ, r_frac3_new)
        
        h = MathTex(int1, eq, int2).move_to(g_new); eq.save_x()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g_new, [h[0][1], h[2][1]]),
                AnimationGroup(
                    Write(int1[0]),
                    Write(int2[0]),
                ),
                run_time=1.5,
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1  --------- 
        #p2 = MathTex("+")
        #ln, c = MathTex(r"\ln", "C")
        #lnx = Function(ln, x)
        #rhs1 = MathTex(eq, int2); eq.restore_x()
        #rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x()

        #i = MathTex(int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()

        #self.play(

                #TransformFromCopy(h[2], rhs2, run_time=1.5),
        #)

        #self.wait()

        # ---------  Anim10.2  --------- 
        p2 = MathTex("+")
        ln, c = MathTex(r"\ln", "C")
        lnx = Function(ln, x)
        rhs1 = MathTex(eq, int2); eq.restore_x()
        rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x()

        i = MathTex(int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()
        
        self.play(
            LaggedStart(
                TransformInStages.from_copy(h[2][1].denominator, rhs2[1][2], run_time=1.5),
                Write(rhs2, run_time=1.5),
                lag_ratio=0.6
            )
        )

        #p2 = MathTex("+")
        #ln, c = MathTex(r"\ln", "C")
        #lnx = Function(ln, x); eq.restore_x()
        #rhs = MathTex(eq, lnx, p2, c); eq.restore_x()

        #i = MathTex(int1, eq, rhs).next_to(h, DOWN, buff=0.6); eq.restore_x()

        #self.play(
         #   LaggedStart(
          #      TransformInStages.from_copy(h[2][1].denominator, i[2][1][2], run_time=1.5),
           #     Write(i[2], run_time=1.5),
            #    lag_ratio=0.5
            #)
        #)

        # ---------  Anim10.2.1  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        y1 = MathTex(l_frac3_new.denominator.input[2][0])
        
        
        u, du = MathTex("u", "du").set_color(GREEN)
        u_paren = MathTex(wan, p, Term(y1, tu))

        u_paren_phantom = create_phantom(u_paren)

        u_eq = MathTex(u, eq, u_paren_phantom).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()

        u_paren.move_to(u_paren_phantom).set_color(GREEN)

        du_eq = MathTex(du, eq, tu, y1, sp, dy).set_color(GREEN).next_to(u_eq, DOWN, buff=0.5); eq.restore_x()
        dy.set_color(YELLOW)

        self.play(
            LaggedStart(
                Write(u_eq, **rt),
                TransformInStages.from_copy(h[0][1].denominator, u_paren, **rt),
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.2.2  --------- 
        u_eq = MathTex(u, eq, u_paren).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()

        self.play(
            TransformInStages.from_copy(
                u_eq, du_eq,
                **rt
            ),
        )

        self.wait()

class Scene3Attempt2(Scene):
    def construct(self):

        rt = {"run_time":1.5}
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        y1.set_color(YELLOW)
        y2.set_color(YELLOW)
        x.set_color(BLUE)

        sp = MathTex(r"\ ")

        # ---------  Anim8  --------- 
        paren_new = Parentheses([wan, p, Term(y1, tu)])
        l_frac3_new = Fraction([y1, sp, dy], paren_new)
        r_frac3_new = Fraction(dx, x)

        g_new = MathTex(l_frac3_new, eq, r_frac3_new).to_edge(UP)

        self.add(g_new)

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        int1 = MathTex(integ, l_frac3_new)
        int2 = MathTex(integ, r_frac3_new)
        
        h = MathTex(int1, eq, int2).move_to(g_new); eq.save_x()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g_new, [h[0][1], h[2][1]]),
                AnimationGroup(
                    Write(int1[0]),
                    Write(int2[0]),
                ),
                run_time=1.5,
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1  --------- 
        p2 = MathTex("+")
        ln, c = MathTex(r"\ln", "C")
        lnx = Function(ln, x)
        rhs1 = MathTex(eq, int2); eq.restore_x()
        rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x()

        i = MathTex(int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()
        
        self.play(
            LaggedStart(
                TransformInStages.from_copy(h[2][1].denominator, rhs2[1][2], run_time=1.5),
                Write(rhs2, run_time=1.5),
                lag_ratio=0.6
            )
        )

        # ---------  Anim10.1.1  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        y1 = MathTex(l_frac3_new.denominator.input[2][0])
        
        
        u, du = MathTex("u", "du").set_color(GREEN)

        u_rhs = MathTex(wan, p, Term(y1, tu))
        u_rhs_phantom = create_phantom(u_rhs)

        u_eq = MathTex(u, eq, u_rhs_phantom).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()
        u_rhs.move_to(u_rhs_phantom).set_color(GREEN)

        dy.set_color(YELLOW)

        self.play(
            LaggedStart(
                Write(u_eq, **rt),
                TransformInStages.from_copy(h[0][1].denominator, u_rhs, **rt),
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1.2  --------- 
        du_rhs = MathTex(tu, y1, sp, dy)

        du_rhs_phantom = create_phantom(du_rhs)

        du_eq = MathTex(du, eq, du_rhs_phantom).set_color(GREEN).next_to(u_eq, DOWN, buff=0.5); eq.restore_x()
        du_rhs.move_to(du_rhs_phantom)

        self.play(
            LaggedStart(
                Write(du_eq, **rt),
                TransformInStages.from_copy(u_rhs, du_rhs, **rt),
  
                lag_ratio=0.5
            ),
        )

        self.wait()

class Scene3Attempt3(Scene):
    def construct(self):

        rt = {"run_time":1.5}
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        y1.set_color(YELLOW)
        y2.set_color(YELLOW)
        x.set_color(BLUE)

        sp = MathTex(r"\ ")

        # ---------  Anim8  --------- 
        paren_new = Parentheses([wan, p, Term(y1, tu)])
        l_frac3_new = Fraction([y1, sp, dy], paren_new)
        r_frac3_new = Fraction(dx, x)

        g_new = MathTex(l_frac3_new, eq, r_frac3_new).to_edge(UP)

        self.add(g_new)

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        int1 = MathTex(integ, l_frac3_new)
        int2 = MathTex(integ, r_frac3_new)
        
        h = MathTex(int1, eq, int2).move_to(g_new); eq.save_x()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g_new, [h[0][1], h[2][1]]),
                AnimationGroup(
                    Write(int1[0]),
                    Write(int2[0]),
                ),
                run_time=1.5,
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1  --------- 
        p2 = MathTex("+")
        ln, c = MathTex(r"\ln", "C")
        lnx = Function(ln, x)
        rhs1 = MathTex(eq, int2); eq.restore_x()
        rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x()

        i = MathTex(int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()
        
        self.play(
            LaggedStart(
                TransformInStages.from_copy(h[2][1].denominator, rhs2[1][2], run_time=1.5),
                Write(rhs2, run_time=1.5),
                lag_ratio=0.6
            )
        )

        # ---------  Anim10.1.1  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        y1 = MathTex(l_frac3_new.denominator.input[2][0])
        
        
        u, du = MathTex("u", "du").set_color(GREEN)

        u_rhs = MathTex(wan, p, Term(y1, tu))
        u_rhs_phantom = create_phantom(u_rhs)

        u_eq = MathTex(u, eq, u_rhs_phantom).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()
        u_rhs.move_to(u_rhs_phantom).set_color(GREEN)

        dy.set_color(YELLOW)

        self.play(
            LaggedStart(
                Write(u_eq, **rt),
                TransformInStages.from_copy(h[0][1].denominator, u_rhs, **rt),
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1.2  --------- 
        du_rhs = MathTex(tu, y1, sp, dy)
        du_rhs_phantom = create_phantom(du_rhs)

        dy_phantom = create_phantom(dy)
        du_rhs_dy_phantom = MathTex(tu, y1, sp, dy_phantom)

        du_eq = MathTex(du, eq, du_rhs_phantom).set_color(GREEN).next_to(u_eq, DOWN, buff=0.5); eq.restore_x()
        du_rhs.move_to(du_rhs_phantom)
        du_rhs_dy_phantom.move_to(du_rhs_phantom)   # moved here, after du_eq is in place

        self.play(
            LaggedStart(
                Write(du_eq, **rt),
                TransformInStages.from_copy(u_rhs, du_rhs_dy_phantom, **rt),
                Write(du_rhs[3]),
                lag_ratio=0.5
            ),
        )

        self.wait()

class Scene3Attempt4(Scene):
    def construct(self):

        rt = {"run_time":1.5}
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        y1.set_color(YELLOW)
        y2.set_color(YELLOW)
        x.set_color(BLUE)

        sp = MathTex(r"\ ")

        # ---------  Anim8  --------- 
        paren_new = Parentheses([wan, p, Term(y1, tu)])
        l_frac3_new = Fraction([y1, sp, dy], paren_new)
        r_frac3_new = Fraction(dx, x)

        g_new = MathTex(l_frac3_new, eq, r_frac3_new).to_edge(UP)

        self.add(g_new)

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        l_int1 = MathTex(integ, l_frac3_new)
        r_int1 = MathTex(integ, r_frac3_new)
        
        h = MathTex(l_int1, eq, r_int1).move_to(g_new); eq.save_x()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g_new, [h[0][1], h[2][1]]),
                AnimationGroup(
                    Write(l_int1[0]),
                    Write(r_int1[0]),
                ),
                run_time=1.5,
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1  --------- 
        p2 = MathTex("+")
        ln, c = MathTex(r"\ln", "C")
        lnx = Function(ln, x)
        rhs1 = MathTex(eq, r_int1); eq.restore_x()
        rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x(); eq.save_y()

        i = MathTex(l_int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()
        
        self.play(
            LaggedStart(
                TransformInStages.from_copy(h[2][1].denominator, rhs2[1][2], run_time=1.5),
                Write(rhs2, run_time=1.5),
                lag_ratio=0.6
            )
        )

        # ---------  Anim10.1.1  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        y1 = MathTex(l_frac3_new.denominator.input[2][0])
        
        
        u, du = MathTex("u", "du").set_color(GREEN)

        u_rhs = MathTex(wan, p, Term(y1, tu))
        u_rhs_phantom = create_phantom(u_rhs)

        u_eq = MathTex(u, eq, u_rhs_phantom).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()
        u_rhs.move_to(u_rhs_phantom).set_color(GREEN)

        dy.set_color(YELLOW)

        self.play(
            LaggedStart(
                Write(u_eq, **rt),
                TransformInStages.from_copy(h[0][1].denominator, u_rhs, **rt),
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1.2  --------- 
        du_rhs = MathTex(tu, y1, sp, dy)
        du_rhs_phantom = create_phantom(du_rhs)

        dy_phantom = create_phantom(dy)
        du_rhs_dy_phantom = MathTex(tu, y1, sp, dy_phantom)

        du_eq = MathTex(du, eq, du_rhs_phantom).set_color(GREEN).next_to(u_eq, DOWN, buff=0.5); eq.restore_x()
        du_rhs.move_to(du_rhs_phantom)
        du_rhs_dy_phantom.move_to(du_rhs_phantom)   # moved here, after du_eq is in place

        self.play(
            LaggedStart(
                Write(du_eq, **rt),
                TransformInStages.from_copy(u_rhs, du_rhs_dy_phantom, **rt),
                Write(du_rhs[3], **rt),
                lag_ratio=0.6
            ),
        )

        # ---------  Anim10.2  --------- 
        wanhap = Fraction(wan, du_rhs[0]).set_color(WHITE)
        l_frac4 = Fraction(du_eq[0], u_eq[0])
        l_int2 = MathTex(integ, l_frac4).set_color(WHITE)

        # nadiskubre tong vector trick
        # basically isusubtract niya yung position ng original eq (nasa rhs[0]) sa fake eq (nasa j[2]),
        # then by shifting the entire expression by that difference, it would end up at the original position
        j = MathTex(wanhap, l_int2, eq)
        j.shift(rhs2[0].get_center() - j[2].get_center())

        self.play(TransformInStages.from_copy(du_rhs[0], wanhap.denominator), run_time=2)
        self.play(
            LaggedStart(
                Write(
                    VGroup(wanhap.numerator, wanhap.vinculum), **rt
                ),
                Write(integ, **rt),
                lag_ratio=0.2
            )       
        )

        tu_cancel = Line(du_rhs[0].get_corner(DL), du_rhs[0].get_corner(UR), color=RED)
        self.play(Write(tu_cancel), **rt)

        self.play(TransformInStages.from_copy(du_eq[0], l_frac4.numerator), run_time=2)
        

        self.play(Write(VGroup(j[0], j[1])))   
        self.wait()

class Scene3Attempt5(Scene):
    def construct(self):

        rt = {"run_time":1.5}
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        y1.set_color(YELLOW)
        y2.set_color(YELLOW)
        x.set_color(BLUE)

        sp = MathTex(r"\ ")

        # ---------  Anim8  --------- 
        paren_new = Parentheses([wan, p, Term(y1, tu)])
        l_frac3_new = Fraction([y1, sp, dy], paren_new)
        r_frac3_new = Fraction(dx, x)

        g_new = MathTex(l_frac3_new, eq, r_frac3_new).to_edge(UP)

        self.add(g_new)

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        l_int1 = MathTex(integ, l_frac3_new)
        r_int1 = MathTex(integ, r_frac3_new)
        
        h = MathTex(l_int1, eq, r_int1).move_to(g_new); eq.save_x()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g_new, [h[0][1], h[2][1]], run_time=1.5,),
                AnimationGroup(
                    Write(l_int1[0]),
                    Write(r_int1[0]),
                    run_time=1.5,
                ),
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1  --------- 
        p2 = MathTex("+")
        ln, c = MathTex(r"\ln", "C")
        lnx = Function(ln, x)
        rhs1 = MathTex(eq, r_int1); eq.restore_x()
        rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x(); eq.save_y()

        i = MathTex(l_int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()
        
        self.play(
            LaggedStart(
                TransformInStages.from_copy(h[2][1].denominator, rhs2[1][2], run_time=1.5),
                Write(rhs2, run_time=1.5),
                lag_ratio=0.6
            )
        )

        # ---------  Anim10.1.1  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        y1 = MathTex(l_frac3_new.denominator.input[2][0])
        
        
        u, du = MathTex("u", "du").set_color(GREEN)

        u_rhs = MathTex(wan, p, Term(y1, tu))
        u_rhs_phantom = create_phantom(u_rhs)

        u_eq = MathTex(u, eq, u_rhs_phantom).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()
        u_rhs.move_to(u_rhs_phantom).set_color(GREEN)

        dy.set_color(YELLOW)

        self.play(Write(u_eq), **rt)
        self.play(TransformInStages.from_copy(h[0][1].denominator, u_rhs, **rt))

        # ---------  Anim10.1.2  --------- 
        du_rhs = MathTex(tu, y1, sp, dy)
        du_rhs_phantom = create_phantom(du_rhs)

        dy_phantom = create_phantom(dy)
        du_rhs_dy_phantom = MathTex(tu, y1, sp, dy_phantom)

        du_eq = MathTex(du, eq, du_rhs_phantom).set_color(GREEN).next_to(u_eq, DOWN, buff=0.5); eq.restore_x()
        du_rhs.move_to(du_rhs_phantom)
        du_rhs_dy_phantom.move_to(du_rhs_phantom)   # moved here, after du_eq is in place

        self.play(Write(du_eq), **rt)
        self.play(TransformInStages.from_copy(u_rhs, du_rhs_dy_phantom, **rt))
        self.play(Write(du_rhs[3]), **rt)

        # ---------  Anim10.2  --------- 
        wanhap = Fraction(wan, du_rhs[0]).set_color(WHITE)
        l_frac4 = Fraction(du_eq[0], u_eq[0])
        l_int2 = MathTex(integ, l_frac4).set_color(WHITE)

        # nadiskubre tong vector trick
        # basically isusubtract niya yung position ng original eq (nasa rhs[0]) sa fake eq (nasa j[2]),
        # then by shifting the entire expression by that difference, it would end up at the original position
        j = MathTex(create_phantom(wanhap), create_phantom(l_int2), eq)
        j.shift(rhs2[0].get_center() - j[2].get_center())

        wanhap.move_to(j[0])
        l_int2.move_to(j[1])
        l_frac4.set_color(GREEN)

        self.play(TransformInStages.from_copy(du_rhs[0], wanhap.denominator, run_time=1.5))
        self.play(
            LaggedStart(
                Write(
                    VGroup(wanhap.numerator, wanhap.vinculum), **rt
                ),
                Write(integ, **rt),
                lag_ratio=0.2
            )       
        )

        tu_cancel = Line(du_rhs[0].get_corner(DL), du_rhs[0].get_corner(UR), color=RED)

        self.play(Write(tu_cancel), **rt)

        du_copy = du_eq[0].copy()
        u_copy = u_eq[0].copy()

        self.play(
            LaggedStart(
                AnimationGroup(
                    u_copy.animate.move_to(l_frac4.denominator), 
                    du_copy.animate.move_to(l_frac4.numerator),
                    **rt
                ), 
                Write(l_frac4.vinculum),
                lag_ratio=0.9
            )
        )

        j = MathTex(wanhap, l_int2, rhs2).next_to(i, DOWN, buff=0.6)
        j.shift(rhs2[0].get_center() - j[2][0].get_center()); eq.save_x()
        self.add(j)
        # i mean ts works

        # self.play(Write(VGroup(j[0], j[1]))) 

class Scene3Attempt6(Scene):
    def construct(self):

        rt = {"run_time":1.5}
        
        x, y1, yp, eq, wan, p, y2, tu = MathTex("x", "y", "y'", "=", "1", "+", "y", "2")

        dy = MathTex("dy").set_color(YELLOW)
        dx = MathTex("dx").set_color(BLUE)
        y1.set_color(YELLOW)
        y2.set_color(YELLOW)
        x.set_color(BLUE)

        sp = MathTex(r"\ ")

        # ---------  Anim8  --------- 
        paren_new = Parentheses([wan, p, Term(y1, tu)])
        l_frac3_new = Fraction([y1, sp, dy], paren_new)
        r_frac3_new = Fraction(dx, x)

        g_new = MathTex(l_frac3_new, eq, r_frac3_new).to_edge(UP)

        self.add(g_new)

        # ---------  Anim9  --------- 
        integ = MathTex(r"\int")
        l_int1 = MathTex(integ, l_frac3_new)
        r_int1 = MathTex(integ, r_frac3_new)
        
        h = MathTex(l_int1, eq, r_int1).move_to(g_new); eq.save_x()

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(g_new, [h[0][1], h[2][1]], run_time=1.5,),
                AnimationGroup(
                    Write(l_int1[0]),
                    Write(r_int1[0]),
                    run_time=1.5,
                ),
                lag_ratio=0.5
            )
        )

        # ---------  Anim10.1  --------- 
        p2 = MathTex("+")
        ln, c = MathTex(r"\ln", "C")
        lnx = Function(ln, x)
        rhs1 = MathTex(eq, r_int1); eq.restore_x()
        rhs2 = MathTex(eq, lnx, p2, c); eq.next_to(h, DOWN, buff=0.6); eq.restore_x(); eq.save_y()

        i = MathTex(l_int1, rhs1).next_to(h, DOWN, buff=0.6); eq.restore_x()
        
        self.play(
            LaggedStart(
                TransformInStages.from_copy(h[2][1].denominator, rhs2[1][2], run_time=1.5),
                Write(rhs2, run_time=1.5),
                lag_ratio=0.6
            )
        )

        # ---------  Anim10.1.1  --------- 
        def create_phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        y1 = MathTex(l_frac3_new.denominator.input[2][0])
        
        
        u, du = MathTex("u", "du").set_color(GREEN)

        u_rhs = MathTex(wan, p, Term(y1, tu))
        u_rhs_phantom = create_phantom(u_rhs)

        u_eq = MathTex(u, eq, u_rhs_phantom).set_color(GREEN).next_to(h, LEFT, buff=1); eq.save_x()
        u_rhs.move_to(u_rhs_phantom).set_color(GREEN)

        dy.set_color(YELLOW)

        self.play(Write(u_eq), **rt)
        self.play(TransformInStages.from_copy(h[0][1].denominator, u_rhs, **rt))

        # ---------  Anim10.1.2  --------- 
        du_rhs = MathTex(tu, y1, sp, dy)
        du_rhs_phantom = create_phantom(du_rhs)

        dy_phantom = create_phantom(dy)
        du_rhs_dy_phantom = MathTex(tu, y1, sp, dy_phantom)

        du_eq = MathTex(du, eq, du_rhs_phantom).set_color(GREEN).next_to(u_eq, DOWN, buff=0.5); eq.restore_x()
        du_rhs.move_to(du_rhs_phantom)
        du_rhs_dy_phantom.move_to(du_rhs_phantom)   # moved here, after du_eq is in place

        self.play(Write(du_eq), **rt)
        self.play(TransformInStages.from_copy(u_rhs, du_rhs_dy_phantom, **rt))
        self.play(Write(du_rhs[3]), **rt)

        # ---------  Anim10.2  --------- 
        wanhap = Fraction(wan, du_rhs[0]).set_color(WHITE)
        l_frac4 = Fraction(du_eq[0], u_eq[0])
        l_int2 = MathTex(integ, l_frac4).set_color(WHITE)

        # nadiskubre tong vector trick
        # basically isusubtract niya yung position ng original eq (nasa rhs[0]) sa fake eq (nasa j[2]),
        # then by shifting the entire expression by that difference, it would end up at the original position
        j = MathTex(create_phantom(wanhap), create_phantom(l_int2), eq)
        j.shift(rhs2[0].get_center() - j[2].get_center())

        wanhap.move_to(j[0])
        l_int2.move_to(j[1])
        l_frac4.set_color(GREEN)

        self.play(TransformInStages.from_copy(du_rhs[0], wanhap.denominator, run_time=1.5))
        self.play(
            LaggedStart(
                Write(
                    VGroup(wanhap.numerator, wanhap.vinculum), **rt
                ),
                Write(integ, **rt),
                lag_ratio=0.2
            )       
        )

        tu_cancel = Line(du_rhs[0].get_corner(DL), du_rhs[0].get_corner(UR), color=RED)

        self.play(Write(tu_cancel), **rt)

        du_copy = du_eq[0].copy()
        u_copy = u_eq[0].copy()

        self.play(
            LaggedStart(
                AnimationGroup(
                    u_copy.animate.move_to(l_frac4.denominator), 
                    du_copy.animate.move_to(l_frac4.numerator),
                    **rt
                ), 
                Write(l_frac4.vinculum),
                lag_ratio=0.9
            )
        )
        # i mean ts works

        # self.play(Write(VGroup(j[0], j[1]))) 

        # we need to do this first para ma-align yung equal sign
        eq_pos = rhs2[0].get_center()            

        j = MathTex(wanhap, l_int2, rhs2)
        j.shift(eq_pos - j[2][0].get_center())   

        self.remove(du_copy, u_copy)             
        self.add(j)

        # ---------  Anim11  --------- 
        lnu = Function(ln, u)
        wanhap = wanhap.copy()
        rhs2 = rhs2.copy()

        k = MathTex(wanhap, lnu, rhs2).next_to(j, DOWN, buff=0.8)
        self.play(TransformInStages.from_copy(j, k), **rt)

          
        self.wait()

        # I should just stop here and now show the integration part at all
