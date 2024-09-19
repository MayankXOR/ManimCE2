from manim import *
def riemann_rectangles_def(self, func, x_min, x_max, dx):
    x_range = np.arange(x_min, x_max, dx)
    rects = VGroup()
    for c in x_range:
        dot1 = self.c2p(c, 0)
        dot2 = self.input_to_graph_point(x=c, graph=func)
        dot3 = self.c2p(c+dx, 0)
        dot4 = self.input_to_graph_point(x=c+dx, graph=func)
        dots = [dot1, dot2, dot3, dot4]
        rect = Polygon(*dots)
        rects.add(rect)
    return rects
