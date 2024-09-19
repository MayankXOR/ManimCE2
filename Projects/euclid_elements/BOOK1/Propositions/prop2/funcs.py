from manim import *

def EquilateralTriangleFromLine(line: Line) -> VGroup:
    line2 = line.copy()
    line3 = line.copy()
    line2.rotate(angle=PI/3, about_point=line.get_start())
    line3.rotate(angle=5*PI/3, about_point=line.get_end())
    triangle = VGroup(line, line2, line3)
    return triangle
