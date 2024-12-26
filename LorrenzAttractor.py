from pdb import run
from pickle import FRAME
from turtle import width
import numpy as np
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from manim import *
from manim_physics import *


def lorenz_system(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

def ode_solution_points(function, state0, time, dt=0.01):
    solution = solve_ivp(
        function,
        t_span=(0, time),
        y0 = state0,
        t_eval=np.arange(0, time, dt)
    )
    return solution.y.T

class LorrenzAttractor(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=(-50, 50, 5),
            y_range=(-50, 50, 5),
            z_range=(0, 50, 5),
            x_length=10,
            y_length=10,
            z_length=10,
        )
        axes.set_width(config.frame_width)
        axes.center()
        self.add(axes)

        # Display the Lorrenz Solutions
        epsilon = 0.001
        evolution_time = 30
        states = [
            [10, 10, 10+n*epsilon]
             for n in range(20)

        ]
        colors = color_gradient([BLUE_A, BLUE_E], len(states))
        curves = VGroup()
        for state, color in zip(states, colors):
            points = ode_solution_points(lorenz_system, state, evolution_time)
            curve = VMobject().set_points_smoothly([axes.c2p(x, y, z) for x, y, z in points])
            curve.set_stroke(color,width=1.5)
            curves.add(curve)
        
        dots = Group(*[Dot(color=color) for color in colors])
        globals().update(locals())
        def update_dots(dots):
            for dot, curve in zip(dots, curves):
                dot.move_to(curve.get_end())
        
        dots.add_updater(update_dots)
        self.add(dots)
        self.set_camera_orientation(phi=75 * DEGREES, theta=150 * DEGREES, zoom=0.35)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(
            *(
                Create(curve, rate_func=linear)
                for curve in curves
            ),
            run_time=evolution_time
        )
        self.wait(1)
        
