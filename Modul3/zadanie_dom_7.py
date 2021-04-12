def find_divisor(num):
    return {x for x in range(2, num + 1) if num % x == 0}

def find_great_divisor(a, b):
    d1 = find_divisor(a)
    d2 = find_divisor(b)

    return max(d1 & d2)


print(find_great_divisor(30, 60))
