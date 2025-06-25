# R4. Potˆencia Recursiva
# Implemente uma fun¸c˜ao recursiva que calcula base^expoente, onde ambos s˜ao inteiros positivos.

def base_expoente( b, e, n = None):
    if n is None:
        n = b
    if e == 1:
        return b
    return base_expoente(b * n, e - 1 , n)

print(base_expoente(2, 10))