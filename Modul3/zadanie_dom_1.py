def sum_two_lists(a: list, b: list) -> list:
    return [x+y for x, y in zip(a, b)]

print(sum_two_lists([2, 4, 6], [8, 6, 4]))
