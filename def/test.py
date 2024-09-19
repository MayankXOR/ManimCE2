# from rieman_rectangles import riemann_rectangles_def
from manim import *
class Test(Scene):
    def construct(self):
        ax = Axes()
        func = lambda x: x**2
        graph = ax.plot(func)
        area = ax.riemann_rectangles_def(func=graph, x_max=3, x_min=5, dx=0.1)
        self.add(ax, graph)
        self.play(Create(area, run_time=10))