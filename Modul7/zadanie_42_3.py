try:
    text = input('Podaj tekst do odwrócenia: ')
    if text == 0:
        raise Exception('Pusto, pusto')
    print(text[::-1])
except Exception as e:
    print(e)
