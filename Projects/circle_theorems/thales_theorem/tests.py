from manim import *

class  testcircle(Scene):
    def construct(self):

        circle = Circle(radius=2.5)
        value = ValueTracker(0.2)
        dot = always_redraw(lambda:Dot().move_to(circle.point_at_angle(value.get_value()))) 
        diameter = Line(circle.get_left(), circle.get_right())
        angle_line1 = always_redraw(lambda: Line(start=circle.get_left(), end=dot.get_center()))
        angle_line2 = always_redraw(lambda: Line(start=circle.get_right(), end=dot.get_center()))
        right_angle = always_redraw(lambda: RightAngle(line1=angle_line1, line2=angle_line2, quadrant=(-1, -1), length=0.2))



        self.add(circle,dot, diameter, angle_line1, angle_line2,right_angle)
        self.play(value.animate.set_value(PI-0.2), rate_func=there_and_back_with_pause, run_time=5 )
        self.wait()


class scene2(Scene):
    def construct(self):
        
        circle = Circle(radius=2.5)
        dot = always_redraw(lambda: Dot().move_to(circle.point_at_angle(3.2/4)))
        diameter = Line(circle.get_left(), circle.get_right())
        line1 = Line(start=circle.get_left(), end=dot.get_center())
        line2 = Line(start=circle.get_right(), end=dot.get_center())
        line_to_center = Line(start=dot.get_center(), end=ORIGIN)
        origin_dot = Dot(point=ORIGIN)
        circle_left_dot = Dot(point=circle.get_left())
        circle_right_dot = Dot(point=circle.get_right())
        dot_dot = Dot(point=dot.get_center())
        alpha_angle1 = Angle(line1=line1, line2=diameter, other_angle=True, quadrant=(1, 1))
        alpha_angle2 = Angle(line1=line1, line2=line_to_center, other_angle=False, quadrant=(-1, 1))
        beta_angle1 = Angle(line1=line2, line2=diameter, other_angle=False, quadrant=(1, -1))
        beta_angle2 = Angle(line1=line2, line2=line_to_center,radius= 0.5, other_angle=True, quadrant=(-1, 1))
        alpha_angle1_label = MathTex(r"\alpha").next_to(alpha_angle1, RIGHT, buff=0.1).scale(0.75)
        alpha_angle2_label = MathTex(r"\alpha").next_to(alpha_angle2, LEFT+DOWN*0.1, buff=0.1).scale(0.75)
        beta_angle1_label = MathTex(r"\beta").next_to(beta_angle1, LEFT, buff=0.1).scale(0.7)
        beta_angle2_label = MathTex(r"\beta").next_to(beta_angle2, DOWN, buff=0.1).scale(0.7)


        self.add(circle, line1, line2, diameter,
                line_to_center, alpha_angle1, alpha_angle2, beta_angle1, beta_angle2
                , alpha_angle1_label, alpha_angle2_label, beta_angle1_label, beta_angle2_label,
                  origin_dot, circle_left_dot, circle_right_dot, dot_dot)
        




