from manim import *
from manim.opengl import *

class SS(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 5, 1])
        self.add(ax)
        dot = Dot()
        self.dot = dot
        x_line = always_redraw(lambda: ax.get_vertical_line(point=dot.get_center()))
        y_line = always_redraw(lambda: ax.get_horizontal_line(point=dot.get_center()))
        self.add(x_line, y_line)
        self.x_line = x_line
        self.y_line = y_line
        self.play(Create(ax))
        self.interactive_embed()
    def on_key_press(self, symbol, modifiers):
        from pyglet.window import key as KEYY
        if symbol == KEYY.G:
            self.play(self.dot.animate.move_to(self.mouse_point.get_center()))
            # self.play(Create(VGroup(self.x_line, self.y_line)))
        return super().on_key_press(symbol, modifiers)