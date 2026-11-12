from manim import *

class AdvancedTransform(Scene):
    def construct(self):
        # Original equation
        eq_start = MathTex("x", "+", "y", "=", "10")
        self.play(Write(eq_start))
        self.wait(1)

        # Target equation (substituting x = 3)
        eq_end = MathTex("3", "+", "y", "=", "10")
        eq_end.shift(DOWN * 1.5).set_color(BLUE)

        # Transform matching parts seamlessly
        self.play(TransformMatchingTex(eq_start, eq_end))
        self.wait(2)

