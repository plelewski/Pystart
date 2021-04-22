from datetime import datetime, timedelta


if __name__ == '__main__':

    flag = True
    while flag:
        try:
            date_start = datetime.strptime(input('Podaj datę rozpoczęcia pracy w formacie dd.mm.yy: '), '%d.%m.%Y')
            date_end = datetime.strptime(input('Podaj datę zakończenia pracy w formacie dd.mm.yy: '), '%d.%m.%Y')
            if (date_end - date_start).days < 1:
                print('... lepiej sprawdź te daty bo kasy nie będzie')
                continue

            md = int(input('Podaj stawkę za dzień: '))
            flag = False
        except ValueError:
            print('Podaj daty w prawidłowym formacie')
            continue

        non_working_days = 0
        print('Pracowałeś w dni:')
        for i in range(0, (date_end - date_start).days + 1):
            if (date_start + timedelta(days=i)).strftime("%w") in ('0', '6'):
                non_working_days += 1
                print((date_start + timedelta(days=i)).strftime('%d.%m.%Y') + ' *')
            else:
                print((date_start + timedelta(days=i)).strftime('%d.%m.%Y'))

        salary = ((date_end - date_start).days + 1 - non_working_days) * md + non_working_days * md * 2
        print(f'Zarobiłeś: {salary:3,d} zł')
