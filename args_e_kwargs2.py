from functools import reduce

def multi_args(*args):
    numbersss = [x for x in args if isinstance(x, (int, float))]
    return reduce(lambda x, y: x* y, numbersss)

print(multi_args(1, 3, 54, "eita bicho teste",  2))