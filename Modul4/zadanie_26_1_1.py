from math import sqrt
# inny sposób bez funkcji
# values = [16, 36, 25, 49]
#
# print(list(filter(lambda q: q % 2 == 0, map(lambda n: sqrt(n), values))))

def map_and_filter(values: list) -> list:
    return list(filter(lambda q: q % 2 == 0, map(lambda n: sqrt(n), values)))


def test_map_and_filter():
    a = [16, 36, 25, 49]
    assert map_and_filter(a) == [4, 6]
