import sys
from math import sqrt


class Equation:
    def __init__(self):
        self.D = 0
        self.args = []

    def set_coefs(self):
        self.args = sys.argv[1:]
        if not self.args:
            self.args = input("Input A: "), input("Input B: "), input("Input C: ")

        while True:
            if all(i for i in self.args):
                try:
                    for i in range(len(self.args)):
                        self.args = list(map(float, self.args))
                    break
                except Exception as e:
                    pass
            self.args = input("Input A: "), input("Input B: "), input("Input C: ")

    def find_D(self):
        A, B, C = self.args
        self.D = B * B - 4 * A * C

    def find_ans(self):
        A, B, C = self.args
        if self.D > 0:
            x1, x2 = (-B + sqrt(self.D)) / (2 * A), (-B - sqrt(self.D)) / (2 * A)
            print("Корни:", x1, ',', x2)
        elif self.D == 0:
            x = (-B + sqrt(self.D)) / (2 * A)
            print("Корень:", x)
        else:
            print("Корней нет")

    def calculate(self):
        self.set_coefs()
        self.find_D()
        self.find_ans()


def main():
    eq = Equation()
    eq.calculate()


if __name__ == '__main__':
    sys.exit(main())
