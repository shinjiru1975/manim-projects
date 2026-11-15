from manim import *
from reactive_manim import *
from common import X_COLOR, Y_COLOR

def symbols_main():
    """
    To import to scene:
    x, y1, y2, yp, wan, tu, z, p, mn, eq, dy, dx, sp, C, integ = symbols_main()
    """
    x, y1, y2, yp, wan, tu, z, p, mn, eq, dy, dx, sp, C, integ = MathTex(
        "x", "y", "y", "y'", "1", "2", "0", "+", "-", "=", "dy", "dx", r"\ ", "C", r"\int"
    )

    dy.set_color(Y_COLOR)
    dx.set_color(X_COLOR)
    
    return x, y1, y2, yp, wan, tu, z, p, mn, eq, dy, dx, sp, C, integ

def symbols_conditions():
    """
    To import to scene:
    x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = symbols_conditions()
    """
    x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi = MathTex(
        "x", "=", "1", ",", "y", "=", "0", ";"
    )

    x_con.set_color(X_COLOR)
    y_con.set_color(Y_COLOR)

    return x_con, eq1_con, wan_con, comma, y_con, eq2_con, z_con, semi

def symbols_introduction():

    x, y, m, n, p, eq, z, f, g, dy, dx, sp, com = MathTex(
        "x", "y", "M", "N", "+", "=", "0", "f", "g", "dy", "dx", r"\ ", ","
    )

    x.set_color(X_COLOR)
    dx.set_color(X_COLOR)

    y.set_color(Y_COLOR)
    dy.set_color(Y_COLOR)

    return x, y, m, n, p, eq, z, f, g, dy, dx, sp, com
