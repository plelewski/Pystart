from datetime import date


def show_next_birth_date(y, m, d):
    print(f'kolejne balanga z okazji urodzin: {(date(y, m, d)).strftime("%a %d.%m.%Y")}')
    print(f'pozostało do niej: {(date(y, m, d) - date.today()).days} dni')

def give_the_next_birth_date(mon:int, day:int):
    today = date.today()
    if today > date(today.year, month=mon, day=day):
        show_next_birth_date(today.year + 1, mon, day)
    elif today < date(today.year, month=mon, day=day):
        show_next_birth_date(today.year, mon, day)
    else:
        print('to dzisiaj ćwoku')


if __name__ == '__main__':
    give_the_next_birth_date(2, 23)
