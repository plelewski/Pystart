imie = input('Podaj swoje imię: ')
if imie[-1].lower() == 'a':
    print('Witam Panią')
else:
    print('Witam Pana')

if input("Jak masz na imię? ").endswith('a'):
    print('Witam Panią')