def calculate_common_divisor(a, b, start_value=0):
    return [i for i in range(2, min(a,b) + 1) if a % i == 0 and b % i == 0 and i > start_value]

print(calculate_common_divisor(3, 6, 4))
