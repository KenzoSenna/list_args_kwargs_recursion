import time

def contagem(n):
    if n == 0:
        time.sleep(3)
        print("Ué, por quê não explodi-")
        time.sleep(1)
        return print("BooOOOOOOOOOOOmmmmmmmmmm!")
    time.sleep(1)
    print(f"Contagem regressiva: {n}")
    return contagem(n - 1)
contagem(10)