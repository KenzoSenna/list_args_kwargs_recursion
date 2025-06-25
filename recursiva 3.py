def somar_algarismos_nm(n):
    if n < 10:
        return n
    return somar_algarismos_nm(n // 10) + n % 10

print(somar_algarismos_nm(102))