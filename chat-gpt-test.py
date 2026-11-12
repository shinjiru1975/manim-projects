
from manim import *
import inspect
import manim.animation.transform_matching_parts as matching

class DiagnoseTex(Scene):
    def construct(self):
        eq = MathTex(r"{{x}}^2 + {{y}}^2 = {{z}}^2")

        print("\n--- MANIM DIAGNOSTICS ---")
        print("Manim version:", __import__("manim").__version__)
        print("Manim location:", __import__("manim").__file__)
        print("MathTexPart class:", matching.MathTexPart)
        print("Matching module:", inspect.getfile(matching))

        print("\nEquation parts:")
        for part in eq.submobjects:
            print(
                "Type:", type(part),
                "| Is MathTexPart:", isinstance(part, matching.MathTexPart),
                "| TeX:", getattr(part, "tex_string", None)
            )

        print("\nParts seen by TransformMatchingTex:")
        for part in matching.TransformMatchingTex.get_mobject_parts(eq):
            print(
                "Type:", type(part),
                "| Is MathTexPart:", isinstance(part, matching.MathTexPart),
                "| TeX:", getattr(part, "tex_string", None)
            )

        self.add(eq)
        self.wait()

class MatchingTest(Scene):
    def construct(self):
        a = MathTex(r"{{xyy'}} = {{1+y^2}}")
        b = MathTex(r"\frac{ {{xyy'}} }{x} = {{1+y^2}}")

        a.to_edge(UP)
        b.next_to(a, DOWN)

        self.play(Write(a))
        self.play(TransformMatchingTex(a.copy(), b), run_time=1.5)
        self.wait()

