from functools import reduce

def soma_argniana(*args):
    return reduce(lambda x, y: x + y, args)

print(soma_argniana(1, 2, 3, 4))