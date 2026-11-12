from manim import *
from reactive_manim import *

class Scene2Attempt1(Scene):
    def construct(self):
        
        x, y1, y2, wan, tu, z, p, min, eq, dy, dx, sp = MathTex("x", "y", "y", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ")

        x.set_color(BLUE),
        y1.set_color(YELLOW),
        y2.set_color(YELLOW),

        dy.set_color(YELLOW)
        dx.set_color(BLUE)

        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex("x", "=", "1", ",", "y", "=", "0", ";")
        
        x_con.set_color(BLUE)
        y_con.set_color(YELLOW)

        rt = {"run_time":1.5}

        ans = MathTex(Term(x, tu), eq, y2, min, Function(r"\ln", [y2, p, wan]), p, "C")
        conds = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)

        def phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        g_ans_ph = phantom(ans)
        g_cond_ph = phantom(conds)

        g = MathTex(g_ans_ph, g_cond_ph).to_edge(UP).shift(DOWN * 0.4)
        ans.move_to(g_ans_ph)
        conds.move_to(g_cond_ph)

        self.add(ans)
        self.add(conds)

        g = MathTex(ans, conds).to_edge(UP).shift(DOWN * 0.4)

        ans_copy = ans.copy().next_to(g, DOWN, buff=0.9)

        self.play(TransformFromCopy(ans, ans_copy), **rt)

        # ---------  AnimH  --------- 
        wan_con_ph = phantom(wan_con)
        x_sub = Term(wan_con_ph, tu, paren=True)

        h = MathTex(x_sub, g[0][1:7]).move_to(ans_copy)

        wan_con_target = wan_con_ph.get_center().copy()   # frozen numpy point

        wan_con_copy = wan_con.copy()

        self.play(
            TransformInStages.replacement_transform(ans_copy, h, **rt),
            wan_con_copy.animate.move_to(wan_con_target).set_color(BLUE),
            **rt
        )

        self.remove(h)
        self.remove(wan_con_copy)
        x_sub = Term(wan_con_copy, tu, paren=True)
        h1 = MathTex(x_sub, g[0][1:7]).move_to(h)
        self.add(h1)

        # ---------  AnimI  ---------
        z_con_ph = phantom(z_con)
        y_sub = Parentheses(z_con_ph)
          
        i = MathTex(x_sub, eq, y_sub, min, Function(r"\ln", [y_sub, p, wan]), p, "C").move_to(h)

        self.play(TransformInStages.replacement_transform(h, i, **rt))

        self.wait()

class Scene2Attempt2(Scene):
    def construct(self):
        
        x, y1, y2, wan, tu, z, p, min, eq, dy, dx, sp = MathTex("x", "y", "y", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ")

        x.set_color(BLUE),
        y1.set_color(YELLOW),
        y2.set_color(YELLOW),

        dy.set_color(YELLOW)
        dx.set_color(BLUE)

        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex("x", "=", "1", ",", "y", "=", "0", ";")
        
        x_con.set_color(BLUE)
        y_con.set_color(YELLOW)

        rt = {"run_time":1.5}

        ans = MathTex(Term(x, tu), eq, y2, min, Function(r"\ln", [y2, p, wan]), p, "C")
        conds = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)

        def phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        g = MathTex(ans, conds).to_edge(UP).shift(DOWN * 0.4)

        self.add(g)

        ans_copy = ans.copy().next_to(g, DOWN, buff=0.9)

        self.play(TransformFromCopy(ans, ans_copy), **rt)

        # ---------  AnimH  --------- 
        x_sub = Term(wan_con, tu, paren=True)

        h = MathTex(x_sub, g[0][1:7]).move_to(ans_copy)

        self.play(
            TransformInStages.from_copy(g[1][5], h, **rt),
            wan_con.animate.set_color(BLUE),
            **rt
        )

        # ---------  AnimI  ---------
        # z_con_ph = phantom(z_con)
        # y_sub = Parentheses(z_con_ph)
          
        # i = MathTex(x_sub, eq, y_sub, min, Function(r"\ln", [y_sub, p, wan]), p, "C").move_to(h)

        # self.play(TransformInStages.replacement_transform(h, i, **rt))

        self.wait()

class Scene2Attempt3(Scene):
    def construct(self):
        
        x, y1, y2, wan, tu, z, p, min, eq, dy, dx, sp = MathTex("x", "y", "y", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ")

        x.set_color(BLUE),
        y1.set_color(YELLOW),
        y2.set_color(YELLOW),

        dy.set_color(YELLOW)
        dx.set_color(BLUE)

        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex("x", "=", "1", ",", "y", "=", "0", ";")
        
        x_con.set_color(BLUE)
        y_con.set_color(YELLOW)

        rt = {"run_time":1.5}

        ans = MathTex(Term(x, tu), eq, y2, min, Function(r"\ln", [y2, p, wan]), p, "C")
        conds = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)

        def phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        g_ans_ph = phantom(ans)
        g_cond_ph = phantom(conds)

        g = MathTex(g_ans_ph, g_cond_ph).to_edge(UP).shift(DOWN * 0.4)
        ans.move_to(g_ans_ph)
        conds.move_to(g_cond_ph)

        self.add(ans)
        self.add(conds)

        g = MathTex(ans, conds).to_edge(UP).shift(DOWN * 0.4)

        ans_copy = ans.copy().next_to(g, DOWN, buff=0.9)

        self.play(TransformFromCopy(ans, ans_copy), **rt)

        # ---------  AnimH  --------- 
        def substitute(old, build, sources, color=None, **rt):
            """
            old     : solid equation currently on screen
            build   : fn(slot_contents) -> equation; MUST build fresh pieces on each call
            sources : mobjects whose values fly in (repeat one for several slots)
            """
            ghosts  = [phantom(s) for s in sources]
            new_ph  = build(ghosts).move_to(old)
            targets = [g.get_center().copy() for g in ghosts]   # read after layout, frozen
            fliers  = [s.copy() for s in sources]

            moves = [
                f.animate.move_to(t).set_color(color) if color is not None
                else f.animate.move_to(t)
                for f, t in zip(fliers, targets)
            ]
            self.play(
                TransformInStages.replacement_transform(old, new_ph, **rt),
                *moves,
                **rt
            )

            solid = build(fliers).move_to(new_ph)    # fliers become the real glyphs
            self.remove(new_ph, *fliers)
            self.add(solid)
            return solid                              # always continue from this
        
        # ---------  AnimH  --------- 
        h = self.substitute(
            ans_copy,
            lambda f: MathTex(Term(f[0], tu.copy(), paren=True), g[0][1:7].copy()),
            [wan_con], color=BLUE, **rt
        )

        # ---------  AnimI  --------- 
        i = self.substitute(
            h,
            lambda f: MathTex(
                h[0].copy(), eq.copy(),
                Parentheses(f[0]), min.copy(),
                Function(r"\ln", [Parentheses(f[1]), p.copy(), wan.copy()]),
                p.copy(), "C"
            ),
            [z_con, z_con], color=YELLOW, **rt
        )

class Scene2Attempt4(Scene):
    def construct(self):
        
        x, y1, y2, wan, tu, z, p, min, eq, dy, dx, sp, C = MathTex("x", "y", "y", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ", "C")

        x.set_color(BLUE),
        y1.set_color(YELLOW),
        y2.set_color(YELLOW),

        dy.set_color(YELLOW)
        dx.set_color(BLUE)

        x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex("x", "=", "1", ",", "y", "=", "0", ";")
        
        x_con.set_color(BLUE)
        y_con.set_color(YELLOW)
        
        C.set_color(GREEN)

        rt = {"run_time":1.5}

        ln1 = Function(r"\ln", [y2, p, wan])
        ans = MathTex(Term(x, tu), eq, y2, min, ln1, p, C)
        conds = MathTex(sp, semi, sp, x_con, eq1_con, wan_con, comma, sp, y_con, eq2_con, z_con)

        def phantom(term):
            return term.clone().clear_tracking().set_opacity(0)
        
        g_ans_ph = phantom(ans)
        g_cond_ph = phantom(conds)

        g = MathTex(g_ans_ph, g_cond_ph).to_edge(UP).shift(DOWN * 0.4)
        ans.move_to(g_ans_ph)
        conds.move_to(g_cond_ph)

        self.add(ans)
        self.add(conds)

        g = MathTex(ans, conds).to_edge(UP).shift(DOWN * 0.4)

        ans_copy = ans.copy().next_to(g, DOWN, buff=0.8)

        self.play(TransformFromCopy(ans, ans_copy), **rt)

        # ---------  AnimH  --------- 
        wan_con_ph = phantom(wan_con)
        x_sub = Term(wan_con_ph, tu, paren=True)

        h = MathTex(x_sub, g[0][1:7]).move_to(ans_copy)

        wan_con_target = x_sub.term.get_center().copy()   
        wan_con_copy = wan_con.copy()

        self.play(
            TransformInStages.replacement_transform(ans_copy, h, **rt),
            wan_con_copy.animate.move_to(wan_con_target).set_color(BLUE),
            **rt
        )

        self.remove(h)
        self.remove(wan_con_copy)
        x_sub = Term(wan_con_copy, tu, paren=True)
        h1 = MathTex(x_sub, g[0][1:7]).move_to(h)
        self.add(h1)

        # ---------  AnimI  ---------
        def dump(m, name="", depth=0, max_depth=3):
            pad = "  " * depth
            keys = sorted(vars(m).keys())
            track = {k: getattr(m, k) for k in keys
                    if any(s in k.lower() for s in ("track", "id", "key", "tag"))}
            print(f"{pad}{name} <{type(m).__name__}> obj_id={id(m)} "
                f"center={m.get_center().round(3)} track={track}")
            if depth < max_depth:
                for i, sm in enumerate(m.submobjects):
                    dump(sm, f"[{i}]", depth + 1, max_depth)

        z_con_ph = phantom(z_con)
        y_sub1 = Parentheses(z_con_ph)
        y_sub2 = Parentheses(z_con_ph)
        
        ln2 = Function(ln1.function, [y_sub2, p, wan], paren=ln1.paren)

        i = MathTex(x_sub, eq, y_sub1, min, ln2, g[0][5:7]).move_to(h)

        z_con_target1 = y_sub1.input.get_center().copy()
        z_con_target2 = y_sub2.input.get_center().copy()
        z_con_copy1 = z_con.copy()
        z_con_copy2 = z_con.copy()

        print("===== MANUAL OLD (h1) =====")
        dump(h1, "h1")
        print("===== MANUAL NEW (i) =====")
        dump(i, "i")
        print("same x_sub in both?", h1[0] is i[0])

        self.play(
            TransformInStages.replacement_transform(h1, i, **rt),
            z_con_copy1.animate.move_to(z_con_target1).set_color(YELLOW),
            z_con_copy2.animate.move_to(z_con_target2).set_color(YELLOW),
            **rt
        )

        self.remove(i)
        self.remove(z_con_copy1)
        self.remove(z_con_copy2)
        y_sub1 = Parentheses(z_con_copy1)
        y_sub2 = Parentheses(z_con_copy2)
        ln2 = Function(ln1.function, [y_sub2, p, wan], paren=ln1.paren)
        i1 = MathTex(x_sub, eq, y_sub1, min, ln2, g[0][5:7]).move_to(h)
        self.add(i1)

        # ---------  AnimJ  ---------
        j = MathTex(ans[6], ans[1], wan_con_copy).next_to(i1, DOWN, buff=0.4)
        j[2].set_color(GREEN)

        self.play(
            TransformInStages.from_copy(i1, j, **rt),
        )

        # ---------  AnimK  ---------
        ans_copy2 = ans.copy().next_to(j, DOWN, buff=0.8)
        self.play(TransformFromCopy(ans, ans_copy2), **rt)

        wan_con_copy_ph = phantom(wan_con_copy)
        C_sub = MathTex(wan_con_copy_ph)

        k = MathTex(ans[0:6], C_sub).move_to(ans_copy2)

        wan_con_copy_target = C_sub.get_center().copy()
        wan_con_copy2 = wan_con_copy.copy()

        box = SurroundingRectangle(k, color=LIGHT_PINK, buff=0.2).move_to(k)

        self.play(
            TransformInStages.replacement_transform(ans_copy2, k, **rt),
            LaggedStart(
                wan_con_copy2.animate.move_to(wan_con_copy_target),
                Write(box, **rt,),
                lag_ratio=0.7,
            )
        )

        parsol = Text("particular solution", font="LMRoman10").next_to(k, DOWN, buff=0.4).scale(0.7)
        self.play(DrawBorderThenFill(parsol), **rt)

        self.wait()