value1 = int(input('Podaj pierwszą cyfrę (mniejsza): '))
value2 = int(input('Podaj drugą cyfrę (większa): '))
licznik = 0

for j in range(value1, value2 + 1):
    if j > 2:
        for i in range(2, j):
            if j % i == 0:
                licznik += 1

    if licznik == 0 or j == 2:
        print(f"{j} jest liczbą pierwszą")
    else:
        print(f"{j} nie jest liczbą pierwszą")
    licznik = 0

print(int(5 ** 0.5) + 1)
