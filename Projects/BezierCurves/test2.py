from manim import *

class LinearBezier(Scene):
    def construct(self):


        p0 = Dot(point=1.54*DOWN + 2.54*LEFT)
        p1 = Dot(point=3.14*RIGHT + 2.21*UP)
        line = Line(start= p0,end= p1)
        t = ValueTracker(0)

        p = Dot().move_to(p0.get_center())
        def follow_t_value(mob):
            mob.become(Dot().move_to(line.point_from_proportion(t.get_value())))
        p.add_updater(follow_t_value)
        braces = BraceBetweenPoints(point_1=p0.get_center(), point_2=p.get_center())
        def braces_updater(mob):=<
            mob.become(BraceBetweenPoints(point_2=p0.get_center(), point_1=p.get_center()))
        braces.add_updater(braces_updater)
        def JasonsBrace(point_a, point_b, label, buff):
            dummy = Line(point_a, point_b)
            alpha = dummy.get_angle()+PI/2
            brace = BraceLabel(dummy, label, brace_direction=[np.cos(alpha),np.sin(alpha),0], buff=buff)
            return brace
        Bracers =always_redraw(lambda: JasonsBrace(point_a=p0.get_center(), point_b=p.get_center(), label="t=", buff=0.1))



        # self.add(p0, p1, line, p, Bracers)
        # self.wait()
        # self.play(t.animate.set_value(0.5))
        # self.play(t.animate.set_value(0.25))
        # self.play(t.animate.set_value(0.75))
        # self.wait()
        self.add(NumberPlane())


class QuadraticBezier(Scene):
    def construct(self):
        dot1 = Dot([-3, -2, 0])
        dot2 = Dot([0, 3, 0])
        dot3 = Dot([3, -2, 0])
        line1 = Line(dot1, dot2)
        line2 = Line(dot2, dot3)
        t = ValueTracker(0)
        d1 = Dot().move_to(dot1.get_center())
        d2 = Dot().move_to(dot2.get_center())
        def follow_t_value(mob):
            mob.become(Dot().move_to(line1.point_from_proportion(t.get_value())))
        d1.add_updater(follow_t_value)
        def follow_t_value_2(mob):
            mob.become(Dot().move_to(line2.point_from_proportion(t.get_value())))
        d2.add_updater(follow_t_value_2)
        line3 = Line(d1, d2)
        def line3_updater(mob):
            mob.become(Line(start=d1, end=d2))
        line3.add_updater(line3_updater)
        d3 = Dot().move_to(line3.get_start())
        def d3_updater(mob):
            mob.become(Dot().move_to(line3.point_from_proportion(t.get_value())))
        d3.add_updater(d3_updater)
        trace = TracedPath(d3.get_center)




        self.add(VGroup(dot1, dot2, dot3, line1, line2, d1, d2, line3, d3, trace))
        self.play(t.animate.set_value(1), run_time = 3)
        self.wait()



class CubicBezier(Scene):
    def construct(self):
        

        t = ValueTracker(0)
        d1 = Dot([-4, -3, 0]).set(color=RED)
        d2 = Dot([-2, 2, 0]).set(color=BLUE)
        d3 = Dot([2, 2, 0]).set(color=GREEN)
        d4 = Dot([4, -3, 0]).set(color=YELLOW)
        l1 = Line(d1, d2).set_color_by_gradient(RED, BLUE)
        l2 = Line(d2, d3).set_color_by_gradient(BLUE, GREEN)
        l3 = Line(d3, d4).set_color_by_gradient(GREEN, YELLOW)
        d11 = always_redraw(lambda: Dot().move_to(l1.point_from_proportion(t.get_value())))
        d12 = always_redraw(lambda: Dot().move_to(l2.point_from_proportion(t.get_value())))
        d13 = always_redraw(lambda: Dot().move_to(l3.point_from_proportion(t.get_value())))
        l11 = always_redraw(lambda: Line(d11, d12))
        l12 = always_redraw(lambda: Line(d12, d13))
        d111 = always_redraw(lambda: Dot().move_to(l11.point_from_proportion(t.get_value())))
        d112 = always_redraw(lambda: Dot().move_to(l12.point_from_proportion(t.get_value())))
        l111 = always_redraw(lambda: Line(d111, d112))
        d1111 = always_redraw(lambda: Dot().move_to(l111.point_from_proportion(t.get_value())))
        trace = TracedPath(d1111.get_center)

        self.add(d1, d2, d3, d4, l1, l2, l3, d11, d12, d13, l11, l12, d111, d112, l111, d1111, trace)

        # self.add(NumberPlane())
        self.play(t.animate.set_value(1), rate_func = there_and_back_with_pause, run_time=5)
        self.wait()
