value = int(input('Podaj pierwszą liczbę: '))

setvalue1 = set()
setvalue2 = set()

for i in range(1, value):
    if i % 3 == 0:
        setvalue1.add(i)
    if i % 5 == 0:
        setvalue2.add(i)

print('liczby podzielne przez 3', setvalue1)
print('liczby podzielne przez 5', setvalue2)
print('Liczby podzielne przez 3 i 5', setvalue1 & setvalue2)
