# podzielność przez 5 i 11
value = int(input('Podaj liczbę całkowitą '))

if value % 5 == 0 and value % 11 == 0:
    print('Cyfra podzielna przez 5 i 11')
elif value % 5 == 0:
    print('Cyfra podzielna przez 5')
elif value % 11 == 0:
    print('Cyfra podzielna przez 11')
else:
    print('Cyfra nie jest podzielna przez 5 i 11')
