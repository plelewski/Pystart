list_of_fruits = []

try:
    while len(list_of_fruits) < 10:
        fruit = input('Podaj owoc, którego wcześniej nie podałeś: ')
        if fruit in list_of_fruits:
            raise Exception('Już podawałeś cwaniaku')
        list_of_fruits.append(fruit)

except Exception as e:
    print('To koniec', e)

print(list_of_fruits)
