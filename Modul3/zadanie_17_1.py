pesel = input('Podaj PESEL do weryfikacji: ')
check = '13791379131'  # mnożniki dla sprawdzenia PESELu
control = 0

for i,j in zip(pesel, check):
    control += int(i) * int(j)

if str(control)[-1] == '0':
    print('PESEL poprawny')
else:
    print('PESEL nie jest poprawny')
