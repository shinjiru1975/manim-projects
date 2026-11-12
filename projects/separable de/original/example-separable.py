from manim import *

# Attempt 1: pwede na
class Separable1(Scene):
    def construct(self):

        a = MathTex("xyy'=1+y^2")
        b = MathTex("\\frac{xyy'}{x}=1+y^2")
        c = MathTex("\\frac{xyy'}{x}=\\frac{1+y^2}{x}")
        d = MathTex("\\frac{xyy'}{x}=\\frac{1+y^2}{x(1+y^2)}")
        e = MathTex("\\frac{xyy'}{x(1+y^2)}=\\frac{1+y^2}{x(1+y^2)}")

        a.to_edge(UP)
        b.next_to(a, DOWN)
        c.next_to(b, DOWN)
        d.next_to(c, DOWN)
        e.next_to(d, DOWN)

        self.play(Write(a), run_time=1.5)
        self.play(TransformFromCopy(a, b), run_time=1.5) 
        self.play(TransformFromCopy(b, c), run_time=1.5)
        self.play(TransformFromCopy(c, d), run_time=1.5)
        self.play(TransformFromCopy(d, e), run_time=1.5)

# Attempt 2: mas pagagandahin (fail)
class Separable2(Scene):
    def construct(self):

        Term("x", "y", "y'")
        x, y, yp = MathTex("x", "y", "y'")
        
        x.set_color(GREEN) 
        y.set_color(RED)

# Attempt 3: mas maganda pa
class Separable3(Scene):
    def construct(self):

        a = MathTex(r"{{xyy'}} {{=}} {{1+y^2}}")
        b = MathTex(r"\frac{ {{xyy'}} }{x} {{=}} {{1+y^2}}")
        c = MathTex(r"\frac{ {{xyy'}} }{x} {{=}} \frac{ {{1+y^2}} }{x}")

        a.to_edge(UP)
        b.next_to(a, DOWN, buff=0.5)
        c.next_to(b, DOWN, buff=0.5)

        print("BEFORE Write:", type(a).__name__)
        print("BEFORE subobjects:",
            [(type(s).__name__, getattr(s, "tex_string", None))
            for s in a.submobjects])

        self.play(Write(a), run_time=1.5)

        print("AFTER Write:", type(a).__name__)
        print("AFTER subobjects:",
            [(type(s).__name__, getattr(s, "tex_string", None))
            for s in a.submobjects])

        self.play(TransformMatchingTex(a.copy(), b), run_time=1.5)
        self.play(TransformMatchingTex(b.copy(), c), run_time=1.5)
        self.wait()

class CleanMatchingTest(Scene):
    def construct(self):
        first = MathTex(r"{{x}}^2 + {{y}}^2")
        second = MathTex(r"{{a}}^2 + {{b}}^2")

        self.play(Write(first))
        self.wait(0.5)
        self.play(TransformMatchingTex(first, second))
        self.wait()

# Attempt 4: mas lalo pang gumanda
class Separable4(Scene):
    def construct(self):
        a = MathTex(r"{{xyy'}} {{=}} {{1+y^2}}")
        b = MathTex(r"\frac{ {{xyy'}} }{x} {{=}} {{1+y^2}}")
        c = MathTex(r"\frac{ {{xyy'}} }{x} {{=}} \frac{ {{1+y^2}} }{x}")

        a.to_edge(UP)
        b.next_to(a, DOWN, buff=0.5)
        c.next_to(b, DOWN, buff=0.5)

        # Eq1
        self.play(Write(a), run_time=1.5)

        # Eq2
        a_copy = a.copy()
        a_copy.move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(a_copy, b),
            run_time=1.5
        )

        # Eq3
        b_copy = b.copy()
        b_copy.move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(b_copy, c),
            run_time=1.5
        )

        self.wait()

# Attempt 5: gah damn ang ganda
class Separable5(Scene):
    def construct(self):
        a = MathTex(r"{{xyy'}} {{=}} {{1+y^2}}")
        b = MathTex(r"{{xy}} {{\frac{dy}{dx}}} {{=}} {{1+y^2}}")
        c = MathTex(r"{{(dx)}} \ {{xy}} {{\frac{dy}{dx}}} {{=}} {{1+y^2}} \ {{(dx)}}")

        a.to_edge(UP)
        b.next_to(a, DOWN, buff=0.5)
        c.next_to(b, DOWN, buff=0.5)

        # Eq1
        self.play(Write(a), run_time=1.5)

        # Eq2
        a_copy = a.copy()
        a_copy.move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(a_copy, b),
            run_time=1.5
        )

        # Eq3
        b_copy = b.copy()
        b_copy.move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(b_copy, c),
            run_time=1.5
        )

        self.wait()

# Attempt 6: ang ganda neto, kaso parang verbose yung may napakaraming MathTex at makalat na grouping
class Separable6(Scene):
    def construct(self):
        a = MathTex(r"{{xyy'}} {{=}} {{1+y^2}}")
        b = VGroup(
            MathTex("xy"),
            MathTex(r"\frac{dy}{dx}"),
            MathTex("="),
            MathTex(r"1+y^2"),
        ).arrange(RIGHT, buff=0.2)

        c = VGroup(
            MathTex(r"(dx)"),
            MathTex("xy"),
            MathTex(r"\frac{dy}{dx}"),
            MathTex("="),
            MathTex(r"1+y^2"),
            MathTex(r"(dx)"),
        ).arrange(RIGHT, buff=0.2)

        a.to_edge(UP)
        b.next_to(a, DOWN, buff=0.5)
        c.next_to(b, DOWN, buff=0.5)

        # Eq1
        self.play(Write(a), run_time=1.5)

        # Eq2
        a_copy = a.copy()
        a_copy.move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(a_copy, b),
            run_time=1.5
        )

        # Eq3
        b_copy = b.copy()
        b_copy.move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        # Group only the existing terms of equation c
        c_existing = VGroup(c[1], c[2], c[3], c[4])

        # Transform matching terms and write the two new dx terms
        self.play(
            TransformMatchingTex(b_copy, c_existing),
            Write(c[0]),
            Write(c[5]),
            run_time=1.5
        )

# Attempt 7: ang ganda na gagi at malinis na
class Separable7(Scene):
    def construct(self):
        a = MathTex("xyy'", "=", "1+y^2")
        b = MathTex("xy\ ", r"\frac{dy}{dx}", "=", "1+y^2")
        c = MathTex("(dx)\ ", "xy\ ", r"\frac{dy}{dx}", "=", "1+y^2", "\ (dx)")

        a.to_edge(UP)
        b.next_to(a, DOWN, buff=0.5)
        c.next_to(b, DOWN, buff=0.5)

        # Eq1
        self.play(Write(a), run_time=1.5)

        # Eq2
        a_copy = a.copy()
        a_copy.move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            AnimationGroup(
                TransformMatchingTex(a_copy, b),
                Write(b[1]),
                run_time=1.5,
                lag_ratio=0
            )
        )

        # Eq3
        b_copy = b.copy()
        b_copy.move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            Write(c[0]),
            Write(c[5]),
            run_time=1.5
        )

        self.wait()

# Attempt 8: subukan naitng mas linisin pa
    # dito ko natutuhan kung paano mas hatiin pa yung substring ng rational functions para sa cancellation
    # normally kasi "\frac{dy}{dx}" yon, and hindi mo mapaghihiwalay yung numerator at denominator
    # so napaghiwalay na siya sa Line 301
    # it already looks so good, i made it look like how i wanted it to look
class Separable8(Scene):
    def construct(self):
        
        # Anim1
        a = MathTex("xy", "y'", "=", "1+y^2").to_edge(UP)
        
        self.play(Write(a), run_time=1.5)

        # Anim2
        b = MathTex("xy\ ", r"\frac{", "dy", r"}{", "dx", r"}", "=", "1+y^2").next_to(a, DOWN, buff=0.5)
        a_copy = a.copy().move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        # bagong natutuhan: Indicate
        self.play(
            Indicate(a_copy[1], color=YELLOW, scale_factor=1.5, run_time=1.5)
        )

        # defined dy and dx fraction to have different colors grouped them with differential
        differential = VGroup(b[2].set_color(YELLOW), b[3], b[4].set_color(BLUE)) 
        self.play(
            TransformMatchingTex(a_copy, b),
            Write(differential), 
            run_time=1.5,
        )

        # Anim3
        c = MathTex("(", "dx", ")\ ", "xy\ ", r"\frac{", "dy", r"}{", "dx", r"}", "=", "1+y^2", "\ (", "dx", ")").next_to(b, DOWN, buff=0.5)
        c[1].set_color(BLUE)
        c[12].set_color(BLUE)
        b_copy = b.copy().move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            Write(c[0:3]),
            Write(c[11:14])
        )

        self.play(
            Create(
                Line(
                    c[1].get_corner(DL), c[1].get_corner(UR), color=RED
                )
            ),
            Create(
                Line(
                    c[7].get_corner(DL), c[7].get_corner(UR), color=RED
                )
            )
        )
        self.wait()

# Attempt 9: maganda din to, kaso hindi smooth yung transition ng dx
class Separable9(Scene):
    def construct(self):
        
        # Anim1
        a = MathTex("xy", "y'", "=", "1+y^2").to_edge(UP)
        
        self.play(Write(a), run_time=1.5)

        # Anim2
        b = MathTex("xy\ ", r"\frac{", "dy", r"}{", "dx", r"}", "=", "1+y^2").next_to(a, DOWN, buff=0.5)
        a_copy = a.copy().move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            Indicate(a_copy[1], color=YELLOW, scale_factor=1.5, run_time=1.5)
        )

        differential = VGroup(b[2].set_color(YELLOW), b[3], b[4].set_color(BLUE)) 
        self.play(
            TransformMatchingTex(a_copy, b),
            Write(differential), 
            run_time=1.5,
        )

        # Anim3
        c = MathTex("(", "dx", ")\ ", "xy\ ", r"\frac{", "dy", r"}{", "dx", r"}", "=", "1+y^2", "\ (", "dx", ")").next_to(b, DOWN, buff=0.5)
        c[1].set_color(BLUE)
        c[12].set_color(BLUE)
        b_copy = b.copy().move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            Write(c[0:3]),
            Write(c[11:14])
        )

        left_cancel = Line(c[1].get_corner(DL), c[1].get_corner(UR), color=RED)
        right_cancel = Line(c[7].get_corner(DL), c[7].get_corner(UR), color=RED)

        self.play(Write(left_cancel), Write(right_cancel))

        # Anim4
        d = MathTex("xy", "\ ", "dy", "=", "(", "1+y^2", ")", "\ ", "dx").next_to(c, DOWN, buff=0.5)
        d[2].set_color(YELLOW)
        d[8].set_color(BLUE)
        c_copy = c.copy().move_to(d)

        cancelled = VGroup(c_copy, c[0:3], c[11:14], left_cancel, right_cancel)

        self.play(
            TransformFromCopy(c, c_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(c_copy, d),
            run_time=1.5
        )

        self.wait()

# Attempt 12: copied from Separable 9, no more reactive manim for now
# susubukan na bigyan ng values yung mga terms sa halip na raw values gaya ng sa Separable11
class Separable12(Scene):
    def construct(self):
        
        # Anim1
        a = MathTex("xy", "y'", "=", "1+y^2").to_edge(UP)
        
        self.play(Write(a), run_time=1.5)

        # Anim2
        b = MathTex("xy\ ", r"\frac{", "dy", r"}{", "dx", r"}", "=", "1+y^2").next_to(a, DOWN, buff=0.5)
        a_copy = a.copy().move_to(b)

        self.play(
            TransformFromCopy(a, a_copy),
            run_time=1.5
        )

        self.play(
            Indicate(a_copy[1], color=YELLOW, scale_factor=1.5, run_time=1.5)
        )

        differential = VGroup(b[2].set_color(YELLOW), b[3], b[4].set_color(BLUE)) 
        self.play(
            TransformMatchingTex(a_copy, b),
            Write(differential), 
            run_time=1.5,
        )

        # Anim3
        dx1 = MathTex("dx")
        dx2 = MathTex("dx")
        c = MathTex("(", dx1, ")\ ", "xy\ ", r"\frac{", "dy", r"}{", "dx", r"}", "=", "1+y^2", "\ (", dx2, ")").next_to(b, DOWN, buff=0.5)
        c[1].set_color(BLUE)
        c[12].set_color(BLUE)
        b_copy = b.copy().move_to(c)

        self.play(
            TransformFromCopy(b, b_copy),
            run_time=1.5
        )

        self.play(
            Write(c[0:3]),
            Write(c[11:14])
        )

        left_cancel = Line(c[1].get_corner(DL), c[1].get_corner(UR), color=RED)
        right_cancel = Line(c[7].get_corner(DL), c[7].get_corner(UR), color=RED)

        self.play(Write(left_cancel), Write(right_cancel))

        # Anim4
        d = MathTex("xy", "\ ", "dy", "=", "(", "1+y^2", ")", "\ ", "dx").next_to(c, DOWN, buff=0.5)
        d[2].set_color(YELLOW)
        d[8].set_color(BLUE)
        c_copy = c.copy().move_to(d)

        cancelled = VGroup(c_copy, c[0:3], c[11:14], left_cancel, right_cancel)

        self.play(
            TransformFromCopy(c, c_copy),
            run_time=1.5
        )

        self.play(
            TransformMatchingTex(c_copy, d),
            run_time=1.5
        )

        self.wait()

class SeparateRationalFunction(Scene):
    def construct(self):
        # 1. Split the rational function into distinct string parts
        # Index map:
        # [0] -> "f(x)"
        # [1] -> "="
        # [2] -> "\frac{"  (LaTeX fraction open)
        # [3] -> "x^2 + 1" (Numerator)
        # [4] -> "}{"      (LaTeX fraction middle divider)
        # [5] -> "x - 3"   (Denominator)
        # [6] -> "}"       (LaTeX fraction close)
        func = MathTex(
            r"f(x)", r"=", r"\frac{", r"x^2 + 1", r"}{", r"x - 3", r"}"
        ).scale(2)

        self.play(Write(func))
        self.wait(1)

        # 2. Target the indexes directly
        # Index 3 is the numerator, Index 5 is the denominator
        numerator = func[3]
        denominator = func[5]

        # 3. Animate or modify them independently
        # Let's highlight the numerator in Teal and Denominator in Red
        self.play(
            numerator.animate.set_color(TEAL),
            run_time=1
        )
        self.wait(0.5)

        self.play(
            denominator.animate.set_color(RED),
            run_time=1
        )
        self.wait(1)

        # 4. Transform or move them independently
        # Example: Pulling the numerator out of the fraction
        self.play(
            numerator.animate.next_to(func, UP, buff=1),
            denominator.animate.next_to(func, DOWN, buff=1),
        )
        self.wait(2)


class VisualCancellation(Scene):
    def construct(self):
        eq = MathTex("3", "+", "x", "-", "3", "+", "y")
        self.play(Write(eq))
        self.wait(1)

        # Create lines crossing out '3' (eq[0]) and '-3' (eq[3])
        strike1 = Line(eq[0].get_corner(DL), eq[0].get_corner(UR), color=RED)
        strike2 = Line(eq[3].get_corner(DL), eq[3].get_corner(UR), color=RED)

        self.play(Create(strike1), Create(strike2))
        self.wait(1)

        # Fade out the cancelled terms and the strike lines
        self.play(
            FadeOut(eq[0]), FadeOut(eq[1]), FadeOut(eq[3]),
            FadeOut(strike1), FadeOut(strike2)
        )
        self.wait(1)

class MovingFrameBox(Scene):
    def construct(self):
        a = MathTex(
            "xyy'", "=", "1+y^2"
        )
        self.play(Write(a))
        framebox1 = SurroundingRectangle(a[0], buff = .1)
        framebox2 = SurroundingRectangle(a[2], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()


class BoxEquationTerm(Scene):
    def construct(self):
        # Create the equation
        equation = MathTex("2x^2 - 5x + 2", "=", "(x - 2)(2x - 1)")
        
        # Write the equation on screen
        self.play(Write(equation))
        self.wait(1)
        
        # Create a surrounding rectangle around the first term (equation[0])
        box = SurroundingRectangle(equation[0], buff=0.1, color=YELLOW)
        
        # Animate drawing the box
        self.play(Create(box))
        self.wait(2)
        
        # Optional: Move or replace the box to another term (equation[2])
        box2 = SurroundingRectangle(equation[1], buff=0.1, color=RED)
        self.play(ReplacementTransform(box, box2))
        self.wait(2)