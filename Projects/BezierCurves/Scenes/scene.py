from manim import *

p.add_updater(follow_t_value)
braces.add_updater(braces_updater)

self.add(p0, p1, line, p, Bracers)
self.wait()
self.play(t.animate.set_value(0.5))
self.play(t.animate.set_value(0.25))
self.play(t.animate.set_value(0.75))
self.wait()