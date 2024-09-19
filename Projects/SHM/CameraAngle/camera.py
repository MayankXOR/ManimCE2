from manim import *
from manim.opengl import *
class TracedPathExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = always_rotate(Circle().scale(2), rate=2)
        dot = always_redraw(lambda : Dot().move_to(circle.get_start()))

        self.add(circle, dot, axes)
        self.wait()
        self.begin_ambient_camera_rotation(about="theta")