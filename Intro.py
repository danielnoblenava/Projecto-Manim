from manim import *
import math

config.media_width = "100%"

class Intro(Scene):
    def construct(self):
        say = Text('Demostración del Teorema de Pitágoras. Equipo 1 de Algebra\n:)', 
        slant=NORMAL,
        font_size=32,
        )


        self.play(Create(say),  run_time=4)
        self.wait(duration=2)
