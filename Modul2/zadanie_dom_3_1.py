import string


list_az = list(string.ascii_lowercase + string.ascii_uppercase)
list_dc = list_az.copy()
for _ in range(3):
    list_dc.append(list_dc.pop(0))

return_list = []

def encrypt_decrypt(str_to_change ,source_list, dest_list):
    for letter in str_to_change:
        if letter != ' ':
            return_list.append(dest_list[source_list.index(letter)])
        else:
            return_list.append(letter)


str_to_encr_decr = input('Podaj tekst do zmiany: ')
print('Wybierz:')
print('\t1 - szyfrowanie')
print('\t2 - deszyfrowanie')
selection = int(input('Twój wybór: '))

if selection == 1:
    encrypt_decrypt(str_to_encr_decr ,list_az, list_dc)
else:
    encrypt_decrypt(str_to_encr_decr, list_dc, list_az)

for pet in range(len(return_list)):
    print(return_list[pet], end='')
print()
