def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    odds = [number for number in numbers if number % 2 != 0]
    even = [number for number in numbers if number % 2 == 0]

    total = 0 if not count_odd else len(odds)
    total += 0 if not count_even else len(even)

    return total


print(count_numbers([1, 2, 3, 4, 5, 6]))
print(count_numbers([1, 2, 3, 4, 5, 6], count_odd=False))
print(count_numbers([1, 2, 3, 4, 5, 6], count_even=False))
print(count_numbers([1, 3, 5, 7, 9, 10], count_even=False))
