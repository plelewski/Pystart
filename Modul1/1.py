# liczba parzysta/nieparzysta
number = int(input('Podaj liczbę całkowitą '))
if number % 2 == 0:
    print(f'liczba {number} jest liczbą parzystą')
else:
    print(f'liczba {number} jest liczbą nieparzystą')

# < lub = lub >
number1 = int(input('Podaj liczbę całkowitą '))
number2 = int(input('Podaj liczbę całkowitą '))
if number1 < number2:
    print(f'liczba {number2} jest większa od liczby {number1}')
elif number1 > number2:
    print(f'liczba {number1} jest większa od liczby {number2}')
else:
    print('Podałeś dwie takie same liczby')

# zabawa z temperaturą
temperature = int(input('Podaj temperaturę na zewnątrz '))
if temperature <= 10:
    print('zostań w domu')
elif 10 < temperature < 20:
    print('weź kurtkę')
else:
    print('baw się dobrze')
