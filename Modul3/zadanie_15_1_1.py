numbers = []

while len(numbers) < 10:
    number = int(input('Podaj liczbę dodatnią: '))
    if number > 0:
        numbers.append(number)

print(sum(numbers) / 10)
