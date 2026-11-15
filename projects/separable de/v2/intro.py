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

        # ---------  AnimB: separated variables  ---------
        self.play(
            a.animate.shift(UP * 0.5),
            **RT
        )

        b, parts = self.write_substitute(
            lambda slot: [
                Function(f, slot[0]), sp, dx, p, Function(g, slot[1]), sp, dy,
                eq,
                z
            ],
            [
                [mxy.input[0], nxy.input[0]],   # slot 0 (inside f): the x from M and the x from N
                [mxy.input[2], nxy.input[2]],   # slot 1 (inside g): the y from M and the y from N
            ],
            buff=DOWN * 0.5,
            write_time=1.5
        )

        self.wait()