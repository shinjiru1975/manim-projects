from manim import *

class Test(Scene):
    def construct(self):
        t = MathTex("xyy'=1+y^2")
        self.play(Write(t))
        self.play(t.animate.shift(UP))

        eq2 = MathTex("\\frac{d}{dx}f(x)g(x)=f(x)\\frac{d}{dx}g(x)+g(x)\\frac{d}{dx}f(x)")
        self.play(Write(eq2))

        self.play(t.animate.shift(UP), eq2.animate.shift(UP))
