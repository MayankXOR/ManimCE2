from manim import *




class SimpleUpdaterFunc(Scene):
    def construct(self):


        circle = Circle()
        dot = Dot()
        dot.add_updater(
            lambda x: x.next_to(circle, RIGHT)
        )

        self.play(Create(circle), Create(dot), lag_ratio=0)
        self.wait()
        self.play(circle.animate.shift(2 * RIGHT))
        self.wait()





class SceneUpdater(Scene):
    def construct(self):



        axis = NumberPlane().add_coordinates().set(opacity=0.4)
        sample = Square(color=BLUE).set(opacity=0.6).shift(6 * LEFT).scale(0.25)
        if sample.get_x()<0:
            force_vector = always_redraw(lambda: Arrow(start=sample.get_center(),end = axis.c2p(int(sample.get_x())+1), buff=0).set_color(RED))
        else:
            force_vector = always_redraw(lambda: Arrow(start=sample.get_center(), end=axis.c2p(int(sample.get_x())-1), buff=0).set_color(RED))
        def scaler(mob):
            pass
        #     d = np.linalg.norm(mob.get_end())
        #     if d != 0:
        #         mob.set_length(1/(d))
        #     elif d == 0 :
        #         mob.set_length(0)
        # force_vector.add_updater(scaler)




        self.add(sample, force_vector)
        self.wait()
        self.play(sample.animate.shift(12*RIGHT), rate_func=there_and_back_with_pause, run_time=12)