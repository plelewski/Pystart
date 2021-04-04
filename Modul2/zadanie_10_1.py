# 10.1.1
suma = 0
lista_liczb = list(range(101))
for liczba in lista_liczb:
    if liczba % 4 == 0 and liczba % 5 == 0:
        suma += liczba
print(suma)

# coś podobnego
num_div_by_4 = 0
num_div_by_5 = 0
for i in range(1, 21):
    if i % 4 == 0:
        num_div_by_4 += 1
    if i % 5 == 0:
        num_div_by_5 += 1
print('Liczb podzielnych przez 4', num_div_by_4)
print('Liczb podzielnych przez 5', num_div_by_5)

# 10.1.2
list_of_names = ["Ada", "Bartek", "Konstanty", "Piotr", "Marek"]
sorted_list_of_names_by_len = sorted(list_of_names, key=len)
print(sorted_list_of_names_by_len[0], sorted_list_of_names_by_len[-1])

# inny sposób
shortest_name = None
for name in list_of_names:
    if shortest_name is None or len(shortest_name) > len(name):
        shortest_name = name
print(f"Najkrótsze imię to: {shortest_name}")

# 10.1.3
number = int(input("Podaj liczbę całkowitą: "))
licznik = 0
for i in range(2, number):
    if number % i == 0:
        licznik += 1

if licznik == 0 or number == 2:
    print(f"{number} jest liczbą pierwszą")
else:
    print(f"{number} nie jest liczbą pierwszą")

# lepszy sposób
is_prime = True
number_sqrt = int(number ** 0.5) # de facto pierwiastek drugiego stopnia
for x in range(2, number_sqrt + 1):
    if number % x == 0:
        is_prime = False
        print(f"{x} jest dzielnikiem {number}")
        break

if is_prime:
    print('Liczba jest pierwszą')
else:
    print('Liczba nie jest pierwszą')

# 10.1.4
value = int(input('Podaj liczbę: '))
for j in range(value):
    for i in range(1, value + 1 - j):
        print(i, end=' ')
    print('')
