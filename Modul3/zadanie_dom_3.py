def factorial(number: int) -> int:
    i = 1
    result = 1
    while i <= number:
        result *= i
        i += 1
    return result

print(factorial(3))
print(factorial(4))
print(factorial(5))
