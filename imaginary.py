from manim import *

class Imaginary(Scene):
    def construct(self):
        # Text Configuration
        text = Text("Sometimes we imagine stuff which can never be real.", font_size = 20)
        text_2 = Text("But if we imagine it a lot of times, maybe an imaginary number of times,", font_size = 20)
        text_3 = Text("Then it would soon be real...", font_size = 20)
        text.set_color_by_gradient(TEAL, WHITE)
        text_2.set_color_by_gradient(TEAL, WHITE)
        text_3.set_color_by_gradient(TEAL, WHITE)
        
        # Equation Configuration
        equation_1 = MathTex(r"i")
        equation_2 = MathTex(r"i^i")
        equation_3 = MathTex(r"\left(e^{i \frac{\pi}{2}}\right)^i")
        equation_4 = MathTex(r"e^{\frac{-\pi}{2}}")
        equation_5 = MathTex(r"e^{\frac{-\pi}{2}} = 0.20787...")

        # Text Position
        text.to_edge(UP)
        text_2.next_to(text, DOWN, buff=0.5)
        text_3.next_to(text_2, DOWN, buff=0.5)
        
        # create the animations
        self.play(Write(text.copy()), run_time = 3)
        self.wait(1)
        self.play(Write(equation_1, run_time = 1))
        self.wait(1)
        self.play(Write(text_2.copy()), TransformMatchingShapes(equation_1, equation_2), run_time = 3)
        self.wait(1)
        self.play(Write(text_3),
                  TransformMatchingShapes(equation_2, equation_3),
                  run_time = 3)
        self.play(TransformMatchingShapes(equation_3, equation_4), run_time = 3)
        self.play(TransformMatchingShapes(equation_4, equation_5), run_time = 3)
        self.wait(3)
        