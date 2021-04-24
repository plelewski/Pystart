from json import load, dump


try:
    with open('books.json') as data:
        library = load(data)
except FileNotFoundError:
    print('brak pliku')
    quit()

while True:
    answer = input('Dostępne polecenia: [w]ypisz / [d]odaj / [k]oniec ')

    if answer.lower() == 'k':
        break
    elif answer.lower() == 'w':
        print('Dostępne książki:')
        for b in library['book']:
            print(f"Imię i nazwisko autora: {b['author']}")
            print(f"Tytuł: {b['title']}")
            print(f"Ilość stron: {b['pages']}")
    elif answer.lower() == 'd':
        d_name = input('Podaj imię i nazwisko autora: ')
        d_title = input('Podaj tytuł ksiązki: ')
        d_pages = input('Podaj ilość stron: ')

        with open('books.json', 'w') as f:
            library['book'].append(
                {
                    "id": len(library['book']) + 1,
                    "author": d_name,
                    "title": d_title,
                    "pages": d_pages
                }
            )

            dump(library, f, indent=2)
    else:
        print('Nieprawidłowy wybór')
