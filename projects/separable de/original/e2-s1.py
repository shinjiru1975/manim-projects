from manim import *
from reactive_manim import *

class Scene1Attempt1(Scene):
    def construct(self):
        
        x, y1, y2, wan, tu, z, p, min, eq, dy, dx, sp = MathTex("x", "y", "y", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ")

        dy.set_color(YELLOW)
        dx.set_color(BLUE)

        rt = {"run_time":1.5}

        # ---------  AnimA1  --------- 
        paren = Parentheses([y1, p, wan])

        a = MathTex(tu, x, paren, sp, dx, min, y2, sp, dy, eq, z).to_edge(UP).shift(DOWN * 0.4)

        self.play(Write(a), **rt)

        # ---------  AnimA2  --------- 
        def phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex("x", "=", "1", ",", "y", "=", "0", ";")
        
        conditions = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)
        conditions_ph = phantom(conditions)
        
        a1 = MathTex(tu, x, paren, sp, dx, min, y2, sp, dy, eq, z, conditions_ph).move_to(a); 
        conditions.move_to(conditions_ph)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(a, a1, **rt),
                Write(conditions, **rt),
                lag_ratio=0.6
            )
        )

        self.play(
            x.animate.set_color(BLUE),
            y1.animate.set_color(YELLOW),
            y2.animate.set_color(YELLOW),
            run_time=1.5
        )

        # ---------  AnimB  --------- 
        paren = Parentheses([y1, p, wan], paren=a1[2].paren)

        b = MathTex(tu, x, paren, sp, dx, eq, y2, sp, dy).next_to(a1, DOWN, buff=0.9)
        a_copy = a1.copy().move_to(b).shift(RIGHT * 1.75)
        
        self.play(TransformFromCopy(a1, a_copy, **rt))
        self.play(TransformInStages.replacement_transform(a_copy, b, **rt))

        # ---------  AnimC1  --------- 
        l_frac = Fraction([tu, x, paren], paren)

        c1 = MathTex(l_frac, sp, dx, eq, y2, sp, dy).move_to(b)

        self.play(TransformInStages.replacement_transform(b, c1, **rt))

        # ---------  AnimC2  --------- 
        r_frac = Fraction(y2, paren)

        c2 = MathTex([l_frac], sp, dx, eq, r_frac, sp, dy).move_to(c1)

        self.play(TransformInStages.replacement_transform(c1, c2, **rt))

        # ---------  AnimC3  --------- 
        l_cancel_num = Line(
            c2[0][0].numerator[2].get_corner(DL), 
            c2[0][0].numerator[2].get_corner(UR), 
            color=RED
        )
        l_cancel_den = Line(
            c2[0][0].denominator.get_corner(DL), 
            c2[0][0].denominator.get_corner(UR), 
            color=RED
        )

        self.play(
            Create(l_cancel_num),
            Create(l_cancel_den),
            run_time=1.5
        )

        # ---------  AnimD  --------- 
        d = MathTex(tu, x, sp, dx, eq, r_frac, sp, dy).next_to(c2, DOWN, buff=0.75); eq.save_y

        self.play(TransformInStages.from_copy(c2, d, **rt))

        # ---------  AnimE  --------- 
        int = MathTex(r"\int")
        l_int = MathTex(int, tu, x, sp, dx)
        r_int = MathTex(int, r_frac, sp, dy)

        e = MathTex(l_int, eq, r_int).move_to(d); eq.restore_y

        self.play(TransformInStages.replacement_transform(d, e, **rt))

        # ---------  AnimF  --------- 
        ans = MathTex(Term(x, tu), eq, y2, min, Function(r"\ln", [y2, p, wan]), p, "C")
        arrow = MathTex(sp, r"\rightarrow", sp)
        ans_ph = phantom(ans)
        arrow_ph = phantom(arrow)

        f = MathTex([l_int, eq, r_int], arrow_ph, ans_ph).move_to(e)

        ans.move_to(ans_ph)
        arrow.move_to(arrow_ph)

        box = SurroundingRectangle(ans, color=LIGHT_PINK, buff=0.2).move_to(ans)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(e, f, **rt),
                Write(arrow, **rt),
                Write(ans, **rt),
                Write(box, **rt),
                lag_ratio=0.5
            )
        )

        # ---------  AnimG  --------- 
        conditions2 = MathTex(x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con).to_edge(UP).shift(DOWN * 0.4)
        
        keep = [conditions, conditions2, ans]

        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in keep])

        self.play(
                AnimationGroup(
                    ans.animate.next_to(conditions2, DOWN, buff=0.5),
                    TransformInStages.replacement_transform(conditions, conditions2, **rt),

                )
                 
   

                
                # *[FadeOut(mob) for mob in self.mobjects if mob not in keep],
                

            
        )

        # self.play(

        #         AnimationGroup(
        #             TransformInStages.replacement_transform(conditions, conditions2, **rt), 
        #             ans.animate.next_to(conditions2, DOWN, buff=0.5),
        #             **rt
        #         ),
        #         *[FadeOut(mob) for mob in self.mobjects], 
        #         **rt,
        #         lag_ratio=0.5
            
        # )

        self.wait()

class Scene1Attempt2(Scene):
    def construct(self):
        
        x, y1, y2, wan, tu, z, p, min, eq, dy, dx, sp = MathTex("x", "y", "y", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ")

        dy.set_color(YELLOW)
        dx.set_color(BLUE)

        rt = {"run_time":1.5}

        # ---------  AnimA1  --------- 
        paren = Parentheses([y1, p, wan])

        a = MathTex(tu, x, paren, sp, dx, min, y2, sp, dy, eq, z).to_edge(UP).shift(DOWN * 0.4)

        self.play(Write(a), **rt)

        # ---------  AnimA2  --------- 
        def phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex("x", "=", "1", ",", "y", "=", "0", ";")
        
        x_con.set_color(BLUE)
        y_con.set_color(YELLOW)
        
        conditions = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)
        conditions_ph = phantom(conditions)
        
        a1 = MathTex(tu, x, paren, sp, dx, min, y2, sp, dy, eq, z, conditions_ph).move_to(a); 
        conditions.move_to(conditions_ph)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(a, a1, **rt),
                Write(conditions, **rt),
                lag_ratio=0.6
            )
        )

        self.play(
            x.animate.set_color(BLUE),
            y1.animate.set_color(YELLOW),
            y2.animate.set_color(YELLOW),
            run_time=1.5
        )

        # ---------  AnimB  --------- 
        paren = Parentheses([y1, p, wan], paren=a1[2].paren)

        b = MathTex(tu, x, paren, sp, dx, eq, y2, sp, dy).next_to(a1, DOWN, buff=0.9)
        a_copy = a1.copy().move_to(b).shift(RIGHT * 1.75)
        
        self.play(TransformFromCopy(a1, a_copy, **rt))
        self.play(TransformInStages.replacement_transform(a_copy, b, **rt))

        # ---------  AnimC1  --------- 
        l_frac = Fraction([tu, x, paren], paren)

        c1 = MathTex(l_frac, sp, dx, eq, y2, sp, dy).move_to(b)

        self.play(TransformInStages.replacement_transform(b, c1, **rt))

        # ---------  AnimC2  --------- 
        r_frac = Fraction(y2, paren)

        c2 = MathTex([l_frac], sp, dx, eq, r_frac, sp, dy).move_to(c1)

        self.play(TransformInStages.replacement_transform(c1, c2, **rt))

        # ---------  AnimC3  --------- 
        l_cancel_num = Line(
            c2[0][0].numerator[2].get_corner(DL), 
            c2[0][0].numerator[2].get_corner(UR), 
            color=RED
        )
        l_cancel_den = Line(
            c2[0][0].denominator.get_corner(DL), 
            c2[0][0].denominator.get_corner(UR), 
            color=RED
        )

        self.play(
            Create(l_cancel_num),
            Create(l_cancel_den),
            run_time=1.5
        )

        # ---------  AnimD  --------- 
        d = MathTex(tu, x, sp, dx, eq, r_frac, sp, dy).next_to(c2, DOWN, buff=0.75); eq.save_y()

        self.play(TransformInStages.from_copy(c2, d, **rt))

        # ---------  AnimE  --------- 
        int = MathTex(r"\int")
        l_int = MathTex(int, tu, x, sp, dx)
        r_int = MathTex(int, r_frac, sp, dy)

        e = MathTex(l_int, eq, r_int).move_to(d); eq.restore_y()

        self.play(TransformInStages.replacement_transform(d, e, **rt))

        # ---------  AnimF  --------- 
        ans = MathTex(Term(x, tu), eq, y2, min, Function(r"\ln", [y2, p, wan]), p, "C")
        arrow = MathTex(sp, r"\rightarrow", sp)
        ans_ph = phantom(ans)
        arrow_ph = phantom(arrow)

        f = MathTex([l_int, eq, r_int], arrow_ph, ans_ph).move_to(e)

        ans.move_to(ans_ph)
        arrow.move_to(arrow_ph)

        box = SurroundingRectangle(ans, color=LIGHT_PINK, buff=0.2).move_to(ans)

        self.play(
            LaggedStart(
                TransformInStages.replacement_transform(e, f, **rt),
                Write(arrow, **rt),
                Write(ans, **rt),
                Write(box, **rt),
                lag_ratio=0.5
            )
        )

        gensol = Text("general solution", font="LMRoman10").next_to(ans, DOWN, buff=0.4).scale(0.8)
        self.play(DrawBorderThenFill(gensol), **rt)

        # ---------  AnimG  --------- 
        g_ans_ph = phantom(ans)
        g_cond_ph = phantom(conditions)

        g = MathTex(g_ans_ph, g_cond_ph).move_to(a1)

        keep = [ans, conditions, box]
        fade = [m for m in self.mobjects if m not in keep]

        self.play(
            ans.animate.move_to(g_ans_ph),
            box.animate.move_to(g_ans_ph).set_opacity(0),   
            conditions.animate.move_to(g_cond_ph),
            *[FadeOut(m) for m in fade],
            **rt
        )
        
        self.remove(box)

        self.wait()