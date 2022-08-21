"""
Script takes the following input variables: dimensions, type2, type3, type4
(type2 + type3 + type4 <= dimensions x dimensions).

Black background. Grey circle (solid grey outline, 10% transparent fill) appears in the center of frame.        +
Splits into 4 identical circles. Leftmost circle remains grey (type 1). Circle type 2 (to the right of 1)       +
fill becomes 50% red. Next circle (3) fill becomes 50% yellow. Next circle (4) fill becomes 50% white.          +

All four circles fade to black,                                                                             +

then an array of grey circles (type 1) is formed based on 'dimensions'.                                     +
If 'dimensions' = 3, a 3x3 array is generated. If 'dimensions' = 10, a 10x10 array is generated.            +
Sized to take up most of the screen. Total array size may be as large as 1000.                              +

Based on the variable type2, some circles randomly transform into circle 2 (50% red fill).                  +
If type2 = 2, then two circles randomly transform into circle type 2.                                       +

Based on the variable type3, some circles randomly transform into circle 3.                                 +

Based on the variable type4, some circles randomly transform into circle 4.                                 +
Circles that have transformed into one type cannot transform again.                                         +

Array transforms so that circle type 2 moves to the top of the array (counted left to right, top to bottom),
then circle type 3, then circle type 1. Circle type 4 moves to the bottom right of the array.

"""

# C:\Users\pxgeo2.geo\AppData\Local\Programs\Python\Python310\python.exe -m manim -qm -p c:\Users\pxgeo2.geo\PycharmProjects\AS_workshop_01\manim_1.py
# C:\Users\pxgeo2.geo\AppData\Local\Programs\Python\Python310\python.exe c:\Users\pxgeo2.geo\PycharmProjects\AS_workshop_01\manim_1.py 3 1 2 3

import random
import sys
from manim import *
import numpy as np

from manim.utils.color import Colors

dimensions = int(sys.argv[1])
type2 = int(sys.argv[2])
type3 = int(sys.argv[3])
type4 = int(sys.argv[4])

canvas_h = 8
canvas_w = 14

#dimensions = 20
#type2 = 40
#type3 = 50
#type4 = 60
from random import seed
from random import choice



# type3 = sys.argv[3]
# type4 = sys.argv[4]

class Upwork(Scene):
    def construct(self):
        """      # Black background. Grey circle (solid grey outline, 10% transparent fill) appears in the center of frame.
        grey_circle11 = Circle(color=GREY, fill_opacity=0.225, stroke_color=GREY, stroke_width=4, stroke_opacity=100)
        grey_circle12 = grey_circle11.copy()
        grey_circle13 = grey_circle11.copy()
        grey_circle14 = grey_circle11.copy()
        self.play(FadeIn(grey_circle11), FadeIn(grey_circle12), FadeIn(grey_circle13), FadeIn(grey_circle14))


        #  Splits into 4 identical circles.
        grey_circle21 = Circle(color=GREY, fill_opacity=0.9, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(3.5*LEFT)
        grey_circle22 = Circle(color=GREY, fill_opacity=0.9, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(1.25*LEFT)
        grey_circle23 = Circle(color=GREY, fill_opacity=0.9, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(1.25*RIGHT)
        grey_circle24 = Circle(color=GREY, fill_opacity=0.9, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(3.5*RIGHT)


        self.play(FadeTransform(grey_circle11, grey_circle21),
                  FadeTransform(grey_circle12, grey_circle22),
                  FadeTransform(grey_circle13, grey_circle23),
                  FadeTransform(grey_circle14, grey_circle24))


        # Leftmost circle remains grey (type 1). Circle type 2 (to the right of 1) fill becomes 50% red.
        # Next circle (3) fill becomes 50% yellow. Next circle (4) fill becomes 50% white.
        grey_circle31 = Circle(color=GREY, fill_opacity=0.9, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(3.5*LEFT)
        red_circle32 = Circle(color=RED, fill_opacity=0.5, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(1.25*LEFT)
        yellow_circle33 = Circle(color=YELLOW, fill_opacity=0.5, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(1.25*RIGHT)
        white_circle34 = Circle(color=WHITE, fill_opacity=0.7, stroke_color=GREY, stroke_width=4, stroke_opacity=100).shift(3.5*RIGHT)

        self.play(FadeTransform(grey_circle21, grey_circle31),
                  FadeTransform(grey_circle22, red_circle32),
                  FadeTransform(grey_circle23, yellow_circle33),
                  FadeTransform(grey_circle24, white_circle34))

        # All four circles fade to black
        self.play(FadeOut(grey_circle31),
                  FadeOut(red_circle32),
                  FadeOut(yellow_circle33),
                  FadeOut(white_circle34))

        # then an array of grey circles (type 1) is formed based on 'dimensions'."""
        unit = 2 * canvas_h / dimensions
        radius = unit * 0.2
        array = []
        stroke_width = radius*4
        print(stroke_width)
        for i in range(1, dimensions + 1):
            line = []
            for k in range(1, dimensions + 1):
                line.append(i)
            array.append(line)
        vgroup1 = VGroup()
        for h in range(1, dimensions+1):
            for w in range(1, dimensions+1):
                shift_up = (canvas_h - unit * (h - 0.5))/2
                shift_left = (canvas_h - unit * (w - 0.5))/2
                grey_circle4 = Circle(color=GREY, fill_opacity=0.9, stroke_color=GREY, stroke_width=stroke_width,
                                           stroke_opacity=100, radius=radius).shift(shift_up*UP, shift_left*LEFT)
                vgroup1.add(grey_circle4)
        self.play(FadeIn(vgroup1, run_time=(1)))
        vgroup2 = vgroup1.copy()
        listred = random.sample(range(1, dimensions*dimensions + 1), type2)
        print(listred)
        for p in listred:
            shift_up = vgroup2[p-1].get_y()
            shift_right = vgroup2[p-1].get_x()
            vgroup2[p-1] = Circle(color=RED, fill_opacity=0.5, stroke_color=GREY, stroke_width=stroke_width,
                                           stroke_opacity=100, radius=radius).shift(shift_up*UP, shift_right*RIGHT)

        listgrey = list(set(range(1, dimensions*dimensions + 1)) - set(listred))
        listyellow = random.sample(listgrey, type3)
        vgroup3 = vgroup2.copy()
        for q in listyellow:
            shift_up = vgroup3[q-1].get_y()
            shift_right = vgroup3[q-1].get_x()
            vgroup3[q-1] = Circle(color=YELLOW, fill_opacity=0.5, stroke_color=GREY, stroke_width=stroke_width,
                                           stroke_opacity=100, radius=radius).shift(shift_up*UP, shift_right*RIGHT)

        listgrey = list(set(listgrey) - set(listyellow))
        listwhite = random.sample(listgrey, type4)
        vgroup4 = vgroup3.copy()
        for r in listwhite:
            shift_up = vgroup4[r-1].get_y()
            shift_right = vgroup4[r-1].get_x()
            vgroup4[r-1] = Circle(color=WHITE, fill_opacity=0.7, stroke_color=GREY, stroke_width=stroke_width,
                                           stroke_opacity=100, radius=radius).shift(shift_up*UP, shift_right*RIGHT)
            print(vgroup4[r-1].get_color())

        listgrey = list(set(listgrey) - set(listwhite))

        print(listgrey)
        for s in listred:
            self.play(FadeOut(vgroup1[s - 1], run_time=(1 / type2)), FadeIn(vgroup2[s - 1], run_time=(1/type2)))
            self.remove(vgroup1[s - 1])
        for t in listyellow:
            self.play(FadeOut(vgroup2[t - 1], run_time=(1 / type3)), FadeIn(vgroup3[t - 1], run_time=(1 / type3)))
            self.remove(vgroup2[t - 1])
        for u in listwhite:
            self.play(FadeOut(vgroup3[u - 1], run_time=(1 / type4)), FadeIn(vgroup4[u - 1], run_time=(1 / type4)))
            self.remove(vgroup3[u - 1])
        self.wait(2)


if __name__ == '__main__':
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = Upwork()
        scene.render()