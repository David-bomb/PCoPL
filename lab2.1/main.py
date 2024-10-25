from lab_python_oop.Round import Round
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Square import Square
from lab_python_oop.Color import Color
import numpy as np


color1 = Color(0, 0, 255)
color2 = Color(0, 255, 0)
color3 = Color(255, 0, 0)

rect = Rectangle(10, 15, 'RECT', color1)
round = Round(12, 'RND', color2)
square = Square(20, "SQR", color3)

print(rect)
print(round)
print(square)


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nArr = np.array(arr)
print(nArr.ndim)