my_dict = {
    'k1': 'klucz1',
    'k2': 'klucz2',
    'k3': 'klucz3'
}

try:
    print(my_dict['d'])
except KeyError:
    print('nie ma takiego klucza')
