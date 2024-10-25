import sys
from math import sqrt


def generate_coef():  # Функция возвращает вводимые коэффициенты, используется глобальный объект "sys"
    args = sys.argv[1:]

    if not args:
        A, B, C = input("Input A: "), input("Input B: "), input("Input C: ")
        args = [A, B, C]

    while True:
        if all(i for i in args):
            #if all([any([i.count('.') < 2 and i.replace('.', '').isdigit(), all([i.count('.') < 2, i[1] != '.', i.replace('.', '')[1:].isdigit(), i[0] == '-'])]) for i in args]): # супер-условие: число должно быть с минусом или без
            try:
                for i in range(len(args)):
                    args = list(map(float, args))
                break
            except Exception as e:
                pass
        A, B, C = input("Input A: "), input("Input B: "), input("Input C: ")
        args = [A, B, C]
    return args


def find_decision(args):  # Функция подсчета корней.
    A, B, C = args
    D = B * B - 4 * A * C
    if D > 0:
        x1, x2 = (-B + sqrt(D)) / (2 * A), (-B - sqrt(D)) / (2 * A)
        print("Корни:", x1, ',', x2)
    elif D == 0:
        x = (-B + sqrt(D)) / (2 * A)
        print("Корень:", x)
    else:
        print("Корней нет")


def main():
    find_decision(generate_coef())


if __name__ == '__main__':
    sys.exit(main())
