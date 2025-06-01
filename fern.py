from manim import *
import numpy as np
import random

class Fern(Scene):
    def construct(self):
        # Title
        title = Text("From Chaos", font_size=36)
        title.to_edge(UP, buff=0.5)
        title.set_color_by_gradient(TEAL_A, TEAL_E)
        self.play(Write(title), run_time = 2)
        self.wait(1)
        
        title_2 = Text("comes Order", font_size=36)
        title_2.next_to(title, DOWN, buff=0.5)
        title_2.set_color_by_gradient(TEAL_E, TEAL_A)
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 10, 1],
            x_length=6,
            y_length=8,
            axis_config={"color": BLUE_E, "stroke_width": 2}
        ).shift(DOWN * 1.5)
        
        # Barnsley fern transformation functions
        def f1(x, y):
            return 0, 0.16 * y
        
        def f2(x, y):
            return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        
        def f3(x, y):
            return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        
        def f4(x, y):
            return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
        
        # Probabilities for each transformation
        transformations = [
            (f1, 0.01),   # 1% - stem
            (f2, 0.85),   # 85% - main body
            (f3, 0.07),   # 7% - left frond
            (f4, 0.07)    # 7% - right frond
        ]
        
        # Generate all points first
        x, y = 0, 0
        all_points = []
        
        # Generate points without animation first
        num_points = 15000
        for i in range(num_points):
            # Choose transformation based on probability
            rand = random.random()
            cumulative_prob = 0
            
            for transform, prob in transformations:
                cumulative_prob += prob
                if rand <= cumulative_prob:
                    x, y = transform(x, y)
                    break
            
            # Convert to screen coordinates and store with y-coordinate for sorting
            screen_point = axes.coords_to_point(x, y)
            all_points.append((screen_point, y))  # Store point with original y-coordinate
        
        # Sort points by y-coordinate (bottom to top)
        all_points.sort(key=lambda point: point[1])
        
        # Animate points growing from bottom to top
        dots = VGroup()
        batch_size = 15  # Smaller batches for smoother growth effect
        
        for batch in range(0, len(all_points), batch_size):
            batch_points = []
            
            for i in range(min(batch_size, len(all_points) - batch)):
                point_coord = all_points[batch + i][0]
                batch_points.append(point_coord)
            
            # Create dots for this batch
            if batch_points:
                # Use gradient colors - darker green at bottom, brighter at top
                height_ratio = batch / len(all_points)
                color = interpolate_color(TEAL_A, TEAL_E, height_ratio)
                
                batch_dots = VGroup(*[
                    Dot(point, radius=0.01, color=color).set_opacity(0.8)
                    for point in batch_points
                ])
                dots.add(batch_dots)
                
                # Animate the appearance with growing effect
                self.play(FadeIn(batch_dots), run_time=0.02)
        self.play(Transform(title.copy(), title_2), run_time = 2)
        self.wait(3)