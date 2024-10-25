from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Color import Color


class Square(Rectangle):
    def __init__(self, x: float, name: str, color : Color):
        super().__init__(x, x, name, color)
        self.x = x
        self.name = name
        self.color = color

    def findS(self) -> float:
        return super().findS()

    def __repr__(self):
        return f'{self.name} with S = {self.findS()} colored in {self.color}'