from datetime import datetime
from dateutil.relativedelta import relativedelta


class InvalidDateOfEmployment(Exception):
    pass


class BaseEmployee:
    def __init__(self, f_name: str, s_name: str, hire_date: datetime):
        self.hire_date = hire_date
        self.s_name = s_name
        self.f_name = f_name

    @property
    def employment_time(self):
        now = datetime.now()
        return (now - self.hire_date).days

    def __lt__(self, other):
        return self.employment_time < other.employment_time

    def __str__(self):
        return f'{self.f_name} {self.s_name} rozpoczął pracę: {self.hire_date}'


def main():
    now = datetime.now()
    num_of_obj = 0
    list_of_obj = []

    while num_of_obj < 3:
        try:
            fn = input('Podaj imię: ')
            ln = input('Podaj nazwisko: ')
            hd = datetime.strptime(input('Podaj datę rozpoczęcia pracy w formacie yyyy.mm.dd: '), '%Y.%d.%m')
            if hd > now or relativedelta(now, hd).years > 50:
                raise InvalidDateOfEmployment
            be = BaseEmployee(fn, ln, hd)
            list_of_obj.append(be)
            num_of_obj += 1

        except InvalidDateOfEmployment:
            print('Nieprawidłowa data')
            print()

    for i in sorted(list_of_obj):
        print(i)


if __name__ == '__main__':
    main()
