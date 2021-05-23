my_list = [a for a in range(10)]

try:
    idx = int(input('Podaj index o 1 do 10: '))
    print(my_list[idx - 1])
except IndexError:
    print('Podałeś wartość spoza zakresu')
except (TypeError, ValueError) as error:
    print('nie rozumiem')
    print(error)
