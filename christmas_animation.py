from manim import *

class ChristmasAnimation(Scene):
    def construct(self):
        #Title configuration
        title = MarkupText(
            f'Christmas <span fgcolor="{RED}">Equation</span>', color=GREEN
        )

        #First equation confirguration
        equation_1 = MathTex(
            r"y = \frac{\ln \left(\frac{x}{m} - s a\right)}{r^2}",
            substrings_to_isolate=["y","="]
        )
        equation_1.set_color(RED)
        equation_1.set_color_by_tex("=", WHITE)
        equation_1.set_color_by_tex("y", GREEN)
        
        #Second equation configuration
        equation_2 = MathTex(
            r"y r^2 = \ln \left(\frac{x}{m} - s a\right)", 
            substrings_to_isolate=["y", "r^2","="]
        )
        equation_2.set_color(RED)
        equation_2.set_color_by_tex("=", WHITE)
        equation_2.set_color_by_tex("y", GREEN)
        equation_2.set_color_by_tex("r^2", GREEN)

        #Third equation configuration
        equation_3 = MathTex(
            r"e^{y r^2}=\frac{x}{m}-s a",
            substrings_to_isolate=["e^{y r^2}","="]
        )
        equation_3.set_color(RED)
        equation_3.set_color_by_tex("=", WHITE)
        equation_3.set_color_by_tex("e^{y r^2}", GREEN)

        #Fourth equation configuration
        equation_4 = MathTex(
            r"m e^{y r^2}=x-s a m",
            substrings_to_isolate=["m e^{y r^2}","="]
        )
        equation_4.set_color(RED)
        equation_4.set_color_by_tex("=", WHITE)
        equation_4.set_color_by_tex("m e^{y r^2}", GREEN)

        #Fifth equation configuration
        equation_5 = MathTex(
            r"m e^{r r y}=x-m a s",
            substrings_to_isolate=["m e^{r r y}","="]
            )
        equation_5.set_color(RED)
        equation_5.set_color_by_tex("=", WHITE)
        equation_5.set_color_by_tex("m e^{r r y}", GREEN)

        #Adding the title to the scene
        self.add(title)
        VGroup(title).to_edge(UP)
        self.play(
            Write(title),
            run_time=1.5
        )
        self.wait(0.75)
        self.play(Write(equation_1), run_time = 2)
        self.wait(1)
        self.play(TransformMatchingShapes(equation_1, equation_2))
        self.wait(1)
        self.play(TransformMatchingShapes(equation_2, equation_3))
        self.wait(1)
        self.play(TransformMatchingShapes(equation_3, equation_4))
        self.wait(1)
        self.play(TransformMatchingShapes(equation_4, equation_5))
        self.wait(4)