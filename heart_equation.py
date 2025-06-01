from manim import *
import numpy as np

class Heart(Scene):
    def construct(self):
        #Title
        title = Text("", font_size=30)
        title.to_edge(UP)
        title.set_color_by_gradient(RED_A, RED_E)
        # Set up the axes with a better range for heart
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": True}
        ).next_to(title, DOWN).scale(0.75)

        # Tracker for k (starts at 1)
        k_tracker = ValueTracker(0)

        # Define the function safely
        def heart_function(x):
            x_23 = abs(x)**(2/3)  # Real-valued x^(2/3)
            return x_23 + 0.9 * np.sin(k_tracker.get_value() * x) * np.sqrt(3 - x**2)

        # Dynamic heart curve
        heart_curve = always_redraw(
            lambda: axes.plot(
                lambda x: heart_function(x),
                x_range=[-1.73, 1.73],
                color=RED,
            )
        )

        # k label
        
        equation = MathTex(
            r"y = \left| x \right|^{\frac{2}{3}} + 0.9 \sin(kx) \sqrt{3 - x^2}",
            font_size=28
        ).next_to(axes, DOWN)
        equation.set_color_by_gradient(RED_E, RED_A)

        k_label = always_redraw(
            lambda: MathTex(r"k = {:.2f}".format(k_tracker.get_value()), font_size=28, color=RED)
            .next_to(equation, DOWN)
            
        )
        # Add to scene
        self.play(Write(title), run_time=2)
        self.play(Create(axes), run_time=2)
        # Animate: k from 1 to 5
        self.play(Create(heart_curve),run_time=2)
        self.play(Write(equation), run_time=2)
        self.play(Write(k_label), run_time=2)
        self.play(k_tracker.animate.set_value(40), run_time=14, rate_func=linear)
        
        self.wait(1)
