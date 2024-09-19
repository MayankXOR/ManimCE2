from manim import *
import numpy as np

class FourierCirclesScene(Scene):
    n_vectors = 51
    center_point = ORIGIN
    slow_factor = 0.1

    def get_freqs(self):
        n = self.n_vectors
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    # Computing Fourier series
    # i.e. where all the math happens
    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples = np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples -= self.center_point
        complex_samples = samples[:, 0] + 1j * samples[:, 1]

        result = []
        for freq in freqs:
            riemann_sum = np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples)
            ]).sum() * dt
            result.append(riemann_sum)

        return result
    
    def get_paths(self):
        tex_mob = Tex("NOOR")
        tex_mob.scale_to_fit_width(10)
        paths = tex_mob.family_members_with_points()
        for p in paths:
            p.set_fill(opacity=0)
            p.set_stroke(WHITE, 1)
        return paths
        
    def construct(self):
        npl = NumberPlane()
        npl.add_coordinates()
        self.add(npl)

        freqs = self.get_freqs()
        paths = self.get_paths()
        for path in paths:
            coefs = self.get_coefficients_of_path(path, n_samples=500, freqs=freqs)

            self.play(Create(path))
            self.wait(2)

            vectorsCircles = VGroup()
            origin = ORIGIN
            for i in range(len(freqs)):
                print("{:3.0f}: abs = {:5.3f}  Z = {:-5.3f} + {:-5.3f}j".format(
                    freqs[i], 
                    np.abs(coefs[i]), 
                    np.real(coefs[i]), 
                    np.imag(coefs[i])))
                dummy = Line(
                    start = ORIGIN, 
                    end   = [np.real(coefs[i]), np.imag(coefs[i]), 0]
                )
                circ = Circle(radius=np.abs(coefs[i])).set_stroke(width=1, color=RED)
                vectorsCircles += VGroup(dummy, circ).shift(origin)
                origin = dummy.get_end()


            self.add(vectorsCircles)
            self.wait()

            dot = always_redraw(lambda: Dot(vectorsCircles[-1][0].get_end(), radius=0.04, color=GREEN))

            trace = VMobject().set_points([vectorsCircles[-1][0].get_end()]).set_color(YELLOW)
            self.add(trace,dot)

            def vectorsUpdater(mobj, dt):
                origin = mobj[0][0].get_end()
                for i in range(1, len(freqs)):
                    mobj[i][0].rotate(2*PI*dt*freqs[i]*self.slow_factor, about_point=mobj[i][0].get_start())
                    mobj[i].shift(origin - mobj[i][0].get_start())
                    origin = mobj[i][0].get_end()
                trace.add_line_to(mobj[-1][0].get_end())    
            vectorsCircles.add_updater(vectorsUpdater)

            self.wait(1/self.slow_factor)
 
            self.remove(vectorsCircles)
            self.wait(2)





