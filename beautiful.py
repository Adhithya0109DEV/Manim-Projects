from manim import *

class Equation(Scene):
    def construct(self):
        # Create the text
        text = Tex(r"Which is more beautiful? ")
        text.to_edge(UP)
        text.set_color_by_gradient(TEAL_A, TEAL_D)

        # Euler's equation
        euler_equation = MathTex(r"e^{i \pi} + 1 = 0")
        euler_equation.next_to(text, DOWN, buff=1)
        euler_equation.set_color_by_gradient(GREEN, BLUE)
        
        # Text 2
        text_2 = Tex(r"or")
        text_2.next_to(euler_equation, DOWN, buff=1)

        # Square root equation
        square_root_equation = MathTex(r"\sqrt{2^{6^{2^{1^{4^4}}}}} = 262144")
        square_root_equation.next_to(euler_equation, DOWN, buff=2)
        square_root_equation.set_color_by_gradient(BLUE, GREEN)

        # Play the animations
        self.play(Write(text), run_time = 3)
        self.wait(1)
        self.play(Transform(text.copy(), euler_equation), run_time = 1.5)
        self.wait(1)
        self.play(Transform(euler_equation, text_2))
        self.wait(1)
        self.play(Transform(text_2, square_root_equation), run_time = 1.5)
        self.wait(3)