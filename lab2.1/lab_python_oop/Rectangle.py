from lab_python_oop.Figure import Figure
from lab_python_oop.Color import Color


class Rectangle(Figure):
    def __init__(self, a: float, b: float, name: str, color: Color):
        self.a = a
        self.b = b
        self.color = color
        self.name = name

    def findS(self) -> float:
        return self.a * self.b

    def __repr__(self):
        return f'{self.name} with S = {self.findS()} colored in {self.color}'

