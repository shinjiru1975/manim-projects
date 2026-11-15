from manim import *
from common import *
from symbols import *
from reactive_manim import *

class Introduction(DEScene):
    def construct(self):
        
        x, y, m, n, p, eq, z, f, g, dy, dx, sp, com = symbols_introduction()

        # ---------  AnimA: write equation  ---------
        mxy = Function(m, [x, com, y])
        nxy = Function(n, [x, com, y])

        a = MathTex(
            mxy, sp, dx, p, nxy, sp, dy,
            eq,
            z
        )

        self.play(Write(a), **RT)

        # ---------  AnimB: write equation  ---------
        fx = Function(f, x)
        gy = Function(g, y)

        b = MathTex(
            fx, sp, dx, p, gy, sp, dy, 
            eq, 
            z
        )

        self.play(
            a.animate.shift(UP * 0.5),
            **RT
        )

        b.next_to(a, DOWN, buff=0.5)
        self.play(Write(b), **RT)

        self.wait()