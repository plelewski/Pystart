from math import sqrt

def calc_length(a:tuple, b:tuple) -> float:
    return round(sqrt((b[1] - a[1]) ** 2 + (b[0] - a[0]) ** 2), 2)


print(calc_length((0, 0),(4, 2)))
