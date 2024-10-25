from lab_python_oop.Figure import Figure
from math import pi
from lab_python_oop.Color import Color


class Round(Figure):
    def __init__(self, r: float, name: str, color : Color):
        self.r = r
        self.name = name
        self.color = color

    def findS(self) -> float:
        return self.r * self.r * pi

    def __repr__(self):
        return f'{self.name} with S = {self.findS()} colored in {self.color}'

