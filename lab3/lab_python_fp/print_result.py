# Здесь должна быть реализация декоратора
#
from traceback import walk_stack


def my_print(original_result):
    if type(original_result) == list:
        for i in range(len(original_result)):
            print(original_result[i])
    elif type(original_result) == dict:
        for key in original_result.keys():
            print(key, '=', original_result[key], end='\n')
    else:
        print(original_result)

def print_result(func):
    def wrap(*temp):
        print(func.__name__)
        #TODO ОШИБКА В ТИПЕ func/temp
        my_print(func(*temp))
        # return func
        return func(*temp)
    return wrap


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()