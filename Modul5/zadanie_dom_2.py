from datetime import datetime


if __name__ == '__main__':
    list_of_prods = set()
    filename = datetime.now().strftime('%d%m%Y') + '.txt'

    while True:
        answer = input('Podaj nazwę produktu: ').lower()
        if answer.lower() == 'koniec':
            break
        list_of_prods.add(answer)

    with open(filename, 'w') as file:
        file.writelines("\n".join(list_of_prods))
