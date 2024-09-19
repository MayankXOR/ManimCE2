from manim import *
from manim_slides import Slide


class Example(Slide):
    def construct(self):

        circle = Circle(radius=3, color=BLUE)
        dot = Dot().move_to(circle.get_right())

        self.play(Create(circle), GrowFromCenter(dot))
        self.stop() #waits for user to interact to go to next slide

        #self.start_loop() start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.stop()
        #self.end_loop()

        self.play(dot.animate.move_to(ORIGIN))
        self.stop()

        self.wait()
    
    def stop(self):
        self.wait(0.3)
        self.pause()