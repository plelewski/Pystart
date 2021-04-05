pesel = input('Podaj PESEL do weryfikacji: ')
pesel_list = []

for i in pesel:
    pesel_list.append(i)

validation_sum = (int(pesel_list[0]) * 1 + int(pesel_list[1]) * 3 + int(pesel_list[2]) * 7 + int(pesel_list[3]) * 9
                  + int(pesel_list[4]) * 1 + int(pesel_list[5]) * 3 + int(pesel_list[6]) * 7 + int(pesel_list[7]) * 9
                  + int(pesel_list[8]) * 1 + int(pesel_list[9]) * 3 + int(pesel_list[10]) * 1)

if str(validation_sum)[-1] == '0':
    print('PESEL poprawny')
else:
    print('PESEL nie jest poprawny')

# lepszy sposób
# check = '13791379131' # mnożniki dla sprawdzenia PESELu
# control = 0
# for index, _ in enumerate(pesel):
#     control += int(pesel[index]) * int(check[index])
#
# if str(control)[-1] == '0':
#     print('PESEL poprawny')
# else:
#     print('PESEL nie jest poprawny')
