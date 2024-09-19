from manim import *
p0 = Dot(point=1.54*DOWN + 2.54*LEFT)
p1 = Dot(point=3.14*RIGHT + 2.21*UP)
line = Line(start= p0,end= p1)
t = ValueTracker(0)
p = Dot().move_to(p0.get_center())
braces = BraceBetweenPoints(point_1=p0.get_center(), point_2=p.get_center())
Bracers =always_redraw(lambda: JasonsBrace(point_a=p0.get_center(), point_b=p.get_center(), label="t=", buff=0.1))
