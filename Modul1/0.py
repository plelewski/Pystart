weight = float(input('Podaj wagę '))
height = float(input('Podaj wzrost '))
bmi = weight / ((height / 100) ** 2)
print(f'Twoje BMI wynosi {bmi:.2f}')    # zaokrąglenie float do 2 miejsc po przecinku

netto = float(input('Podaj netto a policzę brutto '))
brutto = netto * 1.23
print(f'Brutto = {brutto:.2f}')

side_a = float(input('Podaj bok 1 trapezu '))
side_b = float(input('Podaj drugi bok trapezu '))
height_t = float(input('Podaj wysokość trapezu '))
pole_t = ((side_a + side_b) * height_t) / 2
print(f'Pole trapezu wynosi {pole_t}')
