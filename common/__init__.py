"""
common/  --  everything your scenes share.

Every scene file starts with ONE line:

    from common import *

That line gives you manim, reactive_manim, the colours/constants, the
symbol factory, the helper functions and the base scene class.
(This is the same idea as 3b1b's `manim_imports_ext`.)
"""
from manim import *
from .style import *
from .symbols import *
from .helpers import *
from .scene_base import *
from reactive_manim import *   # LAST on purpose: its MathTex must override manim's
