import math


def masodfoku(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        raise ValueError('Nincs megoldása')
    return [(-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a)]

try:
    masodfoku(100, 1, 1)
except ValueError as hiba:
    print(hiba)
        