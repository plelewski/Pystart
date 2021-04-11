result = []
wynik = 1
x = ''

while x != 'koniec':
    x = input('Podaj cyfrę: ')
    if x != 'koniec' and int(x) % 2 == 0:
        wynik *= int(x)

print(wynik)
