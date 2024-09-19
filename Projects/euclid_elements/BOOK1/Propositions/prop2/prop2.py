#March, 18, 2023
# @Mayankk20007
from manim import *
# from manim.opengl import *
from funcs import EquilateralTriangleFromLine
class prop2(Scene):
    def construct(self):
        BC = Line(start=ORIGIN, end=1.7*UP+2*LEFT).shift(UP+LEFT).set_color(RED)
        A = Dot(DOWN*0.4 + LEFT*0.8).shift(DOWN*0.5+LEFT)
        BA = Line(start=A, end=BC)
        # self.add(A, BC)
        BAD = EquilateralTriangleFromLine(line=BA)
        DB = BAD[2]
        slope_of_DB = DB.get_slope()
        BF = Line(start=DB.get_end(), end = [BC.get_length()+2,0,0]).rotate(slope_of_DB+0.135, about_point=DB.get_end())
        CHG = Circle(radius=BC.get_length()).move_to(DB.get_end())
        KLG = Circle(radius=DB.get_length()+BC.get_length()).move_to(DB.get_start())

        DA = BAD[1]
        slope_of_DA = DA.get_slope()
        DE = Line(start = DA.get_start()).rotate(slope_of_DA+0.135, about_point=DA.get_start()).set_length(5)
        BG = Line(start=CHG.get_center(), end=CHG.get_right()).rotate(slope_of_DB-0.045, about_point = CHG.get_center())
        BG_copy = BG.copy()
        BC_copy = BC.copy()
        
        BG_copy_vertical = Line().set_length(BG.get_length()).rotate(PI/2).to_corner(UR)
        BC_copy_vertical = BG_copy_vertical.copy().shift(0.5*LEFT)
        BCequalsBGTex = Tex("BC", " = ","BG").to_corner(UR)
        DL = Line(start=KLG.get_center(), end=KLG.get_bottom()).rotate(slope_of_DB+0.517, about_point=KLG.get_center())
        BAD1_copy = BAD[1].copy()
        BAD2_copy = BAD[2].copy()
        BAD1_copy_vertical = Line().set_length(BAD[1].get_length()).to_corner(UR).shift( 1.5*DOWN).rotate(PI/2)
        BAD2_copy_vertical = BAD1_copy_vertical.copy().shift(0.5* LEFT)
        DAequalsDBTex = Tex("DA"," = ","DB").next_to(BCequalsBGTex, DOWN)
        DG = Line(start=KLG.get_center(), end=BG.get_end())
        DL_copy_vertical = Line().set_length(DL.get_length()).rotate(PI/2).to_corner(UR).shift(1.2*DOWN)
        DG_copy_vertical = DL_copy_vertical.copy().shift(0.5*LEFT)
        DLequalsDGTex = Tex("DL"," = ","DG").next_to(DAequalsDBTex, DOWN)
        BGBrace = BraceBetweenPoints(point_2=BG.get_start(), point_1=BG.get_end())
        DBBrace = BraceBetweenPoints(point_2=DB.get_start(), point_1=DB.get_end())
        DGBrace = BraceBetweenPoints(point_2=DG.get_start(), point_1=DG.get_end())
        DBPlusBGequalsDGTex = Tex("DB ","+"," BG"," = ","DG").next_to(DLequalsDGTex, DOWN).shift(LEFT*0.5)
        DABrace = BraceBetweenPoints(point_1=KLG.get_center(), point_2=A.get_center())
        ALBrace = BraceBetweenPoints(point_1=A.get_center(), point_2=DL.get_end())
        AL = Line(start=A.get_center(), end=DL.get_end())
        DLBrace = BraceBetweenPoints(point_1=KLG.get_center(), point_2=DL.get_end())
        DLequalsDGTexBox = SurroundingRectangle(mobject=DLequalsDGTex)
        DAPlusALequalsDLTex = Tex("DA ","+ ","AL ","= ","DL").next_to(DBPlusBGequalsDGTex, DOWN)
        DBPlusBGequalsDAPlusALTex = Tex("DB"," +"," BG"," ="," DA"," +"," AL").next_to(DAPlusALequalsDLTex, DOWN).shift(0.5*LEFT)
        DAequalsDBTexBox = SurroundingRectangle(DAequalsDBTex)
        BCequalsBGTexBox = SurroundingRectangle(BCequalsBGTex)
        BCequalsBGTex0copy = Tex("BC").move_to(DBPlusBGequalsDAPlusALTex[2].get_center())
        ALCOPY = Line().set_length(AL.get_length())
        BCCOPY = Line().set_length(BC.get_length())
        FinalEquality = VGroup(ALCOPY, BCCOPY).arrange(UP)









        #LABELS:::
        A_label = Tex("A").next_to(A.get_center(), DOWN, buff=0.1).scale(0.5)
        B_label = Tex("B").next_to(BC.get_start(), UP, buff=0.1).scale(0.5)
        C_label = Tex("C").next_to(BC.get_end(), UP, buff=0.1).scale(0.5)
        D_label = Tex("D").next_to(DB.get_start(), UP, buff=0.1).scale(0.5)
        L_label = Tex("L").next_to(AL.get_end(), UP).scale(0.5)
        G_label = Tex("G").next_to(BG.get_end(), UL).scale(0.5)














        self.play(Create(VGroup(BC, A, A_label, B_label, C_label)))
        self.wait()
        self.play(DrawBorderThenFill(BAD))
        self.play(Write(D_label))
        self.wait()
        self.play(Create(VGroup(DE, BF)))
        self.play(Write(L_label))
        self.wait()
        self.play(Create(CHG))
        self.play(Write(G_label))
        self.wait(0.5)
        self.play(Create(KLG))
        self.wait()
        self.play(AnimationGroup(Wiggle(BG, rotation_angle=0.05*TAU), Wiggle(BC, rotation_angle=0.05*TAU), lag_ratio=0))
        self.play(AnimationGroup(ReplacementTransform(BG_copy, BG_copy_vertical), ReplacementTransform(BC_copy, BC_copy_vertical)))
        self.wait()
        self.play(ReplacementTransform(VGroup(BG_copy_vertical, BC_copy_vertical), BCequalsBGTex))
        self.wait()
        self.play(AnimationGroup(Wiggle(BAD[1], rotation_angle=0.05*TAU), Wiggle(BAD[2], rotation_angle=0.05*TAU)))
        self.play(AnimationGroup(ReplacementTransform(BAD1_copy, BAD1_copy_vertical), ReplacementTransform(BAD2_copy, BAD2_copy_vertical)))
        self.wait()
        self.play(ReplacementTransform(VGroup(BAD1_copy_vertical, BAD2_copy_vertical), DAequalsDBTex))
        self.wait()
        self.play(AnimationGroup(Wiggle(DL, rotation_angle=0.05*TAU), Wiggle(DG, rotation_angle=0.05*TAU)))
        self.play(AnimationGroup(ReplacementTransform(DL, DL_copy_vertical), ReplacementTransform(DG, DG_copy_vertical)))
        self.wait()
        self.play(ReplacementTransform(VGroup(DL_copy_vertical, DG_copy_vertical), DLequalsDGTex))
        self.play(DrawBorderThenFill(VGroup(BGBrace, DBBrace)))
        self.wait()
        self.play(ReplacementTransform(VGroup(BGBrace, DBBrace), DGBrace))
        self.play(Write(DBPlusBGequalsDGTex))
        self.play(FadeOut(DGBrace))
        self.play(DrawBorderThenFill(VGroup(DABrace, ALBrace)))
        self.wait()
        self.play(ReplacementTransform(VGroup(DABrace, ALBrace), DLBrace))
        self.play(AnimationGroup(
            Write(DAPlusALequalsDLTex),
            FadeOut(DLBrace),
            lag_ratio=0
        ))
        self.wait()
        self.play(AnimationGroup(
            Write(DBPlusBGequalsDAPlusALTex),
            GrowFromEdge(mobject=DLequalsDGTexBox, edge=UP),
            lag_ratio=0
        ))
        self.play(FadeOut(DLequalsDGTexBox))
        self.wait()
        self.play(AnimationGroup(
            FadeOut(DBPlusBGequalsDAPlusALTex[0:2]),
            FadeOut(DBPlusBGequalsDAPlusALTex[4:6]),
            GrowFromCenter(DAequalsDBTexBox),
            lag_ratio=0
        ))
        self.play(FadeOut(DAequalsDBTexBox))
        self.play(DBPlusBGequalsDAPlusALTex[-1].animate.shift(LEFT*1.5))
        self.wait()
        self.play(AnimationGroup(
            ReplacementTransform(DBPlusBGequalsDAPlusALTex[2], BCequalsBGTex0copy),
            GrowFromCenter(BCequalsBGTexBox),
            lag_ratio=0))
        self.play(FadeOut(BCequalsBGTexBox))
        self.wait()
        self.add(AL)
        self.add(BC)
        mobs_to_fade = self.mobjects.copy()
        mobs_to_fade.remove(AL)
        mobs_to_fade.remove(BC)
        self.play(FadeOut(Group(*mobs_to_fade)))
        self.wait()
        self.play(AnimationGroup(
            ReplacementTransform(AL, FinalEquality[0]),
            ReplacementTransform(BC, FinalEquality[1])
        ))
        self.wait()
        self.add()
        # self.add(A, BC, BAD, DE, BF, CHG, KLG, BCequalsBGTex, DAequalsDBTex, DLequalsDGTex, DBPlusBGequalsDGTex)
        # self.add(A_label, B_label, C_label, D_label, L_label)
        
        
        self.wait()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # self.mobjects.append(BAD)
        for obj in self.mobjects:
            obj.shift(DOWN+RIGHT)
        # self.add(BC, A, BA, BAD)
 



        # self.add(BF, CHG, KLG, DA, DE)

        # self.interactive_embed()

        # circ1 = Circle(radius=2).shift(LEFT)
        # circ2 = Circle(radius=2).shift(RIGHT)
        # inters = Intersection(circ1, circ2).set_fill(WHITE)
        # self.add(circ1, circ2, Dot(point=inters.get_top()))
            # sq = Square(color=RED, fill_opacity=1)
            # sq.move_to([-2, 0, 0])
            # cr = Circle(color=BLUE, fill_opacity=1)
            # cr.move_to([-1.3, 0.7, 0])
            # un = Intersection(sq, cr, color=GREEN, fill_opacity=1)
            # un.move_to([1.5, 0, 0])
            # self.add(sq, cr, un)









        # line_length = line.get_length()
        # circ1 = Circle(radius=line_length).move_to(line.get_start()).set_color(GREEN)
        # circ2 = Circle(radius=line_length).move_to(line.get_end()).set_color(BLUE)
        # intersection = Intersection(circ1, circ2).set_color(PINK)
        # topdot = Dot(point=intersection.get_top()).set_color(MAROON)
        # botdot = Dot(point=intersection.get_bottom()).set_color(PURPLE)
        # line2 = Line(start=line.get_start(), end=intersection.get_top()).set_color(YELLOW)
        # line3 = Line(start=line.get_end(), end= intersection.get_bottom()).set_color(TEAL)
        # triangle = VGroup(line, line2, line3)
        # direc = [UP, DOWN, LEFT, RIGHT, UL, DL, DR]
        # grp = VGroup(triangle, circ1, circ2, intersection, topdot, botdot).rotate(PI/3)
        # for c in direc:
        #     self.add(Cross().scale(0.2).move_to(intersection.get_critical_point(direction=c)))
        # self.add(Cross().set_color(TEAL).scale(0.2).move_to(intersection.get_critical_point(UR)))
        # self.add(grp)