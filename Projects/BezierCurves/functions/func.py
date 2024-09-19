from manim import *
def follow_t_value(mob):
            mob.become(Dot().move_to(line.point_from_proportion(t.get_value())))

def braces_updater(mob):
            mob.become(BraceBetweenPoints(point_2=p0.get_center(), point_1=p.get_center()))

def JasonsBrace(point_a, point_b, label, buff):
            dummy = Line(point_a, point_b)
            alpha = dummy.get_angle()+PI/2
            brace = BraceLabel(dummy, label, brace_direction=[np.cos(alpha),np.sin(alpha),0], buff=buff)
            return brace