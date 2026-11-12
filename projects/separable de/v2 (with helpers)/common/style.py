"""Constants only. Change a look here once -> every scene follows."""
from manim import *

__all__ = ["X_COLOR","Y_COLOR","CANCEL_COLOR","ANSWER_COLOR","CONST_COLOR",
           "RT","TOP_SHIFT","LABEL_FONT"]   # constants ONLY: never re-export manim names

# --- colour meaning (x-stuff is blue, y-stuff is yellow, etc.) -------------
X_COLOR      = BLUE
Y_COLOR      = YELLOW
CANCEL_COLOR = RED          # the red slash through cancelled terms
ANSWER_COLOR = LIGHT_PINK   # box around a final answer
CONST_COLOR  = GREEN        # the constant C

# --- timing ---------------------------------------------------------------
RT = {"run_time": 1.5}      # use as  self.play(..., **RT)

# --- layout ---------------------------------------------------------------
TOP_SHIFT = DOWN * 0.4      # first equation sits slightly below the top edge
LABEL_FONT = "LMRoman10"    # font for words like "general solution"
