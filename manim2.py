import random
import collections
from manim import *

class Upwork(Scene):
    def construct(self):
        # grid = NumberPlane(x_range=(-10, 10, 1), y_range=(-6.0, 6.0, 1))
        # self.play(FadeIn(grid))
        dimension = 4
        type1 = 4
        type2 = 5
        type3 = 4
        radius1 = 11 / ( 4 * dimension)

        circle1 = Circle(fill_color=GREY, fill_opacity=0.9, color=GREY)
        self.play(FadeIn(circle1))
        circle2 = circle1.copy().set(fill_color=RED, fill_opacity=0.5)
        circle3 = circle1.copy().set(fill_color=YELLOW, fill_opacity=0.5)
        circle4 = circle1.copy().set(fill_color=WHITE, fill_opacity=0.5)

        array0 = VGroup()
        array0 += circle1
        array0 += circle2
        array0 += circle3
        array0 += circle4

        self.remove(circle1)
        self.play(array0.animate.arrange(direction=RIGHT, buff=0.3))
        self.play(FadeOut(array0))


        array1 = VGroup()
        for i in range(dimension * dimension):
            array1.add(Circle(color=GREY, fill_opacity=0.9, radius = radius1))

        self.play(array1.animate.arrange_in_grid(rows=dimension, buff=radius1/2))

        rangegrey = range(dimension**2)

        index1 = random.sample(rangegrey, type1)
        index2 = random.sample([item for item in rangegrey if item not in index1],type2)
        index3 = random.sample([item for item in rangegrey if ( item not in index1) & (item not in index2)],type3)
        index4 = []
        for i in range(dimension**2):
            if str(array1[i].get_fill_color()) == "#888":
                index4.append(i)

        for i in index1:
            array1[i].set(fill_color=RED, fill_opacity=0.5)
            self.wait(1/len(index1))
        for i in index2:
            array1[i].set(fill_color=YELLOW, fill_opacity=0.5)
            self.wait(1/len(index2))
        for i in index3:
            array1[i].set(fill_color=WHITE, fill_opacity=0.5)
            self.wait(1/len(index3))
        big_index = index1 + index2 + index4 + index3
        for i in range(dimension ** 2):
            if i < big_index[i]:
                self.play(ReplacementTransform(array1[big_index[i], array1[i]]))
        self.wait(3)

if __name__ == '__main__':
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = Upwork()
        scene.render()