from manim import *
from common import *
from symbols import *
from reactive_manim import *   

class Example2Scene2(DEScene):
    def construct(self):
        
        x, y1, y2, yp, wan, tu, z, p, mn, eq, dy, dx, sp, C, integ = make_symbols()
        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = make_conditions()

        C.set_color(CONST_COLOR)
        
        ln1 = Function(r"\ln", [y2, p, wan])
        ans = MathTex(
            Term(x, tu), 
            eq, 
            y2, mn, ln1, p, C
        )
        conds = MathTex(
            sp, semi, sp, 
            x_con, eq1_con, wan_con, 
            comma, sp, 
            y_con, eq2_con, z_con
        )

        g_ans_ph = phantom(ans)
        g_cond_ph = phantom(conds)

        g = pin_top(
            MathTex(
                g_ans_ph, 
                g_cond_ph
        ))

        ans.move_to(g_ans_ph)
        conds.move_to(g_cond_ph)

        self.add(ans)
        self.add(conds)

        g = pin_top(
            MathTex(
                ans, conds
        ))

        ans_copy = ans.copy().next_to(g, DOWN, buff=0.8)

        self.play(TransformFromCopy(ans, ans_copy), **RT)

        # ---------  AnimH: x = 1 flies into x^2  ---------
        # used self.substitute helper
        h, h_parts = self.substitute(
            ans_copy,
            lambda f: [Term(f[0], tu, paren=True), g[0][1:7]],
            [wan_con], color=X_COLOR
        )
        
        #  ---------  AnimI: y = 0 flies into both y's  ---------
        i, i_parts = self.substitute(
            h,
            lambda f: [
                h_parts[0], eq, Parentheses(f[0]), mn,
                Function(ln1.function, [Parentheses(f[1]), p, wan], paren=ln1.paren),
                g[0][5:7]
            ],
            [z_con, z_con], color=Y_COLOR
        )

        # ---------  AnimJ:solve for C  ---------
        self.play(  
            Create(cancel_slash(i[2:5])),
            **RT,
        )

        wan_con_copy = wan_con.copy()

        j = MathTex(
            ans[6], ans[1], wan_con
        ).next_to(i, DOWN, buff=0.4)

        j[2].set_color(CONST_COLOR)

        self.derive(i, j)

        # ---------  AnimK: put C back -> particular solution  ---------
        ans_copy2 = ans.copy().next_to(j, DOWN, buff=0.8)

        self.play(TransformFromCopy(ans, ans_copy2), **RT)

        wan_con_ph = phantom(wan_con)
        C_sub = MathTex(wan_con_ph)

        k = MathTex(
            ans[0:6], C_sub
        ).move_to(ans_copy2)

        wan_con_target = C_sub.get_center().copy()
        wan_con_copy = wan_con.copy()

        box = answer_box(k)

        self.play(
            TransformInStages.replacement_transform(ans_copy2, k, **RT),
            LaggedStart(
                wan_con_copy.animate.move_to(wan_con_target),
                Write(box, **RT),
                lag_ratio=0.7,
            ),
        )

        self.caption("particular solution", k)

        self.wait()