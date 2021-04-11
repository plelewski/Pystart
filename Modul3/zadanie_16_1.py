salary = 2000
add_salary = 0

period = int(input('Jaki jest Twój staż pracy (w latach): '))
number_of_worked_h = int(input('Ile przepracowałeś w poprzednim miesiącu godzin: '))
number_of_sold_p = int(input('Ile sztuk towaru sprzedałeś: '))

if number_of_sold_p > 30:
    add_salary = salary * 0.25

add_salary += salary * 0.1 if period >= 2 else salary * 0.02
add_salary += salary * 0.08 if number_of_worked_h >= 160 and period > 1 else salary * 0.02

print('Twoje wynagrodzenie to: ', salary + add_salary)
