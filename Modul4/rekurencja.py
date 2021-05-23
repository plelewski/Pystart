def wSzybkie(lista, poczatek, koniec, cel):
    if poczatek > koniec:
        return False

    x = (poczatek + koniec) // 2

    if lista[x] == cel:
        print("mam")
        return x
    if lista[x] < cel:
        return wSzybkie(lista, x + 1, koniec, cel)
    if lista[x] > cel:
        return wSzybkie(lista, poczatek, x - 1, cel)


lista = [1, 3, 7, 44, 55, 66, 78, 89, 123, 134]
cel = 7
print(wSzybkie(lista, 0, len(lista) - 1, cel))
