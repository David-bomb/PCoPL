import random as r


def gen_random(num_count, begin, end):
    return [r.randint(begin, end) for _ in range(num_count)]

# print(gen_random(5, 1, 3))