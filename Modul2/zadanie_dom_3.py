str_after_encdecr = []
value_to_change = 0
add_par = 0

str_to_encr_decr = input('Podaj tekst do zmiany: ')
print('Wybierz:')
print('\t1 - szyfrowanie')
print('\t2 - deszyfrowanie')
selection = int(input('Twój wybór: '))

if selection == 1:
    value_to_change += 3
    add_par += 6
else:
    value_to_change -= 3
    add_par -= 6

for i in str_to_encr_decr:
    if ord(i) == 32:
        v = 32
    else:
        v = ord(i) + value_to_change
        if v > 122:
            v -= 58
        elif v < 65:
            v += 58
        if 90 < v < 97:
            v += add_par

    str_after_encdecr.append(chr(v))

for pet in range(len(str_after_encdecr)):
    print(str_after_encdecr[pet], end='')
print()
