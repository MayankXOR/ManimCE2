from manim import *
import random
from math import modf

class trianglegenerator(Scene):
    def construct(self):
        axis = Axes(y_range=(-50, 50, 1), x_range=(-50, 50, 1)).add_coordinates()
        # for k in range(10):
        d1 = Dot(point=axis.c2p(random.randint(-50, 50), random.randint(-50, 50)))
        d2 = Dot(point=axis.c2p(random.randint(-50, 50), random.randint(-50, 50)))
        d3 = Dot(point=axis.c2p(random.randint(-50, 50), random.randint(-50, 50)))
        tri = Polygon([d1.get_x(), d1.get_y(), 0], [d2.get_x(), d2.get_y(), 0], [d3.get_x(), d3.get_y(), 0])
        # self.play(Create(tri))
        # self.wait()
        # self.play(FadeOut(tri))
        d = Dot(point = axis.c2p(40, 40))
        d1x = int(d1.get_x())
        d1y = int(d1.get_y())
        d2x = int(d2.get_x())
        d2y = int(d2.get_y())
        d3x = int(d3.get_x())
        d3y = int(d3.get_y())
        def areaoftri(d1x_, d1y_, d2x_, d2y_, d3x_, d3y_):
            ar =  (1/2 * ((d1x_ * (d2y_ - d3y_)) - (d1y_ * (d2x_ - d3x_)) + (d2x_ * d3y_ - d3x_ * d2y_)))
            if ar > 0 :
                return ar
            else:
                return ar * (-1)
        # area = tri.get_all_points
        # area = areaoftri(d1x_=d1x, d1y_=d1y, d2x_=d2x, d2y_=d2y, d3x_=d3x, d3y_=d3y)
        # areatex = Tex(f"{area}").to_corner(DR)
        self.add(d1, d2, d3, tri)




class calculusdot(Scene):
    def construct(self):

        axis = Axes(y_range=[-12, 12, 5]).add_coordinates()
        plot = axis.plot(lambda x:(x-1)*(x+2)*(x-3))
        value = ValueTracker(-3)
        dot = always_redraw(lambda : Dot().move_to(axis.c2p(value.get_value(), (value.get_value()-1)*(value.get_value()+2)*(value.get_value()-3))))
        # def shifter(mob, ax, val):
        #     mob.move_to(ax.c2p(val.get_value(), (val.get_value()-1)*(val.get_value()+2)*(val.get_value()-3)))
        # dot.add_updater(shifter(mob=dot, ax=axis, val=value))
        rects = always_redraw(lambda: axis.get_riemann_rectangles(dx=0.001, graph=plot, x_range=(-3, value.get_value())))
        self.add(axis, plot, dot, rects)
        self.play(value.animate.set_value(3.5), run_time=3)


