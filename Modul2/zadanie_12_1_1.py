dictionary = {'oko': 'eye', 'myszka': 'mouse', 'telefon': 'phone', 'palec': 'finger', 'noga': 'leg'}

while True:
    word = input('Podaj słowo do przetłumaczenia (quit => wyjście z programu: ')
    if word == 'quit':
        break
    elif word in dictionary.keys():
        print(dictionary[word])
    else:
        for k,v in dictionary.items():
            if v == word:
                print(k)
