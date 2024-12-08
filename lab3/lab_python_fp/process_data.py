import cm_timer as c, field, gen_random, print_result, sort, unique
import json
import sys

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open('data_light.json', mode='r', encoding="utf_8_sig") as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result.print_result
def f1(arg):
    # print(arg[0])
    # print(list(arg[0].keys()))
    return field.field(arg, "job-name")


@print_result.print_result
def f2(arg):
    return list(filter(lambda x: 'программист' in x.lower(), arg))


@print_result.print_result
def f3(arg):
    return list(map(lambda x: x + 'с опытом Python ', arg))


@print_result.print_result
def f4(arg):
    myList = list(map(lambda x: x + f'зарплата {gen_random.gen_random(1, 100_000, 200_000)[0]} руб.', arg))
    return myList


if __name__ == '__main__':
    with c.cm_timer_1():
        f4(f3(f2(f1(data))))