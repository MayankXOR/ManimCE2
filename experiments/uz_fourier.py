#Mayankk
#March18th2023
#Saturday


from manim import *
import numpy as np

class FourierCirclesScene(Scene):
    n_vectors = 51 #no. of vectors used per curve, the more vectors we use, the better approximation we have but it will take more time to render(DEFAULTS TO 50)
    center_point = ORIGIN #center of camera for normal conditions
    slow_factor = 0.1 #reciprocal of `dt` just to complete "a part of" the animation every frame
    #TODO:
    #Increase the precision of Vectors probably using other libraries like np.tt.ttt


    def get_freqs(self):
        n = self.n_vectors
        all_freqs = list(range(n // 2, -n // 2, -1)) #taking the Euler's modulus function ensures our waves lands on 0 or 1 so it can be converted to binary
        all_freqs.sort(key=abs) #not necessary but just so that the frequencies are printed in chronological order
        return all_freqs

    # Computing Fourier series
    # i.e. where all the math happens
    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt) #for updaters, dt=1/FPS
        samples = np.array([
            path.point_from_proportion(t) #Had the idea to use t-value as the parameter from `Beauty of Bezier Curves` by Freya Holmer
            for t in ts
        ])
        samples -= self.center_point #takes the handles of Bezier involving the mob and returns the coordinates of the 
        complex_samples = samples[:, 0] + 1j * samples[:, 1] #Samples which are too small to be represented as a sum of sin(x) and cos(x) with binary coeffecients

        result = []
        for freq in freqs:
            riemann_sum = np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples) 
            ]).sum() * dt
            result.append(riemann_sum)

        return result

    def get_paths(self):
        tex_mob = MathTex(r"\boxed{\sum_{n=1}^{\infty}{\frac{1}{n^2}}=\frac{\pi^2}{6}}")
        # CAUTION: If you use some Text(like the letter "O") or PMobject that contains breaks and is not continuous, the path may not be much accurate
        # It's because the tex_mob is sliced letter by letter and it's not possible for me to break the 2 curves of "O" as it's very complex
        # due to this tendency, the vectors try to jump to both of the planes of mob(which is not possibe in 3-dimensional world) at the same time
        # resulting in superposition of the vector returning very jaggy approximation of the Beziers
        # However, I'll try to work and find an aliter to this method to increase the accuracy(atleast that's what I hope)"""
        tex_mob.scale_to_fit_width(10)
        tex_mob.scale(1.4)
        paths = tex_mob.family_members_with_points()
        for p in paths:
            p.set_fill(opacity=0) #The initial path should not be shown
            p.set_stroke(WHITE, 1)
        return paths
        
    #SHOW TIME
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
                print("{:3.0f}: abs = {:5.3f}  Z = {:-5.3f} + {:-5.3f}j".format(    #printing only valuable info so
                    freqs[i],                                                                               #slicing the high pass frequencies as 88they consume too much GPU power
                    np.abs(coefs[i]), 
                    np.real(coefs[i]), 
                    np.imag(coefs[i])))                                                                #Remove lower pass frequencies as they don't contribute much but returns errors
                dummy = Vector(
                    [np.real(coefs[i]), np.imag(coefs[i]), 0]
                )
                circ = Circle(radius=np.abs(coefs[i])).set_stroke(width=1, color=RED) #Taking the mob points from the path given by tex_mob
                vectorsCircles += VGroup(dummy, circ).shift(origin)
                origin = dummy.get_end()

            self.play(DrawBorderThenFill(vectorsCircles))
            self.wait()

            dot = always_redraw(lambda: Dot(vectorsCircles[-1][0].get_end(), radius=0.04, color=GREEN)) #The mobject which ultimately traces path

            trace = VMobject().set_points([vectorsCircles[-1][0].get_end()]).set_color(YELLOW) #tracedPath
            self.add(trace,dot)

            def vectorsUpdater(mobj, dt): #dt because it's a `SceneUpdater` dt = 1/FPS and is automatically taken in account
                origin = mobj[0][0].get_end()
                for i in range(1, len(freqs)):
                    mobj[i][0].rotate(2*PI*dt*freqs[i]*self.slow_factor, about_point=mobj[i][0].get_start())
                    mobj[i].shift(origin - mobj[i][0].get_start()) #Finally got it (I wanna DIE now)
                    origin = mobj[i][0].get_end() #ensures that `gamma`&`phi` don't exceed the bounding box
                trace.add_line_to(mobj[-1][0].get_end())    
            vectorsCircles.add_updater(vectorsUpdater)

            self.wait(1/self.slow_factor)
 
            self.remove(vectorsCircles)
            self.wait(2)







