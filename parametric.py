from manim import *

class Parametric(Scene):
    def func_1(self, t):
        return ((np.cos(t)+(1/3)*(np.cos(123*t)+np.sin(250*t))), (np.sin(t)+(1/3)*(np.sin(123*t)+np.cos(245*t))), 0)
    def func_2(self, t):
        return ((11*np.cos(t)-6*np.cos((11/6)*t)),(11*np.sin(t)-6*np.sin((11/6)*t)), 0)
    def func_3(self, t):
        return ((np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)), (np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)), 0)
    
    def construct(self):
        title = Text("Beauty in Curves",font_size = 36)
        title.set_color_by_gradient(RED_A, MAROON)
        title.to_edge(UP)
        curve_1 = ParametricFunction(self.func_1, t_range = (0, TAU), stroke_width = 0.6)
        curve_1.set_color_by_gradient(RED_A, MAROON)
        curve_1.scale(1.5)

        curve_2 = ParametricFunction(self.func_2, t_range = (0, 40), stroke_width = 2)
        curve_2.scale(0.15)
        curve_2.set_color_by_gradient(RED_A, MAROON)

        curve_3 = ParametricFunction(self.func_3, t_range = (0, 12*PI), stroke_width = 1)
        curve_3.scale(1)
        curve_3.shift(DOWN)
        curve_3.set_color_by_gradient(RED_A, MAROON)

        self.play(Write(title), Create(curve_1), run_time = 5, rate_func = linear)
        self.wait(2)
        self.play(ReplacementTransform(curve_1, curve_2), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(curve_2, curve_3), run_time = 2)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(curve_3), run_time = 2)
        
